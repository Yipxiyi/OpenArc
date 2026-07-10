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

- Ask 0-5 questions only for material unknowns that change scope, behavior, compatibility, migration, or risk. Ask zero and continue in the same turn when readiness is `ready` and the original request authorizes implementation.
- Implement routine work directly when scope, expected behavior, and validation are clear.
- Use `docs/specs/*` when behavior, acceptance criteria, or compatibility needs durable alignment.
- Use `docs/plans/*` when sequencing, migration, rollback, or validation risk needs structure.
- Use `docs/TASKS.md` only when work spans multiple stages, people, or agents.
- Prefer minimal changes.
- Reuse existing systems.
- Infer code style from existing config and code before asking for preferences.
- Avoid duplicate abstractions.
- Match governance scope to repository profile; script, CLI, automation, library, and docs-only repositories do not need design or brand docs by default.
- For an `unknown` profile, use only a README and one agent guide as the minimum baseline; do not infer other governance requirements.
- For UI work, check `docs/DESIGN.md` and existing components before creating a new component.
- Add reusable component patterns to `docs/DESIGN.md`; keep one-off component rationale in the related spec or plan.
- Keep diffs reviewable.
- Update specs after implementation.
- Avoid random temporary files.
- Scan the repository before large changes.
- Use the smallest context required to safely complete the task.
- Do not automatically load archived changelogs, old completed tasks, deprecated specs, outdated implementation notes, or unrelated source files.

## Execution Workflow

1. Inspect the affected repository flow and existing conventions.
2. For routine work, implement the smallest coherent change and validate it.
3. For non-trivial work, clarify material unknowns, then choose a spec, a plan, or both only when each is justified.
4. Update `docs/TASKS.md` only for multi-stage or multi-person/agent coordination.
5. Implement incrementally.
6. Validate.
7. Update relevant existing documentation.

## Change Tracking

When the repository already uses `docs/CHANGELOG_AI.md` and the change is material:

1. Update `docs/CHANGELOG_AI.md`; do not create it solely for routine work.
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
