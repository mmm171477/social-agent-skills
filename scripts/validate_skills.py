#!/usr/bin/env python3
"""Lightweight stdlib validator for Agent Skill folders in this repository."""
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors=[]; warnings=[]; checked=0

def fail(msg): errors.append(msg)

def read_frontmatter(path):
    text=path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end=text.find("\n---",4)
    if end < 0:
        return None, text
    raw=text[4:end]
    fields={}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.startswith(' ') or line.startswith('\t'):
            continue
        if ':' in line:
            k,v=line.split(':',1); fields[k.strip()]=v.strip().strip('"\'')
    return fields, text[end+4:]

for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    checked+=1; name=folder.name; skill=folder/'SKILL.md'
    if not skill.exists():
        fail(f"{name}: missing SKILL.md"); continue
    fields,body=read_frontmatter(skill)
    if fields is None:
        fail(f"{name}: missing or malformed YAML frontmatter"); continue
    actual=fields.get('name','')
    desc=fields.get('description','')
    if actual != name: fail(f"{name}: frontmatter name '{actual}' does not match folder")
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", actual) or '--' in actual:
        fail(f"{name}: invalid skill name '{actual}'")
    if not desc: fail(f"{name}: empty description")
    if len(desc)>1024: fail(f"{name}: description exceeds 1024 characters")
    for required in ['## Mission','## Activate when','## Do not activate when','## Operating workflow']:
        if required not in body: fail(f"{name}: missing section {required}")
    for f in ['README.md','CHANGELOG.md','tests/activation-cases.json']:
        if not (folder/f).exists(): fail(f"{name}: missing {f}")
    casefile=folder/'tests/activation-cases.json'
    if casefile.exists():
        try:
            data=json.loads(casefile.read_text(encoding='utf-8'))
            if data.get('skill') != name: fail(f"{name}: activation test skill mismatch")
            if not data.get('cases'): fail(f"{name}: no activation test cases")
        except Exception as e: fail(f"{name}: invalid activation-cases.json: {e}")
    # Validate local Markdown links that point to relative files; skip anchors and URLs.
    for md in folder.rglob('*.md'):
        txt=md.read_text(encoding='utf-8')
        for target in re.findall(r"\]\(([^)]+)\)",txt):
            target=target.split('#',1)[0]
            if not target or target.startswith(('http://','https://','mailto:')): continue
            if not (md.parent/target).resolve().exists():
                warnings.append(f"{name}: unresolved relative link in {md.relative_to(folder)} -> {target}")

if not any(p.is_dir() for p in SKILLS.iterdir()): fail('No skill folders found')
print(f"Validated {checked} skill folders")
for w in warnings: print('WARNING:',w)
for e in errors: print('ERROR:',e)
if errors:
    print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)"); sys.exit(1)
print(f"PASS: {checked} skill folders; {len(warnings)} warning(s)")
