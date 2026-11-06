# Platform Notes (portability)

Goal: keep the core skill portable. The core is plain Markdown with a small frontmatter block (`name`, `description`) in `SKILL.md`, supporting files in subfolders, and no provider-specific dependencies.

## What is established
- The open Agent Skills convention uses a folder with a `SKILL.md` that has YAML frontmatter containing at least `name` and `description`, plus optional supporting folders. Skills load progressively: metadata first, then the body, then referenced files as needed.

## What varies by platform (always verify against current documentation)
- How a skill is installed or uploaded (file upload, folder placement, settings page, repository config).
- Whether file creation, shell, web search, or scripts are available.
- Size limits and which file types are accepted.
- Whether the platform reads `SKILL.md` natively or needs its content pasted into custom instructions, a project, or a system prompt.

## Compatibility language to use
- "Designed to follow the Agent Skills convention."
- "Tested on: (only platforms actually tested)."
- "Should work on (platform) by pasting SKILL.md into its custom-instruction field; unverified."
Never write "works everywhere".

## Fallback for platforms without native skill support
1. Paste the SKILL.md body into the platform's custom instructions or project instructions.
2. Upload or paste the reference files and tell the assistant to consult them when SKILL.md says so.
3. Expect weaker behaviour for stages that need file creation, scripts, or web research; document those.
