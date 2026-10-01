#!/usr/bin/env python3
"""Partition the Connected Care branch into Alex's and Yuri's stories.

Subset:  connected-care-journeys
Type:    Declared (Alex's Story) / Declared-pending (Yuri's Story)
Task:    4.4

Contract
--------
Connected Care entities are NOT on the default branch. They live under
au-fhir-test-data-set/connected-care/ on the connected-care branch, read via
git rather than the working tree (D6). lib.resolve_connected_care_ref finds
the ref, preferring upstream/connected-care.

Verified: 153 files on the branch (150 .json + 2 markdown docs + 1 PDF),
including Patient-thompson-alex.json and Patient-petrov-yuri.json.

Partition rule
--------------
Alex's Story is DECLARED. Each of its 8 care-step sections in
"Alex Story Data Set.md" has a "### FHIR Resources – <step>" table with a
Status column ("Generated" / "Not yet generated") and, for generated
resources, a markdown link `[Type-id.json](Type-id.json)`. That link is the
membership claim.

Verified: 88 distinct files linked, ALL 88 present on the branch (0 broken
links). One row is `*Unresolved*` — a narrative element with no resource
mapped — correctly excluded since it carries no link.

Yuri's Story is DECLARED IN PRINCIPLE, but its source document does not exist
yet. Every branch file NOT claimed by Alex's Story (150 - 88 = 62) is
attributed to Yuri's Story as a PROVISIONAL remainder. That status must
survive into the output — spec scenario "The provisional Yuri's Story
attribution is marked as such".

The shared-infrastructure question, made concrete
---------------------------------------------------
Measured: 56 of the 62 remainder files are Organization, Location,
Practitioner, PractitionerRole or HealthcareService — infrastructure, not
narrative content specific to one patient. This is exactly the ambiguity
design.md's Open Questions names: such entities may serve both stories, and
the remainder rule assigns them to Yuri only for lack of a better rule. Each
remainder entity is tagged `likely_shared` when its type is in that
infrastructure set, so the question stays visible rather than silently
decided.

Output
------
members            Alex's Story entities, with their care-step
needs_confirmation empty — the Yuri remainder is provisional, not a
                   yes/no candidate awaiting a decision
evidence           per entity: claimed-by-Alex-doc vs remainder; likely-shared
                   flag for infrastructure-typed remainder entities; the one
                   unresolved narrative row
source_revision    the connected-care ref and commit read
notes              the provisional-attribution caveat and its blocker
"""

from __future__ import annotations

import re
import subprocess

import lib

DOC_PATH = "au-fhir-test-data-set/connected-care/Alex Story Data Set.md"
CONNECTED_CARE_PREFIX = "au-fhir-test-data-set/connected-care/"

STEP_RE = re.compile(r"^### FHIR Resources\s*[-–]\s*(.+)$", re.MULTILINE)
ROW_RE = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$",
    re.MULTILINE,
)
LINK_RE = re.compile(r"\[([A-Za-z]+-[A-Za-z0-9\-.]+)\.json\]\(([^)]+)\)")

# Entity types where "belongs to Yuri" is a remainder-rule guess rather than a
# claim: shared infrastructure is plausibly used by any story on the branch.
INFRASTRUCTURE_TYPES = frozenset({
    "Organization", "Location", "Practitioner", "PractitionerRole",
    "HealthcareService",
})


def git_show(ref: str, path: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(lib.REPO_ROOT), "show", f"{ref}:{path}"],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise lib.PreconditionError(
            f"git show {ref}:{path} failed: {result.stderr.strip()}"
        )
    return result.stdout


def list_branch_files(ref: str) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(lib.REPO_ROOT), "ls-tree", "-r", "--name-only",
         ref, CONNECTED_CARE_PREFIX],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise lib.PreconditionError(
            f"git ls-tree {ref} {CONNECTED_CARE_PREFIX} failed: "
            f"{result.stderr.strip()}"
        )
    return [p for p in result.stdout.splitlines() if p.strip()]


def parse_alex_story(doc_text: str) -> tuple[dict[str, dict], list[dict]]:
    """Return (basename -> {care_step, description, documented_label}, unresolved rows).

    Splits the document at each "### FHIR Resources – <step>" heading and
    reads the four-column table under it. A row's Resource Type column being
    exactly "*Unresolved*" (no resource identified for a narrative element)
    is recorded separately rather than treated as a claim.

    The Resource Type column is NOT used to determine the entity's actual FHIR
    resourceType or id — it is free text ("Bundle (AU Patient Summary)",
    "Composition (Episode of Care Summary)"), kept only as a human-readable
    label. Type and id are derived from the linked filename instead, which
    follows the {ResourceType}-{id}.json convention.
    """
    step_headings = list(STEP_RE.finditer(doc_text))
    claims: dict[str, dict] = {}
    unresolved: list[dict] = []

    for i, heading in enumerate(step_headings):
        step_name = heading.group(1).strip()
        start = heading.end()
        end = step_headings[i + 1].start() if i + 1 < len(step_headings) else len(doc_text)
        section = doc_text[start:end]

        for row in ROW_RE.finditer(section):
            resource_type, description, status, reference = row.groups()
            if resource_type in ("Resource Type", "---"):
                continue
            if resource_type == "*Unresolved*":
                unresolved.append({"care_step": step_name,
                                   "description": description.strip()})
                continue
            link = LINK_RE.search(reference)
            if not link:
                continue  # "Not yet generated" rows have "—", no link
            basename = f"{link.group(1)}.json"
            claims[basename] = {"care_step": step_name,
                                "description": description.strip(),
                                "documented_label": resource_type.strip()}
    return claims, unresolved


def main():
    info = lib.check_preconditions(needs_connected_care=True)
    ref = info["connected_care_ref"]

    doc_text = git_show(ref, DOC_PATH)
    claims, unresolved = parse_alex_story(doc_text)

    branch_files = list_branch_files(ref)
    branch_json = {p.rsplit("/", 1)[-1]: p for p in branch_files
                  if p.endswith(".json")}

    members, broken_links = [], []
    for basename, claim in sorted(claims.items()):
        path = branch_json.get(basename)
        if path is None:
            broken_links.append(basename)
            continue
        # {ResourceType}-{id}.json — the filename convention, not the doc's
        # free-text label (see parse_alex_story docstring).
        rtype, _, rest = basename[:-5].partition("-")
        members.append(lib.member(
            rest, resource_type=rtype, path=path,
            why=f"claimed by Alex's Story, step {claim['care_step']!r}",
            story="alex", care_step=claim["care_step"],
            description=claim["description"],
            documented_label=claim["documented_label"],
        ))

    remainder = sorted(set(branch_json) - set(claims))
    yuri_members = []
    for basename in remainder:
        path = branch_json[basename]
        rtype = basename.split("-", 1)[0]
        rid = basename[len(rtype) + 1:-5]
        yuri_members.append(lib.member(
            rid, resource_type=rtype, path=path,
            why="not claimed by Alex's Story; provisional remainder",
            story="yuri", provisional=True,
            likely_shared=(rtype in INFRASTRUCTURE_TYPES),
        ))

    # Subset identification covers administrative entities only (lib). Applied
    # BEFORE the counts below so notes and evidence describe the same set.
    members, dropped_alex = lib.filter_administrative(members)
    yuri_members, dropped_yuri = lib.filter_administrative(yuri_members)
    dropped_nonadmin = dict(dropped_alex)
    for t, n in dropped_yuri.items():
        dropped_nonadmin[t] = dropped_nonadmin.get(t, 0) + n

    shared_count = sum(1 for m in yuri_members if m["likely_shared"])

    notes = [
        f"Alex's Story: {len(members)} entities claimed by "
        f"'{DOC_PATH.rsplit('/', 1)[-1]}', all resolved on {ref}.",
        f"Yuri's Story: {len(yuri_members)} entities attributed by REMAINDER "
        "only — no source document exists for Yuri's Story yet. This "
        "attribution is provisional, not confirmed.",
        f"{shared_count} of the {len(yuri_members)} remainder entities are "
        "infrastructure types (Organization, Location, Practitioner, "
        "PractitionerRole, HealthcareService) that may plausibly serve both "
        "stories — see design.md Open Questions 'Connected Care shared "
        "infrastructure'. Tagged likely_shared rather than resolved here.",
    ]
    if unresolved:
        notes.append(
            f"{len(unresolved)} narrative element(s) in Alex's Story have no "
            "resource mapped (marked *Unresolved* in the document)."
        )
    if broken_links:
        notes.append(
            "Alex's Story links a file not present on the branch: "
            + ", ".join(broken_links)
        )
    admin_note = lib.administrative_note(dropped_nonadmin)
    if admin_note:
        notes.append(admin_note)

    return lib.emit(
        "connected-care-journeys",
        members=members + yuri_members,
        source_revision=info["connected_care_revision"],
        evidence={
            "ref": ref,
            "doc_path": DOC_PATH,
            "counts": {
                "alex_story": len(members),
                "yuri_story_provisional": len(yuri_members),
                "yuri_likely_shared_infrastructure": shared_count,
                "unresolved_narrative_rows": len(unresolved),
                "broken_links": len(broken_links),
            },
            "non_administrative_excluded": dropped_nonadmin,
            "unresolved_narrative_rows": unresolved,
            "broken_links": broken_links,
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
