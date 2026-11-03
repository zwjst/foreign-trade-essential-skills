#!/usr/bin/env python3
"""Lightweight repository validation; uses only the Python standard library."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = {
    "medical-lead-development",
    "medical-prospect-development",
    "client-progress-summary",
}
errors = []

# Validate all JSON files.
for path in sorted(ROOT.rglob("*.json")):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")

# Validate Skill frontmatter and metadata.
found = set()
for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
    if not match:
        errors.append(f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
        continue
    fm = match.group(1)
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name:
        errors.append(f"Missing/invalid name: {path.relative_to(ROOT)}")
        continue
    found.add(name.group(1))
    if not desc:
        errors.append(f"Missing description: {path.relative_to(ROOT)}")
    if name.group(1) != path.parent.name:
        errors.append(f"Skill name does not match directory: {path.relative_to(ROOT)}")

missing = REQUIRED_SKILLS - found
extra = found - REQUIRED_SKILLS
if missing:
    errors.append(f"Missing required Skills: {', '.join(sorted(missing))}")
if extra:
    errors.append(f"Unexpected Skill directories: {', '.join(sorted(extra))}")

# Validate local Markdown links (ignore anchors and external URLs).
link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for path in sorted(ROOT.rglob("*.md")):
    body = path.read_text(encoding="utf-8")
    for target in link_re.findall(body):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("https://", "http://", "mailto:", "tel:")):
            continue
        candidate = (path.parent / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {target}")
            continue
        if not candidate.exists():
            errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDATION PASSED")
print(f"- JSON files valid: {len(list(ROOT.rglob('*.json')))}")
print(f"- Skills valid: {len(found)} ({', '.join(sorted(found))})")
print("- Local Markdown links valid")
