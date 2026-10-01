#!/usr/bin/env python3
"""Identify families — RelatedPerson network primary, name/address secondary.

Subset:  families
Type:    Derived + Curated
Task:    4.6

Contract
--------
Two signals of very different strength, kept separate rather than merged into
one confidence score.

PRIMARY — the RelatedPerson network
------------------------------------
A RelatedPerson carries an explicit `patient` reference plus a `relationship`
code (WIFE, MTH, ...) — a stated family link, not an inference.

The data set's RelatedPerson network is richer than a flat list: the same
real person is often described by several RelatedPerson records attached to
different Patients (verified: 24 identifiers shared across multiple
RelatedPerson records), AND that person is often independently a Patient in
their own right (verified: Patient/lowe-valerie shares its IHI with the
RelatedPerson records describing "Valerie" in Cedric's and Alix's charts).
Treating each RelatedPerson record as an isolated edge would miss exactly the
multi-hop families this signal is best at finding — Kelvin and Sandy
Ballantyne are only connected through Flavia, who has no Patient record of
her own but appears as three RelatedPerson entries sharing one identifier.

So: RelatedPerson records are first grouped by shared identifier (IHI or
Medicare number) into "identities" — a group with no shared identifier at all
(4 of 40 records) is its own singleton identity. Each identity is resolved to
an existing Patient when one shares that identifier; otherwise the identity
stands alone (Flavia's case). A graph edge joins each identity to the Patient
whose chart it appears in. Connected components of size >= 2 are the primary
family candidates.

One relationship code is explicitly excluded: FRND, whose FHIR display text
is "unrelated friend" — the data set itself says these are not family.

SECONDARY — matching surname and/or matching address
------------------------------------------------------
Widens the net beyond the RelatedPerson graph. Neither signal is conclusive
alone — same surname is weak (common names), same address is weak (a
share-house, a residential aged care facility), and genuine family members
may live apart. A measured example of the risk: 9 Patient files share both
surname "ITALIA" and one address, but they are 9 test-data variants of ONE
synthetic patient (missing/suppressed-data test cases), not a family of nine.
Emitting this as a plausible candidate — for a human to reject — is exactly
the intended behaviour.

Secondary groups whose members are already fully covered by a primary
component are dropped as redundant; partial overlaps are kept, since they may
reveal a family member the RelatedPerson graph missed.

Families are reusable
----------------------
reserved: false. A family grouping is a starting point for building a new
consumer journey involving related patients.

Output
------
members            previously confirmed families (either signal)
needs_confirmation RelatedPerson-derived groups and name/address groups not
                   yet decided, each tagged with its signal
evidence           per family: the RelatedPerson edges and relationship codes
                   (primary), or which of surname/address matched (secondary)
"""

from __future__ import annotations

from collections import defaultdict

import lib

# HL7 v3 RoleCode. Display text in this data set: "unrelated friend" — the
# data itself states this is not a family relationship.
EXCLUDED_RELATIONSHIP_CODES = frozenset({"FRND"})

MEDICARE_SYSTEM = "http://ns.electronichealth.net.au/id/medicare-number"


def medicare_card(resource: dict) -> str | None:
    """Return the 10-digit Medicare CARD number, dropping the IRN.

    An Australian Medicare number is 10 card digits plus a per-person
    Individual Reference Number as the 11th, so everyone on one card shares the
    first 10 and differs only in the last. That makes a shared card the
    administrative statement of a family unit.

    Only 11-digit values are treated as card+IRN. One value in this data set is
    10 digits; truncating it would invent a 9-digit card that matches nothing,
    so it is skipped and reported instead.
    """
    ids = resource.get("identifier")
    ids = [ids] if isinstance(ids, dict) else (ids or [])
    for i in ids:
        if not isinstance(i, dict) or i.get("system") != MEDICARE_SYSTEM:
            continue
        value = str(i.get("value") or "")
        if len(value) == 11 and value.isdigit():
            return value[:10]
    return None


def malformed_medicare(resource: dict) -> str | None:
    """A Medicare value present but not 11 digits — reported, never parsed."""
    ids = resource.get("identifier")
    ids = [ids] if isinstance(ids, dict) else (ids or [])
    for i in ids:
        if isinstance(i, dict) and i.get("system") == MEDICARE_SYSTEM:
            value = str(i.get("value") or "")
            if len(value) != 11 or not value.isdigit():
                return value
    return None


class UnionFind:
    def __init__(self):
        self.parent: dict[str, str] = {}

    def find(self, x: str) -> str:
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: str, b: str) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb

    def components(self) -> dict[str, set[str]]:
        groups: dict[str, set[str]] = defaultdict(set)
        for node in self.parent:
            groups[self.find(node)].add(node)
        return groups


def identifiers(resource: dict) -> set[str]:
    ids = resource.get("identifier")
    ids = [ids] if isinstance(ids, dict) else (ids or [])
    return {f"{i.get('system')}|{i.get('value')}" for i in ids
            if isinstance(i, dict) and i.get("system") and i.get("value")}


def surname(resource: dict) -> str | None:
    for name in resource.get("name", []) or []:
        family = name.get("family")
        if family:
            return family.strip().upper()
    return None


def family_label(surnames: list[str]) -> str:
    """Display name for a family on the published page.

    Surnames are upper-cased for matching; title-case them for display. A
    family is NOT required to share a surname (the RelatedPerson network is
    the signal, not the name), so more than one is normal and all are named
    rather than picking a winner.
    """
    shown = [s.title() for s in surnames]
    if not shown:
        return "Family (surname not recorded)"
    return " / ".join(shown)


def address_key(resource: dict) -> str | None:
    addresses = resource.get("address")
    if isinstance(addresses, dict):
        addresses = [addresses]
    for addr in (addresses or []):
        line = " ".join(addr.get("line", []) or [])
        city = addr.get("city", "")
        postcode = addr.get("postalCode", "")
        if line or city or postcode:
            return f"{line}|{city}|{postcode}".strip().upper()
    return None


def build_relatedperson_identities(index: dict) -> tuple[dict, dict]:
    """Group RelatedPerson records into identities, resolved to Patients.

    Returns (identity_of: RelatedPerson-key -> identity-id,
             canonical_of: identity-id -> Patient-key or identity-id itself).
    """
    resources = index["resources"]
    related_people = {k: v for k, v in resources.items()
                      if v["resource_type"] == "RelatedPerson"}
    patients = {k: v for k, v in resources.items()
               if v["resource_type"] == "Patient"}

    ident_to_rp: dict[str, set[str]] = defaultdict(set)
    for key, entry in related_people.items():
        for ident in identifiers(entry["resource"]):
            ident_to_rp[ident].add(key)

    uf = UnionFind()
    for key in related_people:
        uf.find(key)  # ensure every RelatedPerson has its own component
    for rp_keys in ident_to_rp.values():
        rp_keys = sorted(rp_keys)
        for other in rp_keys[1:]:
            uf.union(rp_keys[0], other)

    identity_of = {key: uf.find(key) for key in related_people}

    # Resolve each identity to a Patient sharing at least one identifier.
    patient_by_ident: dict[str, str] = {}
    for pkey, pentry in patients.items():
        for ident in identifiers(pentry["resource"]):
            patient_by_ident.setdefault(ident, pkey)

    canonical_of: dict[str, str] = {}
    for identity_id, members in uf.components().items():
        resolved = None
        for rp_key in sorted(members):
            for ident in identifiers(related_people[rp_key]["resource"]):
                if ident in patient_by_ident:
                    resolved = patient_by_ident[ident]
                    break
            if resolved:
                break
        canonical_of[identity_id] = resolved or identity_id

    return identity_of, canonical_of


def build_primary_components(index: dict) -> list[dict]:
    resources = index["resources"]
    related_people = {k: v for k, v in resources.items()
                      if v["resource_type"] == "RelatedPerson"}
    identity_of, canonical_of = build_relatedperson_identities(index)

    graph = UnionFind()
    edges: dict[str, list[dict]] = defaultdict(list)
    excluded = []

    for rp_key, entry in sorted(related_people.items()):
        patient_ref = entry["resource"].get("patient", {}).get("reference")
        if not patient_ref or patient_ref not in resources:
            continue
        codes = [c.get("code") for rel in entry["resource"].get("relationship", [])
                for c in rel.get("coding", [])]
        if any(c in EXCLUDED_RELATIONSHIP_CODES for c in codes):
            excluded.append({"related_person": rp_key, "patient": patient_ref,
                             "codes": codes})
            continue

        described = canonical_of[identity_of[rp_key]]
        graph.find(described)
        graph.find(patient_ref)
        graph.union(described, patient_ref)

        edge_key = graph.find(described)
        edges[edge_key].append({
            "related_person": rp_key, "described_as": described,
            "in_chart_of": patient_ref, "relationship_codes": codes,
        })

    # SECOND PRIMARY SIGNAL — a shared Medicare card.
    #
    # Unioned into the same graph rather than replacing the RelatedPerson
    # signal, because neither dominates. Measured on this data set the two agree
    # on all 7 families, but each catches something the other cannot:
    # baby-banks-john has no Medicare number (a newborn not yet on the card) and
    # is found only via RelatedPerson, while a family whose RelatedPerson links
    # were absent would be found only via the card.
    by_card: dict[str, list[str]] = defaultdict(list)
    malformed: list[dict] = []
    for key, entry in sorted(resources.items()):
        if entry["resource_type"] not in ("Patient", "RelatedPerson"):
            continue
        card = medicare_card(entry["resource"])
        if card:
            by_card[card].append(key)
            continue
        bad = malformed_medicare(entry["resource"])
        if bad is not None:
            malformed.append({"entity": key, "value": bad})

    card_of: dict[str, str] = {}
    for card, keys in sorted(by_card.items()):
        if len(keys) < 2:
            continue
        # Resolve RelatedPerson records to the Patient they describe, so a card
        # links people rather than records.
        resolved = []
        for k in keys:
            if resources[k]["resource_type"] == "RelatedPerson":
                k = canonical_of.get(identity_of.get(k, k), k)
            resolved.append(k)
        resolved = sorted(set(resolved))
        for other in resolved[1:]:
            graph.find(resolved[0]); graph.find(other)
            graph.union(resolved[0], other)
        for k in resolved:
            card_of[k] = card

    components = []
    for root, members in graph.components().items():
        if len(members) < 2:
            continue
        edge_list = edges.get(graph.find(root), [])
        # Only report entities the wiki can display — Patients, or the
        # RelatedPerson-only identity (no independent Patient record).
        display_members = []
        for m in sorted(members):
            if m in resources and resources[m]["resource_type"] == "Patient":
                display_members.append(lib.member(
                    resources[m]["id"], resource_type="Patient",
                    path=resources[m]["path"], why="RelatedPerson network",
                ))
            else:
                # A RelatedPerson-only identity (e.g. Flavia Ballantyne): show
                # via its first RelatedPerson record for a path and a name.
                rp_entry = resources.get(m)
                if rp_entry:
                    display_members.append(lib.member(
                        rp_entry["id"], resource_type="RelatedPerson",
                        path=rp_entry["path"],
                        why="RelatedPerson network; no independent Patient record",
                    ))
        cards = sorted({card_of[m] for m in members if m in card_of})
        signals = []
        if edge_list:
            signals.append("related_person")
        if cards:
            signals.append("medicare_card")
        surnames = sorted({s for s in (surname(resources[m]["resource"])
                                       for m in members if m in resources) if s})
        components.append({
            "id": f"related-{sorted(members)[0].split('/')[-1]}",
            "signal": "related_person" if "related_person" in signals else "medicare_card",
            "signals": signals,
            "medicare_cards": cards,
            "label": family_label(surnames),
            "members": display_members,
            "edges": edge_list,
        })
    return components, excluded, malformed


def build_secondary_candidates(index: dict, primary_sets: list[set[str]]) -> list[dict]:
    resources = index["resources"]
    patients = {k: v for k, v in resources.items()
               if v["resource_type"] == "Patient"}

    by_surname: dict[str, set[str]] = defaultdict(set)
    by_address: dict[str, set[str]] = defaultdict(set)
    for key, entry in patients.items():
        s = surname(entry["resource"])
        if s:
            by_surname[s].add(key)
        a = address_key(entry["resource"])
        if a:
            by_address[a].add(key)

    candidates = []

    def emit_group(keys: set[str], signal: str, label: str):
        if len(keys) < 2:
            return
        if any(keys <= covered for covered in primary_sets):
            return  # fully explained by a primary component already
        members = [lib.member(
            resources[k]["id"], resource_type="Patient", path=resources[k]["path"],
            why=f"{signal} match: {label}",
        ) for k in sorted(keys)]
        candidates.append({
            "id": f"{signal}-{sorted(keys)[0].split('/')[-1]}",
            "signal": signal, "match_value": label, "members": members,
            "label": family_label([label]) if signal == "surname"
                     else f"Shared address: {label}",
        })

    for surname_value, keys in sorted(by_surname.items()):
        emit_group(keys, "surname", surname_value)
    for addr_value, keys in sorted(by_address.items()):
        emit_group(keys, "address", addr_value)

    return candidates


def main():
    lib.check_preconditions()
    index = lib.build_reference_index()

    primary, excluded_edges, malformed_medicare_values = build_primary_components(index)
    primary_sets = [
        {f"Patient/{m['id']}" for m in comp["members"] if m["resource_type"] == "Patient"}
        for comp in primary
    ]
    secondary = build_secondary_candidates(index, primary_sets)

    all_candidates = primary + secondary
    confirmed, rejected, flagged, undecided = lib.partition_candidates(
        "families", all_candidates)

    members = []
    for cand in confirmed:
        # Carry the family's identity onto each member. Without it the page
        # can only show 30 people in one undifferentiated list, which says
        # nothing about who belongs with whom — the only thing this subset
        # exists to establish.
        for m in cand["members"]:
            members.append({**m, "attester": cand.get("attester"),
                            "confirmed_on": cand.get("confirmed_on"),
                            "family": cand["id"],
                            "family_label": cand.get("label") or cand["id"]})

    # Per-family facts, recorded once per family rather than on every member.
    # Which signals support a family is the evidence a reader needs to judge
    # it: two independent signals agreeing is materially stronger than one.
    confirmed_families = [{
        "id": c["id"],
        "label": c.get("label") or c["id"],
        "signals": c.get("signals") or ([c["signal"]] if c.get("signal") else []),
        "medicare_cards": c.get("medicare_cards") or [],
        "members": len(c["members"]),
    } for c in confirmed]

    flagged_out = [{
        "id": c["id"], "signal": c.get("signal"),
        "members": [m["id"] for m in c["members"]],
        "attester": c.get("attester"), "confirmed_on": c.get("confirmed_on"),
        "note": c.get("decision_note"),
    } for c in flagged]

    notes = [
        f"{len(primary)} RelatedPerson-network families "
        f"({sum(len(c['members']) for c in primary)} entities); "
        f"{len(secondary)} additional surname/address candidates.",
        f"{len(confirmed)} confirmed, {len(rejected)} rejected, "
        f"{len(flagged)} flagged as potential families, "
        f"{len(undecided)} awaiting a decision.",
        "A shared Medicare card is treated as a primary signal alongside the "
        "RelatedPerson network: the card number is 10 digits plus a per-person "
        "Individual Reference Number, so a family on one card shares the first "
        "10 digits. Neither signal dominates — a newborn not yet on the card is "
        "found only via RelatedPerson.",
        f"{len(excluded_edges)} RelatedPerson record(s) excluded as "
        "'unrelated friend' (FRND) and not used to join any family.",
        "Family members are not required to share an address. Same-surname "
        "and same-address candidates are proposals only, never asserted — "
        "measured case: 9 Patient files sharing a surname and address are 9 "
        "test-data variants of one synthetic patient, not a family.",
    ]

    # Subset identification covers administrative entities only (lib).
    members, dropped_nonadmin = lib.filter_administrative(members)
    admin_note = lib.administrative_note(dropped_nonadmin)
    if admin_note:
        notes.append(admin_note)

    return lib.emit(
        "families",
        members=members,
        needs_confirmation=undecided,
        evidence={
            "non_administrative_excluded": dropped_nonadmin,
            "confirmed_families": confirmed_families,
            "counts": {
                "primary_families": len(primary),
                "secondary_candidates": len(secondary),
                "confirmed": len(confirmed),
                "rejected": len(rejected),
                "awaiting_decision": len(undecided),
                "excluded_frnd_edges": len(excluded_edges),
                "flagged": len(flagged),
                "malformed_medicare_values": len(malformed_medicare_values),
            },
            "excluded_relationship_codes": sorted(EXCLUDED_RELATIONSHIP_CODES),
            "flagged_potential_families": flagged_out,
            "malformed_medicare_values": malformed_medicare_values,
            "excluded_edges": excluded_edges,
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
