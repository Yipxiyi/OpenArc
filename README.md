# OpenArc

OpenArc is an AI-native operational foundation for vibe-coded projects.

It helps developers initialize and sustain repositories where coding agents remain the primary implementation driver over time. It is not a replacement for Codex, Claude Code, OpenClaw, Cursor, or future AI coding runtimes. It gives those agents a lightweight repository memory and governance layer.

## Status

OpenArc is early-stage and intentionally lightweight.

Current plugin manifest version: `0.1.1`

Recommended next minor release after the current usability and open-source readiness work: `0.2.0` pending maintainer confirmation.

## What OpenArc Solves

- Architectural drift
- Inconsistent documentation
- Context fragmentation
- Unstable AI iteration
- Repository chaos
- Weak implementation traceability

## What OpenArc Enables

- Sustainable AI-driven development
- Long-term repository continuity
- Structured vibe coding
- Scalable AI collaboration
- Spec-driven iteration
- Lightweight governance
- Safer migration of existing workspaces
- Repeatable branch, PR, and release workflows

## Design Principles

- Lightweight over bureaucratic
- Patch-friendly over rewrite-heavy
- Repository-aware over framework-specific
- AI-first over human-only documentation
- Explicit source of truth over scattered intent
- Long-term maintainability over one-off prompting

## Quick Start

Use OpenArc when a repository needs structure before or during AI-driven implementation.

Common prompts:

```text
Use OpenArc here.
Scan this repo with OpenArc and tell me what to do first.
Initialize OpenArc governance for this repository.
Create a lightweight spec and implementation plan.
Migrate this workspace to OpenArc conventions.
Prepare this change for branch, PR, and release.
Review this repo for governance drift.
```

If you have the plugin files checked out locally, the fastest first pass is:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

For plugin maintainers, validate the plugin itself with:

```bash
python3 plugins/openarc/scripts/openarc.py doctor plugins/openarc
```

## Install In Codex

For a local Codex install, place the plugin under `~/plugins/openarc` and register it in `~/.agents/plugins/marketplace.json`.

From a repository checkout:

```bash
mkdir -p ~/plugins
cp -R plugins/openarc ~/plugins/openarc
```

Then add this entry to the `plugins` array in `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "openarc",
  "source": {
    "source": "local",
    "path": "./plugins/openarc"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Developer Tools"
}
```

Validate the local install:

```bash
python3 ~/plugins/openarc/scripts/openarc.py doctor ~/plugins/openarc
```

Restart Codex after registering the plugin. Then try:

```text
Use OpenArc here.
```

## Plugin Layout

```txt
plugins/openarc/
  .codex-plugin/
    plugin.json
  skills/
  templates/
  examples/
  assets/
  scripts/
  README.md
  CONTRIBUTING.md
  CHANGELOG.md
  LICENSE
```

The plugin manifest lives at `.codex-plugin/plugin.json`. Skills live under `skills/`, and reusable document scaffolds live under `templates/`.

## Skill Map

OpenArc is split into focused skills so agents only load the guidance needed for the current task:

| Skill | Use When |
| --- | --- |
| `openarc` | Choosing the right OpenArc workflow or handling a general "use OpenArc" request. |
| `repository-governance` | Scanning a repo, finding source-of-truth docs, and patching or creating the project agent guide. |
| `product-governance` | Creating or maintaining `docs/PRD.md` through a fixed clarification flow. |
| `spec-workflow` | Creating and maintaining versioned feature specs. |
| `planning-engine` | Creating lightweight implementation plans before coding. |
| `design-governance` | Maintaining implementation-facing design rules in `docs/DESIGN.md`. |
| `brand-governance` | Maintaining identity and communication rules in `docs/BRAND.md`. |
| `assets-governance` | Organizing assets under `docs/assets/`. |
| `implementation-workflow` | Guiding incremental implementation, validation, and documentation updates. |
| `version-governance` | Classifying requested changes as patch, minor, or major and proposing a version for confirmation. |
| `release-workflow` | Cutting or merging branches, committing, opening PRs, and triggering GitHub release updates. |
| `workspace-migration` | Migrating existing workspaces into OpenArc conventions without destructive rewrites. |
| `open-source-maintenance` | Preparing the plugin or a governed repo for public open-source maintenance. |
| `change-archive-governance` | Maintaining `docs/CHANGELOG_AI.md`, `docs/archive/`, and context-budget-aware historical memory. |

## Repository Foundation

OpenArc expects these files when relevant:

- `AGENT.md` or `AGENTS.md`
- `docs/PRD.md`
- `docs/DESIGN.md`
- `docs/BRAND.md`
- `docs/specs/*.md`
- `docs/plans/*.md`
- `docs/tasks/*.md`
- `docs/assets/*`
- `docs/CHANGELOG_AI.md`
- `docs/archive/`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `LICENSE`
- release notes or GitHub release configuration when present

Existing files always win. OpenArc should preserve intent and patch carefully instead of rewriting working repository conventions.

## Change Memory and Archive Governance

OpenArc treats AI-assisted development as a long-running collaboration.

`docs/CHANGELOG_AI.md` keeps recent AI changes visible and actionable.

`docs/archive/` stores older historical context without forcing agents to load it every session.

This keeps repositories traceable while protecting context budgets.

Recommended retention:

- keep only the last 10-20 AI-assisted entries in `docs/CHANGELOG_AI.md`
- move older entries to `docs/archive/`
- never delete historical context just to reduce context size
- read archived material only for regressions, architectural history, or prior AI decision investigation

## Helper Scripts

OpenArc includes a small dependency-free helper script:

```bash
python3 plugins/openarc/scripts/openarc.py scan <repo-root>
python3 plugins/openarc/scripts/openarc.py scan <repo-root> --format json
python3 plugins/openarc/scripts/openarc.py doctor <plugin-root>
```

Use `scan` to identify missing governance files and the next recommended OpenArc workflow.

Use `doctor` before releasing plugin changes. It checks the manifest, required public files, required templates, and skill frontmatter.

## Default Clarification Flow

When creating `docs/PRD.md`, `docs/DESIGN.md`, or `docs/BRAND.md`, do not fill unclear sections with generic guesses.

Use this fixed flow:

1. Discover existing repo signals: README, package metadata, app screens, docs, copy, design tokens, assets, and recent specs.
2. Draft a compact assumptions table with knowns, unknowns, contradictions, and risky guesses.
3. Ask the user focused questions only for material gaps.
4. Convert confirmed answers into the target document.
5. Review contradictions across PRD, DESIGN, BRAND, specs, and assets.
6. Ask for confirmation on remaining ambiguous decisions.
7. Write or patch the document only after the core intent is clear.

## Versioning Policy

OpenArc uses semantic versioning by default:

- Patch: typo fixes, copy edits, small bug fixes, docs-only refinements, non-behavioral cleanup.
- Minor: new backward-compatible features, new docs sections, new templates, new optional workflows.
- Major: breaking changes, governance model changes, incompatible API/schema changes, renamed public commands, removed behavior.

For user-requested changes, agents should classify the change, propose the next version, and ask the user to confirm the version before release work.

## Migration Policy

OpenArc migration is conservative:

- Inventory before editing.
- Map existing files to OpenArc targets.
- Patch in place when possible.
- Ask before moving, renaming, archiving, or deleting files.
- Keep legacy intent discoverable through links or notes.
- Validate links and changed formats after migration.

## Release Policy

OpenArc release work should use the repository's existing GitHub release mechanism when available.

Default flow:

1. Inspect branch and working tree.
2. Classify version impact.
3. Ask the user to confirm the proposed version.
4. Create or update a focused branch.
5. Commit with conventional commits.
6. Open a PR with validation and release notes.
7. Trigger the repo's GitHub release update mechanism.
8. Report release trigger status and any blockers.

Do not publish a final public release without maintainer confirmation unless the repository automation explicitly defines that behavior.

## Templates

Templates live in `templates/`:

- `AGENT.template.md`
- `PRD.template.md`
- `DESIGN.template.md`
- `BRAND.template.md`
- `SPEC.template.md`
- `PLAN.template.md`
- `TASKS.template.md`
- `RELEASE.template.md`
- `MIGRATION.template.md`
- `CHANGELOG_AI.template.md`
- `ARCHIVE_INDEX.template.md`

Examples live in `examples/`.

## Development

Validate changed skills with:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py plugins/openarc/skills/<skill-name>
```

Validate the plugin manifest with:

```bash
python3 -m json.tool plugins/openarc/.codex-plugin/plugin.json
```

Before opening a PR:

- Keep skill bodies concise.
- Avoid duplicate workflow instructions across skills.
- Update `CHANGELOG.md` for user-visible changes.
- Run `python3 plugins/openarc/scripts/openarc.py doctor plugins/openarc`.
- Confirm the version bump through `version-governance`.
- Verify README, manifest, and license metadata agree.

## Roadmap

Near-term improvements worth doing next:

- Add `agents/openai.yaml` metadata for each skill if the target Codex distribution uses skill chips.
- Add example migration reports for real repositories.
- Add a sample PR body generated by `release-workflow`.
- Add marketplace metadata only after the target distribution path is confirmed.

## License

OpenArc is released under the MIT License. See [LICENSE](LICENSE).
