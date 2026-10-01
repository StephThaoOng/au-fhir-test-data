#!/usr/bin/env python3
"""Seed scenario groupings from the historical directory structure — ONCE.

Subset:  scenario-groups
Type:    Curated (after seeding)
Task:    4.3

Contract — read this before running
-----------------------------------
This is a ONE-TIME seed extraction, not a recurring derivation (design.md D5).

It reads the au-core/consumer-journey/ directory structure at the pinned ref
recorded in `seed_source` (e2c24ca1eceac3e165df4a5fab7744af1146676f — 7 scenario
folders, 418 distinct files) and produces the resulting groupings. After
seeding, subsets.yaml is authoritative and this script should not be re-run:
the pinned ref is kept for traceability only.

Because subsets.yaml is hand-authored and never machine-written (D12), this
script does NOT write into it directly. It emits the seed as candidate JSON,
same as every other script, and the operator applies it once by hand. The
refuse-if-already-seeded guard checks the CURRENT `members` in subsets.yaml,
so re-running after that hand-edit is a no-op rather than a silent overwrite.

Why the ref rather than the working tree
----------------------------------------
Those directories no longer exist on the default branch — removed in a71f225 /
e2c24ca. The ref is a historical snapshot, not a live source. All 418 files in
the snapshot still exist at HEAD (verified), so the seed maps cleanly onto
current filenames despite the directories themselves being gone.

Scenario folders at the pinned ref, and the slugs slugify() actually produces
(verified by running the script — do not hand-guess these, "&" expands to
"and" and trailing parentheticals survive):
  CCM scenario - Drafted                       -> ccm-scenario-drafted                       44
  CCM_Aged care scenario - Future              -> ccm-aged-care-scenario-future               49
  FIrst nations scenario                       -> first-nations-scenario                      51
  Family scenario w baby (2 month old)         -> family-scenario-w-baby-2-month-old          98
  Paeds scenario (5yo)                         -> paeds-scenario-5yo                          56
  Rural & remote scenario                      -> rural-and-remote-scenario                   74
  Young adult_adolescent scenario (19-20 yo)   -> young-adult-adolescent-scenario-19-20-yo    46

Slugging lowercases, replaces "&" with "and", collapses non-alphanumeric runs
to a single hyphen, and strips leading/trailing hyphens. The original folder
name (including its typo "FIrst" and its parenthetical) is kept as `title` so
it stays traceable even though the slug normalises it away.

A file may appear under more than one scenario folder (verified: some files
recur across scenarios in the snapshot); membership records every scenario
slug a file appears under rather than assuming one-to-one.

Output
------
members            empty — this script never claims membership on its own
needs_confirmation one candidate per scenario: its slug, title and file list,
                   for the operator to apply to subsets.yaml once
evidence           the guard's finding (already-seeded or not), and per-scenario
                   file counts at the pinned ref vs. how many resolve at HEAD
notes              the one-time-only warning, and the refusal reason if guarded
"""

from __future__ import annotations

import re
import subprocess
from collections import defaultdict

import lib

SEED_REF = "e2c24ca1eceac3e165df4a5fab7744af1146676f"
CONSUMER_JOURNEY_PREFIX = "au-fhir-test-data-set/au-core/consumer-journey/"


def slugify(name: str) -> str:
    s = name.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def list_seed_tree() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(lib.REPO_ROOT), "ls-tree", "-r", "--name-only", SEED_REF],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise lib.PreconditionError(
            f"Could not read tree at {SEED_REF}: {result.stderr.strip()}\n"
            "Fix: git fetch --tags (or ensure the commit is reachable)."
        )
    return result.stdout.splitlines()


def already_seeded() -> bool:
    subset = lib.get_subset("scenario-groups")
    members = subset.get("members")
    # The placeholder in subsets.yaml is `members: {}` (empty mapping).
    return bool(members)


def main():
    lib.check_preconditions(needs_git_history=True)

    if already_seeded():
        return lib.emit(
            "scenario-groups",
            evidence={"guard": "refused", "reason": "members already populated"},
            notes=[
                "REFUSED: scenario-groups.members in subsets.yaml is already "
                "populated. This is a one-time seed (D5) — re-running would "
                "overwrite subsequent curation. Nothing was done."
            ],
        )

    paths = [p for p in list_seed_tree() if p.startswith(CONSUMER_JOURNEY_PREFIX)]
    if not paths:
        raise lib.PreconditionError(
            f"No files under {CONSUMER_JOURNEY_PREFIX} at {SEED_REF} — the seed "
            "ref may be wrong, or the tree layout has changed."
        )

    by_scenario: dict[str, dict] = {}
    for p in paths:
        rest = p[len(CONSUMER_JOURNEY_PREFIX):]
        scenario_folder, _, basename = rest.partition("/")
        if not basename:
            continue
        slug = slugify(scenario_folder)
        by_scenario.setdefault(slug, {"title": scenario_folder, "files": set()})
        by_scenario[slug]["files"].add(basename)

    index = lib.build_reference_index()
    by_basename = {}
    for entry in index["resources"].values():
        by_basename.setdefault(entry["path"].rsplit("/", 1)[-1], []).append(entry)

    candidates = []
    dropped_nonadmin: dict[str, int] = {}
    total_seed_files = total_resolved = 0
    for slug, info in sorted(by_scenario.items()):
        members = []
        unresolved = []
        for basename in sorted(info["files"]):
            hits = by_basename.get(basename)
            if not hits:
                unresolved.append(basename)
                continue
            for entry in hits:
                members.append(lib.member(
                    entry["id"], resource_type=entry["resource_type"],
                    path=entry["path"], why=f"seeded from {info['title']!r} at {SEED_REF[:8]}",
                ))
        # Subset identification covers administrative entities only (lib).
        members, dropped = lib.filter_administrative(members)
        for t, n in dropped.items():
            dropped_nonadmin[t] = dropped_nonadmin.get(t, 0) + n
        total_seed_files += len(info["files"])
        total_resolved += len(members)
        candidates.append({
            "slug": slug,
            "title": info["title"],
            "members": members,
            "seed_file_count": len(info["files"]),
            "resolved_count": len(members),
            "unresolved": unresolved,
        })

    notes = [
        "ONE-TIME SEED. Apply this once to scenario-groups.members in "
        "subsets.yaml by hand (D12: subsets.yaml is never machine-written), "
        "then do not re-run — subsequent maintenance is by curation (D5).",
        f"{len(by_scenario)} scenarios, {total_seed_files} file references at "
        f"the seed ref, {total_resolved} resolved to a current file.",
    ]
    admin_note = lib.administrative_note(dropped_nonadmin)
    if admin_note:
        notes.append(admin_note)

    unresolved_total = sum(len(c["unresolved"]) for c in candidates)
    if unresolved_total:
        notes.append(
            f"{unresolved_total} seed file references did not resolve at HEAD "
            "— listed per scenario in needs_confirmation."
        )

    return lib.emit(
        "scenario-groups",
        needs_confirmation=[{"id": c["slug"], **c} for c in candidates],
        source_revision=SEED_REF,
        evidence={
            "guard": "not previously seeded",
            "seed_ref": SEED_REF,
            "non_administrative_excluded": dropped_nonadmin,
            "scenario_count": len(by_scenario),
            "total_seed_file_references": total_seed_files,
            "total_resolved": total_resolved,
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
