# Data subsets — regeneration

This directory holds the facts behind [`docs/DataSubsets.md`](../DataSubsets.md),
the published wiki of logical subsets in the test data set (IG examples, Inferno
default patients, families, geography groupings, and so on).

- **`subsets.yaml`** — hand-authored facts: Declared and Curated values, plus
  confirmed Derived+Curated decisions. Never machine-written.
- **`confirmations.json`** — machine-owned log of human confirm/reject/flag
  decisions for Derived+Curated candidates, keyed by subset and membership.
  Never hand-edited.

## Regenerating the page

There is no orchestrating skill yet (`openspec/changes/add-data-subset-identification/tasks.md`
group 6), so regeneration is manual:

```bash
cd scripts/data-subsets
pip install -r requirements.txt

# Run each derivation script that has one. Most need no input; each writes
# its candidate JSON to a scratch directory and prints anything awaiting a
# human confirm/reject/flag decision.
python3 ig_examples.py
python3 inferno_defaults.py
python3 connected_care.py
python3 contributions.py
python3 missing_suppressed.py
python3 blank_slate_patients.py
python3 geography.py
python3 families.py

# scenario-groups has no re-run mechanism — it was seeded once from a pinned
# git ref (see design.md D5/D12) and is now maintained by hand in
# subsets.yaml.

# Then assemble the page from subsets.yaml + every script's candidate JSON:
python3 assemble.py
```

If a script reports candidates awaiting confirmation, record the decision by
calling `lib.record_confirmation(...)` for each one (see `lib.py`) before
re-running that script and `assemble.py` — a confirmed or rejected candidate
is never re-asked; a changed one is.

The full mechanism per subset — what each script proposes and on what
evidence — is documented in `openspec/changes/add-data-subset-identification/design.md`
and in each script's own docstring.
