"""Shared helpers for the data-subsets derivation scripts.

Every script under scripts/data-subsets/ emits candidate JSON in one common
shape so the regenerate-data-subsets-wiki skill can consume them without
knowing which subset it is looking at:

    {
      "subset": "<slug>",                  # matches a slug in subsets.yaml
      "generated_at": "<ISO-8601 UTC>",
      "source_revision": "<str|null>",     # what this run actually read (D11)
      "members": [ {...}, ... ],           # entities the script is confident about
      "needs_confirmation": [ {...}, ... ],# candidates requiring a human decision
      "evidence": { ... },                 # why the script concluded what it did
      "notes": [ "...", ... ]              # anything the operator should read
    }

Members and candidates are dicts, not bare strings, so evidence can travel with
each entry:

    {"id": "baratz-toni", "resource_type": "Patient",
     "path": "au-fhir-test-data-set/au-core/Patient-baratz-toni.json",
     "why": "postcode prefix 40"}

Design references (openspec/changes/add-data-subset-identification/design.md):
  D2  scripts compute, the skill judges — nothing here prompts or decides
  D3  confirmations are persisted, so a rerun asks nothing new
  D10 reservation constrains writes, not reads
  D11 Declared sources track latest; source_revision is an output
  D12 two facts files: subsets.yaml hand-authored, confirmations.json machine-owned
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml  # PyYAML — the toolchain's only non-stdlib dependency; see
             # scripts/data-subsets/requirements.txt

# --- Repo layout ------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_SET_ROOT = REPO_ROOT / "au-fhir-test-data-set"

# Two facts files, with different owners — see D12.
#   subsets.yaml      hand-authored. Scripts READ it and never write it, so its
#                     comments and structure survive.
#   confirmations.json machine-owned decision log, written by record_confirmation.
FACTS_FILE = REPO_ROOT / "docs" / "data-subsets" / "subsets.yaml"
CONFIRMATIONS_FILE = REPO_ROOT / "docs" / "data-subsets" / "confirmations.json"

# Directories on the default branch. connected-care is deliberately absent —
# it lives on the connected-care branch and is read via git (see D6).
DATA_SET_DIRS = ("au-base", "au-core", "au-erequesting", "au-patient-summary")

CONNECTED_CARE_DIR = "au-fhir-test-data-set/connected-care"

# Administrative resource types — the only ones subset identification covers.
#
# These are the scarce entities: their key identifiers and some core attributes
# are allocated by Services Australia, and correspond to entities provisioned in
# the HI Vendor Test Environment. The instances here map those records into FHIR
# and may include some data enrichment, but generally need to stay aligned with
# the corresponding entities in that environment — so an administrative entity
# cannot simply be created or modified on demand within this project. They are
# therefore the entities that may carry governance considerations, which is what
# the wiki exists to identify and document.
#
# Clinical resources carry far less shared governance with external parties and
# can be authored more freely, so tracking their subset membership is low value.
# Where it is needed, clinical content is retrievable from the administrative
# entity by FHIR mechanisms.
#
# ONE EXEMPTION: missing-suppressed-data. Its instances demonstrate the correct
# REPRESENTATION of missing or suppressed data (a Data Absent Reason extension,
# an `unknown` code, a suppressed valueQuantity) — not a defect. That property
# attaches to an Observation exactly as it does to a Patient, and is unrelated
# to the scarcity argument above. Filtering it would drop 7 of its 11 documented
# cases and leave a subset that no longer means what its name says.
ADMINISTRATIVE_RESOURCE_TYPES = frozenset({
    "Patient", "RelatedPerson", "Practitioner", "PractitionerRole",
    "Organization", "HealthcareService", "Location", "Endpoint",
})


# Resource types that record a clinical fact or event ABOUT a patient.
#
# The test is whether new clinical content could conflict with what is already
# there — which is the question the blank-slate subset exists to answer. So:
#
#   included: clinical statements and events (conditions, observations,
#             medications, encounters, procedures, orders, documents)
#   excluded: financial (Coverage), consent, scheduling (Appointment),
#             workflow (Task, CommunicationRequest), and administrative links
#             (RelatedPerson, PractitionerRole). A patient known only through
#             a RelatedPerson or a Coverage is still a clinical blank slate.
#
# Verified against the current data set: both this list and a looser one that
# also counted Coverage/Task/Appointment/Binary/Medication yield the same 79
# blank-slate patients, so nothing here turns on the disputed entries today.
# The narrower definition is kept because it states the intended rule rather
# than happening to agree with it.
CLINICAL_RESOURCE_TYPES = frozenset({
    "AllergyIntolerance", "Composition", "Condition", "DiagnosticReport",
    "DocumentReference", "Encounter", "Immunization", "MedicationAdministration",
    "MedicationDispense", "MedicationRequest", "MedicationStatement",
    "Observation", "Procedure", "ServiceRequest", "Specimen",
})


# --- Reused from CI ---------------------------------------------------------
# Imported rather than reimplemented so an authoring tool and the CI referential
# integrity check cannot disagree about what counts as a reference (design.md
# "Risks / Trade-offs" accepts the resulting coupling).

sys.path.insert(0, str(REPO_ROOT / ".github" / "scripts"))
from reference_integrity import find_references, get_reference  # noqa: E402


# --- Preconditions ----------------------------------------------------------

class PreconditionError(RuntimeError):
    """A derivation cannot run correctly under the current repo state.

    Raised rather than warned deliberately: a shallow clone or a missing branch
    produces output that looks plausible and is silently incomplete, which the
    design flags as the sharpest risk in this toolchain.
    """


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise PreconditionError(
            f"git {' '.join(args)} failed: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def require_full_clone() -> None:
    """Fail if the clone is shallow.

    Community-contribution attribution walks commit history; on a shallow clone
    it silently under-reports rather than erroring.
    """
    if (REPO_ROOT / ".git" / "shallow").exists():
        raise PreconditionError(
            "Shallow clone detected. Git-history derivations (community "
            "contributions) would silently under-report.\n"
            "Fix: git fetch --unshallow"
        )


def resolve_connected_care_ref() -> str:
    """Return a git ref holding the connected-care directory.

    Prefers upstream, falls back to the fork's review branch, then a local
    branch. Connected Care is not on the default branch (D6).
    """
    for ref in ("upstream/connected-care",
                "origin/review/connected-care",
                "review/connected-care"):
        try:
            _git("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")
        except PreconditionError:
            continue
        listing = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "ls-tree", "--name-only",
             ref, f"{CONNECTED_CARE_DIR}/"],
            capture_output=True, text=True,
        )
        if listing.returncode == 0 and listing.stdout.strip():
            return ref
    raise PreconditionError(
        f"No ref found containing {CONNECTED_CARE_DIR}/.\n"
        "Fix: git fetch upstream connected-care"
    )


def require_data_set() -> None:
    missing = [d for d in DATA_SET_DIRS if not (DATA_SET_ROOT / d).is_dir()]
    if missing:
        raise PreconditionError(
            f"Missing data set directories: {', '.join(missing)} "
            f"under {DATA_SET_ROOT}"
        )


def check_preconditions(*, needs_git_history: bool = False,
                        needs_connected_care: bool = False) -> dict:
    """Run the checks a given derivation depends on.

    Each script declares what it needs rather than paying for all of them, so a
    derivation that only reads the working tree is not blocked by an unfetched
    connected-care branch.
    """
    require_data_set()
    info = {"data_set_root": str(DATA_SET_ROOT)}
    if needs_git_history:
        require_full_clone()
        info["head"] = _git("rev-parse", "HEAD")
    if needs_connected_care:
        ref = resolve_connected_care_ref()
        info["connected_care_ref"] = ref
        info["connected_care_revision"] = _git("rev-parse", ref)
    return info


# --- Facts file -------------------------------------------------------------

def load_facts() -> dict:
    with FACTS_FILE.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_subset(slug: str, facts: dict | None = None) -> dict:
    facts = facts if facts is not None else load_facts()
    for subset in facts["subsets"]:
        if subset["slug"] == slug:
            return subset
    raise KeyError(f"No subset with slug {slug!r} in {FACTS_FILE}")


# --- Data set traversal -----------------------------------------------------

def iter_resource_files(dirs: tuple[str, ...] = DATA_SET_DIRS):
    """Yield (path, parsed_json) for every resource file on the working tree."""
    for d in dirs:
        for path in sorted((DATA_SET_ROOT / d).glob("*.json")):
            try:
                with path.open(encoding="utf-8") as f:
                    yield path, json.load(f)
            except json.JSONDecodeError:
                # Surfaced by the CI referential-integrity job; not this tool's
                # concern, and skipping keeps a derivation from dying on one
                # malformed file.
                continue


def rel_path(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def build_reference_index(dirs: tuple[str, ...] = DATA_SET_DIRS) -> dict:
    """Index the data set once; several derivations need the same view.

    Returns:
        resources:   "Type/id" -> {"path", "resource_type", "id", "resource"}
        referenced_by: "Type/id" -> set of "Type/id" that reference it
    """
    resources, referenced_by = {}, {}
    for path, resource in iter_resource_files(dirs):
        key = get_reference(resource)
        resources[key] = {
            "path": rel_path(path),
            "resource_type": resource.get("resourceType"),
            "id": resource.get("id"),
            "resource": resource,
        }
    for key, entry in resources.items():
        for ref in find_references(entry["resource"]):
            if not ref or ref.startswith("#"):
                continue  # contained resources are internal, not graph edges
            referenced_by.setdefault(ref, set()).add(key)
    return {"resources": resources, "referenced_by": referenced_by}


# --- Candidate output -------------------------------------------------------

def filter_administrative(members: list[dict]) -> tuple[list[dict], dict[str, int]]:
    """Keep only administrative entities; report what was dropped.

    Returns (kept, dropped_counts_by_resource_type). Every caller records the
    dropped counts so the constraint is visible in the output rather than
    silently shrinking a subset.

    Not used by missing_suppressed.py — see ADMINISTRATIVE_RESOURCE_TYPES for
    why that subset is exempt.
    """
    kept, dropped = [], {}
    for m in members:
        rtype = m.get("resource_type")
        # An entity with no resolved type (e.g. a journey participant named
        # without a matching resource) is kept: it is not evidence of a
        # clinical resource, and dropping it would hide a known gap.
        if rtype is None or rtype in ADMINISTRATIVE_RESOURCE_TYPES:
            kept.append(m)
        else:
            dropped[rtype] = dropped.get(rtype, 0) + 1
    return kept, dict(sorted(dropped.items(), key=lambda kv: (-kv[1], kv[0])))


def administrative_note(dropped: dict[str, int]) -> str | None:
    """One-line note describing what the administrative constraint excluded."""
    if not dropped:
        return None
    total = sum(dropped.values())
    detail = ", ".join(f"{t} x{n}" for t, n in dropped.items())
    return (
        f"{total} non-administrative entities excluded: {detail}. Subset "
        "identification covers administrative entities only; clinical content "
        "is retrievable from the administrative entity by FHIR mechanisms."
    )


def member(resource_id: str, resource_type: str | None = None,
           path: str | None = None, why: str | None = None, **extra) -> dict:
    entry = {"id": resource_id}
    if resource_type:
        entry["resource_type"] = resource_type
    if path:
        entry["path"] = path
    if why:
        entry["why"] = why
    entry.update(extra)
    return entry


def emit(subset: str, members=None, needs_confirmation=None, evidence=None,
         notes=None, source_revision=None, out_dir: Path | None = None) -> Path:
    """Write candidate JSON for one subset and return the path written.

    Sorted by id so two runs over an unchanged tree produce byte-identical
    output apart from `generated_at` — the idempotence task 3.5 checks.
    """
    payload = {
        "subset": subset,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revision": source_revision,
        "members": sorted(members or [], key=lambda m: m["id"]),
        "needs_confirmation": sorted(needs_confirmation or [],
                                     key=lambda m: m["id"]),
        "evidence": evidence or {},
        "notes": notes or [],
    }
    out_dir = out_dir or default_out_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{subset}.json"
    with out_path.open("w", encoding="utf-8") as f:
        # PyYAML parses an unquoted `2026-08-31` into a datetime.date, which
        # json cannot serialise. Any confirmed_on / date field read from
        # subsets.yaml arrives that way, so coerce here rather than at every
        # call site.
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    return out_path


def default_out_dir() -> Path:
    """Scratch location for candidate JSON.

    Deliberately outside the repo: candidates are intermediate, and only
    confirmed decisions belong in subsets.yaml (D3).
    """
    import tempfile
    return Path(tempfile.gettempdir()) / "data-subsets-candidates"


# --- Confirmation write-back (task 4.7) -------------------------------------

def qualify(member) -> str:
    """Return a member's canonical identity: "ResourceType/id" when the type
    is known, else the bare id as given.

    Not decorative — bare ids collide across resource types. Discovered live:
    Bundle/aups-section-emptyreason and DocumentReference/aups-section-emptyreason
    are different resources that happen to share an id, and candidate_key
    previously hashed only the bare id, so confirming one silently confirmed
    the other. Type-qualifying is what makes candidate identity actually
    unique.
    """
    if isinstance(member, dict):
        rtype = member.get("resource_type")
        rid = member.get("id")
        return f"{rtype}/{rid}" if rtype else str(rid)
    return str(member)


def candidate_key(subset_slug: str, member_ids) -> str:
    """Stable identity for a candidate, derived from what it contains.

    A candidate is sometimes one entity (a keyword hit) and sometimes a group
    (a family, a geographic grouping). Keying on sorted, type-qualified
    membership gives both the same treatment, avoids the bare-id collision
    qualify() documents, and delivers the spec's "new or changed" rule for
    free: if a group gains or loses a member its key changes, so it is
    re-asked rather than silently inheriting an old decision about a
    different group.

    member_ids may be a mix of member dicts (preferred — carries
    resource_type) and plain id strings (treated as already-qualified or
    intentionally bare).
    """
    ids = sorted({qualify(m) for m in member_ids})
    digest = hashlib.sha256(
        ("|".join([subset_slug] + ids)).encode("utf-8")
    ).hexdigest()
    return digest[:16]


def load_confirmations() -> dict:
    """Read the machine-owned decision log. Returns {} when absent."""
    if not CONFIRMATIONS_FILE.exists():
        return {"schema_version": 1, "decisions": {}}
    with CONFIRMATIONS_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def _write_confirmations(data: dict) -> None:
    CONFIRMATIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with CONFIRMATIONS_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def record_confirmation(subset_slug: str, member_ids, decision: str,
                        attester: str, confirmed_on: str | None = None,
                        note: str | None = None) -> str:
    """Persist one human decision. Returns the candidate key.

    Written to confirmations.json rather than subsets.yaml so the hand-authored
    facts file is never machine-rewritten (D12). Without this persistence every
    regeneration re-asks the same questions and the process is abandoned (D3).
    """
    if decision not in ("confirmed", "rejected", "flagged"):
        raise ValueError(
            f"decision must be confirmed|rejected|flagged, got {decision!r}")

    # member_ids may be member dicts (preferred, carries resource_type so the
    # key is type-qualified) or plain strings. qualify() handles both; the
    # stored "members" list is always the qualified form, for the same reason.
    qualified = sorted({qualify(m) for m in member_ids})
    key = candidate_key(subset_slug, member_ids)
    data = load_confirmations()
    data.setdefault("decisions", {})[key] = {
        "subset": subset_slug,
        "decision": decision,
        "members": qualified,
        "attester": attester,
        "confirmed_on": confirmed_on or datetime.now(timezone.utc).date().isoformat(),
        **({"note": note} if note else {}),
    }
    _write_confirmations(data)
    return key


def decision_for(subset_slug: str, member_ids, data: dict | None = None):
    """Return the recorded decision dict for a candidate, or None."""
    data = data if data is not None else load_confirmations()
    return data.get("decisions", {}).get(candidate_key(subset_slug, member_ids))


def partition_candidates(subset_slug: str,
                        candidates: list[dict]) -> tuple[list, list, list, list]:
    """Split candidates into (confirmed, rejected, flagged, undecided).

    Each candidate is a dict with a "members" list of ids. Confirmed ones become
    subset members; rejected ones are dropped; only undecided ones are put to
    the operator — which is what makes a rerun over an unchanged tree ask
    nothing (task 4.8).

    `flagged` is a real third outcome, not a shade of rejected: the candidate is
    plausible but the evidence that would settle it is unavailable. It stays out
    of published membership AND out of the open-questions queue, and is
    published separately as "potentially related, unconfirmed" so the reasoning
    is not lost. The measured case: two same-surname pairs where exactly one
    member has no Medicare number, so the strongest signal returns silence
    rather than a negative.
    """
    data = load_confirmations()
    confirmed, rejected, flagged, undecided = [], [], [], []
    for cand in candidates:
        # Pass member DICTS through, not bare ids — decision_for/candidate_key
        # need resource_type to qualify. Stripping ids here previously caused
        # a real collision: Bundle/aups-section-emptyreason and
        # DocumentReference/aups-section-emptyreason share a bare id and were
        # silently treated as the same candidate.
        record = decision_for(subset_slug, cand.get("members", []), data)
        if record is None:
            undecided.append(cand)
            continue
        enriched = {**cand, "attester": record["attester"],
                    "confirmed_on": record["confirmed_on"]}
        if record.get("note"):
            enriched["decision_note"] = record["note"]
        {"confirmed": confirmed, "rejected": rejected,
         "flagged": flagged}[record["decision"]].append(enriched)
    return confirmed, rejected, flagged, undecided


# --- CLI --------------------------------------------------------------------

def main_wrapper(fn):
    """Run a derivation's main(), reporting precondition failures clearly."""
    def wrapped():
        try:
            out_path = fn()
        except PreconditionError as e:
            print(f"PRECONDITION FAILED\n\n{e}", file=sys.stderr)
            raise SystemExit(2)
        except NotImplementedError as e:
            print(f"Not implemented yet: {e}", file=sys.stderr)
            raise SystemExit(3)
        if out_path:
            print(f"Wrote {out_path}")
    return wrapped
