# Project Agent Guide

## Source Of Truth

Before implementation, review only the sources relevant to the change:

- `docs/CODE_STYLE.md` for stable code conventions and unresolved style preferences
- `docs/TASKS.md` for active multi-step coordination
- latest `docs/specs/*` when the change has a feature spec

Conditional sources:

- `docs/PRD.md` for product or app work
- `docs/DESIGN.md` for UI, frontend, desktop, mobile, or component work
- `docs/BRAND.md` for public brand, identity, marketing, naming, or copy work, independently of UI

Use `docs/assets/*` only when assets already exist or asset organization is explicitly requested.

## Working Rules

- Implement routine, low-risk work directly when scope and validation are clear.
- Ask 0-5 material clarification questions for broad, ambiguous, risky, or new work; ask none when repository evidence is sufficient and continue in the same turn when ready and authorized.
- Use a spec when behavior, acceptance criteria, or compatibility needs a durable contract.
- Use a plan when sequencing, migration, rollback, or validation needs structure.
- Use `docs/TASKS.md` only for active multi-step coordination.
- Prefer minimal changes.
- Reuse existing systems.
- Infer code style from existing config and code before asking for preferences.
- For `unknown` repositories, require only `README.md` and one agent guide; do not assume app, UI, brand, spec, plan, task, or archive governance.
- Evaluate UI and brand signals independently, and keep assets optional.
- Keep diffs reviewable.
- Update any spec used by the change after implementation.
- Avoid temporary files.

## Execution Workflow

1. Analyze the repository and read only relevant governance docs.
2. Ask 0-5 material questions when needed.
3. Choose direct implementation, a spec, a plan, or active tasks based on actual risk and coordination needs.
4. Implement incrementally.
5. Validate.
6. Update only the documentation used by the change.
