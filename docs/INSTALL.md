# Installation / 安装说明

## Private ChatGPT plugin

The owner-created private plugin is maintained separately in ChatGPT under the name **foreign-trade-essential-skills**. Its audience is private. A public GitHub repository does not grant other ChatGPT accounts access to that private plugin.

Use the repository's independent Skills according to the task:

- `medical-lead-development`: exhaustive public-source research, identity/contact discovery, clinical and institutional qualification, product matching, scoring, and staged outreach.
- `medical-prospect-development`: contact-first, fixed nine-part prospect dossiers. Its mandatory report order places WhatsApp/email drafts immediately after the contact register.
- `client-progress-summary`: concise Chinese CRM summaries based only on actual customer communications.

## Manual Skills-compatible environments

Import each Skill directory under `skills/` according to the host environment's official Skills installation instructions. Keep accompanying `references/` and `examples/` directories alongside the corresponding `SKILL.md`; the main Skill file may rely on these supporting references.

The standalone manifest backup for the prospect-development Skill is stored at `plugins/medical-prospect-development/plugin.json`. The root `plugin.json` describes the combined repository plugin and is not replaced by that standalone manifest.

## Privacy

Before sharing customer conversations, remove unnecessary personal contact details and all patient information. Follow applicable privacy, confidentiality, and anti-spam requirements. Lead-research Skills are limited to relevant public professional sources and must not bypass access controls.
