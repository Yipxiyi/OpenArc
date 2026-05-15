# Changelog

All notable changes to OpenArc should be recorded here.

This project follows semantic versioning.

## Unreleased

## 0.3.1

- Refined README wording for public open-source use.
- Clarified install commands for standalone repository roots and vendored `plugins/openarc` layouts.
- Removed placeholder public metadata from the Codex plugin manifest.
- Reworked README positioning into a clearer marketing-style framework overview.
- Added comparison guidance for Superpowers and GitHub Spec Kit.
- Added README Q&A sections in English and Chinese.
- Rephrased workflow sections to describe OpenArc behavior instead of giving reader-facing commands to agents.

## 0.3.0

- Added component pattern governance rules to `design-governance` and `implementation-workflow`.
- Updated design and agent templates so UI work checks existing components before creating new ones.
- Added a `Component Patterns` section to the design template for reusable component guidance.
- Updated Cursor adapters and README with component reuse and one-off component documentation rules.

## 0.2.0

- Added Claude Code plugin manifest support through `.claude-plugin/plugin.json`.
- Added Cursor adapter files under `integrations/cursor/` for `AGENTS.md` and `.cursor/rules/openarc.mdc` installation paths.
- Updated README with Claude Code and Cursor installation guidance.
- Expanded `openarc.py doctor` to validate Claude Code manifest parity and Cursor adapter files.

## 0.1.3

- Fixed repository scans so `CHANGELOG.md`, `CONTRIBUTING.md`, and `LICENSE` are reported as optional public maintenance files instead of baseline governance gaps.
- Updated README guidance to clarify the difference between core OpenArc governance files and public/open-source maintenance files.

## 0.1.2

- Reworked README for public GitHub use with English/Chinese sections and top language jump links.
- Removed internal status, release policy, and internal roadmap wording from README.
- Added `change-archive-governance` for `CHANGELOG_AI.md`, archive policy, and context-budget-aware repository reading.
- Added `CHANGELOG_AI.template.md` and `ARCHIVE_INDEX.template.md`.
- Updated agent and repository governance guidance with default, conditional, and rare read priorities.
- Updated helper scan/doctor coverage for AI change memory and archive governance.
- Updated plugin repository metadata to `https://github.com/Yipxiyi/OpenArc`.
- Preserved visual asset fields as unset pending final icon/logo selection.
- Added an `openarc` entry skill to route general OpenArc requests into the right focused workflow.
- Added a dependency-free `scripts/openarc.py` helper with `scan` and `doctor` commands.
- Updated README quick start around first-run scanning and maintainer validation.
- Added open-source maintenance guidance.
- Reworked README into a public open-source entrypoint.
- Added MIT license metadata and license file.
- Added contribution guidance for future maintainers.

## 0.1.0

- Added initial OpenArc plugin manifest.
- Added focused governance, spec, planning, design, brand, assets, implementation, version, release, and migration skills.
- Added baseline templates and examples.
