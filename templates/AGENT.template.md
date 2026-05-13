# Project Agent Guide

## Source Of Truth

Default read priority:

- `docs/PROJECT_BRIEF.md`
- `docs/CODE_STYLE.md`
- `docs/TASKS.md`

Conditional read:

- `docs/PRD.md`
- `docs/DESIGN.md`
- `docs/BRAND.md`
- latest `docs/specs/*`
- `docs/assets/*`
- `docs/CHANGELOG_AI.md`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `LICENSE`

Rarely read:

- `docs/archive/*`

## Working Rules

- Spec first.
- Plan before implementation when scope or risk is non-trivial.
- Prefer minimal changes.
- Reuse existing systems.
- Avoid duplicate abstractions.
- Keep diffs reviewable.
- Update specs after implementation.
- Avoid random temporary files.
- Scan the repository before large changes.
- Use the smallest context required to safely complete the task.
- Do not automatically load archived changelogs, old completed tasks, deprecated specs, outdated implementation notes, or unrelated source files.

## Execution Workflow

1. Analyze repository.
2. Read governance docs.
3. Create or update spec.
4. Create implementation plan.
5. Create tasks.
6. Implement incrementally.
7. Validate.
8. Update documentation.

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
