# Foreign Trade Essential Skills

A combined source repository for three independent Skills supporting overseas medical-device sales.

## Included Skills

1. **Medical Lead Development** (`skills/medical-lead-development/`) — exhaustive, evidence-led public-source prospect research, identity and professional contact verification, clinical and institutional qualification, procurement research, product matching, lead scoring, and staged outreach.
2. **Medical Prospect Development** (`skills/medical-prospect-development/`) — a complete prospect dossier workflow with contact discovery first and a fixed nine-part report. The first-contact WhatsApp/email drafts appear immediately after the contact register, followed by professional background, clinical evidence, Perlove product fit, institutional procurement analysis, scoring, next actions, and a CRM summary.
3. **Client Progress Summary** (`skills/client-progress-summary/`) — accurate, concise Chinese CRM progress summaries from actual WhatsApp, email, meeting, and other customer communications.

## Operating defaults

- **Scope:** medical-device overseas sales.
- **Research depth:** broad and systematic across relevant public professional sources.
- **Contact-first:** use the supplied lead as a search seed; prioritize usable professional phone, WhatsApp, and email discovery without a separate preliminary audit of every original field.
- **Report order:** contact register → first-touch / follow-up drafts → professional background → academic and clinical evidence → product matching → institution and procurement → scoring → next actions → CRM summary.
- **Execution:** staged human review; show evidence and sources before material next steps.
- **Privacy:** use professional contact details intentionally made public. Do not collect private personal data, patient data, leaked data, or bypass access controls.
- **Outreach:** no messages, emails, forms, CRM writes, or purchase commitments are executed without explicit user authorization.
- **Accuracy:** distinguish verified facts, inference, unknowns, conflicting evidence, sent messages, automated replies, and planned actions.

## Repository structure

- `skills/medical-lead-development/`: comprehensive prospect research and staged outreach.
- `skills/medical-prospect-development/`: fixed-format prospect dossiers and ready-to-edit localized outreach.
- `skills/client-progress-summary/`: Chinese CRM progress summaries.
- `schemas/`: lead, contact, and communication data structures.
- `tests/`: acceptance criteria and lightweight validation.
- `docs/`: installation and distribution notes.
- `plugins/medical-prospect-development/`: standalone Skill plugin manifest backup.

## Private ChatGPT plugin

The owner-created ChatGPT plugin is named **foreign-trade-essential-skills**. Its private status is independent of this public source repository. Publishing this repository does not make the private ChatGPT plugin publicly discoverable or grant other ChatGPT accounts access.

## Validation

Run:

```bash
python tests/validate_skills.py
```

The validation checks JSON files, Skill frontmatter, required Skill metadata, and local Markdown links.

## Privacy and contribution

Do not commit real customer phone numbers, private email addresses, patient information, raw WhatsApp exports, or confidential commercial records. Use anonymized examples only.

## License

MIT. See [LICENSE](LICENSE).
