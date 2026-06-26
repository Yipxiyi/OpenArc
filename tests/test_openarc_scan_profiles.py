import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
OPENARC = PLUGIN_ROOT / "scripts" / "openarc.py"


def run_scan(repo_root: Path) -> dict:
    result = subprocess.run(
        [sys.executable, str(OPENARC), "scan", str(repo_root), "--format", "json"],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


class ScanProfileTests(unittest.TestCase):
    def test_doctor_requires_clarification_gate_and_code_style_template(self) -> None:
        skill = PLUGIN_ROOT / "skills" / "clarification-gate" / "SKILL.md"
        template = PLUGIN_ROOT / "templates" / "CODE_STYLE.template.md"

        self.assertTrue(skill.exists())
        self.assertTrue(template.exists())

        text = skill.read_text()
        self.assertIn("name: clarification-gate", text)
        self.assertIn("description: Use when", text)

        result = subprocess.run(
            [sys.executable, str(OPENARC), "doctor", str(PLUGIN_ROOT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("OpenArc doctor: PASS", result.stdout)

    def test_script_repo_does_not_recommend_design_or_brand_governance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts = root / "scripts"
            scripts.mkdir()
            (scripts / "run_report.py").write_text("print('ok')\n")

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "script")
        self.assertIn("missing_by_group", payload)
        self.assertNotIn("docs/DESIGN.md", payload["missing_by_group"]["core_files"])
        self.assertNotIn("docs/BRAND.md", payload["missing_by_group"]["core_files"])
        self.assertNotIn("docs/DESIGN.md", payload["missing_files"])
        self.assertNotIn("docs/BRAND.md", payload["missing_files"])
        self.assertIn("docs/DESIGN.md", payload["all_missing_files"])
        self.assertIn("docs/BRAND.md", payload["all_missing_files"])
        self.assertNotIn("design-governance", payload["recommendation"])
        self.assertNotIn("brand-governance", payload["recommendation"])

    def test_app_repo_recommends_design_governance_when_ui_rules_are_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENT.md").write_text("# Agent\n")
            (root / "README.md").write_text("# App\n")
            docs = root / "docs"
            docs.mkdir()
            (docs / "CHANGELOG_AI.md").write_text("# AI Changelog\n")
            (docs / "PRD.md").write_text("# PRD\n")
            (docs / "archive").mkdir()
            (root / "package.json").write_text(
                json.dumps({"dependencies": {"react": "^19.0.0", "vite": "^6.0.0"}})
            )
            src = root / "src"
            src.mkdir()
            (src / "App.tsx").write_text("export default function App() { return null }\n")

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "app")
        self.assertNotIn("AGENTS.md", payload["missing_files"])
        self.assertIn("docs/CODE_STYLE.md", payload["missing_by_group"]["core_files"])
        self.assertIn("docs/DESIGN.md", payload["missing_by_group"]["conditional_files"])
        self.assertIn("design-governance", payload["recommendation"])

    def test_cli_package_repo_is_treated_as_script_governance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text(
                json.dumps({"bin": {"openarc-demo": "./bin/openarc-demo.js"}})
            )
            bin_dir = root / "bin"
            bin_dir.mkdir()
            (bin_dir / "openarc-demo.js").write_text("#!/usr/bin/env node\n")

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "script")
        self.assertEqual(payload["missing_by_group"]["conditional_files"], [])

    def test_plugin_repo_is_detected_without_breaking_doctor(self) -> None:
        payload = run_scan(PLUGIN_ROOT)

        self.assertEqual(payload["repo_profile"], "plugin")

        result = subprocess.run(
            [sys.executable, str(OPENARC), "doctor", str(PLUGIN_ROOT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("OpenArc doctor: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
