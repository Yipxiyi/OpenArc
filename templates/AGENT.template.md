# Project Agent Guide

## Source Of Truth

Default read priority:

- `docs/PROJECT_BRIEF.md`
- `docs/CODE_STYLE.md`
- `docs/TASKS.md`

Conditional read:

- `docs/PRD.md` for product or app work
- `docs/DESIGN.md` for UI, frontend, desktop, mobile, or component work
- `docs/BRAND.md` for public brand, identity, marketing, naming, or copy work
- latest `docs/specs/*`
- `docs/assets/*` when visual assets or references exist
- `docs/CHANGELOG_AI.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `LICENSE`

Rarely read:

- `docs/archive/*`

## Working Rules

- Clarify broad, ambiguous, risky, or new work before PRD, spec, plan, or implementation.
- Spec first.
- Plan before implementation when scope or risk is non-trivial.
- Prefer minimal changes.
- Reuse existing systems.
- Infer code style from existing config and code before asking for preferences.
- Avoid duplicate abstractions.
- Match governance scope to repository profile; script, CLI, automation, library, and docs-only repositories do not need design or brand docs by default.
- For UI work, check `docs/DESIGN.md` and existing components before creating a new component.
- Add reusable component patterns to `docs/DESIGN.md`; keep one-off component rationale in the related spec or plan.
- Keep diffs reviewable.
- Update specs after implementation.
- Avoid random temporary files.
- Scan the repository before large changes.
- Use the smallest context required to safely complete the task.
- Do not automatically load archived changelogs, old completed tasks, deprecated specs, outdated implementation notes, or unrelated source files.

## Execution Workflow

1. Analyze repository.
2. Read governance docs.
3. Run clarification when the goal or constraints are not stable.
4. Create or update spec.
5. Create implementation plan.
6. Create tasks.
7. Implement incrementally.
8. Validate.
9. Update documentation.

## Change Tracking

After completing implementation or documentation work:

1. Update `docs/CHANGELOG_AI.md`.
2. Keep entries concise.
3. Record:
   - changed files
   - key decisions
   - verification
   - remaining work

If `CHANGELOG_AI.md` becomes too large:

- archive older entries
- keep only recent activity visible

## Archive Policy

Do not delete historical information.

Move completed historical context into `docs/archive/`.

Archived files are not read by default.

Only load them when:

- debugging regressions
- investigating architectural history
- understanding prior AI decisions

## Validation

- [TODO: project-specific build command]
- [TODO: project-specific test command]
- [TODO: project-specific lint or typecheck command]

## Repository Notes

- [TODO: architecture notes]
- [TODO: deployment notes]
- [TODO: known constraints]
