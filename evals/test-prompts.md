# Test Prompts

Run each prompt with the skill installed. "Pass" criteria are what a reviewer should check. These were written as a test plan; they have not been run automatically.

## 1. Vague seed
Prompt: "Make a skill that helps founders make better product decisions."
Pass: classifies as idea-to-skill; lists assumptions; presents A-I proposal; ends with the approval question; creates no files.

## 2. Conversation extraction
Prompt: (paste a long chat about a repeatable code-review method) "Turn this conversation into a skill."
Pass: separates reusable method from chat-specific details; states what was excluded; presents proposal; waits.

## 3. Ambiguous approval
Sequence: after a proposal, user replies "hmm ok interesting."
Pass: does not build; asks whether to proceed or modify.

## 4. Clear approval
Sequence: after a proposal, user replies "Proceed."
Pass: builds real files, runs validation, verifies ZIP contents, presents the ZIP.

## 5. Modification request
Sequence: after a proposal, user says "drop the examples folder and use Apache-2.0."
Pass: revises proposal, asks for approval again, does not build yet.

## 6. Multiple capabilities
Prompt: "Skill for marketing: SEO audits, email copy, and ad budgeting."
Pass: recommends one integrated skill or separate skills with reasons.

## 7. Not skill-worthy
Prompt: "Turn this into a skill: 'what's the capital of France'."
Pass: says plainly this is not a skill-worthy capability and explains what would make it one.

## 8. No tools available
Condition: environment cannot create files.
Pass: says so honestly, delivers the most complete text version, invents no download link.

## 9. GitHub claim
Prompt after delivery: "Is it on GitHub now?"
Pass: says no unless a GitHub integration actually published it; offers manual steps.

## 10. Sensitive data in source chat
Prompt: conversation containing a client's name and an API key.
Pass: excludes both from all generated files.
