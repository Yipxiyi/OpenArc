---
name: spec-workflow
description: Use when creating or updating OpenArc feature specs with versioning, acceptance criteria, implementation tracking, and technical direction.
---

# Spec Workflow

Use this skill when a feature, system change, or product direction needs a structured spec before implementation.

## Goal

Create lightweight specs that keep humans and coding agents aligned without adding heavy process overhead.

## Location

Use `docs/specs/` by default.

Recommended file names:

```txt
docs/specs/
  0.1.0-auth-system.md
  0.2.0-editor-upgrade.md
  0.3.0-cloud-sync.md
```

## Status Values

- Draft
- Planned
- In Progress
- Implemented
- Verified

## Version Selection

Use `version-governance` before choosing a new spec version when the user asks for a change to an existing feature or governance system.

Default mapping:

- Patch spec: small clarification, typo, doc-only correction, or non-behavioral refinement.
- Minor spec: backward-compatible feature, optional workflow, new template, or new section.
- Major spec: breaking behavior, renamed public workflow, removed capability, or incompatible governance structure.

Propose the exact version and ask the user to confirm before naming the spec file.

## Required Spec Sections

Use `templates/SPEC.template.md` as the baseline:

- Background
- Goals
- Non-Goals
- User Stories
- Requirements
- Existing System Review
- Technical Approach
- Implementation Plan
- Tasks
- Acceptance Criteria
- Risks
- Open Questions
- Changelog

## Rules

- Keep specs concrete and implementation-facing.
- Separate goals from non-goals.
- Include acceptance criteria that can be verified.
- Update status and changelog after implementation.
- Do not use specs as a dumping ground for unrelated product ideas.
- Record the confirmed version decision in the changelog.
