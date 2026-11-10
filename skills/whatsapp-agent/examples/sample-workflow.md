# Worked example — order-status messaging (illustrative, fictional shop)

**Shop:** "Harbor Coffee Lab". **Goal:** tell customers when their order ships, and handle "where is my order?" without spamming.

1. **Consent first.** Check each recipient against the consent register (`references/consent-register-template.csv`): who opted in, when, how, for which purpose. No record → no message; route to the opt-in step instead.
2. **Classify the message.** "Your order has shipped" is transactional and tied to a purchase. A discount announcement is marketing and needs its own opt-in and policy check (`references/whatsapp-policy-check.md`).
3. **Draft the template.** Plain language, one purpose, variables for name and order number, no invented delivery dates, a way to opt out. Submit for platform approval through the official process; do not claim it is approved until it is.
4. **Pre-flight** (`references/message-preflight.md`): recipient opted in, template approved, variables filled from the system of record, language matches the customer, send window considered.
5. **Approval gate.** Show the exact recipients count, template, variables and send time. A human approves; the skill does not send on its own.
6. **Support flow.** Customer asks "where is my order?" → look up status from the order system, answer with that status only. If the data is missing or the customer is upset → escalate (`references/escalation-policy.md`) with the conversation summary.
7. **Verify.** Read delivery reports from the provider; do not report "delivered" until the provider says so; reconcile before retrying a timed-out send.

Output delivered: consent check result, template draft, pre-flight result, approval summary, escalation hand-off note, "not attempted" list.
