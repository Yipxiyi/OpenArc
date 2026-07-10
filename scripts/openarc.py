#!/usr/bin/env python3
"""Small OpenArc helper for plugin health checks and repository scans."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_PLUGIN_FILES = [
    ".agents/plugins/marketplace.json",
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

REQUIRED_SKILLS = [
    "assets-governance",
    "brand-governance",
    "change-archive-governance",
    "clarification-gate",
    "design-governance",
    "implementation-workflow",
    "open-source-maintenance",
    "openarc",
    "planning-engine",
    "product-governance",
    "release-workflow",
    "repository-governance",
    "spec-workflow",
    "version-governance",
    "workspace-migration",
]

REQUIRED_TEMPLATES = [
    "AGENT.template.md",
    "CODE_STYLE.template.md",
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

AGENT_GUIDE_REQUIREMENT = "AGENT.md or AGENTS.md"

CORE_GOVERNANCE_FILES = [
    *AGENT_GUIDE_FILES,
    "README.md",
    "docs/PROJECT_BRIEF.md",
    "docs/CODE_STYLE.md",
    "docs/TASKS.md",
    "docs/CHANGELOG_AI.md",
]

DELIVERY_GOVERNANCE_FILES = [
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
    ".cs",
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
    "vue",
}

APP_ENTRY_PATHS = {
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

RELEVANT_CORE_FILES = [
    "docs/PROJECT_BRIEF.md",
    "docs/CODE_STYLE.md",
]

LIBRARY_MANIFESTS = {
    "Cargo.toml",
    "go.mod",
    "package.json",
    "Package.swift",
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
}

SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)

OPENARC_REPOSITORY_URL = "https://github.com/Yipxiyi/OpenArc.git"


def rel_exists(root: Path, rel_path: str) -> bool:
    return (root / rel_path).exists()


def load_json(path: Path) -> dict[str, Any]:
    with path.open() as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return payload


def is_semver(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    match = SEMVER_PATTERN.fullmatch(value)
    if not match:
        return False
    prerelease = match.group(4)
    return not prerelease or all(
        not (part.isdigit() and len(part) > 1 and part.startswith("0"))
        for part in prerelease.split(".")
    )


def manifest_matches_plugin_root(plugin_root: Path, manifest: dict[str, Any]) -> bool:
    name = manifest.get("name")
    version = manifest.get("version")
    if not isinstance(name, str) or not name:
        return False
    if plugin_root.name.lower() == name.lower():
        return True
    return (
        is_semver(version)
        and plugin_root.name == version
        and plugin_root.parent.name.lower() == name.lower()
    )


def validate_marketplace_manifest(
    marketplace: dict[str, Any], plugin_version: Any
) -> list[str]:
    failures: list[str] = []
    if marketplace.get("name") != "openarc":
        failures.append("marketplace name must be openarc")
    interface = marketplace.get("interface")
    if not isinstance(interface, dict) or interface.get("displayName") != "OpenArc":
        failures.append("marketplace interface.displayName must be OpenArc")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1 or not isinstance(plugins[0], dict):
        failures.append("marketplace must contain exactly one OpenArc plugin entry")
        return failures

    plugin = plugins[0]
    if plugin.get("name") != "openarc":
        failures.append("marketplace plugin name must be openarc")
    source = plugin.get("source")
    if not isinstance(source, dict) or source.get("source") != "url":
        failures.append("marketplace plugin source must be url")
    else:
        if source.get("url") != OPENARC_REPOSITORY_URL:
            failures.append(f"marketplace plugin URL must be {OPENARC_REPOSITORY_URL}")
        expected_ref = f"v{plugin_version}"
        if source.get("ref") != expected_ref:
            failures.append(f"marketplace plugin ref must match plugin version: {expected_ref}")
    if plugin.get("policy") != {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    }:
        failures.append("marketplace plugin policy must allow installation on install")
    if plugin.get("category") != "Developer Tools":
        failures.append("marketplace plugin category must be Developer Tools")
    return failures


def parse_skill_frontmatter(path: Path) -> dict[str, str]:
    try:
        text = path.read_text()
    except (OSError, UnicodeError):
        return {}
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---", 2)
    if len(parts) != 3:
        return {}
    _, block, _ = parts
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
            if not manifest_matches_plugin_root(plugin_root, manifest):
                failures.append(
                    "plugin.json name must match the plugin folder or its versioned cache parent"
                )
            if manifest.get("license") == "[TODO: MIT]":
                failures.append("plugin.json license still has placeholder value")
            if manifest.get("skills") != "./skills/":
                failures.append("plugin.json skills should be ./skills/")
            if not is_semver(manifest.get("version")):
                failures.append("plugin.json version must be valid SemVer")
            interface = manifest.get("interface")
            if not isinstance(interface, dict):
                failures.append("plugin.json interface must be an object")
            else:
                for field in ("composerIcon", "logo"):
                    asset = interface.get(field)
                    if not isinstance(asset, str) or not asset.startswith("./"):
                        failures.append(f"plugin.json interface.{field} must be a local path")
                        continue
                    asset_path = (plugin_root / asset).resolve()
                    if plugin_root.resolve() not in asset_path.parents:
                        failures.append(f"plugin.json interface.{field} must stay inside the plugin")
                    elif not asset_path.is_file():
                        failures.append(f"missing manifest asset: {asset}")
            warnings.extend(find_manifest_placeholders(manifest))

    claude_manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
    if claude_manifest_path.exists():
        try:
            claude_manifest = load_json(claude_manifest_path)
        except Exception as exc:  # noqa: BLE001 - command-line diagnostic
            failures.append(f"invalid .claude-plugin/plugin.json: {exc}")
        else:
            if not manifest_matches_plugin_root(plugin_root, claude_manifest):
                failures.append(
                    ".claude-plugin/plugin.json name must match the plugin folder or its versioned cache parent"
                )
            if not claude_manifest.get("version"):
                failures.append(".claude-plugin/plugin.json must include version")
            elif not is_semver(claude_manifest.get("version")):
                failures.append(".claude-plugin/plugin.json version must be valid SemVer")
            if claude_manifest.get("version") != manifest.get("version"):
                failures.append("Claude and Codex plugin manifest versions must match")
            warnings.extend(find_manifest_placeholders(claude_manifest))

    marketplace_path = plugin_root / ".agents" / "plugins" / "marketplace.json"
    if marketplace_path.exists():
        try:
            marketplace = load_json(marketplace_path)
        except Exception as exc:  # noqa: BLE001 - command-line diagnostic
            failures.append(f"invalid .agents/plugins/marketplace.json: {exc}")
        else:
            failures.extend(
                validate_marketplace_manifest(marketplace, manifest.get("version"))
            )

    skills_root = plugin_root / "skills"
    if not skills_root.exists():
        failures.append("missing skills directory")
    else:
        for skill in REQUIRED_SKILLS:
            if not (skills_root / skill / "SKILL.md").is_file():
                failures.append(f"missing required skill: skills/{skill}/SKILL.md")
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
    if not repo_root.exists():
        print(
            f"OpenArc scan: ERROR\n- repository path does not exist: {repo_root}",
            file=sys.stderr,
        )
        return 2
    if not repo_root.is_dir():
        print(
            f"OpenArc scan: ERROR\n- repository path is not a directory: {repo_root}",
            file=sys.stderr,
        )
        return 2

    repo_profile = detect_repo_profile(repo_root)
    files = {path: rel_exists(repo_root, path) for path in GOVERNANCE_FILES}
    optional_public_files = {
        path: rel_exists(repo_root, path) for path in OPTIONAL_PUBLIC_FILES
    }
    dirs = {path: rel_exists(repo_root, path) for path in GOVERNANCE_DIRS}

    spec_count = count_files(repo_root / "docs" / "specs", "*.md")
    plan_count = count_files(repo_root / "docs" / "plans", "*.md")
    task_count = int(files["docs/TASKS.md"])

    categories = categorize_governance(
        repo_profile,
        repo_root,
        files,
        dirs,
        optional_public_files,
    )
    missing_by_group = {
        f"{level}_{kind}": missing_from_status(categories[level][kind])
        for level in ("required", "relevant")
        for kind in ("files", "directories")
    }
    profile_missing_files = (
        missing_by_group["required_files"] + missing_by_group["relevant_files"]
    )
    profile_missing_dirs = (
        missing_by_group["required_directories"]
        + missing_by_group["relevant_directories"]
    )
    all_missing_files = profile_missing_files + missing_from_status(
        categories["optional"]["files"]
    )
    all_missing_dirs = profile_missing_dirs + missing_from_status(
        categories["optional"]["directories"]
    )

    payload = {
        "root": str(repo_root),
        "repo_profile": repo_profile,
        **categories,
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
            categories,
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


def iter_repo_files(repo_root: Path) -> list[Path]:
    paths: list[Path] = []
    for current_root, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = sorted(
            dirname for dirname in dirnames if dirname not in IGNORED_SCAN_DIRS
        )
        base = Path(current_root)
        for filename in sorted(filenames):
            paths.append(base / filename)
    return sorted(paths)


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
    if relative_files.intersection(APP_ENTRY_PATHS):
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
    return any(Path(path).name in package_markers for path in relative_files)


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


def has_design_signal(profile: str, repo_root: Path) -> bool:
    return profile == "app" or rel_exists(repo_root, "docs/DESIGN.md") or any(
        rel_exists(repo_root, path) for path in APP_ENTRY_PATHS
    )


def has_brand_signal(repo_root: Path) -> bool:
    brand_assets = repo_root / "docs" / "assets" / "brand"
    return rel_exists(repo_root, "docs/BRAND.md") or (
        brand_assets.is_dir() and any(path.is_file() for path in brand_assets.rglob("*"))
    )


def relevant_governance(profile: str) -> tuple[list[str], list[str]]:
    if profile == "unknown":
        return [], []
    if profile == "docs":
        return ["docs/PROJECT_BRIEF.md"], []

    files = list(RELEVANT_CORE_FILES)
    if profile in {"app", "library", "plugin"}:
        files.append("docs/ARCHITECTURE.md")
    if profile == "app":
        files.append("docs/PRD.md")
    return files, []


def categorize_governance(
    profile: str,
    repo_root: Path,
    files: dict[str, bool],
    dirs: dict[str, bool],
    optional_public_files: dict[str, bool],
) -> dict[str, dict[str, dict[str, bool]]]:
    relevant_file_names, relevant_dir_names = relevant_governance(profile)
    if has_design_signal(profile, repo_root):
        relevant_file_names.append("docs/DESIGN.md")
    if has_brand_signal(repo_root):
        relevant_file_names.append("docs/BRAND.md")

    optional_file_names = [
        path
        for path in GOVERNANCE_FILES
        if path not in AGENT_GUIDE_FILES
        and path != "README.md"
        and path not in relevant_file_names
    ]
    optional_files = {
        path: files[path]
        for path in optional_file_names
    }
    optional_files.update(optional_public_files)

    return {
        "required": {
            "files": {
                AGENT_GUIDE_REQUIREMENT: any(files[path] for path in AGENT_GUIDE_FILES),
                "README.md": files["README.md"],
            },
            "directories": {},
        },
        "relevant": {
            "files": {path: files[path] for path in relevant_file_names},
            "directories": {path: dirs[path] for path in relevant_dir_names},
        },
        "optional": {
            "files": optional_files,
            "directories": {
                path: dirs[path]
                for path in GOVERNANCE_DIRS
                if path not in relevant_dir_names
            },
        },
    }


def missing_from_status(values: dict[str, bool]) -> list[str]:
    return [path for path, exists in values.items() if not exists]


def recommend(
    categories: dict[str, dict[str, dict[str, bool]]],
) -> str:
    required_files = missing_from_status(categories["required"]["files"])
    relevant_files = missing_from_status(categories["relevant"]["files"])
    relevant_dirs = missing_from_status(categories["relevant"]["directories"])

    if AGENT_GUIDE_REQUIREMENT in required_files:
        return "Start with repository-governance and create a profile-aware agent guide."
    if "README.md" in required_files:
        return "Create or update README.md with the repository's purpose and validation path."
    if "docs/PRD.md" in relevant_files:
        return "Use product-governance to clarify and create docs/PRD.md."
    if "docs/DESIGN.md" in relevant_files:
        return "Use design-governance to create docs/DESIGN.md."
    if "docs/BRAND.md" in relevant_files:
        return "Use brand-governance to create docs/BRAND.md."
    if relevant_files or relevant_dirs:
        missing = relevant_files + relevant_dirs
        return f"Address profile-relevant governance: {', '.join(missing)}."
    return "Governance baseline exists; use implementation-workflow for changes."


def print_markdown_scan(payload: dict[str, Any]) -> None:
    print("# OpenArc Scan")
    print()
    print(f"Root: `{payload['root']}`")
    print(f"Repo profile: `{payload['repo_profile']}`")
    for level in ("required", "relevant", "optional"):
        print()
        title = level.capitalize()
        if level == "optional":
            title += " (present only)"
        print(f"## {title}")
        shown = False
        for kind in ("files", "directories"):
            for path, exists in payload[level][kind].items():
                if level == "optional" and not exists:
                    continue
                shown = True
                mark = "ok" if exists else "missing"
                print(f"- {mark}: `{path}`")
        if not shown:
            print("- none")
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
