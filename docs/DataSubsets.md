# HL7 AU FHIR Test Data — Data Subsets

Identifies the logical subsets of the test data set: which entities belong to each, how membership is established, who owns it, and how subsets relate to one another. See [docs/data-subsets/README.md](data-subsets/README.md) for how to regenerate this page.

### Why these subsets are worth tracking

The administrative entities in this data set — Patient, RelatedPerson, Practitioner, PractitionerRole, Organization, HealthcareService, Location and Endpoint — cannot simply be created or modified on demand within this project. Their key identifiers and some core attributes are allocated by Services Australia and correspond to entities provisioned in the HI Vendor Test Environment; the instances here map those records into FHIR and may include some data enrichment, but generally need to stay aligned with them.

Using the test data therefore tends to start with finding entities that already fit, since requesting new ones is a considerably more costly path. That requires knowing which entities are already committed to a purpose that new content could disturb, which are free to build on, and which suit a new need — co-located for a plausible consumer journey, related as a family, or carrying no clinical data at all. This page is where that is recorded.

### What is in scope

Only the eight administrative entity types listed above. Clinical resources carry far less shared governance with external parties and can be authored more freely, so tracking their subset membership is low value — and where clinical content is needed, it is retrievable from the administrative entity by ordinary FHIR mechanisms. One subset is exempt: *Missing and suppressed data examples*, whose instances demonstrate the correct representation of absent data, a property that attaches to an Observation exactly as it does to a Patient.

### Reading versus writing

**Reading is always unconstrained.** Any entity may be read, loaded, queried or tested against without reference to this page. Where a subset's governance restricts something, it restricts *writing* — adding to or modifying an entity or its network of linked resources — because new content joins a graph that may already be shaped to serve a stated purpose.

### How each subset is identified

Every section closes with a classification. The four are defined below; the practical difference is what each needs in order to be trustworthy.

<details><summary>What the four classifications mean</summary>

- **Derived** — computed from the repository by a deterministic script, with no human input. Recomputed on every regeneration, so it is current by construction.
- **Declared** — stated by an authoritative source outside this page, which the page transcribes. Records a resolvable source reference so the transcription can be re-checked, and reports drift rather than silently overwriting.
- **Curated** — decided by this project, with no external source to check against. Records an attester and a confirmation date instead.
- **Derived + Curated** — a script proposes candidate members and a human confirms or rejects each one. Confirmations are persisted, so a regeneration asks only about what is new or changed.

The distinguishing test between Declared and Curated is whether the fact has a source that could change without this page being told. If it does, it is Declared and needs a source reference; if it does not, it is Curated and needs an attester. That is why some sections show a **Source** and others show an attester.

</details>

_Generated 2026-09-01 15:55 UTC from test data at commit `188c3702a6170f6ebec1853bc5e25e44ea3b74bc`. This page is regenerated manually — see [docs/data-subsets/README.md](data-subsets/README.md)._

## Contents

- [AU Core IG example entities](#au-core-ig-examples)
- [AU Patient Summary IG example entities](#au-ps-ig-examples)
- [AU eRequesting IG example entities](#au-erequesting-ig-examples)
- [Inferno AU Core test suite default patients](#inferno-default-patients)
- [AU Patient Summary test patients](#au-ps-test-patients)
- [Smart Health Checks](#smart-health-checks)
- [Sparked Clinical Design Group consumer journeys](#sparked-cdg-journeys)
- [Connected Care consumer journeys](#connected-care-journeys)
- [Community contributions](#community-contributions)
- [Missing and suppressed data examples](#missing-suppressed-data)
- [Scenario groupings](#scenario-groups)
- [Geographic groupings](#geography-groups)
- [Families](#families)
- [Blank-slate patients](#blank-slate-patients)

## AU Core IG example entities <a id="au-core-ig-examples"></a>

### Purpose

Identifies the administrative entities and resources used in the AU Core IG examples.

### Ownership & governance

**Owner:** AU Core IG authors  
Published IG examples must not be modified, added to, or removed without coordination with and approval from the IG authors.

### Provenance & use

Generally derived from Services Australia data mapped to FHIR, with some data enrichment and subsequent curation for the AU Core IG examples. Some mapped data has been stripped to focus the examples on demonstrating support for Must Support elements. The examples are illustrative, not normative or fully representative of real-world data.

### Relationships

Some members are also included in the [Inferno AU Core test suite default patients](#inferno-default-patients) subset.

### How is this subset identified?

Derived automatically. Each entity in this data set is matched against the example set published in the AU Core IG repository under input/examples/. Matching is on resource identity — resource id, or business identifier where the ids differ — never on content, because IG examples are published with some Services Australia identifier data stripped.


**Source:** hl7au/au-fhir-core, input/examples/

**Read at:** [`36e9c7ff08da`](https://github.com/hl7au/au-fhir-core/commit/36e9c7ff08da794cf381802a977a56502e9c715e) — the AU Core IG revision this page was last generated from.

_Classification: Derived._
> 30 distinct administrative entities are published as examples in hl7au/au-fhir-core.
> 51 non-administrative entities excluded: Observation x17, Condition x4, Medication x4, MedicationStatement x4, AllergyIntolerance x3, Encounter x3, MedicationDispense x3, MedicationRequest x3, DiagnosticReport x2, DocumentReference x2, Immunization x2, Procedure x2, Composition x1, Specimen x1. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.
> 2 IG example resources matched nothing in the test data set; they may be IG-only examples. Listed under evidence.

### Members (30)

<details><summary>30 entities — click to expand</summary>

**Patient** (5)

- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `bennelong-anne` — `au-fhir-test-data-set/au-core/Patient-bennelong-anne.json`
- `howe-deangelo` — `au-fhir-test-data-set/au-core/Patient-howe-deangelo.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `irvine-ronny-lawrence` — `au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `wang-li` — `au-fhir-test-data-set/au-core/Patient-wang-li.json`

**PractitionerRole** (4)

- `bobrester-bob-gp` — `au-fhir-test-data-set/au-core/PractitionerRole-bobrester-bob-gp.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `cardiologist-sutherland-sallie` — `au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-sutherland-sallie.json`
- `pharmacist-megan-peterson` — `au-fhir-test-data-set/au-core/PractitionerRole-pharmacist-megan-peterson.json`
- `surgeon-chau-fryer` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeon-chau-fryer.json`

**Practitioner** (5)

- `bobrester-bob` — `au-fhir-test-data-set/au-core/Practitioner-bobrester-bob.json`
- `chau-fryer` — `au-fhir-test-data-set/au-core/Practitioner-chau-fryer.json`
- `mackay-darleen` — `au-fhir-test-data-set/au-core/Practitioner-mackay-darleen.json`
- `megan-peterson` — `au-fhir-test-data-set/au-core/Practitioner-megan-peterson.json`
- `sutherland-sallie` — `au-fhir-test-data-set/au-core/Practitioner-sutherland-sallie.json`

**HealthcareService** (2)

- `murrabit-crisis-hotline` — `au-fhir-test-data-set/au-core/HealthcareService-murrabit-crisis-hotline.json`
- `physiotherapy` — `au-fhir-test-data-set/au-core/HealthcareService-physiotherapy.json`

**Organization** (5)

- `appin-pharmacy` — `au-fhir-test-data-set/au-core/Organization-appin-pharmacy.json`
- `bobrester-medical-center` — `au-fhir-test-data-set/au-core/Organization-bobrester-medical-center.json`
- `mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/Organization-mitchells-hill-audiology.json`
- `murrabit-public-hospital` — `au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json`
- `pullabooka-pathology` — `au-fhir-test-data-set/au-core/Organization-pullabooka-pathology.json`

**Location** (2)

- `bobrester-medical-center` — `au-fhir-test-data-set/au-core/Location-bobrester-medical-center.json`
- `patient-home` — `au-fhir-test-data-set/au-core/Location-patient-home.json`

**Endpoint** (5)

- `bobrester-fhir-rest` — `au-fhir-test-data-set/au-core/Endpoint-bobrester-fhir-rest.json`
- `hl7au-dev-terminology-fhir-rest` — `au-fhir-test-data-set/au-core/Endpoint-hl7au-dev-terminology-fhir-rest.json`
- `mh-audiology-smd` — `au-fhir-test-data-set/au-core/Endpoint-mh-audiology-smd.json`
- `murrabit-hospital-hl7-v2-mllp` — `au-fhir-test-data-set/au-core/Endpoint-murrabit-hospital-hl7-v2-mllp.json`
- `sparked-aucore-fhir-rest` — `au-fhir-test-data-set/au-core/Endpoint-sparked-aucore-fhir-rest.json`

**RelatedPerson** (2)

- `banks-mia-leanne-father` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-mia-leanne-father.json` — *also in: [families](#families) (free to build on)*
- `wang-li-friend` — `au-fhir-test-data-set/au-core/RelatedPerson-wang-li-friend.json`

</details>


## AU Patient Summary IG example entities <a id="au-ps-ig-examples"></a>

### Purpose

Identifies the administrative entities used in the AU Patient Summary IG examples.

### Ownership & governance

**Owner:** AU Patient Summary IG authors  
Published IG examples must not be modified, added to, or removed without coordination with and approval from the IG authors.

### Provenance & use

Generally derived from Services Australia data mapped to FHIR, with some data enrichment and subsequent curation for the AU PS IG examples. The examples are illustrative, not normative or fully representative of real-world data.

### Relationships

A small number of members are also [AU Core IG example entities](#au-core-ig-examples).

### How is this subset identified?

Derived automatically. AU PS examples are document Bundles rather than one resource per file, so entities are extracted from Bundle.entry and matched back to this data set on business identifier — resource ids inside a Bundle are not reliable keys.


**Source:** hl7au/au-fhir-ps, input/examples/ (Bundle.entry, matched by business identifier)

**Read at:** [`0f87741264db`](https://github.com/hl7au/au-fhir-ps/commit/0f87741264db7a9cb5aa7410e50476ee5884f419) — the AU Patient Summary IG revision this page was last generated from.

_Classification: Derived._
> 16 distinct administrative entities are published as examples in hl7au/au-fhir-ps.
> 1 non-administrative entities excluded: Immunization x1. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.
> 155 of the resources scanned came from Bundle entries, matched on business identifier only — ids inside a Bundle are not reliable keys.
> 133 IG example resources matched nothing in the test data set; they may be IG-only examples. Listed under evidence.

### Members (16)

**Patient** (5)

- `banks-jeramy-ezra` — `au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `johnson-joyce` — `au-fhir-test-data-set/au-core/Patient-johnson-joyce.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `martin-shawn` — `au-fhir-test-data-set/au-core/Patient-martin-shawn.json`
- `morris-charlotte` — `au-fhir-test-data-set/au-core/Patient-morris-charlotte.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**PractitionerRole** (3)

- `bobrester-bob-gp` — `au-fhir-test-data-set/au-core/PractitionerRole-bobrester-bob-gp.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*
- `diagnostic-burdett-palmer` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-burdett-palmer.json`
- `generalpractitioner-burrows-ginger` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json`

**Practitioner** (3)

- `burdett-palmer` — `au-fhir-test-data-set/au-core/Practitioner-burdett-palmer.json`
- `burrows-ginger` — `au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `lowe-abe` — `au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**Organization** (5)

- `adv-hearing-care` — `au-fhir-test-data-set/au-core/Organization-adv-hearing-care.json`
- `bungabbee-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json`
- `douglas-radiology` — `au-fhir-test-data-set/au-core/Organization-douglas-radiology.json`
- `kensington-public-hospital` — `au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json`
- `mossy-point-medical-centre` — `au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json`


## AU eRequesting IG example entities <a id="au-erequesting-ig-examples"></a>

### Purpose

Identifies the administrative entities used in the AU eRequesting IG examples.

### Ownership & governance

**Owner:** AU eRequesting IG authors  
Published IG examples must not be modified, added to, or removed without coordination with and approval from the IG authors.

### Provenance & use

Generally derived from Services Australia data mapped to FHIR, with some data enrichment and subsequent curation for the AU eRequesting IG examples. The examples are illustrative, not normative or fully representative of real-world data.

### Relationships

No notable relationships to other subsets.

### How is this subset identified?

Derived automatically, on the same basis as the AU Core IG examples — matched against input/examples/ in the AU eRequesting IG repository on resource identity rather than content. This IG also ships Bundles, whose entries are extracted and matched on business identifier.


**Source:** hl7au/au-fhir-erequesting, input/examples/

**Read at:** [`224341319362`](https://github.com/hl7au/au-fhir-erequesting/commit/2243413193629b004c5edc4fec33a31e2ff6ceb9) — the AU eRequesting IG revision this page was last generated from.

_Classification: Derived._
> 16 distinct administrative entities are published as examples in hl7au/au-fhir-erequesting.
> 20 non-administrative entities excluded: ServiceRequest x8, CommunicationRequest x4, Coverage x2, Encounter x2, Consent x1, DocumentReference x1, Observation x1, Task x1. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.
> 35 of the resources scanned came from Bundle entries, matched on business identifier only — ids inside a Bundle are not reliable keys.
> 19 IG example resources matched nothing in the test data set; they may be IG-only examples. Listed under evidence.

### Members (16)

**Patient** (3)

- `belger-remedios` — `au-fhir-test-data-set/au-erequesting/Patient-belger-remedios.json`
- `roberts-fred` — `au-fhir-test-data-set/au-erequesting/Patient-roberts-fred.json`
- `scott-elijah-ken` — `au-fhir-test-data-set/au-erequesting/Patient-scott-elijah-ken.json`

**PractitionerRole** (4)

- `diagnostic-mclaughlin-kimberlee` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mclaughlin-kimberlee.json`
- `generalpractitioner-guthridge-jarred` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json`
- `obstetrician-losch-sallie` — `au-fhir-test-data-set/au-erequesting/PractitionerRole-obstetrician-losch-sallie.json`
- `pathologist-herbert-aimee` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-herbert-aimee.json`

**Practitioner** (4)

- `guthridge-jarred` — `au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json`
- `herbert-aimee` — `au-fhir-test-data-set/au-core/Practitioner-herbert-aimee.json`
- `losch-sallie` — `au-fhir-test-data-set/au-erequesting/Practitioner-losch-sallie.json`
- `mclaughlin-kimberlee` — `au-fhir-test-data-set/au-core/Practitioner-mclaughlin-kimberlee.json`

**Organization** (4)

- `barney-view-private-hospital` — `au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json`
- `elimbah-medical-centre` — `au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json`
- `kioma-pathology` — `au-fhir-test-data-set/au-core/Organization-kioma-pathology.json`
- `mount-charlton-radiology` — `au-fhir-test-data-set/au-core/Organization-mount-charlton-radiology.json`

**Location** (1)

- `barney-view-private-hospital` — `au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json`


## Inferno AU Core test suite default patients <a id="inferno-default-patients"></a>

### Purpose

Identifies the patients the AU Core Inferno test kit uses as its default patient set.

### Ownership & governance

**Owner:** inferno_suite_generator maintainers  
The set is relied on to exercise every Must Support element in combination. Adding to or modifying these patients or their linked resources must preserve that coverage, and should be coordinated with the test kit maintainers.

### Provenance & use

Stated by the Inferno test kit itself rather than decided here. The set is intended to give full Must Support coverage, but that is an intent rather than a guarantee — nothing verifies that it achieves full coverage or that it is the smallest set that does.

### Relationships

Six of the seven members are also [AU Patient Summary test patients](#au-ps-test-patients), so a change affecting one set very likely affects the other. A few are also [AU Core IG example entities](#au-core-ig-examples).

### How is this subset identified?

Declared, then drift-checked. The patient id list is read from the inferno_suite_generator repository at its current revision on every regeneration and compared against the list recorded here; any difference is reported rather than silently overwritten.


**Source:** inferno_suite_generator, lib/inferno_suite_generator/utils/helpers.rb, method default_patient_ids_string (lines 217-219 at time of transcription)

**Read at:** [`f4c668d05c1d`](https://github.com/hl7au/inferno_suite_generator/commit/f4c668d05c1da45ee14076b81634e89f255180b3) — the Inferno test kit revision this page was last generated from.

_Classification: Declared._
> No drift: source matches the transcribed list.

### Members (7)

**Patient** (7)

- `baby-banks-john` — `au-fhir-test-data-set/au-core/Patient-baby-banks-john.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD)*
- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD)*
- `baratz-toni` — `au-fhir-test-data-set/au-core/Patient-baratz-toni.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD)*
- `hayes-arianne` — `au-fhir-test-data-set/au-core/Patient-hayes-arianne.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD)*
- `howe-deangelo` — `au-fhir-test-data-set/au-core/Patient-howe-deangelo.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD)*
- `irvine-ronny-lawrence` — `au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD)*
- `italia-sofia` — `au-fhir-test-data-set/au-core/Patient-italia-sofia.json`


## AU Patient Summary test patients <a id="au-ps-test-patients"></a>

### Purpose

Identifies the primary test patients for AU Patient Summary testing — those for which the $summary operation can be invoked.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Relied on for $summary operation testing. Adding to or modifying these patients or their linked resources must preserve that coverage.

### Provenance & use

Declared by the AU PS Test Data Coverage page maintained by the project, rather than derived from the data set.

### Relationships

Six of the seven members are also [Inferno AU Core test suite default patients](#inferno-default-patients), so a change affecting one set very likely affects the other.

### How is this subset identified?

Declared. The patient list is transcribed from the AU PS Test Data Coverage page and recorded here; the page is re-read on each regeneration so that divergence can be reported.


**Source:** https://confluence.hl7.org/spaces/HAFWG/pages/404097954/AU+PS+Test+Data+Coverage

_Classification: Declared._
### Members (6)

**Patient** (6)

- `baby-banks-john` — `au-fhir-test-data-set/au-core/Patient-baby-banks-john.json` — *also in: [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `baratz-toni` — `au-fhir-test-data-set/au-core/Patient-baratz-toni.json` — *also in: [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `hayes-arianne` — `au-fhir-test-data-set/au-core/Patient-hayes-arianne.json` — *also in: [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `howe-deangelo` — `au-fhir-test-data-set/au-core/Patient-howe-deangelo.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `irvine-ronny-lawrence` — `au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*


## Smart Health Checks <a id="smart-health-checks"></a>

### Purpose

Identifies the entities used for Smart Health Checks demonstrators and testing.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
These entities are relied on for Smart Health Checks demonstrators and testing. Adding to or modifying them or their linked resources risks changing what those demonstrators show, so it should be coordinated with the project team.

### Provenance & use

Derived from Services Australia data mapped to FHIR, in common with the rest of the au-core data set. Smart Health Checks work may use these entities; data generated by that work is not currently contributed back into this repository.

### Relationships

Its single member also appears in [Families](#families). It carries no clinical data here, so it is also a [Blank-slate patients](#blank-slate-patients) member — but Smart Health Checks data generated against it lives outside this repository, so it is less free of prior content than that listing suggests.

### How is this subset identified?

Curated. Membership is stated by a maintainer in the facts file and changes only when a maintainer adds or removes an entity.


_Classification: Curated._
### Members (1)

**Patient** (1)

- `ballantyne-kelvin-hans` — `au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json` — *also in: [families](#families) (free to build on)*


## Sparked Clinical Design Group consumer journeys <a id="sparked-cdg-journeys"></a>

### Purpose

Identifies the entities used in Sparked Clinical Design Group consumer journeys, grouped by named journey.

### Ownership & governance

**Owner:** Sparked  
Journey membership does not reserve an entity. An entity used in a journey may also appear in the corresponding IG project use case and be progressed into a technical use case, so these entities are free to build on.

### Provenance & use

Declared by the Sparked Clinical Design Group. Members are recorded as resolved resource ids rather than display names so membership is unambiguous.

### Relationships

Several members also appear in [Scenario groupings](#scenario-groups), and some are [AU Patient Summary IG example entities](#au-ps-ig-examples).

### How is this subset identified?

Curated. Journey membership is stated by Sparked and recorded in the facts file; the AU Encounter Records journey additionally records each participant's stated journey role alongside the specialty declared by their PractitionerRole, because the two often differ.


_Classification: Curated._
> **Chemotherapy — acute admission to HITH and outpatient care**
> Case scenario: Kendall presented for chemotherapy but was acutely unwell, requiring inpatient admission and multidisciplinary treatment before transitioning to Hospital in the Home and ongoing outpatient care.
> Status: CARE TEAM ONLY. The 11 named individuals resolve to existing test data, but the clinical narrative this journey describes — chemotherapy, the acute inpatient admission, the HITH transition and outpatient follow-up — does not exist as test data yet. No chemotherapy or admission Encounter references Kendall.
> CONFLICT — `Patient/sandilands-kendall`: Already carries unrelated clinical content: an ambulatory GP visit (Encounter/gpvisit, SNOMED 866149003 "Annual visit"), a pathology ServiceRequest (path-scenario-1) with two eRequesting Tasks, and two Coverage resources. None of it belongs to this chemotherapy journey. New journey content will join that existing graph.

### Members (19)

<details><summary><strong>chemotherapy-acute-admission-to-hith</strong> (13 entities)</summary>

**Patient** (1)

- `sandilands-kendall` — `au-fhir-test-data-set/au-erequesting/Patient-sandilands-kendall.json` — **Patient (age 45)**

**Practitioner** (10)

- `lapthorn-leisa` — `au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json` — **Inpatient Psychologist** — *declared specialty is only "Clinical Psychologist"* — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `levings-richard` — `au-fhir-test-data-set/au-core/Practitioner-levings-richard.json` — **Outpatient Dietitian** — *declared specialty is only "Dietitian"* — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-abe` — `au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json` — **General Practitioner (GP)** — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `mcnab-angelina` — `au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json` — **Inpatient Dietitian** — *declared specialty is only "Dietitian"* — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `milgate-leisa` — `au-fhir-test-data-set/au-core/Practitioner-milgate-leisa.json` — **Day Therapy Unit Nurse** — *declared specialty is only "Registered Nurses nec"*
- `mills-hope` — `au-fhir-test-data-set/au-core/Practitioner-mills-hope.json` — **Occupational Therapist (OT)** — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parker-elijah` — `au-fhir-test-data-set/au-core/Practitioner-parker-elijah.json` — **Physiotherapist**
- `roberts-benjamin` — `au-fhir-test-data-set/au-core/Practitioner-roberts-benjamin.json` — **Specialist Cancer Nurse** — *declared specialty is only "Registered Nurses nec"*
- `sheppard-mathew` — `au-fhir-test-data-set/au-core/Practitioner-sheppard-mathew.json` — **Medical Oncologist**
- `vaughan-blaine` — `au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json` — **Private Psychologist** — *declared specialty is only "Clinical Psychologist"* — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Unresolved** (2)

- `hith-team` — _(no resource)_ — **Hospital-In-The-Home (HITH) team** — *no matching resource in the data set*
- `medical-oncology-team` — _(no resource)_ — **Medical Oncology Team** — *no matching resource in the data set*

</details>

<details><summary><strong>emergency-hospital-attendance</strong> (1 entity)</summary>

**Patient** (1)

- `morris-charlotte` — `au-fhir-test-data-set/au-core/Patient-morris-charlotte.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

</details>

<details><summary><strong>hospital-to-aged-care-interstate-transfer</strong> (1 entity)</summary>

**Patient** (1)

- `nielsen-eleanore` — `au-fhir-test-data-set/au-core/Patient-nielsen-eleanore.json`

</details>

<details><summary><strong>interstate-gp-visit</strong> (1 entity)</summary>

**Patient** (1)

- `banks-jeramy-ezra` — `au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

</details>

<details><summary><strong>pre-operative-surgical</strong> (1 entity)</summary>

**Patient** (1)

- `simpson-tristan` — `au-fhir-test-data-set/au-core/Patient-simpson-tristan.json`

</details>

<details><summary><strong>referral-to-specialist-and-allied-health</strong> (2 entities)</summary>

**Patient** (1)

- `johnson-joyce` — `au-fhir-test-data-set/au-core/Patient-johnson-joyce.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

**Practitioner** (1)

- `burrows-ginger` — `au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

</details>


## Connected Care consumer journeys <a id="connected-care-journeys"></a>

### Purpose

Identifies the entities belonging to the Connected Care consumer journeys — Alex's Story and Yuri's Story.

### Ownership & governance

**Owner:** DoHAC  
Each journey tells one patient's story end-to-end. Adding to or modifying a member entity or its linked resources risks conflicting with that story's clinical timeline, so coordination with DoHAC is required.

### Provenance & use

Alex's Story membership is declared by a data set document held alongside the instances. Yuri's Story has no source document yet, so its membership is the provisional remainder of the directory not claimed by Alex's Story.

### Relationships

Members are geographically clustered — Kalgoorlie WA and Bathurst NSW — but do not appear in [Geographic groupings](#geography-groups), which currently indexes only the default branch.

### How is this subset identified?

Declared, and read from a branch. These entities are not on the default branch, so the derivation reads the connected-care branch directly and partitions it using the Alex's Story document.


**Source:** Alex's Story — au-fhir-test-data-set/connected-care/Alex Story Data Set.md, on the connected-care branch (not on master). Yuri's Story — no source document yet; membership is the provisional remainder of the connected-care directory not claimed by Alex's Story.

**Read at:** [`ddb96e935ee7`](https://github.com/hl7au/au-fhir-test-data/commit/ddb96e935ee71866b48d3b49291609868a414baa) — the Connected Care branch revision this page was last generated from.

_Classification: Declared._
> Alex's Story: 38 entities claimed by 'Alex Story Data Set.md', all resolved on upstream/connected-care.
> Yuri's Story: 57 entities attributed by REMAINDER only — no source document exists for Yuri's Story yet. This attribution is provisional, not confirmed.
> 56 of the 57 remainder entities are infrastructure types (Organization, Location, Practitioner, PractitionerRole, HealthcareService) that may plausibly serve both stories — see design.md Open Questions 'Connected Care shared infrastructure'. Tagged likely_shared rather than resolved here.
> 1 narrative element(s) in Alex's Story have no resource mapped (marked *Unresolved* in the document).
> 55 non-administrative entities excluded: Observation x8, ServiceRequest x7, Encounter x6, MedicationStatement x5, Appointment x4, MedicationRequest x5, Composition x3, MedicationDispense x4, Bundle x2, DiagnosticReport x2, Procedure x2, AllergyIntolerance x1, Condition x1, DocumentReference x1, Task x2, Binary x2. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.

### Members (95)

<details><summary><strong>Alex's Story</strong> (38 entities)</summary>

**Patient** (1)

- `thompson-alex` — `au-fhir-test-data-set/connected-care/Patient-thompson-alex.json`

**PractitionerRole** (8)

- `counsellorsnec-patel-rachel` — `au-fhir-test-data-set/connected-care/PractitionerRole-counsellorsnec-patel-rachel.json`
- `generalpractitioner-lee-chris` — `au-fhir-test-data-set/connected-care/PractitionerRole-generalpractitioner-lee-chris.json`
- `generalpractitioner-smith-jane` — `au-fhir-test-data-set/connected-care/PractitionerRole-generalpractitioner-smith-jane.json`
- `medicaltechnician-johnson-sally` — `au-fhir-test-data-set/connected-care/PractitionerRole-medicaltechnician-johnson-sally.json`
- `obstetrician-chen-emily` — `au-fhir-test-data-set/connected-care/PractitionerRole-obstetrician-chen-emily.json`
- `obstetrician-wilson-mark` — `au-fhir-test-data-set/connected-care/PractitionerRole-obstetrician-wilson-mark.json`
- `physiotherapist-evans-sarah` — `au-fhir-test-data-set/connected-care/PractitionerRole-physiotherapist-evans-sarah.json`
- `retailpharmacist-lee-sarah` — `au-fhir-test-data-set/connected-care/PractitionerRole-retailpharmacist-lee-sarah.json`

**Practitioner** (8)

- `chen-emily` — `au-fhir-test-data-set/connected-care/Practitioner-chen-emily.json`
- `evans-sarah` — `au-fhir-test-data-set/connected-care/Practitioner-evans-sarah.json`
- `johnson-sally` — `au-fhir-test-data-set/connected-care/Practitioner-johnson-sally.json`
- `lee-chris` — `au-fhir-test-data-set/connected-care/Practitioner-lee-chris.json`
- `lee-sarah` — `au-fhir-test-data-set/connected-care/Practitioner-lee-sarah.json`
- `patel-rachel` — `au-fhir-test-data-set/connected-care/Practitioner-patel-rachel.json`
- `smith-jane` — `au-fhir-test-data-set/connected-care/Practitioner-smith-jane.json`
- `wilson-mark` — `au-fhir-test-data-set/connected-care/Practitioner-wilson-mark.json`

**HealthcareService** (7)

- `clinicalpsychology-bathurst-psychology` — `au-fhir-test-data-set/connected-care/HealthcareService-clinicalpsychology-bathurst-psychology.json`
- `communitypharmacy-bathurst-community-pharmacy` — `au-fhir-test-data-set/connected-care/HealthcareService-communitypharmacy-bathurst-community-pharmacy.json`
- `generalmedical-bathurst-medical-centre` — `au-fhir-test-data-set/connected-care/HealthcareService-generalmedical-bathurst-medical-centre.json`
- `pathologylaboratory-bathurst-pathology` — `au-fhir-test-data-set/connected-care/HealthcareService-pathologylaboratory-bathurst-pathology.json`
- `physiotherapyservices-bathurst-physio-centre` — `au-fhir-test-data-set/connected-care/HealthcareService-physiotherapyservices-bathurst-physio-centre.json`
- `privateacute-ashfield-private-hospital` — `au-fhir-test-data-set/connected-care/HealthcareService-privateacute-ashfield-private-hospital.json`
- `specialistmedical-ashfield-private-clinic` — `au-fhir-test-data-set/connected-care/HealthcareService-specialistmedical-ashfield-private-clinic.json`

**Organization** (7)

- `ashfield-private-clinic` — `au-fhir-test-data-set/connected-care/Organization-ashfield-private-clinic.json`
- `ashfield-private-hospital` — `au-fhir-test-data-set/connected-care/Organization-ashfield-private-hospital.json`
- `bathurst-community-pharmacy` — `au-fhir-test-data-set/connected-care/Organization-bathurst-community-pharmacy.json`
- `bathurst-medical-centre` — `au-fhir-test-data-set/connected-care/Organization-bathurst-medical-centre.json`
- `bathurst-pathology` — `au-fhir-test-data-set/connected-care/Organization-bathurst-pathology.json`
- `bathurst-physio-centre` — `au-fhir-test-data-set/connected-care/Organization-bathurst-physio-centre.json`
- `bathurst-psychology` — `au-fhir-test-data-set/connected-care/Organization-bathurst-psychology.json`

**Location** (7)

- `ashfield-private-clinic` — `au-fhir-test-data-set/connected-care/Location-ashfield-private-clinic.json`
- `ashfield-private-hospital` — `au-fhir-test-data-set/connected-care/Location-ashfield-private-hospital.json`
- `bathurst-community-pharmacy` — `au-fhir-test-data-set/connected-care/Location-bathurst-community-pharmacy.json`
- `bathurst-medical-centre` — `au-fhir-test-data-set/connected-care/Location-bathurst-medical-centre.json`
- `bathurst-pathology` — `au-fhir-test-data-set/connected-care/Location-bathurst-pathology.json`
- `bathurst-physio-centre` — `au-fhir-test-data-set/connected-care/Location-bathurst-physio-centre.json`
- `bathurst-psychology` — `au-fhir-test-data-set/connected-care/Location-bathurst-psychology.json`

</details>

<details><summary><strong>Yuri's Story (provisional)</strong> (57 entities)</summary>

**Patient** (1)

- `petrov-yuri` — `au-fhir-test-data-set/connected-care/Patient-petrov-yuri.json`

**PractitionerRole** (12)

- `aboriginal-king-narelle` — `au-fhir-test-data-set/connected-care/PractitionerRole-aboriginal-king-narelle.json`
- `ambulanceofficer-bradley-tom` — `au-fhir-test-data-set/connected-care/PractitionerRole-ambulanceofficer-bradley-tom.json`
- `emergencymedicinespecialist-green-susan-garran-hospital` — `au-fhir-test-data-set/connected-care/PractitionerRole-emergencymedicinespecialist-green-susan-garran-hospital.json`
- `emergencymedicinespecialist-green-susan-garran-hospital-ed` — `au-fhir-test-data-set/connected-care/PractitionerRole-emergencymedicinespecialist-green-susan-garran-hospital-ed.json`
- `endocrinologist-tench-natalie` — `au-fhir-test-data-set/connected-care/PractitionerRole-endocrinologist-tench-natalie.json`
- `generalpractitioner-kumar-ravi` — `au-fhir-test-data-set/connected-care/PractitionerRole-generalpractitioner-kumar-ravi.json`
- `nursepractitioner-brown-sarah` — `au-fhir-test-data-set/connected-care/PractitionerRole-nursepractitioner-brown-sarah.json`
- `nursepractitioner-hayes-linda` — `au-fhir-test-data-set/connected-care/PractitionerRole-nursepractitioner-hayes-linda.json`
- `occupationaltherapist-wong-lisa` — `au-fhir-test-data-set/connected-care/PractitionerRole-occupationaltherapist-wong-lisa.json`
- `physiotherapist-smith-john` — `au-fhir-test-data-set/connected-care/PractitionerRole-physiotherapist-smith-john.json`
- `retailpharmacist-sullivan-joy` — `au-fhir-test-data-set/connected-care/PractitionerRole-retailpharmacist-sullivan-joy.json`
- `socialworker-mitchell-karen` — `au-fhir-test-data-set/connected-care/PractitionerRole-socialworker-mitchell-karen.json`

**Practitioner** (11)

- `bradley-tom` — `au-fhir-test-data-set/connected-care/Practitioner-bradley-tom.json`
- `brown-sarah` — `au-fhir-test-data-set/connected-care/Practitioner-brown-sarah.json`
- `green-susan` — `au-fhir-test-data-set/connected-care/Practitioner-green-susan.json`
- `hayes-linda` — `au-fhir-test-data-set/connected-care/Practitioner-hayes-linda.json`
- `king-narelle` — `au-fhir-test-data-set/connected-care/Practitioner-king-narelle.json`
- `kumar-ravi` — `au-fhir-test-data-set/connected-care/Practitioner-kumar-ravi.json`
- `mitchell-karen` — `au-fhir-test-data-set/connected-care/Practitioner-mitchell-karen.json`
- `smith-john` — `au-fhir-test-data-set/connected-care/Practitioner-smith-john.json`
- `sullivan-joy` — `au-fhir-test-data-set/connected-care/Practitioner-sullivan-joy.json`
- `tench-natalie` — `au-fhir-test-data-set/connected-care/Practitioner-tench-natalie.json`
- `wong-lisa` — `au-fhir-test-data-set/connected-care/Practitioner-wong-lisa.json`

**HealthcareService** (11)

- `agedcare-aged-care-home-help` — `au-fhir-test-data-set/connected-care/HealthcareService-agedcare-aged-care-home-help.json`
- `ambulanceservice-garran-ambulance-service` — `au-fhir-test-data-set/connected-care/HealthcareService-ambulanceservice-garran-ambulance-service.json`
- `communitypharmacy-kalgoorlie-pharmacy` — `au-fhir-test-data-set/connected-care/HealthcareService-communitypharmacy-kalgoorlie-pharmacy.json`
- `generalhospital-garran-hospital-ed` — `au-fhir-test-data-set/connected-care/HealthcareService-generalhospital-garran-hospital-ed.json`
- `generalmedical-kalgoorlie-medical-centre` — `au-fhir-test-data-set/connected-care/HealthcareService-generalmedical-kalgoorlie-medical-centre.json`
- `healthcareservice-kalgoorlie-aged-care-service` — `au-fhir-test-data-set/connected-care/HealthcareService-healthcareservice-kalgoorlie-aged-care-service.json`
- `occupationaltherapy-kalgoorlie-ot-services` — `au-fhir-test-data-set/connected-care/HealthcareService-occupationaltherapy-kalgoorlie-ot-services.json`
- `physiotherapyservices-kalgoorlie-physiotherapy` — `au-fhir-test-data-set/connected-care/HealthcareService-physiotherapyservices-kalgoorlie-physiotherapy.json`
- `publicacute-garran-hospital` — `au-fhir-test-data-set/connected-care/HealthcareService-publicacute-garran-hospital.json`
- `publiccommunity-kalgoorlie-community-health-service` — `au-fhir-test-data-set/connected-care/HealthcareService-publiccommunity-kalgoorlie-community-health-service.json`
- `specialistmedical-kalgoorlie-specialist-clinic` — `au-fhir-test-data-set/connected-care/HealthcareService-specialistmedical-kalgoorlie-specialist-clinic.json`

**Organization** (11)

- `aged-care-home-help` — `au-fhir-test-data-set/connected-care/Organization-aged-care-home-help.json`
- `garran-ambulance-service` — `au-fhir-test-data-set/connected-care/Organization-garran-ambulance-service.json`
- `garran-hospital` — `au-fhir-test-data-set/connected-care/Organization-garran-hospital.json`
- `garran-hospital-ed` — `au-fhir-test-data-set/connected-care/Organization-garran-hospital-ed.json`
- `kalgoorlie-aged-care-service` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-aged-care-service.json`
- `kalgoorlie-community-health-service` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-community-health-service.json`
- `kalgoorlie-medical-centre` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-medical-centre.json`
- `kalgoorlie-ot-services` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-ot-services.json`
- `kalgoorlie-pharmacy` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-pharmacy.json`
- `kalgoorlie-physiotherapy` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-physiotherapy.json`
- `kalgoorlie-specialist-clinic` — `au-fhir-test-data-set/connected-care/Organization-kalgoorlie-specialist-clinic.json`

**Location** (11)

- `aged-care-home-help` — `au-fhir-test-data-set/connected-care/Location-aged-care-home-help.json`
- `garran-ambulance-service` — `au-fhir-test-data-set/connected-care/Location-garran-ambulance-service.json`
- `garran-hospital` — `au-fhir-test-data-set/connected-care/Location-garran-hospital.json`
- `garran-hospital-ed` — `au-fhir-test-data-set/connected-care/Location-garran-hospital-ed.json`
- `kalgoorlie-aged-care-service` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-aged-care-service.json`
- `kalgoorlie-community-health-service` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-community-health-service.json`
- `kalgoorlie-medical-centre` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-medical-centre.json`
- `kalgoorlie-ot-services` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-ot-services.json`
- `kalgoorlie-pharmacy` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-pharmacy.json`
- `kalgoorlie-physiotherapy` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-physiotherapy.json`
- `kalgoorlie-specialist-clinic` — `au-fhir-test-data-set/connected-care/Location-kalgoorlie-specialist-clinic.json`

</details>


## Community contributions <a id="community-contributions"></a>

### Purpose

Identifies which community organisation contributed which entities.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Attribution records origin only. It places no constraint on adding to or modifying the contributed entities or their linked resources.

### Provenance & use

Attributed from the commit that introduced each file, cross-checked against a human-attested list. Attribution is best-effort: a contributor using a personal email address, or a merge that did not preserve original authorship, is not detected, so the list is not exhaustive.

### Relationships

No notable relationships to other subsets.

### How is this subset identified?

Derived from commit authorship, then cross-checked. The commit that introduced each file is matched against recognised organisation email domains, and the result is compared with an independently human-attested list so that a disagreement is reported rather than an entity silently dropping out. (see spec scenario "The limits of git-based attribution are stated").


_Classification: Derived + Curated._
> 12 entities attributed across 1 organisation(s).
> Attribution derives from the commit that introduced each file and may under-report: a contributor using a personal email address, or a merge that did not preserve original authorship, is not detected. The list is not exhaustive.
> 1525 files in the data set carry no recognised-domain attribution; most are project-internal contributions.
> Cross-check passed: all 12 human-attested entities were also found independently by the authorship scan.

### Members (12)

<details><summary><strong>ADHA (Australian Digital Health Agency)</strong> (12 entities)</summary>

**Organization** (12)

- `benalla-care-and-support` — `au-fhir-test-data-set/au-core/Organization-benalla-health-network.json`
- `cremorne-care-and-support` — `au-fhir-test-data-set/au-core/Organization-cremorne-care-and-support.json`
- `curtin-care-and-support` — `au-fhir-test-data-set/au-core/Organization-curtain-care-and-support.json`
- `goondiwindi-health-network` — `au-fhir-test-data-set/au-core/Organization-goondiwindi-health-network.json`
- `hayborough-care-and-support` — `au-fhir-test-data-set/au-core/Organization-hayborough-care-and-support.json`
- `leeton-health-network` — `au-fhir-test-data-set/au-core/Organization-leeton-health-network.json`
- `menzies-health-network` — `au-fhir-test-data-set/au-core/Organization-menzies-health-network.json`
- `oxenford-care-and-support` — `au-fhir-test-data-set/au-core/Organization-oxenford-care-and-support.json`
- `reid-health-network` — `au-fhir-test-data-set/au-core/Organization-reid-health-network.json`
- `sorell-health-network` — `au-fhir-test-data-set/au-core/Organization-sorell-health-network.json`
- `south-lake-care-and-support` — `au-fhir-test-data-set/au-core/Organization-south-lake-care-and-support.json`
- `tarneit-health-network` — `au-fhir-test-data-set/au-core/Organization-tarneit-health-network.json`

</details>


## Missing and suppressed data examples <a id="missing-suppressed-data"></a>

### Purpose

Identifies the instances demonstrating the correct representation of missing or suppressed data.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Instances are deliberately shaped to demonstrate a specific representation of absent data. Adding to or modifying their linked resources risks misrepresenting what they demonstrate.

### Provenance & use

Drawn from the repository's own missing and suppressed data documentation, extended by a keyword scan whose hits are individually confirmed against the resource's actual content. This is the one subset not restricted to administrative entities, because the property it demonstrates attaches to an Observation exactly as it does to a Patient.

### Relationships

Some members are also [Blank-slate patients](#blank-slate-patients).

### How is this subset identified?

Derived from the documented cases, then extended by curation. Resource ids are scanned for keywords such as missing, suppressed and masked, and each hit is put to a human, who checks the resource actually carries a data-absent-reason mechanism rather than matching the keyword by coincidence.


_Classification: Derived + Curated._
> 11 documented cases from docs/MissingAndSuppressedData_TestData.md.
> 56 additional instances confirmed from keyword hits; 1 rejected.

### Members (67)

<details><summary>67 entities — click to expand</summary>

**Patient** (8)

- `italia-sofia-missing-birthDate` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-birthDate.json`
- `italia-sofia-missing-gender` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-gender.json`
- `italia-sofia-missing-identifier` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-identifier.json`
- `italia-sofia-missing-name` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-name.json`
- `italia-sofia-suppressed-birthDate` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-birthDate.json`
- `italia-sofia-suppressed-gender` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-gender.json`
- `italia-sofia-suppressed-identifier` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-identifier.json`
- `italia-sofia-suppressed-name` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-name.json`

**PractitionerRole** (1)

- `missing-practitioner` — `au-fhir-test-data-set/au-core/PractitionerRole-missing-practitioner.json`

**Practitioner** (1)

- `missing-name` — `au-fhir-test-data-set/au-core/Practitioner-missing-name.json`

**Organization** (1)

- `missing-name` — `au-fhir-test-data-set/au-core/Organization-missing-name.json`

**AllergyIntolerance** (2)

- `egg-missing-code` — `au-fhir-test-data-set/au-core/AllergyIntolerance-egg-missing-code.json`
- `egg-suppressed-subject` — `au-fhir-test-data-set/au-core/AllergyIntolerance-egg-suppressed-subject.json`

**Bundle** (2)

- `aups-basicsummary-missing-comp-elements` — `au-fhir-test-data-set/au-patient-summary/Bundle-aups-basicsummary-missing-comp-elements.json`
- `aups-section-emptyreason` — `au-fhir-test-data-set/au-patient-summary/Bundle-aups-section-emptyreason.json`

**Condition** (4)

- `condition-masked` — `au-fhir-test-data-set/au-core/Condition-condition-masked.json`
- `nailwound-missing-category` — `au-fhir-test-data-set/au-core/Condition-nailwound-missing-category.json`
- `nailwound-missing-code` — `au-fhir-test-data-set/au-core/Condition-nailwound-missing-code.json`
- `nailwound-suppressed-subject` — `au-fhir-test-data-set/au-core/Condition-nailwound-suppressed-subject.json`

**DocumentReference** (1)

- `aups-section-emptyreason` — `au-fhir-test-data-set/au-core/DocumentReference-aups-section-emptyreason.json`

**Encounter** (3)

- `annualvisit-missing-class` — `au-fhir-test-data-set/au-core/Encounter-annualvisit-missing-class.json`
- `annualvisit-missing-status` — `au-fhir-test-data-set/au-core/Encounter-annualvisit-missing-status.json`
- `annualvisit-suppressed-subject` — `au-fhir-test-data-set/au-core/Encounter-annualvisit-suppressed-subject.json`

**Immunization** (3)

- `zoster-missing-code` — `au-fhir-test-data-set/au-core/Immunization-zoster-missing-code.json`
- `zoster-missing-occurrence` — `au-fhir-test-data-set/au-core/Immunization-zoster-missing-occurrence.json`
- `zoster-suppressed-subject` — `au-fhir-test-data-set/au-core/Immunization-zoster-suppressed-subject.json`

**Medication** (1)

- `reaptan-missing-code` — `au-fhir-test-data-set/au-core/Medication-reaptan-missing-code.json`

**MedicationRequest** (5)

- `reaptan-missing-authoredOn` — `au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-authoredOn.json`
- `reaptan-missing-medication` — `au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-medication.json`
- `reaptan-missing-requester` — `au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-requester.json`
- `reaptan-missing-status` — `au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-status.json`
- `reaptan-suppressed-subject` — `au-fhir-test-data-set/au-core/MedicationRequest-reaptan-suppressed-subject.json`

**MedicationStatement** (3)

- `missing-medication` — `au-fhir-test-data-set/au-core/MedicationStatement-missing-medication.json`
- `missing-status` — `au-fhir-test-data-set/au-core/MedicationStatement-missing-status.json`
- `suppressed-subject` — `au-fhir-test-data-set/au-core/MedicationStatement-suppressed-subject.json`

**Observation** (29)

- `blood-group-panel-cancelled` — `au-fhir-test-data-set/au-core/Observation-blood-group-panel-cancelled.json`
- `bloodpressure-diastolic-missing` — `au-fhir-test-data-set/au-core/Observation-bloodpressure-diastolic-missing.json`
- `bloodpressure-missing` — `au-fhir-test-data-set/au-core/Observation-bloodpressure-missing.json`
- `bloodpressure-systolic-missing` — `au-fhir-test-data-set/au-core/Observation-bloodpressure-systolic-missing.json`
- `bodyheight-1-device-missing` — `au-fhir-test-data-set/au-core/Observation-bodyheight-1-device-missing.json`
- `bodyheight-cancelled` — `au-fhir-test-data-set/au-core/Observation-bodyheight-cancelled.json`
- `bodytemp-1-device-missing` — `au-fhir-test-data-set/au-core/Observation-bodytemp-1-device-missing.json`
- `bodytemp-cancelled` — `au-fhir-test-data-set/au-core/Observation-bodytemp-cancelled.json`
- `bodyweight-3-clothing-missing` — `au-fhir-test-data-set/au-core/Observation-bodyweight-3-clothing-missing.json`
- `bodyweight-cancelled` — `au-fhir-test-data-set/au-core/Observation-bodyweight-cancelled.json`
- `glasgow-coma-scale-motor-not-performed` — `au-fhir-test-data-set/au-core/Observation-glasgow-coma-scale-motor-not-performed.json`
- `hearing-threshold-cancelled` — `au-fhir-test-data-set/au-core/Observation-hearing-threshold-cancelled.json`
- `heartrate-1-exercise-missing` — `au-fhir-test-data-set/au-core/Observation-heartrate-1-exercise-missing.json`
- `heartrate-cancelled` — `au-fhir-test-data-set/au-core/Observation-heartrate-cancelled.json`
- `observation-masked` — `au-fhir-test-data-set/au-core/Observation-observation-masked.json`
- `pathresult-missing-code` — `au-fhir-test-data-set/au-core/Observation-pathresult-missing-code.json`
- `pathresult-missing-effective` — `au-fhir-test-data-set/au-core/Observation-pathresult-missing-effective.json`
- `pathresult-missing-status` — `au-fhir-test-data-set/au-core/Observation-pathresult-missing-status.json`
- `pathresult-missing-value` — `au-fhir-test-data-set/au-core/Observation-pathresult-missing-value.json`
- `pathresult-suppressed-code` — `au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-code.json`
- `pathresult-suppressed-dataAbsentReason` — `au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-dataAbsentReason.json`
- `pathresult-suppressed-subject` — `au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-subject.json`
- `pathresult-suppressed-valueCodeableConcept` — `au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-valueCodeableConcept.json`
- `pathresult-suppressed-valueQuantity` — `au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-valueQuantity.json`
- `resprate-1-exercise-missing` — `au-fhir-test-data-set/au-core/Observation-resprate-1-exercise-missing.json`
- `resprate-cancelled` — `au-fhir-test-data-set/au-core/Observation-resprate-cancelled.json`
- `smokingstatus-notasked` — `au-fhir-test-data-set/au-core/Observation-smokingstatus-notasked.json`
- `waistcircum-1-position-missing` — `au-fhir-test-data-set/au-core/Observation-waistcircum-1-position-missing.json`
- `waistcircum-cancelled` — `au-fhir-test-data-set/au-core/Observation-waistcircum-cancelled.json`

**Procedure** (3)

- `obstetric-missing-code` — `au-fhir-test-data-set/au-core/Procedure-obstetric-missing-code.json`
- `obstetric-missing-status` — `au-fhir-test-data-set/au-core/Procedure-obstetric-missing-status.json`
- `obstetric-missing-subject` — `au-fhir-test-data-set/au-core/Procedure-obstetric-missing-subject.json`

</details>


## Scenario groupings <a id="scenario-groups"></a>

### Purpose

Groups entities by the consumer-journey scenario they were originally built for.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Grouping identifies plausible co-location as a starting point for new consumer journeys or test scenarios. Members are free to build on and are not reserved to their originating scenario.

### Provenance & use

Seeded once from a historical directory structure that no longer exists on the default branch, then maintained by curation. The originating git ref is recorded for traceability but is no longer consulted.

### Relationships

Members are extensively represented in [Geographic groupings](#geography-groups), reflecting that each scenario was built around a specific locality. Several members also appear in [Sparked Clinical Design Group consumer journeys](#sparked-cdg-journeys).

### How is this subset identified?

Curated, seeded once. The groupings were extracted a single time from the au-core/consumer-journey directory structure at a pinned git ref; from that point the facts file is authoritative and the seed is not re- run.


_Classification: Curated._
### Members (418)

<details><summary><strong>CCM_Aged care scenario - Future</strong> (49 entities)</summary>

**Patient** (1)

- `reece-karen` — `au-fhir-test-data-set/au-core/Patient-reece-karen.json`

**PractitionerRole** (18)

- `baker-troy` — `au-fhir-test-data-set/au-core/PractitionerRole-baker-troy.json`
- `baynton-lolita` — `au-fhir-test-data-set/au-core/PractitionerRole-baynton-lolita.json`
- `bell-rudolf` — `au-fhir-test-data-set/au-core/PractitionerRole-bell-rudolf.json`
- `berry-lisa` — `au-fhir-test-data-set/au-core/PractitionerRole-berry-lisa.json`
- `carey-joyce` — `au-fhir-test-data-set/au-core/PractitionerRole-carey-joyce.json`
- `couch-joel` — `au-fhir-test-data-set/au-core/PractitionerRole-couch-joel.json`
- `cruickshank-marlyn` — `au-fhir-test-data-set/au-core/PractitionerRole-cruickshank-marlyn.json`
- `fleming-skye` — `au-fhir-test-data-set/au-core/PractitionerRole-fleming-skye.json`
- `freeman-anya` — `au-fhir-test-data-set/au-core/PractitionerRole-freeman-anya.json`
- `harley-reynalda` — `au-fhir-test-data-set/au-core/PractitionerRole-harley-reynalda.json`
- `hoskins-earl` — `au-fhir-test-data-set/au-core/PractitionerRole-hoskins-earl.json`
- `huddlestone-velda` — `au-fhir-test-data-set/au-core/PractitionerRole-huddlestone-velda.json`
- `hutton-cortez` — `au-fhir-test-data-set/au-core/PractitionerRole-hutton-cortez.json`
- `lawrence-drew` — `au-fhir-test-data-set/au-core/PractitionerRole-lawrence-drew.json`
- `manning-opal` — `au-fhir-test-data-set/au-core/PractitionerRole-manning-opal.json`
- `rowlands-donya` — `au-fhir-test-data-set/au-core/PractitionerRole-rowlands-donya.json`
- `tierney-gisela` — `au-fhir-test-data-set/au-core/PractitionerRole-tierney-gisela.json`
- `vaughan-sol` — `au-fhir-test-data-set/au-core/PractitionerRole-vaughan-sol.json`

**Practitioner** (18)

- `baker-troy` — `au-fhir-test-data-set/au-core/Practitioner-baker-troy.json`
- `baynton-lolita` — `au-fhir-test-data-set/au-core/Practitioner-baynton-lolita.json`
- `bell-rudolf` — `au-fhir-test-data-set/au-core/Practitioner-bell-rudolf.json`
- `berry-lisa` — `au-fhir-test-data-set/au-core/Practitioner-berry-lisa.json`
- `carey-joyce` — `au-fhir-test-data-set/au-core/Practitioner-carey-joyce.json`
- `couch-joel` — `au-fhir-test-data-set/au-core/Practitioner-couch-joel.json`
- `cruickshank-marlyn` — `au-fhir-test-data-set/au-core/Practitioner-cruickshank-marlyn.json`
- `fleming-skye` — `au-fhir-test-data-set/au-core/Practitioner-fleming-skye.json`
- `freeman-anya` — `au-fhir-test-data-set/au-core/Practitioner-freeman-anya.json`
- `harley-reynalda` — `au-fhir-test-data-set/au-core/Practitioner-harley-reynalda.json`
- `hoskins-earl` — `au-fhir-test-data-set/au-core/Practitioner-hoskins-earl.json`
- `huddlestone-velda` — `au-fhir-test-data-set/au-core/Practitioner-huddlestone-velda.json`
- `hutton-cortez` — `au-fhir-test-data-set/au-core/Practitioner-hutton-cortez.json`
- `lawrence-drew` — `au-fhir-test-data-set/au-core/Practitioner-lawrence-drew.json`
- `manning-opal` — `au-fhir-test-data-set/au-core/Practitioner-manning-opal.json`
- `rowlands-donya` — `au-fhir-test-data-set/au-core/Practitioner-rowlands-donya.json`
- `tierney-gisela` — `au-fhir-test-data-set/au-core/Practitioner-tierney-gisela.json`
- `vaughan-sol` — `au-fhir-test-data-set/au-core/Practitioner-vaughan-sol.json`

**Organization** (12)

- `adelaide-public-hospital` — `au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json`
- `royal-park-medical-centre` — `au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json`
- `semaphore-aged-care` — `au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json`
- `woodville-cardiology` — `au-fhir-test-data-set/au-core/Organization-woodville-cardiology.json`
- `woodville-dental` — `au-fhir-test-data-set/au-core/Organization-woodville-dental.json`
- `woodville-dietitian-service` — `au-fhir-test-data-set/au-core/Organization-woodville-dietitian-service.json`
- `woodville-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-woodville-medical-clinic.json`
- `woodville-ot-services` — `au-fhir-test-data-set/au-core/Organization-woodville-ot-services.json`
- `woodville-pathology` — `au-fhir-test-data-set/au-core/Organization-woodville-pathology.json`
- `woodville-pharmacy` — `au-fhir-test-data-set/au-core/Organization-woodville-pharmacy.json`
- `woodville-podiatry` — `au-fhir-test-data-set/au-core/Organization-woodville-podiatry.json`
- `woodville-radiology` — `au-fhir-test-data-set/au-core/Organization-woodville-radiology.json`

</details>

<details><summary><strong>CCM scenario - Drafted</strong> (44 entities)</summary>

**Patient** (1)

- `foreman-caterina` — `au-fhir-test-data-set/au-core/Patient-foreman-caterina.json`

**PractitionerRole** (16)

- `bond-edmundo` — `au-fhir-test-data-set/au-core/PractitionerRole-bond-edmundo.json`
- `bowyer-norbert` — `au-fhir-test-data-set/au-core/PractitionerRole-bowyer-norbert.json`
- `fuller-kendrick` — `au-fhir-test-data-set/au-core/PractitionerRole-fuller-kendrick.json`
- `hallan-maggie` — `au-fhir-test-data-set/au-core/PractitionerRole-hallan-maggie.json`
- `hamel-opal` — `au-fhir-test-data-set/au-core/PractitionerRole-hamel-opal.json`
- `kelly-arlene` — `au-fhir-test-data-set/au-core/PractitionerRole-kelly-arlene.json`
- `keyes-chau` — `au-fhir-test-data-set/au-core/PractitionerRole-keyes-chau.json`
- `mcnaughton-opal` — `au-fhir-test-data-set/au-core/PractitionerRole-mcnaughton-opal.json`
- `mullins-bonita` — `au-fhir-test-data-set/au-core/PractitionerRole-mullins-bonita.json`
- `osland-deanne` — `au-fhir-test-data-set/au-core/PractitionerRole-osland-deanne.json`
- `patterson-teri` — `au-fhir-test-data-set/au-core/PractitionerRole-patterson-teri.json`
- `phillips-gerard` — `au-fhir-test-data-set/au-core/PractitionerRole-phillips-gerard.json`
- `quinn-jeramy` — `au-fhir-test-data-set/au-core/PractitionerRole-quinn-jeramy.json`
- `schaefer-elden` — `au-fhir-test-data-set/au-core/PractitionerRole-schaefer-elden.json`
- `sharp-cherish` — `au-fhir-test-data-set/au-core/PractitionerRole-sharp-cherish.json`
- `vaughan-blaine` — `au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json`

**Practitioner** (16)

- `bond-edmundo` — `au-fhir-test-data-set/au-core/Practitioner-bond-edmundo.json`
- `bowyer-norbert` — `au-fhir-test-data-set/au-core/Practitioner-bowyer-norbert.json`
- `fuller-kendrick` — `au-fhir-test-data-set/au-core/Practitioner-fuller-kendrick.json`
- `hallan-maggie` — `au-fhir-test-data-set/au-core/Practitioner-hallan-maggie.json`
- `hamel-opal` — `au-fhir-test-data-set/au-core/Practitioner-hamel-opal.json`
- `kelly-arlene` — `au-fhir-test-data-set/au-core/Practitioner-kelly-arlene.json`
- `keyes-chau` — `au-fhir-test-data-set/au-core/Practitioner-keyes-chau.json`
- `mcnaughton-opal` — `au-fhir-test-data-set/au-core/Practitioner-mcnaughton-opal.json`
- `mullins-bonita` — `au-fhir-test-data-set/au-core/Practitioner-mullins-bonita.json`
- `osland-deanne` — `au-fhir-test-data-set/au-core/Practitioner-osland-deanne.json`
- `patterson-teri` — `au-fhir-test-data-set/au-core/Practitioner-patterson-teri.json`
- `phillips-gerard` — `au-fhir-test-data-set/au-core/Practitioner-phillips-gerard.json`
- `quinn-jeramy` — `au-fhir-test-data-set/au-core/Practitioner-quinn-jeramy.json`
- `schaefer-elden` — `au-fhir-test-data-set/au-core/Practitioner-schaefer-elden.json`
- `sharp-cherish` — `au-fhir-test-data-set/au-core/Practitioner-sharp-cherish.json`
- `vaughan-blaine` — `au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**Organization** (11)

- `sunshine-cardiology` — `au-fhir-test-data-set/au-core/Organization-sunshine-cardiology.json`
- `sunshine-endocrinology` — `au-fhir-test-data-set/au-core/Organization-sunshine-endocrinology.json`
- `sunshine-medical-centre` — `au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json`
- `sunshine-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json`
- `sunshine-nephrology` — `au-fhir-test-data-set/au-core/Organization-sunshine-nephrology.json`
- `sunshine-ophthalmology` — `au-fhir-test-data-set/au-core/Organization-sunshine-ophthalmology.json`
- `sunshine-optical` — `au-fhir-test-data-set/au-core/Organization-sunshine-optical.json`
- `sunshine-pathology` — `au-fhir-test-data-set/au-core/Organization-sunshine-pathology.json`
- `sunshine-pharmacy` — `au-fhir-test-data-set/au-core/Organization-sunshine-pharmacy.json`
- `sunshine-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-sunshine-physiotherapy.json`
- `sunshine-radiology` — `au-fhir-test-data-set/au-core/Organization-sunshine-radiology.json`

</details>

<details><summary><strong>Family scenario w baby (2 month old)</strong> (98 entities)</summary>

**Patient** (4)

- `lowe-alessandra` — `au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json` — *also in: [families](#families) (free to build on)*
- `lowe-alix` — `au-fhir-test-data-set/au-core/Patient-lowe-alix.json` — *also in: [families](#families) (free to build on)*
- `lowe-cedric` — `au-fhir-test-data-set/au-core/Patient-lowe-cedric.json` — *also in: [families](#families) (free to build on)*
- `lowe-valerie` — `au-fhir-test-data-set/au-core/Patient-lowe-valerie.json` — *also in: [families](#families) (free to build on)*

**PractitionerRole** (33)

- `berridge-beulah` — `au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json`
- `breadmore-phillip` — `au-fhir-test-data-set/au-core/PractitionerRole-breadmore-phillip.json`
- `cox-sandra` — `au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json`
- `dawson-kent` — `au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json`
- `duncan-xenia` — `au-fhir-test-data-set/au-core/PractitionerRole-duncan-xenia.json`
- `ellison-abby` — `au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json`
- `ewing-jude` — `au-fhir-test-data-set/au-core/PractitionerRole-ewing-jude.json`
- `fleming-kitty` — `au-fhir-test-data-set/au-core/PractitionerRole-fleming-kitty.json`
- `frank-gaylene` — `au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json`
- `fuller-christeen` — `au-fhir-test-data-set/au-core/PractitionerRole-fuller-christeen.json`
- `goodwin-rae` — `au-fhir-test-data-set/au-core/PractitionerRole-goodwin-rae.json`
- `hamilton-errol` — `au-fhir-test-data-set/au-core/PractitionerRole-hamilton-errol.json`
- `healey-tamiko` — `au-fhir-test-data-set/au-core/PractitionerRole-healey-tamiko.json`
- `howe-elden` — `au-fhir-test-data-set/au-core/PractitionerRole-howe-elden.json`
- `knowles-sunshine` — `au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json`
- `lapthorn-leisa` — `au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json`
- `little-jerrie` — `au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json`
- `macey-brant` — `au-fhir-test-data-set/au-core/PractitionerRole-macey-brant.json`
- `mcbean-nicollette` — `au-fhir-test-data-set/au-core/PractitionerRole-mcbean-nicollette.json`
- `mcintosh-angelica` — `au-fhir-test-data-set/au-core/PractitionerRole-mcintosh-angelica.json`
- `mcnab-angelina` — `au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json`
- `mills-hope` — `au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json`
- `nairn-vince` — `au-fhir-test-data-set/au-core/PractitionerRole-nairn-vince.json`
- `neville-isaiah` — `au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json`
- `nutley-bradley` — `au-fhir-test-data-set/au-core/PractitionerRole-nutley-bradley.json`
- `ohalloran-sheryl` — `au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json`
- `osmond-michele` — `au-fhir-test-data-set/au-core/PractitionerRole-osmond-michele.json`
- `perkins-amee` — `au-fhir-test-data-set/au-core/PractitionerRole-perkins-amee.json`
- `redman-mariah` — `au-fhir-test-data-set/au-core/PractitionerRole-redman-mariah.json`
- `roche-garfield` — `au-fhir-test-data-set/au-core/PractitionerRole-roche-garfield.json`
- `seaby-penelope` — `au-fhir-test-data-set/au-core/PractitionerRole-seaby-penelope.json`
- `stephens-nellie` — `au-fhir-test-data-set/au-core/PractitionerRole-stephens-nellie.json`
- `tate-melvin` — `au-fhir-test-data-set/au-core/PractitionerRole-tate-melvin.json`

**Practitioner** (33)

- `berridge-beulah` — `au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json`
- `breadmore-phillip` — `au-fhir-test-data-set/au-core/Practitioner-breadmore-phillip.json`
- `cox-sandra` — `au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json`
- `dawson-kent` — `au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json`
- `duncan-xenia` — `au-fhir-test-data-set/au-core/Practitioner-duncan-xenia.json`
- `ellison-abby` — `au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json`
- `ewing-jude` — `au-fhir-test-data-set/au-core/Practitioner-ewing-jude.json`
- `fleming-kitty` — `au-fhir-test-data-set/au-core/Practitioner-fleming-kitty.json`
- `frank-gaylene` — `au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json`
- `fuller-christeen` — `au-fhir-test-data-set/au-core/Practitioner-fuller-christeen.json`
- `goodwin-rae` — `au-fhir-test-data-set/au-core/Practitioner-goodwin-rae.json`
- `hamilton-errol` — `au-fhir-test-data-set/au-core/Practitioner-hamilton-errol.json`
- `healey-tamiko` — `au-fhir-test-data-set/au-core/Practitioner-healey-tamiko.json`
- `howe-elden` — `au-fhir-test-data-set/au-core/Practitioner-howe-elden.json`
- `knowles-sunshine` — `au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json`
- `lapthorn-leisa` — `au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `little-jerrie` — `au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json`
- `macey-brant` — `au-fhir-test-data-set/au-core/Practitioner-macey-brant.json`
- `mcbean-nicollette` — `au-fhir-test-data-set/au-core/Practitioner-mcbean-nicollette.json`
- `mcintosh-angelica` — `au-fhir-test-data-set/au-core/Practitioner-mcintosh-angelica.json`
- `mcnab-angelina` — `au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `mills-hope` — `au-fhir-test-data-set/au-core/Practitioner-mills-hope.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `nairn-vince` — `au-fhir-test-data-set/au-core/Practitioner-nairn-vince.json`
- `neville-isaiah` — `au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json`
- `nutley-bradley` — `au-fhir-test-data-set/au-core/Practitioner-nutley-bradley.json`
- `ohalloran-sheryl` — `au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json`
- `osmond-michele` — `au-fhir-test-data-set/au-core/Practitioner-osmond-michele.json`
- `perkins-amee` — `au-fhir-test-data-set/au-core/Practitioner-perkins-amee.json`
- `redman-mariah` — `au-fhir-test-data-set/au-core/Practitioner-redman-mariah.json`
- `roche-garfield` — `au-fhir-test-data-set/au-core/Practitioner-roche-garfield.json`
- `seaby-penelope` — `au-fhir-test-data-set/au-core/Practitioner-seaby-penelope.json`
- `stephens-nellie` — `au-fhir-test-data-set/au-core/Practitioner-stephens-nellie.json`
- `tate-melvin` — `au-fhir-test-data-set/au-core/Practitioner-tate-melvin.json`

**Organization** (16)

- `parramatta-community-health` — `au-fhir-test-data-set/au-core/Organization-parramatta-community-health.json`
- `parramatta-dental` — `au-fhir-test-data-set/au-core/Organization-parramatta-dental.json`
- `parramatta-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json`
- `parramatta-midwifery` — `au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json`
- `parramatta-nutrition` — `au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json`
- `parramatta-public-hospital` — `au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json`
- `parramatta-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json`
- `westmead-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json`
- `westmead-optical` — `au-fhir-test-data-set/au-core/Organization-westmead-optical.json`
- `westmead-ot-services` — `au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json`
- `westmead-pathology` — `au-fhir-test-data-set/au-core/Organization-westmead-pathology.json`
- `westmead-pharmacy` — `au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json`
- `westmead-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json`
- `westmead-public-hospital` — `au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json`
- `westmead-radiology` — `au-fhir-test-data-set/au-core/Organization-westmead-radiology.json`
- `westmead-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json`

**RelatedPerson** (12)

- `lowe-alessandra-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-1.json`
- `lowe-alessandra-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-2.json`
- `lowe-alessandra-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-3.json`
- `lowe-alix-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-1.json`
- `lowe-alix-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-2.json`
- `lowe-alix-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-3.json`
- `lowe-cedric-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-1.json`
- `lowe-cedric-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-2.json`
- `lowe-cedric-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-3.json`
- `lowe-valerie-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-1.json`
- `lowe-valerie-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-2.json`
- `lowe-valerie-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-3.json`

</details>

<details><summary><strong>FIrst nations scenario</strong> (51 entities)</summary>

**Patient** (1)

- `coombe-ross` — `au-fhir-test-data-set/au-core/Patient-coombe-ross.json`

**PractitionerRole** (20)

- `allardice-della` — `au-fhir-test-data-set/au-core/PractitionerRole-allardice-della.json`
- `baratz-layla` — `au-fhir-test-data-set/au-core/PractitionerRole-baratz-layla.json`
- `bassett-elmer` — `au-fhir-test-data-set/au-core/PractitionerRole-bassett-elmer.json`
- `butler-cheryl` — `au-fhir-test-data-set/au-core/PractitionerRole-butler-cheryl.json`
- `clapham-laurie` — `au-fhir-test-data-set/au-core/PractitionerRole-clapham-laurie.json`
- `davies-keiko` — `au-fhir-test-data-set/au-core/PractitionerRole-davies-keiko.json`
- `devine-frank` — `au-fhir-test-data-set/au-core/PractitionerRole-devine-frank.json`
- `gates-anton` — `au-fhir-test-data-set/au-core/PractitionerRole-gates-anton.json`
- `giles-veronique` — `au-fhir-test-data-set/au-core/PractitionerRole-giles-veronique.json`
- `goldsmith-monique` — `au-fhir-test-data-set/au-core/PractitionerRole-goldsmith-monique.json`
- `hackett-norman` — `au-fhir-test-data-set/au-core/PractitionerRole-hackett-norman.json`
- `hodges-julia` — `au-fhir-test-data-set/au-core/PractitionerRole-hodges-julia.json`
- `horn-wes` — `au-fhir-test-data-set/au-core/PractitionerRole-horn-wes.json`
- `ibbotson-destiny` — `au-fhir-test-data-set/au-core/PractitionerRole-ibbotson-destiny.json`
- `lowry-bennett` — `au-fhir-test-data-set/au-core/PractitionerRole-lowry-bennett.json`
- `moran-linoel` — `au-fhir-test-data-set/au-core/PractitionerRole-moran-linoel.json`
- `patrick-thalia` — `au-fhir-test-data-set/au-core/PractitionerRole-patrick-thalia.json`
- `poulson-lisa` — `au-fhir-test-data-set/au-core/PractitionerRole-poulson-lisa.json`
- `simmons-ashton` — `au-fhir-test-data-set/au-core/PractitionerRole-simmons-ashton.json`
- `thorburn-juanita` — `au-fhir-test-data-set/au-core/PractitionerRole-thorburn-juanita.json`

**Practitioner** (20)

- `allardice-della` — `au-fhir-test-data-set/au-core/Practitioner-allardice-della.json`
- `baratz-layla` — `au-fhir-test-data-set/au-core/Practitioner-baratz-layla.json`
- `bassett-elmer` — `au-fhir-test-data-set/au-core/Practitioner-bassett-elmer.json`
- `butler-cheryl` — `au-fhir-test-data-set/au-core/Practitioner-butler-cheryl.json`
- `clapham-laurie` — `au-fhir-test-data-set/au-core/Practitioner-clapham-laurie.json`
- `davies-keiko` — `au-fhir-test-data-set/au-core/Practitioner-davies-keiko.json`
- `devine-frank` — `au-fhir-test-data-set/au-core/Practitioner-devine-frank.json`
- `gates-anton` — `au-fhir-test-data-set/au-core/Practitioner-gates-anton.json`
- `giles-veronique` — `au-fhir-test-data-set/au-core/Practitioner-giles-veronique.json`
- `goldsmith-monique` — `au-fhir-test-data-set/au-core/Practitioner-goldsmith-monique.json`
- `hackett-norman` — `au-fhir-test-data-set/au-core/Practitioner-hackett-norman.json`
- `hodges-julia` — `au-fhir-test-data-set/au-core/Practitioner-hodges-julia.json`
- `horn-wes` — `au-fhir-test-data-set/au-core/Practitioner-horn-wes.json`
- `ibbotson-destiny` — `au-fhir-test-data-set/au-core/Practitioner-ibbotson-destiny.json`
- `lowry-bennett` — `au-fhir-test-data-set/au-core/Practitioner-lowry-bennett.json`
- `moran-linoel` — `au-fhir-test-data-set/au-core/Practitioner-moran-linoel.json`
- `patrick-thalia` — `au-fhir-test-data-set/au-core/Practitioner-patrick-thalia.json`
- `poulson-lisa` — `au-fhir-test-data-set/au-core/Practitioner-poulson-lisa.json`
- `simmons-ashton` — `au-fhir-test-data-set/au-core/Practitioner-simmons-ashton.json`
- `thorburn-juanita` — `au-fhir-test-data-set/au-core/Practitioner-thorburn-juanita.json`

**Organization** (10)

- `broome-community-health` — `au-fhir-test-data-set/au-core/Organization-broome-community-health.json`
- `broome-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json`
- `broome-nutrition` — `au-fhir-test-data-set/au-core/Organization-broome-nutrition.json`
- `broome-optometry` — `au-fhir-test-data-set/au-core/Organization-broome-optometry.json`
- `broome-ot-services` — `au-fhir-test-data-set/au-core/Organization-broome-ot-services.json`
- `broome-physiology` — `au-fhir-test-data-set/au-core/Organization-broome-physiology.json`
- `broome-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-broome-physiotherapy.json`
- `broome-podiatry` — `au-fhir-test-data-set/au-core/Organization-broome-podiatry.json`
- `broome-psychology` — `au-fhir-test-data-set/au-core/Organization-broome-psychology.json`
- `broome-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json`

</details>

<details><summary><strong>Paeds scenario (5yo)</strong> (56 entities)</summary>

**Patient** (3)

- `hennessy-billy` — `au-fhir-test-data-set/au-core/Patient-hennessy-billy.json` — *also in: [families](#families) (free to build on)*
- `hennessy-jenny` — `au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json` — *also in: [families](#families) (free to build on)*
- `hennessy-kacey` — `au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json` — *also in: [families](#families) (free to build on)*

**PractitionerRole** (17)

- `allerton-skye` — `au-fhir-test-data-set/au-core/PractitionerRole-allerton-skye.json`
- `bennett-tawnya` — `au-fhir-test-data-set/au-core/PractitionerRole-bennett-tawnya.json`
- `colliss-jocelyn` — `au-fhir-test-data-set/au-core/PractitionerRole-colliss-jocelyn.json`
- `harris-stephan` — `au-fhir-test-data-set/au-core/PractitionerRole-harris-stephan.json`
- `harrower-austin` — `au-fhir-test-data-set/au-core/PractitionerRole-harrower-austin.json`
- `harwood-kathaleen` — `au-fhir-test-data-set/au-core/PractitionerRole-harwood-kathaleen.json`
- `henderson-elaine` — `au-fhir-test-data-set/au-core/PractitionerRole-henderson-elaine.json`
- `humphreys-christeen` — `au-fhir-test-data-set/au-core/PractitionerRole-humphreys-christeen.json`
- `krug-chas` — `au-fhir-test-data-set/au-core/PractitionerRole-krug-chas.json`
- `levings-richard` — `au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json`
- `mackenzie-wilbur` — `au-fhir-test-data-set/au-core/PractitionerRole-mackenzie-wilbur.json`
- `maxwell-israel` — `au-fhir-test-data-set/au-core/PractitionerRole-maxwell-israel.json`
- `murphy-kyla` — `au-fhir-test-data-set/au-core/PractitionerRole-murphy-kyla.json`
- `newling-mariella` — `au-fhir-test-data-set/au-core/PractitionerRole-newling-mariella.json`
- `patrick-tricia` — `au-fhir-test-data-set/au-core/PractitionerRole-patrick-tricia.json`
- `sawtell-tomasa` — `au-fhir-test-data-set/au-core/PractitionerRole-sawtell-tomasa.json`
- `short-tandra` — `au-fhir-test-data-set/au-core/PractitionerRole-short-tandra.json`

**Practitioner** (17)

- `allerton-skye` — `au-fhir-test-data-set/au-core/Practitioner-allerton-skye.json`
- `bennett-tawnya` — `au-fhir-test-data-set/au-core/Practitioner-bennett-tawnya.json`
- `colliss-jocelyn` — `au-fhir-test-data-set/au-core/Practitioner-colliss-jocelyn.json`
- `harris-stephan` — `au-fhir-test-data-set/au-core/Practitioner-harris-stephan.json`
- `harrower-austin` — `au-fhir-test-data-set/au-core/Practitioner-harrower-austin.json`
- `harwood-kathaleen` — `au-fhir-test-data-set/au-core/Practitioner-harwood-kathaleen.json`
- `henderson-elaine` — `au-fhir-test-data-set/au-core/Practitioner-henderson-elaine.json`
- `humphreys-christeen` — `au-fhir-test-data-set/au-core/Practitioner-humphreys-christeen.json`
- `krug-chas` — `au-fhir-test-data-set/au-core/Practitioner-krug-chas.json`
- `levings-richard` — `au-fhir-test-data-set/au-core/Practitioner-levings-richard.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `mackenzie-wilbur` — `au-fhir-test-data-set/au-core/Practitioner-mackenzie-wilbur.json`
- `maxwell-israel` — `au-fhir-test-data-set/au-core/Practitioner-maxwell-israel.json`
- `murphy-kyla` — `au-fhir-test-data-set/au-core/Practitioner-murphy-kyla.json`
- `newling-mariella` — `au-fhir-test-data-set/au-core/Practitioner-newling-mariella.json`
- `patrick-tricia` — `au-fhir-test-data-set/au-core/Practitioner-patrick-tricia.json`
- `sawtell-tomasa` — `au-fhir-test-data-set/au-core/Practitioner-sawtell-tomasa.json`
- `short-tandra` — `au-fhir-test-data-set/au-core/Practitioner-short-tandra.json`

**Organization** (13)

- `garran-cardiology-clinic` — `au-fhir-test-data-set/au-core/Organization-garran-cardiology-clinic.json`
- `garran-dental` — `au-fhir-test-data-set/au-core/Organization-garran-dental.json`
- `garran-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json`
- `garran-nephrology` — `au-fhir-test-data-set/au-core/Organization-garran-nephrology.json`
- `garran-nutrition` — `au-fhir-test-data-set/au-core/Organization-garran-nutrition.json`
- `garran-ophthalmology` — `au-fhir-test-data-set/au-core/Organization-garran-ophthalmology.json`
- `garran-optical` — `au-fhir-test-data-set/au-core/Organization-garran-optical.json`
- `garran-ot-services` — `au-fhir-test-data-set/au-core/Organization-garran-ot-services.json`
- `garran-pathology` — `au-fhir-test-data-set/au-core/Organization-garran-pathology.json`
- `garran-pharmacy` — `au-fhir-test-data-set/au-core/Organization-garran-pharmacy.json`
- `garran-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-garran-physiotherapy.json`
- `garran-radiology` — `au-fhir-test-data-set/au-core/Organization-garran-radiology.json`
- `manuka-medical-centre` — `au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json`

**RelatedPerson** (6)

- `hennessy-billy-1` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-1.json`
- `hennessy-billy-2` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-2.json`
- `hennessy-jenny-1` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-1.json`
- `hennessy-jenny-2` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-2.json`
- `hennessy-kacey-1` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-1.json`
- `hennessy-kacey-2` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-2.json`

</details>

<details><summary><strong>Rural &amp; remote scenario</strong> (74 entities)</summary>

**Patient** (1)

- `mclennan-karl` — `au-fhir-test-data-set/au-core/Patient-mclennan-karl.json`

**PractitionerRole** (28)

- `bailey-buck` — `au-fhir-test-data-set/au-core/PractitionerRole-bailey-buck.json`
- `barrett-kirstie` — `au-fhir-test-data-set/au-core/PractitionerRole-barrett-kirstie.json`
- `bowden-hiroko` — `au-fhir-test-data-set/au-core/PractitionerRole-bowden-hiroko.json`
- `gaynor-jasper` — `au-fhir-test-data-set/au-core/PractitionerRole-gaynor-jasper.json`
- `greenhill-edmond` — `au-fhir-test-data-set/au-core/PractitionerRole-greenhill-edmond.json`
- `haywood-dot` — `au-fhir-test-data-set/au-core/PractitionerRole-haywood-dot.json`
- `hipwood-fatimah` — `au-fhir-test-data-set/au-core/PractitionerRole-hipwood-fatimah.json`
- `hobden-mark` — `au-fhir-test-data-set/au-core/PractitionerRole-hobden-mark.json`
- `hodge-irving` — `au-fhir-test-data-set/au-core/PractitionerRole-hodge-irving.json`
- `irwin-corinna` — `au-fhir-test-data-set/au-core/PractitionerRole-irwin-corinna.json`
- `jeffery-herman` — `au-fhir-test-data-set/au-core/PractitionerRole-jeffery-herman.json`
- `jeffery-nicolas` — `au-fhir-test-data-set/au-core/PractitionerRole-jeffery-nicolas.json`
- `jeffery-sammy` — `au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json`
- `livingstone-yvonne` — `au-fhir-test-data-set/au-core/PractitionerRole-livingstone-yvonne.json`
- `lyons-shay` — `au-fhir-test-data-set/au-core/PractitionerRole-lyons-shay.json`
- `mccormack-gertie` — `au-fhir-test-data-set/au-core/PractitionerRole-mccormack-gertie.json`
- `mcintyre-hsiu` — `au-fhir-test-data-set/au-core/PractitionerRole-mcintyre-hsiu.json`
- `mclean-brenda` — `au-fhir-test-data-set/au-core/PractitionerRole-mclean-brenda.json`
- `mills-kim` — `au-fhir-test-data-set/au-core/PractitionerRole-mills-kim.json`
- `murray-xenia` — `au-fhir-test-data-set/au-core/PractitionerRole-murray-xenia.json`
- `oritz-philomena` — `au-fhir-test-data-set/au-core/PractitionerRole-oritz-philomena.json`
- `osborne-buster` — `au-fhir-test-data-set/au-core/PractitionerRole-osborne-buster.json`
- `pearce-teresa` — `au-fhir-test-data-set/au-core/PractitionerRole-pearce-teresa.json`
- `potts-xuan` — `au-fhir-test-data-set/au-core/PractitionerRole-potts-xuan.json`
- `pratt-colleen` — `au-fhir-test-data-set/au-core/PractitionerRole-pratt-colleen.json`
- `randall-anthony` — `au-fhir-test-data-set/au-core/PractitionerRole-randall-anthony.json`
- `robbins-wilhelmina` — `au-fhir-test-data-set/au-core/PractitionerRole-robbins-wilhelmina.json`
- `sherry-dean` — `au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json`

**Practitioner** (28)

- `bailey-buck` — `au-fhir-test-data-set/au-core/Practitioner-bailey-buck.json`
- `barrett-kirstie` — `au-fhir-test-data-set/au-core/Practitioner-barrett-kirstie.json`
- `bowden-hiroko` — `au-fhir-test-data-set/au-core/Practitioner-bowden-hiroko.json`
- `gaynor-jasper` — `au-fhir-test-data-set/au-core/Practitioner-gaynor-jasper.json`
- `greenhill-edmond` — `au-fhir-test-data-set/au-core/Practitioner-greenhill-edmond.json`
- `haywood-dot` — `au-fhir-test-data-set/au-core/Practitioner-haywood-dot.json`
- `hipwood-fatimah` — `au-fhir-test-data-set/au-core/Practitioner-hipwood-fatimah.json`
- `hobden-mark` — `au-fhir-test-data-set/au-core/Practitioner-hobden-mark.json`
- `hodge-irving` — `au-fhir-test-data-set/au-core/Practitioner-hodge-irving.json`
- `irwin-corinna` — `au-fhir-test-data-set/au-core/Practitioner-irwin-corinna.json`
- `jeffery-herman` — `au-fhir-test-data-set/au-core/Practitioner-jeffery-herman.json`
- `jeffery-nicolas` — `au-fhir-test-data-set/au-core/Practitioner-jeffery-nicolas.json`
- `jeffery-sammy` — `au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json`
- `livingstone-yvonne` — `au-fhir-test-data-set/au-core/Practitioner-livingstone-yvonne.json`
- `lyons-shay` — `au-fhir-test-data-set/au-core/Practitioner-lyons-shay.json`
- `mccormack-gertie` — `au-fhir-test-data-set/au-core/Practitioner-mccormack-gertie.json`
- `mcintyre-hsiu` — `au-fhir-test-data-set/au-core/Practitioner-mcintyre-hsiu.json`
- `mclean-brenda` — `au-fhir-test-data-set/au-core/Practitioner-mclean-brenda.json`
- `mills-kim` — `au-fhir-test-data-set/au-core/Practitioner-mills-kim.json`
- `murray-xenia` — `au-fhir-test-data-set/au-core/Practitioner-murray-xenia.json`
- `oritz-philomena` — `au-fhir-test-data-set/au-core/Practitioner-oritz-philomena.json`
- `osborne-buster` — `au-fhir-test-data-set/au-core/Practitioner-osborne-buster.json`
- `pearce-teresa` — `au-fhir-test-data-set/au-core/Practitioner-pearce-teresa.json`
- `potts-xuan` — `au-fhir-test-data-set/au-core/Practitioner-potts-xuan.json`
- `pratt-colleen` — `au-fhir-test-data-set/au-core/Practitioner-pratt-colleen.json`
- `randall-anthony` — `au-fhir-test-data-set/au-core/Practitioner-randall-anthony.json`
- `robbins-wilhelmina` — `au-fhir-test-data-set/au-core/Practitioner-robbins-wilhelmina.json`
- `sherry-dean` — `au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json`

**Organization** (17)

- `camooweal-community-health` — `au-fhir-test-data-set/au-core/Organization-camooweal-community-health.json`
- `camooweal-pharmacy` — `au-fhir-test-data-set/au-core/Organization-camooweal-pharmacy.json`
- `herston-pathology` — `au-fhir-test-data-set/au-core/Organization-herston-pathology.json`
- `herston-public-hospital` — `au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json`
- `herston-radiology` — `au-fhir-test-data-set/au-core/Organization-herston-radiology.json`
- `mt-isa-community-health` — `au-fhir-test-data-set/au-core/Organization-mt-isa-community-health.json`
- `mt-isa-dental` — `au-fhir-test-data-set/au-core/Organization-mt-isa-dental.json`
- `mt-isa-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-mt-isa-medical-clinic.json`
- `mt-isa-ot-services` — `au-fhir-test-data-set/au-core/Organization-mt-isa-ot-services.json`
- `mt-isa-pathology` — `au-fhir-test-data-set/au-core/Organization-mt-isa-pathology.json`
- `mt-isa-pharmacy` — `au-fhir-test-data-set/au-core/Organization-mt-isa-pharmacy.json`
- `mt-isa-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-mt-isa-physiotherapy.json`
- `mt-isa-psychology` — `au-fhir-test-data-set/au-core/Organization-mt-isa-psychology.json`
- `mt-isa-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-mt-isa-specialist-clinic.json`
- `townsville-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-townsville-medical-clinic.json`
- `townsville-public-hospital` — `au-fhir-test-data-set/au-core/Organization-townsville-public-hospital.json`
- `townsville-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-townsville-specialist-clinic.json`

</details>

<details><summary><strong>Young adult_adolescent scenario (19-20 yo)</strong> (46 entities)</summary>

**Patient** (1)

- `vaughan-seymour` — `au-fhir-test-data-set/au-core/Patient-vaughan-seymour.json`

**PractitionerRole** (18)

- `alcock-devon` — `au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json`
- `blackwood-ella` — `au-fhir-test-data-set/au-core/PractitionerRole-blackwood-ella.json`
- `dempsey-carli` — `au-fhir-test-data-set/au-core/PractitionerRole-dempsey-carli.json`
- `egan-anja` — `au-fhir-test-data-set/au-core/PractitionerRole-egan-anja.json`
- `findley-betty` — `au-fhir-test-data-set/au-core/PractitionerRole-findley-betty.json`
- `frankel-caroline` — `au-fhir-test-data-set/au-core/PractitionerRole-frankel-caroline.json`
- `greene-delores` — `au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json`
- `hatcher-merrill` — `au-fhir-test-data-set/au-core/PractitionerRole-hatcher-merrill.json`
- `higgs-allegra` — `au-fhir-test-data-set/au-core/PractitionerRole-higgs-allegra.json`
- `hilton-della` — `au-fhir-test-data-set/au-core/PractitionerRole-hilton-della.json`
- `joyce-mae` — `au-fhir-test-data-set/au-core/PractitionerRole-joyce-mae.json`
- `keith-margot` — `au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json`
- `laing-malinda` — `au-fhir-test-data-set/au-core/PractitionerRole-laing-malinda.json`
- `mckane-eugena` — `au-fhir-test-data-set/au-core/PractitionerRole-mckane-eugena.json`
- `mullin-kenny` — `au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json`
- `murray-ashli` — `au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json`
- `rodd-illa` — `au-fhir-test-data-set/au-core/PractitionerRole-rodd-illa.json`
- `shephard-vern` — `au-fhir-test-data-set/au-core/PractitionerRole-shephard-vern.json`

**Practitioner** (18)

- `alcock-devon` — `au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json`
- `blackwood-ella` — `au-fhir-test-data-set/au-core/Practitioner-blackwood-ella.json`
- `dempsey-carli` — `au-fhir-test-data-set/au-core/Practitioner-dempsey-carli.json`
- `egan-anja` — `au-fhir-test-data-set/au-core/Practitioner-egan-anja.json`
- `findley-betty` — `au-fhir-test-data-set/au-core/Practitioner-findley-betty.json`
- `frankel-caroline` — `au-fhir-test-data-set/au-core/Practitioner-frankel-caroline.json`
- `greene-delores` — `au-fhir-test-data-set/au-core/Practitioner-greene-delores.json`
- `hatcher-merrill` — `au-fhir-test-data-set/au-core/Practitioner-hatcher-merrill.json`
- `higgs-allegra` — `au-fhir-test-data-set/au-core/Practitioner-higgs-allegra.json`
- `hilton-della` — `au-fhir-test-data-set/au-core/Practitioner-hilton-della.json`
- `joyce-mae` — `au-fhir-test-data-set/au-core/Practitioner-joyce-mae.json`
- `keith-margot` — `au-fhir-test-data-set/au-core/Practitioner-keith-margot.json`
- `laing-malinda` — `au-fhir-test-data-set/au-core/Practitioner-laing-malinda.json`
- `mckane-eugena` — `au-fhir-test-data-set/au-core/Practitioner-mckane-eugena.json`
- `mullin-kenny` — `au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json`
- `murray-ashli` — `au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json`
- `rodd-illa` — `au-fhir-test-data-set/au-core/Practitioner-rodd-illa.json`
- `shephard-vern` — `au-fhir-test-data-set/au-core/Practitioner-shephard-vern.json`

**Organization** (9)

- `melbourne-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json`
- `southbank-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json`
- `southbank-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json`
- `southbank-speech-pathology` — `au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json`
- `st-kilda-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json`
- `st-kilda-ot-services` — `au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json`
- `st-kilda-physiology` — `au-fhir-test-data-set/au-core/Organization-st-kilda-physiology.json`
- `st-kilda-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-st-kilda-physiotherapy.json`
- `st-kilda-psychology` — `au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json`

</details>


## Geographic groupings <a id="geography-groups"></a>

### Purpose

Proposes groupings of entities that are plausibly co-located, as a starting point for constructing new consumer journeys.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Grouping identifies plausible co-location only. Members are free to build on and are not reserved to their originating group.

### Provenance & use

Proposed by a script from address data and confirmed by a human. Best- effort by design: postcode proximity is a weak proxy, and there are no coordinates anywhere in the data set to check real distance against.

### Relationships

[Scenario groupings](#scenario-groups) draw heavily on the same entities, since each scenario was built around a specific locality.

### How is this subset identified?

Derived, then confirmed by a human. Metro entities group by capital city; regional entities group by three-digit postcode bucket, widened to buckets whose third digit differs by one. Each grouping is then expanded by reverse reference to pull in the HealthcareServices and PractitionerRoles attached to its organisations, locations and practitioners. Every proposal is put to a human with its full suburb list, which stands in for the distance check the data cannot support.


_Classification: Derived + Curated._
> 8 metro groups (one per capital city) and 85 regional windows (3-digit postcode bucket, widened to buckets whose 3rd digit is +/-1).
> 467 geo-eligible entities have no usable postcode and are excluded.
> 11 entities have a non-Australian address and are excluded — Australian postcode logic does not apply to them, and their postcodes collide with Australian ones (Napier NZ 4104 falls inside Brisbane's metro range).
> 60 confirmed, 33 rejected, 0 awaiting a decision.
> Metro groups by city because Australian postcodes are not spatially ordered — Southbank 3006 and St Kilda 3182 are ~6km apart but differ in the 3rd digit by 8.
> LIMITATION: a regional window can still span great distances where postcodes cover vast areas (Townsville 4810 and Mount Isa 4825 are +/-1 adjacent but ~900km apart). Check each candidate's suburb list — there are no coordinates in the data set to check distance against.

### Members (1022)

<details><summary><strong>ACT</strong> (1 grouping, 128 entities)</summary>

<blockquote>
<details><summary><strong>Canberra metropolitan</strong> (128 entities)</summary>


_Bonython, Calwell, Chisholm, Conder, Curtin, Erindale Centre, Garran, Gilmore, Ginninderra Village, Gordon, Gowrie, Macarthur, Manuka, Mitchell, Monash, Ngunnawal, Nicholls, Oxley, Palmerston, Reid, Richardson._


**Patient** (13)

- `black-kerry-dougal` — `au-fhir-test-data-set/au-core/Patient-black-kerry-dougal.json`
- `davis-juan` — `au-fhir-test-data-set/au-core/Patient-davis-juan.json`
- `dietrich-blake-louis` — `au-fhir-test-data-set/au-core/Patient-dietrich-blake-louis.json` — *also in: [families](#families) (free to build on)*
- `dietrich-diedre-alicia` — `au-fhir-test-data-set/au-core/Patient-dietrich-diedre-alicia.json` — *also in: [families](#families) (free to build on)*
- `dietrich-kimbra-althea` — `au-fhir-test-data-set/au-core/Patient-dietrich-kimbra-althea.json` — *also in: [families](#families) (free to build on)*
- `dietrich-phillipa-grace` — `au-fhir-test-data-set/au-core/Patient-dietrich-phillipa-grace.json` — *also in: [families](#families) (free to build on)*
- `downie-grant` — `au-fhir-test-data-set/au-core/Patient-downie-grant.json`
- `hennessy-billy` — `au-fhir-test-data-set/au-core/Patient-hennessy-billy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-jenny` — `au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-kacey` — `au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hulme-brant` — `au-fhir-test-data-set/au-core/Patient-hulme-brant.json`
- `ridgewell-troy` — `au-fhir-test-data-set/au-core/Patient-ridgewell-troy.json`
- `scott-elijah-ken` — `au-fhir-test-data-set/au-erequesting/Patient-scott-elijah-ken.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**PractitionerRole** (31)

- `allerton-skye` — `au-fhir-test-data-set/au-core/PractitionerRole-allerton-skye.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bennett-tawnya` — `au-fhir-test-data-set/au-core/PractitionerRole-bennett-tawnya.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `colliss-jocelyn` — `au-fhir-test-data-set/au-core/PractitionerRole-colliss-jocelyn.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `diagnostic-hill-maryln` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-hill-maryln.json`
- `generalpractitioner-bishop-horace` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-bishop-horace.json`
- `harris-stephan` — `au-fhir-test-data-set/au-core/PractitionerRole-harris-stephan.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `harrower-austin` — `au-fhir-test-data-set/au-core/PractitionerRole-harrower-austin.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `harwood-kathaleen` — `au-fhir-test-data-set/au-core/PractitionerRole-harwood-kathaleen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `henderson-elaine` — `au-fhir-test-data-set/au-core/PractitionerRole-henderson-elaine.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `humphreys-christeen` — `au-fhir-test-data-set/au-core/PractitionerRole-humphreys-christeen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `krug-chas` — `au-fhir-test-data-set/au-core/PractitionerRole-krug-chas.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `levings-richard` — `au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mackenzie-wilbur` — `au-fhir-test-data-set/au-core/PractitionerRole-mackenzie-wilbur.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `maxwell-israel` — `au-fhir-test-data-set/au-core/PractitionerRole-maxwell-israel.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `medicaldiagnostic-alderson-helene` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-alderson-helene.json`
- `midwife-pollock-dinah` — `au-fhir-test-data-set/au-core/PractitionerRole-midwife-pollock-dinah.json`
- `murphy-kyla` — `au-fhir-test-data-set/au-core/PractitionerRole-murphy-kyla.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `newling-mariella` — `au-fhir-test-data-set/au-core/PractitionerRole-newling-mariella.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `nursepractitioner-cohen-jamel` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-cohen-jamel.json`
- `nursepractitioner-grant-lindsay` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-grant-lindsay.json`
- `paediatrician-rowlands-alvera` — `au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-rowlands-alvera.json`
- `pathologist-stevens-chelsea` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-stevens-chelsea.json`
- `patrick-tricia` — `au-fhir-test-data-set/au-core/PractitionerRole-patrick-tricia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `registerednurses-donaldson-stephanie` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-donaldson-stephanie.json`
- `registerednurses-gidley-stan` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-stan.json`
- `registerednurses-nairn-ricky` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-nairn-ricky.json`
- `retailpharmacist-lees-noreen` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-lees-noreen.json`
- `sawtell-tomasa` — `au-fhir-test-data-set/au-core/PractitionerRole-sawtell-tomasa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `short-tandra` — `au-fhir-test-data-set/au-core/PractitionerRole-short-tandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `surgeongeneral-cross-lizzie` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-cross-lizzie.json`
- `surgeongeneral-pickford-aimee` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-pickford-aimee.json`

**Practitioner** (42)

- `alderson-helene` — `au-fhir-test-data-set/au-core/Practitioner-alderson-helene.json`
- `allen-yelena` — `au-fhir-test-data-set/au-core/Practitioner-allen-yelena.json`
- `allerton-skye` — `au-fhir-test-data-set/au-core/Practitioner-allerton-skye.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `becker-valentina` — `au-fhir-test-data-set/au-core/Practitioner-becker-valentina.json`
- `bennett-tawnya` — `au-fhir-test-data-set/au-core/Practitioner-bennett-tawnya.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bishop-horace` — `au-fhir-test-data-set/au-core/Practitioner-bishop-horace.json`
- `briggs-cheyenne` — `au-fhir-test-data-set/au-core/Practitioner-briggs-cheyenne.json`
- `brooksby-susanna` — `au-fhir-test-data-set/au-core/Practitioner-brooksby-susanna.json`
- `cohen-jamel` — `au-fhir-test-data-set/au-core/Practitioner-cohen-jamel.json`
- `colliss-jocelyn` — `au-fhir-test-data-set/au-core/Practitioner-colliss-jocelyn.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cross-lizzie` — `au-fhir-test-data-set/au-core/Practitioner-cross-lizzie.json`
- `donaldson-stephanie` — `au-fhir-test-data-set/au-core/Practitioner-donaldson-stephanie.json`
- `gidley-stan` — `au-fhir-test-data-set/au-core/Practitioner-gidley-stan.json`
- `gilkinson-tyron` — `au-fhir-test-data-set/au-core/Practitioner-gilkinson-tyron.json`
- `grant-lindsay` — `au-fhir-test-data-set/au-core/Practitioner-grant-lindsay.json`
- `harris-stephan` — `au-fhir-test-data-set/au-core/Practitioner-harris-stephan.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `harrower-austin` — `au-fhir-test-data-set/au-core/Practitioner-harrower-austin.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `harwood-kathaleen` — `au-fhir-test-data-set/au-core/Practitioner-harwood-kathaleen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `henderson-elaine` — `au-fhir-test-data-set/au-core/Practitioner-henderson-elaine.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hill-maryln` — `au-fhir-test-data-set/au-core/Practitioner-hill-maryln.json`
- `humphreys-christeen` — `au-fhir-test-data-set/au-core/Practitioner-humphreys-christeen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `krug-chas` — `au-fhir-test-data-set/au-core/Practitioner-krug-chas.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lees-noreen` — `au-fhir-test-data-set/au-core/Practitioner-lees-noreen.json`
- `levings-richard` — `au-fhir-test-data-set/au-core/Practitioner-levings-richard.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `mackenzie-wilbur` — `au-fhir-test-data-set/au-core/Practitioner-mackenzie-wilbur.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `maxwell-israel` — `au-fhir-test-data-set/au-core/Practitioner-maxwell-israel.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mccarthy-heide` — `au-fhir-test-data-set/au-core/Practitioner-mccarthy-heide.json`
- `mcmahon-yasuko` — `au-fhir-test-data-set/au-core/Practitioner-mcmahon-yasuko.json`
- `murphy-kyla` — `au-fhir-test-data-set/au-core/Practitioner-murphy-kyla.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `murphy-virginia` — `au-fhir-test-data-set/au-core/Practitioner-murphy-virginia.json`
- `nairn-ricky` — `au-fhir-test-data-set/au-core/Practitioner-nairn-ricky.json`
- `newling-mariella` — `au-fhir-test-data-set/au-core/Practitioner-newling-mariella.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parkinson-ethel` — `au-fhir-test-data-set/au-core/Practitioner-parkinson-ethel.json`
- `patrick-tricia` — `au-fhir-test-data-set/au-core/Practitioner-patrick-tricia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `pickford-aimee` — `au-fhir-test-data-set/au-core/Practitioner-pickford-aimee.json`
- `pollock-dinah` — `au-fhir-test-data-set/au-core/Practitioner-pollock-dinah.json`
- `rowlands-alvera` — `au-fhir-test-data-set/au-core/Practitioner-rowlands-alvera.json`
- `sawtell-tomasa` — `au-fhir-test-data-set/au-core/Practitioner-sawtell-tomasa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `seymour-sol` — `au-fhir-test-data-set/au-core/Practitioner-seymour-sol.json`
- `short-tandra` — `au-fhir-test-data-set/au-core/Practitioner-short-tandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `stevens-chelsea` — `au-fhir-test-data-set/au-core/Practitioner-stevens-chelsea.json`
- `turnbull-daniel` — `au-fhir-test-data-set/au-core/Practitioner-turnbull-daniel.json`

**HealthcareService** (6)

- `diagnosticimaging-nicholls-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-nicholls-radiology.json`
- `generalmedical-ngunnawal-medical-practice` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-ngunnawal-medical-practice.json`
- `pathologylaboratory-calwell-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-calwell-pathology.json`
- `pharmacyretail-ginninderra-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-ginninderra-pharmacy.json`
- `privateacute-monash-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-monash-private-hospital.json`
- `publicacute-oxley-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-oxley-public-hospital.json`

**Organization** (21)

- `calwell-pathology` — `au-fhir-test-data-set/au-core/Organization-calwell-pathology.json`
- `curtin-care-and-support` — `au-fhir-test-data-set/au-core/Organization-curtain-care-and-support.json` — *also in: [community-contributions](#community-contributions) (free to build on)*
- `garran-cardiology-clinic` — `au-fhir-test-data-set/au-core/Organization-garran-cardiology-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-dental` — `au-fhir-test-data-set/au-core/Organization-garran-dental.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-nephrology` — `au-fhir-test-data-set/au-core/Organization-garran-nephrology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-nutrition` — `au-fhir-test-data-set/au-core/Organization-garran-nutrition.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-ophthalmology` — `au-fhir-test-data-set/au-core/Organization-garran-ophthalmology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-optical` — `au-fhir-test-data-set/au-core/Organization-garran-optical.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-ot-services` — `au-fhir-test-data-set/au-core/Organization-garran-ot-services.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-pathology` — `au-fhir-test-data-set/au-core/Organization-garran-pathology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-pharmacy` — `au-fhir-test-data-set/au-core/Organization-garran-pharmacy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-garran-physiotherapy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `garran-radiology` — `au-fhir-test-data-set/au-core/Organization-garran-radiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ginninderra-pharmacy` — `au-fhir-test-data-set/au-core/Organization-ginninderra-pharmacy.json`
- `manuka-medical-centre` — `au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `monash-private-hospital` — `au-fhir-test-data-set/au-core/Organization-monash-private-hospital.json`
- `ngunnawal-medical-practice` — `au-fhir-test-data-set/au-core/Organization-ngunnawal-medical-practice.json`
- `nicholls-radiology` — `au-fhir-test-data-set/au-core/Organization-nicholls-radiology.json`
- `oxley-public-hospital` — `au-fhir-test-data-set/au-core/Organization-oxley-public-hospital.json`
- `reid-health-network` — `au-fhir-test-data-set/au-core/Organization-reid-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

**Location** (6)

- `calwell-pathology` — `au-fhir-test-data-set/au-core/Location-calwell-pathology.json`
- `ginninderra-pharmacy` — `au-fhir-test-data-set/au-core/Location-ginninderra-pharmacy.json`
- `monash-private-hospital` — `au-fhir-test-data-set/au-core/Location-monash-private-hospital.json`
- `ngunnawal-medical-practice` — `au-fhir-test-data-set/au-core/Location-ngunnawal-medical-practice.json`
- `nicholls-radiology` — `au-fhir-test-data-set/au-core/Location-nicholls-radiology.json`
- `oxley-public-hospital` — `au-fhir-test-data-set/au-core/Location-oxley-public-hospital.json`

**RelatedPerson** (9)

- `dietrich-phillipa-2` — `au-fhir-test-data-set/au-core/RelatedPerson-dietrich-phillipa-2.json`
- `dietrich-phillipa-3` — `au-fhir-test-data-set/au-core/RelatedPerson-dietrich-phillipa-3.json`
- `dietrich-phillipa-4` — `au-fhir-test-data-set/au-core/RelatedPerson-dietrich-phillipa-4.json`
- `hennessy-billy-1` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-billy-2` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-jenny-1` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-jenny-2` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-kacey-1` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-kacey-2` — `au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

</details>
</blockquote>

</details>

<details><summary><strong>NSW</strong> (14 groupings, 222 entities)</summary>

<blockquote>
<details><summary><strong>Postcodes 224xx-226xx</strong> (8 entities)</summary>


_Bucketty, Canton Beach, Koolewong._


**PractitionerRole** (1)

- `medicaldiagnostic-tennant-carlyn` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-tennant-carlyn.json`

**Practitioner** (1)

- `tennant-carlyn` — `au-fhir-test-data-set/au-core/Practitioner-tennant-carlyn.json`

**HealthcareService** (2)

- `physiotherapyservices-canton-beach-physiotherapy` — `au-fhir-test-data-set/au-core/HealthcareService-physiotherapyservices-canton-beach-physiotherapy.json`
- `specialistmedical-bucketty-oncology-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-bucketty-oncology-clinic.json`

**Organization** (2)

- `bucketty-oncology-clinic` — `au-fhir-test-data-set/au-core/Organization-bucketty-oncology-clinic.json`
- `canton-beach-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-canton-beach-physiotherapy.json`

**Location** (2)

- `bucketty-oncology-clinic` — `au-fhir-test-data-set/au-core/Location-bucketty-oncology-clinic.json`
- `canton-beach-physiotherapy` — `au-fhir-test-data-set/au-core/Location-canton-beach-physiotherapy.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 235xx-237xx</strong> (9 entities)</summary>


_Mount Mitchell._


**PractitionerRole** (3)

- `nursepractitioner-munro-rose` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-munro-rose.json`
- `registerednurses-milgate-leisa` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-milgate-leisa.json`
- `surgeongeneral-guthrie-daine` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-guthrie-daine.json`

**Practitioner** (3)

- `guthrie-daine` — `au-fhir-test-data-set/au-core/Practitioner-guthrie-daine.json`
- `milgate-leisa` — `au-fhir-test-data-set/au-core/Practitioner-milgate-leisa.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `munro-rose` — `au-fhir-test-data-set/au-core/Practitioner-munro-rose.json`

**HealthcareService** (1)

- `privateacute-mount-mitchell-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-mount-mitchell-private-hospital.json`

**Organization** (1)

- `mount-mitchell-private-hospital` — `au-fhir-test-data-set/au-core/Organization-mount-mitchell-private-hospital.json`

**Location** (1)

- `mount-mitchell-private-hospital` — `au-fhir-test-data-set/au-core/Location-mount-mitchell-private-hospital.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 241xx-243xx</strong> (5 entities)</summary>


_Cundle Flat, Gangat._


**PractitionerRole** (1)

- `medicaldiagnostic-gates-glenda` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-gates-glenda.json`

**Practitioner** (1)

- `gates-glenda` — `au-fhir-test-data-set/au-core/Practitioner-gates-glenda.json`

**HealthcareService** (1)

- `specialistmedical-gangat-endocrinology-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-gangat-endocrinology-clinic.json`

**Organization** (1)

- `gangat-endocrinology-clinic` — `au-fhir-test-data-set/au-core/Organization-gangat-endocrinology-clinic.json`

**Location** (1)

- `gangat-endocrinology-clinic` — `au-fhir-test-data-set/au-core/Location-gangat-endocrinology-clinic.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 243xx-245xx</strong> (8 entities)</summary>


_Belmore River, Fishermans Reach, Yarravel._


**Patient** (1)

- `irvine-ronny-lawrence` — `au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*

**PractitionerRole** (2)

- `complementaryhealth-gilchrist-daniel` — `au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-gilchrist-daniel.json`
- `diagnostic-osborne-bonny` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-osborne-bonny.json`

**Practitioner** (2)

- `gilchrist-daniel` — `au-fhir-test-data-set/au-core/Practitioner-gilchrist-daniel.json`
- `osborne-bonny` — `au-fhir-test-data-set/au-core/Practitioner-osborne-bonny.json`

**HealthcareService** (1)

- `diagnosticimaging-fishermans-reach-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-fishermans-reach-radiology.json`

**Organization** (1)

- `fishermans-reach-radiology` — `au-fhir-test-data-set/au-core/Organization-fishermans-reach-radiology.json`

**Location** (1)

- `fishermans-reach-radiology` — `au-fhir-test-data-set/au-core/Location-fishermans-reach-radiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 245xx-247xx</strong> (8 entities)</summary>


_Kippenduff, Lilydale._


**PractitionerRole** (1)

- `retailpharmacist-cane-elden` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-cane-elden.json`

**Practitioner** (1)

- `cane-elden` — `au-fhir-test-data-set/au-core/Practitioner-cane-elden.json`

**HealthcareService** (2)

- `pharmacyretail-lilydale-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-lilydale-pharmacy.json`
- `specialistmedical-kippenduff-cardiologist` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-kippenduff-cardiologist.json`

**Organization** (2)

- `kippenduff-cardiologist` — `au-fhir-test-data-set/au-core/Organization-kippenduff-cardiologist.json`
- `lilydale-pharmacy` — `au-fhir-test-data-set/au-core/Organization-lilydale-pharmacy.json`

**Location** (2)

- `kippenduff-cardiologist` — `au-fhir-test-data-set/au-core/Location-kippenduff-cardiologist.json`
- `lilydale-pharmacy` — `au-fhir-test-data-set/au-core/Location-lilydale-pharmacy.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 247xx-249xx</strong> (8 entities)</summary>


_Bungabbee, Palmvale._


**Patient** (1)

- `johnson-joyce` — `au-fhir-test-data-set/au-core/Patient-johnson-joyce.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**PractitionerRole** (2)

- `generalpractitioner-burrows-ginger` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `registerednurses-patrick-fletcher` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-patrick-fletcher.json`

**Practitioner** (2)

- `burrows-ginger` — `au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `patrick-fletcher` — `au-fhir-test-data-set/au-core/Practitioner-patrick-fletcher.json`

**HealthcareService** (1)

- `generalpractice-bungabbee-medical-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-generalpractice-bungabbee-medical-clinic.json`

**Organization** (1)

- `bungabbee-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

**Location** (1)

- `bungabbee-medical-clinic` — `au-fhir-test-data-set/au-core/Location-bungabbee-medical-clinic.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 252xx-254xx</strong> (7 entities)</summary>


_Mossy Point._


**PractitionerRole** (2)

- `generalpractitioner-lowe-abe` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json`
- `registerednurses-roberts-benjamin` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-roberts-benjamin.json`

**Practitioner** (2)

- `lowe-abe` — `au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `roberts-benjamin` — `au-fhir-test-data-set/au-core/Practitioner-roberts-benjamin.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**HealthcareService** (1)

- `generalmedical-mossy-point-medical-centre` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json`

**Organization** (1)

- `mossy-point-medical-centre` — `au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

**Location** (1)

- `mossy-point-medical-centre` — `au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 254xx-256xx</strong> (9 entities)</summary>


_Appin, Mogareeka, Stony Creek._


**PractitionerRole** (3)

- `endocrinologist-cruickshank-bryce` — `au-fhir-test-data-set/au-core/PractitionerRole-endocrinologist-cruickshank-bryce.json`
- `medicaloncologist-sheppard-mathew` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-sheppard-mathew.json`
- `retailpharmacist-peterson-megan` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-peterson-megan.json`

**Practitioner** (3)

- `cruickshank-bryce` — `au-fhir-test-data-set/au-core/Practitioner-cruickshank-bryce.json`
- `peterson-megan` — `au-fhir-test-data-set/au-core/Practitioner-peterson-megan.json`
- `sheppard-mathew` — `au-fhir-test-data-set/au-core/Practitioner-sheppard-mathew.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**HealthcareService** (1)

- `communitypharmacy-appin-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-appin-pharmacy.json`

**Organization** (1)

- `appin-pharmacy` — `au-fhir-test-data-set/au-core/Organization-appin-pharmacy.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

**Location** (1)

- `appin-pharmacy` — `au-fhir-test-data-set/au-core/Location-appin-pharmacy.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 257xx-259xx</strong> (11 entities)</summary>


_Tarlo, Wallendbeen._


**PractitionerRole** (4)

- `nursepractitioner-gartshore-indira` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-gartshore-indira.json`
- `ophthalmologist-jenkins-miranda` — `au-fhir-test-data-set/au-core/PractitionerRole-ophthalmologist-jenkins-miranda.json`
- `registerednurses-fraser-abbie` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-fraser-abbie.json`
- `registerednurses-taylor-kittie` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-taylor-kittie.json`

**Practitioner** (4)

- `fraser-abbie` — `au-fhir-test-data-set/au-core/Practitioner-fraser-abbie.json`
- `gartshore-indira` — `au-fhir-test-data-set/au-core/Practitioner-gartshore-indira.json`
- `jenkins-miranda` — `au-fhir-test-data-set/au-core/Practitioner-jenkins-miranda.json`
- `taylor-kittie` — `au-fhir-test-data-set/au-core/Practitioner-taylor-kittie.json`

**HealthcareService** (1)

- `privateprofit-wallendbeen-aged-care` — `au-fhir-test-data-set/au-core/HealthcareService-privateprofit-wallendbeen-aged-care.json`

**Organization** (1)

- `wallendbeen-aged-care` — `au-fhir-test-data-set/au-core/Organization-wallendbeen-aged-care.json`

**Location** (1)

- `wallendbeen-aged-care` — `au-fhir-test-data-set/au-core/Location-wallendbeen-aged-care.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 270xx-272xx</strong> (13 entities)</summary>


_Hatfield, Leeton, Minjary, Wermatong._


**Patient** (4)

- `banks-jamila-angie` — `au-fhir-test-data-set/au-core/Patient-banks-jamila-angie.json` — *also in: [families](#families) (free to build on)*
- `banks-jeramy-ezra` — `au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `banks-jonas-cary` — `au-fhir-test-data-set/au-core/Patient-banks-jonas-cary.json` — *also in: [families](#families) (free to build on)*
- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*

**PractitionerRole** (2)

- `midwife-browne-wilfred` — `au-fhir-test-data-set/au-core/PractitionerRole-midwife-browne-wilfred.json`
- `nuclearmedicine-thorn-tonya` — `au-fhir-test-data-set/au-core/PractitionerRole-nuclearmedicine-thorn-tonya.json`

**Practitioner** (2)

- `browne-wilfred` — `au-fhir-test-data-set/au-core/Practitioner-browne-wilfred.json`
- `thorn-tonya` — `au-fhir-test-data-set/au-core/Practitioner-thorn-tonya.json`

**Organization** (1)

- `leeton-health-network` — `au-fhir-test-data-set/au-core/Organization-leeton-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

**RelatedPerson** (4)

- `banks-jeramy-2` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-jeramy-2.json`
- `banks-jeramy-3` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-jeramy-3.json`
- `banks-jeramy-4` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-jeramy-4.json`
- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-mia-leanne.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 276xx-278xx</strong> (5 entities)</summary>


_Higher Macdonald._


**PractitionerRole** (1)

- `pathologist-clarke-malcolm` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-clarke-malcolm.json`

**Practitioner** (1)

- `clarke-malcolm` — `au-fhir-test-data-set/au-core/Practitioner-clarke-malcolm.json`

**HealthcareService** (1)

- `pathologylaboratory-higher-macdonald-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-higher-macdonald-pathology.json`

**Organization** (1)

- `higher-macdonald-pathology` — `au-fhir-test-data-set/au-core/Organization-higher-macdonald-pathology.json`

**Location** (1)

- `higher-macdonald-pathology` — `au-fhir-test-data-set/au-core/Location-higher-macdonald-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 280xx-282xx</strong> (5 entities)</summary>


_Pullabooka._


**PractitionerRole** (1)

- `pathologist-pratley-philomena` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-pratley-philomena.json`

**Practitioner** (1)

- `pratley-philomena` — `au-fhir-test-data-set/au-core/Practitioner-pratley-philomena.json`

**HealthcareService** (1)

- `pathologylaboratory-pullabooka-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-pullabooka-pathology.json`

**Organization** (1)

- `pullabooka-pathology` — `au-fhir-test-data-set/au-core/Organization-pullabooka-pathology.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

**Location** (1)

- `pullabooka-pathology` — `au-fhir-test-data-set/au-core/Location-pullabooka-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 282xx-284xx</strong> (7 entities)</summary>


_Balladoran, Dubbo._


**PractitionerRole** (2)

- `emergencymedicine-gilmour-damon` — `au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-gilmour-damon.json`
- `paediatrician-leishman-leesa` — `au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-leishman-leesa.json`

**Practitioner** (2)

- `gilmour-damon` — `au-fhir-test-data-set/au-core/Practitioner-gilmour-damon.json`
- `leishman-leesa` — `au-fhir-test-data-set/au-core/Practitioner-leishman-leesa.json`

**HealthcareService** (1)

- `emergencydepartment-dubbo-emergency` — `au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-dubbo-emergency.json`

**Organization** (1)

- `dubbo-emergency` — `au-fhir-test-data-set/au-core/Organization-dubbo-emergency.json`

**Location** (1)

- `dubbo-emergency` — `au-fhir-test-data-set/au-core/Location-dubbo-emergency.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Sydney metropolitan</strong> (119 entities)</summary>


_Berowra, Blacktown, Canley Heights, Cremorne, Frenchs Forest East, Kensington, Parramatta, Westmead._


**Patient** (6)

- `keaton-jayme` — `au-fhir-test-data-set/au-core/Patient-keaton-jayme.json`
- `lowe-alessandra` — `au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alix` — `au-fhir-test-data-set/au-core/Patient-lowe-alix.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-cedric` — `au-fhir-test-data-set/au-core/Patient-lowe-cedric.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-valerie` — `au-fhir-test-data-set/au-core/Patient-lowe-valerie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `wang-li` — `au-fhir-test-data-set/au-core/Patient-wang-li.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

**PractitionerRole** (38)

- `berridge-beulah` — `au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `breadmore-phillip` — `au-fhir-test-data-set/au-core/PractitionerRole-breadmore-phillip.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cox-sandra` — `au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `dawson-kent` — `au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `diagnostic-barrett-carey` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-barrett-carey.json`
- `duncan-xenia` — `au-fhir-test-data-set/au-core/PractitionerRole-duncan-xenia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ellison-abby` — `au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ewing-jude` — `au-fhir-test-data-set/au-core/PractitionerRole-ewing-jude.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fleming-kitty` — `au-fhir-test-data-set/au-core/PractitionerRole-fleming-kitty.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `frank-gaylene` — `au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fuller-christeen` — `au-fhir-test-data-set/au-core/PractitionerRole-fuller-christeen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `goodwin-rae` — `au-fhir-test-data-set/au-core/PractitionerRole-goodwin-rae.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hamilton-errol` — `au-fhir-test-data-set/au-core/PractitionerRole-hamilton-errol.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `healey-tamiko` — `au-fhir-test-data-set/au-core/PractitionerRole-healey-tamiko.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `howe-elden` — `au-fhir-test-data-set/au-core/PractitionerRole-howe-elden.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `knowles-sunshine` — `au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lapthorn-leisa` — `au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `little-jerrie` — `au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `macey-brant` — `au-fhir-test-data-set/au-core/PractitionerRole-macey-brant.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcbean-nicollette` — `au-fhir-test-data-set/au-core/PractitionerRole-mcbean-nicollette.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcintosh-angelica` — `au-fhir-test-data-set/au-core/PractitionerRole-mcintosh-angelica.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcnab-angelina` — `au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `medicalradiation-fowler-christy` — `au-fhir-test-data-set/au-core/PractitionerRole-medicalradiation-fowler-christy.json`
- `mills-hope` — `au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `nairn-vince` — `au-fhir-test-data-set/au-core/PractitionerRole-nairn-vince.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `neville-isaiah` — `au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `nursepractitioner-simons-reggie` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-simons-reggie.json`
- `nutley-bradley` — `au-fhir-test-data-set/au-core/PractitionerRole-nutley-bradley.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ohalloran-sheryl` — `au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `osmond-michele` — `au-fhir-test-data-set/au-core/PractitionerRole-osmond-michele.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `perkins-amee` — `au-fhir-test-data-set/au-core/PractitionerRole-perkins-amee.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `redman-mariah` — `au-fhir-test-data-set/au-core/PractitionerRole-redman-mariah.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `registerednurses-shephard-lizabeth` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shephard-lizabeth.json`
- `roche-garfield` — `au-fhir-test-data-set/au-core/PractitionerRole-roche-garfield.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `seaby-penelope` — `au-fhir-test-data-set/au-core/PractitionerRole-seaby-penelope.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `stephens-nellie` — `au-fhir-test-data-set/au-core/PractitionerRole-stephens-nellie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `surgeongeneral-mackenzie-cinda` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-mackenzie-cinda.json`
- `tate-melvin` — `au-fhir-test-data-set/au-core/PractitionerRole-tate-melvin.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Practitioner** (38)

- `barrett-carey` — `au-fhir-test-data-set/au-core/Practitioner-barrett-carey.json`
- `berridge-beulah` — `au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `breadmore-phillip` — `au-fhir-test-data-set/au-core/Practitioner-breadmore-phillip.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cox-sandra` — `au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `dawson-kent` — `au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `duncan-xenia` — `au-fhir-test-data-set/au-core/Practitioner-duncan-xenia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ellison-abby` — `au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ewing-jude` — `au-fhir-test-data-set/au-core/Practitioner-ewing-jude.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fleming-kitty` — `au-fhir-test-data-set/au-core/Practitioner-fleming-kitty.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fowler-christy` — `au-fhir-test-data-set/au-core/Practitioner-fowler-christy.json`
- `frank-gaylene` — `au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fuller-christeen` — `au-fhir-test-data-set/au-core/Practitioner-fuller-christeen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `goodwin-rae` — `au-fhir-test-data-set/au-core/Practitioner-goodwin-rae.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hamilton-errol` — `au-fhir-test-data-set/au-core/Practitioner-hamilton-errol.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `healey-tamiko` — `au-fhir-test-data-set/au-core/Practitioner-healey-tamiko.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `howe-elden` — `au-fhir-test-data-set/au-core/Practitioner-howe-elden.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `knowles-sunshine` — `au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lapthorn-leisa` — `au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `little-jerrie` — `au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `macey-brant` — `au-fhir-test-data-set/au-core/Practitioner-macey-brant.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mackenzie-cinda` — `au-fhir-test-data-set/au-core/Practitioner-mackenzie-cinda.json`
- `mcbean-nicollette` — `au-fhir-test-data-set/au-core/Practitioner-mcbean-nicollette.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcintosh-angelica` — `au-fhir-test-data-set/au-core/Practitioner-mcintosh-angelica.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcnab-angelina` — `au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `mills-hope` — `au-fhir-test-data-set/au-core/Practitioner-mills-hope.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `nairn-vince` — `au-fhir-test-data-set/au-core/Practitioner-nairn-vince.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `neville-isaiah` — `au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `nutley-bradley` — `au-fhir-test-data-set/au-core/Practitioner-nutley-bradley.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ohalloran-sheryl` — `au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `osmond-michele` — `au-fhir-test-data-set/au-core/Practitioner-osmond-michele.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `perkins-amee` — `au-fhir-test-data-set/au-core/Practitioner-perkins-amee.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `redman-mariah` — `au-fhir-test-data-set/au-core/Practitioner-redman-mariah.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `roche-garfield` — `au-fhir-test-data-set/au-core/Practitioner-roche-garfield.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `seaby-penelope` — `au-fhir-test-data-set/au-core/Practitioner-seaby-penelope.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `shephard-lizabeth` — `au-fhir-test-data-set/au-core/Practitioner-shephard-lizabeth.json`
- `simons-reggie` — `au-fhir-test-data-set/au-core/Practitioner-simons-reggie.json`
- `stephens-nellie` — `au-fhir-test-data-set/au-core/Practitioner-stephens-nellie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `tate-melvin` — `au-fhir-test-data-set/au-core/Practitioner-tate-melvin.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**HealthcareService** (2)

- `diagnosticimaging-frenchs-forest-east-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-frenchs-forest-east-radiology.json`
- `publicacute-kensington-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-kensington-public-hospital.json`

**Organization** (19)

- `cremorne-care-and-support` — `au-fhir-test-data-set/au-core/Organization-cremorne-care-and-support.json` — *also in: [community-contributions](#community-contributions) (free to build on)*
- `frenchs-forest-east-radiology` — `au-fhir-test-data-set/au-core/Organization-frenchs-forest-east-radiology.json`
- `kensington-public-hospital` — `au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `parramatta-community-health` — `au-fhir-test-data-set/au-core/Organization-parramatta-community-health.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parramatta-dental` — `au-fhir-test-data-set/au-core/Organization-parramatta-dental.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parramatta-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parramatta-midwifery` — `au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parramatta-nutrition` — `au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parramatta-public-hospital` — `au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `parramatta-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-optical` — `au-fhir-test-data-set/au-core/Organization-westmead-optical.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-ot-services` — `au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-pathology` — `au-fhir-test-data-set/au-core/Organization-westmead-pathology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-pharmacy` — `au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-public-hospital` — `au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-radiology` — `au-fhir-test-data-set/au-core/Organization-westmead-radiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `westmead-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Location** (2)

- `frenchs-forest-east-radiology` — `au-fhir-test-data-set/au-core/Location-frenchs-forest-east-radiology.json`
- `kensington-public-hospital` — `au-fhir-test-data-set/au-core/Location-kensington-public-hospital.json`

**RelatedPerson** (14)

- `lowe-alessandra-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alessandra-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alessandra-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-3.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alix-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alix-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alix-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-3.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-cedric-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-cedric-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-cedric-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-3.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-valerie-1` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-1.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-valerie-2` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-2.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-valerie-3` — `au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-3.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `rabbit-peter` — `au-fhir-test-data-set/au-core/RelatedPerson-rabbit-peter.json`
- `wang-li-friend` — `au-fhir-test-data-set/au-core/RelatedPerson-wang-li-friend.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

</details>
</blockquote>

</details>

<details><summary><strong>NT</strong> (1 grouping, 37 entities)</summary>

<blockquote>
<details><summary><strong>Darwin metropolitan</strong> (37 entities)</summary>


_Acacia Hills, Annie River, Bayview, Coconut Grove, Cullen Bay, East Point, Ludmilla, Mitchell, Nguiu, Pulumpa, Southport._


**Patient** (2)

- `archibald-dante` — `au-fhir-test-data-set/au-core/Patient-archibald-dante.json`
- `todd-tanya-estelle` — `au-fhir-test-data-set/au-core/Patient-todd-tanya-estelle.json`

**PractitionerRole** (10)

- `aboriginal-gillies-han` — `au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-gillies-han.json`
- `counsellorsnec-polglase-belen` — `au-fhir-test-data-set/au-core/PractitionerRole-counsellorsnec-polglase-belen.json`
- `generalpractitioner-faint-darryl` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-faint-darryl.json`
- `medicaldiagnostic-coulter-francine` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-coulter-francine.json`
- `osteopath-cook-natalie` — `au-fhir-test-data-set/au-core/PractitionerRole-osteopath-cook-natalie.json`
- `pathologist-gifford-cassidy` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-gifford-cassidy.json`
- `physiotherapist-darcy-alexandra` — `au-fhir-test-data-set/au-core/PractitionerRole-physiotherapist-darcy-alexandra.json`
- `registerednurses-craig-kenneth` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-craig-kenneth.json`
- `registerednurses-mccormack-annamaria` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-mccormack-annamaria.json`
- `retailpharmacist-harding-clyde` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-harding-clyde.json`

**Practitioner** (10)

- `cook-natalie` — `au-fhir-test-data-set/au-core/Practitioner-cook-natalie.json`
- `coulter-francine` — `au-fhir-test-data-set/au-core/Practitioner-coulter-francine.json`
- `craig-kenneth` — `au-fhir-test-data-set/au-core/Practitioner-craig-kenneth.json`
- `darcy-alexandra` — `au-fhir-test-data-set/au-core/Practitioner-darcy-alexandra.json`
- `faint-darryl` — `au-fhir-test-data-set/au-core/Practitioner-faint-darryl.json`
- `gifford-cassidy` — `au-fhir-test-data-set/au-core/Practitioner-gifford-cassidy.json`
- `gillies-han` — `au-fhir-test-data-set/au-core/Practitioner-gillies-han.json`
- `harding-clyde` — `au-fhir-test-data-set/au-core/Practitioner-harding-clyde.json`
- `mccormack-annamaria` — `au-fhir-test-data-set/au-core/Practitioner-mccormack-annamaria.json`
- `polglase-belen` — `au-fhir-test-data-set/au-core/Practitioner-polglase-belen.json`

**HealthcareService** (5)

- `communityhealth-annie-river-practice` — `au-fhir-test-data-set/au-core/HealthcareService-communityhealth-annie-river-practice.json`
- `generalpractice-cullen-bay-medical-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-generalpractice-cullen-bay-medical-clinic.json`
- `pathologylaboratory-bayview-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-bayview-pathology.json`
- `pharmacyretail-ludmilla-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-ludmilla-pharmacy.json`
- `specialistmedical-east-point-renal-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-east-point-renal-clinic.json`

**Organization** (5)

- `annie-river-practice` — `au-fhir-test-data-set/au-core/Organization-annie-river-practice.json`
- `bayview-pathology` — `au-fhir-test-data-set/au-core/Organization-bayview-pathology.json`
- `cullen-bay-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-cullen-bay-medical-clinic.json`
- `east-point-renal-clinic` — `au-fhir-test-data-set/au-core/Organization-east-point-renal-clinic.json`
- `ludmilla-pharmacy` — `au-fhir-test-data-set/au-core/Organization-ludmilla-pharmacy.json`

**Location** (5)

- `annie-river-practice` — `au-fhir-test-data-set/au-core/Location-annie-river-practice.json`
- `bayview-pathology` — `au-fhir-test-data-set/au-core/Location-bayview-pathology.json`
- `cullen-bay-medical-clinic` — `au-fhir-test-data-set/au-core/Location-cullen-bay-medical-clinic.json`
- `east-point-renal-clinic` — `au-fhir-test-data-set/au-core/Location-east-point-renal-clinic.json`
- `ludmilla-pharmacy` — `au-fhir-test-data-set/au-core/Location-ludmilla-pharmacy.json`

</details>
</blockquote>

</details>

<details><summary><strong>QLD</strong> (12 groupings, 131 entities)</summary>

<blockquote>
<details><summary><strong>Brisbane metropolitan</strong> (22 entities)</summary>


_Brisbane, Herston, Logan Reserve, Loganlea, Wilston._


**Patient** (3)

- `belger-remedios` — `au-fhir-test-data-set/au-erequesting/Patient-belger-remedios.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*
- `bennelong-anne` — `au-fhir-test-data-set/au-core/Patient-bennelong-anne.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*
- `odonnell-gillian` — `au-fhir-test-data-set/au-core/Patient-odonnell-gillian.json`

**PractitionerRole** (8)

- `bowden-hiroko` — `au-fhir-test-data-set/au-core/PractitionerRole-bowden-hiroko.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `greenhill-edmond` — `au-fhir-test-data-set/au-core/PractitionerRole-greenhill-edmond.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `irwin-corinna` — `au-fhir-test-data-set/au-core/PractitionerRole-irwin-corinna.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `jeffery-sammy` — `au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lyons-shay` — `au-fhir-test-data-set/au-core/PractitionerRole-lyons-shay.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mclean-brenda` — `au-fhir-test-data-set/au-core/PractitionerRole-mclean-brenda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sherry-dean` — `au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `speechpathologist-stapleton-carole` — `au-fhir-test-data-set/au-core/PractitionerRole-speechpathologist-stapleton-carole.json`

**Practitioner** (8)

- `bowden-hiroko` — `au-fhir-test-data-set/au-core/Practitioner-bowden-hiroko.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `greenhill-edmond` — `au-fhir-test-data-set/au-core/Practitioner-greenhill-edmond.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `irwin-corinna` — `au-fhir-test-data-set/au-core/Practitioner-irwin-corinna.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `jeffery-sammy` — `au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lyons-shay` — `au-fhir-test-data-set/au-core/Practitioner-lyons-shay.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mclean-brenda` — `au-fhir-test-data-set/au-core/Practitioner-mclean-brenda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sherry-dean` — `au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `stapleton-carole` — `au-fhir-test-data-set/au-core/Practitioner-stapleton-carole.json`

**Organization** (3)

- `herston-pathology` — `au-fhir-test-data-set/au-core/Organization-herston-pathology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `herston-public-hospital` — `au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `herston-radiology` — `au-fhir-test-data-set/au-core/Organization-herston-radiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 420xx-422xx</strong> (2 entities)</summary>


_Miami, Oxenford._


**Patient** (1)

- `lynch-alyce-shauna` — `au-fhir-test-data-set/au-core/Patient-lynch-alyce-shauna.json`

**Organization** (1)

- `oxenford-care-and-support` — `au-fhir-test-data-set/au-core/Organization-oxenford-care-and-support.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 427xx-429xx</strong> (15 entities)</summary>


_Barney View, Cedar Grove._


**PractitionerRole** (5)

- `cardiothoracicsurgeon-manning-meg` — `au-fhir-test-data-set/au-core/PractitionerRole-cardiothoracicsurgeon-manning-meg.json`
- `dietitian-kelly-virginia` — `au-fhir-test-data-set/au-core/PractitionerRole-dietitian-kelly-virginia.json`
- `nursepractitioner-haywood-byron` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-haywood-byron.json`
- `registerednurses-sinclair-forrest` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-sinclair-forrest.json`
- `surgeongeneral-armstrong-amada` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-armstrong-amada.json`

**Practitioner** (5)

- `armstrong-amada` — `au-fhir-test-data-set/au-core/Practitioner-armstrong-amada.json`
- `haywood-byron` — `au-fhir-test-data-set/au-core/Practitioner-haywood-byron.json`
- `kelly-virginia` — `au-fhir-test-data-set/au-core/Practitioner-kelly-virginia.json`
- `manning-meg` — `au-fhir-test-data-set/au-core/Practitioner-manning-meg.json`
- `sinclair-forrest` — `au-fhir-test-data-set/au-core/Practitioner-sinclair-forrest.json`

**HealthcareService** (1)

- `privateacute-barney-view-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-barney-view-private-hospital.json`

**Organization** (1)

- `barney-view-private-hospital` — `au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**Location** (3)

- `au-hospital-pharm-out` — `au-fhir-test-data-set/au-core/Location-au-hospital-pharm-out.json`
- `barney-view-private-hospital` — `au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*
- `renal-dialysis-unit` — `au-fhir-test-data-set/au-core/Location-renal-dialysis-unit.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 430xx-432xx</strong> (5 entities)</summary>


_Tarampa._


**PractitionerRole** (1)

- `emergencymedicine-mitchell-frankie` — `au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-mitchell-frankie.json`

**Practitioner** (1)

- `mitchell-frankie` — `au-fhir-test-data-set/au-core/Practitioner-mitchell-frankie.json`

**HealthcareService** (1)

- `emergencydepartment-tarampa-emergency` — `au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-tarampa-emergency.json`

**Organization** (1)

- `tarampa-emergency` — `au-fhir-test-data-set/au-core/Organization-tarampa-emergency.json`

**Location** (1)

- `tarampa-emergency` — `au-fhir-test-data-set/au-core/Location-tarampa-emergency.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 435xx-437xx</strong> (30 entities)</summary>


_Berat, Carrington, Glennie Heights, Loch Lomond, Morgan Park, Purrawunda, Westbrook._


**Patient** (2)

- `hayes-arianne` — `au-fhir-test-data-set/au-core/Patient-hayes-arianne.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `roberts-fred` — `au-fhir-test-data-set/au-erequesting/Patient-roberts-fred.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**PractitionerRole** (8)

- `diagnostic-berry-millicent` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-berry-millicent.json`
- `generalpractitioner-samuels-wyatt` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-samuels-wyatt.json`
- `nursepractitioner-springett-angelo` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-springett-angelo.json`
- `pathologist-shearer-joesfine` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-shearer-joesfine.json`
- `psychiatrist-macnab-gregory` — `au-fhir-test-data-set/au-core/PractitionerRole-psychiatrist-macnab-gregory.json`
- `registerednurses-morton-eric` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-morton-eric.json`
- `registerednurses-rowland-roger` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-rowland-roger.json`
- `surgeongeneral-marchant-ricki` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-marchant-ricki.json`

**Practitioner** (8)

- `berry-millicent` — `au-fhir-test-data-set/au-core/Practitioner-berry-millicent.json`
- `macnab-gregory` — `au-fhir-test-data-set/au-core/Practitioner-macnab-gregory.json`
- `marchant-ricki` — `au-fhir-test-data-set/au-core/Practitioner-marchant-ricki.json`
- `morton-eric` — `au-fhir-test-data-set/au-core/Practitioner-morton-eric.json`
- `rowland-roger` — `au-fhir-test-data-set/au-core/Practitioner-rowland-roger.json`
- `samuels-wyatt` — `au-fhir-test-data-set/au-core/Practitioner-samuels-wyatt.json`
- `shearer-joesfine` — `au-fhir-test-data-set/au-core/Practitioner-shearer-joesfine.json`
- `springett-angelo` — `au-fhir-test-data-set/au-core/Practitioner-springett-angelo.json`

**HealthcareService** (4)

- `diagnosticimaging-berat-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-berat-radiology.json`
- `generalpractice-loch-lomond-medical-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-generalpractice-loch-lomond-medical-clinic.json`
- `pathologylaboratory-carrington-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-carrington-pathology.json`
- `publicacute-glennie-heights-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-glennie-heights-public-hospital.json`

**Organization** (4)

- `berat-radiology` — `au-fhir-test-data-set/au-core/Organization-berat-radiology.json`
- `carrington-pathology` — `au-fhir-test-data-set/au-core/Organization-carrington-pathology.json`
- `glennie-heights-public-hospital` — `au-fhir-test-data-set/au-core/Organization-glennie-heights-public-hospital.json`
- `loch-lomond-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-loch-lomond-medical-clinic.json`

**Location** (4)

- `berat-radiology` — `au-fhir-test-data-set/au-core/Location-berat-radiology.json`
- `carrington-pathology` — `au-fhir-test-data-set/au-core/Location-carrington-pathology.json`
- `glennie-heights-public-hospital` — `au-fhir-test-data-set/au-core/Location-glennie-heights-public-hospital.json`
- `loch-lomond-medical-clinic` — `au-fhir-test-data-set/au-core/Location-loch-lomond-medical-clinic.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 438xx-439xx</strong> (3 entities)</summary>


_Goondiwindi, Lundavra._


**PractitionerRole** (1)

- `chiropractor-gore-jess` — `au-fhir-test-data-set/au-core/PractitionerRole-chiropractor-gore-jess.json`

**Practitioner** (1)

- `gore-jess` — `au-fhir-test-data-set/au-core/Practitioner-gore-jess.json`

**Organization** (1)

- `goondiwindi-health-network` — `au-fhir-test-data-set/au-core/Organization-goondiwindi-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 448xx-449xx</strong> (5 entities)</summary>


_Kioma._


**PractitionerRole** (1)

- `pathologist-herbert-aimee` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-herbert-aimee.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**Practitioner** (1)

- `herbert-aimee` — `au-fhir-test-data-set/au-core/Practitioner-herbert-aimee.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**HealthcareService** (1)

- `pathologylaboratory-kioma-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kioma-pathology.json`

**Organization** (1)

- `kioma-pathology` — `au-fhir-test-data-set/au-core/Organization-kioma-pathology.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**Location** (1)

- `kioma-pathology` — `au-fhir-test-data-set/au-core/Location-kioma-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 450xx-452xx</strong> (8 entities)</summary>


_Draper, Elimbah._


**Patient** (1)

- `boulton-annika` — `au-fhir-test-data-set/au-core/Patient-boulton-annika.json`

**PractitionerRole** (2)

- `generalpractitioner-guthridge-jarred` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*
- `registerednurses-egan-shae` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-egan-shae.json`

**Practitioner** (2)

- `egan-shae` — `au-fhir-test-data-set/au-core/Practitioner-egan-shae.json`
- `guthridge-jarred` — `au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**HealthcareService** (1)

- `generalmedical-elimbah-medical-centre` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-elimbah-medical-centre.json`

**Organization** (1)

- `elimbah-medical-centre` — `au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**Location** (1)

- `elimbah-medical-centre` — `au-fhir-test-data-set/au-core/Location-elimbah-medical-centre.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 464xx-466xx</strong> (3 entities)</summary>


_Tindal RAAF, Walliebum._


**Patient** (1)

- `martin-shawn` — `au-fhir-test-data-set/au-core/Patient-martin-shawn.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*

**Organization** (1)

- `bobrester-medical-center` — `au-fhir-test-data-set/au-core/Organization-bobrester-medical-center.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

**Location** (1)

- `bobrester-medical-center` — `au-fhir-test-data-set/au-core/Location-bobrester-medical-center.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 470xx-471xx</strong> (7 entities)</summary>


_Banana, Cracow._


**PractitionerRole** (2)

- `plastic-crowley-pablo` — `au-fhir-test-data-set/au-core/PractitionerRole-plastic-crowley-pablo.json`
- `retailpharmacist-patrick-manual` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-patrick-manual.json`

**Practitioner** (2)

- `crowley-pablo` — `au-fhir-test-data-set/au-core/Practitioner-crowley-pablo.json`
- `patrick-manual` — `au-fhir-test-data-set/au-core/Practitioner-patrick-manual.json`

**HealthcareService** (1)

- `communitypharmacy-cracow-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-cracow-pharmacy.json`

**Organization** (1)

- `cracow-pharmacy` — `au-fhir-test-data-set/au-core/Organization-cracow-pharmacy.json`

**Location** (1)

- `cracow-pharmacy` — `au-fhir-test-data-set/au-core/Location-cracow-pharmacy.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 473xx-475xx</strong> (10 entities)</summary>


_East Mackay, Mount Charlton._


**PractitionerRole** (2)

- `diagnostic-mclaughlin-kimberlee` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mclaughlin-kimberlee.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*
- `retailpharmacist-ford-dean` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-ford-dean.json`

**Practitioner** (2)

- `ford-dean` — `au-fhir-test-data-set/au-core/Practitioner-ford-dean.json`
- `mclaughlin-kimberlee` — `au-fhir-test-data-set/au-core/Practitioner-mclaughlin-kimberlee.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**HealthcareService** (2)

- `diagnosticimaging-mount-charlton-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mount-charlton-radiology.json`
- `pharmacyretail-east-mackay-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-east-mackay-pharmacy.json`

**Organization** (2)

- `east-mackay-pharmacy` — `au-fhir-test-data-set/au-core/Organization-east-mackay-pharmacy.json`
- `mount-charlton-radiology` — `au-fhir-test-data-set/au-core/Organization-mount-charlton-radiology.json` — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples) (reserved)*

**Location** (2)

- `east-mackay-pharmacy` — `au-fhir-test-data-set/au-core/Location-east-mackay-pharmacy.json`
- `mount-charlton-radiology` — `au-fhir-test-data-set/au-core/Location-mount-charlton-radiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 485xx-487xx</strong> (21 entities)</summary>


_Bayview Heights, Hudson, Southedge._


**PractitionerRole** (6)

- `aboriginal-coulter-oliver` — `au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-coulter-oliver.json`
- `medicaloncologist-leeds-luigi` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-leeds-luigi.json`
- `nursepractitioner-mcleod-clinton` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-mcleod-clinton.json`
- `registerednurses-berry-shay` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-berry-shay.json`
- `registerednurses-lamerton-buck` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-lamerton-buck.json`
- `registerednurses-mclean-lizzette` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-mclean-lizzette.json`

**Practitioner** (6)

- `berry-shay` — `au-fhir-test-data-set/au-core/Practitioner-berry-shay.json`
- `coulter-oliver` — `au-fhir-test-data-set/au-core/Practitioner-coulter-oliver.json`
- `lamerton-buck` — `au-fhir-test-data-set/au-core/Practitioner-lamerton-buck.json`
- `leeds-luigi` — `au-fhir-test-data-set/au-core/Practitioner-leeds-luigi.json`
- `mclean-lizzette` — `au-fhir-test-data-set/au-core/Practitioner-mclean-lizzette.json`
- `mcleod-clinton` — `au-fhir-test-data-set/au-core/Practitioner-mcleod-clinton.json`

**HealthcareService** (3)

- `communityhealth-southedge-practice` — `au-fhir-test-data-set/au-core/HealthcareService-communityhealth-southedge-practice.json`
- `privateprofit-hudson-aged-care` — `au-fhir-test-data-set/au-core/HealthcareService-privateprofit-hudson-aged-care.json`
- `specialistmedical-bayview-heights-oncology-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-bayview-heights-oncology-clinic.json`

**Organization** (3)

- `bayview-heights-oncology-clinic` — `au-fhir-test-data-set/au-core/Organization-bayview-heights-oncology-clinic.json`
- `hudson-aged-care` — `au-fhir-test-data-set/au-core/Organization-hudson-aged-care.json`
- `southedge-practice` — `au-fhir-test-data-set/au-core/Organization-southedge-practice.json`

**Location** (3)

- `bayview-heights-oncology-clinic` — `au-fhir-test-data-set/au-core/Location-bayview-heights-oncology-clinic.json`
- `hudson-aged-care` — `au-fhir-test-data-set/au-core/Location-hudson-aged-care.json`
- `southedge-practice` — `au-fhir-test-data-set/au-core/Location-southedge-practice.json`

</details>
</blockquote>

</details>

<details><summary><strong>SA</strong> (6 groupings, 118 entities)</summary>

<blockquote>
<details><summary><strong>Adelaide metropolitan</strong> (74 entities)</summary>


_Adelaide, Croydon, Edwardstown, Hawthorn, Park Holme, Royal park, Salisbury South Dc, Semaphore, South Brighton, Wingfield, Woodcroft, Woodville._


**Patient** (1)

- `reece-karen` — `au-fhir-test-data-set/au-core/Patient-reece-karen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**PractitionerRole** (26)

- `baker-troy` — `au-fhir-test-data-set/au-core/PractitionerRole-baker-troy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `baynton-lolita` — `au-fhir-test-data-set/au-core/PractitionerRole-baynton-lolita.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bell-rudolf` — `au-fhir-test-data-set/au-core/PractitionerRole-bell-rudolf.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `berry-lisa` — `au-fhir-test-data-set/au-core/PractitionerRole-berry-lisa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cardiothoracicsurgeon-mackee-sara` — `au-fhir-test-data-set/au-core/PractitionerRole-cardiothoracicsurgeon-mackee-sara.json`
- `carey-joyce` — `au-fhir-test-data-set/au-core/PractitionerRole-carey-joyce.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `couch-joel` — `au-fhir-test-data-set/au-core/PractitionerRole-couch-joel.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cruickshank-marlyn` — `au-fhir-test-data-set/au-core/PractitionerRole-cruickshank-marlyn.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `dietitian-henderson-nelson` — `au-fhir-test-data-set/au-core/PractitionerRole-dietitian-henderson-nelson.json`
- `fleming-skye` — `au-fhir-test-data-set/au-core/PractitionerRole-fleming-skye.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `freeman-anya` — `au-fhir-test-data-set/au-core/PractitionerRole-freeman-anya.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `harley-reynalda` — `au-fhir-test-data-set/au-core/PractitionerRole-harley-reynalda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hoskins-earl` — `au-fhir-test-data-set/au-core/PractitionerRole-hoskins-earl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `huddlestone-velda` — `au-fhir-test-data-set/au-core/PractitionerRole-huddlestone-velda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hutton-cortez` — `au-fhir-test-data-set/au-core/PractitionerRole-hutton-cortez.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lawrence-drew` — `au-fhir-test-data-set/au-core/PractitionerRole-lawrence-drew.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `manning-opal` — `au-fhir-test-data-set/au-core/PractitionerRole-manning-opal.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `medicaldiagnostic-lavender-astrid` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-lavender-astrid.json`
- `nuclearmedicine-hyde-cortez` — `au-fhir-test-data-set/au-core/PractitionerRole-nuclearmedicine-hyde-cortez.json`
- `paediatrician-ellison-shawn` — `au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-ellison-shawn.json`
- `pathologist-dixon-astrid` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-dixon-astrid.json`
- `pathologist-hickson-eldora` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hickson-eldora.json`
- `retailpharmacist-newling-louis` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-newling-louis.json`
- `rowlands-donya` — `au-fhir-test-data-set/au-core/PractitionerRole-rowlands-donya.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `tierney-gisela` — `au-fhir-test-data-set/au-core/PractitionerRole-tierney-gisela.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `vaughan-sol` — `au-fhir-test-data-set/au-core/PractitionerRole-vaughan-sol.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Practitioner** (26)

- `baker-troy` — `au-fhir-test-data-set/au-core/Practitioner-baker-troy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `baynton-lolita` — `au-fhir-test-data-set/au-core/Practitioner-baynton-lolita.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bell-rudolf` — `au-fhir-test-data-set/au-core/Practitioner-bell-rudolf.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `berry-lisa` — `au-fhir-test-data-set/au-core/Practitioner-berry-lisa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `carey-joyce` — `au-fhir-test-data-set/au-core/Practitioner-carey-joyce.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `couch-joel` — `au-fhir-test-data-set/au-core/Practitioner-couch-joel.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cruickshank-marlyn` — `au-fhir-test-data-set/au-core/Practitioner-cruickshank-marlyn.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `dixon-astrid` — `au-fhir-test-data-set/au-core/Practitioner-dixon-astrid.json`
- `ellison-shawn` — `au-fhir-test-data-set/au-core/Practitioner-ellison-shawn.json`
- `fleming-skye` — `au-fhir-test-data-set/au-core/Practitioner-fleming-skye.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `freeman-anya` — `au-fhir-test-data-set/au-core/Practitioner-freeman-anya.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `harley-reynalda` — `au-fhir-test-data-set/au-core/Practitioner-harley-reynalda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `henderson-nelson` — `au-fhir-test-data-set/au-core/Practitioner-henderson-nelson.json`
- `hickson-eldora` — `au-fhir-test-data-set/au-core/Practitioner-hickson-eldora.json`
- `hoskins-earl` — `au-fhir-test-data-set/au-core/Practitioner-hoskins-earl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `huddlestone-velda` — `au-fhir-test-data-set/au-core/Practitioner-huddlestone-velda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hutton-cortez` — `au-fhir-test-data-set/au-core/Practitioner-hutton-cortez.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hyde-cortez` — `au-fhir-test-data-set/au-core/Practitioner-hyde-cortez.json`
- `lavender-astrid` — `au-fhir-test-data-set/au-core/Practitioner-lavender-astrid.json`
- `lawrence-drew` — `au-fhir-test-data-set/au-core/Practitioner-lawrence-drew.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mackee-sara` — `au-fhir-test-data-set/au-core/Practitioner-mackee-sara.json`
- `manning-opal` — `au-fhir-test-data-set/au-core/Practitioner-manning-opal.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `newling-louis` — `au-fhir-test-data-set/au-core/Practitioner-newling-louis.json`
- `rowlands-donya` — `au-fhir-test-data-set/au-core/Practitioner-rowlands-donya.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `tierney-gisela` — `au-fhir-test-data-set/au-core/Practitioner-tierney-gisela.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `vaughan-sol` — `au-fhir-test-data-set/au-core/Practitioner-vaughan-sol.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**HealthcareService** (3)

- `pathologylaboratory-wingfield-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-wingfield-pathology.json`
- `pathologylaboratory-woodcroft-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-woodcroft-pathology.json`
- `pharmacyretail-edwardstown-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-edwardstown-pharmacy.json`

**Organization** (15)

- `adelaide-public-hospital` — `au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `edwardstown-pharmacy` — `au-fhir-test-data-set/au-core/Organization-edwardstown-pharmacy.json`
- `royal-park-medical-centre` — `au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `semaphore-aged-care` — `au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `wingfield-pathology` — `au-fhir-test-data-set/au-core/Organization-wingfield-pathology.json`
- `woodcroft-pathology` — `au-fhir-test-data-set/au-core/Organization-woodcroft-pathology.json`
- `woodville-cardiology` — `au-fhir-test-data-set/au-core/Organization-woodville-cardiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-dental` — `au-fhir-test-data-set/au-core/Organization-woodville-dental.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-dietitian-service` — `au-fhir-test-data-set/au-core/Organization-woodville-dietitian-service.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-woodville-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-ot-services` — `au-fhir-test-data-set/au-core/Organization-woodville-ot-services.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-pathology` — `au-fhir-test-data-set/au-core/Organization-woodville-pathology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-pharmacy` — `au-fhir-test-data-set/au-core/Organization-woodville-pharmacy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-podiatry` — `au-fhir-test-data-set/au-core/Organization-woodville-podiatry.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `woodville-radiology` — `au-fhir-test-data-set/au-core/Organization-woodville-radiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Location** (3)

- `edwardstown-pharmacy` — `au-fhir-test-data-set/au-core/Location-edwardstown-pharmacy.json`
- `wingfield-pathology` — `au-fhir-test-data-set/au-core/Location-wingfield-pathology.json`
- `woodcroft-pathology` — `au-fhir-test-data-set/au-core/Location-woodcroft-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 520xx-521xx</strong> (8 entities)</summary>


_Back Valley, Deep Creek, Hayborough._


**PractitionerRole** (2)

- `diagnostic-heaney-brock` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-heaney-brock.json`
- `obstetrician-rogers-lorilee` — `au-fhir-test-data-set/au-core/PractitionerRole-obstetrician-rogers-lorilee.json`

**Practitioner** (2)

- `heaney-brock` — `au-fhir-test-data-set/au-core/Practitioner-heaney-brock.json`
- `rogers-lorilee` — `au-fhir-test-data-set/au-core/Practitioner-rogers-lorilee.json`

**HealthcareService** (1)

- `diagnosticimaging-back-valley-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-back-valley-radiology.json`

**Organization** (2)

- `back-valley-radiology` — `au-fhir-test-data-set/au-core/Organization-back-valley-radiology.json`
- `hayborough-care-and-support` — `au-fhir-test-data-set/au-core/Organization-hayborough-care-and-support.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

**Location** (1)

- `back-valley-radiology` — `au-fhir-test-data-set/au-core/Location-back-valley-radiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 526xx-528xx</strong> (5 entities)</summary>


_Cape Jaffa._


**PractitionerRole** (1)

- `diagnostic-parr-adelaide` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-parr-adelaide.json`

**Practitioner** (1)

- `parr-adelaide` — `au-fhir-test-data-set/au-core/Practitioner-parr-adelaide.json`

**HealthcareService** (1)

- `diagnosticimaging-cape-jaffa-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-cape-jaffa-radiology.json`

**Organization** (1)

- `cape-jaffa-radiology` — `au-fhir-test-data-set/au-core/Organization-cape-jaffa-radiology.json`

**Location** (1)

- `cape-jaffa-radiology` — `au-fhir-test-data-set/au-core/Location-cape-jaffa-radiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 544xx-546xx</strong> (20 entities)</summary>


_Leasingham, Stockyard Creek, Yunta._


**PractitionerRole** (7)

- `nursepractitioner-doyle-hana` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-doyle-hana.json`
- `nursepractitioner-rowland-josh` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-rowland-josh.json`
- `plastic-pye-dusty` — `au-fhir-test-data-set/au-core/PractitionerRole-plastic-pye-dusty.json`
- `registerednurses-frankel-mary` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-frankel-mary.json`
- `registerednurses-steele-clyde` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-steele-clyde.json`
- `surgeongeneral-patrick-nancy` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-patrick-nancy.json`
- `surgeongeneral-pratley-maynard` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-pratley-maynard.json`

**Practitioner** (7)

- `doyle-hana` — `au-fhir-test-data-set/au-core/Practitioner-doyle-hana.json`
- `frankel-mary` — `au-fhir-test-data-set/au-core/Practitioner-frankel-mary.json`
- `patrick-nancy` — `au-fhir-test-data-set/au-core/Practitioner-patrick-nancy.json`
- `pratley-maynard` — `au-fhir-test-data-set/au-core/Practitioner-pratley-maynard.json`
- `pye-dusty` — `au-fhir-test-data-set/au-core/Practitioner-pye-dusty.json`
- `rowland-josh` — `au-fhir-test-data-set/au-core/Practitioner-rowland-josh.json`
- `steele-clyde` — `au-fhir-test-data-set/au-core/Practitioner-steele-clyde.json`

**HealthcareService** (2)

- `privateacute-yunta-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-yunta-private-hospital.json`
- `publicacute-leasingham-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-leasingham-public-hospital.json`

**Organization** (2)

- `leasingham-public-hospital` — `au-fhir-test-data-set/au-core/Organization-leasingham-public-hospital.json`
- `yunta-private-hospital` — `au-fhir-test-data-set/au-core/Organization-yunta-private-hospital.json`

**Location** (2)

- `leasingham-public-hospital` — `au-fhir-test-data-set/au-core/Location-leasingham-public-hospital.json`
- `yunta-private-hospital` — `au-fhir-test-data-set/au-core/Location-yunta-private-hospital.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 560xx-561xx</strong> (4 entities)</summary>


_Karkoo, Mitchellville._


**Patient** (1)

- `britton-brian-edwin` — `au-fhir-test-data-set/au-core/Patient-britton-brian-edwin.json`

**HealthcareService** (1)

- `chiropractic-karkoo-chiropractic` — `au-fhir-test-data-set/au-core/HealthcareService-chiropractic-karkoo-chiropractic.json`

**Organization** (1)

- `karkoo-chiropractic` — `au-fhir-test-data-set/au-core/Organization-karkoo-chiropractic.json`

**Location** (1)

- `karkoo-chiropractic` — `au-fhir-test-data-set/au-core/Location-karkoo-chiropractic.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 572xx-574xx</strong> (7 entities)</summary>


_Beltana._


**PractitionerRole** (2)

- `generalpractitioner-packham-delores` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-packham-delores.json`
- `registerednurses-pickford-lisa` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-pickford-lisa.json`

**Practitioner** (2)

- `packham-delores` — `au-fhir-test-data-set/au-core/Practitioner-packham-delores.json`
- `pickford-lisa` — `au-fhir-test-data-set/au-core/Practitioner-pickford-lisa.json`

**HealthcareService** (1)

- `generalmedical-beltana-medical-practice` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-beltana-medical-practice.json`

**Organization** (1)

- `beltana-medical-practice` — `au-fhir-test-data-set/au-core/Organization-beltana-medical-practice.json`

**Location** (1)

- `beltana-medical-practice` — `au-fhir-test-data-set/au-core/Location-beltana-medical-practice.json`

</details>
</blockquote>

</details>

<details><summary><strong>TAS</strong> (4 groupings, 56 entities)</summary>

<blockquote>
<details><summary><strong>Hobart metropolitan</strong> (15 entities)</summary>


_Derwent Park, Moonah, Opossum Bay, Rosetta._


**Patient** (2)

- `cummings-angelo` — `au-fhir-test-data-set/au-core/Patient-cummings-angelo.json`
- `potts-felix-ernie` — `au-fhir-test-data-set/au-core/Patient-potts-felix-ernie.json`

**PractitionerRole** (5)

- `diagnostic-beale-collette` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-beale-collette.json`
- `nursepractitioner-mortenson-kerry` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-mortenson-kerry.json`
- `paediatrician-rawlings-hong` — `au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-rawlings-hong.json`
- `registerednurses-harvey-brooke` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-harvey-brooke.json`
- `surgeongeneral-burrows-tegan` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-burrows-tegan.json`

**Practitioner** (5)

- `beale-collette` — `au-fhir-test-data-set/au-core/Practitioner-beale-collette.json`
- `burrows-tegan` — `au-fhir-test-data-set/au-core/Practitioner-burrows-tegan.json`
- `harvey-brooke` — `au-fhir-test-data-set/au-core/Practitioner-harvey-brooke.json`
- `mortenson-kerry` — `au-fhir-test-data-set/au-core/Practitioner-mortenson-kerry.json`
- `rawlings-hong` — `au-fhir-test-data-set/au-core/Practitioner-rawlings-hong.json`

**HealthcareService** (1)

- `publicacute-rosetta-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-rosetta-public-hospital.json`

**Organization** (1)

- `rosetta-public-hospital` — `au-fhir-test-data-set/au-core/Organization-rosetta-public-hospital.json`

**Location** (1)

- `rosetta-public-hospital` — `au-fhir-test-data-set/au-core/Location-rosetta-public-hospital.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 710xx-711xx</strong> (14 entities)</summary>


_Garden Island Creek, Southport, Verona Sands._


**PractitionerRole** (4)

- `ambulanceofficer-fletcher-dani` — `au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-fletcher-dani.json`
- `generalpractitioner-moran-vincent` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-moran-vincent.json`
- `pathologist-emmett-wilhelmina` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-emmett-wilhelmina.json`
- `registerednurses-ellison-malinda` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-ellison-malinda.json`

**Practitioner** (4)

- `ellison-malinda` — `au-fhir-test-data-set/au-core/Practitioner-ellison-malinda.json`
- `emmett-wilhelmina` — `au-fhir-test-data-set/au-core/Practitioner-emmett-wilhelmina.json`
- `fletcher-dani` — `au-fhir-test-data-set/au-core/Practitioner-fletcher-dani.json`
- `moran-vincent` — `au-fhir-test-data-set/au-core/Practitioner-moran-vincent.json`

**HealthcareService** (2)

- `generalmedical-southport-medical-practice` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-southport-medical-practice.json`
- `pathologylaboratory-verona-sands-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-verona-sands-pathology.json`

**Organization** (2)

- `southport-medical-practice` — `au-fhir-test-data-set/au-core/Organization-southport-medical-practice.json`
- `verona-sands-pathology` — `au-fhir-test-data-set/au-core/Organization-verona-sands-pathology.json`

**Location** (2)

- `southport-medical-practice` — `au-fhir-test-data-set/au-core/Location-southport-medical-practice.json`
- `verona-sands-pathology` — `au-fhir-test-data-set/au-core/Location-verona-sands-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 716xx-718xx</strong> (5 entities)</summary>


_Lewisham, Saltwater River, Sorell._


**PractitionerRole** (2)

- `cardiologist-felmingham-emma` — `au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-felmingham-emma.json`
- `medicalradiation-coulter-lani` — `au-fhir-test-data-set/au-core/PractitionerRole-medicalradiation-coulter-lani.json`

**Practitioner** (2)

- `coulter-lani` — `au-fhir-test-data-set/au-core/Practitioner-coulter-lani.json`
- `felmingham-emma` — `au-fhir-test-data-set/au-core/Practitioner-felmingham-emma.json`

**Organization** (1)

- `sorell-health-network` — `au-fhir-test-data-set/au-core/Organization-sorell-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 725xx-727xx</strong> (22 entities)</summary>


_Blumont, Launceston, Norwood, Robigana, Rushy Lagoon._


**Patient** (1)

- `robson-adam` — `au-fhir-test-data-set/au-core/Patient-robson-adam.json`

**PractitionerRole** (6)

- `diagnostic-houston-katrina` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-houston-katrina.json`
- `medicaldiagnostic-goldsmith-melody` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-goldsmith-melody.json`
- `nursepractitioner-patten-annie` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-patten-annie.json`
- `registerednurses-marchant-ivy` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-marchant-ivy.json`
- `retailpharmacist-jolley-beulah` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-jolley-beulah.json`
- `surgeongeneral-mcguire-jesse` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-mcguire-jesse.json`

**Practitioner** (6)

- `goldsmith-melody` — `au-fhir-test-data-set/au-core/Practitioner-goldsmith-melody.json`
- `houston-katrina` — `au-fhir-test-data-set/au-core/Practitioner-houston-katrina.json`
- `jolley-beulah` — `au-fhir-test-data-set/au-core/Practitioner-jolley-beulah.json`
- `marchant-ivy` — `au-fhir-test-data-set/au-core/Practitioner-marchant-ivy.json`
- `mcguire-jesse` — `au-fhir-test-data-set/au-core/Practitioner-mcguire-jesse.json`
- `patten-annie` — `au-fhir-test-data-set/au-core/Practitioner-patten-annie.json`

**HealthcareService** (3)

- `diagnosticimaging-blumont-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-blumont-radiology.json`
- `pharmacyretail-launceston-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-launceston-pharmacy.json`
- `privateacute-robigana-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-robigana-private-hospital.json`

**Organization** (3)

- `blumont-radiology` — `au-fhir-test-data-set/au-core/Organization-blumont-radiology.json`
- `launceston-pharmacy` — `au-fhir-test-data-set/au-core/Organization-launceston-pharmacy.json`
- `robigana-private-hospital` — `au-fhir-test-data-set/au-core/Organization-robigana-private-hospital.json`

**Location** (3)

- `blumont-radiology` — `au-fhir-test-data-set/au-core/Location-blumont-radiology.json`
- `launceston-pharmacy` — `au-fhir-test-data-set/au-core/Location-launceston-pharmacy.json`
- `robigana-private-hospital` — `au-fhir-test-data-set/au-core/Location-robigana-private-hospital.json`

</details>
</blockquote>

</details>

<details><summary><strong>VIC</strong> (11 groupings, 198 entities)</summary>

<blockquote>
<details><summary><strong>Melbourne metropolitan</strong> (102 entities)</summary>


_Blackburn South, Eltham North, Launching Place, Melbourne, Ringwood East, Southbank, St Kilda, Sunshine, Tarneit._


**Patient** (3)

- `ewing-ferdinand` — `au-fhir-test-data-set/au-core/Patient-ewing-ferdinand.json`
- `foreman-caterina` — `au-fhir-test-data-set/au-core/Patient-foreman-caterina.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `vaughan-seymour` — `au-fhir-test-data-set/au-core/Patient-vaughan-seymour.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**PractitionerRole** (36)

- `alcock-devon` — `au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `blackwood-ella` — `au-fhir-test-data-set/au-core/PractitionerRole-blackwood-ella.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bond-edmundo` — `au-fhir-test-data-set/au-core/PractitionerRole-bond-edmundo.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bowyer-norbert` — `au-fhir-test-data-set/au-core/PractitionerRole-bowyer-norbert.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `dempsey-carli` — `au-fhir-test-data-set/au-core/PractitionerRole-dempsey-carli.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `dentalpractitioner-quinn-aisha` — `au-fhir-test-data-set/au-core/PractitionerRole-dentalpractitioner-quinn-aisha.json`
- `egan-anja` — `au-fhir-test-data-set/au-core/PractitionerRole-egan-anja.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `findley-betty` — `au-fhir-test-data-set/au-core/PractitionerRole-findley-betty.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `frankel-caroline` — `au-fhir-test-data-set/au-core/PractitionerRole-frankel-caroline.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fuller-kendrick` — `au-fhir-test-data-set/au-core/PractitionerRole-fuller-kendrick.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `greene-delores` — `au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hallan-maggie` — `au-fhir-test-data-set/au-core/PractitionerRole-hallan-maggie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hamel-opal` — `au-fhir-test-data-set/au-core/PractitionerRole-hamel-opal.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hatcher-merrill` — `au-fhir-test-data-set/au-core/PractitionerRole-hatcher-merrill.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `higgs-allegra` — `au-fhir-test-data-set/au-core/PractitionerRole-higgs-allegra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hilton-della` — `au-fhir-test-data-set/au-core/PractitionerRole-hilton-della.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `joyce-mae` — `au-fhir-test-data-set/au-core/PractitionerRole-joyce-mae.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `keith-margot` — `au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `kelly-arlene` — `au-fhir-test-data-set/au-core/PractitionerRole-kelly-arlene.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `keyes-chau` — `au-fhir-test-data-set/au-core/PractitionerRole-keyes-chau.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `laing-malinda` — `au-fhir-test-data-set/au-core/PractitionerRole-laing-malinda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mckane-eugena` — `au-fhir-test-data-set/au-core/PractitionerRole-mckane-eugena.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcnaughton-opal` — `au-fhir-test-data-set/au-core/PractitionerRole-mcnaughton-opal.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mullin-kenny` — `au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mullins-bonita` — `au-fhir-test-data-set/au-core/PractitionerRole-mullins-bonita.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `murray-ashli` — `au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `osland-deanne` — `au-fhir-test-data-set/au-core/PractitionerRole-osland-deanne.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `patterson-teri` — `au-fhir-test-data-set/au-core/PractitionerRole-patterson-teri.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `phillips-gerard` — `au-fhir-test-data-set/au-core/PractitionerRole-phillips-gerard.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `quinn-jeramy` — `au-fhir-test-data-set/au-core/PractitionerRole-quinn-jeramy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `retailpharmacist-coughlin-tonda` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-coughlin-tonda.json`
- `rodd-illa` — `au-fhir-test-data-set/au-core/PractitionerRole-rodd-illa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `schaefer-elden` — `au-fhir-test-data-set/au-core/PractitionerRole-schaefer-elden.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sharp-cherish` — `au-fhir-test-data-set/au-core/PractitionerRole-sharp-cherish.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `shephard-vern` — `au-fhir-test-data-set/au-core/PractitionerRole-shephard-vern.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `vaughan-blaine` — `au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Practitioner** (36)

- `alcock-devon` — `au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `blackwood-ella` — `au-fhir-test-data-set/au-core/Practitioner-blackwood-ella.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bond-edmundo` — `au-fhir-test-data-set/au-core/Practitioner-bond-edmundo.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bowyer-norbert` — `au-fhir-test-data-set/au-core/Practitioner-bowyer-norbert.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `coughlin-tonda` — `au-fhir-test-data-set/au-core/Practitioner-coughlin-tonda.json`
- `dempsey-carli` — `au-fhir-test-data-set/au-core/Practitioner-dempsey-carli.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `egan-anja` — `au-fhir-test-data-set/au-core/Practitioner-egan-anja.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `findley-betty` — `au-fhir-test-data-set/au-core/Practitioner-findley-betty.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `frankel-caroline` — `au-fhir-test-data-set/au-core/Practitioner-frankel-caroline.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `fuller-kendrick` — `au-fhir-test-data-set/au-core/Practitioner-fuller-kendrick.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `greene-delores` — `au-fhir-test-data-set/au-core/Practitioner-greene-delores.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hallan-maggie` — `au-fhir-test-data-set/au-core/Practitioner-hallan-maggie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hamel-opal` — `au-fhir-test-data-set/au-core/Practitioner-hamel-opal.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hatcher-merrill` — `au-fhir-test-data-set/au-core/Practitioner-hatcher-merrill.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `higgs-allegra` — `au-fhir-test-data-set/au-core/Practitioner-higgs-allegra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hilton-della` — `au-fhir-test-data-set/au-core/Practitioner-hilton-della.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `joyce-mae` — `au-fhir-test-data-set/au-core/Practitioner-joyce-mae.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `keith-margot` — `au-fhir-test-data-set/au-core/Practitioner-keith-margot.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `kelly-arlene` — `au-fhir-test-data-set/au-core/Practitioner-kelly-arlene.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `keyes-chau` — `au-fhir-test-data-set/au-core/Practitioner-keyes-chau.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `laing-malinda` — `au-fhir-test-data-set/au-core/Practitioner-laing-malinda.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mckane-eugena` — `au-fhir-test-data-set/au-core/Practitioner-mckane-eugena.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mcnaughton-opal` — `au-fhir-test-data-set/au-core/Practitioner-mcnaughton-opal.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mullin-kenny` — `au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `mullins-bonita` — `au-fhir-test-data-set/au-core/Practitioner-mullins-bonita.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `murray-ashli` — `au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `osland-deanne` — `au-fhir-test-data-set/au-core/Practitioner-osland-deanne.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `patterson-teri` — `au-fhir-test-data-set/au-core/Practitioner-patterson-teri.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `phillips-gerard` — `au-fhir-test-data-set/au-core/Practitioner-phillips-gerard.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `quinn-aisha` — `au-fhir-test-data-set/au-core/Practitioner-quinn-aisha.json`
- `quinn-jeramy` — `au-fhir-test-data-set/au-core/Practitioner-quinn-jeramy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `rodd-illa` — `au-fhir-test-data-set/au-core/Practitioner-rodd-illa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `schaefer-elden` — `au-fhir-test-data-set/au-core/Practitioner-schaefer-elden.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sharp-cherish` — `au-fhir-test-data-set/au-core/Practitioner-sharp-cherish.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `shephard-vern` — `au-fhir-test-data-set/au-core/Practitioner-shephard-vern.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `vaughan-blaine` — `au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*

**HealthcareService** (2)

- `communitypharmacy-launching-place-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-launching-place-pharmacy.json`
- `opticaldispensing-eltham-north-optical` — `au-fhir-test-data-set/au-core/HealthcareService-opticaldispensing-eltham-north-optical.json`

**Organization** (23)

- `eltham-north-optical` — `au-fhir-test-data-set/au-core/Organization-eltham-north-optical.json`
- `launching-place-pharmacy` — `au-fhir-test-data-set/au-core/Organization-launching-place-pharmacy.json`
- `melbourne-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `southbank-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `southbank-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `southbank-speech-pathology` — `au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `st-kilda-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `st-kilda-ot-services` — `au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `st-kilda-physiology` — `au-fhir-test-data-set/au-core/Organization-st-kilda-physiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `st-kilda-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-st-kilda-physiotherapy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `st-kilda-psychology` — `au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-cardiology` — `au-fhir-test-data-set/au-core/Organization-sunshine-cardiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-endocrinology` — `au-fhir-test-data-set/au-core/Organization-sunshine-endocrinology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-medical-centre` — `au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-nephrology` — `au-fhir-test-data-set/au-core/Organization-sunshine-nephrology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-ophthalmology` — `au-fhir-test-data-set/au-core/Organization-sunshine-ophthalmology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-optical` — `au-fhir-test-data-set/au-core/Organization-sunshine-optical.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-pathology` — `au-fhir-test-data-set/au-core/Organization-sunshine-pathology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-pharmacy` — `au-fhir-test-data-set/au-core/Organization-sunshine-pharmacy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-sunshine-physiotherapy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `sunshine-radiology` — `au-fhir-test-data-set/au-core/Organization-sunshine-radiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `tarneit-health-network` — `au-fhir-test-data-set/au-core/Organization-tarneit-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

**Location** (2)

- `eltham-north-optical` — `au-fhir-test-data-set/au-core/Location-eltham-north-optical.json`
- `launching-place-pharmacy` — `au-fhir-test-data-set/au-core/Location-launching-place-pharmacy.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 325xx-327xx</strong> (3 entities)</summary>


_Cooriemungle._


**HealthcareService** (1)

- `specialistmedical-cooriemungle-cardiology-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-cooriemungle-cardiology-clinic.json`

**Organization** (1)

- `cooriemungle-cardiology-clinic` — `au-fhir-test-data-set/au-core/Organization-cooriemungle-cardiology-clinic.json`

**Location** (1)

- `cooriemungle-cardiology-clinic` — `au-fhir-test-data-set/au-core/Location-cooriemungle-cardiology-clinic.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 330xx-331xx</strong> (11 entities)</summary>


_Langkoop, Wannon._


**PractitionerRole** (4)

- `midwife-spiers-erich` — `au-fhir-test-data-set/au-core/PractitionerRole-midwife-spiers-erich.json`
- `nursepractitioner-healy-damian` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-healy-damian.json`
- `registerednurses-chambers-greg` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-chambers-greg.json`
- `surgeongeneral-lamerton-betsy` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-lamerton-betsy.json`

**Practitioner** (4)

- `chambers-greg` — `au-fhir-test-data-set/au-core/Practitioner-chambers-greg.json`
- `healy-damian` — `au-fhir-test-data-set/au-core/Practitioner-healy-damian.json`
- `lamerton-betsy` — `au-fhir-test-data-set/au-core/Practitioner-lamerton-betsy.json`
- `spiers-erich` — `au-fhir-test-data-set/au-core/Practitioner-spiers-erich.json`

**HealthcareService** (1)

- `privateacute-wannon-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-wannon-private-hospital.json`

**Organization** (1)

- `wannon-private-hospital` — `au-fhir-test-data-set/au-core/Organization-wannon-private-hospital.json`

**Location** (1)

- `wannon-private-hospital` — `au-fhir-test-data-set/au-core/Location-wannon-private-hospital.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 332xx-334xx</strong> (12 entities)</summary>


_Maddingley, Mount Doran, Rowsley._


**Patient** (1)

- `inveraity-polly` — `au-fhir-test-data-set/au-core/Patient-inveraity-polly.json`

**PractitionerRole** (4)

- `nursepractitioner-thorpe-mia` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-thorpe-mia.json`
- `paediatrician-corbett-clementine` — `au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-corbett-clementine.json`
- `registerednurses-goodwin-aida` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-goodwin-aida.json`
- `registerednurses-ross-moses` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-ross-moses.json`

**Practitioner** (4)

- `corbett-clementine` — `au-fhir-test-data-set/au-core/Practitioner-corbett-clementine.json`
- `goodwin-aida` — `au-fhir-test-data-set/au-core/Practitioner-goodwin-aida.json`
- `ross-moses` — `au-fhir-test-data-set/au-core/Practitioner-ross-moses.json`
- `thorpe-mia` — `au-fhir-test-data-set/au-core/Practitioner-thorpe-mia.json`

**HealthcareService** (1)

- `privateprofit-rowsley-aged-care` — `au-fhir-test-data-set/au-core/HealthcareService-privateprofit-rowsley-aged-care.json`

**Organization** (1)

- `rowsley-aged-care` — `au-fhir-test-data-set/au-core/Organization-rowsley-aged-care.json`

**Location** (1)

- `rowsley-aged-care` — `au-fhir-test-data-set/au-core/Location-rowsley-aged-care.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 336xx-338xx</strong> (5 entities)</summary>


_Mount Glasgow._


**PractitionerRole** (1)

- `emergencymedicine-hickson-ngoc` — `au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-hickson-ngoc.json`

**Practitioner** (1)

- `hickson-ngoc` — `au-fhir-test-data-set/au-core/Practitioner-hickson-ngoc.json`

**HealthcareService** (1)

- `emergencydepartment-mount-glasgow-emergency` — `au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-mount-glasgow-emergency.json`

**Organization** (1)

- `mount-glasgow-emergency` — `au-fhir-test-data-set/au-core/Organization-mount-glasgow-emergency.json`

**Location** (1)

- `mount-glasgow-emergency` — `au-fhir-test-data-set/au-core/Location-mount-glasgow-emergency.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 340xx-341xx</strong> (12 entities)</summary>


_Douglas, Mckenzie Creek._


**PractitionerRole** (3)

- `diagnostic-burdett-palmer` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-burdett-palmer.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `diagnostic-mccarthy-kate` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mccarthy-kate.json`
- `medicaldiagnostic-short-miranda` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-short-miranda.json`

**Practitioner** (3)

- `burdett-palmer` — `au-fhir-test-data-set/au-core/Practitioner-burdett-palmer.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `mccarthy-kate` — `au-fhir-test-data-set/au-core/Practitioner-mccarthy-kate.json`
- `short-miranda` — `au-fhir-test-data-set/au-core/Practitioner-short-miranda.json`

**HealthcareService** (2)

- `diagnosticimaging-douglas-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-douglas-radiology.json`
- `diagnosticimaging-mckenzie-creek-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mckenzie-creek-radiology.json`

**Organization** (2)

- `douglas-radiology` — `au-fhir-test-data-set/au-core/Organization-douglas-radiology.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `mckenzie-creek-radiology` — `au-fhir-test-data-set/au-core/Organization-mckenzie-creek-radiology.json`

**Location** (2)

- `douglas-radiology` — `au-fhir-test-data-set/au-core/Location-douglas-radiology.json`
- `mckenzie-creek-radiology` — `au-fhir-test-data-set/au-core/Location-mckenzie-creek-radiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 345xx-347xx</strong> (15 entities)</summary>


_Joyces Creek, Mitchells Hill, Trentham._


**PractitionerRole** (3)

- `generalpractitioner-lumb-mary` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lumb-mary.json`
- `pathologist-hart-clifton` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hart-clifton.json`
- `registerednurses-gidley-dee` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-dee.json`

**Practitioner** (3)

- `gidley-dee` — `au-fhir-test-data-set/au-core/Practitioner-gidley-dee.json`
- `hart-clifton` — `au-fhir-test-data-set/au-core/Practitioner-hart-clifton.json`
- `lumb-mary` — `au-fhir-test-data-set/au-core/Practitioner-lumb-mary.json`

**HealthcareService** (3)

- `audiologyservice-mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/HealthcareService-audiologyservice-mitchells-hill-audiology.json`
- `generalpractice-joyces-creek-medical-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json`
- `pathologylaboratory-trentham-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-trentham-pathology.json`

**Organization** (3)

- `joyces-creek-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json`
- `mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/Organization-mitchells-hill-audiology.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*
- `trentham-pathology` — `au-fhir-test-data-set/au-core/Organization-trentham-pathology.json`

**Location** (3)

- `joyces-creek-medical-clinic` — `au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json`
- `mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/Location-mitchells-hill-audiology.json`
- `trentham-pathology` — `au-fhir-test-data-set/au-core/Location-trentham-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 346xx-348xx</strong> (14 entities)</summary>


_Areegra, Joyces Creek, Mitchells Hill, Swanwater West._


**PractitionerRole** (4)

- `complementaryhealth-sheehan-ginger` — `au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-sheehan-ginger.json`
- `diagnostic-baldwin-chi` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-baldwin-chi.json`
- `generalpractitioner-lumb-mary` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lumb-mary.json`
- `registerednurses-gidley-dee` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-dee.json`

**Practitioner** (4)

- `baldwin-chi` — `au-fhir-test-data-set/au-core/Practitioner-baldwin-chi.json`
- `gidley-dee` — `au-fhir-test-data-set/au-core/Practitioner-gidley-dee.json`
- `lumb-mary` — `au-fhir-test-data-set/au-core/Practitioner-lumb-mary.json`
- `sheehan-ginger` — `au-fhir-test-data-set/au-core/Practitioner-sheehan-ginger.json`

**HealthcareService** (2)

- `audiologyservice-mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/HealthcareService-audiologyservice-mitchells-hill-audiology.json`
- `generalpractice-joyces-creek-medical-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json`

**Organization** (2)

- `joyces-creek-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json`
- `mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/Organization-mitchells-hill-audiology.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

**Location** (2)

- `joyces-creek-medical-clinic` — `au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json`
- `mitchells-hill-audiology` — `au-fhir-test-data-set/au-core/Location-mitchells-hill-audiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 350xx-352xx</strong> (5 entities)</summary>


_Bridgewater On Loddon._


**PractitionerRole** (1)

- `pathologist-hollands-beryl` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hollands-beryl.json`

**Practitioner** (1)

- `hollands-beryl` — `au-fhir-test-data-set/au-core/Practitioner-hollands-beryl.json`

**HealthcareService** (1)

- `pathologylaboratory-bridgewater-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-bridgewater-pathology.json`

**Organization** (1)

- `bridgewater-pathology` — `au-fhir-test-data-set/au-core/Organization-bridgewater-pathology.json`

**Location** (1)

- `bridgewater-pathology` — `au-fhir-test-data-set/au-core/Location-bridgewater-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 356xx-358xx</strong> (28 entities)</summary>


_Appin South, Milnes Bridge, Murrabit, Piavella, Pine View._


**Patient** (3)

- `mackay-elliott` — `au-fhir-test-data-set/au-core/Patient-mackay-elliott.json` — *also in: [families](#families) (free to build on)*
- `mackay-fritz` — `au-fhir-test-data-set/au-core/Patient-mackay-fritz.json` — *also in: [families](#families) (free to build on)*
- `mackay-heather` — `au-fhir-test-data-set/au-core/Patient-mackay-heather.json` — *also in: [families](#families) (free to build on)*

**PractitionerRole** (7)

- `cardiologist-sutherland-sallie` — `au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-sutherland-sallie.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*
- `gastroenterologist-roche-louis` — `au-fhir-test-data-set/au-core/PractitionerRole-gastroenterologist-roche-louis.json`
- `generalpractitioner-moss-jaime` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-moss-jaime.json`
- `nursepractitioner-hilton-jaclyn` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-hilton-jaclyn.json`
- `registerednurses-leech-darnell` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-leech-darnell.json`
- `registerednurses-shea-ingrid` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shea-ingrid.json`
- `retailpharmacist-howell-natalia` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-howell-natalia.json`

**Practitioner** (7)

- `hilton-jaclyn` — `au-fhir-test-data-set/au-core/Practitioner-hilton-jaclyn.json`
- `howell-natalia` — `au-fhir-test-data-set/au-core/Practitioner-howell-natalia.json`
- `leech-darnell` — `au-fhir-test-data-set/au-core/Practitioner-leech-darnell.json`
- `moss-jaime` — `au-fhir-test-data-set/au-core/Practitioner-moss-jaime.json`
- `roche-louis` — `au-fhir-test-data-set/au-core/Practitioner-roche-louis.json`
- `shea-ingrid` — `au-fhir-test-data-set/au-core/Practitioner-shea-ingrid.json`
- `sutherland-sallie` — `au-fhir-test-data-set/au-core/Practitioner-sutherland-sallie.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

**HealthcareService** (3)

- `generalmedical-milnes-bridge-medical-centre` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-milnes-bridge-medical-centre.json`
- `pharmacyretail-pine-view-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-pine-view-pharmacy.json`
- `publicacute-murrabit-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json`

**Organization** (3)

- `milnes-bridge-medical-centre` — `au-fhir-test-data-set/au-core/Organization-milnes-bridge-medical-centre.json`
- `murrabit-public-hospital` — `au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*
- `pine-view-pharmacy` — `au-fhir-test-data-set/au-core/Organization-pine-view-pharmacy.json`

**Location** (3)

- `milnes-bridge-medical-centre` — `au-fhir-test-data-set/au-core/Location-milnes-bridge-medical-centre.json`
- `murrabit-public-hospital` — `au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json`
- `pine-view-pharmacy` — `au-fhir-test-data-set/au-core/Location-pine-view-pharmacy.json`

**RelatedPerson** (2)

- `mackay-heather-2` — `au-fhir-test-data-set/au-core/RelatedPerson-mackay-heather-2.json`
- `mackay-heather-3` — `au-fhir-test-data-set/au-core/RelatedPerson-mackay-heather-3.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 366xx-368xx</strong> (1 entity)</summary>


_Benalla._


**Organization** (1)

- `benalla-care-and-support` — `au-fhir-test-data-set/au-core/Organization-benalla-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

</details>
</blockquote>

</details>

<details><summary><strong>WA</strong> (11 groupings, 132 entities)</summary>

<blockquote>
<details><summary><strong>Perth metropolitan</strong> (4 entities)</summary>


_Bassendean, Henderson, South Lake._


**Patient** (1)

- `baratz-toni` — `au-fhir-test-data-set/au-core/Patient-baratz-toni.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*

**PractitionerRole** (1)

- `clinicalpsychologist-mcnaughton-chante` — `au-fhir-test-data-set/au-core/PractitionerRole-clinicalpsychologist-mcnaughton-chante.json`

**Practitioner** (1)

- `mcnaughton-chante` — `au-fhir-test-data-set/au-core/Practitioner-mcnaughton-chante.json`

**Organization** (1)

- `south-lake-care-and-support` — `au-fhir-test-data-set/au-core/Organization-south-lake-care-and-support.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 622xx-624xx</strong> (18 entities)</summary>


_Bunbury, Wellington Forest._


**Patient** (4)

- `ballantyne-flavia-indira` — `au-fhir-test-data-set/au-core/Patient-ballantyne-flavia-indira.json` — *also in: [families](#families) (free to build on)*
- `ballantyne-kelvin-hans` — `au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json` — *also in: [smart-health-checks](#smart-health-checks) (maybe reserved — TBD)*
- `ballantyne-sandy-choy` — `au-fhir-test-data-set/au-core/Patient-ballantyne-sandy-choy.json` — *also in: [families](#families) (free to build on)*
- `ballantyne-terry-bob` — `au-fhir-test-data-set/au-core/Patient-ballantyne-terry-bob.json` — *also in: [families](#families) (free to build on)*

**PractitionerRole** (3)

- `nursepractitioner-osmond-deadra` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-osmond-deadra.json`
- `registerednurses-dent-aldo` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-dent-aldo.json`
- `surgeongeneral-potter-lamar` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-potter-lamar.json`

**Practitioner** (3)

- `dent-aldo` — `au-fhir-test-data-set/au-core/Practitioner-dent-aldo.json`
- `osmond-deadra` — `au-fhir-test-data-set/au-core/Practitioner-osmond-deadra.json`
- `potter-lamar` — `au-fhir-test-data-set/au-core/Practitioner-potter-lamar.json`

**HealthcareService** (1)

- `publicacute-bunbury-public-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-publicacute-bunbury-public-hospital.json`

**Organization** (1)

- `bunbury-public-hospital` — `au-fhir-test-data-set/au-core/Organization-bunbury-public-hospital.json`

**Location** (1)

- `bunbury-public-hospital` — `au-fhir-test-data-set/au-core/Location-bunbury-public-hospital.json`

**RelatedPerson** (5)

- `ballantyne-flavia-2` — `au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-flavia-2.json`
- `ballantyne-flavia-3` — `au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-flavia-3.json`
- `ballantyne-flavia-4` — `au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-flavia-4.json`
- `ballantyne-sandy` — `au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-sandy.json`
- `ballantyne-terry` — `au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-terry.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 624xx-626xx</strong> (14 entities)</summary>


_Balbarrup, Quinninup._


**PractitionerRole** (4)

- `aboriginal-darcy-stella` — `au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-darcy-stella.json`
- `generalpractitioner-jones-blanch` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-jones-blanch.json`
- `registerednurses-clare-evonne` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-clare-evonne.json`
- `registerednurses-power-linda` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-power-linda.json`

**Practitioner** (4)

- `clare-evonne` — `au-fhir-test-data-set/au-core/Practitioner-clare-evonne.json`
- `darcy-stella` — `au-fhir-test-data-set/au-core/Practitioner-darcy-stella.json`
- `jones-blanch` — `au-fhir-test-data-set/au-core/Practitioner-jones-blanch.json`
- `power-linda` — `au-fhir-test-data-set/au-core/Practitioner-power-linda.json`

**HealthcareService** (2)

- `communityhealth-balbarrup-practice` — `au-fhir-test-data-set/au-core/HealthcareService-communityhealth-balbarrup-practice.json`
- `generalpractice-quinninup-medical-clinic` — `au-fhir-test-data-set/au-core/HealthcareService-generalpractice-quinninup-medical-clinic.json`

**Organization** (2)

- `balbarrup-practice` — `au-fhir-test-data-set/au-core/Organization-balbarrup-practice.json`
- `quinninup-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-quinninup-medical-clinic.json`

**Location** (2)

- `balbarrup-practice` — `au-fhir-test-data-set/au-core/Location-balbarrup-practice.json`
- `quinninup-medical-clinic` — `au-fhir-test-data-set/au-core/Location-quinninup-medical-clinic.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 630xx-631xx</strong> (6 entities)</summary>


_Broomehill, Bulyee, Piesseville._


**Patient** (1)

- `thomson-mika` — `au-fhir-test-data-set/au-core/Patient-thomson-mika.json`

**PractitionerRole** (1)

- `optometrist-coulter-rosalina` — `au-fhir-test-data-set/au-core/PractitionerRole-optometrist-coulter-rosalina.json`

**Practitioner** (1)

- `coulter-rosalina` — `au-fhir-test-data-set/au-core/Practitioner-coulter-rosalina.json`

**HealthcareService** (1)

- `specialistmedical-piesseville-gastroenterology` — `au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-piesseville-gastroenterology.json`

**Organization** (1)

- `piesseville-gastroenterology` — `au-fhir-test-data-set/au-core/Organization-piesseville-gastroenterology.json`

**Location** (1)

- `piesseville-gastroenterology` — `au-fhir-test-data-set/au-core/Location-piesseville-gastroenterology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 641xx-643xx</strong> (4 entities)</summary>


_Bruce Rock, Menzies, Moorine Rock._


**Patient** (1)

- `bassett-imogene-betsy` — `au-fhir-test-data-set/au-core/Patient-bassett-imogene-betsy.json`

**PractitionerRole** (1)

- `medicaldiagnostic-oritz-abbie` — `au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-oritz-abbie.json`

**Practitioner** (1)

- `oritz-abbie` — `au-fhir-test-data-set/au-core/Practitioner-oritz-abbie.json`

**Organization** (1)

- `menzies-health-network` — `au-fhir-test-data-set/au-core/Organization-menzies-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 642xx-644xx</strong> (9 entities)</summary>


_Lake Wells, Menzies, Moorine Rock._


**Patient** (1)

- `bassett-imogene-betsy` — `au-fhir-test-data-set/au-core/Patient-bassett-imogene-betsy.json`

**PractitionerRole** (2)

- `generalpractitioner-harding-diana` — `au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-harding-diana.json`
- `registerednurses-lumb-lovie` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-lumb-lovie.json`

**Practitioner** (2)

- `harding-diana` — `au-fhir-test-data-set/au-core/Practitioner-harding-diana.json`
- `lumb-lovie` — `au-fhir-test-data-set/au-core/Practitioner-lumb-lovie.json`

**HealthcareService** (1)

- `generalmedical-lake-wells-medical-practice` — `au-fhir-test-data-set/au-core/HealthcareService-generalmedical-lake-wells-medical-practice.json`

**Organization** (2)

- `lake-wells-medical-practice` — `au-fhir-test-data-set/au-core/Organization-lake-wells-medical-practice.json`
- `menzies-health-network` — `au-fhir-test-data-set/au-core/Organization-menzies-health-network.json` — *also in: [community-contributions](#community-contributions) (free to build on)*

**Location** (1)

- `lake-wells-medical-practice` — `au-fhir-test-data-set/au-core/Location-lake-wells-medical-practice.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 661xx-663xx</strong> (7 entities)</summary>


_Bunjil, Koolanooka._


**PractitionerRole** (2)

- `diagnostic-gidley-aubrey` — `au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-gidley-aubrey.json`
- `specialistphysicians-hickman-sally` — `au-fhir-test-data-set/au-core/PractitionerRole-specialistphysicians-hickman-sally.json`

**Practitioner** (2)

- `gidley-aubrey` — `au-fhir-test-data-set/au-core/Practitioner-gidley-aubrey.json`
- `hickman-sally` — `au-fhir-test-data-set/au-core/Practitioner-hickman-sally.json`

**HealthcareService** (1)

- `diagnosticimaging-koolanooka-radiology` — `au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-koolanooka-radiology.json`

**Organization** (1)

- `koolanooka-radiology` — `au-fhir-test-data-set/au-core/Organization-koolanooka-radiology.json`

**Location** (1)

- `koolanooka-radiology` — `au-fhir-test-data-set/au-core/Location-koolanooka-radiology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 670xx-671xx</strong> (11 entities)</summary>


_Morgantown, Wooramel._


**PractitionerRole** (4)

- `gastroenterologist-miller-kittie` — `au-fhir-test-data-set/au-core/PractitionerRole-gastroenterologist-miller-kittie.json`
- `nursepractitioner-gaynor-phil` — `au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-gaynor-phil.json`
- `registerednurses-cooke-arthur` — `au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-cooke-arthur.json`
- `surgeongeneral-brooksby-caterina` — `au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-brooksby-caterina.json`

**Practitioner** (4)

- `brooksby-caterina` — `au-fhir-test-data-set/au-core/Practitioner-brooksby-caterina.json`
- `cooke-arthur` — `au-fhir-test-data-set/au-core/Practitioner-cooke-arthur.json`
- `gaynor-phil` — `au-fhir-test-data-set/au-core/Practitioner-gaynor-phil.json`
- `miller-kittie` — `au-fhir-test-data-set/au-core/Practitioner-miller-kittie.json`

**HealthcareService** (1)

- `privateacute-morgantown-private-hospital` — `au-fhir-test-data-set/au-core/HealthcareService-privateacute-morgantown-private-hospital.json`

**Organization** (1)

- `morgantown-private-hospital` — `au-fhir-test-data-set/au-core/Organization-morgantown-private-hospital.json`

**Location** (1)

- `morgantown-private-hospital` — `au-fhir-test-data-set/au-core/Location-morgantown-private-hospital.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 671xx-673xx</strong> (51 entities)</summary>


_Broome._


**Patient** (1)

- `coombe-ross` — `au-fhir-test-data-set/au-core/Patient-coombe-ross.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**PractitionerRole** (20)

- `allardice-della` — `au-fhir-test-data-set/au-core/PractitionerRole-allardice-della.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `baratz-layla` — `au-fhir-test-data-set/au-core/PractitionerRole-baratz-layla.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bassett-elmer` — `au-fhir-test-data-set/au-core/PractitionerRole-bassett-elmer.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `butler-cheryl` — `au-fhir-test-data-set/au-core/PractitionerRole-butler-cheryl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `clapham-laurie` — `au-fhir-test-data-set/au-core/PractitionerRole-clapham-laurie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `davies-keiko` — `au-fhir-test-data-set/au-core/PractitionerRole-davies-keiko.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `devine-frank` — `au-fhir-test-data-set/au-core/PractitionerRole-devine-frank.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `gates-anton` — `au-fhir-test-data-set/au-core/PractitionerRole-gates-anton.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `giles-veronique` — `au-fhir-test-data-set/au-core/PractitionerRole-giles-veronique.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `goldsmith-monique` — `au-fhir-test-data-set/au-core/PractitionerRole-goldsmith-monique.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hackett-norman` — `au-fhir-test-data-set/au-core/PractitionerRole-hackett-norman.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hodges-julia` — `au-fhir-test-data-set/au-core/PractitionerRole-hodges-julia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `horn-wes` — `au-fhir-test-data-set/au-core/PractitionerRole-horn-wes.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ibbotson-destiny` — `au-fhir-test-data-set/au-core/PractitionerRole-ibbotson-destiny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowry-bennett` — `au-fhir-test-data-set/au-core/PractitionerRole-lowry-bennett.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `moran-linoel` — `au-fhir-test-data-set/au-core/PractitionerRole-moran-linoel.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `patrick-thalia` — `au-fhir-test-data-set/au-core/PractitionerRole-patrick-thalia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `poulson-lisa` — `au-fhir-test-data-set/au-core/PractitionerRole-poulson-lisa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `simmons-ashton` — `au-fhir-test-data-set/au-core/PractitionerRole-simmons-ashton.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `thorburn-juanita` — `au-fhir-test-data-set/au-core/PractitionerRole-thorburn-juanita.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Practitioner** (20)

- `allardice-della` — `au-fhir-test-data-set/au-core/Practitioner-allardice-della.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `baratz-layla` — `au-fhir-test-data-set/au-core/Practitioner-baratz-layla.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `bassett-elmer` — `au-fhir-test-data-set/au-core/Practitioner-bassett-elmer.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `butler-cheryl` — `au-fhir-test-data-set/au-core/Practitioner-butler-cheryl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `clapham-laurie` — `au-fhir-test-data-set/au-core/Practitioner-clapham-laurie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `davies-keiko` — `au-fhir-test-data-set/au-core/Practitioner-davies-keiko.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `devine-frank` — `au-fhir-test-data-set/au-core/Practitioner-devine-frank.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `gates-anton` — `au-fhir-test-data-set/au-core/Practitioner-gates-anton.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `giles-veronique` — `au-fhir-test-data-set/au-core/Practitioner-giles-veronique.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `goldsmith-monique` — `au-fhir-test-data-set/au-core/Practitioner-goldsmith-monique.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hackett-norman` — `au-fhir-test-data-set/au-core/Practitioner-hackett-norman.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hodges-julia` — `au-fhir-test-data-set/au-core/Practitioner-hodges-julia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `horn-wes` — `au-fhir-test-data-set/au-core/Practitioner-horn-wes.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ibbotson-destiny` — `au-fhir-test-data-set/au-core/Practitioner-ibbotson-destiny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowry-bennett` — `au-fhir-test-data-set/au-core/Practitioner-lowry-bennett.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `moran-linoel` — `au-fhir-test-data-set/au-core/Practitioner-moran-linoel.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `patrick-thalia` — `au-fhir-test-data-set/au-core/Practitioner-patrick-thalia.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `poulson-lisa` — `au-fhir-test-data-set/au-core/Practitioner-poulson-lisa.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `simmons-ashton` — `au-fhir-test-data-set/au-core/Practitioner-simmons-ashton.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `thorburn-juanita` — `au-fhir-test-data-set/au-core/Practitioner-thorburn-juanita.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

**Organization** (10)

- `broome-community-health` — `au-fhir-test-data-set/au-core/Organization-broome-community-health.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-medical-clinic` — `au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-nutrition` — `au-fhir-test-data-set/au-core/Organization-broome-nutrition.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-optometry` — `au-fhir-test-data-set/au-core/Organization-broome-optometry.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-ot-services` — `au-fhir-test-data-set/au-core/Organization-broome-ot-services.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-physiology` — `au-fhir-test-data-set/au-core/Organization-broome-physiology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-physiotherapy` — `au-fhir-test-data-set/au-core/Organization-broome-physiotherapy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-podiatry` — `au-fhir-test-data-set/au-core/Organization-broome-podiatry.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-psychology` — `au-fhir-test-data-set/au-core/Organization-broome-psychology.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `broome-specialist-clinic` — `au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 673xx-675xx</strong> (5 entities)</summary>


_Kununurra._


**PractitionerRole** (1)

- `pathologist-khouri-stewart` — `au-fhir-test-data-set/au-core/PractitionerRole-pathologist-khouri-stewart.json`

**Practitioner** (1)

- `khouri-stewart` — `au-fhir-test-data-set/au-core/Practitioner-khouri-stewart.json`

**HealthcareService** (1)

- `pathologylaboratory-kununurra-pathology` — `au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kununurra-pathology.json`

**Organization** (1)

- `kununurra-pathology` — `au-fhir-test-data-set/au-core/Organization-kununurra-pathology.json`

**Location** (1)

- `kununurra-pathology` — `au-fhir-test-data-set/au-core/Location-kununurra-pathology.json`

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 676xx-678xx</strong> (5 entities)</summary>


_Mcbeath._


**PractitionerRole** (1)

- `retailpharmacist-mclennan-miguel` — `au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-mclennan-miguel.json`

**Practitioner** (1)

- `mclennan-miguel` — `au-fhir-test-data-set/au-core/Practitioner-mclennan-miguel.json`

**HealthcareService** (1)

- `pharmacyretail-mcbeath-pharmacy` — `au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-mcbeath-pharmacy.json`

**Organization** (1)

- `mcbeath-pharmacy` — `au-fhir-test-data-set/au-core/Organization-mcbeath-pharmacy.json`

**Location** (1)

- `mcbeath-pharmacy` — `au-fhir-test-data-set/au-core/Location-mcbeath-pharmacy.json`

</details>
</blockquote>

</details>


## Families <a id="families"></a>

### Purpose

Identifies entities that constitute a family, for constructing consumer journeys involving related patients.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Grouping identifies plausible family relationships. Members are free to build on and are not reserved to their originating group.

### Provenance & use

Proposed by a script from two independent signals and confirmed by a human. Where a candidate can be neither confirmed nor rejected because the evidence that would settle it is unavailable, it is recorded as potentially related rather than forced into a binary.

### Relationships

Most members currently have no clinical data, so they are also [Blank-slate patients](#blank-slate-patients).

### How is this subset identified?

Derived from two primary signals, then confirmed by a human. A shared Medicare card is the strongest: the card number is shared by a family and only the final individual reference number differs. The RelatedPerson network is the second, giving an explicit relationship code. Neither subsumes the other — a newborn not yet on the card is found only by the RelatedPerson network — so both are applied and combined. Matching surname or address is used only to propose further candidates for review.


_Classification: Derived + Curated._
> 7 RelatedPerson-network families (30 entities); 4 additional surname/address candidates.
> 7 confirmed, 2 rejected, 2 flagged as potential families, 0 awaiting a decision.
> A shared Medicare card is treated as a primary signal alongside the RelatedPerson network: the card number is 10 digits plus a per-person Individual Reference Number, so a family on one card shares the first 10 digits. Neither signal dominates — a newborn not yet on the card is found only via RelatedPerson.
> 2 RelatedPerson record(s) excluded as 'unrelated friend' (FRND) and not used to join any family.
> Family members are not required to share an address. Same-surname and same-address candidates are proposals only, never asserted — measured case: 9 Patient files sharing a surname and address are 9 test-data variants of one synthetic patient, not a family.

### Members (30)

<details><summary><strong>Ballantyne</strong> (4 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (6951826031)._

**Patient** (4)

- `ballantyne-flavia-indira` — `au-fhir-test-data-set/au-core/Patient-ballantyne-flavia-indira.json`
- `ballantyne-kelvin-hans` — `au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json` — *also in: [smart-health-checks](#smart-health-checks) (maybe reserved — TBD)*
- `ballantyne-sandy-choy` — `au-fhir-test-data-set/au-core/Patient-ballantyne-sandy-choy.json`
- `ballantyne-terry-bob` — `au-fhir-test-data-set/au-core/Patient-ballantyne-terry-bob.json`

</details>

<details><summary><strong>Banks</strong> (7 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954541041)._

**Patient** (5)

- `baby-banks-john` — `au-fhir-test-data-set/au-core/Patient-baby-banks-john.json` — *also in: [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*
- `banks-jamila-angie` — `au-fhir-test-data-set/au-core/Patient-banks-jamila-angie.json`
- `banks-jeramy-ezra` — `au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `banks-jonas-cary` — `au-fhir-test-data-set/au-core/Patient-banks-jonas-cary.json`
- `banks-mia-leanne` — `au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved), [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [au-ps-test-patients](#au-ps-test-patients) (maybe reserved — TBD), [inferno-default-patients](#inferno-default-patients) (maybe reserved — TBD)*

**RelatedPerson** (2)

- `banks-bob` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-bob.json`
- `banks-mia-leanne-father` — `au-fhir-test-data-set/au-core/RelatedPerson-banks-mia-leanne-father.json` — *also in: [au-core-ig-examples](#au-core-ig-examples) (reserved)*

</details>

<details><summary><strong>Dietrich</strong> (4 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954541131)._

**Patient** (4)

- `dietrich-blake-louis` — `au-fhir-test-data-set/au-core/Patient-dietrich-blake-louis.json`
- `dietrich-diedre-alicia` — `au-fhir-test-data-set/au-core/Patient-dietrich-diedre-alicia.json`
- `dietrich-kimbra-althea` — `au-fhir-test-data-set/au-core/Patient-dietrich-kimbra-althea.json`
- `dietrich-phillipa-grace` — `au-fhir-test-data-set/au-core/Patient-dietrich-phillipa-grace.json`

</details>

<details><summary><strong>Hennessy</strong> (3 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954663691)._

**Patient** (3)

- `hennessy-billy` — `au-fhir-test-data-set/au-core/Patient-hennessy-billy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-jenny` — `au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-kacey` — `au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

</details>

<details><summary><strong>Lowe</strong> (4 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954664391)._

**Patient** (4)

- `lowe-alessandra` — `au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alix` — `au-fhir-test-data-set/au-core/Patient-lowe-alix.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-cedric` — `au-fhir-test-data-set/au-core/Patient-lowe-cedric.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-valerie` — `au-fhir-test-data-set/au-core/Patient-lowe-valerie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*

</details>

<details><summary><strong>Mackay</strong> (3 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (3951334131)._

**Patient** (3)

- `mackay-elliott` — `au-fhir-test-data-set/au-core/Patient-mackay-elliott.json`
- `mackay-fritz` — `au-fhir-test-data-set/au-core/Patient-mackay-fritz.json`
- `mackay-heather` — `au-fhir-test-data-set/au-core/Patient-mackay-heather.json`

</details>

<details><summary><strong>Veitch</strong> (5 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (4951652281)._

**Patient** (5)

- `veitch-beau-bradley` — `au-fhir-test-data-set/au-core/Patient-veitch-beau-bradley.json`
- `veitch-miles-dudley` — `au-fhir-test-data-set/au-core/Patient-veitch-miles-dudley.json`
- `veitch-mitchell-carl` — `au-fhir-test-data-set/au-core/Patient-veitch-mitchell-carl.json`
- `veitch-nathan-chris` — `au-fhir-test-data-set/au-core/Patient-veitch-nathan-chris.json`
- `veitch-savannah-sheena` — `au-fhir-test-data-set/au-core/Patient-veitch-savannah-sheena.json`

</details>


<details><summary><strong>Potentially related — unconfirmed</strong> (2 candidates)</summary>

| Candidate | Entities | Why it is unresolved |
| --- | --- | --- |
| `surname-hoskins-marisa` | hoskins-marisa, hoskins-sergio-lionel | Potential family, unproven. Marisa (F, Napier NZ, 1991-02-06) and Sergio (M, Tostaree VIC, 1991-05-13) share a surname; born ~3 months apart so not full siblings, but step-siblings, cousins or partners remain possible. No RelatedPerson link. The Medicare card test cannot adjudicate: Sergio holds 3951334041, Marisa has no Medicare number. |
| `surname-sandilands-kendall` | sandilands-kendall, sandilands-young | Potential family, unproven. Kendall (F, Sheaoak Flat SA, 1981) and Young (Warnertown SA, 1962) share a surname and state, ~19 years apart — plausibly parent/child. No RelatedPerson link. The Medicare card test cannot adjudicate: Kendall holds 5951138661, Young has no Medicare number at all. |

</details>


## Blank-slate patients <a id="blank-slate-patients"></a>

### Purpose

Identifies patients with no clinical data, so they can be selected for a new consumer journey without pre-existing content conflicting.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
The purpose of this subset is to identify patients that are free to build on. Adding clinical data to a member simply removes it from the subset on the next regeneration.

### Provenance & use

Computed from the data set on every regeneration rather than recorded. Membership therefore changes automatically as clinical data is added.

### Relationships

Many members also appear in [Families](#families), and some are [Missing and suppressed data examples](#missing-suppressed-data) instances.

### How is this subset identified?

Derived automatically. A patient is a member when no clinical resource in the data set references it as subject. Administrative links such as RelatedPerson or Coverage do not count, because they record no clinical fact for new content to conflict with.


_Classification: Derived._
> 79 of 93 patients have no clinical data.
> A patient referenced only by RelatedPerson, Coverage or Appointment counts as a blank slate: those record no clinical fact for new content to conflict with.

### Members (79)

<details><summary>79 entities — click to expand</summary>

**Patient** (79)

- `archibald-dante` — `au-fhir-test-data-set/au-core/Patient-archibald-dante.json`
- `baldry-terence-emile` — `au-fhir-test-data-set/au-core/Patient-baldry-terence-emile.json`
- `baldwin-dinah` — `au-fhir-test-data-set/au-core/Patient-baldwin-dinah.json`
- `ballantyne-flavia-indira` — `au-fhir-test-data-set/au-core/Patient-ballantyne-flavia-indira.json` — *also in: [families](#families) (free to build on)*
- `ballantyne-kelvin-hans` — `au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json` — *also in: [smart-health-checks](#smart-health-checks) (maybe reserved — TBD)*
- `ballantyne-sandy-choy` — `au-fhir-test-data-set/au-core/Patient-ballantyne-sandy-choy.json` — *also in: [families](#families) (free to build on)*
- `ballantyne-terry-bob` — `au-fhir-test-data-set/au-core/Patient-ballantyne-terry-bob.json` — *also in: [families](#families) (free to build on)*
- `banks-jamila-angie` — `au-fhir-test-data-set/au-core/Patient-banks-jamila-angie.json` — *also in: [families](#families) (free to build on)*
- `banks-jeramy-ezra` — `au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `banks-jonas-cary` — `au-fhir-test-data-set/au-core/Patient-banks-jonas-cary.json` — *also in: [families](#families) (free to build on)*
- `bassett-imogene-betsy` — `au-fhir-test-data-set/au-core/Patient-bassett-imogene-betsy.json`
- `black-kerry-dougal` — `au-fhir-test-data-set/au-core/Patient-black-kerry-dougal.json`
- `boulton-annika` — `au-fhir-test-data-set/au-core/Patient-boulton-annika.json`
- `britton-brian-edwin` — `au-fhir-test-data-set/au-core/Patient-britton-brian-edwin.json`
- `callow-veronica-connie` — `au-fhir-test-data-set/au-core/Patient-callow-veronica-connie.json`
- `campbell-ambrose` — `au-fhir-test-data-set/au-core/Patient-campbell-ambrose.json`
- `cane-cheyenne-elaina` — `au-fhir-test-data-set/au-core/Patient-cane-cheyenne-elaina.json`
- `coombe-ross` — `au-fhir-test-data-set/au-core/Patient-coombe-ross.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `cummings-angelo` — `au-fhir-test-data-set/au-core/Patient-cummings-angelo.json`
- `davis-juan` — `au-fhir-test-data-set/au-core/Patient-davis-juan.json`
- `dietrich-blake-louis` — `au-fhir-test-data-set/au-core/Patient-dietrich-blake-louis.json` — *also in: [families](#families) (free to build on)*
- `dietrich-diedre-alicia` — `au-fhir-test-data-set/au-core/Patient-dietrich-diedre-alicia.json` — *also in: [families](#families) (free to build on)*
- `dietrich-kimbra-althea` — `au-fhir-test-data-set/au-core/Patient-dietrich-kimbra-althea.json` — *also in: [families](#families) (free to build on)*
- `dietrich-phillipa-grace` — `au-fhir-test-data-set/au-core/Patient-dietrich-phillipa-grace.json` — *also in: [families](#families) (free to build on)*
- `downie-grant` — `au-fhir-test-data-set/au-core/Patient-downie-grant.json`
- `ewing-ferdinand` — `au-fhir-test-data-set/au-core/Patient-ewing-ferdinand.json`
- `foreman-caterina` — `au-fhir-test-data-set/au-core/Patient-foreman-caterina.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `frost-rhett-kent` — `au-fhir-test-data-set/au-core/Patient-frost-rhett-kent.json`
- `hampton-jenice` — `au-fhir-test-data-set/au-core/Patient-hampton-jenice.json`
- `hennessy-billy` — `au-fhir-test-data-set/au-core/Patient-hennessy-billy.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-jenny` — `au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hennessy-kacey` — `au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `hoskins-marisa` — `au-fhir-test-data-set/au-core/Patient-hoskins-marisa.json`
- `hoskins-sergio-lionel` — `au-fhir-test-data-set/au-core/Patient-hoskins-sergio-lionel.json`
- `hulme-brant` — `au-fhir-test-data-set/au-core/Patient-hulme-brant.json`
- `humphries-jayson` — `au-fhir-test-data-set/au-core/Patient-humphries-jayson.json`
- `inveraity-polly` — `au-fhir-test-data-set/au-core/Patient-inveraity-polly.json`
- `italia-sofia-missing-birthDate` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-birthDate.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-missing-gender` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-gender.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-missing-identifier` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-identifier.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-missing-name` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-name.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-suppressed-birthDate` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-birthDate.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-suppressed-gender` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-gender.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-suppressed-identifier` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-identifier.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `italia-sofia-suppressed-name` — `au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-name.json` — *also in: [missing-suppressed-data](#missing-suppressed-data) (reserved)*
- `johnson-joyce` — `au-fhir-test-data-set/au-core/Patient-johnson-joyce.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `keaton-jayme` — `au-fhir-test-data-set/au-core/Patient-keaton-jayme.json`
- `little-rose-gretal` — `au-fhir-test-data-set/au-core/Patient-little-rose-gretal.json`
- `lowe-alessandra` — `au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-alix` — `au-fhir-test-data-set/au-core/Patient-lowe-alix.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-cedric` — `au-fhir-test-data-set/au-core/Patient-lowe-cedric.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lowe-valerie` — `au-fhir-test-data-set/au-core/Patient-lowe-valerie.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `lynch-alyce-shauna` — `au-fhir-test-data-set/au-core/Patient-lynch-alyce-shauna.json`
- `mackay-elliott` — `au-fhir-test-data-set/au-core/Patient-mackay-elliott.json` — *also in: [families](#families) (free to build on)*
- `mackay-heather` — `au-fhir-test-data-set/au-core/Patient-mackay-heather.json` — *also in: [families](#families) (free to build on)*
- `martin-shawn` — `au-fhir-test-data-set/au-core/Patient-martin-shawn.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved)*
- `mclennan-karl` — `au-fhir-test-data-set/au-core/Patient-mclennan-karl.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `moffitt-heath-igor` — `au-fhir-test-data-set/au-core/Patient-moffitt-heath-igor.json`
- `morris-charlotte` — `au-fhir-test-data-set/au-core/Patient-morris-charlotte.json` — *also in: [au-ps-ig-examples](#au-ps-ig-examples) (reserved), [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `moylan-brock` — `au-fhir-test-data-set/au-core/Patient-moylan-brock.json`
- `nash-abel` — `au-fhir-test-data-set/au-core/Patient-nash-abel.json`
- `nielsen-eleanore` — `au-fhir-test-data-set/au-core/Patient-nielsen-eleanore.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `odonnell-gillian` — `au-fhir-test-data-set/au-core/Patient-odonnell-gillian.json`
- `pennington-donnie-kip` — `au-fhir-test-data-set/au-core/Patient-pennington-donnie-kip.json`
- `potts-felix-ernie` — `au-fhir-test-data-set/au-core/Patient-potts-felix-ernie.json`
- `ralph-rudolf` — `au-fhir-test-data-set/au-core/Patient-ralph-rudolf.json`
- `reece-karen` — `au-fhir-test-data-set/au-core/Patient-reece-karen.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `ridgewell-troy` — `au-fhir-test-data-set/au-core/Patient-ridgewell-troy.json`
- `robson-adam` — `au-fhir-test-data-set/au-core/Patient-robson-adam.json`
- `sandilands-young` — `au-fhir-test-data-set/au-core/Patient-sandilands-young.json`
- `simpson-tristan` — `au-fhir-test-data-set/au-core/Patient-simpson-tristan.json` — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys) (maybe reserved — TBD)*
- `thomson-mika` — `au-fhir-test-data-set/au-core/Patient-thomson-mika.json`
- `todd-tanya-estelle` — `au-fhir-test-data-set/au-core/Patient-todd-tanya-estelle.json`
- `vaughan-seymour` — `au-fhir-test-data-set/au-core/Patient-vaughan-seymour.json` — *also in: [scenario-groups](#scenario-groups) (maybe reserved — TBD)*
- `veitch-beau-bradley` — `au-fhir-test-data-set/au-core/Patient-veitch-beau-bradley.json` — *also in: [families](#families) (free to build on)*
- `veitch-miles-dudley` — `au-fhir-test-data-set/au-core/Patient-veitch-miles-dudley.json` — *also in: [families](#families) (free to build on)*
- `veitch-mitchell-carl` — `au-fhir-test-data-set/au-core/Patient-veitch-mitchell-carl.json` — *also in: [families](#families) (free to build on)*
- `veitch-nathan-chris` — `au-fhir-test-data-set/au-core/Patient-veitch-nathan-chris.json` — *also in: [families](#families) (free to build on)*
- `veitch-savannah-sheena` — `au-fhir-test-data-set/au-core/Patient-veitch-savannah-sheena.json` — *also in: [families](#families) (free to build on)*

</details>

