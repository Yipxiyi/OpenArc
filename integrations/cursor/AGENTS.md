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
8. Use `docs/specs/*.md` as the canonical feature-spec location and `docs/TASKS.md` as the single active task ledger.
9. Use `docs/CODE_STYLE.md` for stable code conventions and unresolved style preferences.
10. Treat `docs/PRD.md`, `docs/DESIGN.md`, and `docs/BRAND.md` as independent conditional surfaces; UI evidence does not imply brand work, and brand evidence does not imply UI work.
11. Treat `docs/assets/*` as optional. Use it only when assets already exist or the user explicitly requests asset organization.
12. For broad, ambiguous, risky, or new work, ask 0-5 material questions. Ask none when repository evidence is sufficient; if ready and already authorized, continue in the same turn.
13. For routine, low-risk work with clear scope and validation, implement directly without creating a spec, plan, or task document.
14. For UI work, check `docs/DESIGN.md` and existing components before creating a new component.

## OpenArc Tasks

- For a general "use OpenArc" request, identify the narrowest relevant workflow first.
- For drift review, inspect and report only. For explicit repository setup, create or patch an agent guide.
- For unclear or risky work, clarify goal, non-goals, constraints, target docs, and implementation readiness before coding.
- For repository setup or migration, infer code style from existing config and code; ask only for material preferences that are not discoverable.
- For product, design, or brand docs, ask only for material unknowns instead of filling gaps with generic guesses.
- For `unknown` repositories, require only `README.md` and one agent guide; do not assume app, UI, brand, spec, plan, task, or archive governance.
- Evaluate UI and brand signals independently. Do not create design, brand, or asset docs from an unrelated signal.
- Use a spec when behavior, acceptance criteria, or compatibility needs a durable contract; use a plan when sequencing, migration, rollback, or validation needs structure; use `docs/TASKS.md` only for active multi-step coordination.
- For version changes, use semantic versioning: patch for fixes/docs, minor for backward-compatible additions, major for breaking governance or API/schema changes.
- For branch, commit, or PR work, stop after the requested operation; trigger or publish a release only after an explicit release request and confirmation.
- For migration, inventory first and avoid moving, renaming, deleting, or archiving files without confirmation.
- For reusable UI components, update `docs/DESIGN.md` with a Component Patterns entry in the same change.
- For one-off UI components, keep the reason in the change context instead of adding noise to `docs/DESIGN.md`.

## Helper

If this OpenArc package is available in the workspace, run:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the scan as evidence, then verify important findings manually.

Interpret scan results as `required`, `relevant`, and `optional`: required gaps affect the profile baseline, relevant items depend on current evidence or work, and optional items never make the repository unhealthy.
