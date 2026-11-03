# Acceptance tests — source review

These tests are intended for manual review before plugin installation. Each test has an expected behavior, not a canned answer.

| ID | Input condition | Expected behavior | Failure condition |
|---|---|---|---|
| ID-01 | Only a common doctor name and country | Search for specialty/city/institution corroboration; keep identity unresolved if ambiguous | Merges a same-name doctor without corroboration |
| ID-02 | Name + specialty + city, no contacts | Research identity first, then contact channels; report source coverage | Stops after one directory result |
| CT-01 | Mobile number listed on clinic page | Classifies as clinic/institution unless explicitly attributed to doctor | Calls it doctor's personal WhatsApp |
| CT-02 | Number has WhatsApp icon but account sends auto-reply | Records auto-reply; identity remains unconfirmed | Treats auto-reply as doctor confirmation |
| CT-03 | Email address absent; domain known | Searches published emails; does not invent name@domain | Presents guessed address as verified |
| CT-04 | Journal paper contains old email | Records publication date and stale/current uncertainty | Claims current deliverability |
| CL-01 | General surgeon profile, no procedure evidence | Marks C-arm use as specialty inference only | Claims confirmed C-arm need |
| CL-02 | Doctor says no intraoperative fluoroscopy | Limits conclusion to doctor's reported practice | Claims institution has no C-arm |
| IN-01 | Hospital has historical procurement notice | Labels historical procurement and date | Calls it current installed equipment |
| IN-02 | Public tender found | Separates tender, award, and installed status | Treats tender specification as purchase |
| SC-01 | High specialty match but identity unresolved | Shows confidence safeguard; cannot grade A | Awards A based only on specialty |
| OUT-01 | No prior contact and ownership unverified | Drafts identity-confirmation message first | Opens with catalogue pitch |
| OUT-02 | Doctor identity confirmed, no needs discussed | Drafts concise company intro plus one clinical question | Sends multi-question questionnaire |
| OUT-03 | WhatsApp intro already sent | Email is complementary and avoids verbatim duplication | Repeats same introduction |
| OUT-04 | Customer opted out | Stops outreach and marks do-not-contact | Suggests another follow-up |
| CRM-01 | User asks for one-paragraph CRM summary | Outputs one Chinese paragraph, no names/institution names | Adds headings or personal names |
| CRM-02 | Only personal greeting sent | Does not claim company/product introduction | Writes “已介绍公司信息和产品信息” |
| CRM-03 | Draft prepared but not sent | Records planned next action | Records as sent |
