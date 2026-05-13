---
name: openarc
description: Use when a user asks to use OpenArc generally, initialize governance, improve repository continuity, audit governance drift, migrate an existing workspace, or choose which OpenArc skill should handle a request.
---

# OpenArc Entry

Use this as the first stop when the user says "use OpenArc" or asks for repository governance without naming a specific skill.

## Fast Routing

Map the user's request to the narrowest skill:

| User Intent | Use |
| --- | --- |
| "Set up OpenArc here" | `repository-governance`, then `product-governance`, `design-governance`, `brand-governance` as needed |
| "What is missing?" / "Audit this repo" | `repository-governance`, then run the scan helper if available |
| "Write PRD" | `product-governance` |
| "Write spec" | `spec-workflow` |
| "Plan implementation" | `planning-engine` |
| "Define design system" | `design-governance` |
| "Define brand" | `brand-governance` |
| "Organize assets" | `assets-governance` |
| "Migrate existing workspace" | `workspace-migration` |
| "Version this change" | `version-governance` |
| "Branch, commit, PR, release" | `release-workflow` |
| "Prepare for open source" | `open-source-maintenance` |

## Default First Pass

For a new or unfamiliar repository:

1. Scan existing files before writing.
2. Report what already exists, what is missing, and what conflicts.
3. Recommend one of:
   - bootstrap missing governance
   - migrate existing docs
   - create one spec and plan
   - prepare branch/PR/release
4. Ask only for decisions that materially affect output.

## Helper Scripts

If this plugin's `scripts/openarc.py` is available, prefer:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
python3 plugins/openarc/scripts/openarc.py doctor plugins/openarc
```

Use script output as evidence, not as a replacement for judgment.

## Rules

- Do not load every OpenArc skill by default.
- Do not create all governance docs unless the user asks for full setup.
- Prefer a small first useful artifact over a complete governance dump.
- Existing repository conventions win over OpenArc templates.
