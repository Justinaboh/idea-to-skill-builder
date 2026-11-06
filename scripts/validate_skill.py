#!/usr/bin/env python3
"""Mechanical checks for a skill folder. Usage: python validate_skill.py <skill-folder>"""
import re
import sys
from pathlib import Path

MARKERS = re.compile(r"\b(TODO|TBD|FIXME|lorem ipsum)\b", re.I)
PATH_REF = re.compile(r"`?((?:references|examples|evals|scripts)/[\w./-]+\.\w+)`?")
JUNK = {".DS_Store", "Thumbs.db"}


def main(folder):
    root = Path(folder).resolve()
    errors = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        print("FAIL: SKILL.md missing")
        return 1
    text = skill.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md has no frontmatter block")
    else:
        fm = m.group(1)
        name = re.search(r"^name:\s*(.+)$", fm, re.M)
        desc = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not name:
            errors.append("frontmatter missing name")
        else:
            n = name.group(1).strip()
            if n != root.name:
                errors.append(f"name '{n}' does not match folder '{root.name}'")
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n):
                errors.append("name must be lowercase-hyphenated")
        if not desc or len(desc.group(1).strip()) < 40:
            errors.append("description missing or too short")
    for doc in ("SKILL.md", "README.md"):
        p = root / doc
        if not p.is_file():
            errors.append(f"{doc} missing")
            continue
        for ref in set(PATH_REF.findall(p.read_text(encoding="utf-8"))):
            if not (root / ref).exists():
                errors.append(f"{doc} references missing file: {ref}")
    if not (root / "LICENSE").is_file():
        errors.append("LICENSE missing")
    for d in [p for p in root.rglob("*") if p.is_dir()]:
        if not any(d.iterdir()):
            errors.append(f"empty directory: {d.relative_to(root)}")
    for f in root.rglob("*"):
        if f.name in JUNK or "__pycache__" in f.parts:
            errors.append(f"junk file: {f.relative_to(root)}")
    scan = [root / "SKILL.md", root / "README.md"] + list((root / "examples").glob("*.md"))
    for p in scan:
        if p.is_file() and MARKERS.search(p.read_text(encoding="utf-8")):
            errors.append(f"unfinished-work marker in {p.relative_to(root)}")
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS: all mechanical checks passed")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
