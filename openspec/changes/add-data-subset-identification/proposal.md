## Why

Administrative resources — Patient, RelatedPerson, Practitioner, PractitionerRole,
Organization, Location and HealthcareService — cannot be created on demand, nor freely
enriched. Their key identifiers are issued by Services Australia: IHI, HPI-I and HPI-O are
allocations reserved for testing in the HI Vendor Test Environment, while Medicare, DVA,
provider and PBS prescriber numbers are valid identifiers not reserved for testing.
Governance is therefore, at a minimum, shared with the organisation issuing the identifiers:
creation and allocation run through the project team, by processes that may be fluid or
not yet fully established.

Using the test data may therefore start with finding entities that already fit, since
requesting new ones is a considerably more costly and involved path. Read-only use is
unconstrained — anyone may load, query or test against any entity as they see fit. The
constraint bites only when adding to or modifying an entity or its network of linked resources,
where new content can conflict with a purpose the entity already serves. That requires
knowing, across ~1,540 resources in four directories and the `connected-care` branch, which
entities are committed to a purpose that new content could disturb, which are free to build
on, and which suit a new need — co-located for a plausible consumer journey or test scenario,
related as a family, or patients without clinical data (blank slates).
At least a dozen such subsets exist, but nothing identifies them in one place, states how
each is identified, or documents who owns and confirmed them; and several can only be
proposed from weak signals such as postcode proximity or commit authorship, so membership is
credible only when the source or attester behind it is documented.

This change establishes a capability spec, a stable facts file, and an orchestration
procedure — a foundation that a future subset (e.g. one requested by a partner project) can
be added to as a one-requirement delta, without re-deriving the whole approach.

## What Changes

- Introduce the `data-subset-identification` capability: one requirement per known subset,
  each stating its type (Derived / Declared / Curated / Derived+Curated per the taxonomy
  defined in the capability spec) and its identification mechanism, plus a mechanically
  checkable acceptance criterion.
- Separate stable facts (resource ids, owners, confirmation dates) out of the requirements
  and into `docs/data-subsets/subsets.yaml`, so requirements describe mechanisms and the
  facts file carries the data.
- Define the whole-of-wiki presentation requirements: per-section structure (mechanism,
  properties, governance/provenance/intended-use/relationships), grouping by resource type,
  expand/collapse over 20 entities, manual-trigger-only regeneration, and a generation stamp
  (source commit, date).
- Define a human-confirmation write-back loop for Derived+Curated subsets: a regeneration
  run surfaces only new or changed candidates, and confirmed answers are persisted back to
  `subsets.yaml` with `attester` and `confirmed_on` so the same question is never re-asked.
- Record reservation status per subset: whether a subset's entities are reserved to that
  purpose or may be reused elsewhere, declared in `subsets.yaml` as a governance property
  rather than inferred from how many subsets an entity appears in.

## Capabilities

### New Capabilities
- `data-subset-identification`: identifies and documents every logical subset of the test
  data set (which entities belong to it, how membership is determined, who owns/confirmed
  it, and how it relates to other subsets), and defines how the resulting wiki page is
  regenerated and presented.

### Modified Capabilities
(none — no existing capability specs)

## Impact

- **New files**: `openspec/specs/data-subset-identification/spec.md` (via this change),
  `docs/data-subsets/subsets.yaml`, `docs/data-subsets/README.md`,
  `scripts/data-subsets/*.py` (stubs), `.claude/skills/regenerate-data-subsets-wiki/`,
  `.claude/commands/regenerate-data-subsets-wiki.md`.
- **No changes to test data instances** — this change concerns documentation and tooling
  only, not `au-fhir-test-data-set/*`.
- **External dependencies**: read access to three `hl7au/` IG repos and
  `inferno_suite_generator` for IG-example and Inferno-default derivations; a full,
  all-branches clone of `hl7au/au-fhir-test-data` for the community-contributions and
  Connected Care derivations.
- **Non-goals**: authoring test data to fill gaps this work exposes — the AU Encounter
  Records care team now resolves, but its clinical narrative (chemotherapy, admission,
  HITH) does not exist and creating it is separate work; proposing anything upstream to
  `hl7au/au-fhir-test-data` (only the generated wiki is ever proposed there, and only when
  explicitly promoted); correcting test data defects the derivations surface.
