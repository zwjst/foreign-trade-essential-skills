---
name: client-progress-summary
description: "Use when the user supplies WhatsApp, email, meeting, or other overseas medical-device sales conversations and wants a concise Chinese CRM progress summary, registration-table note, or accurate follow-up status."
---

# Client Progress Summary

## Goal
Turn user-supplied overseas medical-device sales conversations into one concise, objective Chinese paragraph suitable for a CRM registration log. Preserve actual progress and customer feedback. Never invent an action, response, identity, need, or equipment fact.

## Default output format
`国家 城市 专业医生／联系人身份。已介绍公司信息和产品信息，并[实际沟通主题]。对方[明确反馈]，[有事实依据的需求判断]。[下一步具体动作或已发出询问的状态]。`

Adapt the sentence naturally when company/product introduction has not happened. Do not force every field into the paragraph.

## Mandatory rules

1. When the user asks for a summary, registration note, or CRM entry, output one paragraph only. No heading, bullet list, table, explanation, or extra sales advice unless explicitly requested.
2. Put known personal context first in this order: country, city, specialty/contact role, then actual progress. Omit unknown fields; never invent them.
3. **Do not include the doctor's name, individual contact's name, or specific hospital/clinic/practice name** in the CRM paragraph. Use “医院工作人员”, “诊所工作人员”, “经销商”, “采购人员”, or another verified role. General institution descriptions are acceptable.
4. When the company and product information have actually been introduced, use exactly **“已介绍公司信息和产品信息”**. Do not list product types again in that opening phrase. If only a personal greeting or self-introduction occurred, do not claim company/product introduction.
5. Preserve the contact's actual specialty. If the contact is not a physician, do not label them as a doctor. Unknown roles remain “联系人身份待确认” or a similarly concise phrase.
6. Mention WhatsApp, email, phone, or meeting only when the channel materially affects progress or the user asks for it.
7. Distinguish sent messages, received replies, automated replies, internal notes, and proposed drafts. A message drafted by the assistant is not sent unless the user says it was sent.
8. If a question has been sent but not answered, write “已询问……，目前等待回复。” If it is only a planned next step, write “下一步询问……。” Never convert a plan into a completed action.
9. An automatic WhatsApp greeting or out-of-office reply is not a human response. Record it as an automatic reply if relevant; do not claim the doctor has replied or confirmed identity.
10. A clinic or hospital account does not prove the doctor personally uses that number. Do not upgrade contact ownership without evidence.
11. A doctor saying they do not use intraoperative fluoroscopy does not prove the hospital has no C-arm, DR, or other imaging equipment.
12. A staff member who cannot provide equipment details does not establish that the institution lacks the equipment. State that the configuration is unknown.
13. Describe product-demand fit only when supported by the actual conversation or reliable research. Use cautious wording such as “目前 C 臂需求匹配度尚待确认” where appropriate.
14. Do not claim that a referral, meeting, quotation, purchase, or technical confirmation occurred unless it actually happened.
15. If the user says previous content has already been sent, provide only the new incremental message when drafting; do not repeat the old message unless asked to rewrite the full sequence.

## Language and drafting boundary
This skill is for CRM summaries. If the user asks to translate, analyze, or draft a WhatsApp/email message:
- Complete that task rather than forcing a CRM paragraph.
- For Spanish or English drafts, provide a Chinese translation unless the user says otherwise.
- Preserve the exact displayed spelling and order of contact names when a name is needed in the message.
- Do not add a sender name/company at the end of email drafts when the user's automatic signature is configured.
- Choose a greeting based on the recipient's local time when known; otherwise use a neutral greeting.
- Draft only content that is appropriate to the recipient type (doctor, assistant, institution, distributor).

## Summary quality check
Before responding, confirm:
- Country/city/specialty/role are supported.
- Personal names and specific institution names are omitted.
- Company/product introduction is described truthfully.
- Actual questions and actual replies are distinguished.
- Auto-replies are not treated as human replies.
- No unsupported equipment or purchase inference appears.
- Next action is clearly either completed or planned.
- Output is one concise paragraph when a CRM summary was requested.

## Examples

### 1. Doctor has not confirmed identity
Input: A message was sent to a number asking whether it is the named doctor. The only response is a clinic auto-reply.
Output:
`墨西哥 医生身份待确认。已通过 WhatsApp 联系相关号码并收到诊所自动回复，目前无法确认该号码是否由医生本人使用。下一步在诊所工作时间询问医生是否在该机构执业，并请求转达或提供适当的专业联系渠道。`

### 2. Doctor says they do not use intraoperative imaging
Input: A Tegucigalpa surgical oncologist was introduced to the company and products and asked about intraoperative imaging. The doctor said their own procedures do not use it; institution equipment is still unknown.
Output:
`洪都拉斯 Tegucigalpa 肿瘤外科医生。已介绍公司信息和产品信息，并询问其手术中 X 射线及术中透视设备的使用情况。对方明确表示本人手术中不使用相关设备，当前个人 C 臂需求匹配度较低，机构层面的设备情况尚未确认。下一步询问其执业机构的设备使用情况。`

### 3. Hospital staff referral requested
Input: A Cartagena hospital staff member confirmed the institution. The seller introduced the company and products, asked about imaging equipment, and requested a biomedical engineering or purchasing contact. No reply yet.
Output:
`哥伦比亚 Cartagena 医院工作人员。已介绍公司信息和产品信息，并询问医院医学影像设备情况及合作机会。对方确认所属机构，但具体职务及设备配置尚未明确。已询问能否转介生物医学工程或采购部门负责人，目前等待回复。`

### 4. Only a greeting and self-introduction
Input: The seller greeted the contact and introduced themselves as Jef from Perlove, but did not yet describe the company or products.
Output:
`[国家] [城市] 联系人身份待确认。已发送首次问候及个人身份介绍，目前尚未确认对方身份，也未介绍公司及产品信息。下一步确认对方是否为目标医生或相关机构联系人。`

### 5. Planned, not sent
Input: The seller plans to ask whether the hospital has an equipment replacement plan but has not sent the question.
Output:
`[国家] [城市] [专业/联系人身份]。……下一步询问医院是否有影像设备更新或新增计划。`
