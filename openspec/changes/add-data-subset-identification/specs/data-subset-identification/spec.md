## Purpose

Identifies the logical subsets within the HL7 AU FHIR test data set — which entities belong
to each subset, how membership is determined, who owns and confirmed it, and how subsets
relate to one another — and defines how that information is published as a regenerable wiki
page so users have a human-readable view of the data subsets.

## ADDED Requirements

### Requirement: Subset classification by identification type

Every subset SHALL be classified by how its membership is established, using exactly one of
four types:

- **Derived** — computed from the repository by a deterministic script. No human input.
- **Declared** — stated by an authoritative source outside the wiki, which the wiki
  transcribes. The source SHALL be recorded as a resolvable reference (URL, file path, or
  git ref) so the transcription can be re-checked against it.
- **Curated** — decided by this project, with the facts file as the authoritative home.
  There is no external source to check against, so the entry SHALL record an attester and a
  confirmation date.
- **Derived + Curated** — a script proposes candidate members and a human confirms or
  rejects them.

The distinguishing test between Declared and Curated is whether the fact has a source that
could change without the wiki being told. If it does, it is Declared and needs a source
reference; if it does not, it is Curated and needs an attester.

#### Scenario: Every subset declares its type
- **WHEN** the wiki is generated
- **THEN** each subset section states one of Derived, Declared, Curated, or Derived + Curated

#### Scenario: Declared subsets carry a resolvable source
- **WHEN** a subset is classified Declared
- **THEN** its facts file entry contains a source reference that resolves to a URL, file path, or git ref

#### Scenario: Curated subsets carry an attester
- **WHEN** a subset is classified Curated
- **THEN** its facts file entry contains an attester and a confirmation date

### Requirement: Stable subset identifiers

Each subset SHALL have a stable kebab-case slug that serves as its key in the facts file and
as the anchor by which other subsets reference it. Slugs SHALL NOT change once published,
so that cross-references between subsets and external links into the wiki remain valid.

#### Scenario: Subsets are addressable by slug
- **WHEN** one subset's "relationships to other subsets" property names another subset
- **THEN** it refers to that subset by its slug, and the slug resolves to a section in the wiki

### Requirement: Reservation status of entities

Read-only use of the test data is unconstrained: any entity may be read, loaded, queried or
tested against as the user sees fit, without reference to this wiki. Reservation governs
**write intent** only — adding to or modifying an entity or its network of linked resources —
because new content joins a graph that may already be shaped to serve a stated purpose.

Each subset SHALL state whether its entities are reserved, meaning new or altered content in
their linked resources risks conflicting with the subset's purpose, or are free to build on.

Reservation status is a declared governance property recorded per subset in the facts file.
It SHALL NOT be inferred from how many subsets an entity appears in: an entity may belong to
a single subset and still be free to build on, or belong to several and still be reserved.

Where an entity belongs to more than one subset, its reservation status SHALL be discoverable
from the wiki, so that someone intending to extend the entity can see what it is already
committed to.

#### Scenario: A subset states its reservation status
- **WHEN** a subset section is generated
- **THEN** it states whether the subset's entities are reserved to its purpose or are free to build on

#### Scenario: Read-only use is not constrained
- **WHEN** the wiki states that a subset's entities are reserved
- **THEN** it scopes that reservation to adding to or modifying the entity or its network of linked resources, not to reading or testing against it

#### Scenario: Reservation is declared, not inferred
- **WHEN** a subset contains entities that appear in no other subset
- **THEN** its reservation status is taken from the facts file, not inferred from that entity count

#### Scenario: An entity committed to a reserved subset is discoverable as such
- **WHEN** an entity belongs to more than one subset and at least one of those reserves it
- **THEN** the wiki makes that reservation discoverable from the entity's other listings, so the overlap is visible before the entity is extended

### Requirement: Identification of AU Core IG example entities

The wiki SHALL identify test data entities that are also used as examples in the AU Core
implementation guide, by matching against the example set in the `hl7au/au-fhir-core`
repository under `input/examples/`.

Matching SHALL be on resource identity (resource id, or business identifier where ids
differ) and SHALL NOT require byte-equality of the resource content: IG examples are
published with some Services Australia identifier data intentionally stripped, so an entity
and its IG-example counterpart may legitimately differ in content while being the same
entity.

#### Scenario: An entity used as an AU Core IG example is identified
- **WHEN** a test data entity matches an example in `hl7au/au-fhir-core/input/examples/` on resource identity
- **THEN** the wiki lists that entity under the AU Core IG example subset

#### Scenario: Stripped identifier data does not prevent a match
- **WHEN** a test data entity and its IG example counterpart share a resource identity but differ in identifier content
- **THEN** the entity is still identified as a member of the subset

### Requirement: Identification of AU Patient Summary IG example entities

The wiki SHALL identify test data entities used as examples in the AU Patient Summary
implementation guide. Because AU PS examples are document Bundles rather than individual
resource files, entities SHALL be extracted from `Bundle.entry` and matched back to test
data instances on business identifier.

#### Scenario: An entity inside an AU PS example Bundle is identified
- **WHEN** a resource within an AU PS example Bundle matches a test data instance on business identifier
- **THEN** the wiki lists that test data entity under the AU PS IG example subset

### Requirement: Identification of AU eRequesting IG example entities

The wiki SHALL identify test data entities that are also used as examples in the AU
eRequesting implementation guide, by matching against the example set in the
`hl7au/au-fhir-erequesting` repository under `input/examples/`, on the same matching basis
as the AU Core IG example subset.

#### Scenario: An entity used as an AU eRequesting IG example is identified
- **WHEN** a test data entity matches an example in `hl7au/au-fhir-erequesting/input/examples/` on resource identity
- **THEN** the wiki lists that entity under the AU eRequesting IG example subset

### Requirement: Identification of Inferno AU Core test suite default patients

The wiki SHALL identify the patients that the AU Core Inferno test kit uses as its default
patient set — the patients that together exercise all Must Support elements. This subset is
Declared: its authoritative source is the default patient id list in the
`inferno_suite_generator` repository, read at its current revision on each generation. The
revision read SHALL be recorded, so that a later drift report can name what changed.

#### Scenario: The Inferno default patients are listed
- **WHEN** the wiki is generated
- **THEN** it lists the patients transcribed from the Inferno source, and states that source and the revision read

#### Scenario: Drift from the Inferno source is surfaced
- **WHEN** the Inferno source at its current revision no longer matches the transcribed list
- **THEN** the discrepancy is reported to the operator rather than silently overwritten

### Requirement: Identification of AU Patient Summary test patients

The wiki SHALL identify the primary test patients for AU Patient Summary testing — those for
which the `$summary` operation can be invoked. This subset is Declared: its authoritative
source is the AU PS Test Data Coverage page, referenced by URL in the facts file and read at
its current state on each generation. The page revision or last-modified date read SHALL be
recorded, so that a later drift report can name what changed.

#### Scenario: The AU PS test patients are listed
- **WHEN** the wiki is generated
- **THEN** it lists the AU PS test patients and states the source page and the revision read

### Requirement: Identification of Smart Health Checks entities

The wiki SHALL identify the entities used for Smart Health Checks demonstrators and testing. This subset is
Curated: membership is a project decision recorded in the facts file with an attester, and
changes when a maintainer adds or removes an entity.

#### Scenario: Smart Health Checks entities are listed
- **WHEN** the wiki is generated
- **THEN** it lists the entities recorded under the Smart Health Checks subset in the facts file

#### Scenario: A maintainer adds an entity to the subset
- **WHEN** a maintainer records an additional entity under the Smart Health Checks subset in the facts file
- **THEN** the next generation includes that entity, with the attester and confirmation date shown

### Requirement: Identification of Sparked Clinical Design Group journey entities

The wiki SHALL identify entities used in Sparked Clinical Design Group consumer journeys,
grouped by named journey, with the owning organisation recorded as Sparked. Journey members
SHALL be recorded in the facts file as resolved resource ids rather than display names, so
that membership is unambiguous.

Membership of this subset does not imply exclusivity. Entities used in a Clinical Design
Group consumer journey may also appear in the corresponding IG project use cases, which may
in turn be progressed into technical use cases. The wiki SHALL therefore record this subset
as reusable rather than reserved, and SHALL surface the downstream use cases an entity has
been carried into as a relationship, so that a reader can see where a journey entity is
already in play before reusing it. Downstream use is Curated: there is no source document
identifying it, so it is recorded as a manual entry in the facts file, with an attester and
confirmation date per the classification requirement above.

Where a journey states a participant's role, that stated role SHALL be recorded as
authoritative for the journey, alongside the specialty declared by the entity's own
PractitionerRole. Where the two differ, the wiki SHALL surface the difference rather than
preferring either silently — a journey routinely distinguishes roles (inpatient versus
outpatient, or a named specialisation) that a coded specialty does not capture.

A journey participant named without a corresponding resource — a care team rather than an
individual — SHALL still be listed, marked as unresolved, so the gap is visible.

A journey whose participants exist but whose clinical narrative does not SHALL state that,
rather than implying the journey is fully represented in the data.

#### Scenario: AU PS consumer journey entities are listed by journey
- **WHEN** the wiki is generated
- **THEN** each AU PS consumer journey is listed as a named group with its member entities

#### Scenario: Journey entities are shown as reusable, not reserved
- **WHEN** an entity belongs to a Clinical Design Group consumer journey
- **THEN** the wiki shows it as reusable, and its journey membership does not mark it as reserved to that journey

#### Scenario: Downstream use of a journey entity is visible
- **WHEN** a journey entity has been carried into an IG project use case or a technical use case
- **THEN** the wiki records that downstream use as a relationship on the entity's journey listing

#### Scenario: A journey with no declared content is shown as pending
- **WHEN** a journey group has no members recorded in the facts file
- **THEN** the wiki shows it as pending with the reason stated, rather than omitting it

#### Scenario: A stated journey role differs from the declared specialty
- **WHEN** a journey states a participant's role and the entity's PractitionerRole declares a different or less specific specialty
- **THEN** the wiki shows both, identifying which is the journey's stated role and which is the declared specialty

#### Scenario: A journey participant with no resource is still listed
- **WHEN** a journey names a participant that has no corresponding resource in the data set
- **THEN** the wiki lists it as an unresolved member rather than omitting it

#### Scenario: A journey with participants but no clinical narrative says so
- **WHEN** a journey's participants resolve but the clinical events it describes do not exist in the data set
- **THEN** the wiki states that the journey is not fully represented, rather than implying it is

### Requirement: Identification of Connected Care journey entities

The wiki SHALL identify entities belonging to the Connected Care consumer journeys, with the
owning organisation recorded as DoHAC. These entities reside on the `connected-care` branch
rather than the default branch, so this subset SHALL be derived from that branch.

Alex's Story is Declared: its authoritative source is the data set document held alongside
the instances in the `connected-care` directory. Yuri's Story is also Declared, but its
source document is **blocked scope** — not yet available. Until it is supplied, entities in
the `connected-care` directory that are not identified as Alex's Story SHALL be attributed
to Yuri's Story as a stated provisional assumption, not as a confirmed fact.

#### Scenario: Alex's Story entities are identified from its source document
- **WHEN** an entity is named in the Alex's Story data set document
- **THEN** the wiki lists it under Alex's Story, citing that document as the source

#### Scenario: The provisional Yuri's Story attribution is marked as such
- **WHEN** entities are attributed to Yuri's Story by remainder rather than by a source document
- **THEN** the wiki states that the attribution is provisional and names the missing source as the blocker

### Requirement: Identification of community contributions

The wiki SHALL identify entities contributed by community organisations, attributed by the
author or committer email domain on the commits that introduced them.

Because this mechanism is best-effort — a contributor using a personal email address, or a
merge that did not preserve original authorship, is not detected — the subset SHALL support
human-confirmed additions recorded in the facts file, and the wiki SHALL state that the
derived attribution is not exhaustive.

#### Scenario: An entity introduced by a recognised organisation domain is attributed
- **WHEN** the commit introducing an entity has an author or committer email on a recognised organisation domain
- **THEN** the wiki lists that entity under that organisation's community contributions

#### Scenario: The limits of git-based attribution are stated
- **WHEN** the community contributions section is generated
- **THEN** it states that attribution derives from commit authorship and may under-report

### Requirement: Identification of missing and suppressed data examples

The wiki SHALL identify test data instances that demonstrate missing or suppressed data,
drawing on the maintained documentation of those cases in the repository.

The generation process SHALL additionally scan for instances whose resource ids contain
keywords indicating missing or suppressed data, and SHALL prompt the operator to confirm
whether newly matching instances belong to the subset, rather than adding them automatically.

#### Scenario: Documented missing and suppressed instances are listed
- **WHEN** the wiki is generated
- **THEN** it lists the instances recorded in the repository's missing and suppressed data documentation

#### Scenario: A newly matching instance is queued for confirmation
- **WHEN** an instance not already in the subset has a resource id matching a missing or suppressed data keyword
- **THEN** the operator is prompted to confirm or reject its membership before it is added

### Requirement: Identification of scenario groupings

The wiki SHALL identify entities grouped by consumer journey scenario. This subset is seeded
once from the historical scenario directory structure at a pinned git ref, after which the
facts file becomes its authoritative home and membership is maintained by curation.

The wiki SHALL record that the pinned git ref was the seed source, so the origin of the
grouping remains traceable after it stops being consulted.

#### Scenario: Scenario groups are listed with their members
- **WHEN** the wiki is generated
- **THEN** each scenario group is listed as a named group with its member entities

#### Scenario: The seed source remains traceable after curation takes over
- **WHEN** the scenario groupings section is generated
- **THEN** it records the pinned git ref the groupings were originally seeded from

### Requirement: Identification of geographic groupings

The wiki SHALL propose groupings of Practitioner, Organization, Location, Patient and
RelatedPerson entities that are plausibly co-located, using the leading digits of the address
postcode as the proximity signal.

Each proposed grouping SHALL be expanded to include entities reachable by reverse reference —
HealthcareServices referencing a grouped Organization or Location, and PractitionerRoles
referencing a grouped Practitioner — and SHALL incorporate scenario groupings, whose members
are typically co-located by construction.

Because postcode proximity is a weak proxy for a meaningful grouping, proposals SHALL be
presented to a human for confirmation and only confirmed groupings SHALL be published as
such. The wiki SHALL describe this subset as best-effort.

#### Scenario: A candidate geographic grouping is proposed for confirmation
- **WHEN** entities share a leading postcode prefix
- **THEN** they are proposed as a candidate grouping for human confirmation, not published directly

#### Scenario: Reverse-referenced entities join the grouping
- **WHEN** a grouping contains an Organization, Location or Practitioner
- **THEN** HealthcareServices and PractitionerRoles referencing those entities are included in the grouping

### Requirement: Identification of families

The wiki SHALL identify entities that constitute a family. Two primary mechanisms apply, and
neither is subordinate to the other:

- **A shared Medicare card.** An Australian Medicare number is a card number plus a
  per-person Individual Reference Number, so members of one family on one card differ only
  in that reference number. This is the administrative statement of a family unit.
- **The RelatedPerson network.** A RelatedPerson's reference to a Patient, together with its
  relationship code, establishes a family link directly.

Neither mechanism subsumes the other, so both SHALL be applied and their results combined: a
person not yet on the card (a newborn) is found only by the RelatedPerson network, while a
family whose RelatedPerson links are absent is found only by the shared card.

A secondary mechanism SHALL propose additional candidate family members on the basis of
matching surname and/or matching address. Family members are not required to share an
address, so neither secondary signal alone is conclusive; candidates found this way SHALL be
presented to a human for validation and published only once confirmed.

Where a candidate can be neither confirmed nor rejected because the evidence that would
settle it is unavailable, the wiki SHALL record it as potentially related and unconfirmed,
stating what is missing — rather than forcing it into a binary the evidence does not support.

#### Scenario: A family is identified from the RelatedPerson network
- **WHEN** a RelatedPerson references a Patient with a family relationship code
- **THEN** those entities are identified as members of the same family

#### Scenario: A family is identified from a shared Medicare card
- **WHEN** two entities' Medicare numbers differ only in the individual reference number
- **THEN** they are identified as members of the same family

#### Scenario: A family member not on the card is still identified
- **WHEN** a person has no Medicare number but is linked by a RelatedPerson relationship code
- **THEN** they are included in the family found by the shared card

#### Scenario: A surname or address match is proposed rather than asserted
- **WHEN** entities share a surname and/or an address but no RelatedPerson link connects them
- **THEN** they are presented to a human as candidate family members for validation

#### Scenario: An unresolvable candidate is recorded as potentially related
- **WHEN** a candidate cannot be settled because the evidence that would decide it is unavailable
- **THEN** the wiki records it as potentially related and unconfirmed, stating what is missing

### Requirement: Identification of blank-slate patients

The wiki SHALL identify patients that have no clinical data associated with them — patients
not referenced as the subject of any clinical resource. This answers which patients can be
selected for a new consumer journey, or matched with externally generated data, without
pre-existing clinical content conflicting with what is to be created.

#### Scenario: A patient with no referencing clinical resource is identified
- **WHEN** no clinical resource in the data set references a patient as its subject
- **THEN** the wiki lists that patient as a blank-slate patient

### Requirement: Subset section structure

Each subset section in the wiki SHALL present, in a consistent order: its purpose; its
ownership and governance, naming the accountable owner and any restriction on changing its
entities; its data provenance and intended use; its relationships to other subsets; and how
the subset is identified, covering both the mechanism and the classification type.

Where a property does not apply or is not yet known, the section SHALL say so explicitly
rather than omitting the field.

Statements that hold for every subset SHALL be made once at page level rather than repeated
per subset — specifically, that reservation governs writing and never reading, and the
external source versions the generation was run against.

#### Scenario: A subset section carries the full property set
- **WHEN** a subset section is generated
- **THEN** it presents purpose, ownership and governance, provenance and use, relationships, and how the subset is identified

#### Scenario: A page-level statement is not repeated per subset
- **WHEN** a statement holds for every subset — that reservation governs writes not reads, or which external source versions were read
- **THEN** the page states it once rather than repeating it in each subset section

#### Scenario: An unknown property is stated rather than omitted
- **WHEN** a subset property is not applicable or not yet known
- **THEN** the section states that explicitly rather than leaving the field absent

### Requirement: Entity list presentation

Lists of entities SHALL be grouped by FHIR resource type. Where a list is large, it SHALL be
rendered so that it is collapsed by default and can be expanded on demand, keeping the page
scannable.

#### Scenario: Entities are grouped by resource type
- **WHEN** a subset section lists its member entities
- **THEN** the entities are grouped under their FHIR resource type

#### Scenario: A large list is collapsed by default
- **WHEN** an entity list exceeds the size threshold
- **THEN** it is rendered collapsed, expandable on demand

### Requirement: Manual regeneration

Regeneration of the wiki SHALL be triggered manually by an operator. It SHALL NOT be
triggered automatically by commits to the test data repository, so that the published page
changes only when someone has reviewed the result.

#### Scenario: A commit does not regenerate the wiki
- **WHEN** a commit lands in the test data repository
- **THEN** the wiki is not regenerated as a consequence

### Requirement: Generation stamp

The generated wiki SHALL record what it was generated from: the source commit of the test
data it describes, and the date of generation. This allows a reader to determine whether the
page is current with respect to the data set.

#### Scenario: The wiki states its generation basis
- **WHEN** the wiki is generated
- **THEN** it records the source commit of the test data and the generation date

### Requirement: Confirmation persistence

Where a subset requires human confirmation, confirmed decisions SHALL be persisted together
with the attester and the confirmation date. Subsequent regeneration SHALL present only
candidates that are new or changed since the last confirmation, and SHALL NOT re-ask
questions that have already been answered.

Hand-authored facts and machine-recorded decisions SHALL be kept in separate files, so that
persisting a decision cannot overwrite hand-authored content.

A candidate's identity SHALL derive from its membership, so that a candidate whose membership
has changed is treated as new and put to the operator again rather than inheriting a decision
made about a different set of entities.

#### Scenario: A confirmed decision is not re-asked
- **WHEN** the wiki is regenerated after a candidate has been confirmed or rejected
- **THEN** that candidate is not presented for confirmation again

#### Scenario: A changed candidate is re-asked
- **WHEN** a previously decided candidate is regenerated with a different set of member entities
- **THEN** it is presented to the operator again rather than inheriting the earlier decision

#### Scenario: Recording a decision leaves hand-authored facts untouched
- **WHEN** a confirmation is persisted
- **THEN** the hand-authored facts file is not rewritten

#### Scenario: A new candidate is presented
- **WHEN** regeneration finds a candidate that has not previously been confirmed or rejected
- **THEN** that candidate is presented to the operator for a decision
