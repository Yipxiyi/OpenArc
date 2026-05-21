#!/usr/bin/env python3
"""Small OpenArc helper for plugin health checks and repository scans."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


REQUIRED_PLUGIN_FILES = [
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
]

REQUIRED_INTEGRATION_FILES = [
    "integrations/cursor/AGENTS.md",
    "integrations/cursor/openarc.mdc",
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

AGENT_GUIDE_FILES = [
    "AGENT.md",
    "AGENTS.md",
]

CORE_GOVERNANCE_FILES = [
    *AGENT_GUIDE_FILES,
    "README.md",
    "docs/PROJECT_BRIEF.md",
    "docs/CODE_STYLE.md",
    "docs/TASKS.md",
    "docs/CHANGELOG_AI.md",
]

DELIVERY_GOVERNANCE_FILES = [
    "docs/SPEC.md",
    "docs/ARCHITECTURE.md",
]

PRODUCT_GOVERNANCE_FILES = [
    "docs/PRD.md",
]

UI_BRAND_GOVERNANCE_FILES = [
    "docs/DESIGN.md",
    "docs/BRAND.md",
]

GOVERNANCE_FILES = [
    *CORE_GOVERNANCE_FILES,
    *PRODUCT_GOVERNANCE_FILES,
    *DELIVERY_GOVERNANCE_FILES,
    *UI_BRAND_GOVERNANCE_FILES,
]

OPTIONAL_PUBLIC_FILES = [
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
]

DELIVERY_GOVERNANCE_DIRS = [
    "docs/specs",
    "docs/plans",
    "docs/tasks",
]

ARCHIVE_GOVERNANCE_DIRS = [
    "docs/archive",
]

UI_BRAND_GOVERNANCE_DIRS = [
    "docs/assets",
    "docs/assets/brand",
    "docs/assets/icons",
    "docs/assets/illustrations",
    "docs/assets/screenshots",
    "docs/assets/references",
]

GOVERNANCE_DIRS = [
    *DELIVERY_GOVERNANCE_DIRS,
    *UI_BRAND_GOVERNANCE_DIRS,
    *ARCHIVE_GOVERNANCE_DIRS,
]

IGNORED_SCAN_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "target",
    "vendor",
}

SOURCE_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".go",
    ".java",
    ".js",
    ".jsx",
    ".kt",
    ".m",
    ".mm",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".sh",
    ".swift",
    ".ts",
    ".tsx",
    ".vue",
}

SCRIPT_EXTENSIONS = {
    ".js",
    ".mjs",
    ".py",
    ".rb",
    ".sh",
    ".ts",
}

APP_PACKAGE_HINTS = {
    "@angular/core",
    "@remix-run/react",
    "@sveltejs/kit",
    "astro",
    "electron",
    "expo",
    "next",
    "react",
    "react-dom",
    "solid-js",
    "svelte",
    "vite",
    "vue",
}

LIBRARY_MANIFESTS = {
    "Cargo.toml",
    "go.mod",
    "package.json",
    "Package.swift",
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
}


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
    manifest: dict[str, Any] = {}

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

    claude_manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
    if claude_manifest_path.exists():
        try:
            claude_manifest = load_json(claude_manifest_path)
        except Exception as exc:  # noqa: BLE001 - command-line diagnostic
            failures.append(f"invalid .claude-plugin/plugin.json: {exc}")
        else:
            if claude_manifest.get("name") != plugin_root.name:
                failures.append(".claude-plugin/plugin.json name must match plugin folder name")
            if not claude_manifest.get("version"):
                failures.append(".claude-plugin/plugin.json must include version")
            if claude_manifest.get("version") != manifest.get("version"):
                failures.append("Claude and Codex plugin manifest versions must match")
            warnings.extend(find_manifest_placeholders(claude_manifest))

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

    for rel_path in REQUIRED_INTEGRATION_FILES:
        if not rel_exists(plugin_root, rel_path):
            failures.append(f"missing integration file: {rel_path}")

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
    repo_profile = detect_repo_profile(repo_root)
    files = {path: rel_exists(repo_root, path) for path in GOVERNANCE_FILES}
    optional_public_files = {
        path: rel_exists(repo_root, path) for path in OPTIONAL_PUBLIC_FILES
    }
    dirs = {path: rel_exists(repo_root, path) for path in GOVERNANCE_DIRS}

    spec_count = count_files(repo_root / "docs" / "specs", "*.md")
    plan_count = count_files(repo_root / "docs" / "plans", "*.md")
    task_count = count_files(repo_root / "docs" / "tasks", "*.md")

    all_missing_files = [path for path, exists in files.items() if not exists]
    all_missing_dirs = [path for path, exists in dirs.items() if not exists]
    missing_by_group = group_missing_governance(repo_profile, repo_root, files, dirs)
    profile_missing_files = flatten_missing_files(missing_by_group)
    profile_missing_dirs = flatten_missing_directories(missing_by_group)

    payload = {
        "root": str(repo_root),
        "repo_profile": repo_profile,
        "files": files,
        "optional_public_files": optional_public_files,
        "directories": dirs,
        "counts": {
            "specs": spec_count,
            "plans": plan_count,
            "tasks": task_count,
        },
        "missing_files": profile_missing_files,
        "all_missing_files": all_missing_files,
        "profile_missing_files": profile_missing_files,
        "missing_by_group": missing_by_group,
        "missing_optional_public_files": [
            path for path, exists in optional_public_files.items() if not exists
        ],
        "missing_directories": profile_missing_dirs,
        "all_missing_directories": all_missing_dirs,
        "profile_missing_directories": profile_missing_dirs,
        "recommendation": recommend(
            repo_profile,
            repo_root,
            files,
            dirs,
            spec_count,
            plan_count,
        ),
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


def iter_repo_files(repo_root: Path, limit: int = 500) -> list[Path]:
    paths: list[Path] = []
    for current_root, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = [
            dirname for dirname in dirnames if dirname not in IGNORED_SCAN_DIRS
        ]
        base = Path(current_root)
        for filename in filenames:
            paths.append(base / filename)
            if len(paths) >= limit:
                return paths
    return paths


def detect_repo_profile(repo_root: Path) -> str:
    files = iter_repo_files(repo_root)
    relative_files = {
        path.relative_to(repo_root).as_posix()
        for path in files
        if path.is_file()
    }
    top_level_names = {path.name for path in repo_root.iterdir()} if repo_root.is_dir() else set()

    if is_plugin_repo(repo_root):
        return "plugin"
    if has_app_signal(repo_root, relative_files):
        return "app"
    if has_cli_script_signal(repo_root):
        return "script"
    if has_library_signal(top_level_names, relative_files):
        return "library"
    if has_script_signal(repo_root, files, relative_files):
        return "script"
    if has_docs_signal(files, relative_files):
        return "docs"
    return "unknown"


def is_plugin_repo(repo_root: Path) -> bool:
    if rel_exists(repo_root, ".codex-plugin/plugin.json"):
        return True
    if rel_exists(repo_root, ".claude-plugin/plugin.json"):
        return True
    skills_root = repo_root / "skills"
    if skills_root.is_dir() and any(skills_root.glob("*/SKILL.md")):
        return True
    return False


def has_app_signal(repo_root: Path, relative_files: set[str]) -> bool:
    app_paths = {
        "index.html",
        "public/index.html",
        "src/App.jsx",
        "src/App.tsx",
        "src/main.jsx",
        "src/main.tsx",
        "app/page.jsx",
        "app/page.tsx",
        "pages/index.jsx",
        "pages/index.tsx",
    }
    if relative_files.intersection(app_paths):
        return True

    package_json = repo_root / "package.json"
    if package_json.exists():
        try:
            payload = load_json(package_json)
        except Exception:  # noqa: BLE001 - invalid metadata should not abort scan
            payload = {}
        dependency_names = set()
        for key in ("dependencies", "devDependencies", "peerDependencies"):
            dependencies = payload.get(key)
            if isinstance(dependencies, dict):
                dependency_names.update(dependencies)
        if dependency_names.intersection(APP_PACKAGE_HINTS):
            return True

    return any(path.endswith((".vue", ".svelte")) for path in relative_files)


def has_cli_script_signal(repo_root: Path) -> bool:
    package_json = repo_root / "package.json"
    if package_json.exists():
        try:
            payload = load_json(package_json)
        except Exception:  # noqa: BLE001 - invalid metadata should not abort scan
            payload = {}
        if payload.get("bin"):
            return True

    pyproject = repo_root / "pyproject.toml"
    if pyproject.exists():
        text = read_text_safely(pyproject)
        if "[project.scripts]" in text or "[tool.poetry.scripts]" in text:
            return True

    setup_cfg = repo_root / "setup.cfg"
    if setup_cfg.exists() and "console_scripts" in read_text_safely(setup_cfg):
        return True

    cargo_toml = repo_root / "Cargo.toml"
    if cargo_toml.exists() and "[[bin]]" in read_text_safely(cargo_toml):
        return True

    return False


def read_text_safely(path: Path) -> str:
    try:
        return path.read_text()
    except UnicodeDecodeError:
        return ""


def has_library_signal(top_level_names: set[str], relative_files: set[str]) -> bool:
    if top_level_names.intersection(LIBRARY_MANIFESTS):
        return True
    package_markers = {
        "__init__.py",
        "lib.rs",
        "mod.rs",
    }
    return any(path.endswith(tuple(package_markers)) for path in relative_files)


def has_script_signal(
    repo_root: Path,
    files: list[Path],
    relative_files: set[str],
) -> bool:
    scripts_root = repo_root / "scripts"
    if scripts_root.is_dir():
        for path in scripts_root.rglob("*"):
            if path.is_file() and path.suffix in SCRIPT_EXTENSIONS:
                return True
    if "Makefile" in relative_files:
        return True
    runnable_files = [
        path for path in files if path.suffix in SCRIPT_EXTENSIONS and path.parent == repo_root
    ]
    return bool(runnable_files)


def has_docs_signal(files: list[Path], relative_files: set[str]) -> bool:
    markdown_count = sum(1 for path in files if path.suffix.lower() == ".md")
    source_count = sum(1 for path in files if path.suffix in SOURCE_EXTENSIONS)
    return markdown_count > 0 and source_count == 0 and (
        "README.md" in relative_files or any(path.startswith("docs/") for path in relative_files)
    )


def profile_uses_product(profile: str) -> bool:
    return profile in {"app", "unknown"}


def profile_uses_ui_brand(profile: str, repo_root: Path) -> bool:
    if profile in {"app", "unknown"}:
        return True
    if profile == "plugin":
        return has_ui_or_brand_assets(repo_root)
    return False


def has_ui_or_brand_assets(repo_root: Path) -> bool:
    asset_roots = [repo_root / "assets", repo_root / "docs" / "assets"]
    asset_extensions = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
    for asset_root in asset_roots:
        if not asset_root.is_dir():
            continue
        for path in asset_root.rglob("*"):
            if path.is_file() and path.suffix.lower() in asset_extensions:
                return True
    return False


def group_missing_governance(
    profile: str,
    repo_root: Path,
    files: dict[str, bool],
    dirs: dict[str, bool],
) -> dict[str, list[str]]:
    conditional_files: list[str] = []
    if profile_uses_product(profile):
        conditional_files.extend(PRODUCT_GOVERNANCE_FILES)
    if profile_uses_ui_brand(profile, repo_root):
        conditional_files.extend(UI_BRAND_GOVERNANCE_FILES)

    conditional_dirs = (
        UI_BRAND_GOVERNANCE_DIRS if profile_uses_ui_brand(profile, repo_root) else []
    )

    return {
        "core_files": missing_core_files(files),
        "delivery_files": missing_from(files, DELIVERY_GOVERNANCE_FILES),
        "conditional_files": missing_from(files, conditional_files),
        "archive_directories": missing_from(dirs, ARCHIVE_GOVERNANCE_DIRS),
        "delivery_directories": missing_from(dirs, DELIVERY_GOVERNANCE_DIRS),
        "conditional_directories": missing_from(dirs, conditional_dirs),
    }


def missing_from(values: dict[str, bool], paths: list[str]) -> list[str]:
    return [path for path in paths if not values.get(path)]


def missing_core_files(files: dict[str, bool]) -> list[str]:
    missing: list[str] = []
    if not any(files.get(path) for path in AGENT_GUIDE_FILES):
        missing.extend(AGENT_GUIDE_FILES)
    missing.extend(
        missing_from(
            files,
            [
                path
                for path in CORE_GOVERNANCE_FILES
                if path not in AGENT_GUIDE_FILES
            ],
        )
    )
    return missing


def flatten_missing_files(missing_by_group: dict[str, list[str]]) -> list[str]:
    files: list[str] = []
    for key in ("core_files", "delivery_files", "conditional_files"):
        files.extend(missing_by_group[key])
    return files


def flatten_missing_directories(missing_by_group: dict[str, list[str]]) -> list[str]:
    directories: list[str] = []
    for key in ("archive_directories", "delivery_directories", "conditional_directories"):
        directories.extend(missing_by_group[key])
    return directories


def recommend(
    profile: str,
    repo_root: Path,
    files: dict[str, bool],
    dirs: dict[str, bool],
    spec_count: int,
    plan_count: int,
) -> str:
    if not files.get("AGENT.md") and not files.get("AGENTS.md"):
        return "Start with repository-governance and create a profile-aware agent guide."
    if profile == "script" and not files.get("README.md"):
        return "Create or update a README/runbook that explains how to run, configure, and validate the scripts."
    if not files.get("docs/CHANGELOG_AI.md") or not dirs.get("docs/archive"):
        return "Use change-archive-governance to set up AI change memory and archive policy."
    if profile_uses_product(profile) and not files.get("docs/PRD.md"):
        return "Use product-governance to clarify and create docs/PRD.md."
    if profile_uses_ui_brand(profile, repo_root) and not files.get("docs/DESIGN.md"):
        return "Use design-governance to create docs/DESIGN.md."
    if profile_uses_ui_brand(profile, repo_root) and not files.get("docs/BRAND.md"):
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
    print(f"Repo profile: `{payload['repo_profile']}`")
    print()
    print("## Known Governance Files")
    for path, exists in payload["files"].items():
        mark = "ok" if exists else "missing"
        print(f"- {mark}: `{path}`")
    print()
    print("## Profile-Relevant Missing Files")
    for group, paths in payload["missing_by_group"].items():
        if not paths:
            continue
        print(f"- {group}: {', '.join(f'`{path}`' for path in paths)}")
    print()
    print("## Optional Public Files")
    for path, exists in payload["optional_public_files"].items():
        mark = "ok" if exists else "optional"
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
