# OpenArc Agent Guide

Use OpenArc when this repository needs lightweight AI-native governance, source-of-truth discovery, specs, plans, migration, or release/version guidance.

## Default Workflow

1. Scan existing repository files before writing.
2. Preserve existing conventions and source-of-truth documents.
3. Keep changes small, reviewable, and reversible.
4. Create missing governance files only when no suitable source already exists.
5. Prefer `docs/PRD.md`, `docs/DESIGN.md`, `docs/BRAND.md`, `docs/specs/`, `docs/plans/`, `docs/tasks/`, `docs/CHANGELOG_AI.md`, and `docs/archive/` for durable project context.

## OpenArc Tasks

- For a general "use OpenArc" request, identify the narrowest relevant workflow first.
- For repository setup or drift review, inspect current docs and create or patch an agent guide.
- For product, design, or brand docs, ask only for material unknowns instead of filling gaps with generic guesses.
- For non-trivial changes, create or update a spec and implementation plan before coding.
- For version changes, use semantic versioning: patch for fixes/docs, minor for backward-compatible additions, major for breaking governance or API/schema changes.
- For migration, inventory first and avoid moving, renaming, deleting, or archiving files without confirmation.

## Helper

If this OpenArc package is available in the workspace, run:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the scan as evidence, then verify important findings manually.
