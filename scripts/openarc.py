#!/usr/bin/env python3
"""Small OpenArc helper for plugin health checks and repository scans."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_PLUGIN_FILES = [
    ".codex-plugin/plugin.json",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
]

REQUIRED_TEMPLATES = [
    "AGENT.template.md",
    "PRD.template.md",
    "DESIGN.template.md",
    "BRAND.template.md",
    "SPEC.template.md",
    "PLAN.template.md",
    "TASKS.template.md",
    "RELEASE.template.md",
    "MIGRATION.template.md",
    "CHANGELOG_AI.template.md",
    "ARCHIVE_INDEX.template.md",
]

GOVERNANCE_FILES = [
    "AGENT.md",
    "AGENTS.md",
    "docs/PROJECT_BRIEF.md",
    "docs/CODE_STYLE.md",
    "docs/TASKS.md",
    "docs/PRD.md",
    "docs/SPEC.md",
    "docs/ARCHITECTURE.md",
    "docs/DESIGN.md",
    "docs/BRAND.md",
    "docs/CHANGELOG_AI.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
]

GOVERNANCE_DIRS = [
    "docs/specs",
    "docs/plans",
    "docs/tasks",
    "docs/assets",
    "docs/archive",
    "docs/assets/brand",
    "docs/assets/icons",
    "docs/assets/illustrations",
    "docs/assets/screenshots",
    "docs/assets/references",
]


def rel_exists(root: Path, rel_path: str) -> bool:
    return (root / rel_path).exists()


def load_json(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return payload


def parse_skill_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    _, block, _ = text.split("---", 2)
    fields: dict[str, str] = {}
    for raw_line in block.splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def doctor(plugin_root: Path) -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for rel_path in REQUIRED_PLUGIN_FILES:
        if not rel_exists(plugin_root, rel_path):
            failures.append(f"missing required file: {rel_path}")

    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    if manifest_path.exists():
        try:
            manifest = load_json(manifest_path)
        except Exception as exc:  # noqa: BLE001 - command-line diagnostic
            failures.append(f"invalid plugin.json: {exc}")
        else:
            if manifest.get("name") != plugin_root.name:
                failures.append("plugin.json name must match plugin folder name")
            if manifest.get("license") == "[TODO: MIT]":
                failures.append("plugin.json license still has placeholder value")
            if manifest.get("skills") != "./skills/":
                failures.append("plugin.json skills should be ./skills/")
            warnings.extend(find_manifest_placeholders(manifest))

    skills_root = plugin_root / "skills"
    if not skills_root.exists():
        failures.append("missing skills directory")
    else:
        skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
        if not skill_dirs:
            failures.append("skills directory has no skill folders")
        for skill_dir in skill_dirs:
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                failures.append(f"missing SKILL.md: skills/{skill_dir.name}")
                continue
            fields = parse_skill_frontmatter(skill_md)
            if fields.get("name") != skill_dir.name:
                failures.append(f"skill name mismatch: skills/{skill_dir.name}")
            if not fields.get("description", "").startswith("Use when"):
                failures.append(f"description should start with 'Use when': skills/{skill_dir.name}")

    for template in REQUIRED_TEMPLATES:
        if not rel_exists(plugin_root, f"templates/{template}"):
            failures.append(f"missing template: {template}")

    if failures:
        print("OpenArc doctor: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("OpenArc doctor: PASS")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    return 0


def find_manifest_placeholders(manifest: dict[str, Any]) -> list[str]:
    warnings: list[str] = []

    def visit(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, nested in value.items():
                visit(nested, f"{path}.{key}" if path else key)
        elif isinstance(value, list):
            for index, nested in enumerate(value):
                visit(nested, f"{path}[{index}]")
        elif isinstance(value, str) and "[TODO:" in value:
            warnings.append(f"manifest placeholder remains at {path}")

    visit(manifest, "")
    return warnings


def scan(repo_root: Path, output_format: str) -> int:
    files = {path: rel_exists(repo_root, path) for path in GOVERNANCE_FILES}
    dirs = {path: rel_exists(repo_root, path) for path in GOVERNANCE_DIRS}

    spec_count = count_files(repo_root / "docs" / "specs", "*.md")
    plan_count = count_files(repo_root / "docs" / "plans", "*.md")
    task_count = count_files(repo_root / "docs" / "tasks", "*.md")

    missing_files = [path for path, exists in files.items() if not exists]
    missing_dirs = [path for path, exists in dirs.items() if not exists]

    payload = {
        "root": str(repo_root),
        "files": files,
        "directories": dirs,
        "counts": {
            "specs": spec_count,
            "plans": plan_count,
            "tasks": task_count,
        },
        "missing_files": missing_files,
        "missing_directories": missing_dirs,
        "recommendation": recommend(files, dirs, spec_count, plan_count),
    }

    if output_format == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print_markdown_scan(payload)
    return 0


def count_files(path: Path, pattern: str) -> int:
    if not path.exists() or not path.is_dir():
        return 0
    return sum(1 for _ in path.glob(pattern))


def recommend(
    files: dict[str, bool],
    dirs: dict[str, bool],
    spec_count: int,
    plan_count: int,
) -> str:
    if not files.get("AGENT.md") and not files.get("AGENTS.md"):
        return "Start with repository-governance and create an agent guide."
    if not files.get("docs/CHANGELOG_AI.md") or not dirs.get("docs/archive"):
        return "Use change-archive-governance to set up AI change memory and archive policy."
    if not files.get("docs/PRD.md"):
        return "Use product-governance to clarify and create docs/PRD.md."
    if not files.get("docs/DESIGN.md"):
        return "Use design-governance to create docs/DESIGN.md."
    if not files.get("docs/BRAND.md"):
        return "Use brand-governance to create docs/BRAND.md."
    if not dirs.get("docs/specs") or spec_count == 0:
        return "Use spec-workflow for the next non-trivial change."
    if not dirs.get("docs/plans") or plan_count == 0:
        return "Use planning-engine before implementation."
    return "Governance baseline exists; use implementation-workflow for changes."


def print_markdown_scan(payload: dict[str, Any]) -> None:
    print("# OpenArc Scan")
    print()
    print(f"Root: `{payload['root']}`")
    print()
    print("## Files")
    for path, exists in payload["files"].items():
        mark = "ok" if exists else "missing"
        print(f"- {mark}: `{path}`")
    print()
    print("## Directories")
    for path, exists in payload["directories"].items():
        mark = "ok" if exists else "missing"
        print(f"- {mark}: `{path}`")
    print()
    print("## Counts")
    for name, count in payload["counts"].items():
        print(f"- {name}: {count}")
    print()
    print("## Recommendation")
    print(payload["recommendation"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OpenArc helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor_parser = subparsers.add_parser("doctor", help="Validate an OpenArc plugin directory")
    doctor_parser.add_argument("plugin_root", nargs="?", default=".")

    scan_parser = subparsers.add_parser("scan", help="Scan a repository for OpenArc governance files")
    scan_parser.add_argument("repo_root", nargs="?", default=".")
    scan_parser.add_argument("--format", choices=["markdown", "json"], default="markdown")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "doctor":
        return doctor(Path(args.plugin_root).resolve())
    if args.command == "scan":
        return scan(Path(args.repo_root).resolve(), args.format)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
