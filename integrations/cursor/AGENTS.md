# OpenArc Agent Guide

Use OpenArc when this repository needs lightweight AI-native governance, source-of-truth discovery, specs, plans, migration, or release/version guidance.

## Default Workflow

1. Scan existing repository files before writing.
2. Preserve existing conventions and source-of-truth documents.
3. Keep changes small, reviewable, and reversible.
4. Detect the repo profile before deciding which governance files are missing.
5. Create missing governance files only when no suitable source already exists and the file is relevant to the repo profile.
6. Prefer `docs/specs/`, `docs/plans/`, `docs/tasks/`, `docs/CHANGELOG_AI.md`, and `docs/archive/` for durable delivery and change context.
7. Use `docs/CODE_STYLE.md` for stable code conventions and unresolved style preferences.
8. Treat `docs/PRD.md`, `docs/DESIGN.md`, `docs/BRAND.md`, and `docs/assets/*` as conditional surfaces, not universal requirements.
9. For broad, ambiguous, risky, or new work, run a clarification pass before PRD, spec, plan, or implementation.
10. For UI work, check `docs/DESIGN.md` and existing components before creating a new component.

## OpenArc Tasks

- For a general "use OpenArc" request, identify the narrowest relevant workflow first.
- For repository setup or drift review, inspect current docs and create or patch an agent guide.
- For new goals or non-trivial changes, clarify goal, non-goals, constraints, target docs, and implementation readiness before coding.
- For repository setup or migration, infer code style from existing config and code; ask only for material preferences that are not discoverable.
- For product, design, or brand docs, ask only for material unknowns instead of filling gaps with generic guesses.
- For script, CLI, automation, library, or docs-only repos, do not create design or brand docs unless there are UI, visual asset, public product, or identity signals.
- For non-trivial changes, create or update a spec and implementation plan before coding.
- For version changes, use semantic versioning: patch for fixes/docs, minor for backward-compatible additions, major for breaking governance or API/schema changes.
- For migration, inventory first and avoid moving, renaming, deleting, or archiving files without confirmation.
- For reusable UI components, update `docs/DESIGN.md` with a Component Patterns entry in the same change.
- For one-off UI components, document the reason in the related spec or plan instead of adding noise to `docs/DESIGN.md`.

## Helper

If this OpenArc package is available in the workspace, run:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the scan as evidence, then verify important findings manually.
