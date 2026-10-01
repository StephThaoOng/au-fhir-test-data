#!/usr/bin/env python3
"""Read the Inferno default patient list and report drift.

Subset:  inferno-default-patients
Type:    Declared
Task:    3.2

Contract
--------
Reads the default patient id list from hl7au/inferno_suite_generator at its
CURRENT revision (not a pin — design.md D11), compares it against the
transcribed `members` in subsets.yaml, and reports any difference.

Drift is the point of this script. The transcribed list is "what we believe";
the source at its current revision is "what is true now". A difference is
reported to the operator and NOT silently overwritten — the spec scenario
"Drift from the Inferno source is surfaced" leaves the decision to a human.

Also records the revision actually read, so a later drift report can name what
changed (D11).

Source
------
hl7au/inferno_suite_generator, branch main,
lib/inferno_suite_generator/utils/helpers.rb,
method `default_patient_ids_string`.

Matched on the METHOD NAME, not line numbers: the transcription noted lines
217-219, and they happen to still be correct, but they will move.

Network
-------
Read via the GitHub API using the `gh` CLI, which authenticates from the user's
existing login. Plain git access to github.com has been observed to fail
intermittently in this environment while `gh api` succeeds, so this path is
deliberate rather than incidental.

Output
------
members            the ids as read from the source
needs_confirmation empty — drift is reported via `notes`, not as a candidate
evidence           transcribed vs read lists, and the diff between them
source_revision    the commit sha actually read
notes              a drift message when the two lists differ
"""

import base64
import json
import re
import subprocess

import lib

REPO = "hl7au/inferno_suite_generator"
BRANCH = "main"
SOURCE_PATH = "lib/inferno_suite_generator/utils/helpers.rb"
METHOD = "default_patient_ids_string"

# The method body is a single double-quoted string of comma-separated ids.
METHOD_RE = re.compile(
    rf"def\s+self\.{METHOD}\s*\n\s*\"([^\"]*)\"", re.MULTILINE
)


def _gh(*args: str) -> str:
    result = subprocess.run(
        ["gh", *args], capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0:
        raise lib.PreconditionError(
            f"gh {' '.join(args)} failed: {result.stderr.strip()}\n"
            "Fix: check network access to github.com, and that `gh auth status` "
            "reports a logged-in account."
        )
    return result.stdout


def fetch_source() -> tuple[str, str]:
    """Return (file_text, commit_sha) for the source at its current revision."""
    sha = _gh("api", f"repos/{REPO}/commits/{BRANCH}", "--jq", ".sha").strip()
    payload = _gh("api", f"repos/{REPO}/contents/{SOURCE_PATH}?ref={BRANCH}")
    content = json.loads(payload)["content"]
    return base64.b64decode(content).decode("utf-8"), sha


def parse_ids(text: str) -> list[str]:
    match = METHOD_RE.search(text)
    if not match:
        raise lib.PreconditionError(
            f"Could not find `{METHOD}` in {SOURCE_PATH}.\n"
            "The method may have been renamed or restructured upstream — this "
            "is itself drift, and needs a human to look rather than a silent "
            "empty result."
        )
    return [i.strip() for i in match.group(1).split(",") if i.strip()]


def main():
    lib.check_preconditions()

    text, sha = fetch_source()
    read_ids = parse_ids(text)

    subset = lib.get_subset("inferno-default-patients")
    transcribed = list(subset["members"])

    added = [i for i in read_ids if i not in transcribed]
    removed = [i for i in transcribed if i not in read_ids]
    reordered = (not added and not removed and read_ids != transcribed)

    notes = []
    if added or removed:
        notes.append(
            "DRIFT: the Inferno source no longer matches the transcribed list. "
            "Not overwritten — a maintainer must decide."
        )
        if added:
            notes.append(f"  In source but not transcribed: {', '.join(added)}")
        if removed:
            notes.append(f"  Transcribed but not in source: {', '.join(removed)}")
    elif reordered:
        notes.append(
            "Order differs from the transcribed list; membership is identical. "
            "Not treated as drift."
        )
    else:
        notes.append("No drift: source matches the transcribed list.")

    # Resolve each id to a file so the wiki can link entities, and so a patient
    # named upstream but absent here is caught rather than silently listed.
    index = lib.build_reference_index()
    members, missing = [], []
    for pid in read_ids:
        entry = index["resources"].get(f"Patient/{pid}")
        if entry is None:
            missing.append(pid)
            members.append(lib.member(
                pid, resource_type="Patient",
                why="named by the Inferno source but not found in the data set",
            ))
            continue
        members.append(lib.member(
            pid, resource_type="Patient", path=entry["path"],
            why=f"named by {METHOD} in {REPO}",
        ))
    if missing:
        notes.append(
            "Named upstream but absent from the data set: " + ", ".join(missing)
        )

    return lib.emit(
        "inferno-default-patients",
        members=members,
        source_revision=sha,
        evidence={
            "repo": REPO,
            "branch": BRANCH,
            "source_path": SOURCE_PATH,
            "method": METHOD,
            "read_from_source": read_ids,
            "transcribed_in_facts_file": transcribed,
            "added_upstream": added,
            "removed_upstream": removed,
            "order_differs_only": reordered,
            "missing_from_data_set": missing,
        },
        notes=notes,
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
