---
name: medical-lead-development
description: "Use when researching, qualifying, prioritizing, or initiating outreach to overseas physicians, hospitals, clinics, distributors, or other medical-device prospects for medical equipment sales. Supports incomplete lead data, exhaustive public-source contact research, identity verification, clinical and institutional analysis, product fit, lead scoring, and staged WhatsApp/email outreach."
---

# Medical Lead Development

## 1. Purpose and operating profile

Run a rigorous, evidence-led overseas medical-device prospecting workflow. The default business context is medical equipment export sales, with Perlove Medical product families as the initial matching catalogue:

- Mobile DR / mobile digital radiography
- Fixed DR
- Suspended / ceiling-mounted DR
- Dynamic DR / DRF
- Mobile C-arm, including high-frequency and interventional configurations
- 3D C-arm
- CBCT

Treat the product list as a starting catalogue, not proof that a specific model is currently available, certified, or suitable in a target country. Confirm model specifications, regulatory status, voltage/frequency, detector, tube, accessories, warranty, installation, and local registration against current manufacturer documents before making technical or commercial claims.

The user selected these operating defaults:
- Scope: medical-device overseas sales.
- Research depth: exhaustive public-source research.
- Execution: staged review. Complete a stage, show findings and sources, then wait for user approval before moving to the next material stage.
- Never contact a prospect, send an email, submit a form, create a CRM record, or make a purchase commitment without explicit user authorization and a tool that supports that action.

## 2. Core principles

1. **Contact discovery before secondary analysis.** Treat the supplied lead as a search seed. Do not spend a separate preliminary stage re-validating, auditing, or proving the original row/source; immediately search for the prospect's best available professional contact details.
2. **Evidence before inference.** Separate sourced contact facts, reasonable hypotheses, and unanswered questions. Validate newly discovered contact ownership only to the extent needed to avoid misdirected outreach.
3. **Identity before promotion.** When the person and channel are not already verified, the first message should politely confirm the intended doctor/contact, not launch into a product pitch.
4. **Exhaustive means broad and systematic, not intrusive.** Search relevant public sources in local languages and English. Do not bypass logins, paywalls, CAPTCHAs, access controls, robots restrictions, or platform terms; do not obtain leaked, private, or non-public personal data.
5. **No invented contact details.** Never generate likely email addresses or phone numbers and present them as real. Guessed patterns may be listed only in a separate “unverified hypothesis” section if the user explicitly asks, never as usable contacts.
6. **Contact source, ownership, and reachability are separate.** A number published on a clinic page is not automatically the doctor's personal WhatsApp. A public email is not necessarily monitored. A WhatsApp icon or mobile format alone does not prove WhatsApp registration or personal use.
7. **Preserve source provenance.** Give a direct source URL, source type, relevant evidence, access date, and confidence for every material identity/contact/business claim.
8. **Respect privacy and outreach rules.** Use professional contact details intentionally published for professional contact. Avoid sensitive personal data, family details, home addresses, personal accounts unrelated to professional work, and patient information. Follow applicable privacy, anti-spam, telemarketing, and professional-contact laws in both sender and recipient jurisdictions. Stop after an explicit refusal or opt-out.
9. **Do not overstate product need.** A specialty keyword is not evidence of a procedure, equipment ownership, purchasing authority, or purchase intent.
10. **Do not repeat outreach.** Review current conversation and supplied communication history before drafting. Distinguish already sent, proposed, and received messages.
11. **No unsupported certainty.** If a source is inaccessible, contradictory, stale, or incomplete, say so.

## 3. Inputs and intake

Accept one lead or a batch. Inputs may contain any combination of:
- Name, name variants, local spelling, professional title
- Country, state/province, city, language
- Specialty, subspecialty, procedures, institution, department
- Phone, WhatsApp number, landline, email, website, social profile
- Directory row, spreadsheet row, CRM export, conference list, paper, screenshot, or user notes
- Existing conversation history and previous outreach status

Do not require all fields. Parse the supplied material, preserve original spelling and name order, normalize values in separate fields, and retain the original raw value for traceability. Do not silently “correct” a name.

### Intake output
Start with:
- Lead ID or temporary sequence number
- Original input (briefly)
- Parsed known fields
- Missing fields
- Initial ambiguity / duplicate risks
- Existing communication status, if supplied

For batch input, create an independent dossier for each prospect. Deduplicate only when there is sufficient evidence that records refer to the same person or organization. Never merge on name alone.

## 4. Staged execution and approval gates

Default stages:

### Stage 1 — Normalize and identify
Normalize input and research the person's professional identity and current practice. Present identity findings and confidence. Ask for approval to continue if identity remains ambiguous or if a major mismatch appears.

### Stage 2 — Exhaustive contact research
Search all relevant public channels for direct professional phone/WhatsApp, email, institution channels, and professional social profiles. Present a ranked contact register with provenance and confidence. Do not message anyone yet.

### Stage 3 — Clinical and institution research
Research actual services, procedures, facility structure, ownership/type, equipment, purchasing history, procurement plans, and decision chain. Clearly distinguish person-level facts from institution-level facts.

### Stage 4 — Product fit and commercial qualification
Map evidence to product families, identify use cases, gaps, competitive context, decision role, timing signals, and commercial route. Score the lead with evidence and confidence.

### Stage 5 — Outreach preparation
Prepare first-touch WhatsApp and email drafts appropriate to the verified channel. For a new relationship, start with identity confirmation; prepare later-stage copy separately and label it “send only after confirmation”. Include Chinese translation for Spanish/English drafts unless user says otherwise.

### Stage 6 — Follow-up and CRM handoff
After user supplies actual replies or confirms messages sent, update status, propose the next single best action, and optionally hand off to `client-progress-summary` for a CRM paragraph.

Do not skip a stage because the input appears complete. Instead, verify whether the supplied facts have reliable provenance. The user can explicitly ask to skip a stage.

## 5. Identity verification

### 5.1 Search dimensions
Search exact name and variants with combinations of:
- Country, state/province, city
- Specialty and subspecialty
- Hospital, clinic, practice, department
- Professional title and local language equivalents
- Medical registration, professional association, directory
- Paper, conference, speaker, author, interview, news

For Spanish-speaking markets, preserve both surnames and test common ordering/diacritic variants without assuming that different spellings are the same person. For other languages, use transliteration variants cautiously.

### 5.2 Preferred public sources
Prioritize primary or authoritative sources:
1. Government professional registration and health-provider registries.
2. Official hospital, clinic, university, and medical-group pages.
3. Professional colleges, medical associations, specialty societies.
4. Official appointment/booking portals and verified clinic profiles.
5. Academic publications, PubMed, ORCID, Google Scholar, university repositories.
6. Conference programs, speaker bios, professional event pages.
7. Official company registry records where relevant to a practice or clinic.
8. Reputable news, interviews, public talks, and professional social profiles.
9. General directories and aggregators as discovery leads only; corroborate them.

Source priority may vary by country. Record the jurisdiction and the date/cutoff of registry data where available.

### 5.3 Identity evidence
Compare:
- Full name and name order
- Specialty/subspecialty
- City and region
- Current versus historical institution
- Professional registration number only when publicly published and relevant; do not expose unnecessary identifiers in final summaries
- Academic affiliation, biography, practice name, and other cross-links

### 5.4 Confidence labels
- **Confirmed:** at least two independent reliable sources align, or one authoritative current primary source plus a second corroborating identifier.
- **High confidence:** multiple matching details, but current practice or direct identity link is not fully confirmed.
- **Tentative:** one source or limited matching attributes.
- **Conflicting:** credible sources disagree on identity, specialty, location, or current institution.
- **Unresolved:** insufficient evidence to distinguish the person.

Never use “confirmed” solely because a name appears in a directory. Do not treat an old affiliation as current.

## 6. Contact research

### 6.1 Contact categories
Keep these separate:
- Doctor's direct professional mobile
- Doctor's direct WhatsApp (ownership confirmed or not)
- Doctor's professional email
- Institution / clinic WhatsApp
- Institution / clinic telephone
- Department / appointment desk
- General contact email
- Professional social profile / contact form
- Distributor or third-party contact

### 6.2 Search coverage
Search, where relevant and publicly accessible:
- Official doctor profile and clinic/hospital profile
- Online appointment and booking platforms
- Clinic pages, contact pages, location pages, and official social profiles
- Government provider registries and professional association directories
- Papers, abstracts, journal author pages, university profiles, and research repositories
- Conference programs, speaker bios, event announcements
- Public interviews, news articles, professional videos and webinars
- Practice/business websites and public business registry records
- Partner institutions and professional affiliations
- Public professional listings and reputable directories

Use the local language and common contact terms, for example:
- Spanish: WhatsApp, celular, móvil, teléfono, contacto, citas, agenda, correo, email, consultorio
- Portuguese: WhatsApp, celular, telefone, contato, agendamento, e-mail
- English: mobile, phone, contact, appointments, email, office
- French: téléphone, portable, contact, rendez-vous, courriel

Use multiple search combinations. When a newly found clinic, domain, institution, or professional association reveals a new credible path, follow it. Do not claim the search is exhaustive merely because a fixed number of queries was run.

### 6.3 Phone and WhatsApp verification
For every number record:
- Exact displayed form
- Normalized international form, only when country code is clear
- Country/area code
- Published source and URL
- Whether source identifies doctor, clinic, department, or unknown owner
- Whether the number appears in multiple independent sources
- Whether WhatsApp use is explicitly indicated by the source
- Actual reachability status, if the user or an authorized tool has tested it

Ownership labels:
- **Doctor direct — confirmed**
- **Doctor direct — likely**
- **Clinic / institution**
- **Department / appointment desk**
- **Third party**
- **Owner unknown**
- **Conflicting / stale**

Reachability labels:
- Not tested
- Message delivered (only if directly observed)
- Auto-reply received
- Human reply received
- Wrong number / unreachable
- Opted out / do not contact

Never infer that a number is a personal WhatsApp because it has a mobile prefix, appears on a doctor's listing, or has a WhatsApp button on a generic directory. An auto-reply is not a human identity confirmation.

### 6.4 Email verification
For every email record:
- Exact published address
- Source URL and source owner
- Address type: named individual, institutional, department, generic, booking, or unknown
- Domain and its relationship to the institution/practice
- Evidence linking the mailbox to the intended doctor
- Currentness / last-seen date where visible
- Verification status

Do not create or send test emails to verify an address unless the user explicitly authorizes it and a suitable tool exists. Do not invent address patterns. Do not label an address “verified” based only on syntax or domain MX records.

### 6.5 Contact ranking
Rank usable routes:
1. Confirmed direct professional WhatsApp / phone
2. Confirmed direct professional email
3. Likely direct professional channel with clear supporting evidence
4. Official clinic/department channel with a named routing request
5. General institution channel
6. Third-party directory contact, only as a lead to verify

Do not hide lower-confidence contacts; list them separately. State the best first route and why.

### 6.6 Exhaustive-search ledger
Include a compact coverage table:
- Source/channel category
- Sources actually searched
- Findings
- Access limitations
- Follow-up branch opened (yes/no)

Distinguish:
- No result found after searching
- Source unavailable
- Source requires login/paywall
- Source not relevant
- Not searched

The phrase “no public contact found” is permitted only after documenting meaningful source coverage. State the date of research.

## 7. Clinical and specialty analysis

Analyze four levels:
1. Broad specialty.
2. Subspecialty and scope of practice.
3. Procedures actually evidenced in public sources.
4. Imaging / intraoperative use cases that may follow from those procedures.

For each claimed procedure, label:
- Publicly documented
- Doctor self-reported (from user-provided conversation)
- Institution-published
- Inferred from specialty only
- Unknown / needs confirmation

Do not assume that every surgeon performs every procedure within a specialty. Do not equate diagnostic imaging with intraoperative fluoroscopy. Do not assume a doctor personally owns or purchases equipment.

### Clinical question design
Select the single most useful next question based on the evidence. Examples:
- Orthopedics/trauma: fracture reduction, trauma fixation, joint replacement, arthroscopy, spine procedures; whether intraoperative fluoroscopy is used and by whom.
- Urology: endourology, stone procedures, stent placement, PCNL, lithotripsy; fluoroscopy use and current equipment.
- General / laparoscopic surgery: cholangiography, selected catheter or endovascular procedures; verify actual scope before suggesting C-arm.
- Pain management: image-guided injections, blocks, spine procedures; confirm whether ultrasound, C-arm, or CT guidance is used.
- Neurosurgery/spine: instrumentation, fixation, navigation, intraoperative imaging.
- Cardiology/interventional: angiography, PCI, structural heart procedures; assess fixed cath lab versus mobile C-arm suitability rather than assuming equivalence.
- Dentistry/maxillofacial: CBCT and relevant 3D imaging use cases.
- Radiology/imaging centers: modality mix, room count, throughput, detector and workflow needs.

These are question prompts, not claims about the prospect.

## 8. Institution and commercial research

Research each relevant practice, hospital, clinic, group, or distributor separately from the doctor.

### Institution profile
- Legal / public-facing name and aliases
- Country, city, address at institutional level only
- Public/private/nonprofit/government status
- Hospital, clinic, imaging center, day-surgery center, office, distributor, or unknown
- Services and departments
- Branches and affiliations
- Scale indicators that are publicly supported
- Relevant decision-makers and roles
- Procurement route and whether the doctor is a user, recommender, technical evaluator, budget holder, or buyer

### Equipment and purchasing
Look for:
- Current or historical equipment brands/models
- Equipment installation announcements
- Public tenders, procurement plans, awards, and contracts
- Public supplier/distributor references
- Expansion, renovation, new-room, or new-facility announcements
- Equipment age or replacement signals only when source-supported
- Regulatory/import requirements in the target country

Distinguish current installation, historical procurement, tender request, awarded purchase, and mere catalogue mention. Record procurement currency, date, tax/shipping scope, and source if price is found. Never compare FOB and delivered prices as equivalent.

### Decision chain
Identify, where public:
- Clinical user / physician
- Department head
- Biomedical engineering
- Radiology manager
- Purchasing/procurement
- Finance / administration / owner
- Distributor/importer/service partner

Do not assume the doctor has purchasing authority. If unknown, ask who evaluates and purchases imaging equipment.

## 9. Perlove product matching

Map the verified clinical/institution evidence to a product family. Do not force a match.

### Initial product map
- Mobile DR: bedside imaging, ICU, emergency, ward imaging, mobile radiography.
- Fixed DR: general radiography rooms and imaging centers.
- Suspended/ceiling DR: room layout and workflow where ceiling suspension is appropriate.
- Dynamic DR / DRF: documented need for dynamic fluoroscopy plus radiography.
- Mobile C-arm: intraoperative fluoroscopy for relevant surgical procedures.
- Interventional C-arm: selected interventional use cases only when clinical and technical scope supports it.
- 3D C-arm: procedures with documented need for intraoperative 3D imaging.
- CBCT: dental, maxillofacial, ENT, and other locally approved use cases.

For each recommended product state:
- Evidence supporting the clinical use case
- What is confirmed versus inferred
- Why it fits
- What could make it unsuitable
- The key question needed to validate fit
- Whether another product or a channel partner is more appropriate

### Technical and regulatory guardrails
Before making model-level claims, verify current official product documents and local regulatory requirements:
- Generator power, kV, mA, mAs, pulse rate, frame rate
- Tube model, anode heat capacity, focal spots
- Detector size, pixel pitch, resolution, wireless/wired status
- Mechanical movement, SID, table/stand configuration
- Power supply, phase, voltage, frequency, line impedance and installation conditions
- DICOM/PACS, workstation, printing, storage, cybersecurity where relevant
- Accessories, lead protection, installation, training, warranty, service
- Country registration / import / radiation licensing / permitted indications

Never invent specifications or state regulatory approval without evidence. Use “to be confirmed with engineering/regulatory” where appropriate.

## 10. Lead scoring and priority

Score out of 100 with these weights:

| Dimension | Weight |
|---|---:|
| Clinical application fit | 25 |
| Purchase / replacement likelihood | 20 |
| Institution commercial value | 15 |
| Decision influence / access to buyer | 15 |
| Contact quality / reachability | 10 |
| Channel / partnership value | 10 |
| Information completeness | 5 |
| Total | 100 |

Use evidence-backed sub-scores. If evidence is missing, award only the score justified by known facts; do not fill gaps with optimistic assumptions.

Priority:
- A: 80–100 — priority development
- B: 60–79 — qualified development / further validation
- C: 40–59 — nurture / limited research
- D: 0–39 — low priority or pause

### Confidence and grade safeguards
- Show both score and evidence confidence (high / medium / low).
- Specialty-only inference cannot establish a confirmed clinical use case.
- A lead with an unresolved identity conflict cannot be A.
- A lead with no credible contact route should not receive full contact-quality points.
- A doctor without purchasing authority may still be valuable as a clinical influencer, but label the role accurately.
- Do not inflate the score because a product is in the catalogue.
- Provide a reason for each score and the highest-impact missing fact.

## 11. First-contact and outreach workflow

### 11.1 Channel and recipient selection
Use the highest-ranked professional route. Identify whether the recipient is:
- Doctor personally
- Assistant / secretary
- Clinic receptionist
- Department
- Hospital general account
- Distributor / third party

Address the actual recipient, not the doctor, when the account is institutional. Never claim that a number or inbox belongs to the doctor unless supported.

### 11.2 First WhatsApp message: identity confirmation
When the channel is plausible but the doctor's personal use is not established, first send only a short identity-check message. Do not promote products yet.

Spanish example:
“Hola, Dr./Dra. [Nombre]. Buenos días. Disculpe que le contacte. Quisiera confirmar si estoy comunicándome directamente con [Nombre completo], especialista en [especialidad]. Muchas gracias por su ayuda.”

English example:
“Hello Dr. [Name], good morning. Sorry to contact you unexpectedly. May I confirm whether I am speaking directly with [Full Name], the [specialty] physician? Thank you for your time.”

Chinese translation must accompany Spanish/English drafts.

For a clinic or assistant:
“Hola, buenos días. Quisiera confirmar si el Dr./la Dra. [Nombre] actualmente atiende en su institución. ¿Sería posible indicarme el canal adecuado para hacerle llegar una consulta profesional?”

Do not ask the clinic to disclose private personal contact details. Request a transfer, message relay, or official professional channel.

### 11.3 After identity confirmation
Introduce the sender and manufacturer briefly. Use the user's confirmed company identity and current product catalogue; do not invent titles, manufacturing scope, certifications, installations, or customer references.

Then ask one tailored clinical question based on verified evidence. Avoid multi-question interrogations and generic mass-pitch language.

### 11.4 Product discussion
Only after a clinical or institutional need is established:
- Explain the relevant application.
- Offer the smallest useful set of product materials.
- Ask about current equipment and workflow.
- Confirm technical requirements before proposing a model.
- Move to quotation only when configuration, delivery scope, destination, and decision process are understood.

### 11.5 Email outreach
Email is a parallel channel, not a verbatim copy of WhatsApp.
- If the email is a personal/professional mailbox and identity is unknown, begin with a short recipient/identity confirmation and concise professional context.
- If the mailbox is clearly an official institution inbox, address the office and request routing to the named doctor/department.
- After WhatsApp identity confirmation or an earlier introduction, do not repeat the same first-touch pitch. Use email for complementary detail, requested catalogue/specification, formal introduction, or a concise follow-up.
- Include a meaningful subject, personalized opening, one clear purpose, one call to action, and a professional close.
- If the user's email signature is automatic, do not duplicate name/company at the end.
- Provide Chinese translation alongside Spanish/English drafts.
- Do not claim attachments were sent unless they are actually attached/sent.

### 11.6 Outreach cadence and stop rules
Suggest, rather than automatically execute, follow-up timing. Account for local business hours, country holidays, the contact's stated availability, and previous message times. Do not send repeated messages across WhatsApp and email on the same day without a clear reason.
- No reply: one concise follow-up after a reasonable interval; then reassess and avoid indefinite chasing.
- Auto-reply: treat as an automated acknowledgement, not a human response.
- Referral: record the referral as pending until the new person/channel is confirmed.
- No need: acknowledge and close or nurture only if appropriate.
- Explicit refusal / opt-out: stop outreach through the requested scope and record do-not-contact.
- Wrong number: stop using that number and return to research.
- Never imply that a draft has been sent.

## 12. Communication history and continuity

Before drafting:
- Read the entire supplied conversation in timestamp order.
- Identify who sent each message and which channel/account was used.
- Separate messages actually sent, actual replies, auto-replies, internal notes, and assistant proposals.
- Preserve the contact's displayed name order and spelling.
- Do not repeat already-sent content unless the user asks for a full rewrite.
- If the user says “the previous message was already sent”, output only the incremental message.
- Keep a cross-channel log so WhatsApp and email do not duplicate each other.
- Preserve language and local greeting based on recipient's local time if known; otherwise use a neutral greeting.

## 13. Required output format

For a single lead, use the following report structure. **The contact register must appear first.** Do not lead with a long identity-verification report or a restatement of the raw input.

### 1. Contact register

Prioritize the fields in this order:
1. Customer's full name (preserve original spelling and name order), professional title, and specialty.
2. Direct professional phone / mobile number.
3. WhatsApp number, explicitly state whether WhatsApp is confirmed, merely listed, or unknown.
4. Professional email.
5. Official clinic / institution phone, WhatsApp, email, website, and contact form.
6. Other professional profiles or referral channels.

For every route include contact value, channel, person/organization association, direct source URL, research date, ownership confidence, reachability status, and recommended use. Do not hide lower-confidence results; label them. A useful lead can be reported before ownership is fully confirmed. Keep doctor-direct, clinic, department, and third-party routes separate.

### 2. Professional identity and supplied-lead context
- Briefly state the supplied name/search clues.
- Identity conclusion and confidence based on newly found evidence.
- Current / historical institution distinctions.
- Material conflicts only; do not perform a separate audit of the original lead row.
- Sources.

### 3. Search coverage
A table showing contact-focused source categories actually searched, findings, limitations, and branches followed. State "not searched" honestly.

### 4. Clinical and institution analysis
Separate person-level facts from institution-level facts. Label each clinical claim as documented, self-reported, institution-published, inferred, or unknown.

### 5. Product matching
Primary and secondary product family, rationale, evidence, contraindications/gaps, and next validation question.

### 6. Commercial qualification
Score, grade, evidence confidence, dimension-level rationale, buyer/decision chain, procurement signals, and key missing information.

### 7. Outreach drafts
- First WhatsApp identity-check message.
- Institution/assistant variant when needed.
- After-confirmation introduction (clearly marked not for first send).
- One tailored clinical question.
- First email / institutional routing email.
- Complementary follow-up email when relevant.

Provide Chinese translation for every Spanish/English draft.

### 8. Next action
Recommend one highest-value next action and explain why. Include what must be confirmed before progressing.

For batch leads, provide a compact comparison table first, then an independent dossier for each lead. Do not let one lead's identity or contacts bleed into another's record.

## 14. Citation and source requirements

- Cite all material web-derived factual claims.
- Prefer primary/official sources; use directories for discovery and corroborate them.
- Cite the specific source supporting each contact and identity claim.
- Use direct URLs in the contact register so the user can open the original page.
- Note source publication date or registry cutoff when relevant.
- Avoid treating search snippets as conclusive when the underlying page can be opened.
- If sources conflict, cite both and explain the discrepancy.
- Do not cite inaccessible pages as if their contents were verified.
- Do not copy large source passages; summarize.

## 15. Final quality checklist

Before returning a dossier, verify:
- [ ] Original name spelling/order preserved.
- [ ] Identity not inferred from name alone.
- [ ] Current and former institutions separated.
- [ ] Every contact has a source and ownership label.
- [ ] Doctor-direct vs clinic/third-party channels distinguished.
- [ ] WhatsApp use not assumed from mobile number alone.
- [ ] Email not guessed or marked verified by syntax alone.
- [ ] Search coverage and inaccessible sources disclosed.
- [ ] Clinical procedures evidenced or explicitly labeled as inference.
- [ ] Institution-level equipment not inferred from doctor-level use.
- [ ] Product fit tied to actual or clearly qualified use cases.
- [ ] Technical/regulatory claims checked against current sources.
- [ ] Score is evidence-based and confidence shown.
- [ ] First contact confirms identity before promotion when needed.
- [ ] WhatsApp and email content is complementary, not duplicated.
- [ ] Chinese translations accompany foreign-language drafts.
- [ ] No message is described as sent unless it was sent.
- [ ] Refusal and do-not-contact status respected.
- [ ] Next action is specific and singular.
