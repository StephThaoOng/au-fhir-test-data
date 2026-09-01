## Context

See `proposal.md` — Why. Constraints that shape the approach:

- **Derivations read git history and non-default branches.** Community contributions are
  attributed by commit authorship, and Connected Care lives on the `connected-care` branch.
  Both silently under-report on a shallow or single-branch clone.
- **Three sources of truth are outside this repository** — the AU Core, AU PS and eRequesting
  IG repos and `inferno_suite_generator`, all under `github.com/hl7au/`. They move
  independently of this repo.
- **Several subsets cannot be computed reliably.** Postcode proximity, shared surname and
  commit authorship are weak signals; a script can propose members but cannot settle them.
- **The wiki is regenerated repeatedly over a data set that changes underneath it.** Anything
  requiring a human answer will be asked again on every run unless the answer is persisted.
- **Subset identification is constrained to administrative entities** — Patient,
  RelatedPerson, Practitioner, PractitionerRole, Organization, HealthcareService, Location,
  Endpoint. These are the scarce ones: their key identifiers and some core attributes are
  allocated by Services Australia and correspond to entities provisioned in the HI Vendor
  Test Environment, so an administrative entity cannot simply be created or modified on
  demand within this project. They are therefore the entities that may carry governance
  considerations. Clinical resources can be authored far more freely, so tracking their
  subset membership is low value, and where needed clinical content is retrievable from the
  administrative entity by FHIR mechanisms. One exemption: `missing-suppressed-data`, whose
  instances demonstrate the correct *representation* of missing or suppressed data rather
  than a defect — a property that attaches to an Observation exactly as to a Patient, and is
  unrelated to the scarcity argument.

## Goals / Non-Goals

**Goals:**
- Make each subset's membership reproducible — either computed, or traceable to a named
  source or attester.
- Keep the requirements stable while the underlying data changes.
- Make the human-confirmation cost fall to near zero on reruns where nothing changed.

**Non-Goals:**
- Automating decisions that need judgment. Weak-signal subsets stay human-confirmed.
- A queryable index or API over the data set. The output is one markdown page.
- Changing any test data instance.

## Decisions

### D1. Four kinds of knowledge, four homes

| Kind | Home | Changes when |
| --- | --- | --- |
| Facts — what is true now | `docs/data-subsets/subsets.yaml` | Test data changes, or a maintainer states something new |
| Decisions — why it is built this way | this file, archived with the change | Never; append-only history |
| Requirements — what the wiki must identify | the capability spec | A change proposal amends it |
| Procedure — how to regenerate | skill + scripts | The mechanism changes |

The failure this avoids is the one the requirements were extracted from: resource ids and
maintainer decisions embedded directly in requirement text, so that adding one entity means
editing the spec. Requirements name mechanisms; facts live in YAML.

*Alternative considered:* a single generator script holding facts inline as constants.
Rejected — facts would then be reviewable only by reading code, and every curated addition
would be a code change.

### D2. Scripts compute; the skill judges

Anything deterministic and reproducible is a script: diffable output, runnable without a
model. Anything needing judgment, prose cross-referencing, or human confirmation is the
skill. Scripts emit candidate JSON; the skill decides what to do with it and assembles the
page.

*Alternative considered:* doing all of it in the skill. Rejected — derivations over ~1,540
files must be reproducible and reviewable, and a model re-deriving them each run gives
different answers for the same input.

### D3. Confirmations are written back to the facts file

A confirmed or rejected candidate is persisted with its attester and date. Subsequent runs
diff against that record and present only what is new or changed.

This is what makes regeneration cheap enough to actually happen. Without it every run
re-asks the same questions over the same 89 patients, and the process is abandoned after the
second use.

### D4. Declared and Curated are distinguished by whether a source can drift

Declared facts have an authoritative source outside the wiki that could change without the
wiki being told — so they carry a resolvable source reference and are drift-checked. Curated
facts have no such source; the facts file *is* the authority, so they carry an attester and a
date instead.

The two need different maintenance, which is the only reason to separate them. Collapsing
them into "human-stated" would lose the drift check on the Declared half.

### D5. Scenario groupings are seeded once, then curated

The historical scenario directory structure at a pinned git ref is read once to seed
membership. After seeding, the facts file becomes authoritative and the pinned ref is
recorded for traceability only, not re-consulted.

*Alternative considered:* re-deriving from the pinned ref on every run. Rejected — the
directories no longer exist on the default branch, so the ref is a historical snapshot, not
a live source. Continuing to derive from it would freeze the groupings against curation.

### D6. Connected Care is derived from its branch

Its entities are not on the default branch, so the derivation reads `connected-care`
directly rather than waiting for a merge. Alex's Story membership comes from the data set
document held alongside those instances; the remainder is attributed to Yuri's Story
provisionally, and published as provisional, until its own source document exists.

### D7. Authoring tools live in `scripts/`, not `.github/scripts/`

`.github/scripts/` holds CI-triggered PR checks (`reference_integrity.py`,
`check_amt_medication_class.py`) that must pass for a contribution to merge. These are
manually-run authoring tools whose output is reviewed before publication. Different trigger,
different failure mode, different directory.

### D8. Only the generated wiki is ever proposed upstream

The facts file, scripts, skill, command and OpenSpec artifacts are committed to the fork.
The wiki page is the only artifact proposed to `hl7au/au-fhir-test-data`, and only when
explicitly promoted.

### D9. Consumer journey entities are reusable, and their downstream use is tracked

Clinical Design Group consumer journeys are an origin point, not an enclosure. An entity used
in a journey may also appear in the corresponding IG project use cases, and those can be
progressed into technical use cases. The subset is therefore recorded as reusable, and the
downstream use cases an entity has been carried into are recorded as relationships. There is
no document identifying those use cases, so this is Curated — a manual entry in `subsets.yaml`
per journey entity, attester-backed like any other Curated fact.

This is the case the reservation property exists to distinguish: appearing in exactly one
subset says nothing about whether an entity is available. Inferring reservation from subset
membership would wrongly lock these entities away from the very reuse they are intended for.

*Alternative considered:* treating journey membership as reserving the entity. Rejected — it
inverts the actual intent, and would make the wiki discourage the reuse it exists to enable.

### D10. Reservation constrains writes, not reads

Read-only use of the test data is unconstrained — anyone may load, query or test against any
entity as they see fit. Reservation governs write intent only: adding to or modifying an
entity or its network of linked resources, because new content joins a graph already shaped to
serve a stated purpose.

This scoping is what makes overlap meaningful. If an entity sits in both the AU Core IG
example set and a consumer journey, a new Condition referencing it could break the IG's
documented example *and* contradict the journey's clinical timeline. Overlap is a write-time
hazard, not a usage restriction — which is why the wiki surfaces it rather than forbidding
anything.

*Alternative considered:* treating reservation as a usage restriction — "these entities are
spoken for, don't use them". Rejected on two counts: it would discourage the reading and
testing the data set exists for, and it leaves overlap unexplained, since two subsets sharing
an entity is only a problem when someone writes.

### D11. Declared sources track latest; the revision read is an output

The Inferno default patient list and the AU PS Test Data Coverage page are read at their
current state on each generation rather than at a hand-pinned revision. `source_revision` in
the facts file is therefore an output — the revision the last generation actually read —
not an input a maintainer sets.

Drift detection depends on this: the transcribed `members` list is what we believe, the
source at its current revision is what is true now, and `source_revision` records when we
last looked.

*Alternative considered:* pinning each source to a fixed revision. Rejected — a pin would
make the wiki quietly stale. It would keep reporting a transcription that matches its pin
while the upstream source moved on, which is precisely the drift the Declared classification
exists to catch.

### D12. Two facts files, split by who writes them

`docs/data-subsets/subsets.yaml` is hand-authored and never written by a script.
`docs/data-subsets/confirmations.json` is machine-owned and holds the confirmation
decisions, each with its attester and date.

The split exists because the two have different writers and different failure
modes. `subsets.yaml` carries its schema documentation in YAML comments, and
PyYAML's dumper discards comments — round-tripping the file through a script
would silently destroy 4KB of documentation on the first write-back. A
hand-authored file that a machine also rewrites is a file whose hand edits are
one run away from being lost.

Candidate identity is a hash of the candidate's sorted membership. This
delivers the spec's "new or changed" rule directly: a family or geographic
grouping that gains or loses a member gets a different key, so it is re-asked
rather than inheriting a decision made about a different group.

*Alternative considered:* adding `ruamel.yaml`, which round-trips comments, and
keeping everything in one file as the spec's "the facts file" implies. Rejected
— it makes a hand-authored file machine-writable for no gain the split does not
already provide, and the repo otherwise carries no Python dependencies at all.

*Note:* PyYAML is the toolchain's one non-stdlib dependency, used only to READ
`subsets.yaml`, and is declared in `scripts/data-subsets/requirements.txt`. The
CI scripts under `.github/scripts/` that gate pull requests stay stdlib-only.

### D13. A shared Medicare card is a primary family signal, unioned with RelatedPerson

An Australian Medicare number is a card number plus a per-person Individual Reference
Number, so a family on one card shares everything but the last digit. That makes a shared
card the administrative statement of a family unit — stronger evidence than any inference
from names or addresses.

It is unioned with the RelatedPerson network rather than replacing it, because neither
signal dominates. Measured on this data set the two agree on all 7 families, but each
catches something the other cannot: `baby-banks-john` has no Medicare number — a newborn
not yet on the card — and is found only via RelatedPerson, while a family whose
RelatedPerson links were absent would be found only via the card.

Only 11-digit values are parsed as card+IRN. One value in the data set is 10 digits
(`Patient/bennelong-anne`); truncating it would invent a 9-digit card matching nothing, so
it is reported as malformed rather than silently mis-parsed.

*Alternative considered:* treating the card as the sole primary signal and demoting
RelatedPerson. Rejected — it would drop the newborn from his own family.

### D14. `flagged` is a third decision state, not a shade of rejected

A candidate can be plausible while the evidence that would settle it is simply unavailable.
Recording that as "rejected" asserts something the data does not support; leaving it
undecided means it resurfaces forever as an open question nobody can close.

So confirmations carry three states. A flagged candidate stays out of published membership
and out of the open-questions queue, and is published separately as "potentially related,
unconfirmed" with the reason recorded.

The case that forced it: two same-surname pairs where **exactly one member has no Medicare
number**, so the strongest signal returns silence rather than a negative. `sandilands-kendall`
holds a card and `sandilands-young` has none; `hoskins-sergio-lionel` holds a card and
`hoskins-marisa` has none. Absence of evidence, not evidence of absence.

### D15. Confirmation identity is type-qualified, not bare id

`candidate_key` hashes each member's identity to detect whether a candidate is new,
unchanged, or has changed since it was last decided (D3). It hashed bare ids until a real
collision surfaced: `Bundle/aups-section-emptyreason` and
`DocumentReference/aups-section-emptyreason` are two different resources that happen to
share an id, and confirming one silently confirmed the other — discovered when reverting a
batch of decisions removed 57 entries but only 55 keys existed.

Member identity is now `ResourceType/id` wherever the type is known (`lib.qualify`), falling
back to the bare value only when it is not. The 11 family decisions already recorded were
migrated to the new keys, preserving their original attester, date and reasoning — a
mechanical correction, not a re-litigation of decisions a human had already made.

*Alternative considered:* refusing to record a candidate whose bare id collides with another
within the SAME group. Rejected — the collision that occurred was across two different
single-member candidates, not within one, so a within-group check would not have caught it.

### D16. Relationships is curated from computed evidence

A subset's relationship to another is *shared membership*, which a script can compute
exactly. But which overlaps are worth stating is a judgement, not a calculation:
`geography-groups` holds 1,022 of the administrative entities and therefore overlaps almost
every other subset, so listing it everywhere would be true and useless.

So the derivation computes the overlaps and the prose is hand-authored in `subsets.yaml`,
naming only what a reader needs — the same script-proposes/human-decides split the
confirmation machinery already uses. Measured examples of what that judgement keeps:
`inferno-default-patients` and `au-ps-test-patients` share 6 of 7 members, so changing one
almost certainly affects the other; `families` and `blank-slate-patients` share 25.

Prose carries `{slug}` placeholders rendered as links on the subset's title, so it reads as
a sentence while still satisfying the "Subsets are addressable by slug" scenario. The
renderer strips whitespace inside a placeholder, because YAML folds long lines and can split
one across a line break.

*Correction this exposed:* `au-core-ig-examples` previously declared a relationship to
`au-erequesting-ig-examples` — two subsets that share **no members at all**. That was
conceptual kinship (both are IG example sets) recorded in a field that now means shared
membership, so it did not survive.

*A relationship with no membership basis, deliberately kept:* `connected-care-journeys`
entities are clearly geographically clustered (Kalgoorlie WA, Bathurst NSW) but share
nothing with `geography-groups`, because they live on a branch the geography derivation does
not index. The prose states the clustering and explains the absence, rather than either
claiming a false overlap or leaving a reader puzzled.

### D17. The wiki carries its own context, because it travels alone

`docs/DataSubsets.md` is the only artefact ever proposed upstream (D8) — the
proposal, spec, design and scripts all stay in the fork. Anything a reader needs
in order to *interpret* the page therefore has to be on the page.

A concrete instance: the page printed `_Classification: Derived + Curated._`
fourteen times while the definition of those four types existed only in the
capability spec, which upstream never sees. The opening section now carries four
blocks — why these subsets are worth tracking, what is in scope, reading versus
writing, and the four classifications (collapsed, since it is reference material
rather than narrative).

*Consequence to watch:* this duplicates wording between the spec/design and the
generated page. The page is generated from `subsets.yaml` and `assemble.py`, so
the duplication is in the source artefacts rather than maintained by hand in two
places — but a change to the classification definitions now needs applying in
both the spec and the renderer's intro.

### D18. Source revisions belong with the source, not in a page-level table

Each subset states the revision it was read at under "How is this subset
identified?", beside the source it came from, rather than in a page-level
summary table. A reader asking "which version of the AU Core IG?" is already
reading that subset's section; a separate table makes them look in two places
and, when it listed subset slugs rather than repository names, misidentified
what the source even was.

### D19. Governance prose states the write constraint, not who decided membership

A subset's `governance` field says what the entities are relied on for, what a
write would break, and who to coordinate with. It does **not** say who decided
the membership — that belongs under "How is this subset identified?", which
exists to answer exactly that.

Smart Health Checks violated this and showed why it matters. Three of its five
sections stated the same fact in three phrasings — governance said "by
maintainer decision", provenance said "a project decision", identification said
"stated by a maintainer" — so a reader was told the same thing three times while
never being told the one thing governance is for: what breaks if they write to
these entities. The other four reserved subsets each name a concrete
consequence (losing Must Support coverage, conflicting with a story's clinical
timeline, misrepresenting what an instance demonstrates), which is the shape to
follow.

The general rule: each of the five sections answers a different question, so a
fact stated in the section that does not own it is duplication, and duplication
crowds out the content that section was supposed to carry.

### D20. Cross-reference reservation status shown as TBD for six subsets pending review

Inferno default patients, AU PS test patients, Smart Health Checks, Sparked
CDG journeys, Connected Care journeys and Scenario groupings each state a
reservation verdict in their own governance section. That verdict is not yet
reconfirmed for the separate purpose of flagging a conflict on another
entity's cross-reference — so where one of these six is *named* in another
entity's "also in:" note, the page shows "(maybe reserved — TBD)" rather than
asserting reserved or free-to-build-on, pending that review.

Display-only, scoped to `overlap_note()` in `scripts/data-subsets/assemble.py`.
Does not change `reserved` in `subsets.yaml`, does not alter any subset's own
governance section, and does not reopen D9's argument that CDG journey
entities are reusable — D9's reasoning stands; the TBD label reflects only
that its cross-reference use specifically has not yet been reconfirmed.

Two subsets outside this list, geography-groups and blank-slate-patients, are
instead suppressed entirely as overlap targets: both are `reserved: false`
with no exceptions, and every appearance to date has been free-to-build-on
noise rather than a reservation signal, so naming them added nothing a reader
needed to see.

## Sources of truth

| Subset | Type | Source of truth |
| --- | --- | --- |
| AU Core IG examples | Derived | `hl7au/au-fhir-core` → `input/examples/` |
| AU PS IG examples | Derived | `hl7au/au-fhir-ps` → `input/examples/`, extracted from `Bundle.entry` |
| AU eRequesting IG examples | Derived | `hl7au/au-fhir-erequesting` → `input/examples/` |
| Inferno default patients | Declared | `inferno_suite_generator` default patient id list, read at current revision (D11) |
| AU PS test patients | Declared | AU PS Test Data Coverage page (Confluence) |
| Smart Health Checks | Curated | `subsets.yaml` |
| Sparked CDG journeys | Curated | `subsets.yaml`; reusable, not reserved (D9); AU Encounter Records journeys pending |
| Connected Care — Alex's Story | Declared | Alex's Story data set document, `connected-care` branch |
| Connected Care — Yuri's Story | Declared | **Pending** — provisional remainder until supplied |
| Community contributions | Derived + Curated | Commit author/committer domain, plus confirmed overrides |
| Missing and suppressed data | Derived + Curated | Repository documentation of those cases, plus keyword scan |
| Scenario groupings | Curated | `subsets.yaml`, seeded from a pinned git ref (D5) |
| Geographic groupings | Derived + Curated | Postcode prefix + reverse references + scenario overlay, confirmed |
| Families | Derived + Curated | `RelatedPerson` network primary; surname/address secondary, confirmed |
| Blank-slate patients | Derived | Reverse-reference scan over the data set |

## Risks / Trade-offs

- **Commit-authorship attribution under-reports.** A contributor using a personal address, or
  a merge that did not preserve authorship, is invisible to it. → Support human-confirmed
  additions, and state the limitation in the published section rather than implying the list
  is exhaustive.
- **A shallow or single-branch clone produces silently wrong output.** Both the git-history
  and Connected Care derivations degrade without error. → Check the precondition before
  deriving and fail loudly, rather than emitting a plausible but incomplete page.
- **External IG repos move independently.** An entity can stop being an IG example without
  anything here changing. → Record the revision each derivation ran against, so a stale
  result is visible rather than assumed current.
- **Postcode proximity is a weak proxy.** Two entities sharing a prefix may have no
  meaningful relationship. → Publish only confirmed groupings, and describe the subset as
  best-effort.
- **Curated facts rot silently.** A decision recorded once can quietly stop being true. →
  Every curated entry carries an attester and date, so staleness is at least visible.
- **Reusing `find_references` from `reference_integrity.py`** couples an authoring tool to a
  CI script. Accepted: the alternative is a second implementation of reference extraction
  that can disagree with the one enforcing referential integrity in CI.

## Open Questions

- **`meta.source` / `meta.tag` for data provenance.** Adopting
  one would give attribution a stronger mechanism than commit authorship, but it is a data
  set change for project leads to consider, not part of this change.
- **Connected Care shared infrastructure.** Organizations, HealthcareServices and
  Practitioners on the `connected-care` branch appear to serve both stories. The remainder
  rule assigns them to Yuri's Story until Yuri's source document lands — until then both are
  published as provisional, so the answer changes no requirement.

- **Should Must Support coverage drive the Inferno default patient set, rather than the
  reverse?** The Inferno default patients are treated here as Declared: the suite states the
  list, and the wiki transcribes and drift-checks it. The set is *intended* to exercise every
  Must Support element, but that intent carries no guarantee — nothing verifies that it
  achieves full coverage, or that it is the smallest set that does, so the wiki as specified
  repeats the claim without testing it.

  The inversion would be to compute the minimum set of patients whose associated resources
  collectively exercise every Must Support element in a given IG, and generate the suite's
  default patient configuration from that. Coverage would become an asserted property rather
  than an inherited assumption, and both gaps (elements no patient exercises) and redundancy
  (patients contributing nothing the rest do not) would become visible.

  The element-enumeration half already exists — the `fhir-ms-classifier` skill classifies
  every Must Support element in a built StructureDefinition into mandatory, optional and
  choice buckets. What is missing is the coverage solve over the data set, and agreement with
  the suite maintainers on which artifact is authoritative.

  Deferrable: adopting it would reclassify the subset from Declared to Derived, but changes
  nothing here — transcribing and drift-checking the declared list stays correct meanwhile.
  It is a separate capability and belongs in its own change.

