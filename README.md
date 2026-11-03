# Foreign Trade Essential Skills

A combined source repository for two independent Skills supporting overseas medical-device sales.

## Included Skills

1. **Medical Lead Development** (`skills/medical-lead-development/`) — evidence-led public-source prospect research, identity and professional contact verification, clinical and institutional qualification, procurement research, Perlove product matching, lead scoring, and staged WhatsApp/email outreach.
2. **Client Progress Summary** (`skills/client-progress-summary/`) — accurate, concise Chinese CRM progress summaries from actual WhatsApp, email, meeting, and other customer communications.

## Operating defaults

- **Scope:** medical-device overseas sales.
- **Research depth:** exhaustive across relevant public professional sources.
- **Execution:** staged human review; each material stage is presented with evidence and sources before proceeding.
- **Privacy:** use professional contact details intentionally made public. Do not collect private personal data, patient data, leaked data, or bypass access controls.
- **Outreach:** no messages, emails, forms, CRM writes, or purchase commitments are executed without explicit user authorization.
- **Accuracy:** distinguish verified facts, inference, unknowns, conflicting evidence, sent messages, automated replies, and planned actions.

## Repository structure

- `skills/medical-lead-development/`: prospect research and staged outreach.
- `skills/client-progress-summary/`: Chinese CRM progress summaries.
- `schemas/`: lead, contact, and communication data structures.
- `tests/`: acceptance criteria and lightweight validation.
- `docs/`: installation and distribution notes.

## Private ChatGPT plugin

The owner-created ChatGPT plugin is named **foreign-trade-essential-skills**. Its private status is independent of this public source repository. Publishing this repository does not make the plugin publicly discoverable or grant other ChatGPT accounts access.

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
