---
name: planning-engine
description: Use when producing a lightweight implementation plan before coding, including scope, affected systems, migration, rollback, tests, reuse, and architecture impact.
---

# Planning Engine

Use this skill before implementation when a change has meaningful scope, risk, or cross-file impact.

## Goal

Create a short, executable plan that helps agents implement the right change in the right order.

If the goal, non-goals, constraints, acceptance criteria, or target docs are not stable, run `clarification-gate` before writing the plan.

## Plan Requirements

A plan should answer:

- What changes
- Why it changes
- Affected systems
- Existing code or docs to reuse
- Migration requirements
- Rollback strategy
- Testing strategy
- Architecture impact
- Risks and open questions
- Version impact and whether user confirmation is needed

## Output

Use `templates/PLAN.template.md` as the default shape. Save plans under `docs/plans/` when the repository keeps persistent plans. Otherwise, keep the plan in the conversation and execute it.

## Rules

- Keep plans lightweight.
- Prefer the shortest viable path.
- Do not turn routine changes into ceremony.
- Do not proceed to implementation if the plan exposes unresolved blockers that would make the work risky or incoherent.
- Use Clarification Gate output as the preferred input when the request started broad, ambiguous, or cross-cutting.
- Use `version-governance` when the plan implies patch, minor, or major release impact.
