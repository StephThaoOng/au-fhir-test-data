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
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone

import lib

OUTPUT_PATH = lib.REPO_ROOT / "docs" / "DataSubsets.md"
ENTITY_LIST_THRESHOLD = 20

TYPE_LABELS = {
    "derived": "Derived",
    "declared": "Declared",
    "curated": "Curated",
    "derived+curated": "Derived + Curated",
}

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
           "candidate": "candidates"}


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
    "sparked-cdg-journeys": "journey",
    "connected-care-journeys": "story",
    "community-contributions": "organisation",
    "scenario-groups": "scenario",
    "geography-groups": "state",
    "families": "family_label",
}

# A second grouping level, inside GROUP_FIELD's. Geography is the only subset
# that needs one: a grouping is the unit it proposes, but a reader looks for a
# place first, so state is the outer level and the grouping the inner.
SUBGROUP_FIELD = {
    "geography-groups": "grouping_label",
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
                    path=resolved["path"], why=why, journey=journey_slug,
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
    # it's dropped. Only shown when it's the sole signal available.
    stricter = [(s, l) for s, l in labelled if l != "free to build on"]
    shown = stricter or labelled
    return "also in: " + ", ".join(f"[{s}](#{s}) ({l})" for s, l in shown)


# --- Rendering ----------------------------------------------------------

def render_entity_list(members: list[dict], group_field: str | None,
                       res_index: dict, current_slug: str,
                       group_labels: dict | None = None,
                       subgroup_field: str | None = None,
                       group_notes: dict | None = None) -> str:
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
        out = []
        for rtype in sorted(by_type, key=_resource_type_sort_key):
            group = sorted(by_type[rtype], key=lambda m: m["id"])
            out.append(f"**{rtype}** ({len(group)})\n")
            rows = []
            for m in group:
                key = f"{rtype}/{m['id']}"
                note = overlap_note(key, current_slug, res_index)
                path = f"`{m['path']}`" if m.get("path") else "_(no resource)_"
                row = f"- `{m['id']}` — {path}"
                if m.get("journey_role"):
                    row += f" — **{m['journey_role']}**"
                # Where the journey states a role the data's PractitionerRole
                # does not capture, say so — the journey is authoritative for
                # the role, the data for the coded specialty, and the gap is
                # a finding rather than something to smooth over.
                if m.get("alignment") == "journey_role_more_specific":
                    row += (f" — *declared specialty is only "
                            f"\"{m.get('declared_specialty')}\"*")
                elif m.get("alignment") == "unresolved":
                    row += " — *no matching resource in the data set*"
                if note:
                    row += f" — *{note}*"
                rows.append(row)
            out.append("\n".join(rows) + "\n")
        return "\n".join(out)

    def render_body(entries: list[dict]) -> tuple[str, str]:
        """Returns (body, count_phrase) for one outer group.

        With a subgroup field the outer group is a container of groupings, so
        it reports both counts — and distinct entities, not list slots, since
        the same entity can legitimately sit in two adjacent groupings.
        """
        if not subgroup_field:
            return render_flat(entries), plural(len(entries), "entity")


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
            out.append(f"\n{render_flat(sub_entries)}\n</details>\n</blockquote>\n")
        distinct = len({f"{m.get('resource_type')}/{m.get('id')}"
                        for m in entries})
        n = len(by_sub)
        return ("\n".join(out),
                f"{plural(n, 'grouping')}, {plural(distinct, 'entity')}")

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
                  candidate: dict | None, res_index: dict) -> str:
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
    # The four-way classification closes the section rather than leading it —
    # the prose above already opens with "Derived automatically" / "Curated" /
    # "Declared", so a leading label just repeats the next word.
    type_label = TYPE_LABELS.get(subset["type"], subset["type"])
    lines.append("")
    lines.append(f"_Classification: {type_label}._")

    if notes:
        for note in notes:
            lines.append(f"> {note}")
        lines.append("")

    group_field = GROUP_FIELD.get(slug)
    # Display labels for the sub-groups. Story labels are a presentation
    # choice and live here; scenario titles are facts recovered from the seed
    # ref and live in the facts file (D12).
    group_labels = (STORY_LABELS if group_field == "story"
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
    lines.append(f"### Members ({distinct})\n")
    lines.append(render_entity_list(members, group_field, res_index, slug,
                                    group_labels, subgroup_field,
                                    group_notes))

    if candidate:
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

        "### How each subset is identified\n",
        "Every section closes with a classification. The four are defined "
        "below; the practical difference is what each needs in order to be "
        "trustworthy.\n",
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
        "## Contents\n",
    ]
    parts.append("\n".join(
        f"- [{subsets_by_slug[s]['title']}](#{s})" for s in SUBSET_ORDER
    ) + "\n")

    for slug in SUBSET_ORDER:
        parts.append(render_subset(
            subsets_by_slug[slug], resolved[slug], notes_by_slug[slug],
            candidates.get(slug), res_index,
        ))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    return None


if __name__ == "__main__":
    lib.main_wrapper(main)()
