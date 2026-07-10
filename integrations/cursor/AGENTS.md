# OpenArc Agent Guide

Use OpenArc when this repository needs lightweight AI-native governance, source-of-truth discovery, specs, plans, migration, or release/version guidance.

## Default Workflow

1. Scan existing repository files before writing.
2. Preserve existing conventions and source-of-truth documents.
3. Keep changes small, reviewable, and reversible.
4. Keep audit, review, scan, and "what is missing?" requests read-only.
5. Write only for explicit setup, initialization, apply, repair, or migration requests.
6. Detect the repo profile before deciding which governance files are missing.
7. Create missing governance files only when no suitable source already exists and the file is relevant to the repo profile.
8. Prefer `docs/specs/`, `docs/plans/`, `docs/tasks/`, `docs/CHANGELOG_AI.md`, and `docs/archive/` for durable delivery and change context.
9. Use `docs/CODE_STYLE.md` for stable code conventions and unresolved style preferences.
10. Treat `docs/PRD.md`, `docs/DESIGN.md`, `docs/BRAND.md`, and `docs/assets/*` as conditional surfaces, not universal requirements.
11. For broad, ambiguous, risky, or new work, run a clarification pass before PRD, spec, plan, or implementation.
12. For UI work, check `docs/DESIGN.md` and existing components before creating a new component.

## OpenArc Tasks

- For a general "use OpenArc" request, identify the narrowest relevant workflow first.
- For drift review, inspect and report only. For explicit repository setup, create or patch an agent guide.
- For new goals or non-trivial changes, clarify goal, non-goals, constraints, target docs, and implementation readiness before coding.
- For repository setup or migration, infer code style from existing config and code; ask only for material preferences that are not discoverable.
- For product, design, or brand docs, ask only for material unknowns instead of filling gaps with generic guesses.
- For script, CLI, automation, library, or docs-only repos, do not create design or brand docs unless there are UI, visual asset, public product, or identity signals.
- For non-trivial changes, create or update a spec and implementation plan before coding.
- For version changes, use semantic versioning: patch for fixes/docs, minor for backward-compatible additions, major for breaking governance or API/schema changes.
- For branch, commit, or PR work, stop after the requested operation; trigger or publish a release only after an explicit release request and confirmation.
- For migration, inventory first and avoid moving, renaming, deleting, or archiving files without confirmation.
- For reusable UI components, update `docs/DESIGN.md` with a Component Patterns entry in the same change.
- For one-off UI components, document the reason in the related spec or plan instead of adding noise to `docs/DESIGN.md`.

## Helper

If this OpenArc package is available in the workspace, run:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the scan as evidence, then verify important findings manually.
