<p align="center">
  <img src="assets/openarc_icon.png" alt="OpenArc icon" width="112">
</p>

<h1 align="center">OpenArc</h1>

<p align="center">
  Repository memory and lightweight governance for AI coding agents.
</p>

<p align="center">
  <a href="README.zh-CN.md"><strong>中文</strong></a>
</p>

<p align="center">
  <a href="https://github.com/Yipxiyi/OpenArc/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/Yipxiyi/OpenArc?style=flat-square"></a>
  <a href="https://github.com/Yipxiyi/OpenArc/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/Yipxiyi/OpenArc/ci.yml?branch=main&style=flat-square&label=CI"></a>
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-daa520?style=flat-square"></a>
</p>

OpenArc is a plugin made of agent skills, templates, and a dependency-free repository scanner. It helps Codex, Claude Code, and Cursor preserve project intent in ordinary repository files instead of relying on old chat history.

It is not another coding agent, a background documentation bot, or a requirement to create a large docs tree. Routine work stays direct; durable artifacts are added only when they carry a real decision or coordination need.

## Why use it?

OpenArc is useful when:

- multiple agents, tools, or sessions need the same project context;
- product, architecture, design, or release decisions must survive beyond one prompt;
- an AI-built repository is starting to drift or duplicate conventions;
- you want persistent project memory without a heavyweight process framework.

## Two-minute quick start

### 1. Ask your agent to install OpenArc

Copy this prompt into Codex, Claude Code, or Cursor:

```text
Install the latest stable release of OpenArc from https://github.com/Yipxiyi/OpenArc
for the coding agent environment I am currently using.

Use this platform's supported plugin or integration method and perform all necessary
terminal steps yourself. Preserve my existing plugins, marketplaces, rules, and
configuration. Do not initialize governance or modify my current project yet.

Verify the installation, then report the installed OpenArc version, enabled status,
installation method, and whether I need to restart anything. If you are blocked,
report the exact blocker and the single smallest action I need to take.
```

For manual installation or troubleshooting, see [Install OpenArc](docs/INSTALL.md).

### 2. Start with a read-only audit

Ask your coding agent:

```text
Use OpenArc to audit this repository read-only.
Report the repo profile, required gaps, and the single smallest next action.
Do not create or modify files.
```

A successful first run reports:

- the repository profile;
- `required`, `relevant`, and `optional` governance;
- conflicts or risky assumptions found by the agent;
- one smallest next action.

The scanner itself inventories files and profiles. Semantic drift review still requires agent judgment.

### 3. Apply only what you need

When you want OpenArc to write, ask explicitly:

```text
Apply the recommended OpenArc setup for this repository.
Preserve existing conventions and keep the diff minimal.
```

Audit, review, scan, and “what is missing?” requests are read-only by default. Setup, repair, migration, implementation, release, and publish actions require matching user intent.

<p align="center">
  <img src="assets/openarc_poster.png" alt="OpenArc overview" width="900">
</p>

## How OpenArc works

1. **Inspect** — detect the repository profile, existing conventions, and sources of truth.
2. **Choose the smallest path** — direct implementation, a spec, a plan, or active tasks.
3. **Preserve what matters** — keep durable decisions in the repository and validate the result.

### Delivery paths

| Path | Use when | Durable artifact |
| --- | --- | --- |
| Direct | Scope and validation are clear; risk is routine. | None required |
| Spec | Behavior, acceptance criteria, or compatibility needs a contract. | `docs/specs/*.md` |
| Plan | Sequencing, migration, rollback, or validation needs structure. | `docs/plans/*.md` |
| Tasks | Work spans active stages, people, or agents. | `docs/TASKS.md` |

These paths are independent. A change does not need to pass through every artifact.

### Clarification gate

For broad or risky work, OpenArc asks zero to five material questions. It asks none when repository evidence is sufficient, and continues in the same turn when implementation is ready and already authorized.

## Repository model

OpenArc prefers existing repository conventions. Its canonical paths are used only when the corresponding governance is needed:

- `AGENT.md` or `AGENTS.md` for agent instructions;
- `docs/PROJECT_BRIEF.md` for durable project intent;
- `docs/CODE_STYLE.md` and `docs/ARCHITECTURE.md` for implementation guidance;
- `docs/PRD.md`, `docs/DESIGN.md`, and `docs/BRAND.md` as independent, profile-aware surfaces;
- `docs/specs/*.md`, `docs/plans/*.md`, and `docs/TASKS.md` for delivery;
- `docs/CHANGELOG_AI.md` and `docs/archive/` when project memory needs them.

An `unknown` repository profile requires only a README and one agent guide as its minimum baseline. Optional governance never makes a repository unhealthy merely because it is absent.

See the [framework reference](docs/REFERENCE.md) for profiles, scan levels, canonical paths, skill groups, templates, and package layout.

## Example requests

```text
Scan this repository with OpenArc and tell me the smallest next action.
Use OpenArc clarification-gate for this risky migration.
Create a lightweight spec for this behavior change.
Plan this migration with rollback and validation.
Migrate this workspace to OpenArc conventions without destructive rewrites.
```

## Relationship to other tools

OpenArc focuses on durable repository context. Agent workflow tools such as Superpowers focus on execution discipline inside a development session; spec-first toolkits such as GitHub Spec Kit focus on feature delivery. They can be used together.

## Documentation

- [Install OpenArc](docs/INSTALL.md)
- [Framework reference](docs/REFERENCE.md)
- [Examples](examples/)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Releases](https://github.com/Yipxiyi/OpenArc/releases)

## Contributing

Contributions should improve agent behavior without adding process for its own sake. Before opening a pull request, run:

```bash
python3 scripts/openarc.py doctor .
python3 -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for skill, version, validation, and release rules.

## License

OpenArc is released under the [MIT License](LICENSE).
