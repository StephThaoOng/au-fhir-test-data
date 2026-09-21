#!/usr/bin/env python3
"""Assemble subsets.yaml + candidate JSON into the published wiki page.

Output:  docs/DataSubsets.md
Tasks:   5.1 - 5.5

Contract
--------
Pure computation, no judgment (design.md D2): by the time this runs, every
human decision has already been made (candidate JSON's `members` already
reflects confirmations via lib.partition_candidates) and only the merge and
render remain.

docs/DataSubsets.md is the ONLY artifact ever proposed upstream to
hl7au/au-fhir-test-data, and then only when explicitly promoted (D8).

Per-subset membership source (task 5.1)
----------------------------------------
For each of the 14 subsets, in this priority order:

  1. A candidate JSON file exists in the scratch dir (lib.default_out_dir())
     -> use its `members`. This covers every subset with a script: three
     pure Derived (IG examples x3, blank-slate-patients), one Declared with
     drift-checking (inferno-default-patients), one Declared read live
     (connected-care-journeys), and four Derived+Curated whose `members`
     already reflect confirmed decisions (community-contributions,
     missing-suppressed-data, geography-groups, families).

  2. No candidate JSON -> read subsets.yaml's own hand-authored `members`.
     Covers the three subsets with no script at all: au-ps-test-patients and
     smart-health-checks (flat lists of bare ids), and sparked-cdg-journeys
     (nested by journey, each entry carrying `downstream_use`).

  3. scenario-groups is a real third case: it HAS a script, but that script
     never claims membership itself (D5/D12 — scenarios.py emits its one-time
     seed as `needs_confirmation` for the operator to apply BY HAND to
     subsets.yaml, never writing there itself). So scenario-groups falls
     through to subsets.yaml, and if that is still `{}` (unseeded), the
     section renders as pending rather than crashing or showing nothing
     unexplained.

A subset's "extra grouping field" (task 5.2's substructure)
-------------------------------------------------------------
Four subsets carry a natural sub-grouping beyond resource type, preserved
from their own shape rather than flattened away:
  sparked-cdg-journeys      grouped by `journey`
  connected-care-journeys   grouped by `story` (alex / yuri)
  community-contributions   grouped by `organisation`
  scenario-groups           grouped by `scenario`
Every other subset is grouped by resource type only, per the spec's baseline
requirement.

For scenario-groups the sub-grouping is not a nicety: the subset exists to
record which scenario each entity was built for, so flattening it away leaves
418 entities in one list and no scenarios at all.

Required page structure (task 5.2)
------------------------------------
Per subset section, state ALL of: mechanism, classification type, reservation
status (scoped to write intent per D10 — reading and testing is always
unconstrained), governance, data provenance, intended use, relationships.
Where a property is unknown, the section says so explicitly rather than
omitting it — spec scenario "An unknown property is stated rather than
omitted".

Entity lists (task 5.3)
  Grouped by FHIR resource type (and by the extra field above, where one
  exists). Lists over ENTITY_LIST_THRESHOLD are wrapped in
  <details><summary> so they collapse by default on GitHub. The threshold is
  a rendering tuning value, not pinned in the spec (deliberately — see the
  design's separation of requirements from mechanism detail).

Reservation discoverability (task 5.4)
  Built from a global index of every member id -> the subsets it appears in.
  Where an entity appears in more than one subset and at least one reserves
  it, every one of its listings notes the overlap inline — "also in: X
  (reserved), Y (free to build on)" — right where a reader would see it
  before extending the entity, per the spec's "from the entity's other
  listings" wording.

Generation stamp (task 5.5)
  Source commit of the test data, generation date, and the revision each
  Declared/Derived source was read at (from candidate JSON's
  source_revision). NOT called provenance — provenance on this page means
  data provenance (who authored the entities); this is generation provenance.

Constraints
-----------
Single markdown file rendering correctly on GitHub (C3). Wide content
(the resource-type sub-tables) sits inside collapsed <details> rather than
forcing horizontal scroll on the page.
"""

from __future__ import annotations

import html
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone

import lib

OUTPUT_PATH = lib.REPO_ROOT / "docs" / "DataSubsets.md"
ENTITY_LIST_THRESHOLD = 20


def _href(path: str) -> str:
    """A repo-root-relative path, as a link relative to OUTPUT_PATH's own
    directory (docs/) — the path stored on a member is repo-root-relative,
    but the link is embedded one directory down."""
    return os.path.relpath(lib.REPO_ROOT / path, OUTPUT_PATH.parent)


def _resolve_cell(ref: str | None, index: dict) -> str:
    """A "Type/id" reference as a table cell: linked to its file if it
    resolves in the data set (dataset-wide, not gated on subset/group
    membership), plain backtick text if it doesn't (dangling, or the
    reference is simply absent), empty if there's no reference at all.

    Displays the bare id, not "Type/id" — every other entity listing in
    this document shows the bare id (the column/group heading already
    establishes the type), and the drift check's row parser
    (parse_previous_page) assumes exactly that convention when
    reconstructing a subset's previous membership from the rendered page.
    """
    if not ref:
        return ""
    rid = ref.split("/", 1)[-1]
    entry = index["resources"].get(ref)
    return f"[`{rid}`]({_href(entry['path'])})" if entry else f"`{rid}`"

# Canonical publication order — matches the delta spec's requirement order
# (R1-R14), not the order subsets happen to appear in subsets.yaml.
SUBSET_ORDER = [
    "au-core-ig-examples", "au-ps-ig-examples", "au-erequesting-ig-examples",
    "inferno-default-patients", "au-ps-test-patients", "smart-health-checks",
    "sparked-cdg-journeys", "connected-care-journeys", "community-contributions",
    "missing-suppressed-data", "scenario-groups", "geography-groups",
    "families", "blank-slate-patients",
]

# Canonical resource-type order for entity lists — not alphabetical.
RESOURCE_TYPE_ORDER = [
    "Patient", "PractitionerRole", "Practitioner", "HealthcareService",
    "Organization", "Location", "Endpoint", "RelatedPerson",
]


PLURALS = {"entity": "entities", "grouping": "groupings",
           "candidate": "candidates", "journey": "journeys",
           "relationship": "relationships"}


def plural(n: int, word: str) -> str:
    """"1 entity" / "2 entities" — counts appear in every group heading, so a
    stray "1 entities" is visible in dozens of places at once."""
    return f"{n} {word}" if n == 1 else f"{n} {PLURALS[word]}"


def _resource_type_sort_key(rtype: str) -> tuple[int, str]:
    try:
        return (RESOURCE_TYPE_ORDER.index(rtype), "")
    except ValueError:
        return (len(RESOURCE_TYPE_ORDER), rtype)


# Extra sub-grouping field per subset, beyond resource type (task 5.2 note).
# scenario-groups belongs here: grouping by scenario IS the subset — without
# it the page renders 418 entities as one undifferentiated list and the seven
# scenarios it exists to record are invisible.
GROUP_FIELD = {
    "sparked-cdg-journeys": "programme",
    "connected-care-journeys": "story",
    "community-contributions": "organisation",
    "scenario-groups": "scenario",
    "geography-groups": "state",
    "families": "family_label",
}

# A second grouping level, inside GROUP_FIELD's.
#   geography — a grouping is the unit it proposes, but a reader looks for a
#     place first, so state is outer and the grouping inner.
#   sparked — the journeys belong to two distinct programmes (AU PS and AU
#     Encounter Records). Flattened to journey alone, that distinction is
#     invisible and the AU Encounter Records journey is indistinguishable
#     from the five AU PS ones.
SUBGROUP_FIELD = {
    "geography-groups": "grouping_label",
    "sparked-cdg-journeys": "journey",
}

# What the inner level is called in an outer group's count phrase.
SUBGROUP_NOUN = {
    "geography-groups": "grouping",
    "sparked-cdg-journeys": "journey",
}

PROGRAMME_LABELS = {
    "au-ps": "AU Patient Summary",
    "au-encounter-records": "AU Encounter Records",
}

STORY_LABELS = {"alex": "Alex's Story", "yuri": "Yuri's Story (provisional)"}

# How a family's supporting signals are named on the page.
SIGNAL_LABELS = {
    "related_person": "RelatedPerson network",
    "medicare_card": "shared Medicare card",
    "surname": "matching surname",
    "address": "matching address",
}


# --- Loading and normalising membership --------------------------------

def load_candidates() -> dict[str, dict]:
    out_dir = lib.default_out_dir()
    candidates = {}
    if not out_dir.exists():
        return candidates
    for path in out_dir.glob("*.json"):
        import json
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
        candidates[data["subset"]] = data
    return candidates


def flatten_sparked(members: dict, index: dict) -> tuple[list[dict], list[str]]:
    """Resolve journey member ids against the index — without a resource_type
    and path, these entities would be silently invisible to the reservation
    cross-reference (build_reservation_index skips anything unresolved),
    hiding exactly the AU-PS-IG-example overlap this subset is meant to
    surface."""
    flat, pending_notes, unresolved = [], [], []
    id_to_keys: dict[str, list[str]] = defaultdict(list)
    for key, entry in index["resources"].items():
        id_to_keys[entry["id"]].append(key)

    for group_key in ("au-ps", "au-encounter-records"):
        group = members.get(group_key, {}) or {}
        if group.get("status") == "pending":
            pending_notes.append(group.get("note", f"{group_key} journeys pending."))
            continue

        for journey_slug, journey in group.items():
            # A journey is either a plain list of members, or a mapping with
            # `members` plus journey-level metadata (case_scenario,
            # narrative_status, conflicts). Both shapes appear in subsets.yaml.
            if isinstance(journey, list):
                entries, meta = journey, {}
            elif isinstance(journey, dict):
                entries, meta = journey.get("members", []), journey
            else:
                continue

            if meta.get("case_scenario") or meta.get("narrative_status"):
                pending_notes.append(f"**{meta.get('title', journey_slug)}**")
                if meta.get("case_scenario"):
                    pending_notes.append(
                        f"Case scenario: {meta['case_scenario'].strip()}")
                if meta.get("narrative_status"):
                    pending_notes.append(
                        f"Status: {meta['narrative_status'].strip()}")
            for conflict in meta.get("conflicts", []) or []:
                pending_notes.append(
                    f"CONFLICT — `{conflict['entity']}`: "
                    f"{conflict['note'].strip()}"
                )

            for entry in entries:
                rid = entry["id"]
                matches = id_to_keys.get(rid, [])
                if not matches:
                    # An unresolved journey member is recorded deliberately
                    # (e.g. a named team with no CareTeam resource), so the
                    # gap appears in the wiki rather than only in the YAML.
                    if entry.get("alignment") == "unresolved":
                        flat.append(lib.member(
                            rid, resource_type="Unresolved", path=None,
                            why=entry.get("note", "named in the journey; "
                                          "no matching resource").strip(),
                            programme=group_key,
                            journey=journey_slug,
                            journey_role=entry.get("journey_role"),
                            alignment="unresolved",
                            downstream_use=entry.get("downstream_use") or [],
                        ))
                    else:
                        unresolved.append(rid)
                    continue

                resolved = index["resources"][matches[0]]
                why = f"Sparked CDG journey {journey_slug!r}"
                if entry.get("journey_role"):
                    why = f"{entry['journey_role']} in journey {journey_slug!r}"
                flat.append(lib.member(
                    rid, resource_type=resolved["resource_type"],
                    path=resolved["path"], why=why,
                    programme=group_key, journey=journey_slug,
                    journey_role=entry.get("journey_role"),
                    declared_specialty=entry.get("declared_specialty"),
                    alignment=entry.get("alignment"),
                    downstream_use=entry.get("downstream_use") or [],
                ))

    if unresolved:
        pending_notes.append(
            "Could not resolve in the current data set: " + ", ".join(unresolved)
        )
    return flat, pending_notes


def flatten_scenario_groups(members: dict, index: dict) -> tuple[list[dict], list[str]]:
    """Scenario members are stored as "ResourceType/id" strings.

    Bare ids would be ambiguous: verified across all 7 seeded scenarios, every
    one contains an id shared by more than one resource type (an Organization
    and a Location of the same name), so the type prefix is load-bearing, not
    decoration.
    """
    flat, unresolved = [], []
    for scenario_slug, entries in (members or {}).items():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            key = entry if isinstance(entry, str) else entry.get("id")
            resolved = index["resources"].get(key)
            if resolved is None:
                unresolved.append(f"{scenario_slug}: {key}")
                continue
            flat.append(lib.member(
                resolved["id"], resource_type=resolved["resource_type"],
                path=resolved["path"], why=f"scenario {scenario_slug!r}",
                scenario=scenario_slug,
            ))
    notes = []
    if unresolved:
        notes.append(
            f"{len(unresolved)} seeded scenario member(s) no longer resolve: "
            + ", ".join(unresolved[:10])
            + (" ..." if len(unresolved) > 10 else "")
        )
    return flat, notes


def flatten_bare_id_list(members: list, index: dict) -> tuple[list[dict], list[str]]:
    """A subsets.yaml member list may be bare ids (au-ps-test-patients,
    smart-health-checks). Resolve each against the current data set index."""
    flat, unresolved = [], []
    id_to_keys: dict[str, list[str]] = defaultdict(list)
    for key, entry in index["resources"].items():
        id_to_keys[entry["id"]].append(key)

    for raw in members:
        rid = raw["id"] if isinstance(raw, dict) else raw
        matches = id_to_keys.get(rid, [])
        if not matches:
            unresolved.append(rid)
            continue
        key = matches[0]  # bare-id lists here are known-unambiguous (Patient ids)
        entry = index["resources"][key]
        flat.append(lib.member(
            entry["id"], resource_type=entry["resource_type"],
            path=entry["path"], why="recorded in subsets.yaml",
        ))
    return flat, unresolved


def resolve_membership(subset: dict, candidates: dict, index: dict) -> tuple[list[dict], list[str]]:
    """Return (flat members, notes) for one subset, per the priority order
    documented in the module contract."""
    slug = subset["slug"]
    candidate = candidates.get(slug)

    # scenario-groups is case 3 in the module contract: it HAS a script, but
    # that script never claims membership — it emits a one-time seed for the
    # operator to apply to subsets.yaml by hand (D5/D12). Checking only for
    # "a candidate exists" would use its empty members list and shadow the
    # seeded membership, silently reporting 0.
    scripted_membership = (
        candidate is not None
        and not (slug == "scenario-groups" and not candidate.get("members"))
    )
    if scripted_membership:
        return candidate.get("members", []), list(candidate.get("notes", []))

    raw = subset.get("members")
    candidate_notes = list(candidate.get("notes", [])) if candidate else []

    if slug == "sparked-cdg-journeys":
        flat, pending = flatten_sparked(raw, index)
        return flat, pending

    if slug == "scenario-groups":
        flat, notes = flatten_scenario_groups(raw, index)
        if not flat:
            return [], candidate_notes + [
                "PENDING: the one-time scenario seed has not been applied to "
                "subsets.yaml yet. Run scripts/data-subsets/scenarios.py and "
                "apply its output by hand (D5, D12)."
            ]
        return flat, notes

    if isinstance(raw, list):
        flat, unresolved = flatten_bare_id_list(raw, index)
        notes = []
        if unresolved:
            notes.append(
                "Could not resolve in the current data set: " + ", ".join(unresolved)
            )
        return flat, notes

    return [], [f"No membership data available for {slug!r}."]


# --- Reservation cross-reference (task 5.4) ---------------------------

def build_reservation_index(resolved: dict[str, list[dict]],
                            subsets_by_slug: dict[str, dict]) -> dict[str, list[tuple[str, bool]]]:
    index: dict[str, list[tuple[str, bool]]] = defaultdict(list)
    for slug, members in resolved.items():
        reserved = bool(subsets_by_slug[slug]["reserved"])
        for m in members:
            if not m.get("resource_type") or not m.get("id"):
                continue
            key = f"{m['resource_type']}/{m['id']}"
            index[key].append((slug, reserved))
    return index


# Suppressed entirely as overlap TARGETS — both reserved: false, and every
# appearance to date has been (free to build on) noise rather than a
# reservation conflict (geography-groups: 1022 members, blank-slate-patients:
# a similarly broad share). Does not affect these subsets' own sections,
# where their members still show overlaps into OTHER subsets normally.
SUPPRESSED_OVERLAP_TARGETS = {"geography-groups", "blank-slate-patients"}

# Reservation status not yet reconfirmed for cross-reference purposes.
# Display-only (D20): each subset's own governance section is unchanged;
# only a MENTION of one of these from another entity's overlap note reads
# "(maybe reserved — TBD)" instead of asserting reserved/free-to-build-on.
# Does not reopen D9's reusable-journeys argument for sparked-cdg-journeys /
# scenario-groups — D9 stands; this is a pending reconfirmation, not a
# reversal.
RESERVATION_TBD_TARGETS = {
    "inferno-default-patients", "au-ps-test-patients", "smart-health-checks",
    "sparked-cdg-journeys", "connected-care-journeys", "scenario-groups",
}


def overlap_note(key: str, current_slug: str, res_index: dict) -> str | None:
    others = [(s, r) for s, r in res_index.get(key, []) if s != current_slug
              and s not in SUPPRESSED_OVERLAP_TARGETS]
    if not others:
        return None
    labelled = [
        (s, "maybe reserved — TBD" if s in RESERVATION_TBD_TARGETS
            else "reserved" if r else "free to build on")
        for s, r in sorted(set(others))
    ]
    # What governs an entity is the tightest constraint across its
    # memberships (D21) — once any membership is reserved or TBD, a
    # free-to-build-on membership elsewhere adds noise, not information, so
    # it's dropped. Only shown when it's the sole signal available. This
    # still decides WHICH subsets are named, even though the label itself is
    # no longer printed (D22) — a reservation elsewhere is still what makes
    # an overlap worth surfacing at all.
    stricter = [(s, l) for s, l in labelled if l != "free to build on"]
    shown = stricter or labelled
    # D22: the (reserved) / (maybe reserved — TBD) / (free to build on) label
    # is omitted for now — cluttered the page without adding a decision a
    # reader could act on from the note alone. Just the subset names.
    return "also in: " + ", ".join(f"[{s}](#{s})" for s, _ in shown)


# --- Rendering ----------------------------------------------------------

def render_entity_list(members: list[dict], group_field: str | None,
                       res_index: dict, current_slug: str, index: dict,
                       group_labels: dict | None = None,
                       subgroup_field: str | None = None,
                       group_notes: dict | None = None,
                       subgroup_noun: str = "grouping") -> str:
    """Render a subset's entities, optionally grouped and sub-grouped.

    Where a subset is grouped, every group is a collapsible section whatever
    its size: the group heading is the finding (which family, which journey),
    so it must be scannable without expanding, and a mix of collapsed and
    inline groups in one list reads as though the inline ones were different
    in kind. ENTITY_LIST_THRESHOLD therefore governs only ungrouped lists.

    group_notes maps a group OR sub-group display label to a line of evidence
    rendered just inside it — the suburbs behind a geographic grouping, the
    signals behind a family.
    """
    if not members:
        return "_(no members)_\n"

    lines = []

    def render_flat(entries: list[dict]) -> str:
        by_type: dict[str, list[dict]] = defaultdict(list)
        for m in entries:
            by_type[m.get("resource_type") or "Unspecified"].append(m)
        # Wherever both are present, Practitioner and PractitionerRole
        # combine into one table (render_combined_practitioner_role) instead
        # of rendering as two separate type-groups — folded into
        # PractitionerRole's own slot in RESOURCE_TYPE_ORDER so the rest of
        # the type ordering is undisturbed.
        combine = bool(by_type.get("Practitioner") and by_type.get("PractitionerRole"))
        out = []
        for rtype in sorted(by_type, key=_resource_type_sort_key):
            if combine and rtype == "Practitioner":
                continue
            if combine and rtype == "PractitionerRole":
                n, body = render_combined_practitioner_role(
                    by_type["Practitioner"], by_type["PractitionerRole"])
                out.append(f"**Practitioner / PractitionerRole** ({n})\n")
                out.append(body)
                continue
            group = sorted(by_type[rtype], key=lambda m: m["id"])
            out.append(f"**{rtype}** ({len(group)})\n")
            out.append(render_group(rtype, group))
        return "\n".join(out)

    def render_group(rtype: str, group: list[dict]) -> str:
        fields = []
        for m in group:
            key = f"{rtype}/{m['id']}"
            also_in = overlap_note(key, current_slug, res_index)
            if m.get("path"):
                # The id links straight to the file it resolved to, rather
                # than also printing the path inline — the path is still
                # discoverable (link hover / status bar), it just no longer
                # clutters the list.
                id_cell = f"[`{m['id']}`]({_href(m['path'])})"
            else:
                id_cell = f"`{m['id']}`"
            # Where the journey states a role the data's PractitionerRole
            # does not capture, say so — the journey is authoritative for
            # the role, the data for the coded specialty, and the gap is
            # a finding rather than something to smooth over.
            if m.get("alignment") == "journey_role_more_specific":
                note = f"declared specialty is only \"{m.get('declared_specialty')}\""
            elif m.get("alignment") == "unresolved":
                note = "no matching resource in the data set"
            else:
                note = None
            fields.append({
                "id_cell": id_cell, "role": m.get("journey_role"),
                "note": note,
                # Column header already says "Also in" — the prefix would
                # just repeat it.
                "also_in": also_in[len("also in: "):] if also_in else None,
            })

        # A table earns its place only where most rows actually have
        # something to align — a header+separator over one or two rows, or
        # over a group that's almost all plain ids, is overhead without an
        # alignment payoff. Below that, the existing bullet format stays
        # exactly as it was.
        has_extra = sum(1 for f in fields if f["role"] or f["note"] or f["also_in"])
        if len(fields) < 4 or has_extra / len(fields) <= 0.5:
            rows = []
            for f in fields:
                row = f"- {f['id_cell']}" if f["id_cell"].startswith("[") \
                    else f"- {f['id_cell']} — _(no resource)_"
                if f["role"]:
                    row += f" — **{f['role']}**"
                if f["note"]:
                    row += f" — *{f['note']}*"
                if f["also_in"]:
                    row += f" — *also in: {f['also_in']}*"
                rows.append(row)
            return "\n".join(rows) + "\n"

        use_role = any(f["role"] for f in fields)
        use_note = any(f["note"] for f in fields)
        use_also_in = any(f["also_in"] for f in fields)
        headers = ["ID"]
        headers += ["Role"] if use_role else []
        headers += ["Note"] if use_note else []
        headers += ["Also in"] if use_also_in else []
        rows = ["| " + " | ".join(headers) + " |",
                "| " + " | ".join("---" for _ in headers) + " |"]
        for f in fields:
            cells = [f["id_cell"]]
            if use_role:
                cells.append(f"**{f['role']}**" if f["role"] else "")
            if use_note:
                cells.append(f"*{f['note']}*" if f["note"] else "")
            if use_also_in:
                cells.append(f"*{f['also_in']}*" if f["also_in"] else "")
            rows.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
        return "\n".join(rows) + "\n"

    def referencing(key: str | None, rtype: str) -> list[str]:
        """Every "{rtype}/id" that references `key` anywhere in the data
        set — index["referenced_by"] is built from every outgoing reference
        found on every resource (lib.py's find_references()), not just
        PractitionerRole's, so this also surfaces e.g. a HealthcareService
        that names an Organization via its own providedBy field."""
        if not key:
            return []
        return sorted(
            k for k in index["referenced_by"].get(key, set())
            if k.startswith(f"{rtype}/")
        )

    def _role_code_specialty(role_key: str | None) -> str | None:
        if not role_key:
            return None
        role = index["resources"].get(role_key, {}).get("resource") or {}
        code = role.get("code") or []
        code_text = (code[0].get("text") or (code[0].get("coding") or [{}])[0].get("display")
                    if code else None)
        if not code_text:
            return None
        specialty = role.get("specialty") or []
        specialty_text = (specialty[0].get("text")
                          or (specialty[0].get("coding") or [{}])[0].get("display")
                          if specialty else None)
        # Confirmed: never empty parens — the code stands alone when there's
        # no specialty to qualify it.
        return f"{code_text} ({specialty_text})" if specialty_text else code_text

    def _combined_also_in(prac_key: str | None, role_key: str | None) -> str | None:
        # A practitioner and their own role are very often members of the
        # same other subsets (e.g. both in scenario-groups) — union and
        # de-duplicate rather than show the same subset link twice.
        links, seen = [], set()
        for key in (prac_key, role_key):
            note = overlap_note(key, current_slug, res_index) if key else None
            if not note:
                continue
            for link in note[len("also in: "):].split(", "):
                if link not in seen:
                    seen.add(link)
                    links.append(link)
        return ", ".join(links) if links else None

    def render_combined_practitioner_role(
            prac_group: list[dict], role_group: list[dict]) -> tuple[int, str]:
        """Practitioner and PractitionerRole, today rendered as two separate
        type-groups, combined into one table with the role's occupation
        code/specialty alongside — reachability, not membership, decides
        pairing (as in render_practitioner_relationships), so a practitioner
        with no PractitionerRole member here still gets a row instead of
        disappearing, and likewise a PractitionerRole whose practitioner
        isn't itself a member.

        A member's own `path` (from resolve_membership) is preferred over
        index["resources"] for linking — index only scans the CURRENT
        working tree's data-set dirs, but connected-care-journeys resolves
        its members by reading the connected-care branch directly, so its
        members exist with a valid path despite never appearing in index.
        The trade-off: such a PractitionerRole's actual resource content
        (for code/specialty, or to resolve its practitioner reference)
        genuinely isn't available here either way, so those cells stay
        blank rather than guessing — an unpaired row is honest; a guessed
        pairing would not be.
        """
        known_paths = {f"Practitioner/{m['id']}": m["path"] for m in prac_group
                       if m.get("path")}
        known_paths.update({f"PractitionerRole/{m['id']}": m["path"]
                            for m in role_group if m.get("path")})

        def cell(ref: str | None) -> str:
            if not ref:
                return ""
            path = known_paths.get(ref) or (index["resources"].get(ref) or {}).get("path")
            rid = ref.split("/", 1)[-1]
            return f"[`{rid}`]({_href(path)})" if path else f"`{rid}`"

        covered_roles: set[str] = set()
        row_keys: set[tuple[str | None, str | None]] = set()
        for m in prac_group:
            prac_key = f"Practitioner/{m['id']}"
            role_keys = referencing(prac_key, "PractitionerRole")
            if role_keys:
                for role_key in role_keys:
                    row_keys.add((prac_key, role_key))
                    covered_roles.add(role_key)
            else:
                row_keys.add((prac_key, None))
        for m in role_group:
            role_key = f"PractitionerRole/{m['id']}"
            if role_key in covered_roles:
                continue
            role = index["resources"].get(role_key, {}).get("resource") or {}
            prac_ref = (role.get("practitioner") or {}).get("reference")
            row_keys.add((prac_ref, role_key))

        rows = sorted(row_keys, key=lambda r: (r[0] or "", r[1] or ""))
        headers = ["Practitioner", "PractitionerRole", "Role (specialty)", "Also in"]
        table = ["", "| " + " | ".join(headers) + " |",
                "| " + " | ".join("---" for _ in headers) + " |"]
        for prac_key, role_key in rows:
            cells = [
                cell(prac_key), cell(role_key),
                _role_code_specialty(role_key) or "",
                _combined_also_in(prac_key, role_key) or "",
            ]
            table.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
        return len(rows), "\n".join(table) + "\n"

    def render_practitioner_relationships(entries: list[dict]) -> str | None:
        """One row per (Practitioner, PractitionerRole) pair reachable from
        this unit's own Practitioner members, resolved against the WHOLE
        data set — not gated on whether the PractitionerRole, Organization,
        Location, HealthcareService or Endpoint are themselves members of
        this subset or unit. Most subsets track Practitioner without
        separately tracking PractitionerRole, so there would be nothing to
        show if this only looked at existing members.

        HealthcareService and Endpoint aren't referenced FROM PractitionerRole
        in this data set (no PractitionerRole.healthcareService is ever
        populated, and nothing references an Endpoint at all) — they're
        reached in reverse instead: a HealthcareService names an Organization/
        Location via its own providedBy/location fields, so `referencing`
        surfaces it from the Organization/Location side.
        """
        rows = []
        for m in entries:
            if m.get("resource_type") != "Practitioner":
                continue
            prac_key = f"Practitioner/{m['id']}"
            role_keys = referencing(prac_key, "PractitionerRole")
            for role_key in role_keys:
                role = index["resources"].get(role_key, {}).get("resource") or {}
                org_ref = (role.get("organization") or {}).get("reference")
                loc_refs = [l.get("reference") for l in role.get("location") or []
                           if l.get("reference")]
                hs_keys = sorted({
                    *referencing(org_ref, "HealthcareService"),
                    *(k for loc in loc_refs for k in referencing(loc, "HealthcareService")),
                })
                ep_keys = sorted({
                    *referencing(org_ref, "Endpoint"),
                    *(k for loc in loc_refs for k in referencing(loc, "Endpoint")),
                    *(k for hs in hs_keys for k in referencing(hs, "Endpoint")),
                })
                rows.append((prac_key, role_key, org_ref, loc_refs, hs_keys, ep_keys))
        if not rows:
            return None

        rows.sort(key=lambda r: (r[0], r[1]))
        use_hs = any(r[4] for r in rows)
        use_ep = any(r[5] for r in rows)
        headers = ["Practitioner", "PractitionerRole", "Organization", "Location"]
        headers += ["HealthcareService"] if use_hs else []
        headers += ["Endpoint"] if use_ep else []
        # Leading "" so the join below inserts a blank line after </summary>
        # — GitHub only parses Markdown inside an HTML block (<details>) when
        # it's preceded by a blank line; without it this renders as literal
        # pipe text, not a table.
        table = ["", "| " + " | ".join(headers) + " |",
                "| " + " | ".join("---" for _ in headers) + " |"]
        for prac_key, role_key, org_ref, loc_refs, hs_keys, ep_keys in rows:
            cells = [
                _resolve_cell(prac_key, index), _resolve_cell(role_key, index),
                _resolve_cell(org_ref, index),
                ", ".join(_resolve_cell(r, index) for r in loc_refs),
            ]
            if use_hs:
                cells.append(", ".join(_resolve_cell(r, index) for r in hs_keys))
            if use_ep:
                cells.append(", ".join(_resolve_cell(r, index) for r in ep_keys))
            table.append("| " + " | ".join(cells) + " |")
        return (
            f"\n<details><summary>{plural(len(rows), 'relationship')} — "
            + " / ".join(headers) + "</summary>\n"
            + "\n".join(table) + "\n\n</details>\n"
        )

    def render_body(entries: list[dict]) -> tuple[str, str]:
        """Returns (body, count_phrase) for one outer group.

        With a subgroup field the outer group is a container of groupings, so
        it reports both counts — and distinct entities, not list slots, since
        the same entity can legitimately sit in two adjacent groupings.
        """
        if not subgroup_field:
            body = render_flat(entries)
            rel = render_practitioner_relationships(entries)
            if rel:
                body += rel
            return body, plural(len(entries), "entity")


        by_sub: dict[str, list[dict]] = defaultdict(list)
        for m in entries:
            by_sub[m.get(subgroup_field) or "(ungrouped)"].append(m)
        out = []
        for sub_value in sorted(by_sub):
            sub_entries = by_sub[sub_value]
            # <blockquote> indents the nested collapsible so the hierarchy is
            # visible before it is expanded. GitHub strips `style` attributes
            # from markdown, so margin/padding is not an option; blockquote is
            # on its allowed-tag list and indents the summary line and the
            # body together. A bare nested <details> renders flush left and
            # reads as a sibling of the state above it.
            out.append(
                f"<blockquote>\n"
                f"<details><summary>"
                f"<strong>{html.escape(sub_value, quote=False)}</strong> "
                f"({plural(len(sub_entries), 'entity')})</summary>\n"
            )
            note = (group_notes or {}).get(sub_value)
            if note:
                out.append(f"\n{note}\n")
            sub_body = render_flat(sub_entries)
            rel = render_practitioner_relationships(sub_entries)
            if rel:
                sub_body += rel
            out.append(f"\n{sub_body}\n</details>\n</blockquote>\n")
        distinct = len({f"{m.get('resource_type')}/{m.get('id')}"
                        for m in entries})
        n = len(by_sub)
        return ("\n".join(out),
                f"{plural(n, subgroup_noun)}, {plural(distinct, 'entity')}")

    if group_field:
        by_group: dict[str, list[dict]] = defaultdict(list)
        for m in members:
            by_group[m.get(group_field, "(ungrouped)")].append(m)
        # Sort on the group KEY, not the display label, so the section order
        # stays stable when a label is corrected.
        for group_value in sorted(by_group):
            label = (group_labels or {}).get(group_value, group_value)
            entries = by_group[group_value]
            body, count_phrase = render_body(entries)
            note = (group_notes or {}).get(label)
            note_block = f"\n{note}\n" if note else ""
            lines.append(
                # quote=False: this is element text, not an attribute
                # value, so escaping ' would render Alex&#x27;s Story.
                f"<details><summary>"
                f"<strong>{html.escape(label, quote=False)}</strong> "
                f"({count_phrase})</summary>\n{note_block}\n{body}\n</details>\n"
            )
        return "\n".join(lines)

    body = render_flat(members)
    rel = render_practitioner_relationships(members)
    if rel:
        body += rel
    if len(members) > ENTITY_LIST_THRESHOLD:
        return (f"<details><summary>{plural(len(members), 'entity')}"
                f" — click to expand"
                f"</summary>\n\n{body}\n</details>\n")
    return body


def render_property(label: str, value) -> str:
    text = value if (isinstance(value, str) and value.strip()) else None
    return f"- **{label}:** {text or '_not yet known_'}"


SUBSET_TITLES = {}   # slug -> title, populated in main() for link rendering

# Where each external source lives, for turning a recorded revision into a URL.
SOURCE_REPOS = {
    "au-core-ig-examples": "hl7au/au-fhir-core",
    "au-ps-ig-examples": "hl7au/au-fhir-ps",
    "au-erequesting-ig-examples": "hl7au/au-fhir-erequesting",
    "inferno-default-patients": "hl7au/inferno_suite_generator",
    "connected-care-journeys": "hl7au/au-fhir-test-data",
}
SOURCE_LABELS = {
    "au-core-ig-examples": "AU Core IG",
    "au-ps-ig-examples": "AU Patient Summary IG",
    "au-erequesting-ig-examples": "AU eRequesting IG",
    "inferno-default-patients": "Inferno test kit",
    "connected-care-journeys": "Connected Care branch",
}


def link_subsets(text: str) -> str:
    """Render {slug} placeholders as links carrying the subset's title.

    Relationships are prose, not a link list — but the subset's NAME is the
    link, so the spec's "Subsets are addressable by slug" scenario still holds
    without the section reading as a list of anchors.
    """
    def sub(m):
        # YAML folded scalars wrap long lines, which can split a placeholder
        # across a line break ("{au-ps-\n      ig-examples}"). The folding
        # turns that into a space, so strip internal whitespace before lookup
        # rather than requiring authors to hand-manage line breaks.
        slug = re.sub(r"\s+", "", m.group(1))
        title = SUBSET_TITLES.get(slug)
        if title is None:
            # Unknown slug: leave it visible rather than silently emitting a
            # dead link a reader would have no way to notice.
            return f"{{{slug}}}"
        return f"[{title}](#{slug})"
    return re.sub(r"\{([a-z0-9-][a-z0-9\-\s]*)\}", sub, text or "")


def revision_url(slug: str, revision: str) -> str | None:
    repo = SOURCE_REPOS.get(slug)
    if not repo or not revision:
        return None
    if re.fullmatch(r"[0-9a-f]{40}", revision):
        return f"https://github.com/{repo}/commit/{revision}"
    return f"https://github.com/{repo}/tree/{revision}"


def render_subset(subset: dict, members: list[dict], notes: list[str],
                  candidate: dict | None, res_index: dict, index: dict) -> str:
    """Render one subset section.

    Five headings, in a fixed order, then Members. Purpose and governance lead
    because they are what a reader needs first; the mechanism detail supports
    at the end.

    Deliberately NOT rendered here: the reserved/free-to-build-on verdict as
    its own heading. It now reads as part of the governance prose, and the page
    intro states once that reservation governs writes and never reads.

    The source revision IS rendered here, as a labelled "Read at:" line beside
    the source it was read from — see D18. It was previously collected in a
    page-level table instead, which separated each SHA from the source that
    would explain it.
    """
    slug = subset["slug"]
    lines = [f"## {subset['title']} <a id=\"{slug}\"></a>\n"]

    lines.append("### Purpose\n")
    lines.append(link_subsets(subset.get("purpose")) or "_not yet recorded_")

    lines.append("### Ownership & governance\n")
    lines.append(f"**Owner:** {subset.get('owner') or '_not yet recorded_'}  ")
    lines.append(link_subsets(subset.get("governance")) or "_not yet recorded_")

    lines.append("### Provenance & use\n")
    lines.append(link_subsets(subset.get("provenance")) or "_not yet recorded_")

    lines.append("### Relationships\n")
    lines.append(link_subsets(subset.get("relationships_note"))
                 or "_not yet recorded_")

    lines.append("### How is this subset identified?\n")
    lines.append(link_subsets(subset.get("identification")) or "_not yet recorded_")
    source = subset.get("source")
    if source:
        lines.append("")
        lines.append(f"**Source:** {str(source).strip()}")
    # The revision this generation actually read, stated next to the source it
    # came from. Recorded per D11 as an output, not a hand-pinned input.
    revision = (candidate or {}).get("source_revision")
    if revision:
        url = revision_url(slug, str(revision))
        shown = f"[`{str(revision)[:12]}`]({url})" if url else f"`{revision}`"
        label = SOURCE_LABELS.get(slug, "source")
        lines.append("")
        lines.append(f"**Read at:** {shown} — the {label} revision this page "
                     "was last generated from.")
    # No separate classification line (D23): the identification prose above
    # already states Derived/Declared/Curated as its opening word(s) — a
    # trailing "_Classification: X._" line only repeated it.

    # Derivation notes exist only for subsets a script actually derives —
    # counts, exclusions, drift/attribution reasoning a reviewer would want
    # to check the machinery behind. A Curated or Declared subset's notes
    # are a human's own account of what they stated, not something to
    # cross-check against a derivation, so the section doesn't apply there.
    if notes and subset.get("type") in ("derived", "derived+curated"):
        # Collapsed like every other evidence block on the page (D20-era
        # precedent): these are derivation detail — counts, exclusions,
        # limitations — useful to a reviewer but not needed to read the
        # section, so they default to closed rather than a permanent
        # grey wall of text under every subset.
        lines.append(
            "<details><summary>Derivation notes</summary>\n"
        )
        for note in notes:
            lines.append(f"> {note}")
        lines.append("\n</details>\n")

    group_field = GROUP_FIELD.get(slug)
    # Display labels for the sub-groups. Story labels are a presentation
    # choice and live here; scenario titles are facts recovered from the seed
    # ref and live in the facts file (D12).
    group_labels = (STORY_LABELS if group_field == "story"
                    else PROGRAMME_LABELS if group_field == "programme"
                    else subset.get("scenario_titles") or {})
    subgroup_field = SUBGROUP_FIELD.get(slug)
    # The suburb list is what a reader checks a proposed grouping against —
    # postcode proximity is a weak proxy and there are no coordinates in the
    # data set, so this stands in for the distance check (see geography.py).
    evidence = (candidate or {}).get("evidence") or {}
    group_notes = {}
    for g in evidence.get("confirmed_groupings", []):
        if g.get("suburbs"):
            group_notes[g["label"]] = "_" + ", ".join(g["suburbs"]) + "._"
    # Which signals support a family, and the shared card where there is one.
    # Two independent signals agreeing is materially stronger evidence than
    # one, so the reader should not have to open the JSON to see which held.
    for f in evidence.get("confirmed_families", []):
        bits = [SIGNAL_LABELS.get(s, s) for s in f.get("signals", [])]
        if not bits:
            continue
        line = "Signals: " + ", ".join(bits)
        if f.get("medicare_cards"):
            line += f" ({', '.join(f['medicare_cards'])})"
        group_notes[f["label"]] = f"_{line}._"

    # Count distinct entities, not list slots: geography's windowed regional
    # rule is deliberately not a partition, so an entity on a boundary appears
    # under two adjacent groupings and would otherwise be double-counted.
    distinct = len({f"{m.get('resource_type')}/{m.get('id')}"
                    for m in members})
    # Blank separator, not relied on from whatever precedes it (the Read-at
    # line, or a Derivation notes block that's no longer guaranteed to be
    # there) — a heading needs its own paragraph break regardless.
    lines.append("")
    lines.append(f"### Members ({distinct})\n")
    lines.append(render_entity_list(members, group_field, res_index, slug,
                                    index, group_labels, subgroup_field,
                                    group_notes,
                                    SUBGROUP_NOUN.get(slug, "grouping")))

    if candidate:
        # ig_examples.py's note ("N IG example resources matched nothing...
        # Listed under evidence") pointed at evidence that was written to
        # the candidate JSON but never actually rendered anywhere on the
        # page — a dangling reference nobody reading only the wiki could
        # follow. Render it for real.
        unmatched = (candidate.get("evidence") or {}).get(
            "unmatched_ig_examples") or []
        if unmatched:
            rows = ["", "| Example file | Resource | From a Bundle entry? |",
                    "| --- | --- | --- |"]
            for u in unmatched:
                in_bundle = "yes" if u.get("in_bundle") else "no"
                rows.append(
                    f"| `{u['example']}` | `{u['resource']}` | {in_bundle} |")
            n = len(unmatched)
            lines.append(
                f"\n<details><summary>IG example resource{'s' if n != 1 else ''} "
                f"matched nothing in the test data set — {n} "
                f"possibly IG-only</summary>\n"
                + "\n".join(rows) + "\n\n</details>\n"
            )

        flagged = (candidate.get("evidence") or {}).get(
            "flagged_potential_families") or []
        if flagged:
            rows = ["", "| Candidate | Entities | Why it is unresolved |",
                    "| --- | --- | --- |"]
            for f in sorted(flagged, key=lambda f: f["id"]):
                note = (f.get("note") or "").replace("\n", " ").strip()
                rows.append(f"| `{f['id']}` | {', '.join(f['members'])} | {note} |")
            # Collapsed like the members list above it, so the two read as
            # peers rather than the unconfirmed set shouting louder than the
            # confirmed one.
            lines.append(
                f"\n<details><summary><strong>Potentially related — "
                f"unconfirmed</strong> "
                f"({plural(len(flagged), 'candidate')})</summary>\n"
                + "\n".join(rows) + "\n\n</details>\n"
            )

        needs = candidate.get("needs_confirmation") or []
        if needs:
            n = len(needs)
            lines.append(
                f"\n_{n} candidate{'s' if n != 1 else ''} awaiting operator "
                "confirmation._"
            )
            if any(c.get("suburbs") for c in needs):
                rows = ["", "| Candidate | Coverage | Entities | Suburbs |",
                        "| --- | --- | ---: | --- |"]
                for c in sorted(needs, key=lambda c: -len(c.get("members", []))):
                    subs = ", ".join(c.get("suburbs", [])) or "_none_"
                    rows.append(
                        f"| `{c['id']}` | {c.get('coverage','')} | "
                        f"{len(c.get('members', []))} | {subs} |"
                    )
                body = "\n".join(rows)
                lines.append(
                    f"\n<details><summary>Candidates awaiting review — check the "
                    f"suburb list before confirming</summary>\n{body}\n\n</details>\n"
                )

    return "\n".join(lines) + "\n"


# --- Regeneration drift check -------------------------------------------
#
# A regeneration can silently lose a member the previous page had — the
# case that prompted this: an upstream rename orphaned a confirmation keyed
# to the old id (confirmations.json keys on exact Type/id), so the renamed
# entity was re-detected by its script but sat unconfirmed under its new
# identity and vanished from the page with no visible signal beyond a
# smaller count buried in a details block. This compares this run's
# membership against the last COMMITTED page and tries to tell a rename
# (file moved, same content — git's own rename detection settles this)
# apart from a genuine removal or an intentional curation change, so a
# maintainer gets "X was probably renamed to Y" instead of just "it's
# smaller now".

PREVIOUS_ROW_RE = re.compile(r"^(?:- |\| )\[`([^`]+)`\]\(([^)]+)\)")
SECTION_ANCHOR_RE = re.compile(r'^## .*<a id="([^"]+)"></a>')
STAMP_COMMIT_RE = re.compile(r"commit `([0-9a-f]{7,40})`")
FILENAME_TYPE_ID_RE = re.compile(r"^([A-Z][A-Za-z]*)-(.+)\.json$")


def _git_lines(*args: str) -> list[str] | None:
    """Run git read-only; None on any failure rather than raising.

    Unlike lib._git(), a failure here must never block regeneration — this
    check is diagnostic, not a precondition the page depends on (a shallow
    clone or an unreachable old commit just means less can be classified,
    not that generation should stop).
    """
    result = subprocess.run(
        ["git", "-C", str(lib.REPO_ROOT), *args],
        capture_output=True, text=True,
    )
    return result.stdout.splitlines() if result.returncode == 0 else None


def _type_and_id_from_path(path: str) -> tuple[str, str] | None:
    m = FILENAME_TYPE_ID_RE.match(path.rsplit("/", 1)[-1])
    return (m.group(1), m.group(2)) if m else None


def parse_previous_page(text: str) -> tuple[dict[str, set[tuple[str, str, str]]], str | None]:
    """Reconstruct each subset's membership from the last committed page.

    Only resolved rows (a hyperlinked id, from render_group() above) carry a
    path to check a rename or removal against, so unresolved
    (`_(no resource)_`) rows are not tracked here — there is nothing to
    diff them against, and their disappearance is not this check's concern.

    PREVIOUS_ROW_RE matches the id/link on either a bullet row (`- [`id`]
    (href)`) or a table row (`| [`id`](href) | ...`) — render_group() picks
    one or the other per group, so both must parse or a dense group's
    membership would silently read as empty here.
    """
    by_subset: dict[str, set[tuple[str, str, str]]] = defaultdict(set)
    current_slug = None
    commit = None
    for line in text.splitlines():
        anchor = SECTION_ANCHOR_RE.match(line)
        if anchor:
            current_slug = anchor.group(1)
            continue
        if commit is None:
            stamp = STAMP_COMMIT_RE.search(line)
            if stamp:
                commit = stamp.group(1)
        if current_slug is None:
            continue
        row = PREVIOUS_ROW_RE.match(line)
        if not row:
            continue
        rid, href = row.groups()
        path = href[3:] if href.startswith("../") else href
        parsed = _type_and_id_from_path(path)
        rtype = parsed[0] if parsed else "Unspecified"
        by_subset[current_slug].add((rtype, rid, path))
    return dict(by_subset), commit


def check_for_dropped_members(resolved: dict[str, list[dict]]) -> list[dict]:
    """Compare this run's membership against the last committed page.

    Returns a list of finding dicts (subset, severity, resource_type, id,
    old_path, and new_path/new_id when severity is RENAMED), one per entity
    that was a member of some subset in the last committed page and is not
    a member of that same subset now:

      - RENAMED: git's own rename detection ties the old path to a new one
        between the previous page's stamped commit and HEAD.
      - REMOVED: the old file no longer exists and no rename was detected.
      - DROPPED: the old file is unchanged, but the subset's membership
        (curation, confirmation) no longer includes it — often intentional
        (e.g. a journey's roster was edited), surfaced for visibility, not
        as an error.
    """
    prev_lines = _git_lines("show", "HEAD:docs/DataSubsets.md")
    if prev_lines is None:
        return []  # First-ever run, or HEAD predates this file — nothing to compare.
    previous_by_subset, anchor_commit = parse_previous_page("\n".join(prev_lines))

    current_by_subset: dict[str, set[tuple[str, str]]] = {
        slug: {(m.get("resource_type") or "Unspecified", m["id"]) for m in members}
        for slug, members in resolved.items()
    }

    dropped = [
        (slug, rtype, rid, path)
        for slug, prev_members in previous_by_subset.items()
        for rtype, rid, path in prev_members
        if (rtype, rid) not in current_by_subset.get(slug, set())
    ]
    if not dropped:
        return []

    rename_map: dict[str, str] = {}
    if anchor_commit:
        dataset_pathspec = str(lib.DATA_SET_ROOT.relative_to(lib.REPO_ROOT))
        rename_lines = _git_lines(
            "diff", "--find-renames=50%", "--diff-filter=R", "--name-status",
            anchor_commit, "HEAD", "--", dataset_pathspec,
        )
        for line in rename_lines or []:
            cols = line.split("\t")
            if len(cols) == 3 and cols[0].startswith("R"):
                rename_map[cols[1]] = cols[2]

    findings = []
    for slug, rtype, rid, old_path in dropped:
        if old_path in rename_map:
            new_path = rename_map[old_path]
            new_parsed = _type_and_id_from_path(new_path)
            findings.append({
                "subset": slug, "severity": "RENAMED",
                "resource_type": rtype, "id": rid, "old_path": old_path,
                "new_path": new_path,
                "new_id": new_parsed[1] if new_parsed else None,
            })
        elif not (lib.REPO_ROOT / old_path).exists():
            findings.append({
                "subset": slug, "severity": "REMOVED",
                "resource_type": rtype, "id": rid, "old_path": old_path,
            })
        else:
            findings.append({
                "subset": slug, "severity": "DROPPED",
                "resource_type": rtype, "id": rid, "old_path": old_path,
            })
    return findings


def print_drop_report(findings: list[dict]) -> None:
    by_severity = {sev: [f for f in findings if f["severity"] == sev]
                  for sev in ("RENAMED", "REMOVED", "DROPPED")}
    print(f"\n{plural(len(findings), 'entity')} present in the previous "
          "page are missing from this regeneration:\n")
    if by_severity["RENAMED"]:
        print("RENAMED — likely needs a subsets.yaml/confirmations.json "
              "update to the new id:")
        for f in by_severity["RENAMED"]:
            new_id = f" (new id: {f['new_id']})" if f.get("new_id") else ""
            print(f"  [{f['subset']}] {f['resource_type']}/{f['id']} "
                  f"({f['old_path']}) -> {f['new_path']}{new_id}")
    if by_severity["REMOVED"]:
        print("\nREMOVED — file no longer exists, no rename detected:")
        for f in by_severity["REMOVED"]:
            print(f"  [{f['subset']}] {f['resource_type']}/{f['id']} "
                  f"({f['old_path']})")
    if by_severity["DROPPED"]:
        print("\nDROPPED — resource unchanged, no longer a subset member "
              "(verify this was intentional):")
        for f in by_severity["DROPPED"]:
            print(f"  [{f['subset']}] {f['resource_type']}/{f['id']} "
                  f"({f['old_path']})")
    print()


def render_drop_callout(findings: list[dict]) -> str:
    by_severity = {sev: [f for f in findings if f["severity"] == sev]
                  for sev in ("RENAMED", "REMOVED", "DROPPED")}
    body = []
    if by_severity["RENAMED"]:
        body.append("> **Likely renamed** — verify the subset's membership "
                    "or confirmations.json reference the new id:")
        for f in by_severity["RENAMED"]:
            new_id = f" (new id `{f['new_id']}`)" if f.get("new_id") else ""
            body.append(
                f"> - `{f['resource_type']}/{f['id']}` (`{f['old_path']}`) "
                f"→ likely `{f['new_path']}`{new_id} — subset "
                f"[{f['subset']}](#{f['subset']})"
            )
    if by_severity["REMOVED"]:
        body.append("> **No longer exists, no rename detected:**")
        for f in by_severity["REMOVED"]:
            body.append(
                f"> - `{f['resource_type']}/{f['id']}` (`{f['old_path']}`) "
                f"— subset [{f['subset']}](#{f['subset']})"
            )
    if by_severity["DROPPED"]:
        body.append("> **Resource unchanged, no longer a subset member** "
                    "— verify this was intentional:")
        for f in by_severity["DROPPED"]:
            body.append(
                f"> - `{f['resource_type']}/{f['id']}` (`{f['old_path']}`) "
                f"— subset [{f['subset']}](#{f['subset']})"
            )
    summary = (
        f"⚠️ Regeneration drift check — {plural(len(findings), 'entity')} "
        f"present in the previous page {'is' if len(findings) == 1 else 'are'} "
        "missing from this one"
    )
    return (
        f"<details><summary>{summary}</summary>\n\n"
        + "\n".join(body) + "\n\n</details>\n"
    )


def generation_stamp(candidates: dict) -> str:
    """Page-level generation stamp.

    Source revisions are NOT listed here — each subset states its own under
    "How is this subset identified?", next to the source it was read from,
    since that is where a reader asking "which version?" is already looking.
    """
    head = subprocess.run(
        ["git", "-C", str(lib.REPO_ROOT), "rev-parse", "HEAD"],
        capture_output=True, text=True,
    ).stdout.strip()
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return (
        f"_Generated {date} from test data at commit `{head}`. "
        "This page is regenerated manually — see "
        "[docs/data-subsets/README.md](data-subsets/README.md)._\n"
    )


def main():
    lib.check_preconditions()
    facts = lib.load_facts()
    subsets_by_slug = {s["slug"]: s for s in facts["subsets"]}
    # Populate the slug -> title map that link_subsets() uses to render
    # {slug} placeholders in the curated Relationships prose.
    SUBSET_TITLES.clear()
    SUBSET_TITLES.update({s["slug"]: s["title"] for s in facts["subsets"]})
    candidates = load_candidates()
    index = lib.build_reference_index()

    resolved: dict[str, list[dict]] = {}
    notes_by_slug: dict[str, list[str]] = {}
    for slug in SUBSET_ORDER:
        subset = subsets_by_slug[slug]
        members, notes = resolve_membership(subset, candidates, index)
        resolved[slug] = members
        notes_by_slug[slug] = notes

    res_index = build_reservation_index(resolved, subsets_by_slug)
    drop_findings = check_for_dropped_members(resolved)
    if drop_findings:
        print_drop_report(drop_findings)

    parts = [
        "# HL7 AU FHIR Test Data — Data Subsets\n",
        "Identifies the logical subsets of the test data set: which entities "
        "belong to each, how membership is established, who owns it, and how "
        "subsets relate to one another. See "
        "[docs/data-subsets/README.md](data-subsets/README.md) for how to "
        "regenerate this page.\n",

        # This page is the only artefact proposed upstream (D8) — the proposal,
        # spec, design and scripts all stay in the fork. So the context a
        # reader needs to interpret it has to live here, not only in those.
        "### Why these subsets are worth tracking\n",
        "The administrative entities in this data set — Patient, "
        "RelatedPerson, Practitioner, PractitionerRole, Organization, "
        "HealthcareService, Location and Endpoint — cannot simply be created "
        "or modified on demand within this project. Their key identifiers and "
        "some core attributes are allocated by Services Australia and "
        "correspond to entities provisioned in the HI Vendor Test "
        "Environment; the instances here map those records into FHIR and may "
        "include some data enrichment, but generally need to stay aligned "
        "with them.\n",
        "Using the test data therefore tends to start with finding entities "
        "that already fit, since requesting new ones is a considerably more "
        "costly path. That requires knowing which entities are already "
        "committed to a purpose that new content could disturb, which are "
        "free to build on, and which suit a new need — co-located for a "
        "plausible consumer journey, related as a family, or carrying no "
        "clinical data at all. This page is where that is recorded.\n",

        "### What is in scope\n",
        "Only the eight administrative entity types listed above. Clinical "
        "resources carry far less shared governance with external parties and "
        "can be authored more freely, so tracking their subset membership is "
        "low value — and where clinical content is needed, it is retrievable "
        "from the administrative entity by ordinary FHIR mechanisms. One "
        "subset is exempt: *Missing and suppressed data examples*, whose "
        "instances demonstrate the correct representation of absent data, a "
        "property that attaches to an Observation exactly as it does to a "
        "Patient.\n",

        # D10, stated once here rather than repeated in all 14 sections.
        "### Reading versus writing\n",
        "**Reading is always unconstrained.** Any entity may be read, loaded, "
        "queried or tested against without reference to this page. Where a "
        "subset's governance restricts something, it restricts *writing* — "
        "adding to or modifying an entity or its network of linked resources "
        "— because new content joins a graph that may already be shaped to "
        "serve a stated purpose.\n",

        # D24, stated once here so no subset has to draw a conclusion it
        # cannot support from its own membership alone.
        "A subset stating that its own membership does not reserve an entity "
        "does not make that entity free to build on — another subset may "
        "reserve it. What governs is the tightest constraint across all of an "
        "entity's memberships, which is what each entity's *also in* note "
        "surfaces.\n",

        "### How each subset is identified\n",
        # D23 removed the trailing "_Classification: X._" line; the type is
        # now the opening word of each identification description.
        "Every subset states its classification where it describes how it is "
        "identified. The four are defined below; the practical difference is "
        "what each needs in order to be trustworthy.\n",
        "<details><summary>What the four classifications mean</summary>\n\n"
        "- **Derived** — computed from the repository by a deterministic "
        "script, with no human input. Recomputed on every regeneration, so it "
        "is current by construction.\n"
        "- **Declared** — stated by an authoritative source outside this page, "
        "which the page transcribes. Records a resolvable source reference so "
        "the transcription can be re-checked, and reports drift rather than "
        "silently overwriting.\n"
        "- **Curated** — decided by this project, with no external source to "
        "check against. Records an attester and a confirmation date instead.\n"
        "- **Derived + Curated** — a script proposes candidate members and a "
        "human confirms or rejects each one. Confirmations are persisted, so "
        "a regeneration asks only about what is new or changed.\n\n"
        "The distinguishing test between Declared and Curated is whether the "
        "fact has a source that could change without this page being told. If "
        "it does, it is Declared and needs a source reference; if it does "
        "not, it is Curated and needs an attester. That is why some sections "
        "show a **Source** and others show an attester.\n\n"
        "</details>\n",
        generation_stamp(candidates),
    ]
    if drop_findings:
        parts.append(render_drop_callout(drop_findings))
    parts.append("## Contents\n")
    parts.append("\n".join(
        f"- [{subsets_by_slug[s]['title']}](#{s})" for s in SUBSET_ORDER
    ) + "\n")

    for slug in SUBSET_ORDER:
        parts.append(render_subset(
            subsets_by_slug[slug], resolved[slug], notes_by_slug[slug],
            candidates.get(slug), res_index, index,
        ))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    # Never block the write on this — the page is always regenerated. A
    # likely rename is the one finding worth a non-zero exit: it usually
    # means subsets.yaml or confirmations.json needs a follow-up edit,
    # unlike a plain removal or an intentional curation change.
    if any(f["severity"] == "RENAMED" for f in drop_findings):
        sys.exit(1)
    return None


if __name__ == "__main__":
    lib.main_wrapper(main)()
