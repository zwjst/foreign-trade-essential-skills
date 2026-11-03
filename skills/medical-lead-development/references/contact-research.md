# Contact research reference

## Research priority

Treat the supplied lead row as a search seed. Do not spend a preliminary pass proving the original row or auditing every supplied field. Start searching immediately and prioritize: (1) customer's exact name and professional title, (2) direct professional phone/mobile, (3) WhatsApp number and explicit WhatsApp evidence, (4) professional email, then (5) official clinic/institution fallback channels. Report useful public contact findings with their actual confidence even when ownership is not fully confirmed; do not hold back a lead solely because a second source is unavailable. Continue identity/ownership checks only to distinguish the doctor from an institution, assistant, third party, or similarly named person and to avoid misdirected outreach.

## Contact record schema
- `value`: exact published phone/email/profile URL
- `normalized_value`: normalized international phone only when country code is clear
- `channel`: WhatsApp, mobile, landline, email, social, contact form
- `owner_type`: doctor, clinic, institution, department, third party, unknown
- `owner_name`: exact public attribution, if any
- `source_url`: direct page
- `source_type`: official profile, appointment platform, journal, association, news, directory, etc.
- `published_at`: date if visible
- `researched_at`: date checked
- `ownership_confidence`: confirmed, likely, tentative, conflicting, unknown
- `reachability`: not tested, auto-reply, human reply, delivered, invalid, opted out
- `notes`: evidence and caveats

## Phone normalization
Preserve the original display form. Store normalized E.164 only when the country calling code and number are unambiguous. Never strip leading zeros or assume country from language alone.

## WhatsApp distinctions
- WhatsApp explicitly displayed by an official doctor profile: source says WhatsApp, but ownership may still need confirmation.
- WhatsApp icon on clinic page: clinic channel unless explicitly attributed to doctor.
- Mobile phone in directory: phone only; WhatsApp unknown.
- Auto-reply: confirms that the account endpoint responds, not that the doctor personally uses it.
- Human reply: confirms a person is responding, not necessarily that the person is the doctor until they identify themselves or other evidence establishes it.

## Email distinctions
Do not generate address permutations. A named address in a journal or official profile may be a professional contact, but it can be stale. A generic inbox should be labeled as generic and addressed accordingly.

## Research coverage ledger
| Channel | Search queries / pages | Result | Limitation | Next branch |
|---|---|---|---|---|
| Official clinic | | | | |
| Appointment platforms | | | | |
| Hospital directory | | | | |
| Associations | | | | |
| Publications | | | | |
| Conferences | | | | |
| News / interviews | | | | |
| Professional social | | | | |
| Public business records | | | | |

## Privacy and compliance
Use only professional details intentionally made public. Do not seek private residential numbers, private family contacts, breached data, leaked databases, or hidden personal profiles. Respect site terms and applicable privacy/anti-spam rules.
