import json
import re
import unittest
import tempfile
import shutil
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("install_skills", ROOT / "scripts" / "install_skills.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class SkillPackageTests(unittest.TestCase):
    def test_all_skills_have_frontmatter_and_unique_names(self):
        names=[]
        for folder in (ROOT/'skills').iterdir():
            if not folder.is_dir(): continue
            text=(folder/'SKILL.md').read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\n'), folder.name)
            m=re.search(r'^name: (.+)$', text, re.M)
            self.assertIsNotNone(m, folder.name)
            names.append(m.group(1).strip())
            self.assertEqual(m.group(1).strip(), folder.name)
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(names), 7)

    def test_behavioral_cases_are_valid_json(self):
        for path in (ROOT/'skills').glob('*/tests/activation-cases.json'):
            data=json.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(data['skill'], path.parents[1].name)
            self.assertGreaterEqual(len(data['cases']), 3)
            for case in data['cases']:
                self.assertIn('expected_activation', case)
                self.assertIn('input', case)

    def test_installer_skips_existing_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            source = tmp / "source"
            destination = tmp / "destination"
            (source / "instagram-agent").mkdir(parents=True)
            (source / "instagram-agent" / "SKILL.md").write_text("new", encoding="utf-8")
            (destination / "instagram-agent").mkdir(parents=True)
            (destination / "instagram-agent" / "SKILL.md").write_text("existing", encoding="utf-8")
            result = installer.install_skills(source, destination, "instagram-agent", False)
            self.assertEqual(result[0][1], "skipped-existing")
            self.assertEqual((destination / "instagram-agent" / "SKILL.md").read_text(), "existing")

    def test_installer_overwrite_makes_backup(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            source = tmp / "source"
            destination = tmp / "destination"
            (source / "instagram-agent").mkdir(parents=True)
            (source / "instagram-agent" / "SKILL.md").write_text("new", encoding="utf-8")
            (destination / "instagram-agent").mkdir(parents=True)
            (destination / "instagram-agent" / "SKILL.md").write_text("old", encoding="utf-8")
            result = installer.install_skills(source, destination, "instagram-agent", True)
            self.assertEqual(result[0][1], "installed")
            self.assertEqual((destination / "instagram-agent" / "SKILL.md").read_text(), "new")
            backups = list(destination.glob("instagram-agent.backup-*"))
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0] / "SKILL.md").read_text(), "old")

    def test_required_docs_exist(self):
        for folder in (ROOT/'skills').iterdir():
            if folder.is_dir():
                for rel in ['README.md','CHANGELOG.md','references','examples','tests']:
                    self.assertTrue((folder/rel).exists(), f'{folder.name}: {rel}')

if __name__ == '__main__':
    unittest.main()
