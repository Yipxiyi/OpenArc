---
name: repository-governance
description: Use when initializing or repairing OpenArc repository governance, detecting source-of-truth docs, and patching or creating AGENT.md or AGENTS.md without destructive rewrites.
---

# Repository Governance

Use this skill when a repository needs OpenArc governance setup, drift review, or source-of-truth discovery.

## Goal

Help agents understand repository structure, identify governance documents, preserve existing conventions, and create or patch a project agent guide.

## Workflow

1. Scan the repository before changing files.
2. Detect the repository profile: `script`, `library`, `app`, `plugin`, `docs`, or `unknown`.
3. Detect existing conventions, docs, architecture notes, specs, plans, tasks, conditional product/design/brand files, assets, and agent guides.
4. Identify conflicts between existing docs and requested OpenArc structure.
5. Patch existing files when they already carry project intent.
6. Create missing files only when they are relevant to the detected profile and no suitable existing source exists.
7. Keep diffs small and reviewable.

If `scripts/openarc.py` is available, run or request:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the result as a starting point, then verify important findings manually.

## Source Of Truth

Prefer existing repository files over generated defaults. Common OpenArc sources:

Default read priority:

- `docs/PROJECT_BRIEF.md`
- `docs/CODE_STYLE.md`
- `docs/TASKS.md`
- existing `AGENT.md` or `AGENTS.md`

Conditional read:

- `docs/PRD.md`
- `docs/SPEC.md`
- `docs/ARCHITECTURE.md`
- `docs/DESIGN.md` for UI, frontend, desktop, mobile, or component work
- `docs/BRAND.md` for brand, marketing, public-facing, or visual identity work
- latest `docs/specs/*.md`
- `docs/assets/*` when the repo has UI, screenshots, icons, brand assets, or visual references
- `docs/CHANGELOG_AI.md`

Rarely read:

- `docs/archive/*`

## Context Budget Rule

Use the smallest context required to safely complete the task.

Do not automatically load:

- archived changelogs
- old completed tasks
- deprecated specs
- outdated implementation notes
- unrelated source files

Only load archived context when the task explicitly requires historical investigation.

## Agent Guide Rules

If an agent guide exists, preserve its intent and patch only missing governance sections.

If none exists, create one from `templates/AGENT.template.md` and adapt paths to the repository.

The guide should cover:

- Source-of-truth documents
- Working rules
- Execution workflow
- Validation expectations
- Repository-specific constraints
- Profile-specific conditional docs; for pure script repositories, prefer runbook, validation, and change-memory guidance over design or brand scaffolding.

## Hard Rules

- Do not rewrite existing governance docs just to match the template.
- Do not invent architecture facts the repository does not show.
- Do not create product, design, brand, or assets governance for repo profiles that do not need them.
- Do not leave temporary files or duplicate documentation trees.
- Do not make `docs/archive/*` part of default reading.
- Report created files, modified files, detected governance docs, conflicts, and recommended next steps.
