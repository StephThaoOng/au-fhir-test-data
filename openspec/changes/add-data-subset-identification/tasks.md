## 1. Facts file

- [x] 1.1 Define the `subsets.yaml` schema at `docs/data-subsets/subsets.yaml`: per-subset
      `slug`, `title`, `type` (derived / declared / curated / derived+curated), `owner`,
      `reserved` (bool), `governance`, `provenance`, `intended_use`, `relationships` (list of
      slugs), and a `members` block. Declared subsets carry `source` (URL, path or git ref)
      and `source_revision`; curated subsets carry `attester` and `confirmed_on`.
- [x] 1.2 Seed the Declared subsets: Inferno default patients (7 ids, pinned
      `inferno_suite_generator` source and revision) and AU PS test patients (6 ids, AU PS
      Test Data Coverage URL).
- [x] 1.3 Seed the Curated subsets: Smart Health Checks (`ballantyne-kelvin-hans`) and the
      five Sparked AU PS consumer journeys, using resolved resource ids — `banks-jeramy-ezra`,
      `johnson-joyce`, `burrows-ginger`, `morris-charlotte`, `nielsen-eleanore`,
      `simpson-tristan` — not display names. Record AU Encounter Records journeys as pending.
      Mark the CDG journeys `reserved: false` per D9, and add a `downstream_use` field
      (Curated: manual entry, `attester` and `confirmed_on`) for recording the IG project and
      technical use cases a journey entity has been carried into.
- [x] 1.4 Seed the derivation inputs: the community-contribution organisation domains and the
      12 confirmed Organization overrides; the missing/suppressed keyword list (`missing`,
      `suppressed`, `masked`, `not-performed`, `cancelled`, `unknown`, `dataabsentreason`,
      `notasked`, `empty`); the Connected Care branch ref and Alex's Story document path.
- [x] 1.5 Set `reserved` on every seeded subset per D-reservation, and record the rationale in
      each entry's `governance` field.
- [x] 1.6 Verify: the file parses as YAML, every slug is unique, every `relationships` entry
      resolves to another slug, and every member id resolves to a file on the ref it names.

## 2. Script scaffolding

- [x] 2.1 Create `scripts/data-subsets/` with a shared `lib.py`: load `subsets.yaml`, resolve
      the data set root, emit candidate JSON in a common shape (`subset`, `members`,
      `evidence`, `needs_confirmation`).
- [x] 2.2 Add a preconditions check to `lib.py` that fails loudly on a shallow clone, a
      missing `connected-care` ref, or unreachable `hl7au/` sources — per the design's
      silently-wrong-output risk.
- [x] 2.3 Reuse `find_references` from `.github/scripts/reference_integrity.py:6-22` rather
      than reimplementing recursive reference extraction.
- [x] 2.4 Create stub scripts with docstring contracts and `TODO` bodies for each derivation
      named in section 3 and 4, so the skill can be written against a fixed interface.

## 3. Derived scripts

- [x] 3.1 `blank_slate_patients.py` — patients not referenced as subject by any clinical
      resource. Verify against a hand-checked sample of 5 patients.
- [x] 3.2 `inferno_defaults.py` — read the Inferno source at its current revision, emit the id
      list, report drift when it no longer matches `subsets.yaml`, and write the revision read
      back to `source_revision` (D11).
- [x] 3.3 `ig_examples.py` — match test data against the AU Core and eRequesting example sets
      on resource identity. Matching must not require content equality (IG examples are
      published with some Services Australia identifier data stripped).
- [x] 3.4 Extend `ig_examples.py` for AU PS: extract resources from `Bundle.entry` and match
      back on business identifier. (Scope widened: eRequesting also ships Bundles, so entry
      extraction runs for every IG rather than being special-cased to AU PS.)
- [x] 3.5 Verify: each script emits valid candidate JSON and is idempotent across two runs on
      an unchanged tree. (Caught and fixed a real non-determinism: multi-identifier resources
      recorded a varying match basis because identifiers were iterated from a set.)

## 4. Derived + Curated scripts

- [x] 4.1 `contributions.py` — attribute entities by commit author/committer domain, merged
      with the confirmed overrides from `subsets.yaml`. Flag entities it cannot attribute.
      (Scan independently found all 12 confirmed overrides; zero override-only entities.)
- [x] 4.2 `missing_suppressed.py` — read the documented cases, then scan resource ids for the
      keyword list and emit unconfirmed hits as `needs_confirmation`. (11 documented cases all
      resolve. 57 keyword hits presented to the user with evidence, split by mechanism strength;
      56 confirmed, 1 rejected (verificationStatus omitted with no explicit absence marker —
      a different representational pattern from the confirmed cases). 67 total members.
      Caught and fixed a real bug during this pass: candidate_key hashed bare ids, so
      Bundle/aups-section-emptyreason and DocumentReference/aups-section-emptyreason (different
      resources sharing an id) collapsed into one decision — see D15. Also caught the same class
      of bug in a confirm script's own bare-id dict, which silently dropped 2 of 57 candidates;
      both recovered and confirmed.)
- [x] 4.3 `scenarios.py` — one-time seed extraction from the pinned git ref (7 scenario
      groups, 418 files) into `subsets.yaml`, after which the ref is recorded for
      traceability only and not re-read. (Emits candidate JSON for manual application per D12
      rather than writing subsets.yaml directly; refuse-if-already-seeded guard verified.
      All 418 files resolved, 0 unresolved.)
- [x] 4.4 `connected_care.py` — read the `connected-care` branch, partition by Alex's Story
      document, and emit the remainder as provisional Yuri's Story membership. (88 Alex / 62
      Yuri-provisional of 150 total, 0 broken links, 1 unresolved narrative row. Caught and
      fixed a bug: the doc's free-text Resource Type column — e.g. "Bundle (AU Patient
      Summary)" — was wrongly used to parse the id; now derived from the filename convention.
      56 of the 62 remainder entities tagged `likely_shared` per the open shared-infrastructure
      question.)
- [x] 4.5 `geography.py` — group by postcode, expand by reverse reference
      (HealthcareService→Organization/Location, PractitionerRole→Practitioner), overlay
      scenario groups, emit as `needs_confirmation`. Rule revised after review: **metro
      groups by capital city, regional by 3-digit postcode bucket windowed ±1** — Australian
      postcodes are not spatially ordered, so no digit arithmetic captures metro proximity
      (Southbank 3006 and St Kilda 3182 are ~6km apart but differ by 8 in the 3rd digit).
      Metro ranges are a curated fact in `subsets.yaml`, not hardcoded. 93 groupings
      (8 metro + 85 regional) from 774 addressed entities; 6 of 7 scenarios now land in a
      single group. Excludes 11 non-Australian addresses whose postcodes collide with
      Australian ranges (Napier NZ 4104 sits inside Brisbane metro) — mixed-state groupings
      went 2 → 0. Known limitation recorded and surfaced on the page: buckets 481/482 are ±1
      adjacent but Townsville↔Mount Isa is ~900km, and there are no coordinates in the data
      set to check distance against.
- [x] 4.6 `families.py` — RelatedPerson network and shared Medicare card as TWO primary
      signals, unioned; surname and/or address emitted separately as `needs_confirmation`.
      Members not required to share an address. (Medicare card = first 10 digits, the card
      number; the 11th is the per-person Individual Reference Number. Verified: 7 shared
      cards mapping exactly onto the 7 RelatedPerson families — two independent signals
      agreeing on every family. Unioned rather than substituted because neither dominates:
      baby-banks-john has no Medicare number and is found only via RelatedPerson. One
      10-digit Medicare value reported as malformed rather than mis-parsed as a card.
      2 FRND "unrelated friend" edges excluded. All 11 candidates decided: 7 confirmed,
      2 rejected (italia-sofia test variants), 2 flagged.)
- [x] 4.7 Implement the confirmation write-back in `lib.py`: persist confirmed and rejected
      decisions with `attester` and `confirmed_on`, and diff against them so a second run
      surfaces nothing new on an unchanged tree. (Decisions go to a machine-owned
      `confirmations.json`, not `subsets.yaml` — see D12. Candidate identity is a hash of
      sorted membership, so a changed group is re-asked.)
- [ ] 4.8 Verify: run each script twice; the second run presents zero candidates for
      confirmation.

## 5. Assembly

- [x] 5.1 `assemble.py` — merge `subsets.yaml` and candidate JSON into `docs/DataSubsets.md`.
      (Three-tier membership resolution: candidate JSON where a script exists, else
      subsets.yaml's hand-authored members, with scenario-groups falling through to an
      explicit "pending" state when its one-time seed hasn't been applied yet.)
- [x] 5.2 Render each subset section with its mechanism, type, reservation status and the
      four properties; state explicitly where a property is unknown rather than omitting it.
      (Distinguishes `relationships: []` — a deliberate "none" — from a genuinely unanalyzed
      property, rather than one generic placeholder for both.)
- [x] 5.3 Group entity lists by FHIR resource type; wrap lists over the size threshold in
      `<details><summary>` so they collapse by default on GitHub. (Three subsets additionally
      sub-group by journey/story/organisation before grouping by resource type.)
- [x] 5.4 Make reservation discoverable for entities appearing in more than one subset.
      (Caught and fixed a real gap: Sparked CDG journey members were left with no
      resource_type, which silently excluded them from the cross-reference index — the exact
      au-ps-ig-examples/sparked-cdg-journeys overlap this feature exists to surface. Fixed by
      resolving journey member ids against the index; overlap now appears in all three of an
      entity's listings.)
- [x] 5.5 Add the generation stamp: source commit of the test data, generation date, and the
      revision each external source was read at.
- [x] 5.6 Verify: the page renders on GitHub with no horizontal scroll, every internal slug
      anchor resolves, and collapsed sections expand. (14/14 anchors resolve, 0 broken links,
      idempotent across two runs apart from the timestamp.)

## 6. Skill and command

- [ ] 6.1 Write `.claude/skills/regenerate-data-subsets-wiki/SKILL.md` covering the five-step
      procedure: preconditions, run scripts, present new/changed candidates, write back
      confirmations, assemble.
- [ ] 6.2 Write `.claude/skills/regenerate-data-subsets-wiki/references/mechanisms.md` with
      per-subset mechanism detail, loaded on demand rather than inlined in `SKILL.md`.
- [ ] 6.3 Write `.claude/commands/regenerate-data-subsets-wiki.md` as a thin trigger taking an
      optional section argument. It invokes the skill and does not restate the procedure.
- [ ] 6.4 Write `docs/data-subsets/README.md` — a short regeneration pointer for readers who
      are not using the skill.
- [ ] 6.5 Verify: the skill appears in the skill listing after a session restart, and the
      command invokes it.

## 7. First generation

- [x] 7.1 Run a full regeneration end to end, answering the confirmation prompts for
      geography, families, community contributions and missing/suppressed data.
      (All 161 confirmations recorded: 93 geography — 8 metro single-state groupings,
      85 regional windows split 46 auto-confirmed/31 auto-rejected by provider-
      infrastructure presence plus 8 individually reviewed for suburb sprawl (5 confirmed,
      3 rejected including the known Townsville/Mount Isa and remote-Central-Australia
      cases); 57 missing/suppressed — 56 confirmed against verified data-absent-reason
      mechanisms, 1 rejected; 11 families — 7 confirmed via RelatedPerson + Medicare card,
      2 rejected, 2 flagged as potential-unconfirmed. community-contributions needed no
      confirmation — domain match is definitive per its design. Two collision bugs found
      and fixed mid-pass: candidate_key hashing bare ids instead of Type/id (D15), and a
      confirm script's own bare-id dict silently dropping colliding entries — both caught
      by verifying awaiting_decision returned to 0 after each batch, not by trusting the
      batch call succeeded.)
- [ ] 7.2 Confirm the write-back persisted: rerun immediately and check that no candidate is
      presented again.
- [ ] 7.3 Cross-check the generated page against `subsets.yaml` — every seeded fact appears,
      and no fact appears that is not seeded or derived.
- [ ] 7.4 Review `docs/DataSubsets.md` for accuracy against the spec's requirements, then
      commit the whole toolchain to the fork.
