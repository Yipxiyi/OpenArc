import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.openarc import iter_repo_files


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


def run_markdown_scan(repo_root: Path) -> str:
    result = subprocess.run(
        [sys.executable, str(OPENARC), "scan", str(repo_root)],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


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

    def test_doctor_accepts_versioned_codex_cache_root(self) -> None:
        version = json.loads(
            (PLUGIN_ROOT / ".codex-plugin/plugin.json").read_text()
        )["version"]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "openarc" / version
            shutil.copytree(
                PLUGIN_ROOT,
                root,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            result = subprocess.run(
                [sys.executable, str(OPENARC), "doctor", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )

        self.assertIn("OpenArc doctor: PASS", result.stdout)

    def test_scan_rejects_missing_or_non_directory_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            file_path = root / "file"
            file_path.write_text("not a repo\n")
            for invalid_path, message in (
                (root / "missing", "does not exist"),
                (file_path, "is not a directory"),
            ):
                result = subprocess.run(
                    [sys.executable, str(OPENARC), "scan", str(invalid_path)],
                    capture_output=True,
                    text=True,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn(message, result.stderr)

    def test_doctor_rejects_missing_skill_asset_and_malformed_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "openarc"
            shutil.copytree(
                PLUGIN_ROOT,
                root,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            shutil.rmtree(root / "skills" / "clarification-gate")
            (root / "assets" / "openarc_icon.png").unlink()
            (root / "skills" / "openarc" / "SKILL.md").write_text(
                "---\nname: openarc\ndescription: Use when broken\n"
            )

            result = subprocess.run(
                [sys.executable, str(OPENARC), "doctor", str(root)],
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("missing required skill: skills/clarification-gate/SKILL.md", result.stdout)
        self.assertIn("missing manifest asset: ./assets/openarc_icon.png", result.stdout)
        self.assertIn("skill name mismatch: skills/openarc", result.stdout)

    def test_doctor_rejects_non_semver_manifest_versions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "openarc"
            shutil.copytree(
                PLUGIN_ROOT,
                root,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            for rel_path in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
                path = root / rel_path
                manifest = json.loads(path.read_text())
                manifest["version"] = "banana"
                path.write_text(json.dumps(manifest))

            result = subprocess.run(
                [sys.executable, str(OPENARC), "doctor", str(root)],
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("plugin.json version must be valid SemVer", result.stdout)
        self.assertIn(".claude-plugin/plugin.json version must be valid SemVer", result.stdout)

    def test_doctor_rejects_marketplace_ref_version_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "openarc"
            shutil.copytree(
                PLUGIN_ROOT,
                root,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            path = root / ".agents" / "plugins" / "marketplace.json"
            marketplace = json.loads(path.read_text())
            marketplace["plugins"][0]["source"]["ref"] = "v0.6.2"
            path.write_text(json.dumps(marketplace))

            result = subprocess.run(
                [sys.executable, str(OPENARC), "doctor", str(root)],
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "marketplace plugin ref must match plugin version: v0.7.0",
            result.stdout,
        )

    def test_script_repo_does_not_recommend_design_or_brand_governance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scripts = root / "scripts"
            scripts.mkdir()
            (scripts / "run_report.py").write_text("print('ok')\n")

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "script")
        self.assertIn("required", payload)
        self.assertIn("relevant", payload)
        self.assertIn("optional", payload)
        self.assertIn("missing_by_group", payload)
        self.assertNotIn("docs/DESIGN.md", payload["relevant"]["files"])
        self.assertNotIn("docs/BRAND.md", payload["relevant"]["files"])
        self.assertFalse(payload["optional"]["files"]["docs/DESIGN.md"])
        self.assertFalse(payload["optional"]["files"]["docs/BRAND.md"])
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
            (docs / "CODE_STYLE.md").write_text("# Code Style\n")
            (docs / "PROJECT_BRIEF.md").write_text("# Project\n")
            (docs / "TASKS.md").write_text("# Tasks\n")
            (docs / "ARCHITECTURE.md").write_text("# Architecture\n")
            (docs / "archive").mkdir()
            (docs / "specs").mkdir()
            (docs / "plans").mkdir()
            (root / "package.json").write_text(
                json.dumps({"dependencies": {"react": "^19.0.0", "vite": "^6.0.0"}})
            )
            src = root / "src"
            src.mkdir()
            (src / "App.tsx").write_text("export default function App() { return null }\n")

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "app")
        self.assertNotIn("AGENTS.md", payload["missing_files"])
        self.assertIn("docs/DESIGN.md", payload["relevant"]["files"])
        self.assertNotIn("docs/BRAND.md", payload["relevant"]["files"])
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
        self.assertNotIn("docs/PRD.md", payload["relevant"]["files"])

    def test_plugin_repo_is_detected_without_breaking_doctor(self) -> None:
        payload = run_scan(PLUGIN_ROOT)

        self.assertEqual(payload["repo_profile"], "plugin")
        self.assertNotIn("docs/DESIGN.md", payload["relevant"]["files"])
        self.assertNotIn("docs/BRAND.md", payload["relevant"]["files"])

        result = subprocess.run(
            [sys.executable, str(OPENARC), "doctor", str(PLUGIN_ROOT)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("OpenArc doctor: PASS", result.stdout)

    def test_canonical_delivery_sources_do_not_include_legacy_spec_or_task_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs"
            docs.mkdir()
            (docs / "TASKS.md").write_text("# Tasks\n")

            payload = run_scan(root)

        self.assertNotIn("docs/SPEC.md", payload["files"])
        self.assertNotIn("docs/tasks", payload["directories"])
        self.assertIn("docs/specs", payload["directories"])
        self.assertIn("docs/plans", payload["directories"])
        self.assertEqual(payload["counts"]["tasks"], 1)

    def test_unknown_profile_uses_only_the_minimum_required_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data.bin").write_bytes(b"data")

            payload = run_scan(root)
            markdown = run_markdown_scan(root)

        self.assertEqual(payload["repo_profile"], "unknown")
        self.assertEqual(payload["relevant"]["files"], {})
        self.assertEqual(payload["relevant"]["directories"], {})
        self.assertEqual(
            payload["missing_files"],
            ["AGENT.md or AGENTS.md", "README.md"],
        )
        self.assertNotIn("docs/PRD.md", markdown)
        self.assertNotIn("docs/DESIGN.md", markdown)
        self.assertIn("## Optional (present only)", markdown)

    def test_vite_alone_is_not_an_app_signal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text(
                json.dumps({"devDependencies": {"vite": "^6.0.0"}})
            )

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "library")
        self.assertNotIn("docs/DESIGN.md", payload["relevant"]["files"])

    def test_plugin_images_do_not_imply_design_or_brand_governance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_dir = root / ".codex-plugin"
            manifest_dir.mkdir()
            (manifest_dir / "plugin.json").write_text("{}\n")
            assets = root / "assets"
            assets.mkdir()
            (assets / "icon.png").write_bytes(b"png")

            payload = run_scan(root)

        self.assertEqual(payload["repo_profile"], "plugin")
        self.assertNotIn("docs/DESIGN.md", payload["relevant"]["files"])
        self.assertNotIn("docs/BRAND.md", payload["relevant"]["files"])

    def test_explicit_brand_assets_do_not_trigger_design_governance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# Docs\n")
            brand = root / "docs" / "assets" / "brand"
            brand.mkdir(parents=True)
            (brand / "wordmark.svg").write_text("<svg/>\n")

            payload = run_scan(root)

        self.assertIn("docs/BRAND.md", payload["relevant"]["files"])
        self.assertNotIn("docs/DESIGN.md", payload["relevant"]["files"])

    def test_repository_walk_is_complete_and_sorted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for index in range(600):
                (root / f"file-{index:03}.txt").write_text("x\n")
            src = root / "src"
            src.mkdir()
            (src / "App.tsx").write_text("export default null\n")

            paths = iter_repo_files(root)
            payload = run_scan(root)

        self.assertEqual(paths, sorted(paths))
        self.assertEqual(len(paths), 601)
        self.assertEqual(payload["repo_profile"], "app")

    def test_recommendation_does_not_claim_baseline_with_relevant_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "AGENT.md").write_text("# Agent\n")
            (root / "README.md").write_text("# Script\n")
            (root / "run.py").write_text("print('ok')\n")

            payload = run_scan(root)

        self.assertTrue(payload["missing_by_group"]["relevant_files"])
        self.assertEqual(
            set(payload["relevant"]["files"]),
            {"docs/PROJECT_BRIEF.md", "docs/CODE_STYLE.md"},
        )
        self.assertEqual(payload["relevant"]["directories"], {})
        self.assertNotIn("baseline exists", payload["recommendation"])
        self.assertNotIn("archive", payload["recommendation"])
        self.assertNotIn("spec", payload["recommendation"])
        self.assertNotIn("plan", payload["recommendation"])

    def test_csharp_source_prevents_docs_only_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("# C# project\n")
            (root / "Program.cs").write_text("class Program {}\n")

            payload = run_scan(root)

        self.assertNotEqual(payload["repo_profile"], "docs")

    def test_similar_python_filename_is_not_a_package_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "not__init__.py").write_text("print('ok')\n")

            payload = run_scan(root)

        self.assertNotEqual(payload["repo_profile"], "library")

    def test_workflow_contracts_stay_lightweight_and_canonical(self) -> None:
        clarification = (PLUGIN_ROOT / "skills/clarification-gate/SKILL.md").read_text()
        implementation = (PLUGIN_ROOT / "skills/implementation-workflow/SKILL.md").read_text()
        spec = (PLUGIN_ROOT / "skills/spec-workflow/SKILL.md").read_text()
        spec_template = (PLUGIN_ROOT / "templates/SPEC.template.md").read_text()

        self.assertIn("Ask 0-5 questions", clarification)
        self.assertIn("continue in the same turn", clarification)
        self.assertIn("### Routine Work", implementation)
        self.assertIn("Do not create or patch an agent guide", implementation)
        self.assertIn("stable, descriptive kebab-case slug", spec)
        self.assertNotIn("<version>", spec_template)
        self.assertNotIn("## Implementation Plan", spec_template)
        self.assertNotIn("## Tasks", spec_template)

        active_contract = "\n".join(
            path.read_text()
            for root in ("skills", "templates", "integrations", "examples")
            for path in (PLUGIN_ROOT / root).rglob("*.md")
        )
        self.assertNotIn("docs/SPEC.md", active_contract)
        self.assertNotIn("docs/tasks", active_contract)
        self.assertNotIn("Allowed range: 3-7", active_contract)


if __name__ == "__main__":
    unittest.main()
