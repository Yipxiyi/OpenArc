# Changelog

All notable changes to OpenArc should be recorded here.

This project follows semantic versioning.

## Unreleased

## 0.6.0

- Simplified repository scans into required, relevant, and optional governance instead of treating the full OpenArc inventory as mandatory.
- Consolidated delivery sources of truth around `docs/specs/*`, `docs/plans/*`, and `docs/TASKS.md`.
- Added a routine-change path that goes directly from repository evidence to the smallest implementation and validation without mandatory spec, plan, task, or version ceremony.
- Decoupled spec file names from release versions and removed duplicate implementation-plan and task sections from the spec template.
- Refined Clarification Gate to allow zero to five material questions and continue in the same turn when the request is ready and already authorized.
- Improved repository profile detection by removing traversal truncation, separating UI and brand signals, and keeping unknown repositories on a minimal baseline.
- Reduced human-facing scan noise so optional governance does not appear as required remediation.

## 0.5.1

- Fixed audit routing so read-only reviews do not create or modify governance files without explicit apply intent.
- Fixed release guidance so PR work does not trigger release automation without an explicit release request and confirmation.
- Fixed Codex and Cursor installation guidance to install and verify the plugin without overwriting existing agent instructions or creating nested plugin directories.
- Strengthened `openarc.py doctor` and release validation for missing skills, invalid frontmatter, referenced assets, version parity, and test failures.
- Fixed repository scans so invalid paths fail clearly instead of returning a successful `unknown` report.

## 0.5.0

- Added `clarification-gate` as a first-class OpenArc skill for clarifying broad, ambiguous, risky, or new work before PRD, spec, plan, or implementation.
- Added a bounded question-budget model with recommended answers and trade-offs, plus guidance for carrying decisions into existing OpenArc docs instead of creating new intake or ADR trees by default.
- Added `CODE_STYLE.template.md` and required it in `openarc.py doctor` so `docs/CODE_STYLE.md` has a stable template.
- Updated repository setup, workspace migration, product, spec, planning, design, and implementation workflows to consume Clarification Gate output and collect code style or design preferences only when profile-relevant.
- Expanded `DESIGN.template.md` with source-aware evidence, profile/platform rules, tokens, component standards, interaction, accessibility, and do/do-not guidance.
- Updated README, Cursor adapters, examples, manifests, and validation tests for OpenArc 0.5.0.

## 0.4.0

- Added profile-aware repository scans with `repo_profile`, profile-relevant `missing_files`, `all_missing_files`, grouped missing governance, and adaptive recommendations for script, library, app, plugin, docs, and unknown repositories.
- Stopped defaulting script, CLI, automation, library, and docs-only repositories into design, brand, or assets governance unless the repo has matching signals.
- Updated OpenArc skills, Cursor adapters, README, and agent templates so product, design, brand, and asset docs are conditional governance surfaces.

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
