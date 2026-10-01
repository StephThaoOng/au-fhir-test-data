#!/usr/bin/env python3
"""Identify missing and suppressed data example instances.

Subset:  missing-suppressed-data
Type:    Derived + Curated
Task:    4.2

Contract
--------
Two inputs, combined:

1. The documented cases — the markdown table in
   docs/MissingAndSuppressedData_TestData.md, listed under
   `derivation_inputs.documented_sources`. These are authoritative and become
   members directly. Verified: all 11 documented files resolve at HEAD.

   The table's prose points at a `direct-fhir-test-resources/` directory that
   no longer exists, so files are located by NAME across the data set rather
   than by the path the document implies.

2. A keyword scan over resource ids, using `derivation_inputs.keyword_scan`.

A keyword hit is a CANDIDATE, never a member. The keywords are suggestive, not
conclusive: "cancelled" matches genuine cancelled orders, and "unknown" matches
resources using an unknown-value code for ordinary reasons. Hits are emitted as
`needs_confirmation` so a human decides — spec scenario "A newly matching
instance is queued for confirmation".

Candidates already confirmed or rejected are filtered out via
lib.partition_candidates, so a rerun over an unchanged tree asks nothing.

EXEMPT from the administrative-only constraint
-----------------------------------------------
Every other subset is restricted to administrative resource types
(lib.ADMINISTRATIVE_RESOURCE_TYPES), because those are the scarce entities that
carry governance considerations. This subset is the one exemption, and does NOT
call lib.filter_administrative.

The reason: these instances demonstrate the correct REPRESENTATION of missing
or suppressed data — a Data Absent Reason extension, an `unknown` code, a
suppressed valueQuantity. They are not defects, and that property attaches to
an Observation exactly as it does to a Patient. It is unrelated to the scarcity
argument that motivates the administrative-only rule.

Filtering here would drop 7 of the 11 documented cases — every Observation,
including pathresult-missing-effective and pathresult-suppressed-valueQuantity
— leaving a subset that no longer means what its name says.

Why this subset is reserved
---------------------------
These instances are deliberately shaped to demonstrate a specific missing- or
suppressed-data case. Adding to or modifying their linked resources risks
misrepresenting that case. Reading and testing against them is unconstrained.

Output
------
members            documented cases, plus previously confirmed keyword hits
needs_confirmation undecided keyword hits
evidence           per candidate the keyword matched; counts; and any
                   documented file that could not be located
"""

from __future__ import annotations

import re

import lib

DOC_PATH = "docs/MissingAndSuppressedData_TestData.md"


def parse_documented_cases(index: dict) -> tuple[list[dict], list[str]]:
    """Read the markdown table. Returns (members, unlocated filenames)."""
    path = lib.REPO_ROOT / DOC_PATH
    if not path.exists():
        raise lib.PreconditionError(
            f"{DOC_PATH} not found — it is the authoritative source for this "
            "subset's documented cases."
        )

    by_path = {e["path"]: e for e in index["resources"].values()}
    members, unlocated = [], []

    for line in path.read_text(encoding="utf-8").splitlines():
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.split("|")]
        if not cells or not cells[0].endswith(".json"):
            continue
        filename, resource_id, test_case = cells[0], cells[1], (
            cells[2] if len(cells) > 2 else "")

        entry = next(
            (e for p, e in by_path.items() if p.endswith(f"/{filename}")), None)
        if entry is None:
            unlocated.append(filename)
            continue
        members.append(lib.member(
            entry["id"],
            resource_type=entry["resource_type"],
            path=entry["path"],
            why=f"documented case in {DOC_PATH}",
            test_case=test_case,
            documented=True,
        ))
    return members, unlocated


def scan_keywords(index: dict, keywords: list[str],
                  already: set[str]) -> list[dict]:
    """Resource ids containing a keyword, excluding documented members."""
    patterns = [(k, re.compile(re.escape(k), re.IGNORECASE)) for k in keywords]
    hits = []
    for key, entry in sorted(index["resources"].items()):
        rid = entry["id"] or ""
        if key in already:
            continue
        matched = [k for k, pat in patterns if pat.search(rid)]
        if matched:
            hits.append({
                "members": [lib.member(
                    entry["id"],
                    resource_type=entry["resource_type"],
                    path=entry["path"],
                    why=f"resource id contains {', '.join(matched)}",
                    keywords=matched,
                )],
                "keywords": matched,
            })
    return hits


def main():
    lib.check_preconditions()

    subset = lib.get_subset("missing-suppressed-data")
    keywords = subset["derivation_inputs"]["keyword_scan"]
    index = lib.build_reference_index()

    documented, unlocated = parse_documented_cases(index)
    documented_keys = {
        f"{m['resource_type']}/{m['id']}" for m in documented
    }

    candidates = scan_keywords(index, keywords, documented_keys)
    confirmed, rejected, flagged, undecided = lib.partition_candidates(
        "missing-suppressed-data", candidates)

    members = list(documented)
    for cand in confirmed:
        for m in cand["members"]:
            members.append({**m, "documented": False,
                            "attester": cand.get("attester"),
                            "confirmed_on": cand.get("confirmed_on")})

    needs = [m for cand in undecided for m in cand["members"]]

    notes = [
        f"{len(documented)} documented cases from {DOC_PATH}.",
        f"{len(confirmed)} additional instances confirmed from keyword hits; "
        f"{len(rejected)} rejected.",
    ]
    if needs:
        notes.append(
            f"{len(needs)} keyword hits await a decision. Keywords are "
            "suggestive, not conclusive — 'cancelled' matches genuine "
            "cancelled orders, and 'unknown' matches ordinary unknown-value "
            "codes."
        )
    if unlocated:
        notes.append(
            f"{len(unlocated)} documented files could not be located in the "
            "data set: " + ", ".join(unlocated)
        )

    return lib.emit(
        "missing-suppressed-data",
        members=members,
        needs_confirmation=needs,
        evidence={
            "documented_source": DOC_PATH,
            "keywords": keywords,
            "counts": {
                "documented": len(documented),
                "confirmed_keyword_hits": len(confirmed),
                "rejected_keyword_hits": len(rejected),
                "awaiting_decision": len(needs),
                "unlocated_documented_files": len(unlocated),
            },
            "unlocated_documented_files": unlocated,
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
