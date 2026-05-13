---
name: implementation-workflow
description: Use when guiding OpenArc implementation order from repository scan through spec, plan, tasks, incremental implementation, validation, and documentation update.
---

# Implementation Workflow

Use this skill when moving from OpenArc governance into actual implementation.

## Required Workflow

1. Scan repository.
2. Detect existing governance files.
3. Analyze architecture.
4. Patch or create `AGENT.md` or `AGENTS.md`.
5. Patch or create governance docs.
6. Create or update the relevant spec.
7. Create or update the implementation plan.
8. Create or update tasks.
9. Classify version impact and confirm the proposed version when release-visible.
10. Implement incrementally.
11. Validate.
12. Update documentation.

## Optimization Targets

- Long-running repositories
- AI continuity
- Low context drift
- Maintainable vibe coding
- Small, reviewable diffs

## Rules

- Do not begin unrelated business features while setting up OpenArc.
- Reuse existing code, docs, scripts, and conventions.
- Prefer patch-based updates over rewrites.
- Keep implementation and documentation in sync.
- Report created files, modified files, validation performed, conflicts, and next-step recommendations.
- Use `release-workflow` for branch, commit, PR, merge, and GitHub release update work.
