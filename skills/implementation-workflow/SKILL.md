---
name: implementation-workflow
description: Use when guiding OpenArc implementation order from repository scan through spec, plan, tasks, incremental implementation, validation, and documentation update.
---

# Implementation Workflow

Use this skill when moving from OpenArc governance into actual implementation.

## Required Workflow

1. Scan repository.
2. Detect repo profile and existing governance files.
3. Analyze architecture.
4. Run `clarification-gate` when the request is broad, ambiguous, risky, or new.
5. Patch or create `AGENT.md` or `AGENTS.md`.
6. Patch or create profile-relevant governance docs.
7. Create or update the relevant spec.
8. Create or update the implementation plan.
9. Create or update tasks.
10. Classify version impact and confirm the proposed version when release-visible.
11. Implement incrementally.
12. For UI work, check component reuse before adding new components.
13. Validate.
14. Update documentation.

## Component Reuse Gate

For UI or frontend changes:

1. Read `docs/DESIGN.md` when it exists.
2. Inspect the local component library before creating a new component.
3. Reuse or extend an existing component when it covers roughly 70-80% of the use case.
4. If creating a reusable component, update `docs/DESIGN.md` with a `Component Patterns` entry in the same change.
5. If creating a one-off component, document the reason in the related spec or plan.

This gate prevents silent component duplication while keeping `docs/DESIGN.md` from becoming a component inventory dump.

For script, CLI, automation, data-processing, library, or docs-only repositories, skip this gate unless the task introduces UI, visual assets, or public brand surfaces.

## Optimization Targets

- Long-running repositories
- AI continuity
- Low context drift
- Maintainable vibe coding
- Small, reviewable diffs

## Rules

- Do not begin unrelated business features while setting up OpenArc.
- Do not start implementation from an unclear goal; use `clarification-gate` and carry its decisions into PRD, spec, plan, tasks, or existing docs.
- Reuse existing code, docs, scripts, and conventions.
- Prefer patch-based updates over rewrites.
- Keep implementation and documentation in sync.
- Do not create `docs/DESIGN.md`, `docs/BRAND.md`, or `docs/assets/*` just to satisfy a generic checklist.
- Do not create duplicate UI components without first checking existing components and `docs/DESIGN.md`.
- Report created files, modified files, validation performed, conflicts, and next-step recommendations.
- Use `release-workflow` for branch, commit, PR, merge, and GitHub release update work.
