---
name: workspace-migration
description: Use when migrating an existing repository or workspace into OpenArc conventions, aligning docs, specs, plans, assets, agent guides, versions, and release workflow without destructive rewrites.
---

# Workspace Migration

Use this skill when a user wants an existing workspace adjusted to OpenArc conventions.

## Goal

Move an existing repository toward OpenArc structure while preserving working project intent and minimizing churn.

## Migration Workflow

1. Inventory the workspace:
   - agent guides
   - README and docs
   - repo profile and profile-relevant PRD/design/brand materials
   - specs, plans, tasks
   - assets
   - changelog and releases
   - CI and GitHub workflows
2. Map existing files to OpenArc targets.
3. Classify actions:
   - keep as-is
   - patch in place
   - move or rename
   - create missing
   - archive duplicate
4. Produce a migration plan before editing.
5. Ask for confirmation before moving or renaming files.
6. Apply small patches first.
7. Validate links, docs, JSON/YAML, tests, and release workflow as applicable.
8. Report all created, modified, moved, and skipped files.

If `scripts/openarc.py` is available, start with:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

Use the scan to seed the migration plan, not to auto-move files.

## Profile-Aware Target Structure

```txt
AGENT.md or AGENTS.md
README.md
docs/
  PROJECT_BRIEF.md
  CODE_STYLE.md
  TASKS.md
  CHANGELOG_AI.md
  specs/
  plans/
  tasks/
  archive/
  PRD.md        # app/product profile when needed
  DESIGN.md     # UI/frontend/desktop/mobile profile when needed
  BRAND.md      # public brand or identity profile when needed
  assets/       # UI, brand, screenshots, or visual references when needed
    brand/
    icons/
    illustrations/
    screenshots/
    references/
```

## Rules

- Existing files win over templates.
- Repo profile controls target scope; script, CLI, automation, library, and docs-only repositories do not need design or brand scaffolding by default.
- Do not flatten useful project-specific organization.
- Do not move files only for aesthetics.
- Do not delete legacy docs unless the user explicitly confirms deletion.
- Prefer aliases, index links, or patching when moving would break references.
- Use `templates/MIGRATION.template.md` for persistent migration plans.
