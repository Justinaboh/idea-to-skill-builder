# Sample Run (illustrative, fictional)

This example shows the intended behaviour. The skill idea below is invented for demonstration.

## 1. User input
> Turn this into a skill: something that helps freelancers write project proposals.

## 2. Correct behaviour: classify and assume
The assistant classifies this as **idea-to-skill**, asks no questions, and states assumptions:
- **Assumed:** users are solo freelancers selling services to small businesses.
- **Assumed:** output is a proposal document the freelancer edits, not a finished contract.

## 3. Correct behaviour: proposal (abridged)
**A. Identity:** `freelance-proposal-writer`. Helps freelancers produce clear, client-specific project proposals.
**B. Does:** gathers project details, drafts scope, deliverables, timeline, and pricing options; flags missing information.
**E. Adding:** a pricing-options section (**Designed**), a scope-exclusions checklist to reduce scope creep (**Designed**).
**F. Architecture:** `SKILL.md`, `README.md`, `LICENSE`, `references/proposal-structure.md`, `templates/proposal.md`.
**H. Limits:** not legal advice; no contract drafting.

Closing line, verbatim:
"Would you like me to proceed with this skill architecture, or would you like to modify anything before I build it?"

The assistant then **stops**.

## 4. Incorrect behaviour (do not do this)
- Writing SKILL.md in the same reply as the proposal.
- Treating the user's reply "interesting, tell me more" as approval.
- Writing "I researched freelance industry standards" when no research happened.
- Saying "uploaded to GitHub" after only creating a ZIP.

## 5. After the user replies "Proceed"
The assistant builds the files, runs the validator and QA checklist, creates and verifies the ZIP, presents it, and reports what was and was not tested.
