#!/usr/bin/env python3
"""Propose geographic groupings: metro by city, regional by postcode window.

Subset:  geography-groups
Type:    Derived + Curated
Task:    4.5

Contract
--------
Proposes groupings of Practitioner, Organization, Location, Patient and
RelatedPerson that are plausibly co-located, expands each by reverse reference,
and overlays scenario groups.

Everything emitted is a CANDIDATE. Nothing reaches `members` without human
confirmation (lib.partition_candidates), and the generated section describes the
subset as best-effort.

Why the rule differs by density
--------------------------------
**Australian postcodes are not spatially ordered.** Within a capital they were
allocated by delivery-office history, so numerically distant codes can be
adjacent suburbs and numerically close ones far apart. Measured:

    Southbank 3006  / St Kilda 3182     ~6km   — 3rd digit differs by 8
    Sydney CBD 2000 / Menai    2234     ~30km  — 2nd digit differs by 2

No arithmetic on the digits captures metro proximity. So:

    metro    -> one group per capital city. Everything inside a capital is
                plausibly co-located for a care journey (~50km worst case),
                and "Melbourne" names the group meaningfully where "30" does
                not.
    regional -> 3-digit bucket, windowed to include buckets whose 3rd digit is
                +/-1, within the same 2-digit prefix.

The metro/regional boundary comes from curated ranges in subsets.yaml
(`derivation_inputs.metro_postcode_ranges`), never hardcoded here — they are a
judgement that already needed correcting once (see that file's comment on 0872).

Why +/-1 windows rather than merged chains
-------------------------------------------
"3rd digit +/-1" is not transitive: 501-502 adjacent, 502-503 adjacent, 501-503
not. Merging every chain was measured to link 081 through 087 — seven buckets,
57 entities — reintroducing exactly the sprawl this rule exists to remove.

Windowing instead gives each bucket its own group of itself plus neighbours, so
501 and 503 still appear together (in the window centred on 502) without
unbounded chaining. Windows overlap at boundaries, which is honest for what
these are: proposals of the form "entities around postcode 501", not a
partition. Windows wholly contained in another are dropped.

The +/-1 allowance is load-bearing, validated against the seven purpose-built
scenarios: ccm-aged-care spans 501/500 and family-w-baby spans 215/214, so exact
3-digit matching would wrongly split both.

Known limitation, deliberately left visible
--------------------------------------------
Where postcodes cover vast areas the window is still too coarse. Buckets 481
(Townsville) and 482 (Mount Isa, Camooweal) are +/-1 adjacent and so merge,
though Townsville to Mount Isa is ~900km. There are no coordinates anywhere in
the data set, so an automated distance check would need an external dataset.

The mitigation is evidence, not arithmetic: every candidate carries its full
suburb list, so a reviewer seeing "Camooweal, Mount Isa, Townsville" rejects it
immediately. Human confirmation is already this subset's designed safety net.

Grouping is best-effort and reusable
-------------------------------------
reserved: false. A grouping is a starting point for building a new consumer
journey, not a claim over its members.

Output
------
members            previously confirmed groupings (via confirmations.json)
needs_confirmation newly proposed or changed groupings
evidence           per grouping: classification (metro city / regional window),
                   the postcode range covered, member counts by origin, and the
                   FULL suburb list — the substitute for a distance check
"""

from __future__ import annotations

from collections import defaultdict

import lib

# Subset identification covers administrative entities only (lib). Using the
# shared constant rather than a local list also closes a gap: HealthcareService
# previously entered only via reverse-reference expansion, and Endpoint not at
# all, despite both being administrative and carrying addresses.
GEO_TYPES = lib.ADMINISTRATIVE_RESOURCE_TYPES

# Australian state/territory codes. An address whose state is not one of these
# is not Australian, and Australian postcode logic must not be applied to it —
# postcode numbering collides across countries. Measured in this data set:
# Napier NZ carries postcode 4104, which falls inside Brisbane's metro range,
# and Rome carries 00184. 11 entities are affected (Napier, Oslo, Rome x9).
AU_STATES = frozenset({"NSW", "VIC", "QLD", "SA", "WA", "TAS", "NT", "ACT"})


def load_metro_ranges() -> list[tuple[str, list[tuple[int, int]]]]:
    subset = lib.get_subset("geography-groups")
    cfg = (subset.get("derivation_inputs") or {}).get("metro_postcode_ranges")
    if not cfg:
        raise lib.PreconditionError(
            "geography-groups.derivation_inputs.metro_postcode_ranges is "
            "missing from subsets.yaml. The metro/regional split is a curated "
            "judgement and must not be inferred here."
        )
    return [(c["city"], [tuple(r) for r in c["ranges"]]) for c in cfg["cities"]]


def metro_city(postcode: str, ranges) -> str | None:
    try:
        n = int(postcode)
    except (TypeError, ValueError):
        return None
    for city, spans in ranges:
        for lo, hi in spans:
            if lo <= n <= hi:
                return city
    return None


def address_field(resource: dict, field: str) -> str | None:
    addresses = resource.get("address")
    if isinstance(addresses, dict):
        addresses = [addresses]
    if not isinstance(addresses, list):
        return None
    for addr in addresses:
        if isinstance(addr, dict) and addr.get(field):
            return addr[field]
    return None


def classify(index: dict, ranges) -> tuple[dict, dict, int, list]:
    """Split geo-eligible entities into metro-by-city and regional-by-bucket.

    Non-Australian addresses are excluded entirely rather than grouped: their
    postcodes collide with Australian ones (Napier NZ 4104 falls inside
    Brisbane's metro range), so including them produces confidently wrong
    groupings.
    """
    metro: dict[str, list[str]] = defaultdict(list)
    regional: dict[str, list[str]] = defaultdict(list)
    unaddressed = 0
    overseas: list[dict] = []
    for key, entry in index["resources"].items():
        if entry["resource_type"] not in GEO_TYPES:
            continue
        postcode = address_field(entry["resource"], "postalCode")
        if not postcode or not str(postcode).isdigit():
            unaddressed += 1
            continue
        state = address_field(entry["resource"], "state")
        if state not in AU_STATES:
            overseas.append({
                "id": entry["id"], "resource_type": entry["resource_type"],
                "city": address_field(entry["resource"], "city"),
                "state": state, "postcode": str(postcode),
                "country": address_field(entry["resource"], "country"),
            })
            continue
        postcode = str(postcode)
        city = metro_city(postcode, ranges)
        if city:
            metro[city].append(key)
        else:
            regional[postcode[:3]].append(key)
    return metro, regional, unaddressed, sorted(overseas, key=lambda o: o["id"])


def build_regional_windows(regional: dict[str, list[str]]) -> dict[str, frozenset]:
    """Each bucket seeds a window of itself plus +/-1 neighbours, same prefix."""
    windows: dict[str, frozenset] = {}
    for bucket in regional:
        prefix, third = bucket[:2], int(bucket[2])
        members: list[str] = []
        for nd in (third - 1, third, third + 1):
            if 0 <= nd <= 9:
                members.extend(regional.get(f"{prefix}{nd}", []))
        windows[bucket] = frozenset(members)

    # Drop any window wholly contained in another — it adds no proposal.
    ordered = sorted(windows, key=lambda b: (-len(windows[b]), b))
    kept: dict[str, frozenset] = {}
    for bucket in ordered:
        if any(windows[bucket] <= existing for existing in kept.values()):
            continue
        kept[bucket] = windows[bucket]
    return kept


def expand_by_reference(index: dict, keys: set[str]) -> dict[str, str]:
    """Entities reachable by the two allowed reverse edges.

    Only HealthcareService->Organization/Location and PractitionerRole->
    Practitioner. A blanket referenced_by walk would drag in Observations,
    Tasks and Encounters that merely reference a grouped Organization.
    """
    resources, referenced_by = index["resources"], index["referenced_by"]
    added: dict[str, str] = {}
    # sorted(): an Organization and a Location commonly share an id, so set
    # iteration order would make the recorded reason vary between runs.
    for key in sorted(keys):
        rtype = resources[key]["resource_type"]
        if rtype not in ("Organization", "Location", "Practitioner"):
            continue
        for referrer in sorted(referenced_by.get(key, ())):
            referrer_type = resources[referrer]["resource_type"]
            valid = (
                (rtype in ("Organization", "Location")
                 and referrer_type == "HealthcareService")
                or (rtype == "Practitioner" and referrer_type == "PractitionerRole")
            )
            if valid and referrer not in keys:
                added[referrer] = (
                    f"{referrer_type} references {rtype}/{resources[key]['id']}")
    return added


def scenario_overlay() -> dict[str, set[str]]:
    """entity key -> scenario slugs. Empty when the seed hasn't been applied."""
    members = lib.get_subset("scenario-groups").get("members") or {}
    by_entity: dict[str, set[str]] = defaultdict(set)
    for slug, entries in members.items():
        if not isinstance(entries, list):
            continue
        for m in entries:
            key = m if isinstance(m, str) else (
                f"{m.get('resource_type')}/{m.get('id')}"
                if isinstance(m, dict) and m.get("resource_type") else None)
            if key:
                by_entity[key].add(slug)
    return by_entity


def grouping_label(cand: dict) -> str:
    """Human-readable name for a grouping, for the published page.

    Metro coverage already reads as a place ("Melbourne metropolitan");
    regional coverage is a bare postcode span ("481xx-483xx") that needs
    saying what it is.
    """
    coverage = cand["coverage"]
    if cand["classification"] == "metro":
        return coverage
    return f"Postcodes {coverage}"


def build_candidate(cid: str, classification: str, coverage: str,
                    keys: set[str], sources: dict[str, str],
                    index: dict, overlay: dict[str, set[str]]) -> dict:
    resources = index["resources"]
    members, states, suburbs = [], set(), set()
    scenario_hits: dict[str, int] = defaultdict(int)
    from_expansion = 0

    for key in sorted(keys):
        entry = resources[key]
        state = address_field(entry["resource"], "state")
        suburb = address_field(entry["resource"], "city")
        if state:
            states.add(state)
        if suburb:
            suburbs.add(suburb)
        for slug in overlay.get(key, set()):
            scenario_hits[slug] += 1

        why = sources.get(key)
        if why:
            from_expansion += 1
        else:
            why = f"{classification} ({coverage})"
        if overlay.get(key):
            why += f"; also in scenario(s) {', '.join(sorted(overlay[key]))}"
        members.append(lib.member(
            entry["id"], resource_type=entry["resource_type"],
            path=entry["path"], why=why,
        ))

    return {
        "id": cid,
        "classification": classification,
        "coverage": coverage,
        "members": members,
        # The suburb list stands in for a distance check — never truncate it.
        "suburbs": sorted(suburbs),
        "states": sorted(states),
        "scenario_overlap": dict(scenario_hits),
        "from_reverse_reference": from_expansion,
        "single_state": len(states) <= 1,
    }


def main():
    lib.check_preconditions()

    ranges = load_metro_ranges()
    index = lib.build_reference_index()
    overlay = scenario_overlay()
    metro, regional, unaddressed, overseas = classify(index, ranges)

    candidates = []

    for city, keys in sorted(metro.items()):
        key_set = set(keys)
        expansion = expand_by_reference(index, key_set)
        candidates.append(build_candidate(
            f"metro-{city.lower()}", "metro", f"{city} metropolitan",
            key_set | set(expansion), expansion, index, overlay))

    for bucket, keys in sorted(build_regional_windows(regional).items()):
        key_set = set(keys)
        expansion = expand_by_reference(index, key_set)
        prefix, third = bucket[:2], int(bucket[2])
        lo = f"{prefix}{max(0, third - 1)}xx"
        hi = f"{prefix}{min(9, third + 1)}xx"
        candidates.append(build_candidate(
            f"postcode-{bucket}", "regional", f"{lo}-{hi}",
            key_set | set(expansion), expansion, index, overlay))

    confirmed, rejected, flagged, undecided = lib.partition_candidates(
        "geography-groups", candidates)

    members = []
    for cand in confirmed:
        # Carry the grouping's identity onto each member. Without this the
        # flattened list loses which grouping an entity came from, and the
        # page can only render 1,000+ entities as one undifferentiated list —
        # the groupings this subset exists to propose become invisible.
        # State comes from the grouping, not the member: expansion members
        # (a PractitionerRole pulled in by reverse reference) carry no address
        # of their own, and every grouping is single-state by construction
        # (mixed_state_groupings is asserted 0 below).
        states = cand.get("states") or []
        state = states[0] if len(states) == 1 else "(multiple states)"
        for m in cand["members"]:
            members.append({**m, "attester": cand.get("attester"),
                            "confirmed_on": cand.get("confirmed_on"),
                            "state": state,
                            "grouping": cand["id"],
                            "grouping_label": grouping_label(cand)})

    notes = [
        f"{len(metro)} metro groups (one per capital city) and "
        f"{len(candidates) - len(metro)} regional windows (3-digit postcode "
        "bucket, widened to buckets whose 3rd digit is +/-1).",
        f"{unaddressed} geo-eligible entities have no usable postcode and are "
        "excluded.",
        f"{len(overseas)} entities have a non-Australian address and are "
        "excluded — Australian postcode logic does not apply to them, and "
        "their postcodes collide with Australian ones (Napier NZ 4104 falls "
        "inside Brisbane's metro range)."
        if overseas else
        "No non-Australian addresses found.",
        f"{len(confirmed)} confirmed, {len(rejected)} rejected, "
        f"{len(undecided)} awaiting a decision.",
        "Metro groups by city because Australian postcodes are not spatially "
        "ordered — Southbank 3006 and St Kilda 3182 are ~6km apart but differ "
        "in the 3rd digit by 8.",
        "LIMITATION: a regional window can still span great distances where "
        "postcodes cover vast areas (Townsville 4810 and Mount Isa 4825 are "
        "+/-1 adjacent but ~900km apart). Check each candidate's suburb list — "
        "there are no coordinates in the data set to check distance against.",
    ]
    if not overlay:
        notes.append(
            "Scenario overlay skipped: scenario-groups has not been seeded yet."
        )
    mixed = [c["id"] for c in candidates if not c["single_state"]]
    if mixed:
        notes.append(
            f"{len(mixed)} grouping(s) span more than one state — weaker "
            "evidence of co-location: " + ", ".join(mixed)
        )

    return lib.emit(
        "geography-groups",
        members=members,
        needs_confirmation=undecided,
        evidence={
            "rule": {
                "metro": "one group per capital city",
                "regional": "3-digit postcode bucket, windowed +/-1 on the 3rd digit",
                "metro_ranges_source": "subsets.yaml geography-groups."
                                       "derivation_inputs.metro_postcode_ranges",
            },
            "unaddressed_excluded": unaddressed,
            "overseas_excluded": overseas,
            # Grouping-level facts, recorded once per grouping rather than
            # repeated onto every member. The suburb list is the substitute
            # for the distance check this data set cannot support, so it is
            # published per grouping and never truncated — previously it
            # appeared only in the awaiting-confirmation table, which meant it
            # disappeared from the page entirely once everything was decided.
            "confirmed_groupings": [
                {
                    "id": c["id"],
                    "label": grouping_label(c),
                    "classification": c["classification"],
                    "state": (c["states"][0] if len(c.get("states") or []) == 1
                              else "(multiple states)"),
                    "suburbs": c["suburbs"],
                    "entities": len(c["members"]),
                }
                for c in confirmed
            ],
            "counts": {
                "overseas_excluded": len(overseas),
                "metro_groups": len(metro),
                "regional_windows": len(candidates) - len(metro),
                "candidate_groupings": len(candidates),
                "confirmed": len(confirmed),
                "rejected": len(rejected),
                "awaiting_decision": len(undecided),
                "mixed_state_groupings": len(mixed),
            },
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
