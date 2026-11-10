"""Guard against copy-paste skills: per-skill README, example and changelog must be distinct,
and every platform skill must ship a real playbook."""
import re
import unittest
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
N = 6                    # words per shingle
MAX_OVERLAP = 0.30       # per pair of skills, per file kind
MIN_PLAYBOOK_CHARS = 1200


def shingles(text):
    words = re.sub(r"[^\w\s]", " ", text.lower()).split()
    return {" ".join(words[i:i + N]) for i in range(max(0, len(words) - N + 1))}


def overlap(a, b):
    sa, sb = shingles(a), shingles(b)
    return len(sa & sb) / max(1, min(len(sa), len(sb)))


class DistinctnessTests(unittest.TestCase):
    def check_kind(self, relpath, limit=MAX_OVERLAP):
        texts = {p.name: (p / relpath).read_text(encoding="utf-8") for p in SKILLS}
        for (n1, t1), (n2, t2) in combinations(texts.items(), 2):
            ratio = overlap(t1, t2)
            self.assertLess(ratio, limit, f"{relpath}: {n1} vs {n2} overlap {ratio:.0%}")

    def test_readmes_are_distinct(self):
        self.check_kind("README.md")

    def test_examples_are_distinct(self):
        self.check_kind("examples/sample-workflow.md")

    def test_changelogs_are_distinct(self):
        # Release notes share a fixed structure ("Added ... playbook", "Activation tests for ..."),
        # so the limit is looser; the bullets that describe each skill's own workflow must still differ.
        self.check_kind("CHANGELOG.md", limit=0.5)

    def test_every_skill_has_a_substantial_playbook(self):
        for p in SKILLS:
            pb = p / "references" / "playbook.md"
            self.assertTrue(pb.exists(), f"{p.name}: missing references/playbook.md")
            self.assertGreaterEqual(len(pb.read_text(encoding="utf-8")), MIN_PLAYBOOK_CHARS, p.name)


if __name__ == "__main__":
    unittest.main()
