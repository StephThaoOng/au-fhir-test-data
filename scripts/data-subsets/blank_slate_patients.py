#!/usr/bin/env python3
"""Identify patients with no clinical data — free to build on.

Subset:  blank-slate-patients
Type:    Derived (no human confirmation; recomputed every run)
Task:    3.1

Contract
--------
Emits every Patient that is NOT referenced as the subject of any clinical
resource. Answers "which patients can I select for a new consumer journey, or
match with externally generated data, without pre-existing clinical content
conflicting with what I am about to create?"

Mechanism
---------
Build the reference index, then for each Patient check whether any resource
whose type is in lib.CLINICAL_RESOURCE_TYPES references it. A Patient
referenced only by administrative resources (RelatedPerson, Coverage,
Appointment) is still a blank slate for clinical purposes — the distinction
that makes this subset useful rather than a bare orphan check.

Output
------
members            Patients with no referencing clinical resource
needs_confirmation empty — this derivation is deterministic
evidence           counts, and for non-members the clinical types found
"""

import lib


def main():
    lib.check_preconditions()
    idx = lib.build_reference_index()
    resources, referenced_by = idx["resources"], idx["referenced_by"]

    members, populated = [], {}

    for key, entry in sorted(resources.items()):
        if entry["resource_type"] != "Patient":
            continue

        referrer_types = {
            resources[r]["resource_type"] for r in referenced_by.get(key, set())
        }
        clinical = sorted(referrer_types & lib.CLINICAL_RESOURCE_TYPES)

        if clinical:
            populated[entry["id"]] = clinical
            continue

        # Record what DOES reference the patient, so a reviewer can see the
        # difference between "referenced by nothing at all" and "referenced
        # only administratively" without re-deriving it.
        admin = sorted(referrer_types)
        members.append(lib.member(
            entry["id"],
            resource_type="Patient",
            path=entry["path"],
            why=("no referencing clinical resource; referenced only by "
                 f"{', '.join(admin)}" if admin else
                 "not referenced by any resource"),
            referenced_by_types=admin,
        ))

    # Subset identification covers administrative entities only (lib). A no-op
    # here — this derivation only ever emits Patients — applied so the rule is
    # enforced uniformly rather than relying on that staying true.
    members, dropped_nonadmin = lib.filter_administrative(members)

    total = len(members) + len(populated)
    return lib.emit(
        "blank-slate-patients",
        members=members,
        evidence={
            "non_administrative_excluded": dropped_nonadmin,
            "total_patients": total,
            "blank_slate": len(members),
            "with_clinical_data": len(populated),
            "clinical_resource_types": sorted(lib.CLINICAL_RESOURCE_TYPES),
            "patients_with_clinical_data": populated,
        },
        notes=[
            f"{len(members)} of {total} patients have no clinical data.",
            "A patient referenced only by RelatedPerson, Coverage or "
            "Appointment counts as a blank slate: those record no clinical "
            "fact for new content to conflict with.",
        ],
    )


if __name__ == "__main__":
    lib.main_wrapper(main)()
