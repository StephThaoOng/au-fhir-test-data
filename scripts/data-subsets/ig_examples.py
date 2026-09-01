#!/usr/bin/env python3
"""Identify test data entities also published as IG examples.

Subsets: au-core-ig-examples, au-erequesting-ig-examples, au-ps-ig-examples
Type:    Derived
Tasks:   3.3 (AU Core + eRequesting), 3.4 (AU PS)

Contract
--------
Matches entities in the test data set against the example sets published in
three IGs under github.com/hl7au/ (constraint C2). Emits one candidate file
per subset.

IG examples are XML
-------------------
`input/examples/` holds .xml, not .json — verified across all three IGs (83, 7
and 44 files respectively, plus one .txt in eRequesting). Anything globbing for
*.json here silently matches nothing and reports an empty subset.

Matching rule — the part that is easy to get wrong
--------------------------------------------------
Match on resource IDENTITY, never on content. IG examples are published with
some Services Australia identifier data intentionally stripped, so an entity
and its IG-example counterpart legitimately differ in content while being the
same entity. Two identity signals, tried in order:

  1. Resource id      Type/id equality.
  2. Business identifier   Type + system|value.

The fallback is not theoretical. Measured against the current IGs, resource id
alone matches 76/83 AU Core examples; business identifier recovers 5 more,
including cases where the IG and the test data simply name the same entity
differently — IG `Patient/ronny-irvine` is test data `Patient/irvine-ronny-lawrence`,
and IG `Organization/murrabit-hospital` is `Organization-murrabit-public-hospital`.

Bundles need entry extraction — and not only for AU PS
------------------------------------------------------
Resource ids INSIDE a Bundle are not reliable keys: measured, zero of 190
Bundle entries across AU PS and eRequesting match the test data by id. Entries
must be matched on business identifier instead.

The tasks anticipated this for AU PS only. eRequesting also ships Bundles
(bundle-imaging-1, bundle-imaging-put-1, bundle-pathology-multitest-1), so the
extraction path runs for every IG rather than being special-cased to AU PS.

Most Bundle entries carry no business identifier at all — they are clinical
resources like Observation and Condition. The entries that do match are the
administrative ones (Patient, Practitioner, Organization, PractitionerRole),
which are exactly the scarce, governed entities this wiki exists to track.

Why these subsets are reserved
------------------------------
An entity published as an IG example cannot have its linked resources freely
added to or modified: doing so could break the IG build or its documented
example. Read-only use is unconstrained (D10).

Output (per subset)
-------------------
members            entities matched to an IG example
needs_confirmation empty — matching is deterministic
evidence           per entity the IG example file and match basis; plus counts
                   and the list of IG examples that matched nothing
source_revision    the IG commit sha read
"""

from __future__ import annotations

import json
import os
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import lib

FHIR_NS = "{http://hl7.org/fhir}"

IGS = {
    "au-core-ig-examples": ("hl7au/au-fhir-core", "master"),
    "au-erequesting-ig-examples": ("hl7au/au-fhir-erequesting", "master"),
    "au-ps-ig-examples": ("hl7au/au-fhir-ps", "master"),
}

EXAMPLES_PATH = "input/examples"


def cache_dir() -> Path:
    return lib.default_out_dir().parent / "ig-clones"


def ensure_clone(repo: str, branch: str) -> Path:
    """Shallow-clone an IG, or refresh an existing clone. Returns its path."""
    dest = cache_dir() / repo.split("/")[-1]
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--filter=blob:none",
             "--branch", branch, "--quiet",
             f"https://github.com/{repo}.git", str(dest)],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode != 0:
            raise lib.PreconditionError(
                f"Could not clone {repo}: {result.stderr.strip()}\n"
                "Fix: check network access to github.com (a VPN has been "
                "observed to block it while leaving `gh api` working)."
            )
    else:
        subprocess.run(["git", "-C", str(dest), "fetch", "--depth", "1",
                        "--quiet", "origin", branch],
                       capture_output=True, text=True, timeout=300)
        subprocess.run(["git", "-C", str(dest), "reset", "--hard", "--quiet",
                        f"origin/{branch}"],
                       capture_output=True, text=True, timeout=120)
    if not (dest / EXAMPLES_PATH).is_dir():
        raise lib.PreconditionError(f"{repo} has no {EXAMPLES_PATH}/ at {branch}")
    return dest


def head_sha(repo_path: Path) -> str:
    return subprocess.run(["git", "-C", str(repo_path), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


# --- Identity extraction ----------------------------------------------------

def xml_identifiers(element) -> set[str]:
    out = set()
    for ident in element.findall(f"{FHIR_NS}identifier"):
        system = ident.find(f"{FHIR_NS}system")
        value = ident.find(f"{FHIR_NS}value")
        if system is not None and value is not None:
            out.add(f"{system.get('value')}|{value.get('value')}")
    return out


def json_identifiers(resource: dict) -> set[str]:
    ids = resource.get("identifier")
    ids = [ids] if isinstance(ids, dict) else (ids or [])
    return {
        f"{i.get('system')}|{i.get('value')}"
        for i in ids
        if isinstance(i, dict) and i.get("system") and i.get("value")
    }


def build_test_data_index() -> tuple[dict, dict]:
    """Index the test data set by Type/id and by (Type, system|value)."""
    by_key, by_identifier = {}, {}
    for path, resource in lib.iter_resource_files():
        rtype = resource.get("resourceType")
        if not rtype:
            continue
        entry = {"id": resource.get("id"), "resource_type": rtype,
                 "path": lib.rel_path(path)}
        by_key[f"{rtype}/{resource.get('id')}"] = entry
        for ident in json_identifiers(resource):
            by_identifier.setdefault((rtype, ident), entry)
    return by_key, by_identifier


def iter_example_resources(examples_dir: Path):
    """Yield (filename, resource_type, resource_id, element, in_bundle).

    Bundles are expanded into their entries; the Bundle itself is not yielded
    as a matchable resource.
    """
    for path in sorted(examples_dir.glob("*.xml")):
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError:
            continue
        rtype = root.tag.replace(FHIR_NS, "")
        id_el = root.find(f"{FHIR_NS}id")
        rid = id_el.get("value") if id_el is not None else None

        if rtype != "Bundle":
            yield path.name, rtype, rid, root, False
            continue

        for entry in root.findall(f"{FHIR_NS}entry"):
            resource = entry.find(f"{FHIR_NS}resource")
            if resource is None:
                continue
            for child in resource:  # a Bundle entry wraps exactly one resource
                child_type = child.tag.replace(FHIR_NS, "")
                child_id_el = child.find(f"{FHIR_NS}id")
                child_id = (child_id_el.get("value")
                            if child_id_el is not None else None)
                yield path.name, child_type, child_id, child, True
                break


# --- Derivation -------------------------------------------------------------

def derive(slug: str, repo: str, branch: str, by_key: dict,
           by_identifier: dict) -> Path:
    repo_path = ensure_clone(repo, branch)
    sha = head_sha(repo_path)
    examples_dir = repo_path / EXAMPLES_PATH

    members, seen = [], set()
    unmatched = []
    counts = {"by_id": 0, "by_identifier": 0, "unmatched": 0,
              "examples_scanned": 0, "bundle_entries": 0}

    for filename, rtype, rid, element, in_bundle in iter_example_resources(examples_dir):
        counts["examples_scanned"] += 1
        if in_bundle:
            counts["bundle_entries"] += 1

        entry, basis = None, None
        # Resource ids inside a Bundle are not reliable keys (measured: zero
        # of 190 match), so identifier is the only signal for those.
        if not in_bundle:
            entry = by_key.get(f"{rtype}/{rid}")
            basis = "resource id" if entry else None
        if entry is None:
            # sorted(): a resource may carry several identifiers (an IHI and a
            # Medicare number, say). Iterating the set directly makes the
            # recorded match basis vary between runs on identical input.
            for ident in sorted(xml_identifiers(element)):
                entry = by_identifier.get((rtype, ident))
                if entry:
                    basis = f"business identifier ({ident})"
                    break

        if entry is None:
            counts["unmatched"] += 1
            unmatched.append({"example": filename, "resource": f"{rtype}/{rid}",
                              "in_bundle": in_bundle})
            continue

        counts["by_id" if basis == "resource id" else "by_identifier"] += 1

        key = f"{entry['resource_type']}/{entry['id']}"
        if key in seen:
            continue
        seen.add(key)
        members.append(lib.member(
            entry["id"],
            resource_type=entry["resource_type"],
            path=entry["path"],
            why=f"published as an IG example in {filename} (matched on {basis})",
            ig_example_file=filename,
            match_basis=basis.split(" (")[0],
            from_bundle_entry=in_bundle,
        ))

    members, dropped_nonadmin = lib.filter_administrative(members)

    notes = [
        f"{len(members)} distinct administrative entities are published as "
        f"examples in {repo}.",
    ]
    admin_note = lib.administrative_note(dropped_nonadmin)
    if admin_note:
        notes.append(admin_note)
    if counts["bundle_entries"]:
        notes.append(
            f"{counts['bundle_entries']} of the resources scanned came from "
            "Bundle entries, matched on business identifier only — ids inside "
            "a Bundle are not reliable keys."
        )
    if unmatched:
        notes.append(
            f"{len(unmatched)} IG example resources matched nothing in the test "
            "data set; they may be IG-only examples. Listed under evidence."
        )

    return lib.emit(
        slug,
        members=members,
        source_revision=sha,
        evidence={
            "repo": repo,
            "branch": branch,
            "examples_path": EXAMPLES_PATH,
            "counts": counts,
            "non_administrative_excluded": dropped_nonadmin,
            "unmatched_ig_examples": unmatched,
        },
        notes=notes,
    )


def main():
    lib.check_preconditions()
    by_key, by_identifier = build_test_data_index()
    written = [derive(slug, repo, branch, by_key, by_identifier)
               for slug, (repo, branch) in IGS.items()]
    for path in written:
        print(f"Wrote {path}")
    return None  # paths already reported


if __name__ == "__main__":
    lib.main_wrapper(main)()
