#!/usr/bin/env python3
"""Attribute entities to contributing organisations by commit authorship.

Subset:  community-contributions
Type:    Derived + Curated
Task:    4.1

Contract
--------
Finds the commit that introduced each resource file still present in the data
set, and attributes the entity to an organisation when the author or committer
email is on a recognised domain (`derivation_inputs.domains` in subsets.yaml).
Merges in `human_attested` — entities a human has independently stated belong
to an organisation's contributions.

The scan walks HEAD in a single pass rather than running `git log` per file:
41 add-commits cover 1,716 file additions, so the one-pass form completes in
about 0.1s where per-file would take minutes.

Where a file was added more than once (added, deleted, re-added), the EARLIEST
add is taken as the origin — that is the contribution, not a later reinstate.

`human_attested` is a cross-check, not an override
---------------------------------------------------
Attribution is best-effort and known to under-report. A contributor using a
personal email address, or a merge that did not preserve original authorship
(a maintainer copying files in by hand), is invisible to it. Requires a full
clone: on a shallow one the add-commits are simply absent and the scan reports
nothing, hence lib.require_full_clone.

The generated section must state this limitation rather than implying the list
is exhaustive — spec scenario "The limits of git-based attribution are stated".

Verified against current history: one commit (5727b6b, "Examples of HSP-O and
HAE organisations") by richard.townleyoneill@digitalhealth.gov.au added exactly
the 12 attested Organizations. Scan and attestation AGREE — the attested list
is not compensating for a gap, it is independently confirming the derivation.

That agreement is the point. Because the two are derived independently, a
future DISagreement is informative: if one of these files is re-added in a way
that loses its original authorship, the scan stops finding it and this script
reports it as attested-only rather than the entity silently vanishing from the
subset.

Why this subset is not reserved
-------------------------------
Attribution records origin only. It places no constraint on adding to or
modifying the contributed entities or their linked resources (D10).

Output
------
members            entities attributed to a recognised organisation
needs_confirmation empty — a domain match is definitive, and the attested
                   entries are already human decisions
evidence           per entity the introducing commit and its author/committer;
                   counts; and whether the cross-check agreed
"""

from __future__ import annotations

import subprocess
from collections import defaultdict

import lib

DATA_SET_PATHSPEC = "au-fhir-test-data-set/"


def scan_add_events() -> dict[str, dict]:
    """Map repo-relative path -> the earliest commit that added it."""
    result = subprocess.run(
        ["git", "-C", str(lib.REPO_ROOT), "log", "HEAD",
         "--diff-filter=A", "--name-only",
         "--format=C|%H|%ae|%ce|%aI|%s", "--", DATA_SET_PATHSPEC],
        capture_output=True, text=True, timeout=300,
    )
    if result.returncode != 0:
        raise lib.PreconditionError(f"git log failed: {result.stderr.strip()}")

    adds: dict[str, dict] = {}
    current = None
    for line in result.stdout.splitlines():
        if line.startswith("C|"):
            _, sha, author, committer, when, subject = line.split("|", 5)
            current = {"commit": sha, "author_email": author,
                       "committer_email": committer, "date": when,
                       "subject": subject}
        elif line.strip() and current:
            # git log walks newest first, so a later iteration is an EARLIER
            # commit: overwrite so the earliest add wins.
            adds[line.strip()] = current
    return adds


def main():
    lib.check_preconditions(needs_git_history=True)

    subset = lib.get_subset("community-contributions")
    domains = {
        d["domain"].lower(): d["organisation"]
        for d in subset["derivation_inputs"]["domains"]
    }
    attested = subset.get("human_attested", []) or []

    adds = scan_add_events()
    index = lib.build_reference_index()

    # path -> entity, for the files currently present in the data set
    by_path = {e["path"]: e for e in index["resources"].values()}

    members: dict[str, dict] = {}
    per_org = defaultdict(list)
    unattributed = 0

    for path, entity in sorted(by_path.items()):
        event = adds.get(path)
        if event is None:
            unattributed += 1
            continue
        emails = [event["author_email"].lower(), event["committer_email"].lower()]
        org = next(
            (domains[e.split("@")[-1]] for e in emails
             if e.split("@")[-1] in domains),
            None,
        )
        if org is None:
            unattributed += 1
            continue
        members[entity["id"]] = lib.member(
            entity["id"],
            resource_type=entity["resource_type"],
            path=path,
            why=f"introduced by {event['author_email']} in {event['commit'][:8]}",
            organisation=org,
            commit=event["commit"],
            commit_subject=event["subject"],
            attribution="commit authorship",
        )
        per_org[org].append(entity["id"])

    # Merge the human-attested list. These are NOT overrides — they are an
    # independent statement of the same claim, so agreement is the expected
    # case and DISagreement is the signal worth reporting.
    attested_only, attested_agreed = [], []
    for record in attested:
        org = record["organisation"]
        for filename in record.get("members", []):
            entity = next(
                (e for e in index["resources"].values()
                 if e["path"].endswith(f"/{filename}.json")),
                None,
            )
            if entity is None:
                continue
            if entity["id"] in members:
                attested_agreed.append(entity["id"])
                members[entity["id"]]["attribution"] = (
                    "commit authorship, independently attested")
                members[entity["id"]]["attester"] = record.get("attester")
                members[entity["id"]]["confirmed_on"] = record.get("confirmed_on")
                continue
            # The scan did NOT find this one. Either authorship was lost, or
            # the contributor used an unrecognised address — the case the
            # attested list exists to catch.
            attested_only.append(entity["id"])
            members[entity["id"]] = lib.member(
                entity["id"],
                resource_type=entity["resource_type"],
                path=entity["path"],
                why="human-attested; NOT found by the authorship scan",
                organisation=org,
                attribution="human-attested only",
                attester=record.get("attester"),
                confirmed_on=record.get("confirmed_on"),
            )
            per_org[org].append(entity["id"])

    notes = [
        f"{len(members)} entities attributed across "
        f"{len(per_org)} organisation(s).",
        "Attribution derives from the commit that introduced each file and may "
        "under-report: a contributor using a personal email address, or a merge "
        "that did not preserve original authorship, is not detected. The list "
        "is not exhaustive.",
        f"{unattributed} files in the data set carry no recognised-domain "
        "attribution; most are project-internal contributions.",
    ]
    if attested_agreed and not attested_only:
        notes.append(
            f"Cross-check passed: all {len(attested_agreed)} human-attested "
            "entities were also found independently by the authorship scan."
        )
    elif attested_agreed:
        notes.append(
            f"{len(attested_agreed)} of {len(attested_agreed) + len(attested_only)} "
            "human-attested entities were also found by the authorship scan."
        )
    if attested_only:
        notes.append(
            f"CROSS-CHECK DISAGREEMENT: {len(attested_only)} human-attested "
            "entities were NOT found by the authorship scan — their original "
            "commit authorship may have been lost. "
            + ", ".join(sorted(attested_only))
        )

    # Subset identification covers administrative entities only (lib).
    member_list, dropped_nonadmin = lib.filter_administrative(list(members.values()))
    admin_note = lib.administrative_note(dropped_nonadmin)
    if admin_note:
        notes.append(admin_note)

    return lib.emit(
        "community-contributions",
        members=member_list,
        evidence={
            "non_administrative_excluded": dropped_nonadmin,
            "recognised_domains": domains,
            "attributed_by_organisation": {k: sorted(v) for k, v in per_org.items()},
            "counts": {
                "attributed": len(members),
                "unattributed_files": unattributed,
                "attested_confirmed_by_scan": len(attested_agreed),
                "attested_only": len(attested_only),
            },
            "attested_only_entities": sorted(attested_only),
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
