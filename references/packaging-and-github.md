# Packaging and GitHub Readiness (Stage 10)

## Folder rules
- Folder name = skill name = `name` in the SKILL.md frontmatter.
- Include only directories that contain real files.
- No generated junk (`.DS_Store`, `__pycache__`, temp files), no secrets, no private data.

## ZIP rules
- The ZIP contains one top-level folder named after the skill, with the structure intact:
  `my-skill.zip` contains `my-skill/SKILL.md`, `my-skill/README.md`, and so on.
- Typical command: `cd <parent-dir> && zip -r my-skill.zip my-skill -x "*.DS_Store" "*/__pycache__/*"`
- Verify before delivering: the file exists, `unzip -l my-skill.zip` lists every expected file, and the paths start with the skill folder.
- Deliver with the platform's file-presenting tool. Do not paste a made-up URL.

## Repository naming and hygiene
- Repo name: short, lowercase, hyphenated, descriptive (usually the skill name).
- Include README.md, LICENSE, and the skill folder contents at the repo root or in a clearly named folder.
- Suggested GitHub topics (user's choice): agent-skills, ai-skills, prompt-engineering, llm.

## What you may and may not claim
- A ZIP is not a GitHub repository.
- Say "published" only if a GitHub integration actually created and populated the repo, and report the repo URL it returned.
- Otherwise give manual steps: create an empty repo on GitHub, upload or push the files, add a description and topics.
