# idea-to-skill-builder

Turn a conversation, a rough idea, or a one-line concept into a complete, reusable, GitHub-ready AI skill.

## What it is
`idea-to-skill-builder` is an AI skill (a folder of instructions and reference files) that makes an AI assistant act as a skill architect. You give it a discussion, a workflow, or just a sentence. It extracts or develops the idea, designs the skill, shows you a written proposal, waits for your approval, and then builds a downloadable package.

## The problem it solves
Useful thinking gets buried in chat history, and turning it into a clean, shareable skill normally means knowing the file format, structuring knowledge, writing a README, and packaging it. This skill handles that process and keeps you in control with an approval step.

## What it can do
- Extract reusable methods from a conversation and discard one-off details and personal preferences
- Develop a bare idea into a full skill design
- Research gaps when web access is available, and label what was researched, designed, or assumed
- Present a structured proposal (identity, capabilities, workflow, additions, architecture, limits, recommendation)
- Build `SKILL.md`, reference files, examples, evals, README, and LICENSE
- Run mechanical validation and package a ZIP with the folder structure intact
- Prepare the result for GitHub, without claiming publication it did not perform

## How it works
1. Classify the input (conversation, idea, or both)
2. Extract reusable intelligence
3. Judge whether it deserves to be a skill
4. Research and fill gaps
5. Design the architecture
6. **Present a proposal and stop for your approval**
7. Build the files
8. Test honestly
9. Quality-check
10. Package and deliver

## Who it is for
Anyone who wants to create their own AI skills: founders, consultants, educators, developers, and designers, with or without technical experience.

## What makes it different
- A mandatory approval checkpoint: nothing is built until you say so
- Every element is labelled original, researched, designed, or assumed
- Honesty rules: no invented sources, test results, or download links
- Keeps `SKILL.md` lean and moves detail into reference files

## Installation and use
The skill is a folder following the Agent Skills convention: a `SKILL.md` with `name` and `description` frontmatter plus supporting files.

1. Download the ZIP or clone this repository.
2. Install the `idea-to-skill-builder` folder using your platform's skill mechanism. Installation differs by platform, so follow its current documentation.
3. If your platform has no skill support, paste the body of `SKILL.md` into custom or project instructions and provide the files in `references/` as needed. See `references/platform-notes.md`.
4. Start a chat and describe what you want to turn into a skill.

## Supported platforms
Designed to follow the Agent Skills convention. It has not been tested across platforms; treat compatibility as unverified until you try it. Stages that need file creation, scripts, or web research require an environment that provides them.

## Repository contents
```
idea-to-skill-builder/
├── SKILL.md                         Operating instructions for the AI
├── README.md                        This page
├── LICENSE                          MIT
├── references/
│   ├── proposal-template.md        The A-I proposal structure
│   ├── readme-template.md          Sections for generated READMEs
│   ├── qa-checklist.md             Pre-packaging checks
│   ├── packaging-and-github.md     ZIP and GitHub rules
│   └── platform-notes.md           Portability guidance
├── examples/sample-run.md           Illustrative run with right and wrong behaviour
├── evals/test-prompts.md            Ten test scenarios
└── scripts/validate_skill.py        Mechanical validator (Python 3)
```

## Example prompts
- "Turn this conversation into a skill."
- "Build a reusable skill around this: a method for validating business ideas."
- "A skill that teaches people how to understand colour."
- "Extract a skill from this discussion and make it GitHub-ready."
- "Package this workflow as a skill."

## Known limitations
- Cannot create ZIPs or files in environments without file tools
- Research quality depends on web access
- Cannot publish to GitHub without a connected integration
- Evals are a test plan to run by hand; no automated results are included

## Contributing
Issues and pull requests are welcome. Please describe the problem or improvement, keep `SKILL.md` lean, and run `python scripts/validate_skill.py .` from the repository folder's parent before submitting.

## Licence
MIT. See `LICENSE`.
