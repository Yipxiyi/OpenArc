# Project Agent Guide

## Source Of Truth

Before implementation, review:

- `docs/CODE_STYLE.md` for stable code conventions and unresolved style preferences
- `docs/PRD.md` for product or app work
- `docs/DESIGN.md` for UI, frontend, desktop, mobile, or component work
- `docs/BRAND.md` for public brand, identity, marketing, naming, or copy work
- latest `docs/specs/*`
- `docs/assets/*` when visual assets or references exist

## Working Rules

- Spec first for non-trivial work.
- Clarify broad, ambiguous, risky, or new work before PRD, spec, plan, or implementation.
- Plan before implementation when multiple files or systems are affected.
- Prefer minimal changes.
- Reuse existing systems.
- Infer code style from existing config and code before asking for preferences.
- Match governance scope to repository profile; script, CLI, automation, library, and docs-only repositories do not need design or brand docs by default.
- Keep diffs reviewable.
- Update specs after implementation.
- Avoid temporary files.

## Execution Workflow

1. Analyze repository.
2. Read governance docs.
3. Create or update spec.
4. Create implementation plan.
5. Create tasks.
6. Implement incrementally.
7. Validate.
8. Update documentation.
