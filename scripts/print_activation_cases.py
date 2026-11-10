#!/usr/bin/env python3
"""Print the activation cases of each skill as a checklist you can paste into your own agent.

Usage: python scripts/print_activation_cases.py [skill-name]

For each case: paste the input, then check that the answer does what `must_do` says and avoids `must_not_do`.
A case with expected_activation = false should make the agent route elsewhere or refuse. Only the realistic
cases (ids starting with "realistic-") are printed unless you pass --all.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
args = [a for a in sys.argv[1:] if not a.startswith("--")]
show_all = "--all" in sys.argv
only = args[0] if args else None
count = 0
for case_file in sorted((ROOT / "skills").glob("*/tests/activation-cases.json")):
    data = json.loads(case_file.read_text(encoding="utf-8"))
    if only and data["skill"] != only:
        continue
    cases = [c for c in data["cases"] if show_all or c["id"].startswith("realistic-")]
    if not cases:
        continue
    print(f"\n## {data['skill']}")
    for c in cases:
        count += 1
        print(f"\n[{c['id']}] should activate: {'YES' if c['expected_activation'] else 'NO (route elsewhere or refuse)'}")
        print(f"  Paste: {c['input']}")
        for m in c.get("must_do", []):
            print(f"  [ ] must: {m}")
        for m in c.get("must_not_do", []):
            print(f"  [ ] must not: {m}")
print(f"\n{count} cases printed.")
