#!/usr/bin/env python3
"""Install selected Agent Skills to a project or user Claude Code directory."""
from pathlib import Path
import argparse
import shutil
from datetime import datetime


def install_skills(source: Path, destination: Path, selected=None, overwrite=False):
    source = source.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    folders = sorted(p for p in source.iterdir() if p.is_dir())
    if selected:
        folders = [p for p in folders if p.name == selected]
        if not folders:
            raise ValueError(f"Skill not found: {selected}")
    results=[]
    for folder in folders:
        target=destination/folder.name
        if target.exists():
            if not overwrite:
                results.append((folder.name, 'skipped-existing', str(target)))
                continue
            stamp=datetime.now().strftime('%Y%m%d-%H%M%S-%f')
            backup=destination/f'{folder.name}.backup-{stamp}'
            shutil.copytree(target, backup)
            shutil.rmtree(target)
        shutil.copytree(folder, target)
        results.append((folder.name, 'installed', str(target)))
    return results


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=['project','user'], default='project')
    parser.add_argument('--project-root', type=Path, default=Path.cwd())
    parser.add_argument('--skill', help='Install one named skill; omit to install all')
    parser.add_argument('--overwrite', action='store_true', help='Back up and replace existing skill folders')
    args=parser.parse_args()
    source=Path(__file__).resolve().parents[1]/'skills'
    if args.target == 'project':
        root=args.project_root.expanduser().resolve()
        if not root.exists() or not root.is_dir():
            parser.error(f'Project root does not exist or is not a directory: {root}')
        destination=root/'.claude'/'skills'
    else:
        destination=Path.home()/'.claude'/'skills'
    try:
        for name,status,path in install_skills(source,destination,args.skill,args.overwrite):
            print(f'{status}: {name} -> {path}')
    except Exception as exc:
        parser.error(str(exc))
    print(f'Destination: {destination}')

if __name__ == '__main__':
    main()
