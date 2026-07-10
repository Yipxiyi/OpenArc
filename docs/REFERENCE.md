# OpenArc Reference

OpenArc keeps durable project decisions in ordinary repository files. Existing repository conventions remain authoritative; OpenArc patches or maps them instead of creating duplicate sources of truth.

## Operating model

1. Inspect the repository and identify its profile.
2. Treat audit, review, scan, and “what is missing?” requests as read-only.
3. Choose the smallest delivery path justified by the work.
4. Write governance files only for explicit setup, repair, migration, or implementation work.
5. Validate the implementation and update only the sources of truth used by the change.

### Delivery paths

| Path | Use when | Durable artifact |
| --- | --- | --- |
| Direct | Scope and validation are clear; risk is routine. | None required. |
| Spec | Behavior, acceptance criteria, or compatibility needs a contract. | `docs/specs/*.md` |
| Plan | Sequencing, migration, rollback, or validation risk needs structure. | `docs/plans/*.md` |
| Tasks | Work spans active stages, people, or agents. | `docs/TASKS.md` |

The paths are independent. A change does not need a spec, plan, and task ledger by default.

## Repository profiles and scan levels

The helper detects `script`, `library`, `app`, `plugin`, `docs`, or `unknown`.

| Profile | Required | Relevant by default |
| --- | --- | --- |
| All profiles | `README.md`; `AGENT.md` or `AGENTS.md` | Profile-dependent items below |
| `unknown` | Baseline only | None |
| `docs` | Baseline | `docs/PROJECT_BRIEF.md` |
| `script` | Baseline | `docs/PROJECT_BRIEF.md`, `docs/CODE_STYLE.md` |
| `library` | Baseline | Script items plus `docs/ARCHITECTURE.md` |
| `plugin` | Baseline | Script items plus `docs/ARCHITECTURE.md` |
| `app` | Baseline | Script items plus `docs/ARCHITECTURE.md`, `docs/PRD.md`, and `docs/DESIGN.md` |

Scan levels mean:

- `required`: the minimum baseline for the detected profile.
- `relevant`: supported by the profile or current repository signals.
- `optional`: useful only when the repository or requested work needs it; absence is not unhealthy.

`docs/BRAND.md` becomes relevant only when brand evidence already exists. `docs/DESIGN.md` and brand governance are evaluated independently. Asset directories remain optional.

The scan reports file presence and a next action. It is evidence, not a semantic review: a present file may still be stale, contradictory, or empty.

## Canonical paths

Use these locations only when the corresponding governance is needed:

| Concern | Canonical path |
| --- | --- |
| Agent instructions | `AGENT.md` or `AGENTS.md` |
| Project intent | `docs/PROJECT_BRIEF.md` |
| Code conventions | `docs/CODE_STYLE.md` |
| Architecture | `docs/ARCHITECTURE.md` |
| Product requirements | `docs/PRD.md` |
| UI and component rules | `docs/DESIGN.md` |
| Brand, naming, and voice | `docs/BRAND.md` |
| Feature contracts | `docs/specs/*.md` |
| Implementation plans | `docs/plans/*.md` |
| Active coordination | `docs/TASKS.md` |
| Recent AI changes | `docs/CHANGELOG_AI.md` |
| Older decision history | `docs/archive/` |
| Optional working assets | `docs/assets/` |
| Public release history | `CHANGELOG.md` |

`docs/TASKS.md` is the single active task ledger. Do not recreate `docs/SPEC.md`, `docs/tasks/*`, or parallel intake trees as competing sources of truth.

## Skill groups

| Group | Skills |
| --- | --- |
| Routing and discovery | [`openarc`](../skills/openarc/SKILL.md), [`repository-governance`](../skills/repository-governance/SKILL.md), [`clarification-gate`](../skills/clarification-gate/SKILL.md) |
| Intent and continuity | [`product-governance`](../skills/product-governance/SKILL.md), [`design-governance`](../skills/design-governance/SKILL.md), [`brand-governance`](../skills/brand-governance/SKILL.md), [`assets-governance`](../skills/assets-governance/SKILL.md), [`change-archive-governance`](../skills/change-archive-governance/SKILL.md) |
| Delivery | [`spec-workflow`](../skills/spec-workflow/SKILL.md), [`planning-engine`](../skills/planning-engine/SKILL.md), [`implementation-workflow`](../skills/implementation-workflow/SKILL.md), [`workspace-migration`](../skills/workspace-migration/SKILL.md) |
| Release and maintenance | [`version-governance`](../skills/version-governance/SKILL.md), [`release-workflow`](../skills/release-workflow/SKILL.md), [`open-source-maintenance`](../skills/open-source-maintenance/SKILL.md) |

Load the narrowest skill for the request. Do not load the whole set by default.

## Package layout

```text
OpenArc/
├── .agents/plugins/marketplace.json
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── skills/*/SKILL.md
├── templates/*.template.md
├── examples/
├── integrations/cursor/
├── scripts/openarc.py
├── assets/
├── docs/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

- `.agents/plugins/marketplace.json` exposes the pinned GitHub release to Codex.
- `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` describe the same plugin and must keep version parity.
- `skills/` contains routeable instructions.
- `templates/` contains optional scaffolds, not mandatory repository output.
- `examples/` shows filled artifacts.
- `integrations/cursor/` contains the Cursor adapters.
- `scripts/openarc.py` provides dependency-free `scan` and `doctor` commands.

## Templates

| Template | Intended target |
| --- | --- |
| [`AGENT.template.md`](../templates/AGENT.template.md) | `AGENT.md` or adapted `AGENTS.md` |
| [`CODE_STYLE.template.md`](../templates/CODE_STYLE.template.md) | `docs/CODE_STYLE.md` |
| [`PRD.template.md`](../templates/PRD.template.md) | `docs/PRD.md` |
| [`DESIGN.template.md`](../templates/DESIGN.template.md) | `docs/DESIGN.md` |
| [`BRAND.template.md`](../templates/BRAND.template.md) | `docs/BRAND.md` |
| [`SPEC.template.md`](../templates/SPEC.template.md) | `docs/specs/<feature>.md` |
| [`PLAN.template.md`](../templates/PLAN.template.md) | `docs/plans/<feature>.md` |
| [`TASKS.template.md`](../templates/TASKS.template.md) | `docs/TASKS.md` |
| [`RELEASE.template.md`](../templates/RELEASE.template.md) | Release preparation when needed |
| [`MIGRATION.template.md`](../templates/MIGRATION.template.md) | Migration plan when needed |
| [`CHANGELOG_AI.template.md`](../templates/CHANGELOG_AI.template.md) | `docs/CHANGELOG_AI.md` |
| [`ARCHIVE_INDEX.template.md`](../templates/ARCHIVE_INDEX.template.md) | `docs/archive/` index |

Start from repository evidence and delete irrelevant template sections. Examples are available in [`examples/`](../examples/).

## Commands

See [Install OpenArc](INSTALL.md) for installation and root-versus-vendored command paths. Contributors should use the validation gates in [CONTRIBUTING.md](../CONTRIBUTING.md).
