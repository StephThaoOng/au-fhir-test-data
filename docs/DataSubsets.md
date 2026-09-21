# HL7 AU FHIR Test Data — Data Subsets

Identifies the logical subsets of the test data set: which entities belong to each, how membership is established, who owns it, and how subsets relate to one another. See [docs/data-subsets/README.md](data-subsets/README.md) for how to regenerate this page.

### Why these subsets are worth tracking

The administrative entities in this data set — Patient, RelatedPerson, Practitioner, PractitionerRole, Organization, HealthcareService, Location and Endpoint — cannot simply be created or modified on demand within this project. Their key identifiers and some core attributes are allocated by Services Australia and correspond to entities provisioned in the HI Vendor Test Environment; the instances here map those records into FHIR and may include some data enrichment, but generally need to stay aligned with them.

Using the test data therefore tends to start with finding entities that already fit, since requesting new ones is a considerably more costly path. That requires knowing which entities are already committed to a purpose that new content could disturb, which are free to build on, and which suit a new need — co-located for a plausible consumer journey, related as a family, or carrying no clinical data at all. This page is where that is recorded.

### What is in scope

Only the eight administrative entity types listed above. Clinical resources carry far less shared governance with external parties and can be authored more freely, so tracking their subset membership is low value — and where clinical content is needed, it is retrievable from the administrative entity by ordinary FHIR mechanisms. One subset is exempt: *Missing and suppressed data examples*, whose instances demonstrate the correct representation of absent data, a property that attaches to an Observation exactly as it does to a Patient.

### Reading versus writing

**Reading is always unconstrained.** Any entity may be read, loaded, queried or tested against without reference to this page. Where a subset's governance restricts something, it restricts *writing* — adding to or modifying an entity or its network of linked resources — because new content joins a graph that may already be shaped to serve a stated purpose.

A subset stating that its own membership does not reserve an entity does not make that entity free to build on — another subset may reserve it. What governs is the tightest constraint across all of an entity's memberships, which is what each entity's *also in* note surfaces.

### How each subset is identified

Every subset states its classification where it describes how it is identified. The four are defined below; the practical difference is what each needs in order to be trustworthy.

<details><summary>What the four classifications mean</summary>

- **Derived** — computed from the repository by a deterministic script, with no human input. Recomputed on every regeneration, so it is current by construction.
- **Declared** — stated by an authoritative source outside this page, which the page transcribes. Records a resolvable source reference so the transcription can be re-checked, and reports drift rather than silently overwriting.
- **Curated** — decided by this project, with no external source to check against. Records an attester and a confirmation date instead.
- **Derived + Curated** — a script proposes candidate members and a human confirms or rejects each one. Confirmations are persisted, so a regeneration asks only about what is new or changed.

The distinguishing test between Declared and Curated is whether the fact has a source that could change without this page being told. If it does, it is Declared and needs a source reference; if it does not, it is Curated and needs an attester. That is why some sections show a **Source** and others show an attester.

</details>

_Generated 2026-09-21 11:51 UTC from test data at commit `e5469c2a0753a533d1b301a218b3c7509be5ad15`. This page is regenerated manually — see [docs/data-subsets/README.md](data-subsets/README.md)._

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

**Read at:** [`d18d3444e998`](https://github.com/hl7au/au-fhir-core/commit/d18d3444e99890b73078d34fa2e6682a30d88720) — the AU Core IG revision this page was last generated from.
<details><summary>Derivation notes</summary>

> 30 distinct administrative entities are published as examples in hl7au/au-fhir-core.
> 51 non-administrative entities excluded: Observation x17, Condition x4, Medication x4, MedicationStatement x4, AllergyIntolerance x3, Encounter x3, MedicationDispense x3, MedicationRequest x3, DiagnosticReport x2, DocumentReference x2, Immunization x2, Procedure x2, Composition x1, Specimen x1. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.
> 2 IG example resources matched nothing in the test data set; they may be IG-only examples. Listed below, under Members.

</details>


### Members (30)

<details><summary>30 entities — click to expand</summary>

**Patient** (5)

| ID | Also in |
| --- | --- |
| [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json) | *[au-ps-ig-examples](#au-ps-ig-examples), [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |
| [`bennelong-anne`](../au-fhir-test-data-set/au-core/Patient-bennelong-anne.json) |  |
| [`howe-deangelo`](../au-fhir-test-data-set/au-core/Patient-howe-deangelo.json) | *[au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |
| [`irvine-ronny-lawrence`](../au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json) | *[au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |
| [`wang-li`](../au-fhir-test-data-set/au-core/Patient-wang-li.json) |  |

**Practitioner / PractitionerRole** (5)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`bobrester-bob`](../au-fhir-test-data-set/au-core/Practitioner-bobrester-bob.json) | [`bobrester-bob-gp`](../au-fhir-test-data-set/au-core/PractitionerRole-bobrester-bob-gp.json) | General Practitioner | [au-ps-ig-examples](#au-ps-ig-examples) |
| [`chau-fryer`](../au-fhir-test-data-set/au-core/Practitioner-chau-fryer.json) | [`surgeon-chau-fryer`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeon-chau-fryer.json) | Surgeon |  |
| [`mackay-darleen`](../au-fhir-test-data-set/au-core/Practitioner-mackay-darleen.json) | [`renalmedicine-mackay-darleen`](../au-fhir-test-data-set/au-core/PractitionerRole-renalmedicine-mackay-darleen.json) | Renal Medicine Specialist (Nephrology) |  |
| [`megan-peterson`](../au-fhir-test-data-set/au-core/Practitioner-megan-peterson.json) | [`pharmacist-megan-peterson`](../au-fhir-test-data-set/au-core/PractitionerRole-pharmacist-megan-peterson.json) | Pharmacist |  |
| [`sutherland-sallie`](../au-fhir-test-data-set/au-core/Practitioner-sutherland-sallie.json) | [`cardiologist-sutherland-sallie`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-sutherland-sallie.json) | Cardiologist (Cardiology) |  |

**HealthcareService** (2)

- [`murrabit-crisis-hotline`](../au-fhir-test-data-set/au-core/HealthcareService-murrabit-crisis-hotline.json)
- [`physiotherapy`](../au-fhir-test-data-set/au-core/HealthcareService-physiotherapy.json)

**Organization** (5)

- [`appin-pharmacy`](../au-fhir-test-data-set/au-core/Organization-appin-pharmacy.json)
- [`bobrester-medical-center`](../au-fhir-test-data-set/au-core/Organization-bobrester-medical-center.json)
- [`mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/Organization-mitchells-hill-audiology.json)
- [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json)
- [`pullabooka-pathology`](../au-fhir-test-data-set/au-core/Organization-pullabooka-pathology.json)

**Location** (2)

- [`bobrester-medical-center`](../au-fhir-test-data-set/au-core/Location-bobrester-medical-center.json)
- [`patient-home`](../au-fhir-test-data-set/au-core/Location-patient-home.json)

**Endpoint** (5)

- [`bobrester-fhir-rest`](../au-fhir-test-data-set/au-core/Endpoint-bobrester-fhir-rest.json)
- [`hl7au-dev-terminology-fhir-rest`](../au-fhir-test-data-set/au-core/Endpoint-hl7au-dev-terminology-fhir-rest.json)
- [`mh-audiology-smd`](../au-fhir-test-data-set/au-core/Endpoint-mh-audiology-smd.json)
- [`murrabit-hospital-hl7-v2-mllp`](../au-fhir-test-data-set/au-core/Endpoint-murrabit-hospital-hl7-v2-mllp.json)
- [`sparked-aucore-fhir-rest`](../au-fhir-test-data-set/au-core/Endpoint-sparked-aucore-fhir-rest.json)

**RelatedPerson** (2)

- [`banks-mia-leanne-father`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-mia-leanne-father.json) — *also in: [families](#families)*
- [`wang-li-friend`](../au-fhir-test-data-set/au-core/RelatedPerson-wang-li-friend.json)

<details><summary>5 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`bobrester-bob`](../au-fhir-test-data-set/au-core/Practitioner-bobrester-bob.json) | [`bobrester-bob-gp`](../au-fhir-test-data-set/au-core/PractitionerRole-bobrester-bob-gp.json) | [`bobrester-medical-center`](../au-fhir-test-data-set/au-core/Organization-bobrester-medical-center.json) |  |  |
| [`chau-fryer`](../au-fhir-test-data-set/au-core/Practitioner-chau-fryer.json) | [`surgeon-chau-fryer`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeon-chau-fryer.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json) | [`publicacute-murrabit-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json) |
| [`mackay-darleen`](../au-fhir-test-data-set/au-core/Practitioner-mackay-darleen.json) | [`renalmedicine-mackay-darleen`](../au-fhir-test-data-set/au-core/PractitionerRole-renalmedicine-mackay-darleen.json) |  |  |  |
| [`megan-peterson`](../au-fhir-test-data-set/au-core/Practitioner-megan-peterson.json) | [`pharmacist-megan-peterson`](../au-fhir-test-data-set/au-core/PractitionerRole-pharmacist-megan-peterson.json) | [`appin-pharmacy`](../au-fhir-test-data-set/au-core/Organization-appin-pharmacy.json) |  | [`communitypharmacy-appin-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-appin-pharmacy.json) |
| [`sutherland-sallie`](../au-fhir-test-data-set/au-core/Practitioner-sutherland-sallie.json) | [`cardiologist-sutherland-sallie`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-sutherland-sallie.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json) | [`publicacute-murrabit-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json) |

</details>

</details>


<details><summary>IG example resources matched nothing in the test data set — 2 possibly IG-only</summary>

| Example file | Resource | From a Bundle entry? |
| --- | --- | --- |
| `location-murrabit-hospital.xml` | `Location/murrabit-hospital` | no |
| `practitionerrole-nephrologist-darleen-mackay.xml` | `PractitionerRole/nephrologist-darleen-mackay` | no |

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
<details><summary>Derivation notes</summary>

> 16 distinct administrative entities are published as examples in hl7au/au-fhir-ps.
> 1 non-administrative entities excluded: Immunization x1. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.
> 155 of the resources scanned came from Bundle entries, matched on business identifier only — ids inside a Bundle are not reliable keys.
> 4 IG example resources matched nothing in the test data set; they may be IG-only examples. Listed below, under Members.

</details>


### Members (16)

**Patient** (5)

| ID | Also in |
| --- | --- |
| [`banks-jeramy-ezra`](../au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json) | *[sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |
| [`johnson-joyce`](../au-fhir-test-data-set/au-core/Patient-johnson-joyce.json) | *[sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`martin-shawn`](../au-fhir-test-data-set/au-core/Patient-martin-shawn.json) |  |
| [`morris-charlotte`](../au-fhir-test-data-set/au-core/Patient-morris-charlotte.json) | *[sparked-cdg-journeys](#sparked-cdg-journeys)* |

**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`bobrester-bob`](../au-fhir-test-data-set/au-core/Practitioner-bobrester-bob.json) | [`bobrester-bob-gp`](../au-fhir-test-data-set/au-core/PractitionerRole-bobrester-bob-gp.json) | General Practitioner | [au-core-ig-examples](#au-core-ig-examples) |
| [`burdett-palmer`](../au-fhir-test-data-set/au-core/Practitioner-burdett-palmer.json) | [`diagnostic-burdett-palmer`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-burdett-palmer.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`burrows-ginger`](../au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json) | [`generalpractitioner-burrows-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json) | General Practitioner (General medical practice) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`lowe-abe`](../au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json) | [`generalpractitioner-lowe-abe`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json) | General Practitioner (General medical practice) | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**Organization** (5)

- [`adv-hearing-care`](../au-fhir-test-data-set/au-core/Organization-adv-hearing-care.json)
- [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json)
- [`douglas-radiology`](../au-fhir-test-data-set/au-core/Organization-douglas-radiology.json)
- [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json)
- [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json)

<details><summary>3 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`burdett-palmer`](../au-fhir-test-data-set/au-core/Practitioner-burdett-palmer.json) | [`diagnostic-burdett-palmer`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-burdett-palmer.json) | [`douglas-radiology`](../au-fhir-test-data-set/au-core/Organization-douglas-radiology.json) | [`douglas-radiology`](../au-fhir-test-data-set/au-core/Location-douglas-radiology.json) | [`diagnosticimaging-douglas-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-douglas-radiology.json) |
| [`burrows-ginger`](../au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json) | [`generalpractitioner-burrows-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Location-bungabbee-medical-clinic.json) | [`generalpractice-bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-bungabbee-medical-clinic.json) |
| [`lowe-abe`](../au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json) | [`generalpractitioner-lowe-abe`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json) | [`generalmedical-mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json) |

</details>


<details><summary>IG example resources matched nothing in the test data set — 4 possibly IG-only</summary>

| Example file | Resource | From a Bundle entry? |
| --- | --- | --- |
| `Bundle-aups-basicsummary.xml` | `Practitioner/dce50472-2a94-47e6-9501-b52f0df0c813` | yes |
| `Bundle-aups-gpvisit-retrieval.xml` | `Location/None` | yes |
| `Bundle-aups-section-emptyreason.xml` | `Patient/9be88cc6-09e8-4dc6-b058-88676240dbc7` | yes |
| `Bundle-aups-section-emptyreason.xml` | `RelatedPerson/715076f4-007a-4c9d-beed-c155cc46f765` | yes |

</details>


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

**Read at:** [`68ea5951d9c3`](https://github.com/hl7au/au-fhir-erequesting/commit/68ea5951d9c3c36c178e1370da8c29f7b1257d4c) — the AU eRequesting IG revision this page was last generated from.
<details><summary>Derivation notes</summary>

> 16 distinct administrative entities are published as examples in hl7au/au-fhir-erequesting.
> 20 non-administrative entities excluded: ServiceRequest x8, CommunicationRequest x4, Coverage x2, Encounter x2, Consent x1, DocumentReference x1, Observation x1, Task x1. Subset identification covers administrative entities only; clinical content is retrievable from the administrative entity by FHIR mechanisms.
> 35 of the resources scanned came from Bundle entries, matched on business identifier only — ids inside a Bundle are not reliable keys.

</details>


### Members (16)

**Patient** (3)

- [`belger-remedios`](../au-fhir-test-data-set/au-erequesting/Patient-belger-remedios.json)
- [`roberts-fred`](../au-fhir-test-data-set/au-erequesting/Patient-roberts-fred.json) — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys)*
- [`scott-elijah-ken`](../au-fhir-test-data-set/au-erequesting/Patient-scott-elijah-ken.json)

**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`guthridge-jarred`](../au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json) | [`generalpractitioner-guthridge-jarred`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json) | General Practitioner (General medical practice) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`herbert-aimee`](../au-fhir-test-data-set/au-core/Practitioner-herbert-aimee.json) | [`pathologist-herbert-aimee`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-herbert-aimee.json) | Pathologist (Pathology) |  |
| [`losch-sallie`](../au-fhir-test-data-set/au-erequesting/Practitioner-losch-sallie.json) | [`obstetrician-losch-sallie`](../au-fhir-test-data-set/au-erequesting/PractitionerRole-obstetrician-losch-sallie.json) | Obstetrician and Gynaecologist (Obstetrics and gynaecology) |  |
| [`mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/Practitioner-mclaughlin-kimberlee.json) | [`diagnostic-mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mclaughlin-kimberlee.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |

**Organization** (4)

- [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json)
- [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json)
- [`kioma-pathology`](../au-fhir-test-data-set/au-core/Organization-kioma-pathology.json)
- [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Organization-mount-charlton-radiology.json)

**Location** (1)

- [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`guthridge-jarred`](../au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json) | [`generalpractitioner-guthridge-jarred`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Location-elimbah-medical-centre.json) | [`generalmedical-elimbah-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-elimbah-medical-centre.json) |
| [`herbert-aimee`](../au-fhir-test-data-set/au-core/Practitioner-herbert-aimee.json) | [`pathologist-herbert-aimee`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-herbert-aimee.json) | [`kioma-pathology`](../au-fhir-test-data-set/au-core/Organization-kioma-pathology.json) | [`kioma-pathology`](../au-fhir-test-data-set/au-core/Location-kioma-pathology.json) | [`pathologylaboratory-kioma-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kioma-pathology.json) |
| [`losch-sallie`](../au-fhir-test-data-set/au-erequesting/Practitioner-losch-sallie.json) | [`obstetrician-losch-sallie`](../au-fhir-test-data-set/au-erequesting/PractitionerRole-obstetrician-losch-sallie.json) |  |  |  |
| [`mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/Practitioner-mclaughlin-kimberlee.json) | [`diagnostic-mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mclaughlin-kimberlee.json) | [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Organization-mount-charlton-radiology.json) | [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Location-mount-charlton-radiology.json) | [`diagnosticimaging-mount-charlton-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mount-charlton-radiology.json) |

</details>


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

**Read at:** [`754d94714818`](https://github.com/hl7au/inferno_suite_generator/commit/754d947148181516cd48bfe5232659a8bf4b7573) — the Inferno test kit revision this page was last generated from.

### Members (7)

**Patient** (7)

| ID | Also in |
| --- | --- |
| [`baby-banks-john`](../au-fhir-test-data-set/au-core/Patient-baby-banks-john.json) | *[au-ps-test-patients](#au-ps-test-patients)* |
| [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-ig-examples](#au-ps-ig-examples), [au-ps-test-patients](#au-ps-test-patients)* |
| [`baratz-toni`](../au-fhir-test-data-set/au-core/Patient-baratz-toni.json) | *[au-ps-test-patients](#au-ps-test-patients)* |
| [`hayes-arianne`](../au-fhir-test-data-set/au-core/Patient-hayes-arianne.json) | *[au-ps-test-patients](#au-ps-test-patients)* |
| [`howe-deangelo`](../au-fhir-test-data-set/au-core/Patient-howe-deangelo.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-test-patients](#au-ps-test-patients)* |
| [`irvine-ronny-lawrence`](../au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-test-patients](#au-ps-test-patients)* |
| [`italia-sofia`](../au-fhir-test-data-set/au-core/Patient-italia-sofia.json) |  |


## AU Patient Summary test patients <a id="au-ps-test-patients"></a>

### Purpose

Identifies the primary test patients for AU Patient Summary testing — those for which the `$summary` operation can be invoked.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Relied on for `$summary` operation testing. Adding to or modifying these patients or their linked resources must preserve that coverage.

### Provenance & use

Declared by the AU PS Test Data Coverage page maintained by the project, rather than derived from the data set.

### Relationships

Six of the seven members are also [Inferno AU Core test suite default patients](#inferno-default-patients), so a change affecting one set very likely affects the other.

### How is this subset identified?

Declared. The patient list is transcribed from the AU PS Test Data Coverage page and recorded here; the page is re-read on each regeneration so that divergence can be reported.


**Source:** https://confluence.hl7.org/spaces/HAFWG/pages/404097954/AU+PS+Test+Data+Coverage

### Members (6)

**Patient** (6)

| ID | Also in |
| --- | --- |
| [`baby-banks-john`](../au-fhir-test-data-set/au-core/Patient-baby-banks-john.json) | *[inferno-default-patients](#inferno-default-patients)* |
| [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-ig-examples](#au-ps-ig-examples), [inferno-default-patients](#inferno-default-patients)* |
| [`baratz-toni`](../au-fhir-test-data-set/au-core/Patient-baratz-toni.json) | *[inferno-default-patients](#inferno-default-patients)* |
| [`hayes-arianne`](../au-fhir-test-data-set/au-core/Patient-hayes-arianne.json) | *[inferno-default-patients](#inferno-default-patients)* |
| [`howe-deangelo`](../au-fhir-test-data-set/au-core/Patient-howe-deangelo.json) | *[au-core-ig-examples](#au-core-ig-examples), [inferno-default-patients](#inferno-default-patients)* |
| [`irvine-ronny-lawrence`](../au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json) | *[au-core-ig-examples](#au-core-ig-examples), [inferno-default-patients](#inferno-default-patients)* |


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


### Members (1)

**Patient** (1)

- [`ballantyne-kelvin-hans`](../au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json) — *also in: [families](#families)*


## Sparked Clinical Design Group consumer journeys <a id="sparked-cdg-journeys"></a>

### Purpose

Identifies the entities used in Sparked Clinical Design Group consumer journeys, grouped by named journey.

### Ownership & governance

**Owner:** Shared between Sparked CDG and HL7 AU Test Data project — TBC.  
Journey membership does not itself reserve an entity. It does not follow that a journey entity is free to build on — some are also published IG examples, which that subset reserves. What governs an entity is the tightest constraint across all of its memberships, so check its other listings and with the data subset owners before adding to it.

### Provenance & use

Administrative entities are derived from Services Australia provided data. An entity used in a journey may also appear in the corresponding IG project use cases and be progressed into technical use cases and subsequently, the IG examples. Members are recorded as resolved resource ids rather than display names so membership is unambiguous.

### Relationships

Several members also appear in [Scenario groupings](#scenario-groups), and some are [AU Patient Summary IG example entities](#au-ps-ig-examples).

### How is this subset identified?

Curated. Journey membership is stated by Sparked and recorded in the facts file; the AU Encounter Records journey additionally records each participant's stated journey role alongside the specialty declared by their PractitionerRole, because the two can differ.


### Members (66)

<details><summary><strong>AU Encounter Records</strong> (4 journeys, 60 entities)</summary>

<blockquote>
<details><summary><strong>encounter-journey-1-routine-care-and-unplanned-events</strong> (12 entities)</summary>


**Patient** (1)

- [`roberts-fred`](../au-fhir-test-data-set/au-erequesting/Patient-roberts-fred.json) — **Patient** — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*

**Practitioner / PractitionerRole** (9)


| Practitioner | PractitionerRole | Role from journey | Role (specialty) from test data | Notes | Also in |
| --- | --- | --- | --- | --- | --- |
| [`cox-sandra`](../au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json) | [`cox-sandra`](../au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json) | **Registered Nurse** | Registered Nurses nec (Nursing) |  | *[scenario-groups](#scenario-groups)* |
| [`dawson-kent`](../au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json) | [`dawson-kent`](../au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json) | **ED Doctor** | Emergency Medicine Specialist / Emergency Physician (Emergency medicine) |  | *[scenario-groups](#scenario-groups)* |
| [`ellison-abby`](../au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json) | [`ellison-abby`](../au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json) | **ED Physiotherapist** | Physiotherapist (Physiotherapy) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`frank-gaylene`](../au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json) | [`frank-gaylene`](../au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json) | **Nurse Practitioner** | Nurse Practitioner (Nursing) |  | *[scenario-groups](#scenario-groups)* |
| [`gilmore-dane`](../au-fhir-test-data-set/au-core/Practitioner-gilmore-dane.json) | [`ambulanceofficer-gilmore-dane`](../au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-gilmore-dane.json) | **Paramedic** | Ambulance Officer | *journey role may differ from the declared specialty* |  |
| [`little-jerrie`](../au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json) | [`little-jerrie`](../au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json) | **General Practitioner** | General Practitioner (General medical practice) |  | *[scenario-groups](#scenario-groups)* |
| [`neville-isaiah`](../au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json) | [`neville-isaiah`](../au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json) | **Physiotherapist** | Physiotherapist (Physiotherapy) |  | *[scenario-groups](#scenario-groups)* |
| [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json) | [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json) | **Pharmacist** | Pharmacist (Community pharmacy) |  | *[scenario-groups](#scenario-groups)* |
| [`shephard-lizabeth`](../au-fhir-test-data-set/au-core/Practitioner-shephard-lizabeth.json) | [`registerednurses-shephard-lizabeth`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shephard-lizabeth.json) | **ED Triage Nurse** | Registered Nurses nec (Nursing) | *journey role may differ from the declared specialty* |  |

**Unresolved** (2)

- `roberts-nancy` — _(no resource)_ — **Fred's wife** — *no matching resource in the data set*
- `smith-joe` — _(no resource)_ — **Emergency Dispatcher** — *no matching resource in the data set*

<details><summary>9 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`cox-sandra`](../au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json) | [`cox-sandra`](../au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json) | [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) |  |  |
| [`dawson-kent`](../au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json) | [`dawson-kent`](../au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json) | [`parramatta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json) |  |  |
| [`ellison-abby`](../au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json) | [`ellison-abby`](../au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`frank-gaylene`](../au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json) | [`frank-gaylene`](../au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |  |
| [`gilmore-dane`](../au-fhir-test-data-set/au-core/Practitioner-gilmore-dane.json) | [`ambulanceofficer-gilmore-dane`](../au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-gilmore-dane.json) |  |  |  |
| [`little-jerrie`](../au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json) | [`little-jerrie`](../au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json) | [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) |  |  |
| [`neville-isaiah`](../au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json) | [`neville-isaiah`](../au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json) | [`westmead-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json) |  |  |
| [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json) | [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json) | [`westmead-pharmacy`](../au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json) |  |  |
| [`shephard-lizabeth`](../au-fhir-test-data-set/au-core/Practitioner-shephard-lizabeth.json) | [`registerednurses-shephard-lizabeth`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shephard-lizabeth.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Location-kensington-public-hospital.json) | [`publicacute-kensington-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-kensington-public-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>encounter-journey-2-chemotherapy-hith-allied-health</strong> (14 entities)</summary>


**Patient** (1)

- [`sandilands-kendall`](../au-fhir-test-data-set/au-erequesting/Patient-sandilands-kendall.json) — **Patient**

**Practitioner / PractitionerRole** (10)


| Practitioner | PractitionerRole | Role from journey | Role (specialty) from test data | Notes | Also in |
| --- | --- | --- | --- | --- | --- |
| [`gordon-tad`](../au-fhir-test-data-set/au-core/Practitioner-gordon-tad.json) | [`complementaryhealth-gordon-tad`](../au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-gordon-tad.json) | **Exercise Physiologist** | Exercise Physiologist (Exercise physiology service) |  |  |
| [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json) | [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json) | **Inpatient Psychologist** | Clinical Psychologist (Clinical psychology) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`levings-richard`](../au-fhir-test-data-set/au-core/Practitioner-levings-richard.json) | [`levings-richard`](../au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json) | **Outpatient Dietitian** | Dietitian (Dietetics and nutrition) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`lowe-abe`](../au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json) | [`generalpractitioner-lowe-abe`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json) | **General Practitioner (GP)** | General Practitioner (General medical practice) |  | *[au-ps-ig-examples](#au-ps-ig-examples)* |
| [`mcnab-angelina`](../au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json) | [`mcnab-angelina`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json) | **Inpatient Dietitian** | Dietitian (Dietetics and nutrition) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`mills-hope`](../au-fhir-test-data-set/au-core/Practitioner-mills-hope.json) | [`mills-hope`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json) | **Occupational Therapist (OT)** | Occupational Therapist |  | *[scenario-groups](#scenario-groups)* |
| [`roberts-benjamin`](../au-fhir-test-data-set/au-core/Practitioner-roberts-benjamin.json) | [`registerednurses-roberts-benjamin`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-roberts-benjamin.json) | **Specialist Cancer Nurse** | Registered Nurses nec (Nursing) | *journey role may differ from the declared specialty* |  |
| [`sheppard-mathew`](../au-fhir-test-data-set/au-core/Practitioner-sheppard-mathew.json) | [`medicaloncologist-sheppard-mathew`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-sheppard-mathew.json) | **Medical Oncologist** | Medical Oncologist (Medical oncology) |  |  |
| [`taylor-kittie`](../au-fhir-test-data-set/au-core/Practitioner-taylor-kittie.json) | [`registerednurses-taylor-kittie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-taylor-kittie.json) | **Day Therapy Unit Nurse** | Registered Nurses nec (Nursing) | *journey role may differ from the declared specialty* |  |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | **Private Psychologist** | Clinical Psychologist (Clinical psychology) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |

**Unresolved** (3)

- `cedric-lowe-friend` — _(no resource)_ — **Kendall's friend** — *no matching resource in the data set*
- `hith-team` — _(no resource)_ — **Hospital-In-The-Home (HITH) team** — *no matching resource in the data set*
- `medical-oncology-team` — _(no resource)_ — **Medical Oncology Team** — *no matching resource in the data set*

<details><summary>10 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`gordon-tad`](../au-fhir-test-data-set/au-core/Practitioner-gordon-tad.json) | [`complementaryhealth-gordon-tad`](../au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-gordon-tad.json) |  |  |  |
| [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json) | [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |  |
| [`levings-richard`](../au-fhir-test-data-set/au-core/Practitioner-levings-richard.json) | [`levings-richard`](../au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json) | [`garran-nutrition`](../au-fhir-test-data-set/au-core/Organization-garran-nutrition.json) |  |  |
| [`lowe-abe`](../au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json) | [`generalpractitioner-lowe-abe`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json) | [`generalmedical-mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json) |
| [`mcnab-angelina`](../au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json) | [`mcnab-angelina`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json) | [`parramatta-nutrition`](../au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json) |  |  |
| [`mills-hope`](../au-fhir-test-data-set/au-core/Practitioner-mills-hope.json) | [`mills-hope`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`roberts-benjamin`](../au-fhir-test-data-set/au-core/Practitioner-roberts-benjamin.json) | [`registerednurses-roberts-benjamin`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-roberts-benjamin.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json) | [`generalmedical-mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json) |
| [`sheppard-mathew`](../au-fhir-test-data-set/au-core/Practitioner-sheppard-mathew.json) | [`medicaloncologist-sheppard-mathew`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-sheppard-mathew.json) |  |  |  |
| [`taylor-kittie`](../au-fhir-test-data-set/au-core/Practitioner-taylor-kittie.json) | [`registerednurses-taylor-kittie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-taylor-kittie.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Organization-wallendbeen-aged-care.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Location-wallendbeen-aged-care.json) | [`privateprofit-wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-wallendbeen-aged-care.json) |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>encounter-journey-3-child-with-developmental-delay</strong> (10 entities)</summary>


**Practitioner / PractitionerRole** (7)


| Practitioner | PractitionerRole | Role from journey | Role (specialty) from test data | Notes | Also in |
| --- | --- | --- | --- | --- | --- |
| [`alcock-devon`](../au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json) | [`alcock-devon`](../au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json) | **Maternal and Child Health Nurse** | Registered Nurses nec (Nursing) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`bradley-jill`](../au-fhir-test-data-set/au-core/Practitioner-bradley-jill.json) | [`audiologist-bradley-jill`](../au-fhir-test-data-set/au-core/PractitionerRole-audiologist-bradley-jill.json) | **Audiologist** | Audiologist (Audiological medicine) |  |  |
| [`greene-delores`](../au-fhir-test-data-set/au-core/Practitioner-greene-delores.json) | [`greene-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json) | **Paediatrician** | Paediatrician (General paediatric specialty) |  | *[scenario-groups](#scenario-groups)* |
| [`keith-margot`](../au-fhir-test-data-set/au-core/Practitioner-keith-margot.json) | [`keith-margot`](../au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json) | **General Practitioner** | General Practitioner (General medical practice) |  | *[scenario-groups](#scenario-groups)* |
| [`mullin-kenny`](../au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json) | [`mullin-kenny`](../au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json) | **Speech Pathologist** | Speech Pathologist |  | *[scenario-groups](#scenario-groups)* |
| [`murray-ashli`](../au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json) | [`murray-ashli`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json) | **Occupational Therapist** | Occupational Therapist |  | *[scenario-groups](#scenario-groups)* |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | **Private Psychologist** | Clinical Psychologist (Clinical psychology) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |

**Unresolved** (3)

- `smith-heather` — _(no resource)_ — **Noah's Mother** — *no matching resource in the data set*
- `smith-noah` — _(no resource)_ — **Patient (age 3 years 6 months)** — *no matching resource in the data set*
- `smith-shaun` — _(no resource)_ — **Noah's Father** — *no matching resource in the data set*

<details><summary>7 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`alcock-devon`](../au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json) | [`alcock-devon`](../au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |
| [`bradley-jill`](../au-fhir-test-data-set/au-core/Practitioner-bradley-jill.json) | [`audiologist-bradley-jill`](../au-fhir-test-data-set/au-core/PractitionerRole-audiologist-bradley-jill.json) | [`adv-hearing-care`](../au-fhir-test-data-set/au-core/Organization-adv-hearing-care.json) |  |
| [`greene-delores`](../au-fhir-test-data-set/au-core/Practitioner-greene-delores.json) | [`greene-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |
| [`keith-margot`](../au-fhir-test-data-set/au-core/Practitioner-keith-margot.json) | [`keith-margot`](../au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |
| [`mullin-kenny`](../au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json) | [`mullin-kenny`](../au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json) | [`southbank-speech-pathology`](../au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json) |  |
| [`murray-ashli`](../au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json) | [`murray-ashli`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json) | [`st-kilda-ot-services`](../au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json) |  |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>encounter-journey-4-independent-living-admission-and-transition-care</strong> (26 entities)</summary>


**Patient** (1)

- [`boulton-annika`](../au-fhir-test-data-set/au-core/Patient-boulton-annika.json) — **Patient**

**Practitioner / PractitionerRole** (17)


| Practitioner | PractitionerRole | Role from journey | Role (specialty) from test data | Notes | Also in |
| --- | --- | --- | --- | --- | --- |
| [`bailey-buck`](../au-fhir-test-data-set/au-core/Practitioner-bailey-buck.json) | [`bailey-buck`](../au-fhir-test-data-set/au-core/PractitionerRole-bailey-buck.json) | **Inpatient Social worker** | Social Worker | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`barrett-kirstie`](../au-fhir-test-data-set/au-core/Practitioner-barrett-kirstie.json) | [`barrett-kirstie`](../au-fhir-test-data-set/au-core/PractitionerRole-barrett-kirstie.json) | **TCP social worker** | Social Worker | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`berridge-beulah`](../au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json) | [`berridge-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json) | **Anaesthetist** | Anaesthetist (Anaesthetics) |  | *[scenario-groups](#scenario-groups)* |
| [`gilmore-dane`](../au-fhir-test-data-set/au-core/Practitioner-gilmore-dane.json) | [`ambulanceofficer-gilmore-dane`](../au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-gilmore-dane.json) | **Paramedic** | Ambulance Officer | *journey role may differ from the declared specialty* |  |
| [`guthridge-jarred`](../au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json) | [`generalpractitioner-guthridge-jarred`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json) | **General Practitioner (GP)** | General Practitioner (General medical practice) |  | *[au-erequesting-ig-examples](#au-erequesting-ig-examples)* |
| [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/Practitioner-hipwood-fatimah.json) | [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/PractitionerRole-hipwood-fatimah.json) | **TCP OT** | Occupational Therapist | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`hobden-mark`](../au-fhir-test-data-set/au-core/Practitioner-hobden-mark.json) | [`hobden-mark`](../au-fhir-test-data-set/au-core/PractitionerRole-hobden-mark.json) | **Inpatient Pharmacist** | Pharmacist (Community pharmacy) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`jeffery-sammy`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json) | [`jeffery-sammy`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json) | **Inpatient Physiotherapist** | Physiotherapist (Physiotherapy) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`kelly-virginia`](../au-fhir-test-data-set/au-core/Practitioner-kelly-virginia.json) | [`dietitian-kelly-virginia`](../au-fhir-test-data-set/au-core/PractitionerRole-dietitian-kelly-virginia.json) | **Inpatient Dietitian** | Dietitian (Dietetics and nutrition) | *journey role may differ from the declared specialty* |  |
| [`knowles-sunshine`](../au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json) | [`knowles-sunshine`](../au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json) | **Community Occupational Therapist** | Occupational Therapist | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/Practitioner-livingstone-yvonne.json) | [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/PractitionerRole-livingstone-yvonne.json) | **TCP Physiotherapist** | Physiotherapist (Physiotherapy) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`parker-elijah`](../au-fhir-test-data-set/au-core/Practitioner-parker-elijah.json) | [`physiotherapist-parker-elijah`](../au-fhir-test-data-set/au-core/PractitionerRole-physiotherapist-parker-elijah.json) | **Community physiotherapist** | Physiotherapist (Physiotherapy) | *journey role may differ from the declared specialty* |  |
| [`patrick-manual`](../au-fhir-test-data-set/au-core/Practitioner-patrick-manual.json) | [`retailpharmacist-patrick-manual`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-patrick-manual.json) | **Community pharmacist** | Retail Pharmacist (Community pharmacy) |  |  |
| [`randall-anthony`](../au-fhir-test-data-set/au-core/Practitioner-randall-anthony.json) | [`randall-anthony`](../au-fhir-test-data-set/au-core/PractitionerRole-randall-anthony.json) | **Practice nurse** | Registered Nurses nec (Nursing) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/Practitioner-robbins-wilhelmina.json) | [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/PractitionerRole-robbins-wilhelmina.json) | **Transition Care Program (TCP) Nurse** | Nurse Practitioner (Nursing) | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |
| [`rowland-roger`](../au-fhir-test-data-set/au-core/Practitioner-rowland-roger.json) | [`registerednurses-rowland-roger`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-rowland-roger.json) | **Surgical ward nurse** | Registered Nurses nec (Nursing) | *journey role may differ from the declared specialty* |  |
| [`sherry-dean`](../au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json) | [`sherry-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json) | **Inpatient Occupational Therapist (OT)** | Occupational Therapist | *journey role may differ from the declared specialty* | *[scenario-groups](#scenario-groups)* |

**Unresolved** (8)

| ID | Role | Note |
| --- | --- | --- |
| `acat-team` | **Aged Care Assessment Team (ACAT)** | *no matching resource in the data set* |
| `boulton-sophie` | **Annika's Daughter** | *no matching resource in the data set* |
| `donnelly-claire` | **TCP Allied Health Assistant** | *no matching resource in the data set* |
| `ed-team` | **Emergency Department team** | *no matching resource in the data set* |
| `geriatrics-team` | **Geriatrics team** | *no matching resource in the data set* |
| `orthopaedic-team` | **Orthopaedic team** | *no matching resource in the data set* |
| `pain-team` | **Pain team** | *no matching resource in the data set* |
| `radiology-team` | **Radiology team** | *no matching resource in the data set* |

<details><summary>17 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`bailey-buck`](../au-fhir-test-data-set/au-core/Practitioner-bailey-buck.json) | [`bailey-buck`](../au-fhir-test-data-set/au-core/PractitionerRole-bailey-buck.json) | [`townsville-public-hospital`](../au-fhir-test-data-set/au-core/Organization-townsville-public-hospital.json) |  |  |
| [`barrett-kirstie`](../au-fhir-test-data-set/au-core/Practitioner-barrett-kirstie.json) | [`barrett-kirstie`](../au-fhir-test-data-set/au-core/PractitionerRole-barrett-kirstie.json) | [`mt-isa-community-health`](../au-fhir-test-data-set/au-core/Organization-mt-isa-community-health.json) |  |  |
| [`berridge-beulah`](../au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json) | [`berridge-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |  |
| [`gilmore-dane`](../au-fhir-test-data-set/au-core/Practitioner-gilmore-dane.json) | [`ambulanceofficer-gilmore-dane`](../au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-gilmore-dane.json) |  |  |  |
| [`guthridge-jarred`](../au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json) | [`generalpractitioner-guthridge-jarred`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Location-elimbah-medical-centre.json) | [`generalmedical-elimbah-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-elimbah-medical-centre.json) |
| [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/Practitioner-hipwood-fatimah.json) | [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/PractitionerRole-hipwood-fatimah.json) | [`mt-isa-ot-services`](../au-fhir-test-data-set/au-core/Organization-mt-isa-ot-services.json) |  |  |
| [`hobden-mark`](../au-fhir-test-data-set/au-core/Practitioner-hobden-mark.json) | [`hobden-mark`](../au-fhir-test-data-set/au-core/PractitionerRole-hobden-mark.json) | [`camooweal-pharmacy`](../au-fhir-test-data-set/au-core/Organization-camooweal-pharmacy.json) |  |  |
| [`jeffery-sammy`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json) | [`jeffery-sammy`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |  |
| [`kelly-virginia`](../au-fhir-test-data-set/au-core/Practitioner-kelly-virginia.json) | [`dietitian-kelly-virginia`](../au-fhir-test-data-set/au-core/PractitionerRole-dietitian-kelly-virginia.json) |  |  |  |
| [`knowles-sunshine`](../au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json) | [`knowles-sunshine`](../au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json) | [`westmead-ot-services`](../au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json) |  |  |
| [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/Practitioner-livingstone-yvonne.json) | [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/PractitionerRole-livingstone-yvonne.json) | [`mt-isa-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-mt-isa-physiotherapy.json) |  |  |
| [`parker-elijah`](../au-fhir-test-data-set/au-core/Practitioner-parker-elijah.json) | [`physiotherapist-parker-elijah`](../au-fhir-test-data-set/au-core/PractitionerRole-physiotherapist-parker-elijah.json) |  |  |  |
| [`patrick-manual`](../au-fhir-test-data-set/au-core/Practitioner-patrick-manual.json) | [`retailpharmacist-patrick-manual`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-patrick-manual.json) | [`cracow-pharmacy`](../au-fhir-test-data-set/au-core/Organization-cracow-pharmacy.json) | [`cracow-pharmacy`](../au-fhir-test-data-set/au-core/Location-cracow-pharmacy.json) | [`communitypharmacy-cracow-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-cracow-pharmacy.json) |
| [`randall-anthony`](../au-fhir-test-data-set/au-core/Practitioner-randall-anthony.json) | [`randall-anthony`](../au-fhir-test-data-set/au-core/PractitionerRole-randall-anthony.json) | [`mt-isa-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-medical-clinic.json) |  |  |
| [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/Practitioner-robbins-wilhelmina.json) | [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/PractitionerRole-robbins-wilhelmina.json) | [`camooweal-community-health`](../au-fhir-test-data-set/au-core/Organization-camooweal-community-health.json) |  |  |
| [`rowland-roger`](../au-fhir-test-data-set/au-core/Practitioner-rowland-roger.json) | [`registerednurses-rowland-roger`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-rowland-roger.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Organization-glennie-heights-public-hospital.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Location-glennie-heights-public-hospital.json) | [`publicacute-glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-glennie-heights-public-hospital.json) |
| [`sherry-dean`](../au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json) | [`sherry-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |  |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>AU Patient Summary</strong> (5 journeys, 6 entities)</summary>

<blockquote>
<details><summary><strong>emergency-hospital-attendance</strong> (1 entity)</summary>


**Patient** (1)

- [`morris-charlotte`](../au-fhir-test-data-set/au-core/Patient-morris-charlotte.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>hospital-to-aged-care-interstate-transfer</strong> (1 entity)</summary>


**Patient** (1)

- [`nielsen-eleanore`](../au-fhir-test-data-set/au-core/Patient-nielsen-eleanore.json)

</details>
</blockquote>

<blockquote>
<details><summary><strong>interstate-gp-visit</strong> (1 entity)</summary>


**Patient** (1)

- [`banks-jeramy-ezra`](../au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>pre-operative-surgical</strong> (1 entity)</summary>


**Patient** (1)

- [`simpson-tristan`](../au-fhir-test-data-set/au-core/Patient-simpson-tristan.json)

</details>
</blockquote>

<blockquote>
<details><summary><strong>referral-to-specialist-and-allied-health</strong> (2 entities)</summary>


**Patient** (1)

- [`johnson-joyce`](../au-fhir-test-data-set/au-core/Patient-johnson-joyce.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*

**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role from journey | Role (specialty) from test data | Notes | Also in |
| --- | --- | --- | --- | --- | --- |
| [`burrows-ginger`](../au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json) | [`generalpractitioner-burrows-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json) |  | General Practitioner (General medical practice) |  | *[au-ps-ig-examples](#au-ps-ig-examples)* |

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`burrows-ginger`](../au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json) | [`generalpractitioner-burrows-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Location-bungabbee-medical-clinic.json) | [`generalpractice-bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-bungabbee-medical-clinic.json) |

</details>

</details>
</blockquote>

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

### Members (95)

<details><summary><strong>Alex's Story</strong> (38 entities)</summary>

**Patient** (1)

- [`thompson-alex`](../au-fhir-test-data-set/connected-care/Patient-thompson-alex.json)

**Practitioner / PractitionerRole** (8)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`chen-emily`](../au-fhir-test-data-set/connected-care/Practitioner-chen-emily.json) | [`obstetrician-chen-emily`](../au-fhir-test-data-set/connected-care/PractitionerRole-obstetrician-chen-emily.json) | Obstetrician and Gynaecologist (Obstetrics and gynaecology) |  |
| [`evans-sarah`](../au-fhir-test-data-set/connected-care/Practitioner-evans-sarah.json) | [`physiotherapist-evans-sarah`](../au-fhir-test-data-set/connected-care/PractitionerRole-physiotherapist-evans-sarah.json) | Physiotherapist (Physiotherapy) |  |
| [`johnson-sally`](../au-fhir-test-data-set/connected-care/Practitioner-johnson-sally.json) | [`medicaltechnician-johnson-sally`](../au-fhir-test-data-set/connected-care/PractitionerRole-medicaltechnician-johnson-sally.json) | Medical Technician |  |
| [`lee-chris`](../au-fhir-test-data-set/connected-care/Practitioner-lee-chris.json) | [`generalpractitioner-lee-chris`](../au-fhir-test-data-set/connected-care/PractitionerRole-generalpractitioner-lee-chris.json) | General Practitioner (General medical practice) |  |
| [`lee-sarah`](../au-fhir-test-data-set/connected-care/Practitioner-lee-sarah.json) | [`retailpharmacist-lee-sarah`](../au-fhir-test-data-set/connected-care/PractitionerRole-retailpharmacist-lee-sarah.json) | Pharmacist (Community pharmacy) |  |
| [`patel-rachel`](../au-fhir-test-data-set/connected-care/Practitioner-patel-rachel.json) | [`counsellorsnec-patel-rachel`](../au-fhir-test-data-set/connected-care/PractitionerRole-counsellorsnec-patel-rachel.json) | Counsellor |  |
| [`smith-jane`](../au-fhir-test-data-set/connected-care/Practitioner-smith-jane.json) | [`generalpractitioner-smith-jane`](../au-fhir-test-data-set/connected-care/PractitionerRole-generalpractitioner-smith-jane.json) | General Practitioner (General medical practice) |  |
| [`wilson-mark`](../au-fhir-test-data-set/connected-care/Practitioner-wilson-mark.json) | [`obstetrician-wilson-mark`](../au-fhir-test-data-set/connected-care/PractitionerRole-obstetrician-wilson-mark.json) | Reproductive Endocrinologist/Infertility Specialist (Reproductive Endocrinologist/Infertility Specialist) |  |

**HealthcareService** (7)

- [`clinicalpsychology-bathurst-psychology`](../au-fhir-test-data-set/connected-care/HealthcareService-clinicalpsychology-bathurst-psychology.json)
- [`communitypharmacy-bathurst-community-pharmacy`](../au-fhir-test-data-set/connected-care/HealthcareService-communitypharmacy-bathurst-community-pharmacy.json)
- [`generalmedical-bathurst-medical-centre`](../au-fhir-test-data-set/connected-care/HealthcareService-generalmedical-bathurst-medical-centre.json)
- [`pathologylaboratory-bathurst-pathology`](../au-fhir-test-data-set/connected-care/HealthcareService-pathologylaboratory-bathurst-pathology.json)
- [`physiotherapyservices-bathurst-physio-centre`](../au-fhir-test-data-set/connected-care/HealthcareService-physiotherapyservices-bathurst-physio-centre.json)
- [`privateacute-ashfield-private-hospital`](../au-fhir-test-data-set/connected-care/HealthcareService-privateacute-ashfield-private-hospital.json)
- [`specialistmedical-ashfield-private-clinic`](../au-fhir-test-data-set/connected-care/HealthcareService-specialistmedical-ashfield-private-clinic.json)

**Organization** (7)

- [`ashfield-private-clinic`](../au-fhir-test-data-set/connected-care/Organization-ashfield-private-clinic.json)
- [`ashfield-private-hospital`](../au-fhir-test-data-set/connected-care/Organization-ashfield-private-hospital.json)
- [`bathurst-community-pharmacy`](../au-fhir-test-data-set/connected-care/Organization-bathurst-community-pharmacy.json)
- [`bathurst-medical-centre`](../au-fhir-test-data-set/connected-care/Organization-bathurst-medical-centre.json)
- [`bathurst-pathology`](../au-fhir-test-data-set/connected-care/Organization-bathurst-pathology.json)
- [`bathurst-physio-centre`](../au-fhir-test-data-set/connected-care/Organization-bathurst-physio-centre.json)
- [`bathurst-psychology`](../au-fhir-test-data-set/connected-care/Organization-bathurst-psychology.json)

**Location** (7)

- [`ashfield-private-clinic`](../au-fhir-test-data-set/connected-care/Location-ashfield-private-clinic.json)
- [`ashfield-private-hospital`](../au-fhir-test-data-set/connected-care/Location-ashfield-private-hospital.json)
- [`bathurst-community-pharmacy`](../au-fhir-test-data-set/connected-care/Location-bathurst-community-pharmacy.json)
- [`bathurst-medical-centre`](../au-fhir-test-data-set/connected-care/Location-bathurst-medical-centre.json)
- [`bathurst-pathology`](../au-fhir-test-data-set/connected-care/Location-bathurst-pathology.json)
- [`bathurst-physio-centre`](../au-fhir-test-data-set/connected-care/Location-bathurst-physio-centre.json)
- [`bathurst-psychology`](../au-fhir-test-data-set/connected-care/Location-bathurst-psychology.json)

<details><summary>8 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| `chen-emily` | `obstetrician-chen-emily` | `ashfield-private-clinic` | `ashfield-private-clinic` |
| `evans-sarah` | `physiotherapist-evans-sarah` | `bathurst-physio-centre` | `bathurst-physio-centre` |
| `johnson-sally` | `medicaltechnician-johnson-sally` | `bathurst-pathology` | `bathurst-pathology` |
| `lee-chris` | `generalpractitioner-lee-chris` | `bathurst-medical-centre` | `bathurst-medical-centre` |
| `lee-sarah` | `retailpharmacist-lee-sarah` | `bathurst-community-pharmacy` | `bathurst-community-pharmacy` |
| `patel-rachel` | `counsellorsnec-patel-rachel` | `bathurst-psychology` | `bathurst-psychology` |
| `smith-jane` | `generalpractitioner-smith-jane` | `bathurst-medical-centre` | `bathurst-medical-centre` |
| `wilson-mark` | `obstetrician-wilson-mark` | `ashfield-private-hospital` | `ashfield-private-hospital` |

</details>

</details>

<details><summary><strong>Yuri's Story (provisional)</strong> (57 entities)</summary>

**Patient** (1)

- [`petrov-yuri`](../au-fhir-test-data-set/connected-care/Patient-petrov-yuri.json)

**Practitioner / PractitionerRole** (12)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`bradley-tom`](../au-fhir-test-data-set/connected-care/Practitioner-bradley-tom.json) | [`ambulanceofficer-bradley-tom`](../au-fhir-test-data-set/connected-care/PractitionerRole-ambulanceofficer-bradley-tom.json) | Intensive Care Ambulance Paramedic |  |
| [`brown-sarah`](../au-fhir-test-data-set/connected-care/Practitioner-brown-sarah.json) | [`nursepractitioner-brown-sarah`](../au-fhir-test-data-set/connected-care/PractitionerRole-nursepractitioner-brown-sarah.json) | Nurse Practitioner (Nursing) |  |
| [`green-susan`](../au-fhir-test-data-set/connected-care/Practitioner-green-susan.json) | [`emergencymedicinespecialist-green-susan-garran-hospital`](../au-fhir-test-data-set/connected-care/PractitionerRole-emergencymedicinespecialist-green-susan-garran-hospital.json) | Emergency Medicine Specialist/Emergency Physician (Emergency medicine) |  |
| [`green-susan`](../au-fhir-test-data-set/connected-care/Practitioner-green-susan.json) | [`emergencymedicinespecialist-green-susan-garran-hospital-ed`](../au-fhir-test-data-set/connected-care/PractitionerRole-emergencymedicinespecialist-green-susan-garran-hospital-ed.json) | Emergency Medicine Specialist/Emergency Physician (Emergency medicine) |  |
| [`hayes-linda`](../au-fhir-test-data-set/connected-care/Practitioner-hayes-linda.json) | [`nursepractitioner-hayes-linda`](../au-fhir-test-data-set/connected-care/PractitionerRole-nursepractitioner-hayes-linda.json) | Nurse Practitioner (Nursing) |  |
| [`king-narelle`](../au-fhir-test-data-set/connected-care/Practitioner-king-narelle.json) | [`aboriginal-king-narelle`](../au-fhir-test-data-set/connected-care/PractitionerRole-aboriginal-king-narelle.json) | Aboriginal and Torres Strait Health Worker |  |
| [`kumar-ravi`](../au-fhir-test-data-set/connected-care/Practitioner-kumar-ravi.json) | [`generalpractitioner-kumar-ravi`](../au-fhir-test-data-set/connected-care/PractitionerRole-generalpractitioner-kumar-ravi.json) | General Practitioner (General medical practice) |  |
| [`mitchell-karen`](../au-fhir-test-data-set/connected-care/Practitioner-mitchell-karen.json) | [`socialworker-mitchell-karen`](../au-fhir-test-data-set/connected-care/PractitionerRole-socialworker-mitchell-karen.json) | Social Worker |  |
| [`smith-john`](../au-fhir-test-data-set/connected-care/Practitioner-smith-john.json) | [`physiotherapist-smith-john`](../au-fhir-test-data-set/connected-care/PractitionerRole-physiotherapist-smith-john.json) | Physiotherapist (Physiotherapy) |  |
| [`sullivan-joy`](../au-fhir-test-data-set/connected-care/Practitioner-sullivan-joy.json) | [`retailpharmacist-sullivan-joy`](../au-fhir-test-data-set/connected-care/PractitionerRole-retailpharmacist-sullivan-joy.json) | Pharmacist (Community pharmacy) |  |
| [`tench-natalie`](../au-fhir-test-data-set/connected-care/Practitioner-tench-natalie.json) | [`endocrinologist-tench-natalie`](../au-fhir-test-data-set/connected-care/PractitionerRole-endocrinologist-tench-natalie.json) | Endocrinologist (Endocrinology) |  |
| [`wong-lisa`](../au-fhir-test-data-set/connected-care/Practitioner-wong-lisa.json) | [`occupationaltherapist-wong-lisa`](../au-fhir-test-data-set/connected-care/PractitionerRole-occupationaltherapist-wong-lisa.json) | Occupational Therapist (Occupational medicine) |  |

**HealthcareService** (11)

- [`agedcare-aged-care-home-help`](../au-fhir-test-data-set/connected-care/HealthcareService-agedcare-aged-care-home-help.json)
- [`ambulanceservice-garran-ambulance-service`](../au-fhir-test-data-set/connected-care/HealthcareService-ambulanceservice-garran-ambulance-service.json)
- [`communitypharmacy-kalgoorlie-pharmacy`](../au-fhir-test-data-set/connected-care/HealthcareService-communitypharmacy-kalgoorlie-pharmacy.json)
- [`generalhospital-garran-hospital-ed`](../au-fhir-test-data-set/connected-care/HealthcareService-generalhospital-garran-hospital-ed.json)
- [`generalmedical-kalgoorlie-medical-centre`](../au-fhir-test-data-set/connected-care/HealthcareService-generalmedical-kalgoorlie-medical-centre.json)
- [`healthcareservice-kalgoorlie-aged-care-service`](../au-fhir-test-data-set/connected-care/HealthcareService-healthcareservice-kalgoorlie-aged-care-service.json)
- [`occupationaltherapy-kalgoorlie-ot-services`](../au-fhir-test-data-set/connected-care/HealthcareService-occupationaltherapy-kalgoorlie-ot-services.json)
- [`physiotherapyservices-kalgoorlie-physiotherapy`](../au-fhir-test-data-set/connected-care/HealthcareService-physiotherapyservices-kalgoorlie-physiotherapy.json)
- [`publicacute-garran-hospital`](../au-fhir-test-data-set/connected-care/HealthcareService-publicacute-garran-hospital.json)
- [`publiccommunity-kalgoorlie-community-health-service`](../au-fhir-test-data-set/connected-care/HealthcareService-publiccommunity-kalgoorlie-community-health-service.json)
- [`specialistmedical-kalgoorlie-specialist-clinic`](../au-fhir-test-data-set/connected-care/HealthcareService-specialistmedical-kalgoorlie-specialist-clinic.json)

**Organization** (11)

- [`aged-care-home-help`](../au-fhir-test-data-set/connected-care/Organization-aged-care-home-help.json)
- [`garran-ambulance-service`](../au-fhir-test-data-set/connected-care/Organization-garran-ambulance-service.json)
- [`garran-hospital`](../au-fhir-test-data-set/connected-care/Organization-garran-hospital.json)
- [`garran-hospital-ed`](../au-fhir-test-data-set/connected-care/Organization-garran-hospital-ed.json)
- [`kalgoorlie-aged-care-service`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-aged-care-service.json)
- [`kalgoorlie-community-health-service`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-community-health-service.json)
- [`kalgoorlie-medical-centre`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-medical-centre.json)
- [`kalgoorlie-ot-services`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-ot-services.json)
- [`kalgoorlie-pharmacy`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-pharmacy.json)
- [`kalgoorlie-physiotherapy`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-physiotherapy.json)
- [`kalgoorlie-specialist-clinic`](../au-fhir-test-data-set/connected-care/Organization-kalgoorlie-specialist-clinic.json)

**Location** (11)

- [`aged-care-home-help`](../au-fhir-test-data-set/connected-care/Location-aged-care-home-help.json)
- [`garran-ambulance-service`](../au-fhir-test-data-set/connected-care/Location-garran-ambulance-service.json)
- [`garran-hospital`](../au-fhir-test-data-set/connected-care/Location-garran-hospital.json)
- [`garran-hospital-ed`](../au-fhir-test-data-set/connected-care/Location-garran-hospital-ed.json)
- [`kalgoorlie-aged-care-service`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-aged-care-service.json)
- [`kalgoorlie-community-health-service`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-community-health-service.json)
- [`kalgoorlie-medical-centre`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-medical-centre.json)
- [`kalgoorlie-ot-services`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-ot-services.json)
- [`kalgoorlie-pharmacy`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-pharmacy.json)
- [`kalgoorlie-physiotherapy`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-physiotherapy.json)
- [`kalgoorlie-specialist-clinic`](../au-fhir-test-data-set/connected-care/Location-kalgoorlie-specialist-clinic.json)

<details><summary>12 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| `bradley-tom` | `ambulanceofficer-bradley-tom` | `garran-ambulance-service` | `garran-ambulance-service` |
| `brown-sarah` | `nursepractitioner-brown-sarah` | `kalgoorlie-community-health-service` | `kalgoorlie-community-health-service` |
| `green-susan` | `emergencymedicinespecialist-green-susan-garran-hospital` | `garran-hospital` | `garran-hospital` |
| `green-susan` | `emergencymedicinespecialist-green-susan-garran-hospital-ed` | `garran-hospital-ed` | `garran-hospital-ed` |
| `hayes-linda` | `nursepractitioner-hayes-linda` |  |  |
| `king-narelle` | `aboriginal-king-narelle` | `kalgoorlie-community-health-service` | `kalgoorlie-community-health-service` |
| `kumar-ravi` | `generalpractitioner-kumar-ravi` | `kalgoorlie-medical-centre` | `kalgoorlie-medical-centre` |
| `mitchell-karen` | `socialworker-mitchell-karen` | `kalgoorlie-aged-care-service` | `kalgoorlie-aged-care-service` |
| `smith-john` | `physiotherapist-smith-john` | `kalgoorlie-physiotherapy` | `kalgoorlie-physiotherapy` |
| `sullivan-joy` | `retailpharmacist-sullivan-joy` | `kalgoorlie-pharmacy` | `kalgoorlie-pharmacy` |
| `tench-natalie` | `endocrinologist-tench-natalie` | `kalgoorlie-specialist-clinic` | `kalgoorlie-specialist-clinic` |
| `wong-lisa` | `occupationaltherapist-wong-lisa` | `kalgoorlie-ot-services` | `kalgoorlie-ot-services` |

</details>

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

Derived from commit authorship, then curated by cross-checking against an attested list. The commit that introduced each file is matched against recognised organisation email domains, and the result is compared with an independently human-attested list so that a disagreement is reported rather than an entity silently dropping out. (see spec scenario "The limits of git-based attribution are stated").

<details><summary>Derivation notes</summary>

> 12 entities attributed across 1 organisation(s).
> Attribution derives from the commit that introduced each file and may under-report: a contributor using a personal email address, or a merge that did not preserve original authorship, is not detected. The list is not exhaustive.
> 1525 files in the data set carry no recognised-domain attribution; most are project-internal contributions.
> Cross-check passed: all 12 human-attested entities were also found independently by the authorship scan.

</details>


### Members (12)

<details><summary><strong>ADHA (Australian Digital Health Agency)</strong> (12 entities)</summary>

**Organization** (12)

- [`benalla-care-and-support`](../au-fhir-test-data-set/au-core/Organization-benalla-health-network.json)
- [`cremorne-care-and-support`](../au-fhir-test-data-set/au-core/Organization-cremorne-care-and-support.json)
- [`curtin-care-and-support`](../au-fhir-test-data-set/au-core/Organization-curtain-care-and-support.json)
- [`goondiwindi-health-network`](../au-fhir-test-data-set/au-core/Organization-goondiwindi-health-network.json)
- [`hayborough-care-and-support`](../au-fhir-test-data-set/au-core/Organization-hayborough-care-and-support.json)
- [`leeton-health-network`](../au-fhir-test-data-set/au-core/Organization-leeton-health-network.json)
- [`menzies-health-network`](../au-fhir-test-data-set/au-core/Organization-menzies-health-network.json)
- [`oxenford-care-and-support`](../au-fhir-test-data-set/au-core/Organization-oxenford-care-and-support.json)
- [`reid-health-network`](../au-fhir-test-data-set/au-core/Organization-reid-health-network.json)
- [`sorell-health-network`](../au-fhir-test-data-set/au-core/Organization-sorell-health-network.json)
- [`south-lake-care-and-support`](../au-fhir-test-data-set/au-core/Organization-south-lake-care-and-support.json)
- [`tarneit-health-network`](../au-fhir-test-data-set/au-core/Organization-tarneit-health-network.json)

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

<details><summary>Derivation notes</summary>

> 11 documented cases from docs/MissingAndSuppressedData_TestData.md.
> 56 additional instances confirmed from keyword hits; 1 rejected.

</details>


### Members (67)

<details><summary>67 entities — click to expand</summary>

**Patient** (8)

- [`italia-sofia-missing-birthDate`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-birthDate.json)
- [`italia-sofia-missing-gender`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-gender.json)
- [`italia-sofia-missing-identifier`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-identifier.json)
- [`italia-sofia-missing-name`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-name.json)
- [`italia-sofia-suppressed-birthDate`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-birthDate.json)
- [`italia-sofia-suppressed-gender`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-gender.json)
- [`italia-sofia-suppressed-identifier`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-identifier.json)
- [`italia-sofia-suppressed-name`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-name.json)

**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
|  | [`missing-practitioner`](../au-fhir-test-data-set/au-core/PractitionerRole-missing-practitioner.json) | Audiologist (Audiological medicine) |  |
| [`missing-name`](../au-fhir-test-data-set/au-core/Practitioner-missing-name.json) |  |  |  |

**Organization** (1)

- [`missing-name`](../au-fhir-test-data-set/au-core/Organization-missing-name.json)

**AllergyIntolerance** (2)

- [`egg-missing-code`](../au-fhir-test-data-set/au-core/AllergyIntolerance-egg-missing-code.json)
- [`egg-suppressed-subject`](../au-fhir-test-data-set/au-core/AllergyIntolerance-egg-suppressed-subject.json)

**Bundle** (2)

- [`aups-basicsummary-missing-comp-elements`](../au-fhir-test-data-set/au-patient-summary/Bundle-aups-basicsummary-missing-comp-elements.json)
- [`aups-section-emptyreason`](../au-fhir-test-data-set/au-patient-summary/Bundle-aups-section-emptyreason.json)

**Condition** (4)

- [`masked`](../au-fhir-test-data-set/au-core/Condition-masked.json)
- [`nailwound-missing-category`](../au-fhir-test-data-set/au-core/Condition-nailwound-missing-category.json)
- [`nailwound-missing-code`](../au-fhir-test-data-set/au-core/Condition-nailwound-missing-code.json)
- [`nailwound-suppressed-subject`](../au-fhir-test-data-set/au-core/Condition-nailwound-suppressed-subject.json)

**DocumentReference** (1)

- [`aups-section-emptyreason`](../au-fhir-test-data-set/au-core/DocumentReference-aups-section-emptyreason.json)

**Encounter** (3)

- [`annualvisit-missing-class`](../au-fhir-test-data-set/au-core/Encounter-annualvisit-missing-class.json)
- [`annualvisit-missing-status`](../au-fhir-test-data-set/au-core/Encounter-annualvisit-missing-status.json)
- [`annualvisit-suppressed-subject`](../au-fhir-test-data-set/au-core/Encounter-annualvisit-suppressed-subject.json)

**Immunization** (3)

- [`zoster-missing-code`](../au-fhir-test-data-set/au-core/Immunization-zoster-missing-code.json)
- [`zoster-missing-occurrence`](../au-fhir-test-data-set/au-core/Immunization-zoster-missing-occurrence.json)
- [`zoster-suppressed-subject`](../au-fhir-test-data-set/au-core/Immunization-zoster-suppressed-subject.json)

**Medication** (1)

- [`reaptan-missing-code`](../au-fhir-test-data-set/au-core/Medication-reaptan-missing-code.json)

**MedicationRequest** (5)

- [`reaptan-missing-authoredOn`](../au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-authoredOn.json)
- [`reaptan-missing-medication`](../au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-medication.json)
- [`reaptan-missing-requester`](../au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-requester.json)
- [`reaptan-missing-status`](../au-fhir-test-data-set/au-core/MedicationRequest-reaptan-missing-status.json)
- [`reaptan-suppressed-subject`](../au-fhir-test-data-set/au-core/MedicationRequest-reaptan-suppressed-subject.json)

**MedicationStatement** (3)

- [`missing-medication`](../au-fhir-test-data-set/au-core/MedicationStatement-missing-medication.json)
- [`missing-status`](../au-fhir-test-data-set/au-core/MedicationStatement-missing-status.json)
- [`suppressed-subject`](../au-fhir-test-data-set/au-core/MedicationStatement-suppressed-subject.json)

**Observation** (29)

- [`blood-group-panel-cancelled`](../au-fhir-test-data-set/au-core/Observation-blood-group-panel-cancelled.json)
- [`bloodpressure-diastolic-missing`](../au-fhir-test-data-set/au-core/Observation-bloodpressure-diastolic-missing.json)
- [`bloodpressure-missing`](../au-fhir-test-data-set/au-core/Observation-bloodpressure-missing.json)
- [`bloodpressure-systolic-missing`](../au-fhir-test-data-set/au-core/Observation-bloodpressure-systolic-missing.json)
- [`bodyheight-1-device-missing`](../au-fhir-test-data-set/au-core/Observation-bodyheight-1-device-missing.json)
- [`bodyheight-cancelled`](../au-fhir-test-data-set/au-core/Observation-bodyheight-cancelled.json)
- [`bodytemp-1-device-missing`](../au-fhir-test-data-set/au-core/Observation-bodytemp-1-device-missing.json)
- [`bodytemp-cancelled`](../au-fhir-test-data-set/au-core/Observation-bodytemp-cancelled.json)
- [`bodyweight-3-clothing-missing`](../au-fhir-test-data-set/au-core/Observation-bodyweight-3-clothing-missing.json)
- [`bodyweight-cancelled`](../au-fhir-test-data-set/au-core/Observation-bodyweight-cancelled.json)
- [`glasgow-coma-scale-motor-not-performed`](../au-fhir-test-data-set/au-core/Observation-glasgow-coma-scale-motor-not-performed.json)
- [`hearing-threshold-cancelled`](../au-fhir-test-data-set/au-core/Observation-hearing-threshold-cancelled.json)
- [`heartrate-1-exercise-missing`](../au-fhir-test-data-set/au-core/Observation-heartrate-1-exercise-missing.json)
- [`heartrate-cancelled`](../au-fhir-test-data-set/au-core/Observation-heartrate-cancelled.json)
- [`masked`](../au-fhir-test-data-set/au-core/Observation-masked.json)
- [`pathresult-missing-code`](../au-fhir-test-data-set/au-core/Observation-pathresult-missing-code.json)
- [`pathresult-missing-effective`](../au-fhir-test-data-set/au-core/Observation-pathresult-missing-effective.json)
- [`pathresult-missing-status`](../au-fhir-test-data-set/au-core/Observation-pathresult-missing-status.json)
- [`pathresult-missing-value`](../au-fhir-test-data-set/au-core/Observation-pathresult-missing-value.json)
- [`pathresult-suppressed-code`](../au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-code.json)
- [`pathresult-suppressed-dataAbsentReason`](../au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-dataAbsentReason.json)
- [`pathresult-suppressed-subject`](../au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-subject.json)
- [`pathresult-suppressed-valueCodeableConcept`](../au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-valueCodeableConcept.json)
- [`pathresult-suppressed-valueQuantity`](../au-fhir-test-data-set/au-core/Observation-pathresult-suppressed-valueQuantity.json)
- [`resprate-1-exercise-missing`](../au-fhir-test-data-set/au-core/Observation-resprate-1-exercise-missing.json)
- [`resprate-cancelled`](../au-fhir-test-data-set/au-core/Observation-resprate-cancelled.json)
- [`smokingstatus-notasked`](../au-fhir-test-data-set/au-core/Observation-smokingstatus-notasked.json)
- [`waistcircum-1-position-missing`](../au-fhir-test-data-set/au-core/Observation-waistcircum-1-position-missing.json)
- [`waistcircum-cancelled`](../au-fhir-test-data-set/au-core/Observation-waistcircum-cancelled.json)

**Procedure** (3)

- [`obstetric-missing-code`](../au-fhir-test-data-set/au-core/Procedure-obstetric-missing-code.json)
- [`obstetric-missing-status`](../au-fhir-test-data-set/au-core/Procedure-obstetric-missing-status.json)
- [`obstetric-missing-subject`](../au-fhir-test-data-set/au-core/Procedure-obstetric-missing-subject.json)

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


### Members (418)

<details><summary><strong>CCM_Aged care scenario - Future</strong> (49 entities)</summary>

**Patient** (1)

- [`reece-karen`](../au-fhir-test-data-set/au-core/Patient-reece-karen.json)

**Practitioner / PractitionerRole** (18)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`baker-troy`](../au-fhir-test-data-set/au-core/Practitioner-baker-troy.json) | [`baker-troy`](../au-fhir-test-data-set/au-core/PractitionerRole-baker-troy.json) | Pathologist (Clinical pathology) |  |
| [`baynton-lolita`](../au-fhir-test-data-set/au-core/Practitioner-baynton-lolita.json) | [`baynton-lolita`](../au-fhir-test-data-set/au-core/PractitionerRole-baynton-lolita.json) | Physiotherapist (Physiotherapy) |  |
| [`bell-rudolf`](../au-fhir-test-data-set/au-core/Practitioner-bell-rudolf.json) | [`bell-rudolf`](../au-fhir-test-data-set/au-core/PractitionerRole-bell-rudolf.json) | Registered Nurses nec (Nursing) |  |
| [`berry-lisa`](../au-fhir-test-data-set/au-core/Practitioner-berry-lisa.json) | [`berry-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-berry-lisa.json) | Occupational Therapist |  |
| [`carey-joyce`](../au-fhir-test-data-set/au-core/Practitioner-carey-joyce.json) | [`carey-joyce`](../au-fhir-test-data-set/au-core/PractitionerRole-carey-joyce.json) | Geriatrician (Geriatric medicine) |  |
| [`couch-joel`](../au-fhir-test-data-set/au-core/Practitioner-couch-joel.json) | [`couch-joel`](../au-fhir-test-data-set/au-core/PractitionerRole-couch-joel.json) | Surgeon (General) (General surgery) |  |
| [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/Practitioner-cruickshank-marlyn.json) | [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/PractitionerRole-cruickshank-marlyn.json) | Podiatrist (Podiatry) |  |
| [`fleming-skye`](../au-fhir-test-data-set/au-core/Practitioner-fleming-skye.json) | [`fleming-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-skye.json) | Pharmacist (Community pharmacy) |  |
| [`freeman-anya`](../au-fhir-test-data-set/au-core/Practitioner-freeman-anya.json) | [`freeman-anya`](../au-fhir-test-data-set/au-core/PractitionerRole-freeman-anya.json) | Social Worker |  |
| [`harley-reynalda`](../au-fhir-test-data-set/au-core/Practitioner-harley-reynalda.json) | [`harley-reynalda`](../au-fhir-test-data-set/au-core/PractitionerRole-harley-reynalda.json) | Dietitian (Dietetics and nutrition) |  |
| [`hoskins-earl`](../au-fhir-test-data-set/au-core/Practitioner-hoskins-earl.json) | [`hoskins-earl`](../au-fhir-test-data-set/au-core/PractitionerRole-hoskins-earl.json) | Dental Practitioner (Dentistry) |  |
| [`huddlestone-velda`](../au-fhir-test-data-set/au-core/Practitioner-huddlestone-velda.json) | [`huddlestone-velda`](../au-fhir-test-data-set/au-core/PractitionerRole-huddlestone-velda.json) | Gastroenterologist (Gastroenterology) |  |
| [`hutton-cortez`](../au-fhir-test-data-set/au-core/Practitioner-hutton-cortez.json) | [`hutton-cortez`](../au-fhir-test-data-set/au-core/PractitionerRole-hutton-cortez.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`lawrence-drew`](../au-fhir-test-data-set/au-core/Practitioner-lawrence-drew.json) | [`lawrence-drew`](../au-fhir-test-data-set/au-core/PractitionerRole-lawrence-drew.json) | Speech Pathologist |  |
| [`manning-opal`](../au-fhir-test-data-set/au-core/Practitioner-manning-opal.json) | [`manning-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-manning-opal.json) | Nurse Practitioner (Nursing) |  |
| [`rowlands-donya`](../au-fhir-test-data-set/au-core/Practitioner-rowlands-donya.json) | [`rowlands-donya`](../au-fhir-test-data-set/au-core/PractitionerRole-rowlands-donya.json) | Dental Practitioner (Dentistry) |  |
| [`tierney-gisela`](../au-fhir-test-data-set/au-core/Practitioner-tierney-gisela.json) | [`tierney-gisela`](../au-fhir-test-data-set/au-core/PractitionerRole-tierney-gisela.json) | Cardiologist (Cardiology) |  |
| [`vaughan-sol`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-sol.json) | [`vaughan-sol`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-sol.json) | General Practitioner (General medical practice) |  |

**Organization** (12)

- [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json)
- [`royal-park-medical-centre`](../au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json)
- [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json)
- [`woodville-cardiology`](../au-fhir-test-data-set/au-core/Organization-woodville-cardiology.json)
- [`woodville-dental`](../au-fhir-test-data-set/au-core/Organization-woodville-dental.json)
- [`woodville-dietitian-service`](../au-fhir-test-data-set/au-core/Organization-woodville-dietitian-service.json)
- [`woodville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-woodville-medical-clinic.json)
- [`woodville-ot-services`](../au-fhir-test-data-set/au-core/Organization-woodville-ot-services.json)
- [`woodville-pathology`](../au-fhir-test-data-set/au-core/Organization-woodville-pathology.json)
- [`woodville-pharmacy`](../au-fhir-test-data-set/au-core/Organization-woodville-pharmacy.json)
- [`woodville-podiatry`](../au-fhir-test-data-set/au-core/Organization-woodville-podiatry.json)
- [`woodville-radiology`](../au-fhir-test-data-set/au-core/Organization-woodville-radiology.json)

<details><summary>18 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`baker-troy`](../au-fhir-test-data-set/au-core/Practitioner-baker-troy.json) | [`baker-troy`](../au-fhir-test-data-set/au-core/PractitionerRole-baker-troy.json) | [`woodville-pathology`](../au-fhir-test-data-set/au-core/Organization-woodville-pathology.json) |  |
| [`baynton-lolita`](../au-fhir-test-data-set/au-core/Practitioner-baynton-lolita.json) | [`baynton-lolita`](../au-fhir-test-data-set/au-core/PractitionerRole-baynton-lolita.json) | [`woodville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-woodville-medical-clinic.json) |  |
| [`bell-rudolf`](../au-fhir-test-data-set/au-core/Practitioner-bell-rudolf.json) | [`bell-rudolf`](../au-fhir-test-data-set/au-core/PractitionerRole-bell-rudolf.json) | [`royal-park-medical-centre`](../au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json) |  |
| [`berry-lisa`](../au-fhir-test-data-set/au-core/Practitioner-berry-lisa.json) | [`berry-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-berry-lisa.json) | [`woodville-ot-services`](../au-fhir-test-data-set/au-core/Organization-woodville-ot-services.json) |  |
| [`carey-joyce`](../au-fhir-test-data-set/au-core/Practitioner-carey-joyce.json) | [`carey-joyce`](../au-fhir-test-data-set/au-core/PractitionerRole-carey-joyce.json) | [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) |  |
| [`couch-joel`](../au-fhir-test-data-set/au-core/Practitioner-couch-joel.json) | [`couch-joel`](../au-fhir-test-data-set/au-core/PractitionerRole-couch-joel.json) | [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) |  |
| [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/Practitioner-cruickshank-marlyn.json) | [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/PractitionerRole-cruickshank-marlyn.json) | [`woodville-podiatry`](../au-fhir-test-data-set/au-core/Organization-woodville-podiatry.json) |  |
| [`fleming-skye`](../au-fhir-test-data-set/au-core/Practitioner-fleming-skye.json) | [`fleming-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-skye.json) | [`woodville-pharmacy`](../au-fhir-test-data-set/au-core/Organization-woodville-pharmacy.json) |  |
| [`freeman-anya`](../au-fhir-test-data-set/au-core/Practitioner-freeman-anya.json) | [`freeman-anya`](../au-fhir-test-data-set/au-core/PractitionerRole-freeman-anya.json) | [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) |  |
| [`harley-reynalda`](../au-fhir-test-data-set/au-core/Practitioner-harley-reynalda.json) | [`harley-reynalda`](../au-fhir-test-data-set/au-core/PractitionerRole-harley-reynalda.json) | [`woodville-dietitian-service`](../au-fhir-test-data-set/au-core/Organization-woodville-dietitian-service.json) |  |
| [`hoskins-earl`](../au-fhir-test-data-set/au-core/Practitioner-hoskins-earl.json) | [`hoskins-earl`](../au-fhir-test-data-set/au-core/PractitionerRole-hoskins-earl.json) | [`woodville-dental`](../au-fhir-test-data-set/au-core/Organization-woodville-dental.json) |  |
| [`huddlestone-velda`](../au-fhir-test-data-set/au-core/Practitioner-huddlestone-velda.json) | [`huddlestone-velda`](../au-fhir-test-data-set/au-core/PractitionerRole-huddlestone-velda.json) | [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) |  |
| [`hutton-cortez`](../au-fhir-test-data-set/au-core/Practitioner-hutton-cortez.json) | [`hutton-cortez`](../au-fhir-test-data-set/au-core/PractitionerRole-hutton-cortez.json) | [`woodville-radiology`](../au-fhir-test-data-set/au-core/Organization-woodville-radiology.json) |  |
| [`lawrence-drew`](../au-fhir-test-data-set/au-core/Practitioner-lawrence-drew.json) | [`lawrence-drew`](../au-fhir-test-data-set/au-core/PractitionerRole-lawrence-drew.json) | [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) |  |
| [`manning-opal`](../au-fhir-test-data-set/au-core/Practitioner-manning-opal.json) | [`manning-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-manning-opal.json) | [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) |  |
| [`rowlands-donya`](../au-fhir-test-data-set/au-core/Practitioner-rowlands-donya.json) | [`rowlands-donya`](../au-fhir-test-data-set/au-core/PractitionerRole-rowlands-donya.json) | [`woodville-dental`](../au-fhir-test-data-set/au-core/Organization-woodville-dental.json) |  |
| [`tierney-gisela`](../au-fhir-test-data-set/au-core/Practitioner-tierney-gisela.json) | [`tierney-gisela`](../au-fhir-test-data-set/au-core/PractitionerRole-tierney-gisela.json) | [`woodville-cardiology`](../au-fhir-test-data-set/au-core/Organization-woodville-cardiology.json) |  |
| [`vaughan-sol`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-sol.json) | [`vaughan-sol`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-sol.json) | [`royal-park-medical-centre`](../au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json) |  |

</details>

</details>

<details><summary><strong>CCM scenario - Drafted</strong> (44 entities)</summary>

**Patient** (1)

- [`foreman-caterina`](../au-fhir-test-data-set/au-core/Patient-foreman-caterina.json)

**Practitioner / PractitionerRole** (16)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`bond-edmundo`](../au-fhir-test-data-set/au-core/Practitioner-bond-edmundo.json) | [`bond-edmundo`](../au-fhir-test-data-set/au-core/PractitionerRole-bond-edmundo.json) | Pharmacist (Community pharmacy) |  |
| [`bowyer-norbert`](../au-fhir-test-data-set/au-core/Practitioner-bowyer-norbert.json) | [`bowyer-norbert`](../au-fhir-test-data-set/au-core/PractitionerRole-bowyer-norbert.json) | Exercise Physiologist |  |
| [`fuller-kendrick`](../au-fhir-test-data-set/au-core/Practitioner-fuller-kendrick.json) | [`fuller-kendrick`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-kendrick.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) |  |
| [`hallan-maggie`](../au-fhir-test-data-set/au-core/Practitioner-hallan-maggie.json) | [`hallan-maggie`](../au-fhir-test-data-set/au-core/PractitionerRole-hallan-maggie.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`hamel-opal`](../au-fhir-test-data-set/au-core/Practitioner-hamel-opal.json) | [`hamel-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-hamel-opal.json) | General Practitioner (General medical practice) |  |
| [`kelly-arlene`](../au-fhir-test-data-set/au-core/Practitioner-kelly-arlene.json) | [`kelly-arlene`](../au-fhir-test-data-set/au-core/PractitionerRole-kelly-arlene.json) | Ophthalmologist (Ophthalmology) |  |
| [`keyes-chau`](../au-fhir-test-data-set/au-core/Practitioner-keyes-chau.json) | [`keyes-chau`](../au-fhir-test-data-set/au-core/PractitionerRole-keyes-chau.json) | Pathologist (Clinical pathology) |  |
| [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/Practitioner-mcnaughton-opal.json) | [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnaughton-opal.json) | Diabetes Educator |  |
| [`mullins-bonita`](../au-fhir-test-data-set/au-core/Practitioner-mullins-bonita.json) | [`mullins-bonita`](../au-fhir-test-data-set/au-core/PractitionerRole-mullins-bonita.json) | Registered Nurses nec (Nursing) |  |
| [`osland-deanne`](../au-fhir-test-data-set/au-core/Practitioner-osland-deanne.json) | [`osland-deanne`](../au-fhir-test-data-set/au-core/PractitionerRole-osland-deanne.json) | Podiatrist (Podiatry) |  |
| [`patterson-teri`](../au-fhir-test-data-set/au-core/Practitioner-patterson-teri.json) | [`patterson-teri`](../au-fhir-test-data-set/au-core/PractitionerRole-patterson-teri.json) | Dietitian (Dietetics and nutrition) |  |
| [`phillips-gerard`](../au-fhir-test-data-set/au-core/Practitioner-phillips-gerard.json) | [`phillips-gerard`](../au-fhir-test-data-set/au-core/PractitionerRole-phillips-gerard.json) | Endocrinologist (Endocrinology) |  |
| [`quinn-jeramy`](../au-fhir-test-data-set/au-core/Practitioner-quinn-jeramy.json) | [`quinn-jeramy`](../au-fhir-test-data-set/au-core/PractitionerRole-quinn-jeramy.json) | Optometrist |  |
| [`schaefer-elden`](../au-fhir-test-data-set/au-core/Practitioner-schaefer-elden.json) | [`schaefer-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-schaefer-elden.json) | Cardiologist (Cardiology) |  |
| [`sharp-cherish`](../au-fhir-test-data-set/au-core/Practitioner-sharp-cherish.json) | [`sharp-cherish`](../au-fhir-test-data-set/au-core/PractitionerRole-sharp-cherish.json) | Registered Nurses nec (Nursing) |  |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | Clinical Psychologist (Clinical psychology) | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**Organization** (11)

- [`sunshine-cardiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-cardiology.json)
- [`sunshine-endocrinology`](../au-fhir-test-data-set/au-core/Organization-sunshine-endocrinology.json)
- [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json)
- [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json)
- [`sunshine-nephrology`](../au-fhir-test-data-set/au-core/Organization-sunshine-nephrology.json)
- [`sunshine-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-sunshine-ophthalmology.json)
- [`sunshine-optical`](../au-fhir-test-data-set/au-core/Organization-sunshine-optical.json)
- [`sunshine-pathology`](../au-fhir-test-data-set/au-core/Organization-sunshine-pathology.json)
- [`sunshine-pharmacy`](../au-fhir-test-data-set/au-core/Organization-sunshine-pharmacy.json)
- [`sunshine-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-sunshine-physiotherapy.json)
- [`sunshine-radiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-radiology.json)

<details><summary>16 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`bond-edmundo`](../au-fhir-test-data-set/au-core/Practitioner-bond-edmundo.json) | [`bond-edmundo`](../au-fhir-test-data-set/au-core/PractitionerRole-bond-edmundo.json) | [`sunshine-pharmacy`](../au-fhir-test-data-set/au-core/Organization-sunshine-pharmacy.json) |  |
| [`bowyer-norbert`](../au-fhir-test-data-set/au-core/Practitioner-bowyer-norbert.json) | [`bowyer-norbert`](../au-fhir-test-data-set/au-core/PractitionerRole-bowyer-norbert.json) | [`sunshine-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-sunshine-physiotherapy.json) |  |
| [`fuller-kendrick`](../au-fhir-test-data-set/au-core/Practitioner-fuller-kendrick.json) | [`fuller-kendrick`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-kendrick.json) | [`sunshine-nephrology`](../au-fhir-test-data-set/au-core/Organization-sunshine-nephrology.json) |  |
| [`hallan-maggie`](../au-fhir-test-data-set/au-core/Practitioner-hallan-maggie.json) | [`hallan-maggie`](../au-fhir-test-data-set/au-core/PractitionerRole-hallan-maggie.json) | [`sunshine-radiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-radiology.json) |  |
| [`hamel-opal`](../au-fhir-test-data-set/au-core/Practitioner-hamel-opal.json) | [`hamel-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-hamel-opal.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |
| [`kelly-arlene`](../au-fhir-test-data-set/au-core/Practitioner-kelly-arlene.json) | [`kelly-arlene`](../au-fhir-test-data-set/au-core/PractitionerRole-kelly-arlene.json) | [`sunshine-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-sunshine-ophthalmology.json) |  |
| [`keyes-chau`](../au-fhir-test-data-set/au-core/Practitioner-keyes-chau.json) | [`keyes-chau`](../au-fhir-test-data-set/au-core/PractitionerRole-keyes-chau.json) | [`sunshine-pathology`](../au-fhir-test-data-set/au-core/Organization-sunshine-pathology.json) |  |
| [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/Practitioner-mcnaughton-opal.json) | [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnaughton-opal.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |
| [`mullins-bonita`](../au-fhir-test-data-set/au-core/Practitioner-mullins-bonita.json) | [`mullins-bonita`](../au-fhir-test-data-set/au-core/PractitionerRole-mullins-bonita.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |
| [`osland-deanne`](../au-fhir-test-data-set/au-core/Practitioner-osland-deanne.json) | [`osland-deanne`](../au-fhir-test-data-set/au-core/PractitionerRole-osland-deanne.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |
| [`patterson-teri`](../au-fhir-test-data-set/au-core/Practitioner-patterson-teri.json) | [`patterson-teri`](../au-fhir-test-data-set/au-core/PractitionerRole-patterson-teri.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |
| [`phillips-gerard`](../au-fhir-test-data-set/au-core/Practitioner-phillips-gerard.json) | [`phillips-gerard`](../au-fhir-test-data-set/au-core/PractitionerRole-phillips-gerard.json) | [`sunshine-endocrinology`](../au-fhir-test-data-set/au-core/Organization-sunshine-endocrinology.json) |  |
| [`quinn-jeramy`](../au-fhir-test-data-set/au-core/Practitioner-quinn-jeramy.json) | [`quinn-jeramy`](../au-fhir-test-data-set/au-core/PractitionerRole-quinn-jeramy.json) | [`sunshine-optical`](../au-fhir-test-data-set/au-core/Organization-sunshine-optical.json) |  |
| [`schaefer-elden`](../au-fhir-test-data-set/au-core/Practitioner-schaefer-elden.json) | [`schaefer-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-schaefer-elden.json) | [`sunshine-cardiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-cardiology.json) |  |
| [`sharp-cherish`](../au-fhir-test-data-set/au-core/Practitioner-sharp-cherish.json) | [`sharp-cherish`](../au-fhir-test-data-set/au-core/PractitionerRole-sharp-cherish.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |

</details>

</details>

<details><summary><strong>Family scenario w baby (2 month old)</strong> (98 entities)</summary>

**Patient** (4)

| ID | Also in |
| --- | --- |
| [`lowe-alessandra`](../au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json) | *[families](#families)* |
| [`lowe-alix`](../au-fhir-test-data-set/au-core/Patient-lowe-alix.json) | *[families](#families)* |
| [`lowe-cedric`](../au-fhir-test-data-set/au-core/Patient-lowe-cedric.json) | *[families](#families)* |
| [`lowe-valerie`](../au-fhir-test-data-set/au-core/Patient-lowe-valerie.json) | *[families](#families)* |

**Practitioner / PractitionerRole** (33)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`berridge-beulah`](../au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json) | [`berridge-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json) | Anaesthetist (Anaesthetics) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`breadmore-phillip`](../au-fhir-test-data-set/au-core/Practitioner-breadmore-phillip.json) | [`breadmore-phillip`](../au-fhir-test-data-set/au-core/PractitionerRole-breadmore-phillip.json) | Registered Nurses nec (Nursing) |  |
| [`cox-sandra`](../au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json) | [`cox-sandra`](../au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`dawson-kent`](../au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json) | [`dawson-kent`](../au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json) | Emergency Medicine Specialist / Emergency Physician (Emergency medicine) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`duncan-xenia`](../au-fhir-test-data-set/au-core/Practitioner-duncan-xenia.json) | [`duncan-xenia`](../au-fhir-test-data-set/au-core/PractitionerRole-duncan-xenia.json) | Social Worker |  |
| [`ellison-abby`](../au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json) | [`ellison-abby`](../au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json) | Physiotherapist (Physiotherapy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`ewing-jude`](../au-fhir-test-data-set/au-core/Practitioner-ewing-jude.json) | [`ewing-jude`](../au-fhir-test-data-set/au-core/PractitionerRole-ewing-jude.json) | Registered Nurses nec (Nursing) |  |
| [`fleming-kitty`](../au-fhir-test-data-set/au-core/Practitioner-fleming-kitty.json) | [`fleming-kitty`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-kitty.json) | General Practitioner (General medical practice) |  |
| [`frank-gaylene`](../au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json) | [`frank-gaylene`](../au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json) | Nurse Practitioner (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`fuller-christeen`](../au-fhir-test-data-set/au-core/Practitioner-fuller-christeen.json) | [`fuller-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-christeen.json) | Gastroenterologist (Gastroenterology) |  |
| [`goodwin-rae`](../au-fhir-test-data-set/au-core/Practitioner-goodwin-rae.json) | [`goodwin-rae`](../au-fhir-test-data-set/au-core/PractitionerRole-goodwin-rae.json) | Optometrist |  |
| [`hamilton-errol`](../au-fhir-test-data-set/au-core/Practitioner-hamilton-errol.json) | [`hamilton-errol`](../au-fhir-test-data-set/au-core/PractitionerRole-hamilton-errol.json) | Pharmacist (Community pharmacy) |  |
| [`healey-tamiko`](../au-fhir-test-data-set/au-core/Practitioner-healey-tamiko.json) | [`healey-tamiko`](../au-fhir-test-data-set/au-core/PractitionerRole-healey-tamiko.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) |  |
| [`howe-elden`](../au-fhir-test-data-set/au-core/Practitioner-howe-elden.json) | [`howe-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-howe-elden.json) | Midwife (Obstetric nursing) |  |
| [`knowles-sunshine`](../au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json) | [`knowles-sunshine`](../au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json) | Occupational Therapist | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json) | [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json) | Clinical Psychologist (Clinical psychology) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`little-jerrie`](../au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json) | [`little-jerrie`](../au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json) | General Practitioner (General medical practice) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`macey-brant`](../au-fhir-test-data-set/au-core/Practitioner-macey-brant.json) | [`macey-brant`](../au-fhir-test-data-set/au-core/PractitionerRole-macey-brant.json) | Ophthalmologist (Ophthalmology) |  |
| [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/Practitioner-mcbean-nicollette.json) | [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/PractitionerRole-mcbean-nicollette.json) | Surgeon (General) (General surgery) |  |
| [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/Practitioner-mcintosh-angelica.json) | [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/PractitionerRole-mcintosh-angelica.json) | Obstetrician and Gynaecologist (Obstetrics and gynaecology) |  |
| [`mcnab-angelina`](../au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json) | [`mcnab-angelina`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json) | Dietitian (Dietetics and nutrition) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`mills-hope`](../au-fhir-test-data-set/au-core/Practitioner-mills-hope.json) | [`mills-hope`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json) | Occupational Therapist | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`nairn-vince`](../au-fhir-test-data-set/au-core/Practitioner-nairn-vince.json) | [`nairn-vince`](../au-fhir-test-data-set/au-core/PractitionerRole-nairn-vince.json) | General Practitioner (General medical practice) |  |
| [`neville-isaiah`](../au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json) | [`neville-isaiah`](../au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json) | Physiotherapist (Physiotherapy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`nutley-bradley`](../au-fhir-test-data-set/au-core/Practitioner-nutley-bradley.json) | [`nutley-bradley`](../au-fhir-test-data-set/au-core/PractitionerRole-nutley-bradley.json) | Pathologist (Clinical pathology) |  |
| [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json) | [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json) | Pharmacist (Community pharmacy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`osmond-michele`](../au-fhir-test-data-set/au-core/Practitioner-osmond-michele.json) | [`osmond-michele`](../au-fhir-test-data-set/au-core/PractitionerRole-osmond-michele.json) | Dental Practitioner (Dentistry) |  |
| [`perkins-amee`](../au-fhir-test-data-set/au-core/Practitioner-perkins-amee.json) | [`perkins-amee`](../au-fhir-test-data-set/au-core/PractitionerRole-perkins-amee.json) | Sonographer |  |
| [`redman-mariah`](../au-fhir-test-data-set/au-core/Practitioner-redman-mariah.json) | [`redman-mariah`](../au-fhir-test-data-set/au-core/PractitionerRole-redman-mariah.json) | Midwife (Obstetric nursing) |  |
| [`roche-garfield`](../au-fhir-test-data-set/au-core/Practitioner-roche-garfield.json) | [`roche-garfield`](../au-fhir-test-data-set/au-core/PractitionerRole-roche-garfield.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`seaby-penelope`](../au-fhir-test-data-set/au-core/Practitioner-seaby-penelope.json) | [`seaby-penelope`](../au-fhir-test-data-set/au-core/PractitionerRole-seaby-penelope.json) | Cardiologist (Cardiology) |  |
| [`stephens-nellie`](../au-fhir-test-data-set/au-core/Practitioner-stephens-nellie.json) | [`stephens-nellie`](../au-fhir-test-data-set/au-core/PractitionerRole-stephens-nellie.json) | Social Worker |  |
| [`tate-melvin`](../au-fhir-test-data-set/au-core/Practitioner-tate-melvin.json) | [`tate-melvin`](../au-fhir-test-data-set/au-core/PractitionerRole-tate-melvin.json) | Midwife (Obstetric nursing) |  |

**Organization** (16)

- [`parramatta-community-health`](../au-fhir-test-data-set/au-core/Organization-parramatta-community-health.json)
- [`parramatta-dental`](../au-fhir-test-data-set/au-core/Organization-parramatta-dental.json)
- [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json)
- [`parramatta-midwifery`](../au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json)
- [`parramatta-nutrition`](../au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json)
- [`parramatta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json)
- [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json)
- [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json)
- [`westmead-optical`](../au-fhir-test-data-set/au-core/Organization-westmead-optical.json)
- [`westmead-ot-services`](../au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json)
- [`westmead-pathology`](../au-fhir-test-data-set/au-core/Organization-westmead-pathology.json)
- [`westmead-pharmacy`](../au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json)
- [`westmead-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json)
- [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json)
- [`westmead-radiology`](../au-fhir-test-data-set/au-core/Organization-westmead-radiology.json)
- [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json)

**RelatedPerson** (12)

- [`lowe-alessandra-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-1.json)
- [`lowe-alessandra-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-2.json)
- [`lowe-alessandra-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-3.json)
- [`lowe-alix-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-1.json)
- [`lowe-alix-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-2.json)
- [`lowe-alix-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-3.json)
- [`lowe-cedric-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-1.json)
- [`lowe-cedric-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-2.json)
- [`lowe-cedric-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-3.json)
- [`lowe-valerie-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-1.json)
- [`lowe-valerie-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-2.json)
- [`lowe-valerie-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-3.json)

<details><summary>33 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`berridge-beulah`](../au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json) | [`berridge-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |
| [`breadmore-phillip`](../au-fhir-test-data-set/au-core/Practitioner-breadmore-phillip.json) | [`breadmore-phillip`](../au-fhir-test-data-set/au-core/PractitionerRole-breadmore-phillip.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |
| [`cox-sandra`](../au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json) | [`cox-sandra`](../au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json) | [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) |  |
| [`dawson-kent`](../au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json) | [`dawson-kent`](../au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json) | [`parramatta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json) |  |
| [`duncan-xenia`](../au-fhir-test-data-set/au-core/Practitioner-duncan-xenia.json) | [`duncan-xenia`](../au-fhir-test-data-set/au-core/PractitionerRole-duncan-xenia.json) | [`parramatta-community-health`](../au-fhir-test-data-set/au-core/Organization-parramatta-community-health.json) |  |
| [`ellison-abby`](../au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json) | [`ellison-abby`](../au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |
| [`ewing-jude`](../au-fhir-test-data-set/au-core/Practitioner-ewing-jude.json) | [`ewing-jude`](../au-fhir-test-data-set/au-core/PractitionerRole-ewing-jude.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |
| [`fleming-kitty`](../au-fhir-test-data-set/au-core/Practitioner-fleming-kitty.json) | [`fleming-kitty`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-kitty.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |
| [`frank-gaylene`](../au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json) | [`frank-gaylene`](../au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |
| [`fuller-christeen`](../au-fhir-test-data-set/au-core/Practitioner-fuller-christeen.json) | [`fuller-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-christeen.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |
| [`goodwin-rae`](../au-fhir-test-data-set/au-core/Practitioner-goodwin-rae.json) | [`goodwin-rae`](../au-fhir-test-data-set/au-core/PractitionerRole-goodwin-rae.json) | [`westmead-optical`](../au-fhir-test-data-set/au-core/Organization-westmead-optical.json) |  |
| [`hamilton-errol`](../au-fhir-test-data-set/au-core/Practitioner-hamilton-errol.json) | [`hamilton-errol`](../au-fhir-test-data-set/au-core/PractitionerRole-hamilton-errol.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |
| [`healey-tamiko`](../au-fhir-test-data-set/au-core/Practitioner-healey-tamiko.json) | [`healey-tamiko`](../au-fhir-test-data-set/au-core/PractitionerRole-healey-tamiko.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |
| [`howe-elden`](../au-fhir-test-data-set/au-core/Practitioner-howe-elden.json) | [`howe-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-howe-elden.json) | [`parramatta-midwifery`](../au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json) |  |
| [`knowles-sunshine`](../au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json) | [`knowles-sunshine`](../au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json) | [`westmead-ot-services`](../au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json) |  |
| [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json) | [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |
| [`little-jerrie`](../au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json) | [`little-jerrie`](../au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json) | [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) |  |
| [`macey-brant`](../au-fhir-test-data-set/au-core/Practitioner-macey-brant.json) | [`macey-brant`](../au-fhir-test-data-set/au-core/PractitionerRole-macey-brant.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |
| [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/Practitioner-mcbean-nicollette.json) | [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/PractitionerRole-mcbean-nicollette.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |
| [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/Practitioner-mcintosh-angelica.json) | [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/PractitionerRole-mcintosh-angelica.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |
| [`mcnab-angelina`](../au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json) | [`mcnab-angelina`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json) | [`parramatta-nutrition`](../au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json) |  |
| [`mills-hope`](../au-fhir-test-data-set/au-core/Practitioner-mills-hope.json) | [`mills-hope`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |
| [`nairn-vince`](../au-fhir-test-data-set/au-core/Practitioner-nairn-vince.json) | [`nairn-vince`](../au-fhir-test-data-set/au-core/PractitionerRole-nairn-vince.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |
| [`neville-isaiah`](../au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json) | [`neville-isaiah`](../au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json) | [`westmead-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json) |  |
| [`nutley-bradley`](../au-fhir-test-data-set/au-core/Practitioner-nutley-bradley.json) | [`nutley-bradley`](../au-fhir-test-data-set/au-core/PractitionerRole-nutley-bradley.json) | [`westmead-pathology`](../au-fhir-test-data-set/au-core/Organization-westmead-pathology.json) |  |
| [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json) | [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json) | [`westmead-pharmacy`](../au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json) |  |
| [`osmond-michele`](../au-fhir-test-data-set/au-core/Practitioner-osmond-michele.json) | [`osmond-michele`](../au-fhir-test-data-set/au-core/PractitionerRole-osmond-michele.json) | [`parramatta-dental`](../au-fhir-test-data-set/au-core/Organization-parramatta-dental.json) |  |
| [`perkins-amee`](../au-fhir-test-data-set/au-core/Practitioner-perkins-amee.json) | [`perkins-amee`](../au-fhir-test-data-set/au-core/PractitionerRole-perkins-amee.json) | [`westmead-radiology`](../au-fhir-test-data-set/au-core/Organization-westmead-radiology.json) |  |
| [`redman-mariah`](../au-fhir-test-data-set/au-core/Practitioner-redman-mariah.json) | [`redman-mariah`](../au-fhir-test-data-set/au-core/PractitionerRole-redman-mariah.json) | [`parramatta-midwifery`](../au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json) |  |
| [`roche-garfield`](../au-fhir-test-data-set/au-core/Practitioner-roche-garfield.json) | [`roche-garfield`](../au-fhir-test-data-set/au-core/PractitionerRole-roche-garfield.json) | [`westmead-radiology`](../au-fhir-test-data-set/au-core/Organization-westmead-radiology.json) |  |
| [`seaby-penelope`](../au-fhir-test-data-set/au-core/Practitioner-seaby-penelope.json) | [`seaby-penelope`](../au-fhir-test-data-set/au-core/PractitionerRole-seaby-penelope.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |
| [`stephens-nellie`](../au-fhir-test-data-set/au-core/Practitioner-stephens-nellie.json) | [`stephens-nellie`](../au-fhir-test-data-set/au-core/PractitionerRole-stephens-nellie.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |
| [`tate-melvin`](../au-fhir-test-data-set/au-core/Practitioner-tate-melvin.json) | [`tate-melvin`](../au-fhir-test-data-set/au-core/PractitionerRole-tate-melvin.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |

</details>

</details>

<details><summary><strong>FIrst nations scenario</strong> (51 entities)</summary>

**Patient** (1)

- [`coombe-ross`](../au-fhir-test-data-set/au-core/Patient-coombe-ross.json)

**Practitioner / PractitionerRole** (20)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`allardice-della`](../au-fhir-test-data-set/au-core/Practitioner-allardice-della.json) | [`allardice-della`](../au-fhir-test-data-set/au-core/PractitionerRole-allardice-della.json) | Clinical Psychologist (Clinical psychology) |  |
| [`baratz-layla`](../au-fhir-test-data-set/au-core/Practitioner-baratz-layla.json) | [`baratz-layla`](../au-fhir-test-data-set/au-core/PractitionerRole-baratz-layla.json) | Physiotherapist (Physiotherapy) |  |
| [`bassett-elmer`](../au-fhir-test-data-set/au-core/Practitioner-bassett-elmer.json) | [`bassett-elmer`](../au-fhir-test-data-set/au-core/PractitionerRole-bassett-elmer.json) | Registered Nurses nec (Nursing) |  |
| [`butler-cheryl`](../au-fhir-test-data-set/au-core/Practitioner-butler-cheryl.json) | [`butler-cheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-butler-cheryl.json) | Registered Nurses nec (Nursing) |  |
| [`clapham-laurie`](../au-fhir-test-data-set/au-core/Practitioner-clapham-laurie.json) | [`clapham-laurie`](../au-fhir-test-data-set/au-core/PractitionerRole-clapham-laurie.json) | Exercise Physiologist |  |
| [`davies-keiko`](../au-fhir-test-data-set/au-core/Practitioner-davies-keiko.json) | [`davies-keiko`](../au-fhir-test-data-set/au-core/PractitionerRole-davies-keiko.json) | Dietitian (Dietetics and nutrition) |  |
| [`devine-frank`](../au-fhir-test-data-set/au-core/Practitioner-devine-frank.json) | [`devine-frank`](../au-fhir-test-data-set/au-core/PractitionerRole-devine-frank.json) | Diabetes Educator |  |
| [`gates-anton`](../au-fhir-test-data-set/au-core/Practitioner-gates-anton.json) | [`gates-anton`](../au-fhir-test-data-set/au-core/PractitionerRole-gates-anton.json) | General Practitioner (General medical practice) |  |
| [`giles-veronique`](../au-fhir-test-data-set/au-core/Practitioner-giles-veronique.json) | [`giles-veronique`](../au-fhir-test-data-set/au-core/PractitionerRole-giles-veronique.json) | Optometrist |  |
| [`goldsmith-monique`](../au-fhir-test-data-set/au-core/Practitioner-goldsmith-monique.json) | [`goldsmith-monique`](../au-fhir-test-data-set/au-core/PractitionerRole-goldsmith-monique.json) | Endocrinologist (Endocrinology) |  |
| [`hackett-norman`](../au-fhir-test-data-set/au-core/Practitioner-hackett-norman.json) | [`hackett-norman`](../au-fhir-test-data-set/au-core/PractitionerRole-hackett-norman.json) | Nurse Practitioner (Nursing) |  |
| [`hodges-julia`](../au-fhir-test-data-set/au-core/Practitioner-hodges-julia.json) | [`hodges-julia`](../au-fhir-test-data-set/au-core/PractitionerRole-hodges-julia.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) |  |
| [`horn-wes`](../au-fhir-test-data-set/au-core/Practitioner-horn-wes.json) | [`horn-wes`](../au-fhir-test-data-set/au-core/PractitionerRole-horn-wes.json) | Podiatrist (Podiatry) |  |
| [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/Practitioner-ibbotson-destiny.json) | [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/PractitionerRole-ibbotson-destiny.json) | Sleep Medicine Specialist |  |
| [`lowry-bennett`](../au-fhir-test-data-set/au-core/Practitioner-lowry-bennett.json) | [`lowry-bennett`](../au-fhir-test-data-set/au-core/PractitionerRole-lowry-bennett.json) | Occupational Therapist |  |
| [`moran-linoel`](../au-fhir-test-data-set/au-core/Practitioner-moran-linoel.json) | [`moran-linoel`](../au-fhir-test-data-set/au-core/PractitionerRole-moran-linoel.json) | Psychiatrist (Psychiatry) |  |
| [`patrick-thalia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-thalia.json) | [`patrick-thalia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-thalia.json) | Counsellor (Clinical psychology) |  |
| [`poulson-lisa`](../au-fhir-test-data-set/au-core/Practitioner-poulson-lisa.json) | [`poulson-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-poulson-lisa.json) | Aboriginal and Torres Strait Islander Health Worker |  |
| [`simmons-ashton`](../au-fhir-test-data-set/au-core/Practitioner-simmons-ashton.json) | [`simmons-ashton`](../au-fhir-test-data-set/au-core/PractitionerRole-simmons-ashton.json) | Cardiologist (Cardiology) |  |
| [`thorburn-juanita`](../au-fhir-test-data-set/au-core/Practitioner-thorburn-juanita.json) | [`thorburn-juanita`](../au-fhir-test-data-set/au-core/PractitionerRole-thorburn-juanita.json) | Social Worker |  |

**Organization** (10)

- [`broome-community-health`](../au-fhir-test-data-set/au-core/Organization-broome-community-health.json)
- [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json)
- [`broome-nutrition`](../au-fhir-test-data-set/au-core/Organization-broome-nutrition.json)
- [`broome-optometry`](../au-fhir-test-data-set/au-core/Organization-broome-optometry.json)
- [`broome-ot-services`](../au-fhir-test-data-set/au-core/Organization-broome-ot-services.json)
- [`broome-physiology`](../au-fhir-test-data-set/au-core/Organization-broome-physiology.json)
- [`broome-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-broome-physiotherapy.json)
- [`broome-podiatry`](../au-fhir-test-data-set/au-core/Organization-broome-podiatry.json)
- [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json)
- [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json)

<details><summary>20 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`allardice-della`](../au-fhir-test-data-set/au-core/Practitioner-allardice-della.json) | [`allardice-della`](../au-fhir-test-data-set/au-core/PractitionerRole-allardice-della.json) | [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) |  |
| [`baratz-layla`](../au-fhir-test-data-set/au-core/Practitioner-baratz-layla.json) | [`baratz-layla`](../au-fhir-test-data-set/au-core/PractitionerRole-baratz-layla.json) | [`broome-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-broome-physiotherapy.json) |  |
| [`bassett-elmer`](../au-fhir-test-data-set/au-core/Practitioner-bassett-elmer.json) | [`bassett-elmer`](../au-fhir-test-data-set/au-core/PractitionerRole-bassett-elmer.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`butler-cheryl`](../au-fhir-test-data-set/au-core/Practitioner-butler-cheryl.json) | [`butler-cheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-butler-cheryl.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`clapham-laurie`](../au-fhir-test-data-set/au-core/Practitioner-clapham-laurie.json) | [`clapham-laurie`](../au-fhir-test-data-set/au-core/PractitionerRole-clapham-laurie.json) | [`broome-physiology`](../au-fhir-test-data-set/au-core/Organization-broome-physiology.json) |  |
| [`davies-keiko`](../au-fhir-test-data-set/au-core/Practitioner-davies-keiko.json) | [`davies-keiko`](../au-fhir-test-data-set/au-core/PractitionerRole-davies-keiko.json) | [`broome-nutrition`](../au-fhir-test-data-set/au-core/Organization-broome-nutrition.json) |  |
| [`devine-frank`](../au-fhir-test-data-set/au-core/Practitioner-devine-frank.json) | [`devine-frank`](../au-fhir-test-data-set/au-core/PractitionerRole-devine-frank.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`gates-anton`](../au-fhir-test-data-set/au-core/Practitioner-gates-anton.json) | [`gates-anton`](../au-fhir-test-data-set/au-core/PractitionerRole-gates-anton.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`giles-veronique`](../au-fhir-test-data-set/au-core/Practitioner-giles-veronique.json) | [`giles-veronique`](../au-fhir-test-data-set/au-core/PractitionerRole-giles-veronique.json) | [`broome-optometry`](../au-fhir-test-data-set/au-core/Organization-broome-optometry.json) |  |
| [`goldsmith-monique`](../au-fhir-test-data-set/au-core/Practitioner-goldsmith-monique.json) | [`goldsmith-monique`](../au-fhir-test-data-set/au-core/PractitionerRole-goldsmith-monique.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`hackett-norman`](../au-fhir-test-data-set/au-core/Practitioner-hackett-norman.json) | [`hackett-norman`](../au-fhir-test-data-set/au-core/PractitionerRole-hackett-norman.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`hodges-julia`](../au-fhir-test-data-set/au-core/Practitioner-hodges-julia.json) | [`hodges-julia`](../au-fhir-test-data-set/au-core/PractitionerRole-hodges-julia.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`horn-wes`](../au-fhir-test-data-set/au-core/Practitioner-horn-wes.json) | [`horn-wes`](../au-fhir-test-data-set/au-core/PractitionerRole-horn-wes.json) | [`broome-podiatry`](../au-fhir-test-data-set/au-core/Organization-broome-podiatry.json) |  |
| [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/Practitioner-ibbotson-destiny.json) | [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/PractitionerRole-ibbotson-destiny.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`lowry-bennett`](../au-fhir-test-data-set/au-core/Practitioner-lowry-bennett.json) | [`lowry-bennett`](../au-fhir-test-data-set/au-core/PractitionerRole-lowry-bennett.json) | [`broome-ot-services`](../au-fhir-test-data-set/au-core/Organization-broome-ot-services.json) |  |
| [`moran-linoel`](../au-fhir-test-data-set/au-core/Practitioner-moran-linoel.json) | [`moran-linoel`](../au-fhir-test-data-set/au-core/PractitionerRole-moran-linoel.json) | [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) |  |
| [`patrick-thalia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-thalia.json) | [`patrick-thalia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-thalia.json) | [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) |  |
| [`poulson-lisa`](../au-fhir-test-data-set/au-core/Practitioner-poulson-lisa.json) | [`poulson-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-poulson-lisa.json) | [`broome-community-health`](../au-fhir-test-data-set/au-core/Organization-broome-community-health.json) |  |
| [`simmons-ashton`](../au-fhir-test-data-set/au-core/Practitioner-simmons-ashton.json) | [`simmons-ashton`](../au-fhir-test-data-set/au-core/PractitionerRole-simmons-ashton.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`thorburn-juanita`](../au-fhir-test-data-set/au-core/Practitioner-thorburn-juanita.json) | [`thorburn-juanita`](../au-fhir-test-data-set/au-core/PractitionerRole-thorburn-juanita.json) | [`broome-community-health`](../au-fhir-test-data-set/au-core/Organization-broome-community-health.json) |  |

</details>

</details>

<details><summary><strong>Paeds scenario (5yo)</strong> (56 entities)</summary>

**Patient** (3)

- [`hennessy-billy`](../au-fhir-test-data-set/au-core/Patient-hennessy-billy.json) — *also in: [families](#families)*
- [`hennessy-jenny`](../au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json) — *also in: [families](#families)*
- [`hennessy-kacey`](../au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json) — *also in: [families](#families)*

**Practitioner / PractitionerRole** (17)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`allerton-skye`](../au-fhir-test-data-set/au-core/Practitioner-allerton-skye.json) | [`allerton-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-allerton-skye.json) | Paediatrician (General paediatric specialty) |  |
| [`bennett-tawnya`](../au-fhir-test-data-set/au-core/Practitioner-bennett-tawnya.json) | [`bennett-tawnya`](../au-fhir-test-data-set/au-core/PractitionerRole-bennett-tawnya.json) | Physiotherapist (Physiotherapy) |  |
| [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/Practitioner-colliss-jocelyn.json) | [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/PractitionerRole-colliss-jocelyn.json) | Cardiologist (Cardiology) |  |
| [`harris-stephan`](../au-fhir-test-data-set/au-core/Practitioner-harris-stephan.json) | [`harris-stephan`](../au-fhir-test-data-set/au-core/PractitionerRole-harris-stephan.json) | Pharmacist (Community pharmacy) |  |
| [`harrower-austin`](../au-fhir-test-data-set/au-core/Practitioner-harrower-austin.json) | [`harrower-austin`](../au-fhir-test-data-set/au-core/PractitionerRole-harrower-austin.json) | General Practitioner (General medical practice) |  |
| [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/Practitioner-harwood-kathaleen.json) | [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/PractitionerRole-harwood-kathaleen.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`henderson-elaine`](../au-fhir-test-data-set/au-core/Practitioner-henderson-elaine.json) | [`henderson-elaine`](../au-fhir-test-data-set/au-core/PractitionerRole-henderson-elaine.json) | Paediatrician (General paediatric specialty) |  |
| [`humphreys-christeen`](../au-fhir-test-data-set/au-core/Practitioner-humphreys-christeen.json) | [`humphreys-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-humphreys-christeen.json) | Ophthalmologist (Ophthalmology) |  |
| [`krug-chas`](../au-fhir-test-data-set/au-core/Practitioner-krug-chas.json) | [`krug-chas`](../au-fhir-test-data-set/au-core/PractitionerRole-krug-chas.json) | Occupational Therapist |  |
| [`levings-richard`](../au-fhir-test-data-set/au-core/Practitioner-levings-richard.json) | [`levings-richard`](../au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json) | Dietitian (Dietetics and nutrition) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/Practitioner-mackenzie-wilbur.json) | [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/PractitionerRole-mackenzie-wilbur.json) | Speech Pathologist |  |
| [`maxwell-israel`](../au-fhir-test-data-set/au-core/Practitioner-maxwell-israel.json) | [`maxwell-israel`](../au-fhir-test-data-set/au-core/PractitionerRole-maxwell-israel.json) | Dental Practitioner (Dentistry) |  |
| [`murphy-kyla`](../au-fhir-test-data-set/au-core/Practitioner-murphy-kyla.json) | [`murphy-kyla`](../au-fhir-test-data-set/au-core/PractitionerRole-murphy-kyla.json) | Registered Nurses nec (Nursing) |  |
| [`newling-mariella`](../au-fhir-test-data-set/au-core/Practitioner-newling-mariella.json) | [`newling-mariella`](../au-fhir-test-data-set/au-core/PractitionerRole-newling-mariella.json) | Registered Nurses nec (Nursing) |  |
| [`patrick-tricia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-tricia.json) | [`patrick-tricia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-tricia.json) | Optometrist |  |
| [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/Practitioner-sawtell-tomasa.json) | [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/PractitionerRole-sawtell-tomasa.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) |  |
| [`short-tandra`](../au-fhir-test-data-set/au-core/Practitioner-short-tandra.json) | [`short-tandra`](../au-fhir-test-data-set/au-core/PractitionerRole-short-tandra.json) | Pathologist (Clinical pathology) |  |

**Organization** (13)

- [`garran-cardiology-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-cardiology-clinic.json)
- [`garran-dental`](../au-fhir-test-data-set/au-core/Organization-garran-dental.json)
- [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json)
- [`garran-nephrology`](../au-fhir-test-data-set/au-core/Organization-garran-nephrology.json)
- [`garran-nutrition`](../au-fhir-test-data-set/au-core/Organization-garran-nutrition.json)
- [`garran-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-garran-ophthalmology.json)
- [`garran-optical`](../au-fhir-test-data-set/au-core/Organization-garran-optical.json)
- [`garran-ot-services`](../au-fhir-test-data-set/au-core/Organization-garran-ot-services.json)
- [`garran-pathology`](../au-fhir-test-data-set/au-core/Organization-garran-pathology.json)
- [`garran-pharmacy`](../au-fhir-test-data-set/au-core/Organization-garran-pharmacy.json)
- [`garran-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-garran-physiotherapy.json)
- [`garran-radiology`](../au-fhir-test-data-set/au-core/Organization-garran-radiology.json)
- [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json)

**RelatedPerson** (6)

- [`hennessy-billy-1`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-1.json)
- [`hennessy-billy-2`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-2.json)
- [`hennessy-jenny-1`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-1.json)
- [`hennessy-jenny-2`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-2.json)
- [`hennessy-kacey-1`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-1.json)
- [`hennessy-kacey-2`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-2.json)

<details><summary>17 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`allerton-skye`](../au-fhir-test-data-set/au-core/Practitioner-allerton-skye.json) | [`allerton-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-allerton-skye.json) | [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) |  |
| [`bennett-tawnya`](../au-fhir-test-data-set/au-core/Practitioner-bennett-tawnya.json) | [`bennett-tawnya`](../au-fhir-test-data-set/au-core/PractitionerRole-bennett-tawnya.json) | [`garran-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-garran-physiotherapy.json) |  |
| [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/Practitioner-colliss-jocelyn.json) | [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/PractitionerRole-colliss-jocelyn.json) | [`garran-cardiology-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-cardiology-clinic.json) |  |
| [`harris-stephan`](../au-fhir-test-data-set/au-core/Practitioner-harris-stephan.json) | [`harris-stephan`](../au-fhir-test-data-set/au-core/PractitionerRole-harris-stephan.json) | [`garran-pharmacy`](../au-fhir-test-data-set/au-core/Organization-garran-pharmacy.json) |  |
| [`harrower-austin`](../au-fhir-test-data-set/au-core/Practitioner-harrower-austin.json) | [`harrower-austin`](../au-fhir-test-data-set/au-core/PractitionerRole-harrower-austin.json) | [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) |  |
| [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/Practitioner-harwood-kathaleen.json) | [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/PractitionerRole-harwood-kathaleen.json) | [`garran-radiology`](../au-fhir-test-data-set/au-core/Organization-garran-radiology.json) |  |
| [`henderson-elaine`](../au-fhir-test-data-set/au-core/Practitioner-henderson-elaine.json) | [`henderson-elaine`](../au-fhir-test-data-set/au-core/PractitionerRole-henderson-elaine.json) | [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) |  |
| [`humphreys-christeen`](../au-fhir-test-data-set/au-core/Practitioner-humphreys-christeen.json) | [`humphreys-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-humphreys-christeen.json) | [`garran-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-garran-ophthalmology.json) |  |
| [`krug-chas`](../au-fhir-test-data-set/au-core/Practitioner-krug-chas.json) | [`krug-chas`](../au-fhir-test-data-set/au-core/PractitionerRole-krug-chas.json) | [`garran-ot-services`](../au-fhir-test-data-set/au-core/Organization-garran-ot-services.json) |  |
| [`levings-richard`](../au-fhir-test-data-set/au-core/Practitioner-levings-richard.json) | [`levings-richard`](../au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json) | [`garran-nutrition`](../au-fhir-test-data-set/au-core/Organization-garran-nutrition.json) |  |
| [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/Practitioner-mackenzie-wilbur.json) | [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/PractitionerRole-mackenzie-wilbur.json) | [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) |  |
| [`maxwell-israel`](../au-fhir-test-data-set/au-core/Practitioner-maxwell-israel.json) | [`maxwell-israel`](../au-fhir-test-data-set/au-core/PractitionerRole-maxwell-israel.json) | [`garran-dental`](../au-fhir-test-data-set/au-core/Organization-garran-dental.json) |  |
| [`murphy-kyla`](../au-fhir-test-data-set/au-core/Practitioner-murphy-kyla.json) | [`murphy-kyla`](../au-fhir-test-data-set/au-core/PractitionerRole-murphy-kyla.json) | [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) |  |
| [`newling-mariella`](../au-fhir-test-data-set/au-core/Practitioner-newling-mariella.json) | [`newling-mariella`](../au-fhir-test-data-set/au-core/PractitionerRole-newling-mariella.json) | [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) |  |
| [`patrick-tricia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-tricia.json) | [`patrick-tricia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-tricia.json) | [`garran-optical`](../au-fhir-test-data-set/au-core/Organization-garran-optical.json) |  |
| [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/Practitioner-sawtell-tomasa.json) | [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/PractitionerRole-sawtell-tomasa.json) | [`garran-nephrology`](../au-fhir-test-data-set/au-core/Organization-garran-nephrology.json) |  |
| [`short-tandra`](../au-fhir-test-data-set/au-core/Practitioner-short-tandra.json) | [`short-tandra`](../au-fhir-test-data-set/au-core/PractitionerRole-short-tandra.json) | [`garran-pathology`](../au-fhir-test-data-set/au-core/Organization-garran-pathology.json) |  |

</details>

</details>

<details><summary><strong>Rural &amp; remote scenario</strong> (74 entities)</summary>

**Patient** (1)

- [`mclennan-karl`](../au-fhir-test-data-set/au-core/Patient-mclennan-karl.json)

**Practitioner / PractitionerRole** (28)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`bailey-buck`](../au-fhir-test-data-set/au-core/Practitioner-bailey-buck.json) | [`bailey-buck`](../au-fhir-test-data-set/au-core/PractitionerRole-bailey-buck.json) | Social Worker | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`barrett-kirstie`](../au-fhir-test-data-set/au-core/Practitioner-barrett-kirstie.json) | [`barrett-kirstie`](../au-fhir-test-data-set/au-core/PractitionerRole-barrett-kirstie.json) | Social Worker | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`bowden-hiroko`](../au-fhir-test-data-set/au-core/Practitioner-bowden-hiroko.json) | [`bowden-hiroko`](../au-fhir-test-data-set/au-core/PractitionerRole-bowden-hiroko.json) | Neurosurgeon (Neurosurgery) |  |
| [`gaynor-jasper`](../au-fhir-test-data-set/au-core/Practitioner-gaynor-jasper.json) | [`gaynor-jasper`](../au-fhir-test-data-set/au-core/PractitionerRole-gaynor-jasper.json) | Registered Nurses nec (Nursing) |  |
| [`greenhill-edmond`](../au-fhir-test-data-set/au-core/Practitioner-greenhill-edmond.json) | [`greenhill-edmond`](../au-fhir-test-data-set/au-core/PractitionerRole-greenhill-edmond.json) | Pathologist (Clinical pathology) |  |
| [`haywood-dot`](../au-fhir-test-data-set/au-core/Practitioner-haywood-dot.json) | [`haywood-dot`](../au-fhir-test-data-set/au-core/PractitionerRole-haywood-dot.json) | Gastroenterologist (Gastroenterology) |  |
| [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/Practitioner-hipwood-fatimah.json) | [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/PractitionerRole-hipwood-fatimah.json) | Occupational Therapist | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`hobden-mark`](../au-fhir-test-data-set/au-core/Practitioner-hobden-mark.json) | [`hobden-mark`](../au-fhir-test-data-set/au-core/PractitionerRole-hobden-mark.json) | Pharmacist (Community pharmacy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`hodge-irving`](../au-fhir-test-data-set/au-core/Practitioner-hodge-irving.json) | [`hodge-irving`](../au-fhir-test-data-set/au-core/PractitionerRole-hodge-irving.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) |  |
| [`irwin-corinna`](../au-fhir-test-data-set/au-core/Practitioner-irwin-corinna.json) | [`irwin-corinna`](../au-fhir-test-data-set/au-core/PractitionerRole-irwin-corinna.json) | Emergency Medicine Specialist / Emergency Physician (Emergency medicine) |  |
| [`jeffery-herman`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-herman.json) | [`jeffery-herman`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-herman.json) | Social Worker |  |
| [`jeffery-nicolas`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-nicolas.json) | [`jeffery-nicolas`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-nicolas.json) | Pathologist (Clinical pathology) |  |
| [`jeffery-sammy`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json) | [`jeffery-sammy`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json) | Physiotherapist (Physiotherapy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/Practitioner-livingstone-yvonne.json) | [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/PractitionerRole-livingstone-yvonne.json) | Physiotherapist (Physiotherapy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`lyons-shay`](../au-fhir-test-data-set/au-core/Practitioner-lyons-shay.json) | [`lyons-shay`](../au-fhir-test-data-set/au-core/PractitionerRole-lyons-shay.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`mccormack-gertie`](../au-fhir-test-data-set/au-core/Practitioner-mccormack-gertie.json) | [`mccormack-gertie`](../au-fhir-test-data-set/au-core/PractitionerRole-mccormack-gertie.json) | Clinical Psychologist (Clinical psychology) |  |
| [`mcintyre-hsiu`](../au-fhir-test-data-set/au-core/Practitioner-mcintyre-hsiu.json) | [`mcintyre-hsiu`](../au-fhir-test-data-set/au-core/PractitionerRole-mcintyre-hsiu.json) | General Practitioner (General medical practice) |  |
| [`mclean-brenda`](../au-fhir-test-data-set/au-core/Practitioner-mclean-brenda.json) | [`mclean-brenda`](../au-fhir-test-data-set/au-core/PractitionerRole-mclean-brenda.json) | Orthopaedic Surgeon (Surgical orthopedic specialty) |  |
| [`mills-kim`](../au-fhir-test-data-set/au-core/Practitioner-mills-kim.json) | [`mills-kim`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-kim.json) | Cardiologist (Cardiology) |  |
| [`murray-xenia`](../au-fhir-test-data-set/au-core/Practitioner-murray-xenia.json) | [`murray-xenia`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-xenia.json) | Pharmacist (Community pharmacy) |  |
| [`oritz-philomena`](../au-fhir-test-data-set/au-core/Practitioner-oritz-philomena.json) | [`oritz-philomena`](../au-fhir-test-data-set/au-core/PractitionerRole-oritz-philomena.json) | Registered Nurses nec (Nursing) |  |
| [`osborne-buster`](../au-fhir-test-data-set/au-core/Practitioner-osborne-buster.json) | [`osborne-buster`](../au-fhir-test-data-set/au-core/PractitionerRole-osborne-buster.json) | Emergency Medicine Specialist / Emergency Physician (Emergency medicine) |  |
| [`pearce-teresa`](../au-fhir-test-data-set/au-core/Practitioner-pearce-teresa.json) | [`pearce-teresa`](../au-fhir-test-data-set/au-core/PractitionerRole-pearce-teresa.json) | Urologist (Urology) |  |
| [`potts-xuan`](../au-fhir-test-data-set/au-core/Practitioner-potts-xuan.json) | [`potts-xuan`](../au-fhir-test-data-set/au-core/PractitionerRole-potts-xuan.json) | Dental Practitioner (Dentistry) |  |
| [`pratt-colleen`](../au-fhir-test-data-set/au-core/Practitioner-pratt-colleen.json) | [`pratt-colleen`](../au-fhir-test-data-set/au-core/PractitionerRole-pratt-colleen.json) | General Practitioner (General medical practice) |  |
| [`randall-anthony`](../au-fhir-test-data-set/au-core/Practitioner-randall-anthony.json) | [`randall-anthony`](../au-fhir-test-data-set/au-core/PractitionerRole-randall-anthony.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/Practitioner-robbins-wilhelmina.json) | [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/PractitionerRole-robbins-wilhelmina.json) | Nurse Practitioner (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`sherry-dean`](../au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json) | [`sherry-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json) | Occupational Therapist | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**Organization** (17)

- [`camooweal-community-health`](../au-fhir-test-data-set/au-core/Organization-camooweal-community-health.json)
- [`camooweal-pharmacy`](../au-fhir-test-data-set/au-core/Organization-camooweal-pharmacy.json)
- [`herston-pathology`](../au-fhir-test-data-set/au-core/Organization-herston-pathology.json)
- [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json)
- [`herston-radiology`](../au-fhir-test-data-set/au-core/Organization-herston-radiology.json)
- [`mt-isa-community-health`](../au-fhir-test-data-set/au-core/Organization-mt-isa-community-health.json)
- [`mt-isa-dental`](../au-fhir-test-data-set/au-core/Organization-mt-isa-dental.json)
- [`mt-isa-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-medical-clinic.json)
- [`mt-isa-ot-services`](../au-fhir-test-data-set/au-core/Organization-mt-isa-ot-services.json)
- [`mt-isa-pathology`](../au-fhir-test-data-set/au-core/Organization-mt-isa-pathology.json)
- [`mt-isa-pharmacy`](../au-fhir-test-data-set/au-core/Organization-mt-isa-pharmacy.json)
- [`mt-isa-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-mt-isa-physiotherapy.json)
- [`mt-isa-psychology`](../au-fhir-test-data-set/au-core/Organization-mt-isa-psychology.json)
- [`mt-isa-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-specialist-clinic.json)
- [`townsville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-townsville-medical-clinic.json)
- [`townsville-public-hospital`](../au-fhir-test-data-set/au-core/Organization-townsville-public-hospital.json)
- [`townsville-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-townsville-specialist-clinic.json)

<details><summary>28 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`bailey-buck`](../au-fhir-test-data-set/au-core/Practitioner-bailey-buck.json) | [`bailey-buck`](../au-fhir-test-data-set/au-core/PractitionerRole-bailey-buck.json) | [`townsville-public-hospital`](../au-fhir-test-data-set/au-core/Organization-townsville-public-hospital.json) |  |
| [`barrett-kirstie`](../au-fhir-test-data-set/au-core/Practitioner-barrett-kirstie.json) | [`barrett-kirstie`](../au-fhir-test-data-set/au-core/PractitionerRole-barrett-kirstie.json) | [`mt-isa-community-health`](../au-fhir-test-data-set/au-core/Organization-mt-isa-community-health.json) |  |
| [`bowden-hiroko`](../au-fhir-test-data-set/au-core/Practitioner-bowden-hiroko.json) | [`bowden-hiroko`](../au-fhir-test-data-set/au-core/PractitionerRole-bowden-hiroko.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`gaynor-jasper`](../au-fhir-test-data-set/au-core/Practitioner-gaynor-jasper.json) | [`gaynor-jasper`](../au-fhir-test-data-set/au-core/PractitionerRole-gaynor-jasper.json) | [`townsville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-townsville-medical-clinic.json) |  |
| [`greenhill-edmond`](../au-fhir-test-data-set/au-core/Practitioner-greenhill-edmond.json) | [`greenhill-edmond`](../au-fhir-test-data-set/au-core/PractitionerRole-greenhill-edmond.json) | [`herston-pathology`](../au-fhir-test-data-set/au-core/Organization-herston-pathology.json) |  |
| [`haywood-dot`](../au-fhir-test-data-set/au-core/Practitioner-haywood-dot.json) | [`haywood-dot`](../au-fhir-test-data-set/au-core/PractitionerRole-haywood-dot.json) | [`mt-isa-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-specialist-clinic.json) |  |
| [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/Practitioner-hipwood-fatimah.json) | [`hipwood-fatimah`](../au-fhir-test-data-set/au-core/PractitionerRole-hipwood-fatimah.json) | [`mt-isa-ot-services`](../au-fhir-test-data-set/au-core/Organization-mt-isa-ot-services.json) |  |
| [`hobden-mark`](../au-fhir-test-data-set/au-core/Practitioner-hobden-mark.json) | [`hobden-mark`](../au-fhir-test-data-set/au-core/PractitionerRole-hobden-mark.json) | [`camooweal-pharmacy`](../au-fhir-test-data-set/au-core/Organization-camooweal-pharmacy.json) |  |
| [`hodge-irving`](../au-fhir-test-data-set/au-core/Practitioner-hodge-irving.json) | [`hodge-irving`](../au-fhir-test-data-set/au-core/PractitionerRole-hodge-irving.json) | [`mt-isa-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-specialist-clinic.json) |  |
| [`irwin-corinna`](../au-fhir-test-data-set/au-core/Practitioner-irwin-corinna.json) | [`irwin-corinna`](../au-fhir-test-data-set/au-core/PractitionerRole-irwin-corinna.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`jeffery-herman`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-herman.json) | [`jeffery-herman`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-herman.json) | [`camooweal-community-health`](../au-fhir-test-data-set/au-core/Organization-camooweal-community-health.json) |  |
| [`jeffery-nicolas`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-nicolas.json) | [`jeffery-nicolas`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-nicolas.json) | [`mt-isa-pathology`](../au-fhir-test-data-set/au-core/Organization-mt-isa-pathology.json) |  |
| [`jeffery-sammy`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json) | [`jeffery-sammy`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/Practitioner-livingstone-yvonne.json) | [`livingstone-yvonne`](../au-fhir-test-data-set/au-core/PractitionerRole-livingstone-yvonne.json) | [`mt-isa-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-mt-isa-physiotherapy.json) |  |
| [`lyons-shay`](../au-fhir-test-data-set/au-core/Practitioner-lyons-shay.json) | [`lyons-shay`](../au-fhir-test-data-set/au-core/PractitionerRole-lyons-shay.json) | [`herston-radiology`](../au-fhir-test-data-set/au-core/Organization-herston-radiology.json) |  |
| [`mccormack-gertie`](../au-fhir-test-data-set/au-core/Practitioner-mccormack-gertie.json) | [`mccormack-gertie`](../au-fhir-test-data-set/au-core/PractitionerRole-mccormack-gertie.json) | [`mt-isa-psychology`](../au-fhir-test-data-set/au-core/Organization-mt-isa-psychology.json) |  |
| [`mcintyre-hsiu`](../au-fhir-test-data-set/au-core/Practitioner-mcintyre-hsiu.json) | [`mcintyre-hsiu`](../au-fhir-test-data-set/au-core/PractitionerRole-mcintyre-hsiu.json) | [`townsville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-townsville-medical-clinic.json) |  |
| [`mclean-brenda`](../au-fhir-test-data-set/au-core/Practitioner-mclean-brenda.json) | [`mclean-brenda`](../au-fhir-test-data-set/au-core/PractitionerRole-mclean-brenda.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`mills-kim`](../au-fhir-test-data-set/au-core/Practitioner-mills-kim.json) | [`mills-kim`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-kim.json) | [`mt-isa-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-specialist-clinic.json) |  |
| [`murray-xenia`](../au-fhir-test-data-set/au-core/Practitioner-murray-xenia.json) | [`murray-xenia`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-xenia.json) | [`mt-isa-pharmacy`](../au-fhir-test-data-set/au-core/Organization-mt-isa-pharmacy.json) |  |
| [`oritz-philomena`](../au-fhir-test-data-set/au-core/Practitioner-oritz-philomena.json) | [`oritz-philomena`](../au-fhir-test-data-set/au-core/PractitionerRole-oritz-philomena.json) | [`camooweal-community-health`](../au-fhir-test-data-set/au-core/Organization-camooweal-community-health.json) |  |
| [`osborne-buster`](../au-fhir-test-data-set/au-core/Practitioner-osborne-buster.json) | [`osborne-buster`](../au-fhir-test-data-set/au-core/PractitionerRole-osborne-buster.json) | [`townsville-public-hospital`](../au-fhir-test-data-set/au-core/Organization-townsville-public-hospital.json) |  |
| [`pearce-teresa`](../au-fhir-test-data-set/au-core/Practitioner-pearce-teresa.json) | [`pearce-teresa`](../au-fhir-test-data-set/au-core/PractitionerRole-pearce-teresa.json) | [`townsville-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-townsville-specialist-clinic.json) |  |
| [`potts-xuan`](../au-fhir-test-data-set/au-core/Practitioner-potts-xuan.json) | [`potts-xuan`](../au-fhir-test-data-set/au-core/PractitionerRole-potts-xuan.json) | [`mt-isa-dental`](../au-fhir-test-data-set/au-core/Organization-mt-isa-dental.json) |  |
| [`pratt-colleen`](../au-fhir-test-data-set/au-core/Practitioner-pratt-colleen.json) | [`pratt-colleen`](../au-fhir-test-data-set/au-core/PractitionerRole-pratt-colleen.json) | [`mt-isa-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-medical-clinic.json) |  |
| [`randall-anthony`](../au-fhir-test-data-set/au-core/Practitioner-randall-anthony.json) | [`randall-anthony`](../au-fhir-test-data-set/au-core/PractitionerRole-randall-anthony.json) | [`mt-isa-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-mt-isa-medical-clinic.json) |  |
| [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/Practitioner-robbins-wilhelmina.json) | [`robbins-wilhelmina`](../au-fhir-test-data-set/au-core/PractitionerRole-robbins-wilhelmina.json) | [`camooweal-community-health`](../au-fhir-test-data-set/au-core/Organization-camooweal-community-health.json) |  |
| [`sherry-dean`](../au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json) | [`sherry-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |

</details>

</details>

<details><summary><strong>Young adult_adolescent scenario (19-20 yo)</strong> (46 entities)</summary>

**Patient** (1)

- [`vaughan-seymour`](../au-fhir-test-data-set/au-core/Patient-vaughan-seymour.json)

**Practitioner / PractitionerRole** (18)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`alcock-devon`](../au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json) | [`alcock-devon`](../au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`blackwood-ella`](../au-fhir-test-data-set/au-core/Practitioner-blackwood-ella.json) | [`blackwood-ella`](../au-fhir-test-data-set/au-core/PractitionerRole-blackwood-ella.json) | Social Worker |  |
| [`dempsey-carli`](../au-fhir-test-data-set/au-core/Practitioner-dempsey-carli.json) | [`dempsey-carli`](../au-fhir-test-data-set/au-core/PractitionerRole-dempsey-carli.json) | Clinical Immunologist (Clinical immunology) |  |
| [`egan-anja`](../au-fhir-test-data-set/au-core/Practitioner-egan-anja.json) | [`egan-anja`](../au-fhir-test-data-set/au-core/PractitionerRole-egan-anja.json) | Counsellor (Clinical psychology) |  |
| [`findley-betty`](../au-fhir-test-data-set/au-core/Practitioner-findley-betty.json) | [`findley-betty`](../au-fhir-test-data-set/au-core/PractitionerRole-findley-betty.json) | Sleep Medicine Specialist |  |
| [`frankel-caroline`](../au-fhir-test-data-set/au-core/Practitioner-frankel-caroline.json) | [`frankel-caroline`](../au-fhir-test-data-set/au-core/PractitionerRole-frankel-caroline.json) | Registered Nurses nec (Nursing) |  |
| [`greene-delores`](../au-fhir-test-data-set/au-core/Practitioner-greene-delores.json) | [`greene-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json) | Paediatrician (General paediatric specialty) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`hatcher-merrill`](../au-fhir-test-data-set/au-core/Practitioner-hatcher-merrill.json) | [`hatcher-merrill`](../au-fhir-test-data-set/au-core/PractitionerRole-hatcher-merrill.json) | Nurse Practitioner (Nursing) |  |
| [`higgs-allegra`](../au-fhir-test-data-set/au-core/Practitioner-higgs-allegra.json) | [`higgs-allegra`](../au-fhir-test-data-set/au-core/PractitionerRole-higgs-allegra.json) | Physiotherapist (Physiotherapy) |  |
| [`hilton-della`](../au-fhir-test-data-set/au-core/Practitioner-hilton-della.json) | [`hilton-della`](../au-fhir-test-data-set/au-core/PractitionerRole-hilton-della.json) | Clinical Psychologist (Clinical psychology) |  |
| [`joyce-mae`](../au-fhir-test-data-set/au-core/Practitioner-joyce-mae.json) | [`joyce-mae`](../au-fhir-test-data-set/au-core/PractitionerRole-joyce-mae.json) | Exercise Physiologist |  |
| [`keith-margot`](../au-fhir-test-data-set/au-core/Practitioner-keith-margot.json) | [`keith-margot`](../au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json) | General Practitioner (General medical practice) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`laing-malinda`](../au-fhir-test-data-set/au-core/Practitioner-laing-malinda.json) | [`laing-malinda`](../au-fhir-test-data-set/au-core/PractitionerRole-laing-malinda.json) | Endocrinologist (Endocrinology) |  |
| [`mckane-eugena`](../au-fhir-test-data-set/au-core/Practitioner-mckane-eugena.json) | [`mckane-eugena`](../au-fhir-test-data-set/au-core/PractitionerRole-mckane-eugena.json) | Registered Nurses nec (Nursing) |  |
| [`mullin-kenny`](../au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json) | [`mullin-kenny`](../au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json) | Speech Pathologist | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`murray-ashli`](../au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json) | [`murray-ashli`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json) | Occupational Therapist | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`rodd-illa`](../au-fhir-test-data-set/au-core/Practitioner-rodd-illa.json) | [`rodd-illa`](../au-fhir-test-data-set/au-core/PractitionerRole-rodd-illa.json) | Endocrinologist (Endocrinology) |  |
| [`shephard-vern`](../au-fhir-test-data-set/au-core/Practitioner-shephard-vern.json) | [`shephard-vern`](../au-fhir-test-data-set/au-core/PractitionerRole-shephard-vern.json) | Psychiatrist (Psychiatry) |  |

**Organization** (9)

- [`melbourne-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json)
- [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json)
- [`southbank-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json)
- [`southbank-speech-pathology`](../au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json)
- [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json)
- [`st-kilda-ot-services`](../au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json)
- [`st-kilda-physiology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiology.json)
- [`st-kilda-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiotherapy.json)
- [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json)

<details><summary>18 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`alcock-devon`](../au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json) | [`alcock-devon`](../au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |
| [`blackwood-ella`](../au-fhir-test-data-set/au-core/Practitioner-blackwood-ella.json) | [`blackwood-ella`](../au-fhir-test-data-set/au-core/PractitionerRole-blackwood-ella.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |
| [`dempsey-carli`](../au-fhir-test-data-set/au-core/Practitioner-dempsey-carli.json) | [`dempsey-carli`](../au-fhir-test-data-set/au-core/PractitionerRole-dempsey-carli.json) | [`melbourne-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json) |  |
| [`egan-anja`](../au-fhir-test-data-set/au-core/Practitioner-egan-anja.json) | [`egan-anja`](../au-fhir-test-data-set/au-core/PractitionerRole-egan-anja.json) | [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) |  |
| [`findley-betty`](../au-fhir-test-data-set/au-core/Practitioner-findley-betty.json) | [`findley-betty`](../au-fhir-test-data-set/au-core/PractitionerRole-findley-betty.json) | [`southbank-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json) |  |
| [`frankel-caroline`](../au-fhir-test-data-set/au-core/Practitioner-frankel-caroline.json) | [`frankel-caroline`](../au-fhir-test-data-set/au-core/PractitionerRole-frankel-caroline.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |
| [`greene-delores`](../au-fhir-test-data-set/au-core/Practitioner-greene-delores.json) | [`greene-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |
| [`hatcher-merrill`](../au-fhir-test-data-set/au-core/Practitioner-hatcher-merrill.json) | [`hatcher-merrill`](../au-fhir-test-data-set/au-core/PractitionerRole-hatcher-merrill.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |
| [`higgs-allegra`](../au-fhir-test-data-set/au-core/Practitioner-higgs-allegra.json) | [`higgs-allegra`](../au-fhir-test-data-set/au-core/PractitionerRole-higgs-allegra.json) | [`st-kilda-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiotherapy.json) |  |
| [`hilton-della`](../au-fhir-test-data-set/au-core/Practitioner-hilton-della.json) | [`hilton-della`](../au-fhir-test-data-set/au-core/PractitionerRole-hilton-della.json) | [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) |  |
| [`joyce-mae`](../au-fhir-test-data-set/au-core/Practitioner-joyce-mae.json) | [`joyce-mae`](../au-fhir-test-data-set/au-core/PractitionerRole-joyce-mae.json) | [`st-kilda-physiology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiology.json) |  |
| [`keith-margot`](../au-fhir-test-data-set/au-core/Practitioner-keith-margot.json) | [`keith-margot`](../au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |
| [`laing-malinda`](../au-fhir-test-data-set/au-core/Practitioner-laing-malinda.json) | [`laing-malinda`](../au-fhir-test-data-set/au-core/PractitionerRole-laing-malinda.json) | [`southbank-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json) |  |
| [`mckane-eugena`](../au-fhir-test-data-set/au-core/Practitioner-mckane-eugena.json) | [`mckane-eugena`](../au-fhir-test-data-set/au-core/PractitionerRole-mckane-eugena.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |
| [`mullin-kenny`](../au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json) | [`mullin-kenny`](../au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json) | [`southbank-speech-pathology`](../au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json) |  |
| [`murray-ashli`](../au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json) | [`murray-ashli`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json) | [`st-kilda-ot-services`](../au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json) |  |
| [`rodd-illa`](../au-fhir-test-data-set/au-core/Practitioner-rodd-illa.json) | [`rodd-illa`](../au-fhir-test-data-set/au-core/PractitionerRole-rodd-illa.json) | [`melbourne-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json) |  |
| [`shephard-vern`](../au-fhir-test-data-set/au-core/Practitioner-shephard-vern.json) | [`shephard-vern`](../au-fhir-test-data-set/au-core/PractitionerRole-shephard-vern.json) | [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) |  |

</details>

</details>


## Geographic groupings <a id="geography-groups"></a>

### Purpose

Proposes groupings of entities that are plausibly co-located, as a starting point for constructing new consumer journeys.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Grouping identifies plausible co-location only, and does not itself reserve a member to its group. That does not make a member free to build on — many are also IG examples or test patients, which those subsets reserve. What governs an entity is the tightest constraint across all of its memberships, so check its other listings before adding to it.

### Provenance & use

Proposed by a script from address data and confirmed by a human. Best- effort by design: postcode proximity is a weak proxy, and there are no coordinates anywhere in the data set to check real distance against.

### Relationships

[Scenario groupings](#scenario-groups) draw heavily on the same entities, since each scenario was built around a specific locality.

### How is this subset identified?

Derived, then curated by human confirmation. Metro entities group by capital city; regional entities group by three-digit postcode bucket, widened to buckets whose third digit differs by one. Each grouping is then expanded by reverse reference to pull in the HealthcareServices and PractitionerRoles attached to its organisations, locations and practitioners. Every proposal is put to a human with its full suburb list, which stands in for the distance check the data cannot support.

<details><summary>Derivation notes</summary>

> 8 metro groups (one per capital city) and 85 regional windows (3-digit postcode bucket, widened to buckets whose 3rd digit is +/-1).
> 467 geo-eligible entities have no usable postcode and are excluded.
> 11 entities have a non-Australian address and are excluded — Australian postcode logic does not apply to them, and their postcodes collide with Australian ones (Napier NZ 4104 falls inside Brisbane's metro range).
> 60 confirmed, 33 rejected, 0 awaiting a decision.
> Metro groups by city because Australian postcodes are not spatially ordered — Southbank 3006 and St Kilda 3182 are ~6km apart but differ in the 3rd digit by 8.
> LIMITATION: a regional window can still span great distances where postcodes cover vast areas (Townsville 4810 and Mount Isa 4825 are +/-1 adjacent but ~900km apart). Check each candidate's suburb list — there are no coordinates in the data set to check distance against.

</details>


### Members (1022)

<details><summary><strong>ACT</strong> (1 grouping, 128 entities)</summary>

<blockquote>
<details><summary><strong>Canberra metropolitan</strong> (128 entities)</summary>


_Bonython, Calwell, Chisholm, Conder, Curtin, Erindale Centre, Garran, Gilmore, Ginninderra Village, Gordon, Gowrie, Macarthur, Manuka, Mitchell, Monash, Ngunnawal, Nicholls, Oxley, Palmerston, Reid, Richardson._


**Patient** (13)

| ID | Also in |
| --- | --- |
| [`black-kerry-dougal`](../au-fhir-test-data-set/au-core/Patient-black-kerry-dougal.json) |  |
| [`davis-juan`](../au-fhir-test-data-set/au-core/Patient-davis-juan.json) |  |
| [`dietrich-blake-louis`](../au-fhir-test-data-set/au-core/Patient-dietrich-blake-louis.json) | *[families](#families)* |
| [`dietrich-diedre-alicia`](../au-fhir-test-data-set/au-core/Patient-dietrich-diedre-alicia.json) | *[families](#families)* |
| [`dietrich-kimbra-althea`](../au-fhir-test-data-set/au-core/Patient-dietrich-kimbra-althea.json) | *[families](#families)* |
| [`dietrich-phillipa-grace`](../au-fhir-test-data-set/au-core/Patient-dietrich-phillipa-grace.json) | *[families](#families)* |
| [`downie-grant`](../au-fhir-test-data-set/au-core/Patient-downie-grant.json) |  |
| [`hennessy-billy`](../au-fhir-test-data-set/au-core/Patient-hennessy-billy.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-jenny`](../au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-kacey`](../au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json) | *[scenario-groups](#scenario-groups)* |
| [`hulme-brant`](../au-fhir-test-data-set/au-core/Patient-hulme-brant.json) |  |
| [`ridgewell-troy`](../au-fhir-test-data-set/au-core/Patient-ridgewell-troy.json) |  |
| [`scott-elijah-ken`](../au-fhir-test-data-set/au-erequesting/Patient-scott-elijah-ken.json) | *[au-erequesting-ig-examples](#au-erequesting-ig-examples)* |

**Practitioner / PractitionerRole** (42)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`alderson-helene`](../au-fhir-test-data-set/au-core/Practitioner-alderson-helene.json) | [`medicaldiagnostic-alderson-helene`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-alderson-helene.json) | Medical Diagnostic Radiographer |  |
| [`allen-yelena`](../au-fhir-test-data-set/au-core/Practitioner-allen-yelena.json) |  |  |  |
| [`allerton-skye`](../au-fhir-test-data-set/au-core/Practitioner-allerton-skye.json) | [`allerton-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-allerton-skye.json) | Paediatrician (General paediatric specialty) | [scenario-groups](#scenario-groups) |
| [`becker-valentina`](../au-fhir-test-data-set/au-core/Practitioner-becker-valentina.json) |  |  |  |
| [`bennett-tawnya`](../au-fhir-test-data-set/au-core/Practitioner-bennett-tawnya.json) | [`bennett-tawnya`](../au-fhir-test-data-set/au-core/PractitionerRole-bennett-tawnya.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups) |
| [`bishop-horace`](../au-fhir-test-data-set/au-core/Practitioner-bishop-horace.json) | [`generalpractitioner-bishop-horace`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-bishop-horace.json) | General Practitioner (General medical practice) |  |
| [`briggs-cheyenne`](../au-fhir-test-data-set/au-core/Practitioner-briggs-cheyenne.json) |  |  |  |
| [`brooksby-susanna`](../au-fhir-test-data-set/au-core/Practitioner-brooksby-susanna.json) |  |  |  |
| [`cohen-jamel`](../au-fhir-test-data-set/au-core/Practitioner-cohen-jamel.json) | [`nursepractitioner-cohen-jamel`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-cohen-jamel.json) | Nurse Practitioner (Nursing) |  |
| [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/Practitioner-colliss-jocelyn.json) | [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/PractitionerRole-colliss-jocelyn.json) | Cardiologist (Cardiology) | [scenario-groups](#scenario-groups) |
| [`cross-lizzie`](../au-fhir-test-data-set/au-core/Practitioner-cross-lizzie.json) | [`surgeongeneral-cross-lizzie`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-cross-lizzie.json) | Surgeon (General) (General surgery) |  |
| [`donaldson-stephanie`](../au-fhir-test-data-set/au-core/Practitioner-donaldson-stephanie.json) | [`registerednurses-donaldson-stephanie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-donaldson-stephanie.json) | Registered Nurses nec (Nursing) |  |
| [`gidley-stan`](../au-fhir-test-data-set/au-core/Practitioner-gidley-stan.json) | [`registerednurses-gidley-stan`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-stan.json) | Registered Nurses nec (Nursing) |  |
| [`gilkinson-tyron`](../au-fhir-test-data-set/au-core/Practitioner-gilkinson-tyron.json) |  |  |  |
| [`grant-lindsay`](../au-fhir-test-data-set/au-core/Practitioner-grant-lindsay.json) | [`nursepractitioner-grant-lindsay`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-grant-lindsay.json) | Nurse Practitioner (Nursing) |  |
| [`harris-stephan`](../au-fhir-test-data-set/au-core/Practitioner-harris-stephan.json) | [`harris-stephan`](../au-fhir-test-data-set/au-core/PractitionerRole-harris-stephan.json) | Pharmacist (Community pharmacy) | [scenario-groups](#scenario-groups) |
| [`harrower-austin`](../au-fhir-test-data-set/au-core/Practitioner-harrower-austin.json) | [`harrower-austin`](../au-fhir-test-data-set/au-core/PractitionerRole-harrower-austin.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups) |
| [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/Practitioner-harwood-kathaleen.json) | [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/PractitionerRole-harwood-kathaleen.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [scenario-groups](#scenario-groups) |
| [`henderson-elaine`](../au-fhir-test-data-set/au-core/Practitioner-henderson-elaine.json) | [`henderson-elaine`](../au-fhir-test-data-set/au-core/PractitionerRole-henderson-elaine.json) | Paediatrician (General paediatric specialty) | [scenario-groups](#scenario-groups) |
| [`hill-maryln`](../au-fhir-test-data-set/au-core/Practitioner-hill-maryln.json) | [`diagnostic-hill-maryln`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-hill-maryln.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`humphreys-christeen`](../au-fhir-test-data-set/au-core/Practitioner-humphreys-christeen.json) | [`humphreys-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-humphreys-christeen.json) | Ophthalmologist (Ophthalmology) | [scenario-groups](#scenario-groups) |
| [`krug-chas`](../au-fhir-test-data-set/au-core/Practitioner-krug-chas.json) | [`krug-chas`](../au-fhir-test-data-set/au-core/PractitionerRole-krug-chas.json) | Occupational Therapist | [scenario-groups](#scenario-groups) |
| [`lees-noreen`](../au-fhir-test-data-set/au-core/Practitioner-lees-noreen.json) | [`retailpharmacist-lees-noreen`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-lees-noreen.json) | Retail Pharmacist (Community pharmacy) |  |
| [`levings-richard`](../au-fhir-test-data-set/au-core/Practitioner-levings-richard.json) | [`levings-richard`](../au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json) | Dietitian (Dietetics and nutrition) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/Practitioner-mackenzie-wilbur.json) | [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/PractitionerRole-mackenzie-wilbur.json) | Speech Pathologist | [scenario-groups](#scenario-groups) |
| [`maxwell-israel`](../au-fhir-test-data-set/au-core/Practitioner-maxwell-israel.json) | [`maxwell-israel`](../au-fhir-test-data-set/au-core/PractitionerRole-maxwell-israel.json) | Dental Practitioner (Dentistry) | [scenario-groups](#scenario-groups) |
| [`mccarthy-heide`](../au-fhir-test-data-set/au-core/Practitioner-mccarthy-heide.json) |  |  |  |
| [`mcmahon-yasuko`](../au-fhir-test-data-set/au-core/Practitioner-mcmahon-yasuko.json) |  |  |  |
| [`murphy-kyla`](../au-fhir-test-data-set/au-core/Practitioner-murphy-kyla.json) | [`murphy-kyla`](../au-fhir-test-data-set/au-core/PractitionerRole-murphy-kyla.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`murphy-virginia`](../au-fhir-test-data-set/au-core/Practitioner-murphy-virginia.json) |  |  |  |
| [`nairn-ricky`](../au-fhir-test-data-set/au-core/Practitioner-nairn-ricky.json) | [`registerednurses-nairn-ricky`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-nairn-ricky.json) | Registered Nurses nec (Nursing) |  |
| [`newling-mariella`](../au-fhir-test-data-set/au-core/Practitioner-newling-mariella.json) | [`newling-mariella`](../au-fhir-test-data-set/au-core/PractitionerRole-newling-mariella.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`parkinson-ethel`](../au-fhir-test-data-set/au-core/Practitioner-parkinson-ethel.json) |  |  |  |
| [`patrick-tricia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-tricia.json) | [`patrick-tricia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-tricia.json) | Optometrist | [scenario-groups](#scenario-groups) |
| [`pickford-aimee`](../au-fhir-test-data-set/au-core/Practitioner-pickford-aimee.json) | [`surgeongeneral-pickford-aimee`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-pickford-aimee.json) | Surgeon (General) (General surgery) |  |
| [`pollock-dinah`](../au-fhir-test-data-set/au-core/Practitioner-pollock-dinah.json) | [`midwife-pollock-dinah`](../au-fhir-test-data-set/au-core/PractitionerRole-midwife-pollock-dinah.json) | Midwife (Obstetric nursing) |  |
| [`rowlands-alvera`](../au-fhir-test-data-set/au-core/Practitioner-rowlands-alvera.json) | [`paediatrician-rowlands-alvera`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-rowlands-alvera.json) | Paediatrician (General paediatric specialty) |  |
| [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/Practitioner-sawtell-tomasa.json) | [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/PractitionerRole-sawtell-tomasa.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) | [scenario-groups](#scenario-groups) |
| [`seymour-sol`](../au-fhir-test-data-set/au-core/Practitioner-seymour-sol.json) |  |  |  |
| [`short-tandra`](../au-fhir-test-data-set/au-core/Practitioner-short-tandra.json) | [`short-tandra`](../au-fhir-test-data-set/au-core/PractitionerRole-short-tandra.json) | Pathologist (Clinical pathology) | [scenario-groups](#scenario-groups) |
| [`stevens-chelsea`](../au-fhir-test-data-set/au-core/Practitioner-stevens-chelsea.json) | [`pathologist-stevens-chelsea`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-stevens-chelsea.json) | Pathologist (Pathology) |  |
| [`turnbull-daniel`](../au-fhir-test-data-set/au-core/Practitioner-turnbull-daniel.json) |  |  |  |

**HealthcareService** (6)

- [`diagnosticimaging-nicholls-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-nicholls-radiology.json)
- [`generalmedical-ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-ngunnawal-medical-practice.json)
- [`pathologylaboratory-calwell-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-calwell-pathology.json)
- [`pharmacyretail-ginninderra-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-ginninderra-pharmacy.json)
- [`privateacute-monash-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-monash-private-hospital.json)
- [`publicacute-oxley-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-oxley-public-hospital.json)

**Organization** (21)

| ID | Also in |
| --- | --- |
| [`calwell-pathology`](../au-fhir-test-data-set/au-core/Organization-calwell-pathology.json) |  |
| [`curtin-care-and-support`](../au-fhir-test-data-set/au-core/Organization-curtain-care-and-support.json) | *[community-contributions](#community-contributions)* |
| [`garran-cardiology-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-cardiology-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-dental`](../au-fhir-test-data-set/au-core/Organization-garran-dental.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-nephrology`](../au-fhir-test-data-set/au-core/Organization-garran-nephrology.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-nutrition`](../au-fhir-test-data-set/au-core/Organization-garran-nutrition.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-garran-ophthalmology.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-optical`](../au-fhir-test-data-set/au-core/Organization-garran-optical.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-ot-services`](../au-fhir-test-data-set/au-core/Organization-garran-ot-services.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-pathology`](../au-fhir-test-data-set/au-core/Organization-garran-pathology.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-pharmacy`](../au-fhir-test-data-set/au-core/Organization-garran-pharmacy.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-garran-physiotherapy.json) | *[scenario-groups](#scenario-groups)* |
| [`garran-radiology`](../au-fhir-test-data-set/au-core/Organization-garran-radiology.json) | *[scenario-groups](#scenario-groups)* |
| [`ginninderra-pharmacy`](../au-fhir-test-data-set/au-core/Organization-ginninderra-pharmacy.json) |  |
| [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) | *[scenario-groups](#scenario-groups)* |
| [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Organization-monash-private-hospital.json) |  |
| [`ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/Organization-ngunnawal-medical-practice.json) |  |
| [`nicholls-radiology`](../au-fhir-test-data-set/au-core/Organization-nicholls-radiology.json) |  |
| [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Organization-oxley-public-hospital.json) |  |
| [`reid-health-network`](../au-fhir-test-data-set/au-core/Organization-reid-health-network.json) | *[community-contributions](#community-contributions)* |

**Location** (6)

- [`calwell-pathology`](../au-fhir-test-data-set/au-core/Location-calwell-pathology.json)
- [`ginninderra-pharmacy`](../au-fhir-test-data-set/au-core/Location-ginninderra-pharmacy.json)
- [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Location-monash-private-hospital.json)
- [`ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/Location-ngunnawal-medical-practice.json)
- [`nicholls-radiology`](../au-fhir-test-data-set/au-core/Location-nicholls-radiology.json)
- [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Location-oxley-public-hospital.json)

**RelatedPerson** (9)

| ID | Also in |
| --- | --- |
| [`dietrich-phillipa-2`](../au-fhir-test-data-set/au-core/RelatedPerson-dietrich-phillipa-2.json) |  |
| [`dietrich-phillipa-3`](../au-fhir-test-data-set/au-core/RelatedPerson-dietrich-phillipa-3.json) |  |
| [`dietrich-phillipa-4`](../au-fhir-test-data-set/au-core/RelatedPerson-dietrich-phillipa-4.json) |  |
| [`hennessy-billy-1`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-1.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-billy-2`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-billy-2.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-jenny-1`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-1.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-jenny-2`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-jenny-2.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-kacey-1`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-1.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-kacey-2`](../au-fhir-test-data-set/au-core/RelatedPerson-hennessy-kacey-2.json) | *[scenario-groups](#scenario-groups)* |

<details><summary>31 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`alderson-helene`](../au-fhir-test-data-set/au-core/Practitioner-alderson-helene.json) | [`medicaldiagnostic-alderson-helene`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-alderson-helene.json) |  |  |  |
| [`allerton-skye`](../au-fhir-test-data-set/au-core/Practitioner-allerton-skye.json) | [`allerton-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-allerton-skye.json) | [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) |  |  |
| [`bennett-tawnya`](../au-fhir-test-data-set/au-core/Practitioner-bennett-tawnya.json) | [`bennett-tawnya`](../au-fhir-test-data-set/au-core/PractitionerRole-bennett-tawnya.json) | [`garran-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-garran-physiotherapy.json) |  |  |
| [`bishop-horace`](../au-fhir-test-data-set/au-core/Practitioner-bishop-horace.json) | [`generalpractitioner-bishop-horace`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-bishop-horace.json) | [`ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/Organization-ngunnawal-medical-practice.json) | [`ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/Location-ngunnawal-medical-practice.json) | [`generalmedical-ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-ngunnawal-medical-practice.json) |
| [`cohen-jamel`](../au-fhir-test-data-set/au-core/Practitioner-cohen-jamel.json) | [`nursepractitioner-cohen-jamel`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-cohen-jamel.json) | [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Organization-oxley-public-hospital.json) | [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Location-oxley-public-hospital.json) | [`publicacute-oxley-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-oxley-public-hospital.json) |
| [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/Practitioner-colliss-jocelyn.json) | [`colliss-jocelyn`](../au-fhir-test-data-set/au-core/PractitionerRole-colliss-jocelyn.json) | [`garran-cardiology-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-cardiology-clinic.json) |  |  |
| [`cross-lizzie`](../au-fhir-test-data-set/au-core/Practitioner-cross-lizzie.json) | [`surgeongeneral-cross-lizzie`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-cross-lizzie.json) | [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Organization-oxley-public-hospital.json) | [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Location-oxley-public-hospital.json) | [`publicacute-oxley-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-oxley-public-hospital.json) |
| [`donaldson-stephanie`](../au-fhir-test-data-set/au-core/Practitioner-donaldson-stephanie.json) | [`registerednurses-donaldson-stephanie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-donaldson-stephanie.json) | [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Organization-monash-private-hospital.json) | [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Location-monash-private-hospital.json) | [`privateacute-monash-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-monash-private-hospital.json) |
| [`gidley-stan`](../au-fhir-test-data-set/au-core/Practitioner-gidley-stan.json) | [`registerednurses-gidley-stan`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-stan.json) | [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Organization-oxley-public-hospital.json) | [`oxley-public-hospital`](../au-fhir-test-data-set/au-core/Location-oxley-public-hospital.json) | [`publicacute-oxley-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-oxley-public-hospital.json) |
| [`grant-lindsay`](../au-fhir-test-data-set/au-core/Practitioner-grant-lindsay.json) | [`nursepractitioner-grant-lindsay`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-grant-lindsay.json) | [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Organization-monash-private-hospital.json) | [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Location-monash-private-hospital.json) | [`privateacute-monash-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-monash-private-hospital.json) |
| [`harris-stephan`](../au-fhir-test-data-set/au-core/Practitioner-harris-stephan.json) | [`harris-stephan`](../au-fhir-test-data-set/au-core/PractitionerRole-harris-stephan.json) | [`garran-pharmacy`](../au-fhir-test-data-set/au-core/Organization-garran-pharmacy.json) |  |  |
| [`harrower-austin`](../au-fhir-test-data-set/au-core/Practitioner-harrower-austin.json) | [`harrower-austin`](../au-fhir-test-data-set/au-core/PractitionerRole-harrower-austin.json) | [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) |  |  |
| [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/Practitioner-harwood-kathaleen.json) | [`harwood-kathaleen`](../au-fhir-test-data-set/au-core/PractitionerRole-harwood-kathaleen.json) | [`garran-radiology`](../au-fhir-test-data-set/au-core/Organization-garran-radiology.json) |  |  |
| [`henderson-elaine`](../au-fhir-test-data-set/au-core/Practitioner-henderson-elaine.json) | [`henderson-elaine`](../au-fhir-test-data-set/au-core/PractitionerRole-henderson-elaine.json) | [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) |  |  |
| [`hill-maryln`](../au-fhir-test-data-set/au-core/Practitioner-hill-maryln.json) | [`diagnostic-hill-maryln`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-hill-maryln.json) | [`nicholls-radiology`](../au-fhir-test-data-set/au-core/Organization-nicholls-radiology.json) | [`nicholls-radiology`](../au-fhir-test-data-set/au-core/Location-nicholls-radiology.json) | [`diagnosticimaging-nicholls-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-nicholls-radiology.json) |
| [`humphreys-christeen`](../au-fhir-test-data-set/au-core/Practitioner-humphreys-christeen.json) | [`humphreys-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-humphreys-christeen.json) | [`garran-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-garran-ophthalmology.json) |  |  |
| [`krug-chas`](../au-fhir-test-data-set/au-core/Practitioner-krug-chas.json) | [`krug-chas`](../au-fhir-test-data-set/au-core/PractitionerRole-krug-chas.json) | [`garran-ot-services`](../au-fhir-test-data-set/au-core/Organization-garran-ot-services.json) |  |  |
| [`lees-noreen`](../au-fhir-test-data-set/au-core/Practitioner-lees-noreen.json) | [`retailpharmacist-lees-noreen`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-lees-noreen.json) | [`ginninderra-pharmacy`](../au-fhir-test-data-set/au-core/Organization-ginninderra-pharmacy.json) | [`ginninderra-pharmacy`](../au-fhir-test-data-set/au-core/Location-ginninderra-pharmacy.json) | [`pharmacyretail-ginninderra-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-ginninderra-pharmacy.json) |
| [`levings-richard`](../au-fhir-test-data-set/au-core/Practitioner-levings-richard.json) | [`levings-richard`](../au-fhir-test-data-set/au-core/PractitionerRole-levings-richard.json) | [`garran-nutrition`](../au-fhir-test-data-set/au-core/Organization-garran-nutrition.json) |  |  |
| [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/Practitioner-mackenzie-wilbur.json) | [`mackenzie-wilbur`](../au-fhir-test-data-set/au-core/PractitionerRole-mackenzie-wilbur.json) | [`garran-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-garran-medical-clinic.json) |  |  |
| [`maxwell-israel`](../au-fhir-test-data-set/au-core/Practitioner-maxwell-israel.json) | [`maxwell-israel`](../au-fhir-test-data-set/au-core/PractitionerRole-maxwell-israel.json) | [`garran-dental`](../au-fhir-test-data-set/au-core/Organization-garran-dental.json) |  |  |
| [`murphy-kyla`](../au-fhir-test-data-set/au-core/Practitioner-murphy-kyla.json) | [`murphy-kyla`](../au-fhir-test-data-set/au-core/PractitionerRole-murphy-kyla.json) | [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) |  |  |
| [`nairn-ricky`](../au-fhir-test-data-set/au-core/Practitioner-nairn-ricky.json) | [`registerednurses-nairn-ricky`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-nairn-ricky.json) | [`ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/Organization-ngunnawal-medical-practice.json) | [`ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/Location-ngunnawal-medical-practice.json) | [`generalmedical-ngunnawal-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-ngunnawal-medical-practice.json) |
| [`newling-mariella`](../au-fhir-test-data-set/au-core/Practitioner-newling-mariella.json) | [`newling-mariella`](../au-fhir-test-data-set/au-core/PractitionerRole-newling-mariella.json) | [`manuka-medical-centre`](../au-fhir-test-data-set/au-core/Organization-manuka-medical-centre.json) |  |  |
| [`patrick-tricia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-tricia.json) | [`patrick-tricia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-tricia.json) | [`garran-optical`](../au-fhir-test-data-set/au-core/Organization-garran-optical.json) |  |  |
| [`pickford-aimee`](../au-fhir-test-data-set/au-core/Practitioner-pickford-aimee.json) | [`surgeongeneral-pickford-aimee`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-pickford-aimee.json) | [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Organization-monash-private-hospital.json) | [`monash-private-hospital`](../au-fhir-test-data-set/au-core/Location-monash-private-hospital.json) | [`privateacute-monash-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-monash-private-hospital.json) |
| [`pollock-dinah`](../au-fhir-test-data-set/au-core/Practitioner-pollock-dinah.json) | [`midwife-pollock-dinah`](../au-fhir-test-data-set/au-core/PractitionerRole-midwife-pollock-dinah.json) |  |  |  |
| [`rowlands-alvera`](../au-fhir-test-data-set/au-core/Practitioner-rowlands-alvera.json) | [`paediatrician-rowlands-alvera`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-rowlands-alvera.json) |  |  |  |
| [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/Practitioner-sawtell-tomasa.json) | [`sawtell-tomasa`](../au-fhir-test-data-set/au-core/PractitionerRole-sawtell-tomasa.json) | [`garran-nephrology`](../au-fhir-test-data-set/au-core/Organization-garran-nephrology.json) |  |  |
| [`short-tandra`](../au-fhir-test-data-set/au-core/Practitioner-short-tandra.json) | [`short-tandra`](../au-fhir-test-data-set/au-core/PractitionerRole-short-tandra.json) | [`garran-pathology`](../au-fhir-test-data-set/au-core/Organization-garran-pathology.json) |  |  |
| [`stevens-chelsea`](../au-fhir-test-data-set/au-core/Practitioner-stevens-chelsea.json) | [`pathologist-stevens-chelsea`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-stevens-chelsea.json) | [`calwell-pathology`](../au-fhir-test-data-set/au-core/Organization-calwell-pathology.json) | [`calwell-pathology`](../au-fhir-test-data-set/au-core/Location-calwell-pathology.json) | [`pathologylaboratory-calwell-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-calwell-pathology.json) |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>NSW</strong> (14 groupings, 222 entities)</summary>

<blockquote>
<details><summary><strong>Postcodes 224xx-226xx</strong> (8 entities)</summary>


_Bucketty, Canton Beach, Koolewong._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`tennant-carlyn`](../au-fhir-test-data-set/au-core/Practitioner-tennant-carlyn.json) | [`medicaldiagnostic-tennant-carlyn`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-tennant-carlyn.json) | Medical Diagnostic Radiographer |  |

**HealthcareService** (2)

- [`physiotherapyservices-canton-beach-physiotherapy`](../au-fhir-test-data-set/au-core/HealthcareService-physiotherapyservices-canton-beach-physiotherapy.json)
- [`specialistmedical-bucketty-oncology-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-bucketty-oncology-clinic.json)

**Organization** (2)

- [`bucketty-oncology-clinic`](../au-fhir-test-data-set/au-core/Organization-bucketty-oncology-clinic.json)
- [`canton-beach-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-canton-beach-physiotherapy.json)

**Location** (2)

- [`bucketty-oncology-clinic`](../au-fhir-test-data-set/au-core/Location-bucketty-oncology-clinic.json)
- [`canton-beach-physiotherapy`](../au-fhir-test-data-set/au-core/Location-canton-beach-physiotherapy.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`tennant-carlyn`](../au-fhir-test-data-set/au-core/Practitioner-tennant-carlyn.json) | [`medicaldiagnostic-tennant-carlyn`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-tennant-carlyn.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 235xx-237xx</strong> (9 entities)</summary>


_Mount Mitchell._


**Practitioner / PractitionerRole** (3)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`guthrie-daine`](../au-fhir-test-data-set/au-core/Practitioner-guthrie-daine.json) | [`surgeongeneral-guthrie-daine`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-guthrie-daine.json) | Surgeon (General) (General surgery) |  |
| [`milgate-leisa`](../au-fhir-test-data-set/au-core/Practitioner-milgate-leisa.json) | [`registerednurses-milgate-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-milgate-leisa.json) | Registered Nurses nec (Nursing) |  |
| [`munro-rose`](../au-fhir-test-data-set/au-core/Practitioner-munro-rose.json) | [`nursepractitioner-munro-rose`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-munro-rose.json) | Nurse Practitioner (Nursing) |  |

**HealthcareService** (1)

- [`privateacute-mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-mount-mitchell-private-hospital.json)

**Organization** (1)

- [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Organization-mount-mitchell-private-hospital.json)

**Location** (1)

- [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Location-mount-mitchell-private-hospital.json)

<details><summary>3 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`guthrie-daine`](../au-fhir-test-data-set/au-core/Practitioner-guthrie-daine.json) | [`surgeongeneral-guthrie-daine`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-guthrie-daine.json) | [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Organization-mount-mitchell-private-hospital.json) | [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Location-mount-mitchell-private-hospital.json) | [`privateacute-mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-mount-mitchell-private-hospital.json) |
| [`milgate-leisa`](../au-fhir-test-data-set/au-core/Practitioner-milgate-leisa.json) | [`registerednurses-milgate-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-milgate-leisa.json) | [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Organization-mount-mitchell-private-hospital.json) | [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Location-mount-mitchell-private-hospital.json) | [`privateacute-mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-mount-mitchell-private-hospital.json) |
| [`munro-rose`](../au-fhir-test-data-set/au-core/Practitioner-munro-rose.json) | [`nursepractitioner-munro-rose`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-munro-rose.json) | [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Organization-mount-mitchell-private-hospital.json) | [`mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/Location-mount-mitchell-private-hospital.json) | [`privateacute-mount-mitchell-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-mount-mitchell-private-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 241xx-243xx</strong> (5 entities)</summary>


_Cundle Flat, Gangat._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`gates-glenda`](../au-fhir-test-data-set/au-core/Practitioner-gates-glenda.json) | [`medicaldiagnostic-gates-glenda`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-gates-glenda.json) | Medical Diagnostic Radiographer |  |

**HealthcareService** (1)

- [`specialistmedical-gangat-endocrinology-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-gangat-endocrinology-clinic.json)

**Organization** (1)

- [`gangat-endocrinology-clinic`](../au-fhir-test-data-set/au-core/Organization-gangat-endocrinology-clinic.json)

**Location** (1)

- [`gangat-endocrinology-clinic`](../au-fhir-test-data-set/au-core/Location-gangat-endocrinology-clinic.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`gates-glenda`](../au-fhir-test-data-set/au-core/Practitioner-gates-glenda.json) | [`medicaldiagnostic-gates-glenda`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-gates-glenda.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 243xx-245xx</strong> (8 entities)</summary>


_Belmore River, Fishermans Reach, Yarravel._


**Patient** (1)

- [`irvine-ronny-lawrence`](../au-fhir-test-data-set/au-core/Patient-irvine-ronny-lawrence.json) — *also in: [au-core-ig-examples](#au-core-ig-examples), [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)*

**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`gilchrist-daniel`](../au-fhir-test-data-set/au-core/Practitioner-gilchrist-daniel.json) | [`complementaryhealth-gilchrist-daniel`](../au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-gilchrist-daniel.json) | Myotherapist (Myotherapy service) |  |
| [`osborne-bonny`](../au-fhir-test-data-set/au-core/Practitioner-osborne-bonny.json) | [`diagnostic-osborne-bonny`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-osborne-bonny.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |

**HealthcareService** (1)

- [`diagnosticimaging-fishermans-reach-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-fishermans-reach-radiology.json)

**Organization** (1)

- [`fishermans-reach-radiology`](../au-fhir-test-data-set/au-core/Organization-fishermans-reach-radiology.json)

**Location** (1)

- [`fishermans-reach-radiology`](../au-fhir-test-data-set/au-core/Location-fishermans-reach-radiology.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`gilchrist-daniel`](../au-fhir-test-data-set/au-core/Practitioner-gilchrist-daniel.json) | [`complementaryhealth-gilchrist-daniel`](../au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-gilchrist-daniel.json) |  |  |  |
| [`osborne-bonny`](../au-fhir-test-data-set/au-core/Practitioner-osborne-bonny.json) | [`diagnostic-osborne-bonny`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-osborne-bonny.json) | [`fishermans-reach-radiology`](../au-fhir-test-data-set/au-core/Organization-fishermans-reach-radiology.json) | [`fishermans-reach-radiology`](../au-fhir-test-data-set/au-core/Location-fishermans-reach-radiology.json) | [`diagnosticimaging-fishermans-reach-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-fishermans-reach-radiology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 245xx-247xx</strong> (8 entities)</summary>


_Kippenduff, Lilydale._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`cane-elden`](../au-fhir-test-data-set/au-core/Practitioner-cane-elden.json) | [`retailpharmacist-cane-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-cane-elden.json) | Retail Pharmacist (Community pharmacy) |  |

**HealthcareService** (2)

- [`pharmacyretail-lilydale-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-lilydale-pharmacy.json)
- [`specialistmedical-kippenduff-cardiologist`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-kippenduff-cardiologist.json)

**Organization** (2)

- [`kippenduff-cardiologist`](../au-fhir-test-data-set/au-core/Organization-kippenduff-cardiologist.json)
- [`lilydale-pharmacy`](../au-fhir-test-data-set/au-core/Organization-lilydale-pharmacy.json)

**Location** (2)

- [`kippenduff-cardiologist`](../au-fhir-test-data-set/au-core/Location-kippenduff-cardiologist.json)
- [`lilydale-pharmacy`](../au-fhir-test-data-set/au-core/Location-lilydale-pharmacy.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`cane-elden`](../au-fhir-test-data-set/au-core/Practitioner-cane-elden.json) | [`retailpharmacist-cane-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-cane-elden.json) | [`lilydale-pharmacy`](../au-fhir-test-data-set/au-core/Organization-lilydale-pharmacy.json) | [`lilydale-pharmacy`](../au-fhir-test-data-set/au-core/Location-lilydale-pharmacy.json) | [`pharmacyretail-lilydale-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-lilydale-pharmacy.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 247xx-249xx</strong> (8 entities)</summary>


_Bungabbee, Palmvale._


**Patient** (1)

- [`johnson-joyce`](../au-fhir-test-data-set/au-core/Patient-johnson-joyce.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)*

**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`burrows-ginger`](../au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json) | [`generalpractitioner-burrows-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json) | General Practitioner (General medical practice) | [au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`patrick-fletcher`](../au-fhir-test-data-set/au-core/Practitioner-patrick-fletcher.json) | [`registerednurses-patrick-fletcher`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-patrick-fletcher.json) | Registered Nurses nec (Nursing) |  |

**HealthcareService** (1)

- [`generalpractice-bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-bungabbee-medical-clinic.json)

**Organization** (1)

- [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*

**Location** (1)

- [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Location-bungabbee-medical-clinic.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`burrows-ginger`](../au-fhir-test-data-set/au-core/Practitioner-burrows-ginger.json) | [`generalpractitioner-burrows-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-burrows-ginger.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Location-bungabbee-medical-clinic.json) | [`generalpractice-bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-bungabbee-medical-clinic.json) |
| [`patrick-fletcher`](../au-fhir-test-data-set/au-core/Practitioner-patrick-fletcher.json) | [`registerednurses-patrick-fletcher`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-patrick-fletcher.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-bungabbee-medical-clinic.json) | [`bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/Location-bungabbee-medical-clinic.json) | [`generalpractice-bungabbee-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-bungabbee-medical-clinic.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 252xx-254xx</strong> (7 entities)</summary>


_Mossy Point._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`lowe-abe`](../au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json) | [`generalpractitioner-lowe-abe`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json) | General Practitioner (General medical practice) | [au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`roberts-benjamin`](../au-fhir-test-data-set/au-core/Practitioner-roberts-benjamin.json) | [`registerednurses-roberts-benjamin`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-roberts-benjamin.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**HealthcareService** (1)

- [`generalmedical-mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json)

**Organization** (1)

- [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*

**Location** (1)

- [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`lowe-abe`](../au-fhir-test-data-set/au-core/Practitioner-lowe-abe.json) | [`generalpractitioner-lowe-abe`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lowe-abe.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json) | [`generalmedical-mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json) |
| [`roberts-benjamin`](../au-fhir-test-data-set/au-core/Practitioner-roberts-benjamin.json) | [`registerednurses-roberts-benjamin`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-roberts-benjamin.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Organization-mossy-point-medical-centre.json) | [`mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/Location-mossy-point-medical-centre.json) | [`generalmedical-mossy-point-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-mossy-point-medical-centre.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 254xx-256xx</strong> (9 entities)</summary>


_Appin, Mogareeka, Stony Creek._


**Practitioner / PractitionerRole** (3)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`cruickshank-bryce`](../au-fhir-test-data-set/au-core/Practitioner-cruickshank-bryce.json) | [`endocrinologist-cruickshank-bryce`](../au-fhir-test-data-set/au-core/PractitionerRole-endocrinologist-cruickshank-bryce.json) | Endocrinologist (Endocrinology) |  |
| [`peterson-megan`](../au-fhir-test-data-set/au-core/Practitioner-peterson-megan.json) | [`retailpharmacist-peterson-megan`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-peterson-megan.json) | Retail Pharmacist (Community pharmacy) |  |
| [`sheppard-mathew`](../au-fhir-test-data-set/au-core/Practitioner-sheppard-mathew.json) | [`medicaloncologist-sheppard-mathew`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-sheppard-mathew.json) | Medical Oncologist (Medical oncology) | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**HealthcareService** (1)

- [`communitypharmacy-appin-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-appin-pharmacy.json)

**Organization** (1)

- [`appin-pharmacy`](../au-fhir-test-data-set/au-core/Organization-appin-pharmacy.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*

**Location** (1)

- [`appin-pharmacy`](../au-fhir-test-data-set/au-core/Location-appin-pharmacy.json)

<details><summary>3 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`cruickshank-bryce`](../au-fhir-test-data-set/au-core/Practitioner-cruickshank-bryce.json) | [`endocrinologist-cruickshank-bryce`](../au-fhir-test-data-set/au-core/PractitionerRole-endocrinologist-cruickshank-bryce.json) |  |  |  |
| [`peterson-megan`](../au-fhir-test-data-set/au-core/Practitioner-peterson-megan.json) | [`retailpharmacist-peterson-megan`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-peterson-megan.json) | [`appin-pharmacy`](../au-fhir-test-data-set/au-core/Organization-appin-pharmacy.json) | [`appin-pharmacy`](../au-fhir-test-data-set/au-core/Location-appin-pharmacy.json) | [`communitypharmacy-appin-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-appin-pharmacy.json) |
| [`sheppard-mathew`](../au-fhir-test-data-set/au-core/Practitioner-sheppard-mathew.json) | [`medicaloncologist-sheppard-mathew`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-sheppard-mathew.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 257xx-259xx</strong> (11 entities)</summary>


_Tarlo, Wallendbeen._


**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`fraser-abbie`](../au-fhir-test-data-set/au-core/Practitioner-fraser-abbie.json) | [`registerednurses-fraser-abbie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-fraser-abbie.json) | Registered Nurses nec (Nursing) |  |
| [`gartshore-indira`](../au-fhir-test-data-set/au-core/Practitioner-gartshore-indira.json) | [`nursepractitioner-gartshore-indira`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-gartshore-indira.json) | Nurse Practitioner (Nursing) |  |
| [`jenkins-miranda`](../au-fhir-test-data-set/au-core/Practitioner-jenkins-miranda.json) | [`ophthalmologist-jenkins-miranda`](../au-fhir-test-data-set/au-core/PractitionerRole-ophthalmologist-jenkins-miranda.json) | Ophthalmologist (Ophthalmology) |  |
| [`taylor-kittie`](../au-fhir-test-data-set/au-core/Practitioner-taylor-kittie.json) | [`registerednurses-taylor-kittie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-taylor-kittie.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**HealthcareService** (1)

- [`privateprofit-wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-wallendbeen-aged-care.json)

**Organization** (1)

- [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Organization-wallendbeen-aged-care.json)

**Location** (1)

- [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Location-wallendbeen-aged-care.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`fraser-abbie`](../au-fhir-test-data-set/au-core/Practitioner-fraser-abbie.json) | [`registerednurses-fraser-abbie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-fraser-abbie.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Organization-wallendbeen-aged-care.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Location-wallendbeen-aged-care.json) | [`privateprofit-wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-wallendbeen-aged-care.json) |
| [`gartshore-indira`](../au-fhir-test-data-set/au-core/Practitioner-gartshore-indira.json) | [`nursepractitioner-gartshore-indira`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-gartshore-indira.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Organization-wallendbeen-aged-care.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Location-wallendbeen-aged-care.json) | [`privateprofit-wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-wallendbeen-aged-care.json) |
| [`jenkins-miranda`](../au-fhir-test-data-set/au-core/Practitioner-jenkins-miranda.json) | [`ophthalmologist-jenkins-miranda`](../au-fhir-test-data-set/au-core/PractitionerRole-ophthalmologist-jenkins-miranda.json) |  |  |  |
| [`taylor-kittie`](../au-fhir-test-data-set/au-core/Practitioner-taylor-kittie.json) | [`registerednurses-taylor-kittie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-taylor-kittie.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Organization-wallendbeen-aged-care.json) | [`wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/Location-wallendbeen-aged-care.json) | [`privateprofit-wallendbeen-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-wallendbeen-aged-care.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 270xx-272xx</strong> (13 entities)</summary>


_Hatfield, Leeton, Minjary, Wermatong._


**Patient** (4)

| ID | Also in |
| --- | --- |
| [`banks-jamila-angie`](../au-fhir-test-data-set/au-core/Patient-banks-jamila-angie.json) | *[families](#families)* |
| [`banks-jeramy-ezra`](../au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json) | *[au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`banks-jonas-cary`](../au-fhir-test-data-set/au-core/Patient-banks-jonas-cary.json) | *[families](#families)* |
| [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-ig-examples](#au-ps-ig-examples), [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |

**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`browne-wilfred`](../au-fhir-test-data-set/au-core/Practitioner-browne-wilfred.json) | [`midwife-browne-wilfred`](../au-fhir-test-data-set/au-core/PractitionerRole-midwife-browne-wilfred.json) | Midwife (Obstetric nursing) |  |
| [`thorn-tonya`](../au-fhir-test-data-set/au-core/Practitioner-thorn-tonya.json) | [`nuclearmedicine-thorn-tonya`](../au-fhir-test-data-set/au-core/PractitionerRole-nuclearmedicine-thorn-tonya.json) | Nuclear Medicine Technologist |  |

**Organization** (1)

- [`leeton-health-network`](../au-fhir-test-data-set/au-core/Organization-leeton-health-network.json) — *also in: [community-contributions](#community-contributions)*

**RelatedPerson** (4)

- [`banks-jeramy-2`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-jeramy-2.json)
- [`banks-jeramy-3`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-jeramy-3.json)
- [`banks-jeramy-4`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-jeramy-4.json)
- [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-mia-leanne.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`browne-wilfred`](../au-fhir-test-data-set/au-core/Practitioner-browne-wilfred.json) | [`midwife-browne-wilfred`](../au-fhir-test-data-set/au-core/PractitionerRole-midwife-browne-wilfred.json) |  |  |
| [`thorn-tonya`](../au-fhir-test-data-set/au-core/Practitioner-thorn-tonya.json) | [`nuclearmedicine-thorn-tonya`](../au-fhir-test-data-set/au-core/PractitionerRole-nuclearmedicine-thorn-tonya.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 276xx-278xx</strong> (5 entities)</summary>


_Higher Macdonald._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`clarke-malcolm`](../au-fhir-test-data-set/au-core/Practitioner-clarke-malcolm.json) | [`pathologist-clarke-malcolm`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-clarke-malcolm.json) | Pathologist (Pathology) |  |

**HealthcareService** (1)

- [`pathologylaboratory-higher-macdonald-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-higher-macdonald-pathology.json)

**Organization** (1)

- [`higher-macdonald-pathology`](../au-fhir-test-data-set/au-core/Organization-higher-macdonald-pathology.json)

**Location** (1)

- [`higher-macdonald-pathology`](../au-fhir-test-data-set/au-core/Location-higher-macdonald-pathology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`clarke-malcolm`](../au-fhir-test-data-set/au-core/Practitioner-clarke-malcolm.json) | [`pathologist-clarke-malcolm`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-clarke-malcolm.json) | [`higher-macdonald-pathology`](../au-fhir-test-data-set/au-core/Organization-higher-macdonald-pathology.json) | [`higher-macdonald-pathology`](../au-fhir-test-data-set/au-core/Location-higher-macdonald-pathology.json) | [`pathologylaboratory-higher-macdonald-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-higher-macdonald-pathology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 280xx-282xx</strong> (5 entities)</summary>


_Pullabooka._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`pratley-philomena`](../au-fhir-test-data-set/au-core/Practitioner-pratley-philomena.json) | [`pathologist-pratley-philomena`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-pratley-philomena.json) | Pathologist (Pathology) |  |

**HealthcareService** (1)

- [`pathologylaboratory-pullabooka-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-pullabooka-pathology.json)

**Organization** (1)

- [`pullabooka-pathology`](../au-fhir-test-data-set/au-core/Organization-pullabooka-pathology.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*

**Location** (1)

- [`pullabooka-pathology`](../au-fhir-test-data-set/au-core/Location-pullabooka-pathology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`pratley-philomena`](../au-fhir-test-data-set/au-core/Practitioner-pratley-philomena.json) | [`pathologist-pratley-philomena`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-pratley-philomena.json) | [`pullabooka-pathology`](../au-fhir-test-data-set/au-core/Organization-pullabooka-pathology.json) | [`pullabooka-pathology`](../au-fhir-test-data-set/au-core/Location-pullabooka-pathology.json) | [`pathologylaboratory-pullabooka-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-pullabooka-pathology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 282xx-284xx</strong> (7 entities)</summary>


_Balladoran, Dubbo._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`gilmour-damon`](../au-fhir-test-data-set/au-core/Practitioner-gilmour-damon.json) | [`emergencymedicine-gilmour-damon`](../au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-gilmour-damon.json) | Emergency Medicine Specialist (Emergency medicine) |  |
| [`leishman-leesa`](../au-fhir-test-data-set/au-core/Practitioner-leishman-leesa.json) | [`paediatrician-leishman-leesa`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-leishman-leesa.json) | Paediatrician (General paediatric specialty) |  |

**HealthcareService** (1)

- [`emergencydepartment-dubbo-emergency`](../au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-dubbo-emergency.json)

**Organization** (1)

- [`dubbo-emergency`](../au-fhir-test-data-set/au-core/Organization-dubbo-emergency.json)

**Location** (1)

- [`dubbo-emergency`](../au-fhir-test-data-set/au-core/Location-dubbo-emergency.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`gilmour-damon`](../au-fhir-test-data-set/au-core/Practitioner-gilmour-damon.json) | [`emergencymedicine-gilmour-damon`](../au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-gilmour-damon.json) | [`dubbo-emergency`](../au-fhir-test-data-set/au-core/Organization-dubbo-emergency.json) | [`dubbo-emergency`](../au-fhir-test-data-set/au-core/Location-dubbo-emergency.json) | [`emergencydepartment-dubbo-emergency`](../au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-dubbo-emergency.json) |
| [`leishman-leesa`](../au-fhir-test-data-set/au-core/Practitioner-leishman-leesa.json) | [`paediatrician-leishman-leesa`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-leishman-leesa.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Sydney metropolitan</strong> (119 entities)</summary>


_Berowra, Blacktown, Canley Heights, Cremorne, Frenchs Forest East, Kensington, Parramatta, Westmead._


**Patient** (6)

| ID | Also in |
| --- | --- |
| [`keaton-jayme`](../au-fhir-test-data-set/au-core/Patient-keaton-jayme.json) |  |
| [`lowe-alessandra`](../au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alix`](../au-fhir-test-data-set/au-core/Patient-lowe-alix.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-cedric`](../au-fhir-test-data-set/au-core/Patient-lowe-cedric.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-valerie`](../au-fhir-test-data-set/au-core/Patient-lowe-valerie.json) | *[scenario-groups](#scenario-groups)* |
| [`wang-li`](../au-fhir-test-data-set/au-core/Patient-wang-li.json) | *[au-core-ig-examples](#au-core-ig-examples)* |

**Practitioner / PractitionerRole** (38)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`barrett-carey`](../au-fhir-test-data-set/au-core/Practitioner-barrett-carey.json) | [`diagnostic-barrett-carey`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-barrett-carey.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`berridge-beulah`](../au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json) | [`berridge-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json) | Anaesthetist (Anaesthetics) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`breadmore-phillip`](../au-fhir-test-data-set/au-core/Practitioner-breadmore-phillip.json) | [`breadmore-phillip`](../au-fhir-test-data-set/au-core/PractitionerRole-breadmore-phillip.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`cox-sandra`](../au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json) | [`cox-sandra`](../au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`dawson-kent`](../au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json) | [`dawson-kent`](../au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json) | Emergency Medicine Specialist / Emergency Physician (Emergency medicine) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`duncan-xenia`](../au-fhir-test-data-set/au-core/Practitioner-duncan-xenia.json) | [`duncan-xenia`](../au-fhir-test-data-set/au-core/PractitionerRole-duncan-xenia.json) | Social Worker | [scenario-groups](#scenario-groups) |
| [`ellison-abby`](../au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json) | [`ellison-abby`](../au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`ewing-jude`](../au-fhir-test-data-set/au-core/Practitioner-ewing-jude.json) | [`ewing-jude`](../au-fhir-test-data-set/au-core/PractitionerRole-ewing-jude.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`fleming-kitty`](../au-fhir-test-data-set/au-core/Practitioner-fleming-kitty.json) | [`fleming-kitty`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-kitty.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups) |
| [`fowler-christy`](../au-fhir-test-data-set/au-core/Practitioner-fowler-christy.json) | [`medicalradiation-fowler-christy`](../au-fhir-test-data-set/au-core/PractitionerRole-medicalradiation-fowler-christy.json) | Medical Radiation Therapist (Radiation oncology) |  |
| [`frank-gaylene`](../au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json) | [`frank-gaylene`](../au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json) | Nurse Practitioner (Nursing) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`fuller-christeen`](../au-fhir-test-data-set/au-core/Practitioner-fuller-christeen.json) | [`fuller-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-christeen.json) | Gastroenterologist (Gastroenterology) | [scenario-groups](#scenario-groups) |
| [`goodwin-rae`](../au-fhir-test-data-set/au-core/Practitioner-goodwin-rae.json) | [`goodwin-rae`](../au-fhir-test-data-set/au-core/PractitionerRole-goodwin-rae.json) | Optometrist | [scenario-groups](#scenario-groups) |
| [`hamilton-errol`](../au-fhir-test-data-set/au-core/Practitioner-hamilton-errol.json) | [`hamilton-errol`](../au-fhir-test-data-set/au-core/PractitionerRole-hamilton-errol.json) | Pharmacist (Community pharmacy) | [scenario-groups](#scenario-groups) |
| [`healey-tamiko`](../au-fhir-test-data-set/au-core/Practitioner-healey-tamiko.json) | [`healey-tamiko`](../au-fhir-test-data-set/au-core/PractitionerRole-healey-tamiko.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) | [scenario-groups](#scenario-groups) |
| [`howe-elden`](../au-fhir-test-data-set/au-core/Practitioner-howe-elden.json) | [`howe-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-howe-elden.json) | Midwife (Obstetric nursing) | [scenario-groups](#scenario-groups) |
| [`knowles-sunshine`](../au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json) | [`knowles-sunshine`](../au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json) | Occupational Therapist | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json) | [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json) | Clinical Psychologist (Clinical psychology) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`little-jerrie`](../au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json) | [`little-jerrie`](../au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`macey-brant`](../au-fhir-test-data-set/au-core/Practitioner-macey-brant.json) | [`macey-brant`](../au-fhir-test-data-set/au-core/PractitionerRole-macey-brant.json) | Ophthalmologist (Ophthalmology) | [scenario-groups](#scenario-groups) |
| [`mackenzie-cinda`](../au-fhir-test-data-set/au-core/Practitioner-mackenzie-cinda.json) | [`surgeongeneral-mackenzie-cinda`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-mackenzie-cinda.json) | Surgeon (General) (General surgery) |  |
| [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/Practitioner-mcbean-nicollette.json) | [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/PractitionerRole-mcbean-nicollette.json) | Surgeon (General) (General surgery) | [scenario-groups](#scenario-groups) |
| [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/Practitioner-mcintosh-angelica.json) | [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/PractitionerRole-mcintosh-angelica.json) | Obstetrician and Gynaecologist (Obstetrics and gynaecology) | [scenario-groups](#scenario-groups) |
| [`mcnab-angelina`](../au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json) | [`mcnab-angelina`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json) | Dietitian (Dietetics and nutrition) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`mills-hope`](../au-fhir-test-data-set/au-core/Practitioner-mills-hope.json) | [`mills-hope`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json) | Occupational Therapist | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`nairn-vince`](../au-fhir-test-data-set/au-core/Practitioner-nairn-vince.json) | [`nairn-vince`](../au-fhir-test-data-set/au-core/PractitionerRole-nairn-vince.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups) |
| [`neville-isaiah`](../au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json) | [`neville-isaiah`](../au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`nutley-bradley`](../au-fhir-test-data-set/au-core/Practitioner-nutley-bradley.json) | [`nutley-bradley`](../au-fhir-test-data-set/au-core/PractitionerRole-nutley-bradley.json) | Pathologist (Clinical pathology) | [scenario-groups](#scenario-groups) |
| [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json) | [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json) | Pharmacist (Community pharmacy) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`osmond-michele`](../au-fhir-test-data-set/au-core/Practitioner-osmond-michele.json) | [`osmond-michele`](../au-fhir-test-data-set/au-core/PractitionerRole-osmond-michele.json) | Dental Practitioner (Dentistry) | [scenario-groups](#scenario-groups) |
| [`perkins-amee`](../au-fhir-test-data-set/au-core/Practitioner-perkins-amee.json) | [`perkins-amee`](../au-fhir-test-data-set/au-core/PractitionerRole-perkins-amee.json) | Sonographer | [scenario-groups](#scenario-groups) |
| [`redman-mariah`](../au-fhir-test-data-set/au-core/Practitioner-redman-mariah.json) | [`redman-mariah`](../au-fhir-test-data-set/au-core/PractitionerRole-redman-mariah.json) | Midwife (Obstetric nursing) | [scenario-groups](#scenario-groups) |
| [`roche-garfield`](../au-fhir-test-data-set/au-core/Practitioner-roche-garfield.json) | [`roche-garfield`](../au-fhir-test-data-set/au-core/PractitionerRole-roche-garfield.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [scenario-groups](#scenario-groups) |
| [`seaby-penelope`](../au-fhir-test-data-set/au-core/Practitioner-seaby-penelope.json) | [`seaby-penelope`](../au-fhir-test-data-set/au-core/PractitionerRole-seaby-penelope.json) | Cardiologist (Cardiology) | [scenario-groups](#scenario-groups) |
| [`shephard-lizabeth`](../au-fhir-test-data-set/au-core/Practitioner-shephard-lizabeth.json) | [`registerednurses-shephard-lizabeth`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shephard-lizabeth.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`simons-reggie`](../au-fhir-test-data-set/au-core/Practitioner-simons-reggie.json) | [`nursepractitioner-simons-reggie`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-simons-reggie.json) | Nurse Practitioner (Nursing) |  |
| [`stephens-nellie`](../au-fhir-test-data-set/au-core/Practitioner-stephens-nellie.json) | [`stephens-nellie`](../au-fhir-test-data-set/au-core/PractitionerRole-stephens-nellie.json) | Social Worker | [scenario-groups](#scenario-groups) |
| [`tate-melvin`](../au-fhir-test-data-set/au-core/Practitioner-tate-melvin.json) | [`tate-melvin`](../au-fhir-test-data-set/au-core/PractitionerRole-tate-melvin.json) | Midwife (Obstetric nursing) | [scenario-groups](#scenario-groups) |

**HealthcareService** (2)

- [`diagnosticimaging-frenchs-forest-east-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-frenchs-forest-east-radiology.json)
- [`publicacute-kensington-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-kensington-public-hospital.json)

**Organization** (19)

| ID | Also in |
| --- | --- |
| [`cremorne-care-and-support`](../au-fhir-test-data-set/au-core/Organization-cremorne-care-and-support.json) | *[community-contributions](#community-contributions)* |
| [`frenchs-forest-east-radiology`](../au-fhir-test-data-set/au-core/Organization-frenchs-forest-east-radiology.json) |  |
| [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json) | *[au-ps-ig-examples](#au-ps-ig-examples)* |
| [`parramatta-community-health`](../au-fhir-test-data-set/au-core/Organization-parramatta-community-health.json) | *[scenario-groups](#scenario-groups)* |
| [`parramatta-dental`](../au-fhir-test-data-set/au-core/Organization-parramatta-dental.json) | *[scenario-groups](#scenario-groups)* |
| [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`parramatta-midwifery`](../au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json) | *[scenario-groups](#scenario-groups)* |
| [`parramatta-nutrition`](../au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json) | *[scenario-groups](#scenario-groups)* |
| [`parramatta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json) | *[scenario-groups](#scenario-groups)* |
| [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-optical`](../au-fhir-test-data-set/au-core/Organization-westmead-optical.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-ot-services`](../au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-pathology`](../au-fhir-test-data-set/au-core/Organization-westmead-pathology.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-pharmacy`](../au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-radiology`](../au-fhir-test-data-set/au-core/Organization-westmead-radiology.json) | *[scenario-groups](#scenario-groups)* |
| [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) | *[scenario-groups](#scenario-groups)* |

**Location** (2)

- [`frenchs-forest-east-radiology`](../au-fhir-test-data-set/au-core/Location-frenchs-forest-east-radiology.json)
- [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Location-kensington-public-hospital.json)

**RelatedPerson** (14)

| ID | Also in |
| --- | --- |
| [`lowe-alessandra-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-1.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alessandra-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-2.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alessandra-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alessandra-3.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alix-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-1.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alix-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-2.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alix-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-alix-3.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-cedric-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-1.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-cedric-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-2.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-cedric-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-cedric-3.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-valerie-1`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-1.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-valerie-2`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-2.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-valerie-3`](../au-fhir-test-data-set/au-core/RelatedPerson-lowe-valerie-3.json) | *[scenario-groups](#scenario-groups)* |
| [`rabbit-peter`](../au-fhir-test-data-set/au-core/RelatedPerson-rabbit-peter.json) |  |
| [`wang-li-friend`](../au-fhir-test-data-set/au-core/RelatedPerson-wang-li-friend.json) | *[au-core-ig-examples](#au-core-ig-examples)* |

<details><summary>38 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`barrett-carey`](../au-fhir-test-data-set/au-core/Practitioner-barrett-carey.json) | [`diagnostic-barrett-carey`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-barrett-carey.json) | [`frenchs-forest-east-radiology`](../au-fhir-test-data-set/au-core/Organization-frenchs-forest-east-radiology.json) | [`frenchs-forest-east-radiology`](../au-fhir-test-data-set/au-core/Location-frenchs-forest-east-radiology.json) | [`diagnosticimaging-frenchs-forest-east-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-frenchs-forest-east-radiology.json) |
| [`berridge-beulah`](../au-fhir-test-data-set/au-core/Practitioner-berridge-beulah.json) | [`berridge-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-berridge-beulah.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |  |
| [`breadmore-phillip`](../au-fhir-test-data-set/au-core/Practitioner-breadmore-phillip.json) | [`breadmore-phillip`](../au-fhir-test-data-set/au-core/PractitionerRole-breadmore-phillip.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |  |
| [`cox-sandra`](../au-fhir-test-data-set/au-core/Practitioner-cox-sandra.json) | [`cox-sandra`](../au-fhir-test-data-set/au-core/PractitionerRole-cox-sandra.json) | [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) |  |  |
| [`dawson-kent`](../au-fhir-test-data-set/au-core/Practitioner-dawson-kent.json) | [`dawson-kent`](../au-fhir-test-data-set/au-core/PractitionerRole-dawson-kent.json) | [`parramatta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-parramatta-public-hospital.json) |  |  |
| [`duncan-xenia`](../au-fhir-test-data-set/au-core/Practitioner-duncan-xenia.json) | [`duncan-xenia`](../au-fhir-test-data-set/au-core/PractitionerRole-duncan-xenia.json) | [`parramatta-community-health`](../au-fhir-test-data-set/au-core/Organization-parramatta-community-health.json) |  |  |
| [`ellison-abby`](../au-fhir-test-data-set/au-core/Practitioner-ellison-abby.json) | [`ellison-abby`](../au-fhir-test-data-set/au-core/PractitionerRole-ellison-abby.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`ewing-jude`](../au-fhir-test-data-set/au-core/Practitioner-ewing-jude.json) | [`ewing-jude`](../au-fhir-test-data-set/au-core/PractitionerRole-ewing-jude.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |  |
| [`fleming-kitty`](../au-fhir-test-data-set/au-core/Practitioner-fleming-kitty.json) | [`fleming-kitty`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-kitty.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |  |
| [`fowler-christy`](../au-fhir-test-data-set/au-core/Practitioner-fowler-christy.json) | [`medicalradiation-fowler-christy`](../au-fhir-test-data-set/au-core/PractitionerRole-medicalradiation-fowler-christy.json) |  |  |  |
| [`frank-gaylene`](../au-fhir-test-data-set/au-core/Practitioner-frank-gaylene.json) | [`frank-gaylene`](../au-fhir-test-data-set/au-core/PractitionerRole-frank-gaylene.json) | [`westmead-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-medical-clinic.json) |  |  |
| [`fuller-christeen`](../au-fhir-test-data-set/au-core/Practitioner-fuller-christeen.json) | [`fuller-christeen`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-christeen.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |  |
| [`goodwin-rae`](../au-fhir-test-data-set/au-core/Practitioner-goodwin-rae.json) | [`goodwin-rae`](../au-fhir-test-data-set/au-core/PractitionerRole-goodwin-rae.json) | [`westmead-optical`](../au-fhir-test-data-set/au-core/Organization-westmead-optical.json) |  |  |
| [`hamilton-errol`](../au-fhir-test-data-set/au-core/Practitioner-hamilton-errol.json) | [`hamilton-errol`](../au-fhir-test-data-set/au-core/PractitionerRole-hamilton-errol.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`healey-tamiko`](../au-fhir-test-data-set/au-core/Practitioner-healey-tamiko.json) | [`healey-tamiko`](../au-fhir-test-data-set/au-core/PractitionerRole-healey-tamiko.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |  |
| [`howe-elden`](../au-fhir-test-data-set/au-core/Practitioner-howe-elden.json) | [`howe-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-howe-elden.json) | [`parramatta-midwifery`](../au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json) |  |  |
| [`knowles-sunshine`](../au-fhir-test-data-set/au-core/Practitioner-knowles-sunshine.json) | [`knowles-sunshine`](../au-fhir-test-data-set/au-core/PractitionerRole-knowles-sunshine.json) | [`westmead-ot-services`](../au-fhir-test-data-set/au-core/Organization-westmead-ot-services.json) |  |  |
| [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/Practitioner-lapthorn-leisa.json) | [`lapthorn-leisa`](../au-fhir-test-data-set/au-core/PractitionerRole-lapthorn-leisa.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |  |
| [`little-jerrie`](../au-fhir-test-data-set/au-core/Practitioner-little-jerrie.json) | [`little-jerrie`](../au-fhir-test-data-set/au-core/PractitionerRole-little-jerrie.json) | [`parramatta-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-medical-clinic.json) |  |  |
| [`macey-brant`](../au-fhir-test-data-set/au-core/Practitioner-macey-brant.json) | [`macey-brant`](../au-fhir-test-data-set/au-core/PractitionerRole-macey-brant.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |  |
| [`mackenzie-cinda`](../au-fhir-test-data-set/au-core/Practitioner-mackenzie-cinda.json) | [`surgeongeneral-mackenzie-cinda`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-mackenzie-cinda.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Location-kensington-public-hospital.json) | [`publicacute-kensington-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-kensington-public-hospital.json) |
| [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/Practitioner-mcbean-nicollette.json) | [`mcbean-nicollette`](../au-fhir-test-data-set/au-core/PractitionerRole-mcbean-nicollette.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/Practitioner-mcintosh-angelica.json) | [`mcintosh-angelica`](../au-fhir-test-data-set/au-core/PractitionerRole-mcintosh-angelica.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |  |
| [`mcnab-angelina`](../au-fhir-test-data-set/au-core/Practitioner-mcnab-angelina.json) | [`mcnab-angelina`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnab-angelina.json) | [`parramatta-nutrition`](../au-fhir-test-data-set/au-core/Organization-parramatta-nutrition.json) |  |  |
| [`mills-hope`](../au-fhir-test-data-set/au-core/Practitioner-mills-hope.json) | [`mills-hope`](../au-fhir-test-data-set/au-core/PractitionerRole-mills-hope.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`nairn-vince`](../au-fhir-test-data-set/au-core/Practitioner-nairn-vince.json) | [`nairn-vince`](../au-fhir-test-data-set/au-core/PractitionerRole-nairn-vince.json) | [`westmead-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-westmead-specialist-clinic.json) |  |  |
| [`neville-isaiah`](../au-fhir-test-data-set/au-core/Practitioner-neville-isaiah.json) | [`neville-isaiah`](../au-fhir-test-data-set/au-core/PractitionerRole-neville-isaiah.json) | [`westmead-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-westmead-physiotherapy.json) |  |  |
| [`nutley-bradley`](../au-fhir-test-data-set/au-core/Practitioner-nutley-bradley.json) | [`nutley-bradley`](../au-fhir-test-data-set/au-core/PractitionerRole-nutley-bradley.json) | [`westmead-pathology`](../au-fhir-test-data-set/au-core/Organization-westmead-pathology.json) |  |  |
| [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/Practitioner-ohalloran-sheryl.json) | [`ohalloran-sheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-ohalloran-sheryl.json) | [`westmead-pharmacy`](../au-fhir-test-data-set/au-core/Organization-westmead-pharmacy.json) |  |  |
| [`osmond-michele`](../au-fhir-test-data-set/au-core/Practitioner-osmond-michele.json) | [`osmond-michele`](../au-fhir-test-data-set/au-core/PractitionerRole-osmond-michele.json) | [`parramatta-dental`](../au-fhir-test-data-set/au-core/Organization-parramatta-dental.json) |  |  |
| [`perkins-amee`](../au-fhir-test-data-set/au-core/Practitioner-perkins-amee.json) | [`perkins-amee`](../au-fhir-test-data-set/au-core/PractitionerRole-perkins-amee.json) | [`westmead-radiology`](../au-fhir-test-data-set/au-core/Organization-westmead-radiology.json) |  |  |
| [`redman-mariah`](../au-fhir-test-data-set/au-core/Practitioner-redman-mariah.json) | [`redman-mariah`](../au-fhir-test-data-set/au-core/PractitionerRole-redman-mariah.json) | [`parramatta-midwifery`](../au-fhir-test-data-set/au-core/Organization-parramatta-midwifery.json) |  |  |
| [`roche-garfield`](../au-fhir-test-data-set/au-core/Practitioner-roche-garfield.json) | [`roche-garfield`](../au-fhir-test-data-set/au-core/PractitionerRole-roche-garfield.json) | [`westmead-radiology`](../au-fhir-test-data-set/au-core/Organization-westmead-radiology.json) |  |  |
| [`seaby-penelope`](../au-fhir-test-data-set/au-core/Practitioner-seaby-penelope.json) | [`seaby-penelope`](../au-fhir-test-data-set/au-core/PractitionerRole-seaby-penelope.json) | [`parramatta-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-parramatta-specialist-clinic.json) |  |  |
| [`shephard-lizabeth`](../au-fhir-test-data-set/au-core/Practitioner-shephard-lizabeth.json) | [`registerednurses-shephard-lizabeth`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shephard-lizabeth.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Location-kensington-public-hospital.json) | [`publicacute-kensington-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-kensington-public-hospital.json) |
| [`simons-reggie`](../au-fhir-test-data-set/au-core/Practitioner-simons-reggie.json) | [`nursepractitioner-simons-reggie`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-simons-reggie.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Organization-kensington-public-hospital.json) | [`kensington-public-hospital`](../au-fhir-test-data-set/au-core/Location-kensington-public-hospital.json) | [`publicacute-kensington-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-kensington-public-hospital.json) |
| [`stephens-nellie`](../au-fhir-test-data-set/au-core/Practitioner-stephens-nellie.json) | [`stephens-nellie`](../au-fhir-test-data-set/au-core/PractitionerRole-stephens-nellie.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |
| [`tate-melvin`](../au-fhir-test-data-set/au-core/Practitioner-tate-melvin.json) | [`tate-melvin`](../au-fhir-test-data-set/au-core/PractitionerRole-tate-melvin.json) | [`westmead-public-hospital`](../au-fhir-test-data-set/au-core/Organization-westmead-public-hospital.json) |  |  |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>NT</strong> (1 grouping, 37 entities)</summary>

<blockquote>
<details><summary><strong>Darwin metropolitan</strong> (37 entities)</summary>


_Acacia Hills, Annie River, Bayview, Coconut Grove, Cullen Bay, East Point, Ludmilla, Mitchell, Nguiu, Pulumpa, Southport._


**Patient** (2)

- [`archibald-dante`](../au-fhir-test-data-set/au-core/Patient-archibald-dante.json)
- [`todd-tanya-estelle`](../au-fhir-test-data-set/au-core/Patient-todd-tanya-estelle.json)

**Practitioner / PractitionerRole** (10)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`cook-natalie`](../au-fhir-test-data-set/au-core/Practitioner-cook-natalie.json) | [`osteopath-cook-natalie`](../au-fhir-test-data-set/au-core/PractitionerRole-osteopath-cook-natalie.json) | Osteopath (Osteopathic manipulative medicine) |  |
| [`coulter-francine`](../au-fhir-test-data-set/au-core/Practitioner-coulter-francine.json) | [`medicaldiagnostic-coulter-francine`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-coulter-francine.json) | Medical Diagnostic Radiographer |  |
| [`craig-kenneth`](../au-fhir-test-data-set/au-core/Practitioner-craig-kenneth.json) | [`registerednurses-craig-kenneth`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-craig-kenneth.json) | Registered Nurses nec (Nursing) |  |
| [`darcy-alexandra`](../au-fhir-test-data-set/au-core/Practitioner-darcy-alexandra.json) | [`physiotherapist-darcy-alexandra`](../au-fhir-test-data-set/au-core/PractitionerRole-physiotherapist-darcy-alexandra.json) | Physiotherapist (Physiotherapy) |  |
| [`faint-darryl`](../au-fhir-test-data-set/au-core/Practitioner-faint-darryl.json) | [`generalpractitioner-faint-darryl`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-faint-darryl.json) | General Practitioner (General medical practice) |  |
| [`gifford-cassidy`](../au-fhir-test-data-set/au-core/Practitioner-gifford-cassidy.json) | [`pathologist-gifford-cassidy`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-gifford-cassidy.json) | Pathologist (Pathology) |  |
| [`gillies-han`](../au-fhir-test-data-set/au-core/Practitioner-gillies-han.json) | [`aboriginal-gillies-han`](../au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-gillies-han.json) | Aboriginal and Torres Strait Islander Health Worker |  |
| [`harding-clyde`](../au-fhir-test-data-set/au-core/Practitioner-harding-clyde.json) | [`retailpharmacist-harding-clyde`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-harding-clyde.json) | Retail Pharmacist (Community pharmacy) |  |
| [`mccormack-annamaria`](../au-fhir-test-data-set/au-core/Practitioner-mccormack-annamaria.json) | [`registerednurses-mccormack-annamaria`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-mccormack-annamaria.json) | Registered Nurses nec (Nursing) |  |
| [`polglase-belen`](../au-fhir-test-data-set/au-core/Practitioner-polglase-belen.json) | [`counsellorsnec-polglase-belen`](../au-fhir-test-data-set/au-core/PractitionerRole-counsellorsnec-polglase-belen.json) | Counsellors nec |  |

**HealthcareService** (5)

- [`communityhealth-annie-river-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-annie-river-practice.json)
- [`generalpractice-cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-cullen-bay-medical-clinic.json)
- [`pathologylaboratory-bayview-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-bayview-pathology.json)
- [`pharmacyretail-ludmilla-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-ludmilla-pharmacy.json)
- [`specialistmedical-east-point-renal-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-east-point-renal-clinic.json)

**Organization** (5)

- [`annie-river-practice`](../au-fhir-test-data-set/au-core/Organization-annie-river-practice.json)
- [`bayview-pathology`](../au-fhir-test-data-set/au-core/Organization-bayview-pathology.json)
- [`cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-cullen-bay-medical-clinic.json)
- [`east-point-renal-clinic`](../au-fhir-test-data-set/au-core/Organization-east-point-renal-clinic.json)
- [`ludmilla-pharmacy`](../au-fhir-test-data-set/au-core/Organization-ludmilla-pharmacy.json)

**Location** (5)

- [`annie-river-practice`](../au-fhir-test-data-set/au-core/Location-annie-river-practice.json)
- [`bayview-pathology`](../au-fhir-test-data-set/au-core/Location-bayview-pathology.json)
- [`cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/Location-cullen-bay-medical-clinic.json)
- [`east-point-renal-clinic`](../au-fhir-test-data-set/au-core/Location-east-point-renal-clinic.json)
- [`ludmilla-pharmacy`](../au-fhir-test-data-set/au-core/Location-ludmilla-pharmacy.json)

<details><summary>10 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`cook-natalie`](../au-fhir-test-data-set/au-core/Practitioner-cook-natalie.json) | [`osteopath-cook-natalie`](../au-fhir-test-data-set/au-core/PractitionerRole-osteopath-cook-natalie.json) |  |  |  |
| [`coulter-francine`](../au-fhir-test-data-set/au-core/Practitioner-coulter-francine.json) | [`medicaldiagnostic-coulter-francine`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-coulter-francine.json) |  |  |  |
| [`craig-kenneth`](../au-fhir-test-data-set/au-core/Practitioner-craig-kenneth.json) | [`registerednurses-craig-kenneth`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-craig-kenneth.json) | [`annie-river-practice`](../au-fhir-test-data-set/au-core/Organization-annie-river-practice.json) | [`annie-river-practice`](../au-fhir-test-data-set/au-core/Location-annie-river-practice.json) | [`communityhealth-annie-river-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-annie-river-practice.json) |
| [`darcy-alexandra`](../au-fhir-test-data-set/au-core/Practitioner-darcy-alexandra.json) | [`physiotherapist-darcy-alexandra`](../au-fhir-test-data-set/au-core/PractitionerRole-physiotherapist-darcy-alexandra.json) |  |  |  |
| [`faint-darryl`](../au-fhir-test-data-set/au-core/Practitioner-faint-darryl.json) | [`generalpractitioner-faint-darryl`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-faint-darryl.json) | [`cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-cullen-bay-medical-clinic.json) | [`cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/Location-cullen-bay-medical-clinic.json) | [`generalpractice-cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-cullen-bay-medical-clinic.json) |
| [`gifford-cassidy`](../au-fhir-test-data-set/au-core/Practitioner-gifford-cassidy.json) | [`pathologist-gifford-cassidy`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-gifford-cassidy.json) | [`bayview-pathology`](../au-fhir-test-data-set/au-core/Organization-bayview-pathology.json) | [`bayview-pathology`](../au-fhir-test-data-set/au-core/Location-bayview-pathology.json) | [`pathologylaboratory-bayview-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-bayview-pathology.json) |
| [`gillies-han`](../au-fhir-test-data-set/au-core/Practitioner-gillies-han.json) | [`aboriginal-gillies-han`](../au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-gillies-han.json) | [`annie-river-practice`](../au-fhir-test-data-set/au-core/Organization-annie-river-practice.json) | [`annie-river-practice`](../au-fhir-test-data-set/au-core/Location-annie-river-practice.json) | [`communityhealth-annie-river-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-annie-river-practice.json) |
| [`harding-clyde`](../au-fhir-test-data-set/au-core/Practitioner-harding-clyde.json) | [`retailpharmacist-harding-clyde`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-harding-clyde.json) | [`ludmilla-pharmacy`](../au-fhir-test-data-set/au-core/Organization-ludmilla-pharmacy.json) | [`ludmilla-pharmacy`](../au-fhir-test-data-set/au-core/Location-ludmilla-pharmacy.json) | [`pharmacyretail-ludmilla-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-ludmilla-pharmacy.json) |
| [`mccormack-annamaria`](../au-fhir-test-data-set/au-core/Practitioner-mccormack-annamaria.json) | [`registerednurses-mccormack-annamaria`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-mccormack-annamaria.json) | [`cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-cullen-bay-medical-clinic.json) | [`cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/Location-cullen-bay-medical-clinic.json) | [`generalpractice-cullen-bay-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-cullen-bay-medical-clinic.json) |
| [`polglase-belen`](../au-fhir-test-data-set/au-core/Practitioner-polglase-belen.json) | [`counsellorsnec-polglase-belen`](../au-fhir-test-data-set/au-core/PractitionerRole-counsellorsnec-polglase-belen.json) |  |  |  |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>QLD</strong> (12 groupings, 131 entities)</summary>

<blockquote>
<details><summary><strong>Brisbane metropolitan</strong> (22 entities)</summary>


_Brisbane, Herston, Logan Reserve, Loganlea, Wilston._


**Patient** (3)

- [`belger-remedios`](../au-fhir-test-data-set/au-erequesting/Patient-belger-remedios.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*
- [`bennelong-anne`](../au-fhir-test-data-set/au-core/Patient-bennelong-anne.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*
- [`odonnell-gillian`](../au-fhir-test-data-set/au-core/Patient-odonnell-gillian.json)

**Practitioner / PractitionerRole** (8)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`bowden-hiroko`](../au-fhir-test-data-set/au-core/Practitioner-bowden-hiroko.json) | [`bowden-hiroko`](../au-fhir-test-data-set/au-core/PractitionerRole-bowden-hiroko.json) | Neurosurgeon (Neurosurgery) | [scenario-groups](#scenario-groups) |
| [`greenhill-edmond`](../au-fhir-test-data-set/au-core/Practitioner-greenhill-edmond.json) | [`greenhill-edmond`](../au-fhir-test-data-set/au-core/PractitionerRole-greenhill-edmond.json) | Pathologist (Clinical pathology) | [scenario-groups](#scenario-groups) |
| [`irwin-corinna`](../au-fhir-test-data-set/au-core/Practitioner-irwin-corinna.json) | [`irwin-corinna`](../au-fhir-test-data-set/au-core/PractitionerRole-irwin-corinna.json) | Emergency Medicine Specialist / Emergency Physician (Emergency medicine) | [scenario-groups](#scenario-groups) |
| [`jeffery-sammy`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json) | [`jeffery-sammy`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`lyons-shay`](../au-fhir-test-data-set/au-core/Practitioner-lyons-shay.json) | [`lyons-shay`](../au-fhir-test-data-set/au-core/PractitionerRole-lyons-shay.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [scenario-groups](#scenario-groups) |
| [`mclean-brenda`](../au-fhir-test-data-set/au-core/Practitioner-mclean-brenda.json) | [`mclean-brenda`](../au-fhir-test-data-set/au-core/PractitionerRole-mclean-brenda.json) | Orthopaedic Surgeon (Surgical orthopedic specialty) | [scenario-groups](#scenario-groups) |
| [`sherry-dean`](../au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json) | [`sherry-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json) | Occupational Therapist | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`stapleton-carole`](../au-fhir-test-data-set/au-core/Practitioner-stapleton-carole.json) | [`speechpathologist-stapleton-carole`](../au-fhir-test-data-set/au-core/PractitionerRole-speechpathologist-stapleton-carole.json) | Speech Pathologist (Aus) \ Speech Language Therapist (NZ) |  |

**Organization** (3)

- [`herston-pathology`](../au-fhir-test-data-set/au-core/Organization-herston-pathology.json) — *also in: [scenario-groups](#scenario-groups)*
- [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) — *also in: [scenario-groups](#scenario-groups)*
- [`herston-radiology`](../au-fhir-test-data-set/au-core/Organization-herston-radiology.json) — *also in: [scenario-groups](#scenario-groups)*

<details><summary>8 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`bowden-hiroko`](../au-fhir-test-data-set/au-core/Practitioner-bowden-hiroko.json) | [`bowden-hiroko`](../au-fhir-test-data-set/au-core/PractitionerRole-bowden-hiroko.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`greenhill-edmond`](../au-fhir-test-data-set/au-core/Practitioner-greenhill-edmond.json) | [`greenhill-edmond`](../au-fhir-test-data-set/au-core/PractitionerRole-greenhill-edmond.json) | [`herston-pathology`](../au-fhir-test-data-set/au-core/Organization-herston-pathology.json) |  |
| [`irwin-corinna`](../au-fhir-test-data-set/au-core/Practitioner-irwin-corinna.json) | [`irwin-corinna`](../au-fhir-test-data-set/au-core/PractitionerRole-irwin-corinna.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`jeffery-sammy`](../au-fhir-test-data-set/au-core/Practitioner-jeffery-sammy.json) | [`jeffery-sammy`](../au-fhir-test-data-set/au-core/PractitionerRole-jeffery-sammy.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`lyons-shay`](../au-fhir-test-data-set/au-core/Practitioner-lyons-shay.json) | [`lyons-shay`](../au-fhir-test-data-set/au-core/PractitionerRole-lyons-shay.json) | [`herston-radiology`](../au-fhir-test-data-set/au-core/Organization-herston-radiology.json) |  |
| [`mclean-brenda`](../au-fhir-test-data-set/au-core/Practitioner-mclean-brenda.json) | [`mclean-brenda`](../au-fhir-test-data-set/au-core/PractitionerRole-mclean-brenda.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`sherry-dean`](../au-fhir-test-data-set/au-core/Practitioner-sherry-dean.json) | [`sherry-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-sherry-dean.json) | [`herston-public-hospital`](../au-fhir-test-data-set/au-core/Organization-herston-public-hospital.json) |  |
| [`stapleton-carole`](../au-fhir-test-data-set/au-core/Practitioner-stapleton-carole.json) | [`speechpathologist-stapleton-carole`](../au-fhir-test-data-set/au-core/PractitionerRole-speechpathologist-stapleton-carole.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 420xx-422xx</strong> (2 entities)</summary>


_Miami, Oxenford._


**Patient** (1)

- [`lynch-alyce-shauna`](../au-fhir-test-data-set/au-core/Patient-lynch-alyce-shauna.json)

**Organization** (1)

- [`oxenford-care-and-support`](../au-fhir-test-data-set/au-core/Organization-oxenford-care-and-support.json) — *also in: [community-contributions](#community-contributions)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 427xx-429xx</strong> (15 entities)</summary>


_Barney View, Cedar Grove._


**Practitioner / PractitionerRole** (5)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`armstrong-amada`](../au-fhir-test-data-set/au-core/Practitioner-armstrong-amada.json) | [`surgeongeneral-armstrong-amada`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-armstrong-amada.json) | Surgeon (General) (General surgery) |  |
| [`haywood-byron`](../au-fhir-test-data-set/au-core/Practitioner-haywood-byron.json) | [`nursepractitioner-haywood-byron`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-haywood-byron.json) | Nurse Practitioner (Nursing) |  |
| [`kelly-virginia`](../au-fhir-test-data-set/au-core/Practitioner-kelly-virginia.json) | [`dietitian-kelly-virginia`](../au-fhir-test-data-set/au-core/PractitionerRole-dietitian-kelly-virginia.json) | Dietitian (Dietetics and nutrition) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`manning-meg`](../au-fhir-test-data-set/au-core/Practitioner-manning-meg.json) | [`cardiothoracicsurgeon-manning-meg`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiothoracicsurgeon-manning-meg.json) | Cardiothoracic Surgeon (Cardiothoracic surgery) |  |
| [`sinclair-forrest`](../au-fhir-test-data-set/au-core/Practitioner-sinclair-forrest.json) | [`registerednurses-sinclair-forrest`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-sinclair-forrest.json) | Registered Nurses nec (Nursing) |  |

**HealthcareService** (1)

- [`privateacute-barney-view-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-barney-view-private-hospital.json)

**Organization** (1)

- [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*

**Location** (3)

- [`au-hospital-pharm-out`](../au-fhir-test-data-set/au-core/Location-au-hospital-pharm-out.json)
- [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*
- [`renal-dialysis-unit`](../au-fhir-test-data-set/au-core/Location-renal-dialysis-unit.json)

<details><summary>5 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`armstrong-amada`](../au-fhir-test-data-set/au-core/Practitioner-armstrong-amada.json) | [`surgeongeneral-armstrong-amada`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-armstrong-amada.json) | [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json) | [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json) | [`privateacute-barney-view-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-barney-view-private-hospital.json) |
| [`haywood-byron`](../au-fhir-test-data-set/au-core/Practitioner-haywood-byron.json) | [`nursepractitioner-haywood-byron`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-haywood-byron.json) | [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json) | [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json) | [`privateacute-barney-view-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-barney-view-private-hospital.json) |
| [`kelly-virginia`](../au-fhir-test-data-set/au-core/Practitioner-kelly-virginia.json) | [`dietitian-kelly-virginia`](../au-fhir-test-data-set/au-core/PractitionerRole-dietitian-kelly-virginia.json) |  |  |  |
| [`manning-meg`](../au-fhir-test-data-set/au-core/Practitioner-manning-meg.json) | [`cardiothoracicsurgeon-manning-meg`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiothoracicsurgeon-manning-meg.json) |  |  |  |
| [`sinclair-forrest`](../au-fhir-test-data-set/au-core/Practitioner-sinclair-forrest.json) | [`registerednurses-sinclair-forrest`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-sinclair-forrest.json) | [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Organization-barney-view-private-hospital.json) | [`barney-view-private-hospital`](../au-fhir-test-data-set/au-core/Location-barney-view-private-hospital.json) | [`privateacute-barney-view-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-barney-view-private-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 430xx-432xx</strong> (5 entities)</summary>


_Tarampa._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`mitchell-frankie`](../au-fhir-test-data-set/au-core/Practitioner-mitchell-frankie.json) | [`emergencymedicine-mitchell-frankie`](../au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-mitchell-frankie.json) | Emergency Medicine Specialist (Emergency medicine) |  |

**HealthcareService** (1)

- [`emergencydepartment-tarampa-emergency`](../au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-tarampa-emergency.json)

**Organization** (1)

- [`tarampa-emergency`](../au-fhir-test-data-set/au-core/Organization-tarampa-emergency.json)

**Location** (1)

- [`tarampa-emergency`](../au-fhir-test-data-set/au-core/Location-tarampa-emergency.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`mitchell-frankie`](../au-fhir-test-data-set/au-core/Practitioner-mitchell-frankie.json) | [`emergencymedicine-mitchell-frankie`](../au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-mitchell-frankie.json) | [`tarampa-emergency`](../au-fhir-test-data-set/au-core/Organization-tarampa-emergency.json) | [`tarampa-emergency`](../au-fhir-test-data-set/au-core/Location-tarampa-emergency.json) | [`emergencydepartment-tarampa-emergency`](../au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-tarampa-emergency.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 435xx-437xx</strong> (30 entities)</summary>


_Berat, Carrington, Glennie Heights, Loch Lomond, Morgan Park, Purrawunda, Westbrook._


**Patient** (2)

- [`hayes-arianne`](../au-fhir-test-data-set/au-core/Patient-hayes-arianne.json) — *also in: [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)*
- [`roberts-fred`](../au-fhir-test-data-set/au-erequesting/Patient-roberts-fred.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)*

**Practitioner / PractitionerRole** (8)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`berry-millicent`](../au-fhir-test-data-set/au-core/Practitioner-berry-millicent.json) | [`diagnostic-berry-millicent`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-berry-millicent.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`macnab-gregory`](../au-fhir-test-data-set/au-core/Practitioner-macnab-gregory.json) | [`psychiatrist-macnab-gregory`](../au-fhir-test-data-set/au-core/PractitionerRole-psychiatrist-macnab-gregory.json) | Psychiatrist (Psychiatry) |  |
| [`marchant-ricki`](../au-fhir-test-data-set/au-core/Practitioner-marchant-ricki.json) | [`surgeongeneral-marchant-ricki`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-marchant-ricki.json) | Surgeon (General) (General surgery) |  |
| [`morton-eric`](../au-fhir-test-data-set/au-core/Practitioner-morton-eric.json) | [`registerednurses-morton-eric`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-morton-eric.json) | Registered Nurses nec (Nursing) |  |
| [`rowland-roger`](../au-fhir-test-data-set/au-core/Practitioner-rowland-roger.json) | [`registerednurses-rowland-roger`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-rowland-roger.json) | Registered Nurses nec (Nursing) | [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`samuels-wyatt`](../au-fhir-test-data-set/au-core/Practitioner-samuels-wyatt.json) | [`generalpractitioner-samuels-wyatt`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-samuels-wyatt.json) | General Practitioner (General medical practice) |  |
| [`shearer-joesfine`](../au-fhir-test-data-set/au-core/Practitioner-shearer-joesfine.json) | [`pathologist-shearer-joesfine`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-shearer-joesfine.json) | Pathologist (Pathology) |  |
| [`springett-angelo`](../au-fhir-test-data-set/au-core/Practitioner-springett-angelo.json) | [`nursepractitioner-springett-angelo`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-springett-angelo.json) | Nurse Practitioner (Nursing) |  |

**HealthcareService** (4)

- [`diagnosticimaging-berat-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-berat-radiology.json)
- [`generalpractice-loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-loch-lomond-medical-clinic.json)
- [`pathologylaboratory-carrington-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-carrington-pathology.json)
- [`publicacute-glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-glennie-heights-public-hospital.json)

**Organization** (4)

- [`berat-radiology`](../au-fhir-test-data-set/au-core/Organization-berat-radiology.json)
- [`carrington-pathology`](../au-fhir-test-data-set/au-core/Organization-carrington-pathology.json)
- [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Organization-glennie-heights-public-hospital.json)
- [`loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-loch-lomond-medical-clinic.json)

**Location** (4)

- [`berat-radiology`](../au-fhir-test-data-set/au-core/Location-berat-radiology.json)
- [`carrington-pathology`](../au-fhir-test-data-set/au-core/Location-carrington-pathology.json)
- [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Location-glennie-heights-public-hospital.json)
- [`loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/Location-loch-lomond-medical-clinic.json)

<details><summary>8 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`berry-millicent`](../au-fhir-test-data-set/au-core/Practitioner-berry-millicent.json) | [`diagnostic-berry-millicent`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-berry-millicent.json) | [`berat-radiology`](../au-fhir-test-data-set/au-core/Organization-berat-radiology.json) | [`berat-radiology`](../au-fhir-test-data-set/au-core/Location-berat-radiology.json) | [`diagnosticimaging-berat-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-berat-radiology.json) |
| [`macnab-gregory`](../au-fhir-test-data-set/au-core/Practitioner-macnab-gregory.json) | [`psychiatrist-macnab-gregory`](../au-fhir-test-data-set/au-core/PractitionerRole-psychiatrist-macnab-gregory.json) |  |  |  |
| [`marchant-ricki`](../au-fhir-test-data-set/au-core/Practitioner-marchant-ricki.json) | [`surgeongeneral-marchant-ricki`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-marchant-ricki.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Organization-glennie-heights-public-hospital.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Location-glennie-heights-public-hospital.json) | [`publicacute-glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-glennie-heights-public-hospital.json) |
| [`morton-eric`](../au-fhir-test-data-set/au-core/Practitioner-morton-eric.json) | [`registerednurses-morton-eric`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-morton-eric.json) | [`loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-loch-lomond-medical-clinic.json) | [`loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/Location-loch-lomond-medical-clinic.json) | [`generalpractice-loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-loch-lomond-medical-clinic.json) |
| [`rowland-roger`](../au-fhir-test-data-set/au-core/Practitioner-rowland-roger.json) | [`registerednurses-rowland-roger`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-rowland-roger.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Organization-glennie-heights-public-hospital.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Location-glennie-heights-public-hospital.json) | [`publicacute-glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-glennie-heights-public-hospital.json) |
| [`samuels-wyatt`](../au-fhir-test-data-set/au-core/Practitioner-samuels-wyatt.json) | [`generalpractitioner-samuels-wyatt`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-samuels-wyatt.json) | [`loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-loch-lomond-medical-clinic.json) | [`loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/Location-loch-lomond-medical-clinic.json) | [`generalpractice-loch-lomond-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-loch-lomond-medical-clinic.json) |
| [`shearer-joesfine`](../au-fhir-test-data-set/au-core/Practitioner-shearer-joesfine.json) | [`pathologist-shearer-joesfine`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-shearer-joesfine.json) | [`carrington-pathology`](../au-fhir-test-data-set/au-core/Organization-carrington-pathology.json) | [`carrington-pathology`](../au-fhir-test-data-set/au-core/Location-carrington-pathology.json) | [`pathologylaboratory-carrington-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-carrington-pathology.json) |
| [`springett-angelo`](../au-fhir-test-data-set/au-core/Practitioner-springett-angelo.json) | [`nursepractitioner-springett-angelo`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-springett-angelo.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Organization-glennie-heights-public-hospital.json) | [`glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/Location-glennie-heights-public-hospital.json) | [`publicacute-glennie-heights-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-glennie-heights-public-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 438xx-439xx</strong> (3 entities)</summary>


_Goondiwindi, Lundavra._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`gore-jess`](../au-fhir-test-data-set/au-core/Practitioner-gore-jess.json) | [`chiropractor-gore-jess`](../au-fhir-test-data-set/au-core/PractitionerRole-chiropractor-gore-jess.json) | Chiropractor |  |

**Organization** (1)

- [`goondiwindi-health-network`](../au-fhir-test-data-set/au-core/Organization-goondiwindi-health-network.json) — *also in: [community-contributions](#community-contributions)*

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`gore-jess`](../au-fhir-test-data-set/au-core/Practitioner-gore-jess.json) | [`chiropractor-gore-jess`](../au-fhir-test-data-set/au-core/PractitionerRole-chiropractor-gore-jess.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 448xx-449xx</strong> (5 entities)</summary>


_Kioma._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`herbert-aimee`](../au-fhir-test-data-set/au-core/Practitioner-herbert-aimee.json) | [`pathologist-herbert-aimee`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-herbert-aimee.json) | Pathologist (Pathology) | [au-erequesting-ig-examples](#au-erequesting-ig-examples) |

**HealthcareService** (1)

- [`pathologylaboratory-kioma-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kioma-pathology.json)

**Organization** (1)

- [`kioma-pathology`](../au-fhir-test-data-set/au-core/Organization-kioma-pathology.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*

**Location** (1)

- [`kioma-pathology`](../au-fhir-test-data-set/au-core/Location-kioma-pathology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`herbert-aimee`](../au-fhir-test-data-set/au-core/Practitioner-herbert-aimee.json) | [`pathologist-herbert-aimee`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-herbert-aimee.json) | [`kioma-pathology`](../au-fhir-test-data-set/au-core/Organization-kioma-pathology.json) | [`kioma-pathology`](../au-fhir-test-data-set/au-core/Location-kioma-pathology.json) | [`pathologylaboratory-kioma-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kioma-pathology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 450xx-452xx</strong> (8 entities)</summary>


_Draper, Elimbah._


**Patient** (1)

- [`boulton-annika`](../au-fhir-test-data-set/au-core/Patient-boulton-annika.json) — *also in: [sparked-cdg-journeys](#sparked-cdg-journeys)*

**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`egan-shae`](../au-fhir-test-data-set/au-core/Practitioner-egan-shae.json) | [`registerednurses-egan-shae`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-egan-shae.json) | Registered Nurses nec (Nursing) |  |
| [`guthridge-jarred`](../au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json) | [`generalpractitioner-guthridge-jarred`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json) | General Practitioner (General medical practice) | [au-erequesting-ig-examples](#au-erequesting-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys) |

**HealthcareService** (1)

- [`generalmedical-elimbah-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-elimbah-medical-centre.json)

**Organization** (1)

- [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*

**Location** (1)

- [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Location-elimbah-medical-centre.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`egan-shae`](../au-fhir-test-data-set/au-core/Practitioner-egan-shae.json) | [`registerednurses-egan-shae`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-egan-shae.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Location-elimbah-medical-centre.json) | [`generalmedical-elimbah-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-elimbah-medical-centre.json) |
| [`guthridge-jarred`](../au-fhir-test-data-set/au-core/Practitioner-guthridge-jarred.json) | [`generalpractitioner-guthridge-jarred`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-guthridge-jarred.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Organization-elimbah-medical-centre.json) | [`elimbah-medical-centre`](../au-fhir-test-data-set/au-core/Location-elimbah-medical-centre.json) | [`generalmedical-elimbah-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-elimbah-medical-centre.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 464xx-466xx</strong> (3 entities)</summary>


_Tindal RAAF, Walliebum._


**Patient** (1)

- [`martin-shawn`](../au-fhir-test-data-set/au-core/Patient-martin-shawn.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*

**Organization** (1)

- [`bobrester-medical-center`](../au-fhir-test-data-set/au-core/Organization-bobrester-medical-center.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*

**Location** (1)

- [`bobrester-medical-center`](../au-fhir-test-data-set/au-core/Location-bobrester-medical-center.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 470xx-471xx</strong> (7 entities)</summary>


_Banana, Cracow._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`crowley-pablo`](../au-fhir-test-data-set/au-core/Practitioner-crowley-pablo.json) | [`plastic-crowley-pablo`](../au-fhir-test-data-set/au-core/PractitionerRole-plastic-crowley-pablo.json) | Plastic and Reconstructive Surgeon (Plastic surgery - speciality) |  |
| [`patrick-manual`](../au-fhir-test-data-set/au-core/Practitioner-patrick-manual.json) | [`retailpharmacist-patrick-manual`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-patrick-manual.json) | Retail Pharmacist (Community pharmacy) | [sparked-cdg-journeys](#sparked-cdg-journeys) |

**HealthcareService** (1)

- [`communitypharmacy-cracow-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-cracow-pharmacy.json)

**Organization** (1)

- [`cracow-pharmacy`](../au-fhir-test-data-set/au-core/Organization-cracow-pharmacy.json)

**Location** (1)

- [`cracow-pharmacy`](../au-fhir-test-data-set/au-core/Location-cracow-pharmacy.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`crowley-pablo`](../au-fhir-test-data-set/au-core/Practitioner-crowley-pablo.json) | [`plastic-crowley-pablo`](../au-fhir-test-data-set/au-core/PractitionerRole-plastic-crowley-pablo.json) |  |  |  |
| [`patrick-manual`](../au-fhir-test-data-set/au-core/Practitioner-patrick-manual.json) | [`retailpharmacist-patrick-manual`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-patrick-manual.json) | [`cracow-pharmacy`](../au-fhir-test-data-set/au-core/Organization-cracow-pharmacy.json) | [`cracow-pharmacy`](../au-fhir-test-data-set/au-core/Location-cracow-pharmacy.json) | [`communitypharmacy-cracow-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-cracow-pharmacy.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 473xx-475xx</strong> (10 entities)</summary>


_East Mackay, Mount Charlton._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`ford-dean`](../au-fhir-test-data-set/au-core/Practitioner-ford-dean.json) | [`retailpharmacist-ford-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-ford-dean.json) | Retail Pharmacist (Community pharmacy) |  |
| [`mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/Practitioner-mclaughlin-kimberlee.json) | [`diagnostic-mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mclaughlin-kimberlee.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [au-erequesting-ig-examples](#au-erequesting-ig-examples) |

**HealthcareService** (2)

- [`diagnosticimaging-mount-charlton-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mount-charlton-radiology.json)
- [`pharmacyretail-east-mackay-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-east-mackay-pharmacy.json)

**Organization** (2)

- [`east-mackay-pharmacy`](../au-fhir-test-data-set/au-core/Organization-east-mackay-pharmacy.json)
- [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Organization-mount-charlton-radiology.json) — *also in: [au-erequesting-ig-examples](#au-erequesting-ig-examples)*

**Location** (2)

- [`east-mackay-pharmacy`](../au-fhir-test-data-set/au-core/Location-east-mackay-pharmacy.json)
- [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Location-mount-charlton-radiology.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`ford-dean`](../au-fhir-test-data-set/au-core/Practitioner-ford-dean.json) | [`retailpharmacist-ford-dean`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-ford-dean.json) | [`east-mackay-pharmacy`](../au-fhir-test-data-set/au-core/Organization-east-mackay-pharmacy.json) | [`east-mackay-pharmacy`](../au-fhir-test-data-set/au-core/Location-east-mackay-pharmacy.json) | [`pharmacyretail-east-mackay-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-east-mackay-pharmacy.json) |
| [`mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/Practitioner-mclaughlin-kimberlee.json) | [`diagnostic-mclaughlin-kimberlee`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mclaughlin-kimberlee.json) | [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Organization-mount-charlton-radiology.json) | [`mount-charlton-radiology`](../au-fhir-test-data-set/au-core/Location-mount-charlton-radiology.json) | [`diagnosticimaging-mount-charlton-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mount-charlton-radiology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 485xx-487xx</strong> (21 entities)</summary>


_Bayview Heights, Hudson, Southedge._


**Practitioner / PractitionerRole** (6)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`berry-shay`](../au-fhir-test-data-set/au-core/Practitioner-berry-shay.json) | [`registerednurses-berry-shay`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-berry-shay.json) | Registered Nurses nec (Nursing) |  |
| [`coulter-oliver`](../au-fhir-test-data-set/au-core/Practitioner-coulter-oliver.json) | [`aboriginal-coulter-oliver`](../au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-coulter-oliver.json) | Aboriginal and Torres Strait Islander Health Worker |  |
| [`lamerton-buck`](../au-fhir-test-data-set/au-core/Practitioner-lamerton-buck.json) | [`registerednurses-lamerton-buck`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-lamerton-buck.json) | Registered Nurses nec (Nursing) |  |
| [`leeds-luigi`](../au-fhir-test-data-set/au-core/Practitioner-leeds-luigi.json) | [`medicaloncologist-leeds-luigi`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-leeds-luigi.json) | Medical Oncologist (Medical oncology) |  |
| [`mclean-lizzette`](../au-fhir-test-data-set/au-core/Practitioner-mclean-lizzette.json) | [`registerednurses-mclean-lizzette`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-mclean-lizzette.json) | Registered Nurses nec (Nursing) |  |
| [`mcleod-clinton`](../au-fhir-test-data-set/au-core/Practitioner-mcleod-clinton.json) | [`nursepractitioner-mcleod-clinton`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-mcleod-clinton.json) | Nurse Practitioner (Nursing) |  |

**HealthcareService** (3)

- [`communityhealth-southedge-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-southedge-practice.json)
- [`privateprofit-hudson-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-hudson-aged-care.json)
- [`specialistmedical-bayview-heights-oncology-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-bayview-heights-oncology-clinic.json)

**Organization** (3)

- [`bayview-heights-oncology-clinic`](../au-fhir-test-data-set/au-core/Organization-bayview-heights-oncology-clinic.json)
- [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Organization-hudson-aged-care.json)
- [`southedge-practice`](../au-fhir-test-data-set/au-core/Organization-southedge-practice.json)

**Location** (3)

- [`bayview-heights-oncology-clinic`](../au-fhir-test-data-set/au-core/Location-bayview-heights-oncology-clinic.json)
- [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Location-hudson-aged-care.json)
- [`southedge-practice`](../au-fhir-test-data-set/au-core/Location-southedge-practice.json)

<details><summary>6 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`berry-shay`](../au-fhir-test-data-set/au-core/Practitioner-berry-shay.json) | [`registerednurses-berry-shay`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-berry-shay.json) | [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Organization-hudson-aged-care.json) | [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Location-hudson-aged-care.json) | [`privateprofit-hudson-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-hudson-aged-care.json) |
| [`coulter-oliver`](../au-fhir-test-data-set/au-core/Practitioner-coulter-oliver.json) | [`aboriginal-coulter-oliver`](../au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-coulter-oliver.json) | [`southedge-practice`](../au-fhir-test-data-set/au-core/Organization-southedge-practice.json) | [`southedge-practice`](../au-fhir-test-data-set/au-core/Location-southedge-practice.json) | [`communityhealth-southedge-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-southedge-practice.json) |
| [`lamerton-buck`](../au-fhir-test-data-set/au-core/Practitioner-lamerton-buck.json) | [`registerednurses-lamerton-buck`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-lamerton-buck.json) | [`southedge-practice`](../au-fhir-test-data-set/au-core/Organization-southedge-practice.json) | [`southedge-practice`](../au-fhir-test-data-set/au-core/Location-southedge-practice.json) | [`communityhealth-southedge-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-southedge-practice.json) |
| [`leeds-luigi`](../au-fhir-test-data-set/au-core/Practitioner-leeds-luigi.json) | [`medicaloncologist-leeds-luigi`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaloncologist-leeds-luigi.json) |  |  |  |
| [`mclean-lizzette`](../au-fhir-test-data-set/au-core/Practitioner-mclean-lizzette.json) | [`registerednurses-mclean-lizzette`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-mclean-lizzette.json) | [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Organization-hudson-aged-care.json) | [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Location-hudson-aged-care.json) | [`privateprofit-hudson-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-hudson-aged-care.json) |
| [`mcleod-clinton`](../au-fhir-test-data-set/au-core/Practitioner-mcleod-clinton.json) | [`nursepractitioner-mcleod-clinton`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-mcleod-clinton.json) | [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Organization-hudson-aged-care.json) | [`hudson-aged-care`](../au-fhir-test-data-set/au-core/Location-hudson-aged-care.json) | [`privateprofit-hudson-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-hudson-aged-care.json) |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>SA</strong> (6 groupings, 118 entities)</summary>

<blockquote>
<details><summary><strong>Adelaide metropolitan</strong> (74 entities)</summary>


_Adelaide, Croydon, Edwardstown, Hawthorn, Park Holme, Royal park, Salisbury South Dc, Semaphore, South Brighton, Wingfield, Woodcroft, Woodville._


**Patient** (1)

- [`reece-karen`](../au-fhir-test-data-set/au-core/Patient-reece-karen.json) — *also in: [scenario-groups](#scenario-groups)*

**Practitioner / PractitionerRole** (26)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`baker-troy`](../au-fhir-test-data-set/au-core/Practitioner-baker-troy.json) | [`baker-troy`](../au-fhir-test-data-set/au-core/PractitionerRole-baker-troy.json) | Pathologist (Clinical pathology) | [scenario-groups](#scenario-groups) |
| [`baynton-lolita`](../au-fhir-test-data-set/au-core/Practitioner-baynton-lolita.json) | [`baynton-lolita`](../au-fhir-test-data-set/au-core/PractitionerRole-baynton-lolita.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups) |
| [`bell-rudolf`](../au-fhir-test-data-set/au-core/Practitioner-bell-rudolf.json) | [`bell-rudolf`](../au-fhir-test-data-set/au-core/PractitionerRole-bell-rudolf.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`berry-lisa`](../au-fhir-test-data-set/au-core/Practitioner-berry-lisa.json) | [`berry-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-berry-lisa.json) | Occupational Therapist | [scenario-groups](#scenario-groups) |
| [`carey-joyce`](../au-fhir-test-data-set/au-core/Practitioner-carey-joyce.json) | [`carey-joyce`](../au-fhir-test-data-set/au-core/PractitionerRole-carey-joyce.json) | Geriatrician (Geriatric medicine) | [scenario-groups](#scenario-groups) |
| [`couch-joel`](../au-fhir-test-data-set/au-core/Practitioner-couch-joel.json) | [`couch-joel`](../au-fhir-test-data-set/au-core/PractitionerRole-couch-joel.json) | Surgeon (General) (General surgery) | [scenario-groups](#scenario-groups) |
| [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/Practitioner-cruickshank-marlyn.json) | [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/PractitionerRole-cruickshank-marlyn.json) | Podiatrist (Podiatry) | [scenario-groups](#scenario-groups) |
| [`dixon-astrid`](../au-fhir-test-data-set/au-core/Practitioner-dixon-astrid.json) | [`pathologist-dixon-astrid`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-dixon-astrid.json) | Pathologist (Pathology) |  |
| [`ellison-shawn`](../au-fhir-test-data-set/au-core/Practitioner-ellison-shawn.json) | [`paediatrician-ellison-shawn`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-ellison-shawn.json) | Paediatrician (General paediatric specialty) |  |
| [`fleming-skye`](../au-fhir-test-data-set/au-core/Practitioner-fleming-skye.json) | [`fleming-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-skye.json) | Pharmacist (Community pharmacy) | [scenario-groups](#scenario-groups) |
| [`freeman-anya`](../au-fhir-test-data-set/au-core/Practitioner-freeman-anya.json) | [`freeman-anya`](../au-fhir-test-data-set/au-core/PractitionerRole-freeman-anya.json) | Social Worker | [scenario-groups](#scenario-groups) |
| [`harley-reynalda`](../au-fhir-test-data-set/au-core/Practitioner-harley-reynalda.json) | [`harley-reynalda`](../au-fhir-test-data-set/au-core/PractitionerRole-harley-reynalda.json) | Dietitian (Dietetics and nutrition) | [scenario-groups](#scenario-groups) |
| [`henderson-nelson`](../au-fhir-test-data-set/au-core/Practitioner-henderson-nelson.json) | [`dietitian-henderson-nelson`](../au-fhir-test-data-set/au-core/PractitionerRole-dietitian-henderson-nelson.json) | Dietitian (Dietetics and nutrition) |  |
| [`hickson-eldora`](../au-fhir-test-data-set/au-core/Practitioner-hickson-eldora.json) | [`pathologist-hickson-eldora`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hickson-eldora.json) | Pathologist (Pathology) |  |
| [`hoskins-earl`](../au-fhir-test-data-set/au-core/Practitioner-hoskins-earl.json) | [`hoskins-earl`](../au-fhir-test-data-set/au-core/PractitionerRole-hoskins-earl.json) | Dental Practitioner (Dentistry) | [scenario-groups](#scenario-groups) |
| [`huddlestone-velda`](../au-fhir-test-data-set/au-core/Practitioner-huddlestone-velda.json) | [`huddlestone-velda`](../au-fhir-test-data-set/au-core/PractitionerRole-huddlestone-velda.json) | Gastroenterologist (Gastroenterology) | [scenario-groups](#scenario-groups) |
| [`hutton-cortez`](../au-fhir-test-data-set/au-core/Practitioner-hutton-cortez.json) | [`hutton-cortez`](../au-fhir-test-data-set/au-core/PractitionerRole-hutton-cortez.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [scenario-groups](#scenario-groups) |
| [`hyde-cortez`](../au-fhir-test-data-set/au-core/Practitioner-hyde-cortez.json) | [`nuclearmedicine-hyde-cortez`](../au-fhir-test-data-set/au-core/PractitionerRole-nuclearmedicine-hyde-cortez.json) | Nuclear Medicine Technologist |  |
| [`lavender-astrid`](../au-fhir-test-data-set/au-core/Practitioner-lavender-astrid.json) | [`medicaldiagnostic-lavender-astrid`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-lavender-astrid.json) | Medical Diagnostic Radiographer |  |
| [`lawrence-drew`](../au-fhir-test-data-set/au-core/Practitioner-lawrence-drew.json) | [`lawrence-drew`](../au-fhir-test-data-set/au-core/PractitionerRole-lawrence-drew.json) | Speech Pathologist | [scenario-groups](#scenario-groups) |
| [`mackee-sara`](../au-fhir-test-data-set/au-core/Practitioner-mackee-sara.json) | [`cardiothoracicsurgeon-mackee-sara`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiothoracicsurgeon-mackee-sara.json) | Cardiothoracic Surgeon (Cardiothoracic surgery) |  |
| [`manning-opal`](../au-fhir-test-data-set/au-core/Practitioner-manning-opal.json) | [`manning-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-manning-opal.json) | Nurse Practitioner (Nursing) | [scenario-groups](#scenario-groups) |
| [`newling-louis`](../au-fhir-test-data-set/au-core/Practitioner-newling-louis.json) | [`retailpharmacist-newling-louis`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-newling-louis.json) | Retail Pharmacist (Community pharmacy) |  |
| [`rowlands-donya`](../au-fhir-test-data-set/au-core/Practitioner-rowlands-donya.json) | [`rowlands-donya`](../au-fhir-test-data-set/au-core/PractitionerRole-rowlands-donya.json) | Dental Practitioner (Dentistry) | [scenario-groups](#scenario-groups) |
| [`tierney-gisela`](../au-fhir-test-data-set/au-core/Practitioner-tierney-gisela.json) | [`tierney-gisela`](../au-fhir-test-data-set/au-core/PractitionerRole-tierney-gisela.json) | Cardiologist (Cardiology) | [scenario-groups](#scenario-groups) |
| [`vaughan-sol`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-sol.json) | [`vaughan-sol`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-sol.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups) |

**HealthcareService** (3)

- [`pathologylaboratory-wingfield-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-wingfield-pathology.json)
- [`pathologylaboratory-woodcroft-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-woodcroft-pathology.json)
- [`pharmacyretail-edwardstown-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-edwardstown-pharmacy.json)

**Organization** (15)

| ID | Also in |
| --- | --- |
| [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) | *[scenario-groups](#scenario-groups)* |
| [`edwardstown-pharmacy`](../au-fhir-test-data-set/au-core/Organization-edwardstown-pharmacy.json) |  |
| [`royal-park-medical-centre`](../au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json) | *[scenario-groups](#scenario-groups)* |
| [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) | *[scenario-groups](#scenario-groups)* |
| [`wingfield-pathology`](../au-fhir-test-data-set/au-core/Organization-wingfield-pathology.json) |  |
| [`woodcroft-pathology`](../au-fhir-test-data-set/au-core/Organization-woodcroft-pathology.json) |  |
| [`woodville-cardiology`](../au-fhir-test-data-set/au-core/Organization-woodville-cardiology.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-dental`](../au-fhir-test-data-set/au-core/Organization-woodville-dental.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-dietitian-service`](../au-fhir-test-data-set/au-core/Organization-woodville-dietitian-service.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-woodville-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-ot-services`](../au-fhir-test-data-set/au-core/Organization-woodville-ot-services.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-pathology`](../au-fhir-test-data-set/au-core/Organization-woodville-pathology.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-pharmacy`](../au-fhir-test-data-set/au-core/Organization-woodville-pharmacy.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-podiatry`](../au-fhir-test-data-set/au-core/Organization-woodville-podiatry.json) | *[scenario-groups](#scenario-groups)* |
| [`woodville-radiology`](../au-fhir-test-data-set/au-core/Organization-woodville-radiology.json) | *[scenario-groups](#scenario-groups)* |

**Location** (3)

- [`edwardstown-pharmacy`](../au-fhir-test-data-set/au-core/Location-edwardstown-pharmacy.json)
- [`wingfield-pathology`](../au-fhir-test-data-set/au-core/Location-wingfield-pathology.json)
- [`woodcroft-pathology`](../au-fhir-test-data-set/au-core/Location-woodcroft-pathology.json)

<details><summary>26 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`baker-troy`](../au-fhir-test-data-set/au-core/Practitioner-baker-troy.json) | [`baker-troy`](../au-fhir-test-data-set/au-core/PractitionerRole-baker-troy.json) | [`woodville-pathology`](../au-fhir-test-data-set/au-core/Organization-woodville-pathology.json) |  |  |
| [`baynton-lolita`](../au-fhir-test-data-set/au-core/Practitioner-baynton-lolita.json) | [`baynton-lolita`](../au-fhir-test-data-set/au-core/PractitionerRole-baynton-lolita.json) | [`woodville-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-woodville-medical-clinic.json) |  |  |
| [`bell-rudolf`](../au-fhir-test-data-set/au-core/Practitioner-bell-rudolf.json) | [`bell-rudolf`](../au-fhir-test-data-set/au-core/PractitionerRole-bell-rudolf.json) | [`royal-park-medical-centre`](../au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json) |  |  |
| [`berry-lisa`](../au-fhir-test-data-set/au-core/Practitioner-berry-lisa.json) | [`berry-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-berry-lisa.json) | [`woodville-ot-services`](../au-fhir-test-data-set/au-core/Organization-woodville-ot-services.json) |  |  |
| [`carey-joyce`](../au-fhir-test-data-set/au-core/Practitioner-carey-joyce.json) | [`carey-joyce`](../au-fhir-test-data-set/au-core/PractitionerRole-carey-joyce.json) | [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) |  |  |
| [`couch-joel`](../au-fhir-test-data-set/au-core/Practitioner-couch-joel.json) | [`couch-joel`](../au-fhir-test-data-set/au-core/PractitionerRole-couch-joel.json) | [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) |  |  |
| [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/Practitioner-cruickshank-marlyn.json) | [`cruickshank-marlyn`](../au-fhir-test-data-set/au-core/PractitionerRole-cruickshank-marlyn.json) | [`woodville-podiatry`](../au-fhir-test-data-set/au-core/Organization-woodville-podiatry.json) |  |  |
| [`dixon-astrid`](../au-fhir-test-data-set/au-core/Practitioner-dixon-astrid.json) | [`pathologist-dixon-astrid`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-dixon-astrid.json) | [`woodcroft-pathology`](../au-fhir-test-data-set/au-core/Organization-woodcroft-pathology.json) | [`woodcroft-pathology`](../au-fhir-test-data-set/au-core/Location-woodcroft-pathology.json) | [`pathologylaboratory-woodcroft-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-woodcroft-pathology.json) |
| [`ellison-shawn`](../au-fhir-test-data-set/au-core/Practitioner-ellison-shawn.json) | [`paediatrician-ellison-shawn`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-ellison-shawn.json) |  |  |  |
| [`fleming-skye`](../au-fhir-test-data-set/au-core/Practitioner-fleming-skye.json) | [`fleming-skye`](../au-fhir-test-data-set/au-core/PractitionerRole-fleming-skye.json) | [`woodville-pharmacy`](../au-fhir-test-data-set/au-core/Organization-woodville-pharmacy.json) |  |  |
| [`freeman-anya`](../au-fhir-test-data-set/au-core/Practitioner-freeman-anya.json) | [`freeman-anya`](../au-fhir-test-data-set/au-core/PractitionerRole-freeman-anya.json) | [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) |  |  |
| [`harley-reynalda`](../au-fhir-test-data-set/au-core/Practitioner-harley-reynalda.json) | [`harley-reynalda`](../au-fhir-test-data-set/au-core/PractitionerRole-harley-reynalda.json) | [`woodville-dietitian-service`](../au-fhir-test-data-set/au-core/Organization-woodville-dietitian-service.json) |  |  |
| [`henderson-nelson`](../au-fhir-test-data-set/au-core/Practitioner-henderson-nelson.json) | [`dietitian-henderson-nelson`](../au-fhir-test-data-set/au-core/PractitionerRole-dietitian-henderson-nelson.json) |  |  |  |
| [`hickson-eldora`](../au-fhir-test-data-set/au-core/Practitioner-hickson-eldora.json) | [`pathologist-hickson-eldora`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hickson-eldora.json) | [`wingfield-pathology`](../au-fhir-test-data-set/au-core/Organization-wingfield-pathology.json) | [`wingfield-pathology`](../au-fhir-test-data-set/au-core/Location-wingfield-pathology.json) | [`pathologylaboratory-wingfield-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-wingfield-pathology.json) |
| [`hoskins-earl`](../au-fhir-test-data-set/au-core/Practitioner-hoskins-earl.json) | [`hoskins-earl`](../au-fhir-test-data-set/au-core/PractitionerRole-hoskins-earl.json) | [`woodville-dental`](../au-fhir-test-data-set/au-core/Organization-woodville-dental.json) |  |  |
| [`huddlestone-velda`](../au-fhir-test-data-set/au-core/Practitioner-huddlestone-velda.json) | [`huddlestone-velda`](../au-fhir-test-data-set/au-core/PractitionerRole-huddlestone-velda.json) | [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) |  |  |
| [`hutton-cortez`](../au-fhir-test-data-set/au-core/Practitioner-hutton-cortez.json) | [`hutton-cortez`](../au-fhir-test-data-set/au-core/PractitionerRole-hutton-cortez.json) | [`woodville-radiology`](../au-fhir-test-data-set/au-core/Organization-woodville-radiology.json) |  |  |
| [`hyde-cortez`](../au-fhir-test-data-set/au-core/Practitioner-hyde-cortez.json) | [`nuclearmedicine-hyde-cortez`](../au-fhir-test-data-set/au-core/PractitionerRole-nuclearmedicine-hyde-cortez.json) |  |  |  |
| [`lavender-astrid`](../au-fhir-test-data-set/au-core/Practitioner-lavender-astrid.json) | [`medicaldiagnostic-lavender-astrid`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-lavender-astrid.json) |  |  |  |
| [`lawrence-drew`](../au-fhir-test-data-set/au-core/Practitioner-lawrence-drew.json) | [`lawrence-drew`](../au-fhir-test-data-set/au-core/PractitionerRole-lawrence-drew.json) | [`semaphore-aged-care`](../au-fhir-test-data-set/au-core/Organization-semaphore-aged-care.json) |  |  |
| [`mackee-sara`](../au-fhir-test-data-set/au-core/Practitioner-mackee-sara.json) | [`cardiothoracicsurgeon-mackee-sara`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiothoracicsurgeon-mackee-sara.json) |  |  |  |
| [`manning-opal`](../au-fhir-test-data-set/au-core/Practitioner-manning-opal.json) | [`manning-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-manning-opal.json) | [`adelaide-public-hospital`](../au-fhir-test-data-set/au-core/Organization-adelaide-public-hospital.json) |  |  |
| [`newling-louis`](../au-fhir-test-data-set/au-core/Practitioner-newling-louis.json) | [`retailpharmacist-newling-louis`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-newling-louis.json) | [`edwardstown-pharmacy`](../au-fhir-test-data-set/au-core/Organization-edwardstown-pharmacy.json) | [`edwardstown-pharmacy`](../au-fhir-test-data-set/au-core/Location-edwardstown-pharmacy.json) | [`pharmacyretail-edwardstown-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-edwardstown-pharmacy.json) |
| [`rowlands-donya`](../au-fhir-test-data-set/au-core/Practitioner-rowlands-donya.json) | [`rowlands-donya`](../au-fhir-test-data-set/au-core/PractitionerRole-rowlands-donya.json) | [`woodville-dental`](../au-fhir-test-data-set/au-core/Organization-woodville-dental.json) |  |  |
| [`tierney-gisela`](../au-fhir-test-data-set/au-core/Practitioner-tierney-gisela.json) | [`tierney-gisela`](../au-fhir-test-data-set/au-core/PractitionerRole-tierney-gisela.json) | [`woodville-cardiology`](../au-fhir-test-data-set/au-core/Organization-woodville-cardiology.json) |  |  |
| [`vaughan-sol`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-sol.json) | [`vaughan-sol`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-sol.json) | [`royal-park-medical-centre`](../au-fhir-test-data-set/au-core/Organization-royal-park-medical-centre.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 520xx-521xx</strong> (8 entities)</summary>


_Back Valley, Deep Creek, Hayborough._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`heaney-brock`](../au-fhir-test-data-set/au-core/Practitioner-heaney-brock.json) | [`diagnostic-heaney-brock`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-heaney-brock.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`rogers-lorilee`](../au-fhir-test-data-set/au-core/Practitioner-rogers-lorilee.json) | [`obstetrician-rogers-lorilee`](../au-fhir-test-data-set/au-core/PractitionerRole-obstetrician-rogers-lorilee.json) | Obstetrician and Gynaecologist (Obstetrics and gynaecology) |  |

**HealthcareService** (1)

- [`diagnosticimaging-back-valley-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-back-valley-radiology.json)

**Organization** (2)

- [`back-valley-radiology`](../au-fhir-test-data-set/au-core/Organization-back-valley-radiology.json)
- [`hayborough-care-and-support`](../au-fhir-test-data-set/au-core/Organization-hayborough-care-and-support.json) — *also in: [community-contributions](#community-contributions)*

**Location** (1)

- [`back-valley-radiology`](../au-fhir-test-data-set/au-core/Location-back-valley-radiology.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`heaney-brock`](../au-fhir-test-data-set/au-core/Practitioner-heaney-brock.json) | [`diagnostic-heaney-brock`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-heaney-brock.json) | [`back-valley-radiology`](../au-fhir-test-data-set/au-core/Organization-back-valley-radiology.json) | [`back-valley-radiology`](../au-fhir-test-data-set/au-core/Location-back-valley-radiology.json) | [`diagnosticimaging-back-valley-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-back-valley-radiology.json) |
| [`rogers-lorilee`](../au-fhir-test-data-set/au-core/Practitioner-rogers-lorilee.json) | [`obstetrician-rogers-lorilee`](../au-fhir-test-data-set/au-core/PractitionerRole-obstetrician-rogers-lorilee.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 526xx-528xx</strong> (5 entities)</summary>


_Cape Jaffa._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`parr-adelaide`](../au-fhir-test-data-set/au-core/Practitioner-parr-adelaide.json) | [`diagnostic-parr-adelaide`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-parr-adelaide.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |

**HealthcareService** (1)

- [`diagnosticimaging-cape-jaffa-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-cape-jaffa-radiology.json)

**Organization** (1)

- [`cape-jaffa-radiology`](../au-fhir-test-data-set/au-core/Organization-cape-jaffa-radiology.json)

**Location** (1)

- [`cape-jaffa-radiology`](../au-fhir-test-data-set/au-core/Location-cape-jaffa-radiology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`parr-adelaide`](../au-fhir-test-data-set/au-core/Practitioner-parr-adelaide.json) | [`diagnostic-parr-adelaide`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-parr-adelaide.json) | [`cape-jaffa-radiology`](../au-fhir-test-data-set/au-core/Organization-cape-jaffa-radiology.json) | [`cape-jaffa-radiology`](../au-fhir-test-data-set/au-core/Location-cape-jaffa-radiology.json) | [`diagnosticimaging-cape-jaffa-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-cape-jaffa-radiology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 544xx-546xx</strong> (20 entities)</summary>


_Leasingham, Stockyard Creek, Yunta._


**Practitioner / PractitionerRole** (7)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`doyle-hana`](../au-fhir-test-data-set/au-core/Practitioner-doyle-hana.json) | [`nursepractitioner-doyle-hana`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-doyle-hana.json) | Nurse Practitioner (Nursing) |  |
| [`frankel-mary`](../au-fhir-test-data-set/au-core/Practitioner-frankel-mary.json) | [`registerednurses-frankel-mary`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-frankel-mary.json) | Registered Nurses nec (Nursing) |  |
| [`patrick-nancy`](../au-fhir-test-data-set/au-core/Practitioner-patrick-nancy.json) | [`surgeongeneral-patrick-nancy`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-patrick-nancy.json) | Surgeon (General) (General surgery) |  |
| [`pratley-maynard`](../au-fhir-test-data-set/au-core/Practitioner-pratley-maynard.json) | [`surgeongeneral-pratley-maynard`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-pratley-maynard.json) | Surgeon (General) (General surgery) |  |
| [`pye-dusty`](../au-fhir-test-data-set/au-core/Practitioner-pye-dusty.json) | [`plastic-pye-dusty`](../au-fhir-test-data-set/au-core/PractitionerRole-plastic-pye-dusty.json) | Plastic and Reconstructive Surgeon (Plastic surgery - speciality) |  |
| [`rowland-josh`](../au-fhir-test-data-set/au-core/Practitioner-rowland-josh.json) | [`nursepractitioner-rowland-josh`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-rowland-josh.json) | Nurse Practitioner (Nursing) |  |
| [`steele-clyde`](../au-fhir-test-data-set/au-core/Practitioner-steele-clyde.json) | [`registerednurses-steele-clyde`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-steele-clyde.json) | Registered Nurses nec (Nursing) |  |

**HealthcareService** (2)

- [`privateacute-yunta-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-yunta-private-hospital.json)
- [`publicacute-leasingham-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-leasingham-public-hospital.json)

**Organization** (2)

- [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Organization-leasingham-public-hospital.json)
- [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Organization-yunta-private-hospital.json)

**Location** (2)

- [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Location-leasingham-public-hospital.json)
- [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Location-yunta-private-hospital.json)

<details><summary>7 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`doyle-hana`](../au-fhir-test-data-set/au-core/Practitioner-doyle-hana.json) | [`nursepractitioner-doyle-hana`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-doyle-hana.json) | [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Organization-yunta-private-hospital.json) | [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Location-yunta-private-hospital.json) | [`privateacute-yunta-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-yunta-private-hospital.json) |
| [`frankel-mary`](../au-fhir-test-data-set/au-core/Practitioner-frankel-mary.json) | [`registerednurses-frankel-mary`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-frankel-mary.json) | [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Organization-leasingham-public-hospital.json) | [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Location-leasingham-public-hospital.json) | [`publicacute-leasingham-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-leasingham-public-hospital.json) |
| [`patrick-nancy`](../au-fhir-test-data-set/au-core/Practitioner-patrick-nancy.json) | [`surgeongeneral-patrick-nancy`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-patrick-nancy.json) | [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Organization-yunta-private-hospital.json) | [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Location-yunta-private-hospital.json) | [`privateacute-yunta-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-yunta-private-hospital.json) |
| [`pratley-maynard`](../au-fhir-test-data-set/au-core/Practitioner-pratley-maynard.json) | [`surgeongeneral-pratley-maynard`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-pratley-maynard.json) | [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Organization-leasingham-public-hospital.json) | [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Location-leasingham-public-hospital.json) | [`publicacute-leasingham-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-leasingham-public-hospital.json) |
| [`pye-dusty`](../au-fhir-test-data-set/au-core/Practitioner-pye-dusty.json) | [`plastic-pye-dusty`](../au-fhir-test-data-set/au-core/PractitionerRole-plastic-pye-dusty.json) |  |  |  |
| [`rowland-josh`](../au-fhir-test-data-set/au-core/Practitioner-rowland-josh.json) | [`nursepractitioner-rowland-josh`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-rowland-josh.json) | [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Organization-leasingham-public-hospital.json) | [`leasingham-public-hospital`](../au-fhir-test-data-set/au-core/Location-leasingham-public-hospital.json) | [`publicacute-leasingham-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-leasingham-public-hospital.json) |
| [`steele-clyde`](../au-fhir-test-data-set/au-core/Practitioner-steele-clyde.json) | [`registerednurses-steele-clyde`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-steele-clyde.json) | [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Organization-yunta-private-hospital.json) | [`yunta-private-hospital`](../au-fhir-test-data-set/au-core/Location-yunta-private-hospital.json) | [`privateacute-yunta-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-yunta-private-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 560xx-561xx</strong> (4 entities)</summary>


_Karkoo, Mitchellville._


**Patient** (1)

- [`britton-brian-edwin`](../au-fhir-test-data-set/au-core/Patient-britton-brian-edwin.json)

**HealthcareService** (1)

- [`chiropractic-karkoo-chiropractic`](../au-fhir-test-data-set/au-core/HealthcareService-chiropractic-karkoo-chiropractic.json)

**Organization** (1)

- [`karkoo-chiropractic`](../au-fhir-test-data-set/au-core/Organization-karkoo-chiropractic.json)

**Location** (1)

- [`karkoo-chiropractic`](../au-fhir-test-data-set/au-core/Location-karkoo-chiropractic.json)

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 572xx-574xx</strong> (7 entities)</summary>


_Beltana._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`packham-delores`](../au-fhir-test-data-set/au-core/Practitioner-packham-delores.json) | [`generalpractitioner-packham-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-packham-delores.json) | General Practitioner (General medical practice) |  |
| [`pickford-lisa`](../au-fhir-test-data-set/au-core/Practitioner-pickford-lisa.json) | [`registerednurses-pickford-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-pickford-lisa.json) | Registered Nurses nec (Nursing) |  |

**HealthcareService** (1)

- [`generalmedical-beltana-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-beltana-medical-practice.json)

**Organization** (1)

- [`beltana-medical-practice`](../au-fhir-test-data-set/au-core/Organization-beltana-medical-practice.json)

**Location** (1)

- [`beltana-medical-practice`](../au-fhir-test-data-set/au-core/Location-beltana-medical-practice.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`packham-delores`](../au-fhir-test-data-set/au-core/Practitioner-packham-delores.json) | [`generalpractitioner-packham-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-packham-delores.json) | [`beltana-medical-practice`](../au-fhir-test-data-set/au-core/Organization-beltana-medical-practice.json) | [`beltana-medical-practice`](../au-fhir-test-data-set/au-core/Location-beltana-medical-practice.json) | [`generalmedical-beltana-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-beltana-medical-practice.json) |
| [`pickford-lisa`](../au-fhir-test-data-set/au-core/Practitioner-pickford-lisa.json) | [`registerednurses-pickford-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-pickford-lisa.json) | [`beltana-medical-practice`](../au-fhir-test-data-set/au-core/Organization-beltana-medical-practice.json) | [`beltana-medical-practice`](../au-fhir-test-data-set/au-core/Location-beltana-medical-practice.json) | [`generalmedical-beltana-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-beltana-medical-practice.json) |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>TAS</strong> (4 groupings, 56 entities)</summary>

<blockquote>
<details><summary><strong>Hobart metropolitan</strong> (15 entities)</summary>


_Derwent Park, Moonah, Opossum Bay, Rosetta._


**Patient** (2)

- [`cummings-angelo`](../au-fhir-test-data-set/au-core/Patient-cummings-angelo.json)
- [`potts-felix-ernie`](../au-fhir-test-data-set/au-core/Patient-potts-felix-ernie.json)

**Practitioner / PractitionerRole** (5)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`beale-collette`](../au-fhir-test-data-set/au-core/Practitioner-beale-collette.json) | [`diagnostic-beale-collette`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-beale-collette.json) | Nuclear Medicine Specialist (Nuclear medicine - speciality) |  |
| [`burrows-tegan`](../au-fhir-test-data-set/au-core/Practitioner-burrows-tegan.json) | [`surgeongeneral-burrows-tegan`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-burrows-tegan.json) | Surgeon (General) (General surgery) |  |
| [`harvey-brooke`](../au-fhir-test-data-set/au-core/Practitioner-harvey-brooke.json) | [`registerednurses-harvey-brooke`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-harvey-brooke.json) | Registered Nurses nec (Nursing) |  |
| [`mortenson-kerry`](../au-fhir-test-data-set/au-core/Practitioner-mortenson-kerry.json) | [`nursepractitioner-mortenson-kerry`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-mortenson-kerry.json) | Nurse Practitioner (Nursing) |  |
| [`rawlings-hong`](../au-fhir-test-data-set/au-core/Practitioner-rawlings-hong.json) | [`paediatrician-rawlings-hong`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-rawlings-hong.json) | Paediatrician (General paediatric specialty) |  |

**HealthcareService** (1)

- [`publicacute-rosetta-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-rosetta-public-hospital.json)

**Organization** (1)

- [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-rosetta-public-hospital.json)

**Location** (1)

- [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Location-rosetta-public-hospital.json)

<details><summary>5 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`beale-collette`](../au-fhir-test-data-set/au-core/Practitioner-beale-collette.json) | [`diagnostic-beale-collette`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-beale-collette.json) |  |  |  |
| [`burrows-tegan`](../au-fhir-test-data-set/au-core/Practitioner-burrows-tegan.json) | [`surgeongeneral-burrows-tegan`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-burrows-tegan.json) | [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-rosetta-public-hospital.json) | [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Location-rosetta-public-hospital.json) | [`publicacute-rosetta-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-rosetta-public-hospital.json) |
| [`harvey-brooke`](../au-fhir-test-data-set/au-core/Practitioner-harvey-brooke.json) | [`registerednurses-harvey-brooke`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-harvey-brooke.json) | [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-rosetta-public-hospital.json) | [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Location-rosetta-public-hospital.json) | [`publicacute-rosetta-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-rosetta-public-hospital.json) |
| [`mortenson-kerry`](../au-fhir-test-data-set/au-core/Practitioner-mortenson-kerry.json) | [`nursepractitioner-mortenson-kerry`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-mortenson-kerry.json) | [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Organization-rosetta-public-hospital.json) | [`rosetta-public-hospital`](../au-fhir-test-data-set/au-core/Location-rosetta-public-hospital.json) | [`publicacute-rosetta-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-rosetta-public-hospital.json) |
| [`rawlings-hong`](../au-fhir-test-data-set/au-core/Practitioner-rawlings-hong.json) | [`paediatrician-rawlings-hong`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-rawlings-hong.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 710xx-711xx</strong> (14 entities)</summary>


_Garden Island Creek, Southport, Verona Sands._


**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`ellison-malinda`](../au-fhir-test-data-set/au-core/Practitioner-ellison-malinda.json) | [`registerednurses-ellison-malinda`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-ellison-malinda.json) | Registered Nurses nec (Nursing) |  |
| [`emmett-wilhelmina`](../au-fhir-test-data-set/au-core/Practitioner-emmett-wilhelmina.json) | [`pathologist-emmett-wilhelmina`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-emmett-wilhelmina.json) | Pathologist (Pathology) |  |
| [`fletcher-dani`](../au-fhir-test-data-set/au-core/Practitioner-fletcher-dani.json) | [`ambulanceofficer-fletcher-dani`](../au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-fletcher-dani.json) | Ambulance Officer |  |
| [`moran-vincent`](../au-fhir-test-data-set/au-core/Practitioner-moran-vincent.json) | [`generalpractitioner-moran-vincent`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-moran-vincent.json) | General Practitioner (General medical practice) |  |

**HealthcareService** (2)

- [`generalmedical-southport-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-southport-medical-practice.json)
- [`pathologylaboratory-verona-sands-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-verona-sands-pathology.json)

**Organization** (2)

- [`southport-medical-practice`](../au-fhir-test-data-set/au-core/Organization-southport-medical-practice.json)
- [`verona-sands-pathology`](../au-fhir-test-data-set/au-core/Organization-verona-sands-pathology.json)

**Location** (2)

- [`southport-medical-practice`](../au-fhir-test-data-set/au-core/Location-southport-medical-practice.json)
- [`verona-sands-pathology`](../au-fhir-test-data-set/au-core/Location-verona-sands-pathology.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`ellison-malinda`](../au-fhir-test-data-set/au-core/Practitioner-ellison-malinda.json) | [`registerednurses-ellison-malinda`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-ellison-malinda.json) | [`southport-medical-practice`](../au-fhir-test-data-set/au-core/Organization-southport-medical-practice.json) | [`southport-medical-practice`](../au-fhir-test-data-set/au-core/Location-southport-medical-practice.json) | [`generalmedical-southport-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-southport-medical-practice.json) |
| [`emmett-wilhelmina`](../au-fhir-test-data-set/au-core/Practitioner-emmett-wilhelmina.json) | [`pathologist-emmett-wilhelmina`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-emmett-wilhelmina.json) | [`verona-sands-pathology`](../au-fhir-test-data-set/au-core/Organization-verona-sands-pathology.json) | [`verona-sands-pathology`](../au-fhir-test-data-set/au-core/Location-verona-sands-pathology.json) | [`pathologylaboratory-verona-sands-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-verona-sands-pathology.json) |
| [`fletcher-dani`](../au-fhir-test-data-set/au-core/Practitioner-fletcher-dani.json) | [`ambulanceofficer-fletcher-dani`](../au-fhir-test-data-set/au-core/PractitionerRole-ambulanceofficer-fletcher-dani.json) |  |  |  |
| [`moran-vincent`](../au-fhir-test-data-set/au-core/Practitioner-moran-vincent.json) | [`generalpractitioner-moran-vincent`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-moran-vincent.json) | [`southport-medical-practice`](../au-fhir-test-data-set/au-core/Organization-southport-medical-practice.json) | [`southport-medical-practice`](../au-fhir-test-data-set/au-core/Location-southport-medical-practice.json) | [`generalmedical-southport-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-southport-medical-practice.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 716xx-718xx</strong> (5 entities)</summary>


_Lewisham, Saltwater River, Sorell._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`coulter-lani`](../au-fhir-test-data-set/au-core/Practitioner-coulter-lani.json) | [`medicalradiation-coulter-lani`](../au-fhir-test-data-set/au-core/PractitionerRole-medicalradiation-coulter-lani.json) | Medical Radiation Therapist (Radiation oncology) |  |
| [`felmingham-emma`](../au-fhir-test-data-set/au-core/Practitioner-felmingham-emma.json) | [`cardiologist-felmingham-emma`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-felmingham-emma.json) | Cardiologist (Cardiology) |  |

**Organization** (1)

- [`sorell-health-network`](../au-fhir-test-data-set/au-core/Organization-sorell-health-network.json) — *also in: [community-contributions](#community-contributions)*

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`coulter-lani`](../au-fhir-test-data-set/au-core/Practitioner-coulter-lani.json) | [`medicalradiation-coulter-lani`](../au-fhir-test-data-set/au-core/PractitionerRole-medicalradiation-coulter-lani.json) |  |  |
| [`felmingham-emma`](../au-fhir-test-data-set/au-core/Practitioner-felmingham-emma.json) | [`cardiologist-felmingham-emma`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-felmingham-emma.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 725xx-727xx</strong> (22 entities)</summary>


_Blumont, Launceston, Norwood, Robigana, Rushy Lagoon._


**Patient** (1)

- [`robson-adam`](../au-fhir-test-data-set/au-core/Patient-robson-adam.json)

**Practitioner / PractitionerRole** (6)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`goldsmith-melody`](../au-fhir-test-data-set/au-core/Practitioner-goldsmith-melody.json) | [`medicaldiagnostic-goldsmith-melody`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-goldsmith-melody.json) | Medical Diagnostic Radiographer |  |
| [`houston-katrina`](../au-fhir-test-data-set/au-core/Practitioner-houston-katrina.json) | [`diagnostic-houston-katrina`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-houston-katrina.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`jolley-beulah`](../au-fhir-test-data-set/au-core/Practitioner-jolley-beulah.json) | [`retailpharmacist-jolley-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-jolley-beulah.json) | Retail Pharmacist (Community pharmacy) |  |
| [`marchant-ivy`](../au-fhir-test-data-set/au-core/Practitioner-marchant-ivy.json) | [`registerednurses-marchant-ivy`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-marchant-ivy.json) | Registered Nurses nec (Nursing) |  |
| [`mcguire-jesse`](../au-fhir-test-data-set/au-core/Practitioner-mcguire-jesse.json) | [`surgeongeneral-mcguire-jesse`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-mcguire-jesse.json) | Surgeon (General) (General surgery) |  |
| [`patten-annie`](../au-fhir-test-data-set/au-core/Practitioner-patten-annie.json) | [`nursepractitioner-patten-annie`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-patten-annie.json) | Nurse Practitioner (Nursing) |  |

**HealthcareService** (3)

- [`diagnosticimaging-blumont-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-blumont-radiology.json)
- [`pharmacyretail-launceston-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-launceston-pharmacy.json)
- [`privateacute-robigana-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-robigana-private-hospital.json)

**Organization** (3)

- [`blumont-radiology`](../au-fhir-test-data-set/au-core/Organization-blumont-radiology.json)
- [`launceston-pharmacy`](../au-fhir-test-data-set/au-core/Organization-launceston-pharmacy.json)
- [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Organization-robigana-private-hospital.json)

**Location** (3)

- [`blumont-radiology`](../au-fhir-test-data-set/au-core/Location-blumont-radiology.json)
- [`launceston-pharmacy`](../au-fhir-test-data-set/au-core/Location-launceston-pharmacy.json)
- [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Location-robigana-private-hospital.json)

<details><summary>6 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`goldsmith-melody`](../au-fhir-test-data-set/au-core/Practitioner-goldsmith-melody.json) | [`medicaldiagnostic-goldsmith-melody`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-goldsmith-melody.json) |  |  |  |
| [`houston-katrina`](../au-fhir-test-data-set/au-core/Practitioner-houston-katrina.json) | [`diagnostic-houston-katrina`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-houston-katrina.json) | [`blumont-radiology`](../au-fhir-test-data-set/au-core/Organization-blumont-radiology.json) | [`blumont-radiology`](../au-fhir-test-data-set/au-core/Location-blumont-radiology.json) | [`diagnosticimaging-blumont-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-blumont-radiology.json) |
| [`jolley-beulah`](../au-fhir-test-data-set/au-core/Practitioner-jolley-beulah.json) | [`retailpharmacist-jolley-beulah`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-jolley-beulah.json) | [`launceston-pharmacy`](../au-fhir-test-data-set/au-core/Organization-launceston-pharmacy.json) | [`launceston-pharmacy`](../au-fhir-test-data-set/au-core/Location-launceston-pharmacy.json) | [`pharmacyretail-launceston-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-launceston-pharmacy.json) |
| [`marchant-ivy`](../au-fhir-test-data-set/au-core/Practitioner-marchant-ivy.json) | [`registerednurses-marchant-ivy`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-marchant-ivy.json) | [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Organization-robigana-private-hospital.json) | [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Location-robigana-private-hospital.json) | [`privateacute-robigana-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-robigana-private-hospital.json) |
| [`mcguire-jesse`](../au-fhir-test-data-set/au-core/Practitioner-mcguire-jesse.json) | [`surgeongeneral-mcguire-jesse`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-mcguire-jesse.json) | [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Organization-robigana-private-hospital.json) | [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Location-robigana-private-hospital.json) | [`privateacute-robigana-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-robigana-private-hospital.json) |
| [`patten-annie`](../au-fhir-test-data-set/au-core/Practitioner-patten-annie.json) | [`nursepractitioner-patten-annie`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-patten-annie.json) | [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Organization-robigana-private-hospital.json) | [`robigana-private-hospital`](../au-fhir-test-data-set/au-core/Location-robigana-private-hospital.json) | [`privateacute-robigana-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-robigana-private-hospital.json) |

</details>

</details>
</blockquote>

</details>

<details><summary><strong>VIC</strong> (11 groupings, 198 entities)</summary>

<blockquote>
<details><summary><strong>Melbourne metropolitan</strong> (102 entities)</summary>


_Blackburn South, Eltham North, Launching Place, Melbourne, Ringwood East, Southbank, St Kilda, Sunshine, Tarneit._


**Patient** (3)

- [`ewing-ferdinand`](../au-fhir-test-data-set/au-core/Patient-ewing-ferdinand.json)
- [`foreman-caterina`](../au-fhir-test-data-set/au-core/Patient-foreman-caterina.json) — *also in: [scenario-groups](#scenario-groups)*
- [`vaughan-seymour`](../au-fhir-test-data-set/au-core/Patient-vaughan-seymour.json) — *also in: [scenario-groups](#scenario-groups)*

**Practitioner / PractitionerRole** (36)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`alcock-devon`](../au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json) | [`alcock-devon`](../au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`blackwood-ella`](../au-fhir-test-data-set/au-core/Practitioner-blackwood-ella.json) | [`blackwood-ella`](../au-fhir-test-data-set/au-core/PractitionerRole-blackwood-ella.json) | Social Worker | [scenario-groups](#scenario-groups) |
| [`bond-edmundo`](../au-fhir-test-data-set/au-core/Practitioner-bond-edmundo.json) | [`bond-edmundo`](../au-fhir-test-data-set/au-core/PractitionerRole-bond-edmundo.json) | Pharmacist (Community pharmacy) | [scenario-groups](#scenario-groups) |
| [`bowyer-norbert`](../au-fhir-test-data-set/au-core/Practitioner-bowyer-norbert.json) | [`bowyer-norbert`](../au-fhir-test-data-set/au-core/PractitionerRole-bowyer-norbert.json) | Exercise Physiologist | [scenario-groups](#scenario-groups) |
| [`coughlin-tonda`](../au-fhir-test-data-set/au-core/Practitioner-coughlin-tonda.json) | [`retailpharmacist-coughlin-tonda`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-coughlin-tonda.json) | Retail Pharmacist (Community pharmacy) |  |
| [`dempsey-carli`](../au-fhir-test-data-set/au-core/Practitioner-dempsey-carli.json) | [`dempsey-carli`](../au-fhir-test-data-set/au-core/PractitionerRole-dempsey-carli.json) | Clinical Immunologist (Clinical immunology) | [scenario-groups](#scenario-groups) |
| [`egan-anja`](../au-fhir-test-data-set/au-core/Practitioner-egan-anja.json) | [`egan-anja`](../au-fhir-test-data-set/au-core/PractitionerRole-egan-anja.json) | Counsellor (Clinical psychology) | [scenario-groups](#scenario-groups) |
| [`findley-betty`](../au-fhir-test-data-set/au-core/Practitioner-findley-betty.json) | [`findley-betty`](../au-fhir-test-data-set/au-core/PractitionerRole-findley-betty.json) | Sleep Medicine Specialist | [scenario-groups](#scenario-groups) |
| [`frankel-caroline`](../au-fhir-test-data-set/au-core/Practitioner-frankel-caroline.json) | [`frankel-caroline`](../au-fhir-test-data-set/au-core/PractitionerRole-frankel-caroline.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`fuller-kendrick`](../au-fhir-test-data-set/au-core/Practitioner-fuller-kendrick.json) | [`fuller-kendrick`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-kendrick.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) | [scenario-groups](#scenario-groups) |
| [`greene-delores`](../au-fhir-test-data-set/au-core/Practitioner-greene-delores.json) | [`greene-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json) | Paediatrician (General paediatric specialty) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`hallan-maggie`](../au-fhir-test-data-set/au-core/Practitioner-hallan-maggie.json) | [`hallan-maggie`](../au-fhir-test-data-set/au-core/PractitionerRole-hallan-maggie.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [scenario-groups](#scenario-groups) |
| [`hamel-opal`](../au-fhir-test-data-set/au-core/Practitioner-hamel-opal.json) | [`hamel-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-hamel-opal.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups) |
| [`hatcher-merrill`](../au-fhir-test-data-set/au-core/Practitioner-hatcher-merrill.json) | [`hatcher-merrill`](../au-fhir-test-data-set/au-core/PractitionerRole-hatcher-merrill.json) | Nurse Practitioner (Nursing) | [scenario-groups](#scenario-groups) |
| [`higgs-allegra`](../au-fhir-test-data-set/au-core/Practitioner-higgs-allegra.json) | [`higgs-allegra`](../au-fhir-test-data-set/au-core/PractitionerRole-higgs-allegra.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups) |
| [`hilton-della`](../au-fhir-test-data-set/au-core/Practitioner-hilton-della.json) | [`hilton-della`](../au-fhir-test-data-set/au-core/PractitionerRole-hilton-della.json) | Clinical Psychologist (Clinical psychology) | [scenario-groups](#scenario-groups) |
| [`joyce-mae`](../au-fhir-test-data-set/au-core/Practitioner-joyce-mae.json) | [`joyce-mae`](../au-fhir-test-data-set/au-core/PractitionerRole-joyce-mae.json) | Exercise Physiologist | [scenario-groups](#scenario-groups) |
| [`keith-margot`](../au-fhir-test-data-set/au-core/Practitioner-keith-margot.json) | [`keith-margot`](../au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`kelly-arlene`](../au-fhir-test-data-set/au-core/Practitioner-kelly-arlene.json) | [`kelly-arlene`](../au-fhir-test-data-set/au-core/PractitionerRole-kelly-arlene.json) | Ophthalmologist (Ophthalmology) | [scenario-groups](#scenario-groups) |
| [`keyes-chau`](../au-fhir-test-data-set/au-core/Practitioner-keyes-chau.json) | [`keyes-chau`](../au-fhir-test-data-set/au-core/PractitionerRole-keyes-chau.json) | Pathologist (Clinical pathology) | [scenario-groups](#scenario-groups) |
| [`laing-malinda`](../au-fhir-test-data-set/au-core/Practitioner-laing-malinda.json) | [`laing-malinda`](../au-fhir-test-data-set/au-core/PractitionerRole-laing-malinda.json) | Endocrinologist (Endocrinology) | [scenario-groups](#scenario-groups) |
| [`mckane-eugena`](../au-fhir-test-data-set/au-core/Practitioner-mckane-eugena.json) | [`mckane-eugena`](../au-fhir-test-data-set/au-core/PractitionerRole-mckane-eugena.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/Practitioner-mcnaughton-opal.json) | [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnaughton-opal.json) | Diabetes Educator | [scenario-groups](#scenario-groups) |
| [`mullin-kenny`](../au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json) | [`mullin-kenny`](../au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json) | Speech Pathologist | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`mullins-bonita`](../au-fhir-test-data-set/au-core/Practitioner-mullins-bonita.json) | [`mullins-bonita`](../au-fhir-test-data-set/au-core/PractitionerRole-mullins-bonita.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`murray-ashli`](../au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json) | [`murray-ashli`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json) | Occupational Therapist | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |
| [`osland-deanne`](../au-fhir-test-data-set/au-core/Practitioner-osland-deanne.json) | [`osland-deanne`](../au-fhir-test-data-set/au-core/PractitionerRole-osland-deanne.json) | Podiatrist (Podiatry) | [scenario-groups](#scenario-groups) |
| [`patterson-teri`](../au-fhir-test-data-set/au-core/Practitioner-patterson-teri.json) | [`patterson-teri`](../au-fhir-test-data-set/au-core/PractitionerRole-patterson-teri.json) | Dietitian (Dietetics and nutrition) | [scenario-groups](#scenario-groups) |
| [`phillips-gerard`](../au-fhir-test-data-set/au-core/Practitioner-phillips-gerard.json) | [`phillips-gerard`](../au-fhir-test-data-set/au-core/PractitionerRole-phillips-gerard.json) | Endocrinologist (Endocrinology) | [scenario-groups](#scenario-groups) |
| [`quinn-aisha`](../au-fhir-test-data-set/au-core/Practitioner-quinn-aisha.json) | [`dentalpractitioner-quinn-aisha`](../au-fhir-test-data-set/au-core/PractitionerRole-dentalpractitioner-quinn-aisha.json) | Dental Practitioner (Dentistry) |  |
| [`quinn-jeramy`](../au-fhir-test-data-set/au-core/Practitioner-quinn-jeramy.json) | [`quinn-jeramy`](../au-fhir-test-data-set/au-core/PractitionerRole-quinn-jeramy.json) | Optometrist | [scenario-groups](#scenario-groups) |
| [`rodd-illa`](../au-fhir-test-data-set/au-core/Practitioner-rodd-illa.json) | [`rodd-illa`](../au-fhir-test-data-set/au-core/PractitionerRole-rodd-illa.json) | Endocrinologist (Endocrinology) | [scenario-groups](#scenario-groups) |
| [`schaefer-elden`](../au-fhir-test-data-set/au-core/Practitioner-schaefer-elden.json) | [`schaefer-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-schaefer-elden.json) | Cardiologist (Cardiology) | [scenario-groups](#scenario-groups) |
| [`sharp-cherish`](../au-fhir-test-data-set/au-core/Practitioner-sharp-cherish.json) | [`sharp-cherish`](../au-fhir-test-data-set/au-core/PractitionerRole-sharp-cherish.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`shephard-vern`](../au-fhir-test-data-set/au-core/Practitioner-shephard-vern.json) | [`shephard-vern`](../au-fhir-test-data-set/au-core/PractitionerRole-shephard-vern.json) | Psychiatrist (Psychiatry) | [scenario-groups](#scenario-groups) |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | Clinical Psychologist (Clinical psychology) | [scenario-groups](#scenario-groups), [sparked-cdg-journeys](#sparked-cdg-journeys) |

**HealthcareService** (2)

- [`communitypharmacy-launching-place-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-launching-place-pharmacy.json)
- [`opticaldispensing-eltham-north-optical`](../au-fhir-test-data-set/au-core/HealthcareService-opticaldispensing-eltham-north-optical.json)

**Organization** (23)

| ID | Also in |
| --- | --- |
| [`eltham-north-optical`](../au-fhir-test-data-set/au-core/Organization-eltham-north-optical.json) |  |
| [`launching-place-pharmacy`](../au-fhir-test-data-set/au-core/Organization-launching-place-pharmacy.json) |  |
| [`melbourne-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`southbank-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`southbank-speech-pathology`](../au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json) | *[scenario-groups](#scenario-groups)* |
| [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`st-kilda-ot-services`](../au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json) | *[scenario-groups](#scenario-groups)* |
| [`st-kilda-physiology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiology.json) | *[scenario-groups](#scenario-groups)* |
| [`st-kilda-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiotherapy.json) | *[scenario-groups](#scenario-groups)* |
| [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-cardiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-cardiology.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-endocrinology`](../au-fhir-test-data-set/au-core/Organization-sunshine-endocrinology.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-nephrology`](../au-fhir-test-data-set/au-core/Organization-sunshine-nephrology.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-sunshine-ophthalmology.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-optical`](../au-fhir-test-data-set/au-core/Organization-sunshine-optical.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-pathology`](../au-fhir-test-data-set/au-core/Organization-sunshine-pathology.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-pharmacy`](../au-fhir-test-data-set/au-core/Organization-sunshine-pharmacy.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-sunshine-physiotherapy.json) | *[scenario-groups](#scenario-groups)* |
| [`sunshine-radiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-radiology.json) | *[scenario-groups](#scenario-groups)* |
| [`tarneit-health-network`](../au-fhir-test-data-set/au-core/Organization-tarneit-health-network.json) | *[community-contributions](#community-contributions)* |

**Location** (2)

- [`eltham-north-optical`](../au-fhir-test-data-set/au-core/Location-eltham-north-optical.json)
- [`launching-place-pharmacy`](../au-fhir-test-data-set/au-core/Location-launching-place-pharmacy.json)

<details><summary>36 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`alcock-devon`](../au-fhir-test-data-set/au-core/Practitioner-alcock-devon.json) | [`alcock-devon`](../au-fhir-test-data-set/au-core/PractitionerRole-alcock-devon.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |  |
| [`blackwood-ella`](../au-fhir-test-data-set/au-core/Practitioner-blackwood-ella.json) | [`blackwood-ella`](../au-fhir-test-data-set/au-core/PractitionerRole-blackwood-ella.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |  |
| [`bond-edmundo`](../au-fhir-test-data-set/au-core/Practitioner-bond-edmundo.json) | [`bond-edmundo`](../au-fhir-test-data-set/au-core/PractitionerRole-bond-edmundo.json) | [`sunshine-pharmacy`](../au-fhir-test-data-set/au-core/Organization-sunshine-pharmacy.json) |  |  |
| [`bowyer-norbert`](../au-fhir-test-data-set/au-core/Practitioner-bowyer-norbert.json) | [`bowyer-norbert`](../au-fhir-test-data-set/au-core/PractitionerRole-bowyer-norbert.json) | [`sunshine-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-sunshine-physiotherapy.json) |  |  |
| [`coughlin-tonda`](../au-fhir-test-data-set/au-core/Practitioner-coughlin-tonda.json) | [`retailpharmacist-coughlin-tonda`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-coughlin-tonda.json) | [`launching-place-pharmacy`](../au-fhir-test-data-set/au-core/Organization-launching-place-pharmacy.json) | [`launching-place-pharmacy`](../au-fhir-test-data-set/au-core/Location-launching-place-pharmacy.json) | [`communitypharmacy-launching-place-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-communitypharmacy-launching-place-pharmacy.json) |
| [`dempsey-carli`](../au-fhir-test-data-set/au-core/Practitioner-dempsey-carli.json) | [`dempsey-carli`](../au-fhir-test-data-set/au-core/PractitionerRole-dempsey-carli.json) | [`melbourne-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json) |  |  |
| [`egan-anja`](../au-fhir-test-data-set/au-core/Practitioner-egan-anja.json) | [`egan-anja`](../au-fhir-test-data-set/au-core/PractitionerRole-egan-anja.json) | [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) |  |  |
| [`findley-betty`](../au-fhir-test-data-set/au-core/Practitioner-findley-betty.json) | [`findley-betty`](../au-fhir-test-data-set/au-core/PractitionerRole-findley-betty.json) | [`southbank-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json) |  |  |
| [`frankel-caroline`](../au-fhir-test-data-set/au-core/Practitioner-frankel-caroline.json) | [`frankel-caroline`](../au-fhir-test-data-set/au-core/PractitionerRole-frankel-caroline.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |  |
| [`fuller-kendrick`](../au-fhir-test-data-set/au-core/Practitioner-fuller-kendrick.json) | [`fuller-kendrick`](../au-fhir-test-data-set/au-core/PractitionerRole-fuller-kendrick.json) | [`sunshine-nephrology`](../au-fhir-test-data-set/au-core/Organization-sunshine-nephrology.json) |  |  |
| [`greene-delores`](../au-fhir-test-data-set/au-core/Practitioner-greene-delores.json) | [`greene-delores`](../au-fhir-test-data-set/au-core/PractitionerRole-greene-delores.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |  |
| [`hallan-maggie`](../au-fhir-test-data-set/au-core/Practitioner-hallan-maggie.json) | [`hallan-maggie`](../au-fhir-test-data-set/au-core/PractitionerRole-hallan-maggie.json) | [`sunshine-radiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-radiology.json) |  |  |
| [`hamel-opal`](../au-fhir-test-data-set/au-core/Practitioner-hamel-opal.json) | [`hamel-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-hamel-opal.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |  |
| [`hatcher-merrill`](../au-fhir-test-data-set/au-core/Practitioner-hatcher-merrill.json) | [`hatcher-merrill`](../au-fhir-test-data-set/au-core/PractitionerRole-hatcher-merrill.json) | [`southbank-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-medical-clinic.json) |  |  |
| [`higgs-allegra`](../au-fhir-test-data-set/au-core/Practitioner-higgs-allegra.json) | [`higgs-allegra`](../au-fhir-test-data-set/au-core/PractitionerRole-higgs-allegra.json) | [`st-kilda-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiotherapy.json) |  |  |
| [`hilton-della`](../au-fhir-test-data-set/au-core/Practitioner-hilton-della.json) | [`hilton-della`](../au-fhir-test-data-set/au-core/PractitionerRole-hilton-della.json) | [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) |  |  |
| [`joyce-mae`](../au-fhir-test-data-set/au-core/Practitioner-joyce-mae.json) | [`joyce-mae`](../au-fhir-test-data-set/au-core/PractitionerRole-joyce-mae.json) | [`st-kilda-physiology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-physiology.json) |  |  |
| [`keith-margot`](../au-fhir-test-data-set/au-core/Practitioner-keith-margot.json) | [`keith-margot`](../au-fhir-test-data-set/au-core/PractitionerRole-keith-margot.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |  |
| [`kelly-arlene`](../au-fhir-test-data-set/au-core/Practitioner-kelly-arlene.json) | [`kelly-arlene`](../au-fhir-test-data-set/au-core/PractitionerRole-kelly-arlene.json) | [`sunshine-ophthalmology`](../au-fhir-test-data-set/au-core/Organization-sunshine-ophthalmology.json) |  |  |
| [`keyes-chau`](../au-fhir-test-data-set/au-core/Practitioner-keyes-chau.json) | [`keyes-chau`](../au-fhir-test-data-set/au-core/PractitionerRole-keyes-chau.json) | [`sunshine-pathology`](../au-fhir-test-data-set/au-core/Organization-sunshine-pathology.json) |  |  |
| [`laing-malinda`](../au-fhir-test-data-set/au-core/Practitioner-laing-malinda.json) | [`laing-malinda`](../au-fhir-test-data-set/au-core/PractitionerRole-laing-malinda.json) | [`southbank-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-southbank-specialist-clinic.json) |  |  |
| [`mckane-eugena`](../au-fhir-test-data-set/au-core/Practitioner-mckane-eugena.json) | [`mckane-eugena`](../au-fhir-test-data-set/au-core/PractitionerRole-mckane-eugena.json) | [`st-kilda-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-st-kilda-medical-clinic.json) |  |  |
| [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/Practitioner-mcnaughton-opal.json) | [`mcnaughton-opal`](../au-fhir-test-data-set/au-core/PractitionerRole-mcnaughton-opal.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |  |
| [`mullin-kenny`](../au-fhir-test-data-set/au-core/Practitioner-mullin-kenny.json) | [`mullin-kenny`](../au-fhir-test-data-set/au-core/PractitionerRole-mullin-kenny.json) | [`southbank-speech-pathology`](../au-fhir-test-data-set/au-core/Organization-southbank-speech-pathology.json) |  |  |
| [`mullins-bonita`](../au-fhir-test-data-set/au-core/Practitioner-mullins-bonita.json) | [`mullins-bonita`](../au-fhir-test-data-set/au-core/PractitionerRole-mullins-bonita.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |  |
| [`murray-ashli`](../au-fhir-test-data-set/au-core/Practitioner-murray-ashli.json) | [`murray-ashli`](../au-fhir-test-data-set/au-core/PractitionerRole-murray-ashli.json) | [`st-kilda-ot-services`](../au-fhir-test-data-set/au-core/Organization-st-kilda-ot-services.json) |  |  |
| [`osland-deanne`](../au-fhir-test-data-set/au-core/Practitioner-osland-deanne.json) | [`osland-deanne`](../au-fhir-test-data-set/au-core/PractitionerRole-osland-deanne.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |  |
| [`patterson-teri`](../au-fhir-test-data-set/au-core/Practitioner-patterson-teri.json) | [`patterson-teri`](../au-fhir-test-data-set/au-core/PractitionerRole-patterson-teri.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |  |
| [`phillips-gerard`](../au-fhir-test-data-set/au-core/Practitioner-phillips-gerard.json) | [`phillips-gerard`](../au-fhir-test-data-set/au-core/PractitionerRole-phillips-gerard.json) | [`sunshine-endocrinology`](../au-fhir-test-data-set/au-core/Organization-sunshine-endocrinology.json) |  |  |
| [`quinn-aisha`](../au-fhir-test-data-set/au-core/Practitioner-quinn-aisha.json) | [`dentalpractitioner-quinn-aisha`](../au-fhir-test-data-set/au-core/PractitionerRole-dentalpractitioner-quinn-aisha.json) |  |  |  |
| [`quinn-jeramy`](../au-fhir-test-data-set/au-core/Practitioner-quinn-jeramy.json) | [`quinn-jeramy`](../au-fhir-test-data-set/au-core/PractitionerRole-quinn-jeramy.json) | [`sunshine-optical`](../au-fhir-test-data-set/au-core/Organization-sunshine-optical.json) |  |  |
| [`rodd-illa`](../au-fhir-test-data-set/au-core/Practitioner-rodd-illa.json) | [`rodd-illa`](../au-fhir-test-data-set/au-core/PractitionerRole-rodd-illa.json) | [`melbourne-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-melbourne-specialist-clinic.json) |  |  |
| [`schaefer-elden`](../au-fhir-test-data-set/au-core/Practitioner-schaefer-elden.json) | [`schaefer-elden`](../au-fhir-test-data-set/au-core/PractitionerRole-schaefer-elden.json) | [`sunshine-cardiology`](../au-fhir-test-data-set/au-core/Organization-sunshine-cardiology.json) |  |  |
| [`sharp-cherish`](../au-fhir-test-data-set/au-core/Practitioner-sharp-cherish.json) | [`sharp-cherish`](../au-fhir-test-data-set/au-core/PractitionerRole-sharp-cherish.json) | [`sunshine-medical-centre`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-centre.json) |  |  |
| [`shephard-vern`](../au-fhir-test-data-set/au-core/Practitioner-shephard-vern.json) | [`shephard-vern`](../au-fhir-test-data-set/au-core/PractitionerRole-shephard-vern.json) | [`st-kilda-psychology`](../au-fhir-test-data-set/au-core/Organization-st-kilda-psychology.json) |  |  |
| [`vaughan-blaine`](../au-fhir-test-data-set/au-core/Practitioner-vaughan-blaine.json) | [`vaughan-blaine`](../au-fhir-test-data-set/au-core/PractitionerRole-vaughan-blaine.json) | [`sunshine-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-sunshine-medical-clinic.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 325xx-327xx</strong> (3 entities)</summary>


_Cooriemungle._


**HealthcareService** (1)

- [`specialistmedical-cooriemungle-cardiology-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-cooriemungle-cardiology-clinic.json)

**Organization** (1)

- [`cooriemungle-cardiology-clinic`](../au-fhir-test-data-set/au-core/Organization-cooriemungle-cardiology-clinic.json)

**Location** (1)

- [`cooriemungle-cardiology-clinic`](../au-fhir-test-data-set/au-core/Location-cooriemungle-cardiology-clinic.json)

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 330xx-331xx</strong> (11 entities)</summary>


_Langkoop, Wannon._


**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`chambers-greg`](../au-fhir-test-data-set/au-core/Practitioner-chambers-greg.json) | [`registerednurses-chambers-greg`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-chambers-greg.json) | Registered Nurses nec (Nursing) |  |
| [`healy-damian`](../au-fhir-test-data-set/au-core/Practitioner-healy-damian.json) | [`nursepractitioner-healy-damian`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-healy-damian.json) | Nurse Practitioner (Nursing) |  |
| [`lamerton-betsy`](../au-fhir-test-data-set/au-core/Practitioner-lamerton-betsy.json) | [`surgeongeneral-lamerton-betsy`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-lamerton-betsy.json) | Surgeon (General) (General surgery) |  |
| [`spiers-erich`](../au-fhir-test-data-set/au-core/Practitioner-spiers-erich.json) | [`midwife-spiers-erich`](../au-fhir-test-data-set/au-core/PractitionerRole-midwife-spiers-erich.json) | Midwife (Obstetric nursing) |  |

**HealthcareService** (1)

- [`privateacute-wannon-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-wannon-private-hospital.json)

**Organization** (1)

- [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Organization-wannon-private-hospital.json)

**Location** (1)

- [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Location-wannon-private-hospital.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`chambers-greg`](../au-fhir-test-data-set/au-core/Practitioner-chambers-greg.json) | [`registerednurses-chambers-greg`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-chambers-greg.json) | [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Organization-wannon-private-hospital.json) | [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Location-wannon-private-hospital.json) | [`privateacute-wannon-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-wannon-private-hospital.json) |
| [`healy-damian`](../au-fhir-test-data-set/au-core/Practitioner-healy-damian.json) | [`nursepractitioner-healy-damian`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-healy-damian.json) | [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Organization-wannon-private-hospital.json) | [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Location-wannon-private-hospital.json) | [`privateacute-wannon-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-wannon-private-hospital.json) |
| [`lamerton-betsy`](../au-fhir-test-data-set/au-core/Practitioner-lamerton-betsy.json) | [`surgeongeneral-lamerton-betsy`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-lamerton-betsy.json) | [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Organization-wannon-private-hospital.json) | [`wannon-private-hospital`](../au-fhir-test-data-set/au-core/Location-wannon-private-hospital.json) | [`privateacute-wannon-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-wannon-private-hospital.json) |
| [`spiers-erich`](../au-fhir-test-data-set/au-core/Practitioner-spiers-erich.json) | [`midwife-spiers-erich`](../au-fhir-test-data-set/au-core/PractitionerRole-midwife-spiers-erich.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 332xx-334xx</strong> (12 entities)</summary>


_Maddingley, Mount Doran, Rowsley._


**Patient** (1)

- [`inveraity-polly`](../au-fhir-test-data-set/au-core/Patient-inveraity-polly.json)

**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`corbett-clementine`](../au-fhir-test-data-set/au-core/Practitioner-corbett-clementine.json) | [`paediatrician-corbett-clementine`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-corbett-clementine.json) | Paediatrician (General paediatric specialty) |  |
| [`goodwin-aida`](../au-fhir-test-data-set/au-core/Practitioner-goodwin-aida.json) | [`registerednurses-goodwin-aida`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-goodwin-aida.json) | Registered Nurses nec (Nursing) |  |
| [`ross-moses`](../au-fhir-test-data-set/au-core/Practitioner-ross-moses.json) | [`registerednurses-ross-moses`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-ross-moses.json) | Registered Nurses nec (Nursing) |  |
| [`thorpe-mia`](../au-fhir-test-data-set/au-core/Practitioner-thorpe-mia.json) | [`nursepractitioner-thorpe-mia`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-thorpe-mia.json) | Nurse Practitioner (Nursing) |  |

**HealthcareService** (1)

- [`privateprofit-rowsley-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-rowsley-aged-care.json)

**Organization** (1)

- [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Organization-rowsley-aged-care.json)

**Location** (1)

- [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Location-rowsley-aged-care.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`corbett-clementine`](../au-fhir-test-data-set/au-core/Practitioner-corbett-clementine.json) | [`paediatrician-corbett-clementine`](../au-fhir-test-data-set/au-core/PractitionerRole-paediatrician-corbett-clementine.json) |  |  |  |
| [`goodwin-aida`](../au-fhir-test-data-set/au-core/Practitioner-goodwin-aida.json) | [`registerednurses-goodwin-aida`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-goodwin-aida.json) | [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Organization-rowsley-aged-care.json) | [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Location-rowsley-aged-care.json) | [`privateprofit-rowsley-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-rowsley-aged-care.json) |
| [`ross-moses`](../au-fhir-test-data-set/au-core/Practitioner-ross-moses.json) | [`registerednurses-ross-moses`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-ross-moses.json) | [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Organization-rowsley-aged-care.json) | [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Location-rowsley-aged-care.json) | [`privateprofit-rowsley-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-rowsley-aged-care.json) |
| [`thorpe-mia`](../au-fhir-test-data-set/au-core/Practitioner-thorpe-mia.json) | [`nursepractitioner-thorpe-mia`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-thorpe-mia.json) | [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Organization-rowsley-aged-care.json) | [`rowsley-aged-care`](../au-fhir-test-data-set/au-core/Location-rowsley-aged-care.json) | [`privateprofit-rowsley-aged-care`](../au-fhir-test-data-set/au-core/HealthcareService-privateprofit-rowsley-aged-care.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 336xx-338xx</strong> (5 entities)</summary>


_Mount Glasgow._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`hickson-ngoc`](../au-fhir-test-data-set/au-core/Practitioner-hickson-ngoc.json) | [`emergencymedicine-hickson-ngoc`](../au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-hickson-ngoc.json) | Emergency Medicine Specialist (Emergency medicine) |  |

**HealthcareService** (1)

- [`emergencydepartment-mount-glasgow-emergency`](../au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-mount-glasgow-emergency.json)

**Organization** (1)

- [`mount-glasgow-emergency`](../au-fhir-test-data-set/au-core/Organization-mount-glasgow-emergency.json)

**Location** (1)

- [`mount-glasgow-emergency`](../au-fhir-test-data-set/au-core/Location-mount-glasgow-emergency.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`hickson-ngoc`](../au-fhir-test-data-set/au-core/Practitioner-hickson-ngoc.json) | [`emergencymedicine-hickson-ngoc`](../au-fhir-test-data-set/au-core/PractitionerRole-emergencymedicine-hickson-ngoc.json) | [`mount-glasgow-emergency`](../au-fhir-test-data-set/au-core/Organization-mount-glasgow-emergency.json) | [`mount-glasgow-emergency`](../au-fhir-test-data-set/au-core/Location-mount-glasgow-emergency.json) | [`emergencydepartment-mount-glasgow-emergency`](../au-fhir-test-data-set/au-core/HealthcareService-emergencydepartment-mount-glasgow-emergency.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 340xx-341xx</strong> (12 entities)</summary>


_Douglas, Mckenzie Creek._


**Practitioner / PractitionerRole** (3)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`burdett-palmer`](../au-fhir-test-data-set/au-core/Practitioner-burdett-palmer.json) | [`diagnostic-burdett-palmer`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-burdett-palmer.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) | [au-ps-ig-examples](#au-ps-ig-examples) |
| [`mccarthy-kate`](../au-fhir-test-data-set/au-core/Practitioner-mccarthy-kate.json) | [`diagnostic-mccarthy-kate`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mccarthy-kate.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`short-miranda`](../au-fhir-test-data-set/au-core/Practitioner-short-miranda.json) | [`medicaldiagnostic-short-miranda`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-short-miranda.json) | Medical Diagnostic Radiographer |  |

**HealthcareService** (2)

- [`diagnosticimaging-douglas-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-douglas-radiology.json)
- [`diagnosticimaging-mckenzie-creek-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mckenzie-creek-radiology.json)

**Organization** (2)

- [`douglas-radiology`](../au-fhir-test-data-set/au-core/Organization-douglas-radiology.json) — *also in: [au-ps-ig-examples](#au-ps-ig-examples)*
- [`mckenzie-creek-radiology`](../au-fhir-test-data-set/au-core/Organization-mckenzie-creek-radiology.json)

**Location** (2)

- [`douglas-radiology`](../au-fhir-test-data-set/au-core/Location-douglas-radiology.json)
- [`mckenzie-creek-radiology`](../au-fhir-test-data-set/au-core/Location-mckenzie-creek-radiology.json)

<details><summary>3 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`burdett-palmer`](../au-fhir-test-data-set/au-core/Practitioner-burdett-palmer.json) | [`diagnostic-burdett-palmer`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-burdett-palmer.json) | [`douglas-radiology`](../au-fhir-test-data-set/au-core/Organization-douglas-radiology.json) | [`douglas-radiology`](../au-fhir-test-data-set/au-core/Location-douglas-radiology.json) | [`diagnosticimaging-douglas-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-douglas-radiology.json) |
| [`mccarthy-kate`](../au-fhir-test-data-set/au-core/Practitioner-mccarthy-kate.json) | [`diagnostic-mccarthy-kate`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-mccarthy-kate.json) | [`mckenzie-creek-radiology`](../au-fhir-test-data-set/au-core/Organization-mckenzie-creek-radiology.json) | [`mckenzie-creek-radiology`](../au-fhir-test-data-set/au-core/Location-mckenzie-creek-radiology.json) | [`diagnosticimaging-mckenzie-creek-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-mckenzie-creek-radiology.json) |
| [`short-miranda`](../au-fhir-test-data-set/au-core/Practitioner-short-miranda.json) | [`medicaldiagnostic-short-miranda`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-short-miranda.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 345xx-347xx</strong> (15 entities)</summary>


_Joyces Creek, Mitchells Hill, Trentham._


**Practitioner / PractitionerRole** (3)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`gidley-dee`](../au-fhir-test-data-set/au-core/Practitioner-gidley-dee.json) | [`registerednurses-gidley-dee`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-dee.json) | Registered Nurses nec (Nursing) |  |
| [`hart-clifton`](../au-fhir-test-data-set/au-core/Practitioner-hart-clifton.json) | [`pathologist-hart-clifton`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hart-clifton.json) | Pathologist (Pathology) |  |
| [`lumb-mary`](../au-fhir-test-data-set/au-core/Practitioner-lumb-mary.json) | [`generalpractitioner-lumb-mary`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lumb-mary.json) | General Practitioner (General medical practice) |  |

**HealthcareService** (3)

- [`audiologyservice-mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/HealthcareService-audiologyservice-mitchells-hill-audiology.json)
- [`generalpractice-joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json)
- [`pathologylaboratory-trentham-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-trentham-pathology.json)

**Organization** (3)

- [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json)
- [`mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/Organization-mitchells-hill-audiology.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*
- [`trentham-pathology`](../au-fhir-test-data-set/au-core/Organization-trentham-pathology.json)

**Location** (3)

- [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json)
- [`mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/Location-mitchells-hill-audiology.json)
- [`trentham-pathology`](../au-fhir-test-data-set/au-core/Location-trentham-pathology.json)

<details><summary>3 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`gidley-dee`](../au-fhir-test-data-set/au-core/Practitioner-gidley-dee.json) | [`registerednurses-gidley-dee`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-dee.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json) | [`generalpractice-joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json) |
| [`hart-clifton`](../au-fhir-test-data-set/au-core/Practitioner-hart-clifton.json) | [`pathologist-hart-clifton`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hart-clifton.json) | [`trentham-pathology`](../au-fhir-test-data-set/au-core/Organization-trentham-pathology.json) | [`trentham-pathology`](../au-fhir-test-data-set/au-core/Location-trentham-pathology.json) | [`pathologylaboratory-trentham-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-trentham-pathology.json) |
| [`lumb-mary`](../au-fhir-test-data-set/au-core/Practitioner-lumb-mary.json) | [`generalpractitioner-lumb-mary`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lumb-mary.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json) | [`generalpractice-joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 346xx-348xx</strong> (14 entities)</summary>


_Areegra, Joyces Creek, Mitchells Hill, Swanwater West._


**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`baldwin-chi`](../au-fhir-test-data-set/au-core/Practitioner-baldwin-chi.json) | [`diagnostic-baldwin-chi`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-baldwin-chi.json) | Nuclear Medicine Specialist (Nuclear medicine - speciality) |  |
| [`gidley-dee`](../au-fhir-test-data-set/au-core/Practitioner-gidley-dee.json) | [`registerednurses-gidley-dee`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-dee.json) | Registered Nurses nec (Nursing) |  |
| [`lumb-mary`](../au-fhir-test-data-set/au-core/Practitioner-lumb-mary.json) | [`generalpractitioner-lumb-mary`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lumb-mary.json) | General Practitioner (General medical practice) |  |
| [`sheehan-ginger`](../au-fhir-test-data-set/au-core/Practitioner-sheehan-ginger.json) | [`complementaryhealth-sheehan-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-sheehan-ginger.json) | Exercise Physiologist (Exercise physiology service) |  |

**HealthcareService** (2)

- [`audiologyservice-mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/HealthcareService-audiologyservice-mitchells-hill-audiology.json)
- [`generalpractice-joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json)

**Organization** (2)

- [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json)
- [`mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/Organization-mitchells-hill-audiology.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*

**Location** (2)

- [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json)
- [`mitchells-hill-audiology`](../au-fhir-test-data-set/au-core/Location-mitchells-hill-audiology.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`baldwin-chi`](../au-fhir-test-data-set/au-core/Practitioner-baldwin-chi.json) | [`diagnostic-baldwin-chi`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-baldwin-chi.json) |  |  |  |
| [`gidley-dee`](../au-fhir-test-data-set/au-core/Practitioner-gidley-dee.json) | [`registerednurses-gidley-dee`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-gidley-dee.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json) | [`generalpractice-joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json) |
| [`lumb-mary`](../au-fhir-test-data-set/au-core/Practitioner-lumb-mary.json) | [`generalpractitioner-lumb-mary`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-lumb-mary.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-joyces-creek-medical-clinic.json) | [`joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/Location-joyces-creek-medical-clinic.json) | [`generalpractice-joyces-creek-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-joyces-creek-medical-clinic.json) |
| [`sheehan-ginger`](../au-fhir-test-data-set/au-core/Practitioner-sheehan-ginger.json) | [`complementaryhealth-sheehan-ginger`](../au-fhir-test-data-set/au-core/PractitionerRole-complementaryhealth-sheehan-ginger.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 350xx-352xx</strong> (5 entities)</summary>


_Bridgewater On Loddon._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`hollands-beryl`](../au-fhir-test-data-set/au-core/Practitioner-hollands-beryl.json) | [`pathologist-hollands-beryl`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hollands-beryl.json) | Pathologist (Pathology) |  |

**HealthcareService** (1)

- [`pathologylaboratory-bridgewater-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-bridgewater-pathology.json)

**Organization** (1)

- [`bridgewater-pathology`](../au-fhir-test-data-set/au-core/Organization-bridgewater-pathology.json)

**Location** (1)

- [`bridgewater-pathology`](../au-fhir-test-data-set/au-core/Location-bridgewater-pathology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`hollands-beryl`](../au-fhir-test-data-set/au-core/Practitioner-hollands-beryl.json) | [`pathologist-hollands-beryl`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-hollands-beryl.json) | [`bridgewater-pathology`](../au-fhir-test-data-set/au-core/Organization-bridgewater-pathology.json) | [`bridgewater-pathology`](../au-fhir-test-data-set/au-core/Location-bridgewater-pathology.json) | [`pathologylaboratory-bridgewater-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-bridgewater-pathology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 356xx-358xx</strong> (28 entities)</summary>


_Appin South, Milnes Bridge, Murrabit, Piavella, Pine View._


**Patient** (3)

- [`mackay-elliott`](../au-fhir-test-data-set/au-core/Patient-mackay-elliott.json) — *also in: [families](#families)*
- [`mackay-fritz`](../au-fhir-test-data-set/au-core/Patient-mackay-fritz.json) — *also in: [families](#families)*
- [`mackay-heather`](../au-fhir-test-data-set/au-core/Patient-mackay-heather.json) — *also in: [families](#families)*

**Practitioner / PractitionerRole** (7)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`hilton-jaclyn`](../au-fhir-test-data-set/au-core/Practitioner-hilton-jaclyn.json) | [`nursepractitioner-hilton-jaclyn`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-hilton-jaclyn.json) | Nurse Practitioner (Nursing) |  |
| [`howell-natalia`](../au-fhir-test-data-set/au-core/Practitioner-howell-natalia.json) | [`retailpharmacist-howell-natalia`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-howell-natalia.json) | Retail Pharmacist (Community pharmacy) |  |
| [`leech-darnell`](../au-fhir-test-data-set/au-core/Practitioner-leech-darnell.json) | [`registerednurses-leech-darnell`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-leech-darnell.json) | Registered Nurses nec (Nursing) |  |
| [`moss-jaime`](../au-fhir-test-data-set/au-core/Practitioner-moss-jaime.json) | [`generalpractitioner-moss-jaime`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-moss-jaime.json) | General Practitioner (General medical practice) |  |
| [`roche-louis`](../au-fhir-test-data-set/au-core/Practitioner-roche-louis.json) | [`gastroenterologist-roche-louis`](../au-fhir-test-data-set/au-core/PractitionerRole-gastroenterologist-roche-louis.json) | Gastroenterologist (Gastroenterology) |  |
| [`shea-ingrid`](../au-fhir-test-data-set/au-core/Practitioner-shea-ingrid.json) | [`registerednurses-shea-ingrid`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shea-ingrid.json) | Registered Nurses nec (Nursing) |  |
| [`sutherland-sallie`](../au-fhir-test-data-set/au-core/Practitioner-sutherland-sallie.json) | [`cardiologist-sutherland-sallie`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-sutherland-sallie.json) | Cardiologist (Cardiology) | [au-core-ig-examples](#au-core-ig-examples) |

**HealthcareService** (3)

- [`generalmedical-milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-milnes-bridge-medical-centre.json)
- [`pharmacyretail-pine-view-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-pine-view-pharmacy.json)
- [`publicacute-murrabit-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json)

**Organization** (3)

- [`milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/Organization-milnes-bridge-medical-centre.json)
- [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*
- [`pine-view-pharmacy`](../au-fhir-test-data-set/au-core/Organization-pine-view-pharmacy.json)

**Location** (3)

- [`milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/Location-milnes-bridge-medical-centre.json)
- [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json)
- [`pine-view-pharmacy`](../au-fhir-test-data-set/au-core/Location-pine-view-pharmacy.json)

**RelatedPerson** (2)

- [`mackay-heather-2`](../au-fhir-test-data-set/au-core/RelatedPerson-mackay-heather-2.json)
- [`mackay-heather-3`](../au-fhir-test-data-set/au-core/RelatedPerson-mackay-heather-3.json)

<details><summary>7 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`hilton-jaclyn`](../au-fhir-test-data-set/au-core/Practitioner-hilton-jaclyn.json) | [`nursepractitioner-hilton-jaclyn`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-hilton-jaclyn.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json) | [`publicacute-murrabit-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json) |
| [`howell-natalia`](../au-fhir-test-data-set/au-core/Practitioner-howell-natalia.json) | [`retailpharmacist-howell-natalia`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-howell-natalia.json) | [`pine-view-pharmacy`](../au-fhir-test-data-set/au-core/Organization-pine-view-pharmacy.json) | [`pine-view-pharmacy`](../au-fhir-test-data-set/au-core/Location-pine-view-pharmacy.json) | [`pharmacyretail-pine-view-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-pine-view-pharmacy.json) |
| [`leech-darnell`](../au-fhir-test-data-set/au-core/Practitioner-leech-darnell.json) | [`registerednurses-leech-darnell`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-leech-darnell.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json) | [`publicacute-murrabit-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json) |
| [`moss-jaime`](../au-fhir-test-data-set/au-core/Practitioner-moss-jaime.json) | [`generalpractitioner-moss-jaime`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-moss-jaime.json) | [`milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/Organization-milnes-bridge-medical-centre.json) | [`milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/Location-milnes-bridge-medical-centre.json) | [`generalmedical-milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-milnes-bridge-medical-centre.json) |
| [`roche-louis`](../au-fhir-test-data-set/au-core/Practitioner-roche-louis.json) | [`gastroenterologist-roche-louis`](../au-fhir-test-data-set/au-core/PractitionerRole-gastroenterologist-roche-louis.json) |  |  |  |
| [`shea-ingrid`](../au-fhir-test-data-set/au-core/Practitioner-shea-ingrid.json) | [`registerednurses-shea-ingrid`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-shea-ingrid.json) | [`milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/Organization-milnes-bridge-medical-centre.json) | [`milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/Location-milnes-bridge-medical-centre.json) | [`generalmedical-milnes-bridge-medical-centre`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-milnes-bridge-medical-centre.json) |
| [`sutherland-sallie`](../au-fhir-test-data-set/au-core/Practitioner-sutherland-sallie.json) | [`cardiologist-sutherland-sallie`](../au-fhir-test-data-set/au-core/PractitionerRole-cardiologist-sutherland-sallie.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Organization-murrabit-public-hospital.json) | [`murrabit-public-hospital`](../au-fhir-test-data-set/au-core/Location-murrabit-public-hospital.json) | [`publicacute-murrabit-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-murrabit-public-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 366xx-368xx</strong> (1 entity)</summary>


_Benalla._


**Organization** (1)

- [`benalla-care-and-support`](../au-fhir-test-data-set/au-core/Organization-benalla-health-network.json) — *also in: [community-contributions](#community-contributions)*

</details>
</blockquote>

</details>

<details><summary><strong>WA</strong> (11 groupings, 132 entities)</summary>

<blockquote>
<details><summary><strong>Perth metropolitan</strong> (4 entities)</summary>


_Bassendean, Henderson, South Lake._


**Patient** (1)

- [`baratz-toni`](../au-fhir-test-data-set/au-core/Patient-baratz-toni.json) — *also in: [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)*

**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`mcnaughton-chante`](../au-fhir-test-data-set/au-core/Practitioner-mcnaughton-chante.json) | [`clinicalpsychologist-mcnaughton-chante`](../au-fhir-test-data-set/au-core/PractitionerRole-clinicalpsychologist-mcnaughton-chante.json) | Clinical Psychologist (Clinical psychology) |  |

**Organization** (1)

- [`south-lake-care-and-support`](../au-fhir-test-data-set/au-core/Organization-south-lake-care-and-support.json) — *also in: [community-contributions](#community-contributions)*

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`mcnaughton-chante`](../au-fhir-test-data-set/au-core/Practitioner-mcnaughton-chante.json) | [`clinicalpsychologist-mcnaughton-chante`](../au-fhir-test-data-set/au-core/PractitionerRole-clinicalpsychologist-mcnaughton-chante.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 622xx-624xx</strong> (18 entities)</summary>


_Bunbury, Wellington Forest._


**Patient** (4)

| ID | Also in |
| --- | --- |
| [`ballantyne-flavia-indira`](../au-fhir-test-data-set/au-core/Patient-ballantyne-flavia-indira.json) | *[families](#families)* |
| [`ballantyne-kelvin-hans`](../au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json) | *[smart-health-checks](#smart-health-checks)* |
| [`ballantyne-sandy-choy`](../au-fhir-test-data-set/au-core/Patient-ballantyne-sandy-choy.json) | *[families](#families)* |
| [`ballantyne-terry-bob`](../au-fhir-test-data-set/au-core/Patient-ballantyne-terry-bob.json) | *[families](#families)* |

**Practitioner / PractitionerRole** (3)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`dent-aldo`](../au-fhir-test-data-set/au-core/Practitioner-dent-aldo.json) | [`registerednurses-dent-aldo`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-dent-aldo.json) | Registered Nurses nec (Nursing) |  |
| [`osmond-deadra`](../au-fhir-test-data-set/au-core/Practitioner-osmond-deadra.json) | [`nursepractitioner-osmond-deadra`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-osmond-deadra.json) | Nurse Practitioner (Nursing) |  |
| [`potter-lamar`](../au-fhir-test-data-set/au-core/Practitioner-potter-lamar.json) | [`surgeongeneral-potter-lamar`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-potter-lamar.json) | Surgeon (General) (General surgery) |  |

**HealthcareService** (1)

- [`publicacute-bunbury-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-bunbury-public-hospital.json)

**Organization** (1)

- [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Organization-bunbury-public-hospital.json)

**Location** (1)

- [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Location-bunbury-public-hospital.json)

**RelatedPerson** (5)

- [`ballantyne-flavia-2`](../au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-flavia-2.json)
- [`ballantyne-flavia-3`](../au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-flavia-3.json)
- [`ballantyne-flavia-4`](../au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-flavia-4.json)
- [`ballantyne-sandy`](../au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-sandy.json)
- [`ballantyne-terry`](../au-fhir-test-data-set/au-core/RelatedPerson-ballantyne-terry.json)

<details><summary>3 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`dent-aldo`](../au-fhir-test-data-set/au-core/Practitioner-dent-aldo.json) | [`registerednurses-dent-aldo`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-dent-aldo.json) | [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Organization-bunbury-public-hospital.json) | [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Location-bunbury-public-hospital.json) | [`publicacute-bunbury-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-bunbury-public-hospital.json) |
| [`osmond-deadra`](../au-fhir-test-data-set/au-core/Practitioner-osmond-deadra.json) | [`nursepractitioner-osmond-deadra`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-osmond-deadra.json) | [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Organization-bunbury-public-hospital.json) | [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Location-bunbury-public-hospital.json) | [`publicacute-bunbury-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-bunbury-public-hospital.json) |
| [`potter-lamar`](../au-fhir-test-data-set/au-core/Practitioner-potter-lamar.json) | [`surgeongeneral-potter-lamar`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-potter-lamar.json) | [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Organization-bunbury-public-hospital.json) | [`bunbury-public-hospital`](../au-fhir-test-data-set/au-core/Location-bunbury-public-hospital.json) | [`publicacute-bunbury-public-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-publicacute-bunbury-public-hospital.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 624xx-626xx</strong> (14 entities)</summary>


_Balbarrup, Quinninup._


**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`clare-evonne`](../au-fhir-test-data-set/au-core/Practitioner-clare-evonne.json) | [`registerednurses-clare-evonne`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-clare-evonne.json) | Registered Nurses nec (Nursing) |  |
| [`darcy-stella`](../au-fhir-test-data-set/au-core/Practitioner-darcy-stella.json) | [`aboriginal-darcy-stella`](../au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-darcy-stella.json) | Aboriginal and Torres Strait Islander Health Worker |  |
| [`jones-blanch`](../au-fhir-test-data-set/au-core/Practitioner-jones-blanch.json) | [`generalpractitioner-jones-blanch`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-jones-blanch.json) | General Practitioner (General medical practice) |  |
| [`power-linda`](../au-fhir-test-data-set/au-core/Practitioner-power-linda.json) | [`registerednurses-power-linda`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-power-linda.json) | Registered Nurses nec (Nursing) |  |

**HealthcareService** (2)

- [`communityhealth-balbarrup-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-balbarrup-practice.json)
- [`generalpractice-quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-quinninup-medical-clinic.json)

**Organization** (2)

- [`balbarrup-practice`](../au-fhir-test-data-set/au-core/Organization-balbarrup-practice.json)
- [`quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-quinninup-medical-clinic.json)

**Location** (2)

- [`balbarrup-practice`](../au-fhir-test-data-set/au-core/Location-balbarrup-practice.json)
- [`quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/Location-quinninup-medical-clinic.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`clare-evonne`](../au-fhir-test-data-set/au-core/Practitioner-clare-evonne.json) | [`registerednurses-clare-evonne`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-clare-evonne.json) | [`quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-quinninup-medical-clinic.json) | [`quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/Location-quinninup-medical-clinic.json) | [`generalpractice-quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-quinninup-medical-clinic.json) |
| [`darcy-stella`](../au-fhir-test-data-set/au-core/Practitioner-darcy-stella.json) | [`aboriginal-darcy-stella`](../au-fhir-test-data-set/au-core/PractitionerRole-aboriginal-darcy-stella.json) | [`balbarrup-practice`](../au-fhir-test-data-set/au-core/Organization-balbarrup-practice.json) | [`balbarrup-practice`](../au-fhir-test-data-set/au-core/Location-balbarrup-practice.json) | [`communityhealth-balbarrup-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-balbarrup-practice.json) |
| [`jones-blanch`](../au-fhir-test-data-set/au-core/Practitioner-jones-blanch.json) | [`generalpractitioner-jones-blanch`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-jones-blanch.json) | [`quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-quinninup-medical-clinic.json) | [`quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/Location-quinninup-medical-clinic.json) | [`generalpractice-quinninup-medical-clinic`](../au-fhir-test-data-set/au-core/HealthcareService-generalpractice-quinninup-medical-clinic.json) |
| [`power-linda`](../au-fhir-test-data-set/au-core/Practitioner-power-linda.json) | [`registerednurses-power-linda`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-power-linda.json) | [`balbarrup-practice`](../au-fhir-test-data-set/au-core/Organization-balbarrup-practice.json) | [`balbarrup-practice`](../au-fhir-test-data-set/au-core/Location-balbarrup-practice.json) | [`communityhealth-balbarrup-practice`](../au-fhir-test-data-set/au-core/HealthcareService-communityhealth-balbarrup-practice.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 630xx-631xx</strong> (6 entities)</summary>


_Broomehill, Bulyee, Piesseville._


**Patient** (1)

- [`thomson-mika`](../au-fhir-test-data-set/au-core/Patient-thomson-mika.json)

**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`coulter-rosalina`](../au-fhir-test-data-set/au-core/Practitioner-coulter-rosalina.json) | [`optometrist-coulter-rosalina`](../au-fhir-test-data-set/au-core/PractitionerRole-optometrist-coulter-rosalina.json) | Optometrist |  |

**HealthcareService** (1)

- [`specialistmedical-piesseville-gastroenterology`](../au-fhir-test-data-set/au-core/HealthcareService-specialistmedical-piesseville-gastroenterology.json)

**Organization** (1)

- [`piesseville-gastroenterology`](../au-fhir-test-data-set/au-core/Organization-piesseville-gastroenterology.json)

**Location** (1)

- [`piesseville-gastroenterology`](../au-fhir-test-data-set/au-core/Location-piesseville-gastroenterology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`coulter-rosalina`](../au-fhir-test-data-set/au-core/Practitioner-coulter-rosalina.json) | [`optometrist-coulter-rosalina`](../au-fhir-test-data-set/au-core/PractitionerRole-optometrist-coulter-rosalina.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 641xx-643xx</strong> (4 entities)</summary>


_Bruce Rock, Menzies, Moorine Rock._


**Patient** (1)

- [`bassett-imogene-betsy`](../au-fhir-test-data-set/au-core/Patient-bassett-imogene-betsy.json)

**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`oritz-abbie`](../au-fhir-test-data-set/au-core/Practitioner-oritz-abbie.json) | [`medicaldiagnostic-oritz-abbie`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-oritz-abbie.json) | Medical Diagnostic Radiographer |  |

**Organization** (1)

- [`menzies-health-network`](../au-fhir-test-data-set/au-core/Organization-menzies-health-network.json) — *also in: [community-contributions](#community-contributions)*

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`oritz-abbie`](../au-fhir-test-data-set/au-core/Practitioner-oritz-abbie.json) | [`medicaldiagnostic-oritz-abbie`](../au-fhir-test-data-set/au-core/PractitionerRole-medicaldiagnostic-oritz-abbie.json) |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 642xx-644xx</strong> (9 entities)</summary>


_Lake Wells, Menzies, Moorine Rock._


**Patient** (1)

- [`bassett-imogene-betsy`](../au-fhir-test-data-set/au-core/Patient-bassett-imogene-betsy.json)

**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`harding-diana`](../au-fhir-test-data-set/au-core/Practitioner-harding-diana.json) | [`generalpractitioner-harding-diana`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-harding-diana.json) | General Practitioner (General medical practice) |  |
| [`lumb-lovie`](../au-fhir-test-data-set/au-core/Practitioner-lumb-lovie.json) | [`registerednurses-lumb-lovie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-lumb-lovie.json) | Registered Nurses nec (Nursing) |  |

**HealthcareService** (1)

- [`generalmedical-lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-lake-wells-medical-practice.json)

**Organization** (2)

- [`lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/Organization-lake-wells-medical-practice.json)
- [`menzies-health-network`](../au-fhir-test-data-set/au-core/Organization-menzies-health-network.json) — *also in: [community-contributions](#community-contributions)*

**Location** (1)

- [`lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/Location-lake-wells-medical-practice.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`harding-diana`](../au-fhir-test-data-set/au-core/Practitioner-harding-diana.json) | [`generalpractitioner-harding-diana`](../au-fhir-test-data-set/au-core/PractitionerRole-generalpractitioner-harding-diana.json) | [`lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/Organization-lake-wells-medical-practice.json) | [`lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/Location-lake-wells-medical-practice.json) | [`generalmedical-lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-lake-wells-medical-practice.json) |
| [`lumb-lovie`](../au-fhir-test-data-set/au-core/Practitioner-lumb-lovie.json) | [`registerednurses-lumb-lovie`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-lumb-lovie.json) | [`lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/Organization-lake-wells-medical-practice.json) | [`lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/Location-lake-wells-medical-practice.json) | [`generalmedical-lake-wells-medical-practice`](../au-fhir-test-data-set/au-core/HealthcareService-generalmedical-lake-wells-medical-practice.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 661xx-663xx</strong> (7 entities)</summary>


_Bunjil, Koolanooka._


**Practitioner / PractitionerRole** (2)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`gidley-aubrey`](../au-fhir-test-data-set/au-core/Practitioner-gidley-aubrey.json) | [`diagnostic-gidley-aubrey`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-gidley-aubrey.json) | Diagnostic and Interventional Radiologist (Interventional radiology - speciality) |  |
| [`hickman-sally`](../au-fhir-test-data-set/au-core/Practitioner-hickman-sally.json) | [`specialistphysicians-hickman-sally`](../au-fhir-test-data-set/au-core/PractitionerRole-specialistphysicians-hickman-sally.json) | Sleep Medicine Specialist (Sleep medicine service) |  |

**HealthcareService** (1)

- [`diagnosticimaging-koolanooka-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-koolanooka-radiology.json)

**Organization** (1)

- [`koolanooka-radiology`](../au-fhir-test-data-set/au-core/Organization-koolanooka-radiology.json)

**Location** (1)

- [`koolanooka-radiology`](../au-fhir-test-data-set/au-core/Location-koolanooka-radiology.json)

<details><summary>2 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`gidley-aubrey`](../au-fhir-test-data-set/au-core/Practitioner-gidley-aubrey.json) | [`diagnostic-gidley-aubrey`](../au-fhir-test-data-set/au-core/PractitionerRole-diagnostic-gidley-aubrey.json) | [`koolanooka-radiology`](../au-fhir-test-data-set/au-core/Organization-koolanooka-radiology.json) | [`koolanooka-radiology`](../au-fhir-test-data-set/au-core/Location-koolanooka-radiology.json) | [`diagnosticimaging-koolanooka-radiology`](../au-fhir-test-data-set/au-core/HealthcareService-diagnosticimaging-koolanooka-radiology.json) |
| [`hickman-sally`](../au-fhir-test-data-set/au-core/Practitioner-hickman-sally.json) | [`specialistphysicians-hickman-sally`](../au-fhir-test-data-set/au-core/PractitionerRole-specialistphysicians-hickman-sally.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 670xx-671xx</strong> (11 entities)</summary>


_Morgantown, Wooramel._


**Practitioner / PractitionerRole** (4)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`brooksby-caterina`](../au-fhir-test-data-set/au-core/Practitioner-brooksby-caterina.json) | [`surgeongeneral-brooksby-caterina`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-brooksby-caterina.json) | Surgeon (General) (General surgery) |  |
| [`cooke-arthur`](../au-fhir-test-data-set/au-core/Practitioner-cooke-arthur.json) | [`registerednurses-cooke-arthur`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-cooke-arthur.json) | Registered Nurses nec (Nursing) |  |
| [`gaynor-phil`](../au-fhir-test-data-set/au-core/Practitioner-gaynor-phil.json) | [`nursepractitioner-gaynor-phil`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-gaynor-phil.json) | Nurse Practitioner (Nursing) |  |
| [`miller-kittie`](../au-fhir-test-data-set/au-core/Practitioner-miller-kittie.json) | [`gastroenterologist-miller-kittie`](../au-fhir-test-data-set/au-core/PractitionerRole-gastroenterologist-miller-kittie.json) | Gastroenterologist (Gastroenterology) |  |

**HealthcareService** (1)

- [`privateacute-morgantown-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-morgantown-private-hospital.json)

**Organization** (1)

- [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Organization-morgantown-private-hospital.json)

**Location** (1)

- [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Location-morgantown-private-hospital.json)

<details><summary>4 relationships — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`brooksby-caterina`](../au-fhir-test-data-set/au-core/Practitioner-brooksby-caterina.json) | [`surgeongeneral-brooksby-caterina`](../au-fhir-test-data-set/au-core/PractitionerRole-surgeongeneral-brooksby-caterina.json) | [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Organization-morgantown-private-hospital.json) | [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Location-morgantown-private-hospital.json) | [`privateacute-morgantown-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-morgantown-private-hospital.json) |
| [`cooke-arthur`](../au-fhir-test-data-set/au-core/Practitioner-cooke-arthur.json) | [`registerednurses-cooke-arthur`](../au-fhir-test-data-set/au-core/PractitionerRole-registerednurses-cooke-arthur.json) | [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Organization-morgantown-private-hospital.json) | [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Location-morgantown-private-hospital.json) | [`privateacute-morgantown-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-morgantown-private-hospital.json) |
| [`gaynor-phil`](../au-fhir-test-data-set/au-core/Practitioner-gaynor-phil.json) | [`nursepractitioner-gaynor-phil`](../au-fhir-test-data-set/au-core/PractitionerRole-nursepractitioner-gaynor-phil.json) | [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Organization-morgantown-private-hospital.json) | [`morgantown-private-hospital`](../au-fhir-test-data-set/au-core/Location-morgantown-private-hospital.json) | [`privateacute-morgantown-private-hospital`](../au-fhir-test-data-set/au-core/HealthcareService-privateacute-morgantown-private-hospital.json) |
| [`miller-kittie`](../au-fhir-test-data-set/au-core/Practitioner-miller-kittie.json) | [`gastroenterologist-miller-kittie`](../au-fhir-test-data-set/au-core/PractitionerRole-gastroenterologist-miller-kittie.json) |  |  |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 671xx-673xx</strong> (51 entities)</summary>


_Broome._


**Patient** (1)

- [`coombe-ross`](../au-fhir-test-data-set/au-core/Patient-coombe-ross.json) — *also in: [scenario-groups](#scenario-groups)*

**Practitioner / PractitionerRole** (20)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`allardice-della`](../au-fhir-test-data-set/au-core/Practitioner-allardice-della.json) | [`allardice-della`](../au-fhir-test-data-set/au-core/PractitionerRole-allardice-della.json) | Clinical Psychologist (Clinical psychology) | [scenario-groups](#scenario-groups) |
| [`baratz-layla`](../au-fhir-test-data-set/au-core/Practitioner-baratz-layla.json) | [`baratz-layla`](../au-fhir-test-data-set/au-core/PractitionerRole-baratz-layla.json) | Physiotherapist (Physiotherapy) | [scenario-groups](#scenario-groups) |
| [`bassett-elmer`](../au-fhir-test-data-set/au-core/Practitioner-bassett-elmer.json) | [`bassett-elmer`](../au-fhir-test-data-set/au-core/PractitionerRole-bassett-elmer.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`butler-cheryl`](../au-fhir-test-data-set/au-core/Practitioner-butler-cheryl.json) | [`butler-cheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-butler-cheryl.json) | Registered Nurses nec (Nursing) | [scenario-groups](#scenario-groups) |
| [`clapham-laurie`](../au-fhir-test-data-set/au-core/Practitioner-clapham-laurie.json) | [`clapham-laurie`](../au-fhir-test-data-set/au-core/PractitionerRole-clapham-laurie.json) | Exercise Physiologist | [scenario-groups](#scenario-groups) |
| [`davies-keiko`](../au-fhir-test-data-set/au-core/Practitioner-davies-keiko.json) | [`davies-keiko`](../au-fhir-test-data-set/au-core/PractitionerRole-davies-keiko.json) | Dietitian (Dietetics and nutrition) | [scenario-groups](#scenario-groups) |
| [`devine-frank`](../au-fhir-test-data-set/au-core/Practitioner-devine-frank.json) | [`devine-frank`](../au-fhir-test-data-set/au-core/PractitionerRole-devine-frank.json) | Diabetes Educator | [scenario-groups](#scenario-groups) |
| [`gates-anton`](../au-fhir-test-data-set/au-core/Practitioner-gates-anton.json) | [`gates-anton`](../au-fhir-test-data-set/au-core/PractitionerRole-gates-anton.json) | General Practitioner (General medical practice) | [scenario-groups](#scenario-groups) |
| [`giles-veronique`](../au-fhir-test-data-set/au-core/Practitioner-giles-veronique.json) | [`giles-veronique`](../au-fhir-test-data-set/au-core/PractitionerRole-giles-veronique.json) | Optometrist | [scenario-groups](#scenario-groups) |
| [`goldsmith-monique`](../au-fhir-test-data-set/au-core/Practitioner-goldsmith-monique.json) | [`goldsmith-monique`](../au-fhir-test-data-set/au-core/PractitionerRole-goldsmith-monique.json) | Endocrinologist (Endocrinology) | [scenario-groups](#scenario-groups) |
| [`hackett-norman`](../au-fhir-test-data-set/au-core/Practitioner-hackett-norman.json) | [`hackett-norman`](../au-fhir-test-data-set/au-core/PractitionerRole-hackett-norman.json) | Nurse Practitioner (Nursing) | [scenario-groups](#scenario-groups) |
| [`hodges-julia`](../au-fhir-test-data-set/au-core/Practitioner-hodges-julia.json) | [`hodges-julia`](../au-fhir-test-data-set/au-core/PractitionerRole-hodges-julia.json) | Renal Medicine Specialist/Nephrologist/Renal Medicine Physician (Nephrology) | [scenario-groups](#scenario-groups) |
| [`horn-wes`](../au-fhir-test-data-set/au-core/Practitioner-horn-wes.json) | [`horn-wes`](../au-fhir-test-data-set/au-core/PractitionerRole-horn-wes.json) | Podiatrist (Podiatry) | [scenario-groups](#scenario-groups) |
| [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/Practitioner-ibbotson-destiny.json) | [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/PractitionerRole-ibbotson-destiny.json) | Sleep Medicine Specialist | [scenario-groups](#scenario-groups) |
| [`lowry-bennett`](../au-fhir-test-data-set/au-core/Practitioner-lowry-bennett.json) | [`lowry-bennett`](../au-fhir-test-data-set/au-core/PractitionerRole-lowry-bennett.json) | Occupational Therapist | [scenario-groups](#scenario-groups) |
| [`moran-linoel`](../au-fhir-test-data-set/au-core/Practitioner-moran-linoel.json) | [`moran-linoel`](../au-fhir-test-data-set/au-core/PractitionerRole-moran-linoel.json) | Psychiatrist (Psychiatry) | [scenario-groups](#scenario-groups) |
| [`patrick-thalia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-thalia.json) | [`patrick-thalia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-thalia.json) | Counsellor (Clinical psychology) | [scenario-groups](#scenario-groups) |
| [`poulson-lisa`](../au-fhir-test-data-set/au-core/Practitioner-poulson-lisa.json) | [`poulson-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-poulson-lisa.json) | Aboriginal and Torres Strait Islander Health Worker | [scenario-groups](#scenario-groups) |
| [`simmons-ashton`](../au-fhir-test-data-set/au-core/Practitioner-simmons-ashton.json) | [`simmons-ashton`](../au-fhir-test-data-set/au-core/PractitionerRole-simmons-ashton.json) | Cardiologist (Cardiology) | [scenario-groups](#scenario-groups) |
| [`thorburn-juanita`](../au-fhir-test-data-set/au-core/Practitioner-thorburn-juanita.json) | [`thorburn-juanita`](../au-fhir-test-data-set/au-core/PractitionerRole-thorburn-juanita.json) | Social Worker | [scenario-groups](#scenario-groups) |

**Organization** (10)

| ID | Also in |
| --- | --- |
| [`broome-community-health`](../au-fhir-test-data-set/au-core/Organization-broome-community-health.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-nutrition`](../au-fhir-test-data-set/au-core/Organization-broome-nutrition.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-optometry`](../au-fhir-test-data-set/au-core/Organization-broome-optometry.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-ot-services`](../au-fhir-test-data-set/au-core/Organization-broome-ot-services.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-physiology`](../au-fhir-test-data-set/au-core/Organization-broome-physiology.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-broome-physiotherapy.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-podiatry`](../au-fhir-test-data-set/au-core/Organization-broome-podiatry.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) | *[scenario-groups](#scenario-groups)* |
| [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) | *[scenario-groups](#scenario-groups)* |

<details><summary>20 relationships — Practitioner / PractitionerRole / Organization / Location</summary>

| Practitioner | PractitionerRole | Organization | Location |
| --- | --- | --- | --- |
| [`allardice-della`](../au-fhir-test-data-set/au-core/Practitioner-allardice-della.json) | [`allardice-della`](../au-fhir-test-data-set/au-core/PractitionerRole-allardice-della.json) | [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) |  |
| [`baratz-layla`](../au-fhir-test-data-set/au-core/Practitioner-baratz-layla.json) | [`baratz-layla`](../au-fhir-test-data-set/au-core/PractitionerRole-baratz-layla.json) | [`broome-physiotherapy`](../au-fhir-test-data-set/au-core/Organization-broome-physiotherapy.json) |  |
| [`bassett-elmer`](../au-fhir-test-data-set/au-core/Practitioner-bassett-elmer.json) | [`bassett-elmer`](../au-fhir-test-data-set/au-core/PractitionerRole-bassett-elmer.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`butler-cheryl`](../au-fhir-test-data-set/au-core/Practitioner-butler-cheryl.json) | [`butler-cheryl`](../au-fhir-test-data-set/au-core/PractitionerRole-butler-cheryl.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`clapham-laurie`](../au-fhir-test-data-set/au-core/Practitioner-clapham-laurie.json) | [`clapham-laurie`](../au-fhir-test-data-set/au-core/PractitionerRole-clapham-laurie.json) | [`broome-physiology`](../au-fhir-test-data-set/au-core/Organization-broome-physiology.json) |  |
| [`davies-keiko`](../au-fhir-test-data-set/au-core/Practitioner-davies-keiko.json) | [`davies-keiko`](../au-fhir-test-data-set/au-core/PractitionerRole-davies-keiko.json) | [`broome-nutrition`](../au-fhir-test-data-set/au-core/Organization-broome-nutrition.json) |  |
| [`devine-frank`](../au-fhir-test-data-set/au-core/Practitioner-devine-frank.json) | [`devine-frank`](../au-fhir-test-data-set/au-core/PractitionerRole-devine-frank.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`gates-anton`](../au-fhir-test-data-set/au-core/Practitioner-gates-anton.json) | [`gates-anton`](../au-fhir-test-data-set/au-core/PractitionerRole-gates-anton.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`giles-veronique`](../au-fhir-test-data-set/au-core/Practitioner-giles-veronique.json) | [`giles-veronique`](../au-fhir-test-data-set/au-core/PractitionerRole-giles-veronique.json) | [`broome-optometry`](../au-fhir-test-data-set/au-core/Organization-broome-optometry.json) |  |
| [`goldsmith-monique`](../au-fhir-test-data-set/au-core/Practitioner-goldsmith-monique.json) | [`goldsmith-monique`](../au-fhir-test-data-set/au-core/PractitionerRole-goldsmith-monique.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`hackett-norman`](../au-fhir-test-data-set/au-core/Practitioner-hackett-norman.json) | [`hackett-norman`](../au-fhir-test-data-set/au-core/PractitionerRole-hackett-norman.json) | [`broome-medical-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-medical-clinic.json) |  |
| [`hodges-julia`](../au-fhir-test-data-set/au-core/Practitioner-hodges-julia.json) | [`hodges-julia`](../au-fhir-test-data-set/au-core/PractitionerRole-hodges-julia.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`horn-wes`](../au-fhir-test-data-set/au-core/Practitioner-horn-wes.json) | [`horn-wes`](../au-fhir-test-data-set/au-core/PractitionerRole-horn-wes.json) | [`broome-podiatry`](../au-fhir-test-data-set/au-core/Organization-broome-podiatry.json) |  |
| [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/Practitioner-ibbotson-destiny.json) | [`ibbotson-destiny`](../au-fhir-test-data-set/au-core/PractitionerRole-ibbotson-destiny.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`lowry-bennett`](../au-fhir-test-data-set/au-core/Practitioner-lowry-bennett.json) | [`lowry-bennett`](../au-fhir-test-data-set/au-core/PractitionerRole-lowry-bennett.json) | [`broome-ot-services`](../au-fhir-test-data-set/au-core/Organization-broome-ot-services.json) |  |
| [`moran-linoel`](../au-fhir-test-data-set/au-core/Practitioner-moran-linoel.json) | [`moran-linoel`](../au-fhir-test-data-set/au-core/PractitionerRole-moran-linoel.json) | [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) |  |
| [`patrick-thalia`](../au-fhir-test-data-set/au-core/Practitioner-patrick-thalia.json) | [`patrick-thalia`](../au-fhir-test-data-set/au-core/PractitionerRole-patrick-thalia.json) | [`broome-psychology`](../au-fhir-test-data-set/au-core/Organization-broome-psychology.json) |  |
| [`poulson-lisa`](../au-fhir-test-data-set/au-core/Practitioner-poulson-lisa.json) | [`poulson-lisa`](../au-fhir-test-data-set/au-core/PractitionerRole-poulson-lisa.json) | [`broome-community-health`](../au-fhir-test-data-set/au-core/Organization-broome-community-health.json) |  |
| [`simmons-ashton`](../au-fhir-test-data-set/au-core/Practitioner-simmons-ashton.json) | [`simmons-ashton`](../au-fhir-test-data-set/au-core/PractitionerRole-simmons-ashton.json) | [`broome-specialist-clinic`](../au-fhir-test-data-set/au-core/Organization-broome-specialist-clinic.json) |  |
| [`thorburn-juanita`](../au-fhir-test-data-set/au-core/Practitioner-thorburn-juanita.json) | [`thorburn-juanita`](../au-fhir-test-data-set/au-core/PractitionerRole-thorburn-juanita.json) | [`broome-community-health`](../au-fhir-test-data-set/au-core/Organization-broome-community-health.json) |  |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 673xx-675xx</strong> (5 entities)</summary>


_Kununurra._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`khouri-stewart`](../au-fhir-test-data-set/au-core/Practitioner-khouri-stewart.json) | [`pathologist-khouri-stewart`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-khouri-stewart.json) | Pathologist (Pathology) |  |

**HealthcareService** (1)

- [`pathologylaboratory-kununurra-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kununurra-pathology.json)

**Organization** (1)

- [`kununurra-pathology`](../au-fhir-test-data-set/au-core/Organization-kununurra-pathology.json)

**Location** (1)

- [`kununurra-pathology`](../au-fhir-test-data-set/au-core/Location-kununurra-pathology.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`khouri-stewart`](../au-fhir-test-data-set/au-core/Practitioner-khouri-stewart.json) | [`pathologist-khouri-stewart`](../au-fhir-test-data-set/au-core/PractitionerRole-pathologist-khouri-stewart.json) | [`kununurra-pathology`](../au-fhir-test-data-set/au-core/Organization-kununurra-pathology.json) | [`kununurra-pathology`](../au-fhir-test-data-set/au-core/Location-kununurra-pathology.json) | [`pathologylaboratory-kununurra-pathology`](../au-fhir-test-data-set/au-core/HealthcareService-pathologylaboratory-kununurra-pathology.json) |

</details>

</details>
</blockquote>

<blockquote>
<details><summary><strong>Postcodes 676xx-678xx</strong> (5 entities)</summary>


_Mcbeath._


**Practitioner / PractitionerRole** (1)


| Practitioner | PractitionerRole | Role (specialty) | Also in |
| --- | --- | --- | --- |
| [`mclennan-miguel`](../au-fhir-test-data-set/au-core/Practitioner-mclennan-miguel.json) | [`retailpharmacist-mclennan-miguel`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-mclennan-miguel.json) | Retail Pharmacist (Community pharmacy) |  |

**HealthcareService** (1)

- [`pharmacyretail-mcbeath-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-mcbeath-pharmacy.json)

**Organization** (1)

- [`mcbeath-pharmacy`](../au-fhir-test-data-set/au-core/Organization-mcbeath-pharmacy.json)

**Location** (1)

- [`mcbeath-pharmacy`](../au-fhir-test-data-set/au-core/Location-mcbeath-pharmacy.json)

<details><summary>1 relationship — Practitioner / PractitionerRole / Organization / Location / HealthcareService</summary>

| Practitioner | PractitionerRole | Organization | Location | HealthcareService |
| --- | --- | --- | --- | --- |
| [`mclennan-miguel`](../au-fhir-test-data-set/au-core/Practitioner-mclennan-miguel.json) | [`retailpharmacist-mclennan-miguel`](../au-fhir-test-data-set/au-core/PractitionerRole-retailpharmacist-mclennan-miguel.json) | [`mcbeath-pharmacy`](../au-fhir-test-data-set/au-core/Organization-mcbeath-pharmacy.json) | [`mcbeath-pharmacy`](../au-fhir-test-data-set/au-core/Location-mcbeath-pharmacy.json) | [`pharmacyretail-mcbeath-pharmacy`](../au-fhir-test-data-set/au-core/HealthcareService-pharmacyretail-mcbeath-pharmacy.json) |

</details>

</details>
</blockquote>

</details>


## Families <a id="families"></a>

### Purpose

Identifies entities that constitute a family, for constructing consumer journeys involving related patients.

### Ownership & governance

**Owner:** HL7 AU Test Data project  
Grouping identifies plausible family relationships, and does not itself reserve a member to its family. That does not make a member free to build on — some are also IG examples, Inferno default patients or Smart Health Checks entities, which those subsets reserve. What governs an entity is the tightest constraint across all of its memberships, so check its other listings before adding to it.

### Provenance & use

Proposed by a script from two independent signals and confirmed by a human. Where a candidate can be neither confirmed nor rejected because the evidence that would settle it is unavailable, it is recorded as potentially related rather than forced into a binary.

### Relationships

Most members currently have no clinical data, so they are also [Blank-slate patients](#blank-slate-patients).

### How is this subset identified?

Derived from two primary signals, then curated by human confirmation. A shared Medicare card is the strongest: the card number is shared by a family and only the final individual reference number differs. The RelatedPerson network is the second, giving an explicit relationship code. Neither subsumes the other — a newborn not yet on the card is found only by the RelatedPerson network — so both are applied and combined. Matching surname or address is used only to propose further candidates for review.

<details><summary>Derivation notes</summary>

> 7 RelatedPerson-network families (30 entities); 4 additional surname/address candidates.
> 7 confirmed, 2 rejected, 2 flagged as potential families, 0 awaiting a decision.
> A shared Medicare card is treated as a primary signal alongside the RelatedPerson network: the card number is 10 digits plus a per-person Individual Reference Number, so a family on one card shares the first 10 digits. Neither signal dominates — a newborn not yet on the card is found only via RelatedPerson.
> 2 RelatedPerson record(s) excluded as 'unrelated friend' (FRND) and not used to join any family.
> Family members are not required to share an address. Same-surname and same-address candidates are proposals only, never asserted — measured case: 9 Patient files sharing a surname and address are 9 test-data variants of one synthetic patient, not a family.

</details>


### Members (30)

<details><summary><strong>Ballantyne</strong> (4 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (6951826031)._

**Patient** (4)

- [`ballantyne-flavia-indira`](../au-fhir-test-data-set/au-core/Patient-ballantyne-flavia-indira.json)
- [`ballantyne-kelvin-hans`](../au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json) — *also in: [smart-health-checks](#smart-health-checks)*
- [`ballantyne-sandy-choy`](../au-fhir-test-data-set/au-core/Patient-ballantyne-sandy-choy.json)
- [`ballantyne-terry-bob`](../au-fhir-test-data-set/au-core/Patient-ballantyne-terry-bob.json)

</details>

<details><summary><strong>Banks</strong> (7 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954541041)._

**Patient** (5)

| ID | Also in |
| --- | --- |
| [`baby-banks-john`](../au-fhir-test-data-set/au-core/Patient-baby-banks-john.json) | *[au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |
| [`banks-jamila-angie`](../au-fhir-test-data-set/au-core/Patient-banks-jamila-angie.json) |  |
| [`banks-jeramy-ezra`](../au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json) | *[au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`banks-jonas-cary`](../au-fhir-test-data-set/au-core/Patient-banks-jonas-cary.json) |  |
| [`banks-mia-leanne`](../au-fhir-test-data-set/au-core/Patient-banks-mia-leanne.json) | *[au-core-ig-examples](#au-core-ig-examples), [au-ps-ig-examples](#au-ps-ig-examples), [au-ps-test-patients](#au-ps-test-patients), [inferno-default-patients](#inferno-default-patients)* |

**RelatedPerson** (2)

- [`banks-bob`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-bob.json)
- [`banks-mia-leanne-father`](../au-fhir-test-data-set/au-core/RelatedPerson-banks-mia-leanne-father.json) — *also in: [au-core-ig-examples](#au-core-ig-examples)*

</details>

<details><summary><strong>Dietrich</strong> (4 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954541131)._

**Patient** (4)

- [`dietrich-blake-louis`](../au-fhir-test-data-set/au-core/Patient-dietrich-blake-louis.json)
- [`dietrich-diedre-alicia`](../au-fhir-test-data-set/au-core/Patient-dietrich-diedre-alicia.json)
- [`dietrich-kimbra-althea`](../au-fhir-test-data-set/au-core/Patient-dietrich-kimbra-althea.json)
- [`dietrich-phillipa-grace`](../au-fhir-test-data-set/au-core/Patient-dietrich-phillipa-grace.json)

</details>

<details><summary><strong>Hennessy</strong> (3 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954663691)._

**Patient** (3)

- [`hennessy-billy`](../au-fhir-test-data-set/au-core/Patient-hennessy-billy.json) — *also in: [scenario-groups](#scenario-groups)*
- [`hennessy-jenny`](../au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json) — *also in: [scenario-groups](#scenario-groups)*
- [`hennessy-kacey`](../au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json) — *also in: [scenario-groups](#scenario-groups)*

</details>

<details><summary><strong>Lowe</strong> (4 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (2954664391)._

**Patient** (4)

| ID | Also in |
| --- | --- |
| [`lowe-alessandra`](../au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alix`](../au-fhir-test-data-set/au-core/Patient-lowe-alix.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-cedric`](../au-fhir-test-data-set/au-core/Patient-lowe-cedric.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-valerie`](../au-fhir-test-data-set/au-core/Patient-lowe-valerie.json) | *[scenario-groups](#scenario-groups)* |

</details>

<details><summary><strong>Mackay</strong> (3 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (3951334131)._

**Patient** (3)

- [`mackay-elliott`](../au-fhir-test-data-set/au-core/Patient-mackay-elliott.json)
- [`mackay-fritz`](../au-fhir-test-data-set/au-core/Patient-mackay-fritz.json)
- [`mackay-heather`](../au-fhir-test-data-set/au-core/Patient-mackay-heather.json)

</details>

<details><summary><strong>Veitch</strong> (5 entities)</summary>

_Signals: RelatedPerson network, shared Medicare card (4951652281)._

**Patient** (5)

- [`veitch-beau-bradley`](../au-fhir-test-data-set/au-core/Patient-veitch-beau-bradley.json)
- [`veitch-miles-dudley`](../au-fhir-test-data-set/au-core/Patient-veitch-miles-dudley.json)
- [`veitch-mitchell-carl`](../au-fhir-test-data-set/au-core/Patient-veitch-mitchell-carl.json)
- [`veitch-nathan-chris`](../au-fhir-test-data-set/au-core/Patient-veitch-nathan-chris.json)
- [`veitch-savannah-sheena`](../au-fhir-test-data-set/au-core/Patient-veitch-savannah-sheena.json)

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
Carrying no clinical data is not the same as being free to build on: a patient can have no clinical resource here and still be reserved by another subset — several members are [Missing and suppressed data examples](#missing-suppressed-data), deliberately shaped to demonstrate absent data. What governs an entity is the tightest constraint across all of its memberships, so check its other listings before adding to it. Adding clinical data to a member simply removes it from this subset on the next regeneration.

### Provenance & use

Computed from the data set on every regeneration rather than recorded. Membership therefore changes automatically as clinical data is added.

### Relationships

Many members also appear in [Families](#families), and some are [Missing and suppressed data examples](#missing-suppressed-data) instances.

### How is this subset identified?

Derived automatically. A patient is a member when no clinical resource in the data set references it as subject. Administrative links such as RelatedPerson or Coverage do not count, because they record no clinical fact for new content to conflict with.

<details><summary>Derivation notes</summary>

> 79 of 93 patients have no clinical data.
> A patient referenced only by RelatedPerson, Coverage or Appointment counts as a blank slate: those record no clinical fact for new content to conflict with.

</details>


### Members (79)

<details><summary>79 entities — click to expand</summary>

**Patient** (79)

| ID | Also in |
| --- | --- |
| [`archibald-dante`](../au-fhir-test-data-set/au-core/Patient-archibald-dante.json) |  |
| [`baldry-terence-emile`](../au-fhir-test-data-set/au-core/Patient-baldry-terence-emile.json) |  |
| [`baldwin-dinah`](../au-fhir-test-data-set/au-core/Patient-baldwin-dinah.json) |  |
| [`ballantyne-flavia-indira`](../au-fhir-test-data-set/au-core/Patient-ballantyne-flavia-indira.json) | *[families](#families)* |
| [`ballantyne-kelvin-hans`](../au-fhir-test-data-set/au-core/Patient-ballantyne-kelvin-hans.json) | *[smart-health-checks](#smart-health-checks)* |
| [`ballantyne-sandy-choy`](../au-fhir-test-data-set/au-core/Patient-ballantyne-sandy-choy.json) | *[families](#families)* |
| [`ballantyne-terry-bob`](../au-fhir-test-data-set/au-core/Patient-ballantyne-terry-bob.json) | *[families](#families)* |
| [`banks-jamila-angie`](../au-fhir-test-data-set/au-core/Patient-banks-jamila-angie.json) | *[families](#families)* |
| [`banks-jeramy-ezra`](../au-fhir-test-data-set/au-core/Patient-banks-jeramy-ezra.json) | *[au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`banks-jonas-cary`](../au-fhir-test-data-set/au-core/Patient-banks-jonas-cary.json) | *[families](#families)* |
| [`bassett-imogene-betsy`](../au-fhir-test-data-set/au-core/Patient-bassett-imogene-betsy.json) |  |
| [`black-kerry-dougal`](../au-fhir-test-data-set/au-core/Patient-black-kerry-dougal.json) |  |
| [`boulton-annika`](../au-fhir-test-data-set/au-core/Patient-boulton-annika.json) | *[sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`britton-brian-edwin`](../au-fhir-test-data-set/au-core/Patient-britton-brian-edwin.json) |  |
| [`callow-veronica-connie`](../au-fhir-test-data-set/au-core/Patient-callow-veronica-connie.json) |  |
| [`campbell-ambrose`](../au-fhir-test-data-set/au-core/Patient-campbell-ambrose.json) |  |
| [`cane-cheyenne-elaina`](../au-fhir-test-data-set/au-core/Patient-cane-cheyenne-elaina.json) |  |
| [`coombe-ross`](../au-fhir-test-data-set/au-core/Patient-coombe-ross.json) | *[scenario-groups](#scenario-groups)* |
| [`cummings-angelo`](../au-fhir-test-data-set/au-core/Patient-cummings-angelo.json) |  |
| [`davis-juan`](../au-fhir-test-data-set/au-core/Patient-davis-juan.json) |  |
| [`dietrich-blake-louis`](../au-fhir-test-data-set/au-core/Patient-dietrich-blake-louis.json) | *[families](#families)* |
| [`dietrich-diedre-alicia`](../au-fhir-test-data-set/au-core/Patient-dietrich-diedre-alicia.json) | *[families](#families)* |
| [`dietrich-kimbra-althea`](../au-fhir-test-data-set/au-core/Patient-dietrich-kimbra-althea.json) | *[families](#families)* |
| [`dietrich-phillipa-grace`](../au-fhir-test-data-set/au-core/Patient-dietrich-phillipa-grace.json) | *[families](#families)* |
| [`downie-grant`](../au-fhir-test-data-set/au-core/Patient-downie-grant.json) |  |
| [`ewing-ferdinand`](../au-fhir-test-data-set/au-core/Patient-ewing-ferdinand.json) |  |
| [`foreman-caterina`](../au-fhir-test-data-set/au-core/Patient-foreman-caterina.json) | *[scenario-groups](#scenario-groups)* |
| [`frost-rhett-kent`](../au-fhir-test-data-set/au-core/Patient-frost-rhett-kent.json) |  |
| [`hampton-jenice`](../au-fhir-test-data-set/au-core/Patient-hampton-jenice.json) |  |
| [`hennessy-billy`](../au-fhir-test-data-set/au-core/Patient-hennessy-billy.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-jenny`](../au-fhir-test-data-set/au-core/Patient-hennessy-jenny.json) | *[scenario-groups](#scenario-groups)* |
| [`hennessy-kacey`](../au-fhir-test-data-set/au-core/Patient-hennessy-kacey.json) | *[scenario-groups](#scenario-groups)* |
| [`hoskins-marisa`](../au-fhir-test-data-set/au-core/Patient-hoskins-marisa.json) |  |
| [`hoskins-sergio-lionel`](../au-fhir-test-data-set/au-core/Patient-hoskins-sergio-lionel.json) |  |
| [`hulme-brant`](../au-fhir-test-data-set/au-core/Patient-hulme-brant.json) |  |
| [`humphries-jayson`](../au-fhir-test-data-set/au-core/Patient-humphries-jayson.json) |  |
| [`inveraity-polly`](../au-fhir-test-data-set/au-core/Patient-inveraity-polly.json) |  |
| [`italia-sofia-missing-birthDate`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-birthDate.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-missing-gender`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-gender.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-missing-identifier`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-identifier.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-missing-name`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-missing-name.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-suppressed-birthDate`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-birthDate.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-suppressed-gender`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-gender.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-suppressed-identifier`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-identifier.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`italia-sofia-suppressed-name`](../au-fhir-test-data-set/au-core/Patient-italia-sofia-suppressed-name.json) | *[missing-suppressed-data](#missing-suppressed-data)* |
| [`johnson-joyce`](../au-fhir-test-data-set/au-core/Patient-johnson-joyce.json) | *[au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`keaton-jayme`](../au-fhir-test-data-set/au-core/Patient-keaton-jayme.json) |  |
| [`little-rose-gretal`](../au-fhir-test-data-set/au-core/Patient-little-rose-gretal.json) |  |
| [`lowe-alessandra`](../au-fhir-test-data-set/au-core/Patient-lowe-alessandra.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-alix`](../au-fhir-test-data-set/au-core/Patient-lowe-alix.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-cedric`](../au-fhir-test-data-set/au-core/Patient-lowe-cedric.json) | *[scenario-groups](#scenario-groups)* |
| [`lowe-valerie`](../au-fhir-test-data-set/au-core/Patient-lowe-valerie.json) | *[scenario-groups](#scenario-groups)* |
| [`lynch-alyce-shauna`](../au-fhir-test-data-set/au-core/Patient-lynch-alyce-shauna.json) |  |
| [`mackay-elliott`](../au-fhir-test-data-set/au-core/Patient-mackay-elliott.json) | *[families](#families)* |
| [`mackay-heather`](../au-fhir-test-data-set/au-core/Patient-mackay-heather.json) | *[families](#families)* |
| [`martin-shawn`](../au-fhir-test-data-set/au-core/Patient-martin-shawn.json) | *[au-ps-ig-examples](#au-ps-ig-examples)* |
| [`mclennan-karl`](../au-fhir-test-data-set/au-core/Patient-mclennan-karl.json) | *[scenario-groups](#scenario-groups)* |
| [`moffitt-heath-igor`](../au-fhir-test-data-set/au-core/Patient-moffitt-heath-igor.json) |  |
| [`morris-charlotte`](../au-fhir-test-data-set/au-core/Patient-morris-charlotte.json) | *[au-ps-ig-examples](#au-ps-ig-examples), [sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`moylan-brock`](../au-fhir-test-data-set/au-core/Patient-moylan-brock.json) |  |
| [`nash-abel`](../au-fhir-test-data-set/au-core/Patient-nash-abel.json) |  |
| [`nielsen-eleanore`](../au-fhir-test-data-set/au-core/Patient-nielsen-eleanore.json) | *[sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`odonnell-gillian`](../au-fhir-test-data-set/au-core/Patient-odonnell-gillian.json) |  |
| [`pennington-donnie-kip`](../au-fhir-test-data-set/au-core/Patient-pennington-donnie-kip.json) |  |
| [`potts-felix-ernie`](../au-fhir-test-data-set/au-core/Patient-potts-felix-ernie.json) |  |
| [`ralph-rudolf`](../au-fhir-test-data-set/au-core/Patient-ralph-rudolf.json) |  |
| [`reece-karen`](../au-fhir-test-data-set/au-core/Patient-reece-karen.json) | *[scenario-groups](#scenario-groups)* |
| [`ridgewell-troy`](../au-fhir-test-data-set/au-core/Patient-ridgewell-troy.json) |  |
| [`robson-adam`](../au-fhir-test-data-set/au-core/Patient-robson-adam.json) |  |
| [`sandilands-young`](../au-fhir-test-data-set/au-core/Patient-sandilands-young.json) |  |
| [`simpson-tristan`](../au-fhir-test-data-set/au-core/Patient-simpson-tristan.json) | *[sparked-cdg-journeys](#sparked-cdg-journeys)* |
| [`thomson-mika`](../au-fhir-test-data-set/au-core/Patient-thomson-mika.json) |  |
| [`todd-tanya-estelle`](../au-fhir-test-data-set/au-core/Patient-todd-tanya-estelle.json) |  |
| [`vaughan-seymour`](../au-fhir-test-data-set/au-core/Patient-vaughan-seymour.json) | *[scenario-groups](#scenario-groups)* |
| [`veitch-beau-bradley`](../au-fhir-test-data-set/au-core/Patient-veitch-beau-bradley.json) | *[families](#families)* |
| [`veitch-miles-dudley`](../au-fhir-test-data-set/au-core/Patient-veitch-miles-dudley.json) | *[families](#families)* |
| [`veitch-mitchell-carl`](../au-fhir-test-data-set/au-core/Patient-veitch-mitchell-carl.json) | *[families](#families)* |
| [`veitch-nathan-chris`](../au-fhir-test-data-set/au-core/Patient-veitch-nathan-chris.json) | *[families](#families)* |
| [`veitch-savannah-sheena`](../au-fhir-test-data-set/au-core/Patient-veitch-savannah-sheena.json) | *[families](#families)* |

</details>

