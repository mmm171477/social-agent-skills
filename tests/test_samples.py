"""Checks the documented trials and the samples: guides exist, every skill has realistic sample prompts and activation
cases, the installer trial behaves as written, and (Pro only) the filled kit samples match the templates."""
import csv
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def run(*args):
    return subprocess.run([sys.executable, "-I", *map(str, args)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")


class SampleTests(unittest.TestCase):
    def test_guides_exist(self):
        for f in ["docs/BENEFITS.md", "docs/HOW-TO-USE.md", "TRY-IT.md", "scripts/print_activation_cases.py"]:
            self.assertTrue((ROOT / f).exists(), f)
        trials = (ROOT / "TRY-IT.md").read_text(encoding="utf-8")
        for t in ["Trial 1", "Trial 2", "Trial 3", "Trial 4"]:
            self.assertIn(t, trials)

    def test_every_skill_has_realistic_sample_prompts(self):
        for p in SKILLS:
            text = (p / "examples" / "sample-prompts.md").read_text(encoding="utf-8")
            self.assertGreaterEqual(len(re.findall(r"^## \d+\. ", text, re.M)), 3, p.name)
            self.assertGreaterEqual(len(re.findall(r"^### ", text, re.M)), 2, p.name + " boundary prompts")
            self.assertIn("A good answer contains:", text)

    def test_every_skill_has_realistic_activation_cases(self):
        for p in SKILLS:
            data = json.loads((p / "tests" / "activation-cases.json").read_text(encoding="utf-8"))
            real = [c for c in data["cases"] if c["id"].startswith("realistic-")]
            self.assertGreaterEqual(sum(c["expected_activation"] for c in real), 2, p.name)
            self.assertGreaterEqual(sum(not c["expected_activation"] for c in real), 2, p.name)
            for c in real:
                self.assertGreater(len(c["input"].split()), 5, "a realistic case is a full request, not a keyword")

    def test_sample_prompts_match_the_activation_cases(self):
        for p in SKILLS:
            prompts = (p / "examples" / "sample-prompts.md").read_text(encoding="utf-8")
            data = json.loads((p / "tests" / "activation-cases.json").read_text(encoding="utf-8"))
            for c in (c for c in data["cases"] if c["id"].startswith("realistic-")):
                self.assertIn(c["input"], prompts, f"{p.name}: case {c['id']} is not in the sample prompts")

    def test_print_activation_cases_covers_all_skills(self):
        r = run("scripts/print_activation_cases.py")
        self.assertEqual(r.returncode, 0, r.stderr)
        for p in SKILLS:
            self.assertIn(f"## {p.name}", r.stdout)
        self.assertIn("should activate: YES", r.stdout)
        self.assertIn("should activate: NO", r.stdout)

    def test_install_trial_behaves_as_documented(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = run("scripts/install_skills.py", "--target", "project", "--project-root", tmp, "--skill", "youtube-agent")
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            self.assertTrue((Path(tmp) / ".claude" / "skills" / "youtube-agent" / "SKILL.md").exists())
            second = run("scripts/install_skills.py", "--target", "project", "--project-root", tmp, "--skill", "youtube-agent")
            self.assertIn("skipped", (second.stdout + second.stderr).lower())

    def test_pro_kit_samples_match_the_templates(self):
        kit = ROOT / "commercial-kit"
        if not kit.exists():
            self.skipTest("Community edition has no commercial kit")
        for name in ["content-calendar", "platform-qa-scorecard"]:
            tpl = read_csv(kit / f"{name}.csv")[0]
            filled = read_csv(kit / "samples" / f"filled-{name}.csv")
            self.assertEqual(tpl, filled[0], name + " header")
            self.assertGreaterEqual(len(filled), 4, name + " has sample rows")
            self.assertTrue(all(len(r) == len(tpl) for r in filled), name + " rows have the right number of columns")
        labels = re.findall(r"^- ([^:]+):", (kit / "campaign-brief.md").read_text(encoding="utf-8"), re.M)
        brief = (kit / "samples" / "filled-campaign-brief.md").read_text(encoding="utf-8")
        for label in labels:
            self.assertIn(f"- {label}:", brief, f"filled brief lacks '{label}'")
        self.assertTrue((kit / "HOW-TO-USE.md").exists())


if __name__ == "__main__":
    unittest.main()
