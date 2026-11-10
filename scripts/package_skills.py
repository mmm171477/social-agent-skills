#!/usr/bin/env python3
"""Package each standalone Skill and the full community suite."""
from pathlib import Path
import argparse, zipfile, shutil
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--out',default='dist')
args=parser.parse_args()
out=(ROOT/args.out).resolve(); out.mkdir(parents=True,exist_ok=True)
skills=ROOT/'skills'
for folder in sorted(p for p in skills.iterdir() if p.is_dir()):
    target=out/f'{folder.name}-v0.2.0.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for f in folder.rglob('*'):
            if f.is_file(): z.write(f, Path(folder.name)/f.relative_to(folder))
        z.write(ROOT/'LICENSE','LICENSE')
    print(target)
# Community bundle excludes commercial-kit by design.
target=out/'social-agent-skills-community-v0.2.0.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for folder in [skills,ROOT/'docs',ROOT/'templates',ROOT/'scripts']:
        for f in folder.rglob('*'):
            if f.is_file() and '__pycache__' not in f.parts: z.write(f,f.relative_to(ROOT))
    for f in ['README.md','LICENSE','CHANGELOG.md','CONTRIBUTING.md','SECURITY.md','CODE_OF_CONDUCT.md']:
        z.write(ROOT/f,f)
print(target)
