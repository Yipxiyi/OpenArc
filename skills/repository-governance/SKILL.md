---
name: repository-governance
description: Use when initializing or repairing OpenArc repository governance, detecting source-of-truth docs, and patching or creating AGENT.md or AGENTS.md without destructive rewrites.
---

# Repository Governance

Use this skill when a repository needs OpenArc governance setup, drift review, or source-of-truth discovery.

## Goal

Help agents understand repository structure, identify governance documents, preserve existing conventions, and create or patch a project agent guide.

## Workflow

1. Scan the repository before changing files.
2. Detect existing conventions, docs, architecture notes, specs, plans, tasks, design files, brand files, assets, and agent guides.
3. Identify conflicts between existing docs and requested OpenArc structure.
4. Patch existing files when they already carry project intent.
5. Create missing files only when no suitable existing source exists.
6. Keep diffs small and reviewable.

If `scripts/openarc.py` is available, run or request:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the result as a starting point, then verify important findings manually.

## Source Of Truth

Prefer existing repository files over generated defaults. Common OpenArc sources:

- `docs/PRD.md`
- `docs/DESIGN.md`
- `docs/BRAND.md`
- latest `docs/specs/*.md`
- `docs/assets/*`
- existing `AGENT.md` or `AGENTS.md`

## Agent Guide Rules

If an agent guide exists, preserve its intent and patch only missing governance sections.

If none exists, create one from `templates/AGENT.template.md` and adapt paths to the repository.

The guide should cover:

- Source-of-truth documents
- Working rules
- Execution workflow
- Validation expectations
- Repository-specific constraints

## Hard Rules

- Do not rewrite existing governance docs just to match the template.
- Do not invent architecture facts the repository does not show.
- Do not leave temporary files or duplicate documentation trees.
- Report created files, modified files, detected governance docs, conflicts, and recommended next steps.
