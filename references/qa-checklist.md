# QA Checklist (Stage 9)

Run `python scripts/validate_skill.py <skill-folder>` first if possible. It covers the mechanical items marked (auto). Then check the rest by reading.

## Structure
- (auto) SKILL.md exists and has frontmatter with `name` and `description`
- (auto) `name` matches the folder name and is lowercase-hyphenated
- (auto) Every `references/`, `examples/`, `evals/`, or `scripts/` path mentioned in SKILL.md and README.md exists
- (auto) No empty directories; no junk files
- (auto) No leftover unfinished-work markers in SKILL.md, README.md, or examples
- LICENSE present and appropriate

## Content
- SKILL.md covers: purpose, activation, workflow, decision logic, ambiguity handling, missing-info handling, tool use, reference-file guidance, output requirements, quality standards, limitations, prohibited behaviours
- SKILL.md is lean; deep knowledge lives in references with clear "read when" instructions
- Reference files contain substantive material and do not duplicate SKILL.md
- Examples are consistent with the skill and fictional ones are labelled
- README matches the real contents and makes only verified claims

## Safety and honesty
- No credentials, private data, or personal details from the source conversation
- No fabricated sources, statistics, tests, or compatibility claims
- The final message states exactly what was and was not researched and tested

## Behaviour (run if you can; otherwise ship evals for the user)
- Normal, vague, incomplete, complex, ambiguous, edge-case, wrong-assumption, and conflicting-instruction requests
- Output consistent across repeated runs
