<p align="center">
  <img src="assets/openarc_icon.png" alt="OpenArc icon" width="120">
</p>

<h1 align="center">OpenArc</h1>

<p align="center">
  <a href="#english"><strong>English</strong></a> ·
  <a href="#中文说明"><strong>中文</strong></a>
</p>

<p align="center">
  <img alt="OpenArc" src="https://img.shields.io/badge/OpenArc-AI%20governance-1685d9?style=for-the-badge&labelColor=4a4a4a">
  <img alt="Codex plugin" src="https://img.shields.io/badge/Codex-plugin-2563eb?style=for-the-badge&labelColor=4a4a4a">
  <img alt="Claude Code plugin" src="https://img.shields.io/badge/Claude%20Code-plugin-7c3aed?style=for-the-badge&labelColor=4a4a4a">
  <img alt="Cursor rules" src="https://img.shields.io/badge/Cursor-rules-111827?style=for-the-badge&labelColor=4a4a4a">
  <img alt="Version 0.6.0" src="https://img.shields.io/badge/version-0.6.0-84cc16?style=for-the-badge&labelColor=4a4a4a">
  <img alt="License MIT" src="https://img.shields.io/badge/license-MIT-daa520?style=for-the-badge&labelColor=4a4a4a">
</p>

<p align="center">
  <img src="assets/openarc_poster.png" alt="OpenArc introduction poster">
</p>

<a id="english"></a>

## English

OpenArc is a governance framework for repositories built with AI coding agents.

It turns a fast-moving vibe-coded project into a repository that agents can understand, extend, and maintain over time. Instead of relying on long chat history or tribal knowledge, OpenArc gives the repo its own lightweight operating system: source-of-truth docs, specs, plans, design rules, release guidance, and recent AI change memory.

OpenArc is not another coding agent. It is the project layer that helps Codex, Claude Code, Cursor, and other tools work from the same map.

## Why OpenArc

AI can move fast, but repositories drift when intent only lives in prompts.

OpenArc is built for teams and solo builders who want AI-assisted development without losing:

- product intent
- architectural direction
- design consistency
- implementation traceability
- release discipline
- reusable project memory
- context efficiency across long-running work

## How the Framework Works

OpenArc gives a repository a small set of durable coordination surfaces:

| Layer | Purpose |
| --- | --- |
| Repository guide | Tells agents how to work in this repo and where source-of-truth docs live. |
| Clarification gate | Asks 0-5 material questions for broad or ambiguous work, then continues immediately when the work is ready and authorized. |
| Profile-aware product, code style, design, and brand docs | Preserve only the governance supported by repository evidence; UI and brand are evaluated independently. |
| Direct, spec, plan, or task path | Implements routine work directly and adds only the delivery artifact justified by risk or coordination. |
| Component pattern governance | Helps agents reuse UI patterns instead of creating duplicate components. |
| Change memory and archive | Keeps recent AI work visible while moving older context out of the active path. |
| Release and version guidance | Keeps user-visible changes aligned with semantic versioning and changelog hygiene. |

## Core Capabilities

- Initialize governance for a new or existing repo.
- Audit an AI-built workspace for missing structure and drift.
- Clarify broad, ambiguous, risky, or new work with 0-5 material questions.
- Implement routine, low-risk work directly; add PRDs, specs, plans, or tasks only when they carry a real decision or coordination need.
- Capture code style preferences in `docs/CODE_STYLE.md`.
- Preserve reusable component patterns in `docs/DESIGN.md`.
- Migrate existing projects without destructive rewrites.
- Keep recent AI-assisted changes traceable through `docs/CHANGELOG_AI.md`.
- Package the same framework for Codex, Claude Code, and Cursor-based workflows.

## Who It Is For

OpenArc is useful when:

- AI agents are a primary implementation path.
- A project is growing beyond one-off prompts.
- Multiple agents, tools, or sessions need consistent context.
- Product, design, and architecture decisions need to survive across iterations.
- You want structure without adopting a heavyweight process framework.

It is intentionally lightweight: the goal is to make the next AI-assisted change easier, not turn a small project into a documentation program.

## How OpenArc Compares

OpenArc sits beside agent workflow tools and spec-first toolkits. It focuses on the repository layer: the durable structure that survives across agents, sessions, and implementation cycles.

| Project | Primary Focus | Best At | Where OpenArc Is Different |
| --- | --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | Agent development methodology | Brainstorming, planning, TDD, debugging, code review, subagent workflows, and finish-the-branch discipline. | OpenArc is not mainly about single-session agent behavior. It gives the repository a persistent governance model: PRD, design, brand, specs, plans, component patterns, change memory, archive policy, migration, and release guidance. |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Spec-Driven Development toolkit | A strong Spec -> Plan -> Tasks -> Implement workflow, CLI setup, templates, checklists, extensions, presets, and broad agent integrations. | OpenArc covers more than the feature-spec pipeline. It treats the repo as a long-running AI collaboration surface, including product/design/brand governance, reusable component rules, AI change memory, archive hygiene, migration, and release/version workflows. |
| OpenArc | Repository governance for AI-built projects | Making an AI-assisted repo understandable, repeatable, and maintainable across tools and time. | OpenArc is deliberately small and repo-native. It can work with Superpowers for agent discipline or Spec Kit for spec-driven execution, while keeping the broader repository memory and governance layer intact. |

Use OpenArc when you want the project itself to stay coherent, not just the next coding session or the next feature spec.

## Q&A

**Is OpenArc a replacement for Superpowers or Spec Kit?**  
No. Superpowers improves agent behavior during development. Spec Kit provides a spec-driven implementation workflow. OpenArc gives the repository a persistent governance and memory layer. They can be used together.

**Why use OpenArc if Spec Kit already has specs, plans, and tasks?**  
Spec Kit is excellent when the center of gravity is the feature delivery pipeline. OpenArc keeps that pipeline connected to broader repo governance: product intent, design rules, brand language, component reuse, change memory, migration policy, and release/version discipline.

**Why use OpenArc if Superpowers already guides the agent?**  
Superpowers is about agent execution discipline. OpenArc is about durable repository memory. If you use both, Superpowers can drive disciplined execution while OpenArc provides the project map.

**Does OpenArc force a heavy process?**  
No. The default bias is small, patch-friendly, and incremental. Add only the governance surfaces that make the next AI-assisted change safer.

**Does OpenArc automatically update docs?**  
No background automation is assumed. OpenArc defines explicit rules for agents: inspect existing docs, update relevant source-of-truth files, and keep reusable patterns in the right place.

**Can OpenArc be added to an existing repo?**  
Yes. The migration workflow is conservative: inventory first, preserve existing conventions, patch in place, and avoid destructive rewrites.

## Quick Start

Best practice: install OpenArc before starting a new project. Let OpenArc initialize the repository framework first, then begin product and implementation work on top of that structure.

Ask your coding agent to start with OpenArc:

```text
Use OpenArc here.
Scan this repo with OpenArc and tell me what to do first.
Initialize OpenArc governance for this repository.
Use OpenArc clarification-gate for this new requirement before implementation.
Create a lightweight spec and implementation plan.
Migrate this workspace to OpenArc conventions.
Review this repo for governance drift.
```

From this repository or an unpacked OpenArc package, run:

```bash
python3 scripts/openarc.py scan <repo-root>
```

If OpenArc is vendored under another repository at `plugins/openarc`, run:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

## Install in Codex

Codex installs plugins from a marketplace snapshot; copying the files alone does not install or enable OpenArc.

### First local install

Sync the package to one exact directory. The trailing slashes and `--delete` prevent nested copies and stale files.

From the OpenArc repository root:

```bash
mkdir -p ~/plugins/openarc
rsync -a --delete --delete-excluded --exclude '.git/' ./ ~/plugins/openarc/
```

From a monorepo or vendored checkout where OpenArc lives at `plugins/openarc`:

```bash
mkdir -p ~/plugins/openarc
rsync -a --delete --delete-excluded --exclude '.git/' plugins/openarc/ ~/plugins/openarc/
```

Add this entry once to the `plugins` array in `~/.agents/plugins/marketplace.json`:

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

Register the marketplace root once, then perform the actual plugin install:

```bash
codex plugin marketplace list
codex plugin marketplace add ~
codex plugin add openarc@local-codex-plugins
```

Skip `marketplace add` when `local-codex-plugins` is already listed.

Validate both the package and installed state:

```bash
python3 ~/plugins/openarc/scripts/openarc.py doctor ~/plugins/openarc
codex plugin list --marketplace local-codex-plugins
```

Restart Codex after installation. Then try:

```text
Use OpenArc here.
```

### Upgrade an existing local install

Sync the new package with the same `rsync` command above, then refresh Codex's installed snapshot and verify the reported version:

```bash
codex plugin remove openarc@local-codex-plugins
codex plugin add openarc@local-codex-plugins
codex plugin list --marketplace local-codex-plugins
```

## Install in Claude Code

OpenArc includes a Claude Code plugin manifest at `.claude-plugin/plugin.json` and reuses the same `skills/` directory.

From the OpenArc repository root:

```bash
claude --plugin-dir .
```

From a monorepo or vendored checkout where OpenArc lives at `plugins/openarc`:

```bash
claude --plugin-dir ./plugins/openarc
```

For a standalone package copied to `~/plugins/openarc`:

```bash
claude --plugin-dir ~/plugins/openarc
```

Then try the namespaced entry skill:

```text
/openarc:openarc
```

If OpenArc is published through a Claude Code plugin source, install it with Claude Code's `/plugin` flow and restart Claude Code after enabling the plugin.

## Install in Cursor

Cursor does not install Codex or Claude Code plugins directly. Use the OpenArc Cursor adapter files instead.

The default installation is a Cursor Project Rule. From the OpenArc repository root:

```bash
mkdir -p <target-repo>/.cursor/rules
cp integrations/cursor/openarc.mdc <target-repo>/.cursor/rules/openarc.mdc
```

From a vendored checkout:

```bash
mkdir -p .cursor/rules
cp plugins/openarc/integrations/cursor/openarc.mdc .cursor/rules/openarc.mdc
```

Optionally use the root-instruction adapter only when the target has no `AGENTS.md`:

```bash
cp -n integrations/cursor/AGENTS.md <target-repo>/AGENTS.md
```

For a vendored checkout:

```bash
cp -n plugins/openarc/integrations/cursor/AGENTS.md ./AGENTS.md
```

If `AGENTS.md` already exists, `cp -n` leaves it untouched; merge only the relevant OpenArc rules into the existing file instead of replacing it.

Then ask Cursor Agent:

```text
Use OpenArc here.
```

Prefer `.cursor/rules/openarc.mdc`. Use `AGENTS.md` only when a single shared project-wide instruction file is intentional.

## Plugin Layout

```txt
plugins/openarc/
  .codex-plugin/
    plugin.json
  .claude-plugin/
    plugin.json
  skills/
  templates/
  examples/
  integrations/
  assets/
  scripts/
  README.md
  CONTRIBUTING.md
  CHANGELOG.md
  LICENSE
```

The Codex plugin manifest lives at `.codex-plugin/plugin.json`. The Claude Code plugin manifest lives at `.claude-plugin/plugin.json`. Skills live under `skills/`, Cursor adapters live under `integrations/cursor/`, and reusable document scaffolds live under `templates/`.

## What Is Included

OpenArc is packaged as focused skills, templates, examples, and lightweight adapters. Each skill covers one governance job, so agents can load the right guidance without pulling the whole framework into context.

| Skill | What It Provides |
| --- | --- |
| `openarc` | Entry routing for general OpenArc requests. |
| `clarification-gate` | Focused goal, non-goal, constraint, and target-doc clarification before PRD, spec, plan, or implementation work. |
| `repository-governance` | Repository scan, source-of-truth discovery, and agent guide setup. |
| `product-governance` | PRD creation and product-intent clarification. |
| `spec-workflow` | Durable feature specs when behavior, acceptance criteria, or compatibility needs a contract. |
| `planning-engine` | Lightweight plans when sequencing, migration, rollback, or validation needs structure. |
| `design-governance` | UI implementation rules, component standards, and design consistency. |
| `brand-governance` | Product voice, naming, identity, and communication style. |
| `assets-governance` | Optional asset organization under `docs/assets/` when assets exist or organization is requested. |
| `implementation-workflow` | Risk-scaled direct or documented implementation, validation, and documentation sync. |
| `version-governance` | Semantic version classification and release impact guidance. |
| `release-workflow` | Branch, commit, PR, and release-note preparation. |
| `workspace-migration` | Conservative migration of existing workspaces into OpenArc conventions. |
| `open-source-maintenance` | Public README, contribution, license, and changelog readiness. |
| `change-archive-governance` | AI change memory, archive policy, and context-budget control. |

## Design System Continuity

OpenArc helps teams avoid the common "new request, new component" failure mode in AI-built interfaces.

The design governance layer gives UI work a reusable-component loop:

- existing design rules and components are checked before a new component is introduced
- components that already cover roughly 70-80% of the use case are reused or extended
- new components are reserved for cases where reuse would make the existing component unclear, brittle, or over-generalized
- reusable component patterns are recorded in `docs/DESIGN.md`
- one-off component decisions stay with the change context instead of bloating the design guide

`docs/DESIGN.md` is meant to document stable reusable patterns, not every component in the codebase.

## Repository Memory Model

OpenArc uses ordinary repository files as durable memory. Agents read only what is relevant, and the helper scan classifies repositories as `script`, `library`, `app`, `plugin`, `docs`, or `unknown` before recommending governance files.

Canonical locations when used:

- `AGENT.md` or `AGENTS.md`
- `docs/CODE_STYLE.md`
- `docs/specs/*.md` for feature specs
- `docs/plans/*.md`
- `docs/TASKS.md` as the single active task ledger
- `docs/CHANGELOG_AI.md`
- `docs/archive/`

Independent conditional surfaces:

- `docs/PRD.md` for product or app repositories.
- `docs/DESIGN.md` for UI, frontend, desktop, mobile, or component work.
- `docs/BRAND.md` for public brand, identity, marketing, naming, or copy work, independently of UI signals.

`docs/assets/*` is optional. Use it only when assets already exist or the user explicitly requests asset organization. An `unknown` profile requires only `README.md` and one agent guide; it does not assume app, UI, brand, spec, plan, task, or archive governance.

Pure script, CLI, automation, library, and docs-only repositories do not need design or brand scaffolding by default.

For public or open-source repositories, OpenArc can also inspect release and maintenance files:

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `LICENSE`

Existing files always win. OpenArc favors preserving intent and patching carefully over replacing working conventions.

## Delivery Paths

OpenArc stops at the smallest path that safely carries the work:

- Direct: routine, low-risk work with clear scope and validation.
- Spec: behavior, acceptance criteria, or compatibility needs a durable contract in `docs/specs/*.md`.
- Plan: sequencing, migration, rollback, or validation risk needs structure in `docs/plans/*.md`.
- Tasks: active multi-step coordination needs the single `docs/TASKS.md` ledger.

These paths are selected independently; a change does not need to pass through every artifact.

## Change Memory and Archive Governance

OpenArc treats AI-assisted development as a long-running collaboration.

`docs/CHANGELOG_AI.md` keeps recent AI changes visible and actionable.

`docs/archive/` stores older historical context without forcing agents to load it every session.

This keeps repositories traceable while protecting context budgets.

Recommended retention model:

- `docs/CHANGELOG_AI.md` stays focused on the latest 10-20 AI-assisted entries
- older entries move into `docs/archive/`
- historical context remains available instead of being deleted for context-budget reasons
- archived material is reserved for regressions, architectural history, or prior AI decision investigation

## Helper Scripts

OpenArc includes a small dependency-free helper script:

```bash
python3 plugins/openarc/scripts/openarc.py scan <repo-root>
python3 plugins/openarc/scripts/openarc.py scan <repo-root> --format json
python3 plugins/openarc/scripts/openarc.py doctor <plugin-root>
```

`scan` identifies the repo profile and reports governance as `required`, `relevant`, or `optional`. Required gaps belong to the minimal profile baseline, relevant items depend on repository signals or current work, and optional items never make the repository unhealthy. The `unknown` profile requires only `README.md` and one agent guide; UI and brand signals are evaluated independently, and assets remain optional.

`doctor` validates the plugin package before publication by checking manifests, required public files, required templates, integration adapters, and skill frontmatter.

## Clarification Gate

OpenArc treats broad, ambiguous, risky, or new work as clarification-first. Routine work with clear scope and validation can proceed directly. The Clarification Gate keeps PRDs, specs, plans, code style, design, and brand docs grounded in repository evidence and confirmed decisions instead of vague filler.

When the repo profile or user request calls for a new PRD, spec, plan, code style decision, design guide, or brand guidance, the workflow is:

1. Discover existing repo signals: README, package metadata, app screens, code style config, docs, copy, design tokens, assets, and recent specs.
2. Separate known facts, unknowns, contradictions, and risky assumptions.
3. Ask 0-5 material questions that cannot be answered from the repository; ask none when evidence is sufficient.
4. Give each question a recommended answer and trade-off.
5. When readiness is `ready` and implementation is already authorized, continue in the same turn instead of asking the user to say "continue."
6. Convert confirmed decisions into the smallest existing target: PRD, `docs/specs/*.md`, plan, `docs/TASKS.md`, changelog, code style, design, or brand.
7. Leave remaining ambiguity visible instead of hiding it in generic prose.

OpenArc does not create ADRs by default. ADRs are only suggested when a decision is hard to reverse, surprising without context, and the result of a real trade-off.

## Versioning Policy

OpenArc uses semantic versioning by default:

- Patch: typo fixes, copy edits, small bug fixes, docs-only refinements, non-behavioral cleanup.
- Minor: new backward-compatible features, new docs sections, new templates, new optional workflows.
- Major: breaking changes, governance model changes, incompatible API/schema changes, renamed public commands, removed behavior.

For release-visible changes, OpenArc records the version impact before release work begins.

## Migration Policy

OpenArc migration is conservative:

- Inventory before editing.
- Map existing files to OpenArc targets.
- Patch in place when possible.
- Ask before moving, renaming, archiving, or deleting files.
- Keep legacy intent discoverable through links or notes.
- Validate links and changed formats after migration.

## Templates

Templates live in `templates/`:

- `AGENT.template.md`
- `CODE_STYLE.template.md`
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

## Contributing

Contributions are welcome. If you have ideas, fixes, migration examples, or workflow improvements for OpenArc, feel free to open an issue or pull request.

## License

OpenArc is released under the MIT License. See [LICENSE](LICENSE).

---

<a id="中文说明"></a>

## 中文说明

OpenArc 是面向 AI 编程仓库的治理框架。

它把快速推进的 vibe-coded 项目，变成 agent 能长期理解、扩展和维护的仓库。你不需要把产品意图、架构选择和设计规则都塞在聊天记录里；OpenArc 把这些上下文沉淀为仓库自己的轻量操作系统：事实来源文档、规格、计划、设计规则、发布指引和近期 AI 变更记忆。

OpenArc 不是另一个编程 agent。它是项目层框架，让 Codex、Claude Code、Cursor 和其他 AI 编程工具从同一张地图出发。

## 为什么需要 OpenArc

AI 可以很快写代码，但如果意图只存在于提示词里，仓库会很快漂移。

OpenArc 适合希望继续保持 AI 开发速度，同时不丢掉这些东西的项目：

- 产品意图
- 架构方向
- 设计一致性
- 实现可追溯性
- 发布纪律
- 可复用的项目记忆
- 长期迭代中的上下文效率

## 框架如何工作

OpenArc 给仓库提供一组稳定、轻量的协作界面：

| 层级 | 作用 |
| --- | --- |
| 仓库 agent guide | 告诉 agent 如何在这个仓库工作，以及事实来源文档在哪里。 |
| 澄清关卡 | 对宽泛或模糊工作询问 0-5 个关键问题；工作已就绪且已获授权时立即继续。 |
| 自适应产品、代码风格、设计、品牌文档 | 只保留仓库证据支持的治理内容；UI 与品牌信号独立判断。 |
| 直接实现、spec、plan 或 task 路径 | 日常改动直接实现，只增加风险或协作真正需要的交付文档。 |
| 组件模式治理 | 帮助 agent 复用 UI 模式，而不是重复造相似组件。 |
| 变更记忆和归档 | 让近期 AI 工作保持可见，同时把旧上下文移出活跃路径。 |
| 发布和版本指引 | 让用户可见变更、语义化版本和 changelog 保持一致。 |

## 核心能力

- 为新仓库或已有仓库初始化治理结构。
- 审计 AI 构建的工作区，识别结构缺口和漂移。
- 对宽泛、模糊、高风险或全新工作询问 0-5 个关键问题。
- 日常低风险改动直接实现；只有确实承载决策或协作需要时才增加 PRD、spec、plan 或 task。
- 将代码风格偏好沉淀到 `docs/CODE_STYLE.md`。
- 将可复用组件模式沉淀到 `docs/DESIGN.md`。
- 在不破坏已有结构的前提下迁移项目。
- 通过 `docs/CHANGELOG_AI.md` 保留近期 AI 参与变更。
- 同一套框架可用于 Codex、Claude Code 和 Cursor 工作流。

## 适用对象

OpenArc 适合这些项目：

- AI agent 是主要实现路径之一。
- 项目已经不再只是一次性提示词实验。
- 多个 agent、工具或会话需要稳定上下文。
- 产品、设计和架构决策需要跨迭代保留下来。
- 想要结构，但不想引入重型流程框架。

OpenArc 刻意保持轻量：目标是让下一次 AI 辅助变更更容易，而不是把小项目变成文档工程。

## OpenArc 和其他项目的区别

OpenArc 和 agent 工作流工具、spec-first 工具链是并列关系。它关注的是仓库层：那些能跨 agent、跨会话、跨实现周期保留下来的长期结构。

| 项目 | 核心定位 | 最擅长 | OpenArc 的差异 |
| --- | --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | Agent 开发方法论 | 脑暴、计划、TDD、系统化调试、代码评审、subagent 工作流和收尾分支纪律。 | OpenArc 的重点不是单次会话里的 agent 行为，而是给仓库提供持久治理模型：PRD、设计、品牌、specs、plans、组件模式、变更记忆、归档策略、迁移和发布指引。 |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Spec-Driven Development 工具包 | 强规格驱动流程：Spec -> Plan -> Tasks -> Implement，配套 CLI、模板、检查清单、扩展、preset 和多 agent 集成。 | OpenArc 不只覆盖功能规格流水线。它把仓库视为长期 AI 协作界面，包含产品/设计/品牌治理、组件复用规则、AI 变更记忆、归档卫生、迁移策略和发布/版本流程。 |
| OpenArc | AI 构建项目的仓库治理框架 | 让 AI 辅助仓库跨工具、跨时间保持可理解、可复用、可维护。 | OpenArc 刻意保持小而 repo-native。它可以和 Superpowers 一起提供 agent 执行纪律，也可以和 Spec Kit 一起推进规格驱动实现，同时保留更完整的仓库记忆和治理层。 |

当你关心的不只是下一次编码会话或下一份功能 spec，而是整个项目长期保持一致时，就需要 OpenArc。

## Q&A

**OpenArc 是 Superpowers 或 Spec Kit 的替代品吗？**  
不是。Superpowers 改善 agent 在开发过程中的行为，Spec Kit 提供规格驱动实现流程，OpenArc 给仓库提供持久治理和记忆层。它们可以一起使用。

**Spec Kit 已经有 spec、plan、task，为什么还需要 OpenArc？**  
Spec Kit 很适合以功能交付流水线为中心的团队。OpenArc 解决的是更宽的仓库治理问题：产品意图、设计规则、品牌语言、组件复用、变更记忆、迁移策略和发布/版本纪律。

**Superpowers 已经能指导 agent，为什么还需要 OpenArc？**  
Superpowers 关注 agent 执行纪律。OpenArc 关注持久仓库记忆。一起使用时，Superpowers 负责执行纪律，OpenArc 提供项目地图。

**OpenArc 会不会变成重流程？**  
不会。默认原则是小步、可 patch、增量治理。只引入能让下一次 AI 辅助变更更安全的结构。

**OpenArc 会自动更新文档吗？**  
不会假设后台自动化。OpenArc 提供的是清晰的维护约定：基于现有文档和代码更新事实来源文件，并把可复用模式放在正确位置。

**已有项目可以接入 OpenArc 吗？**  
可以。迁移策略是保守的：先盘点，保留已有约定，能原地 patch 就不重写，避免破坏性迁移。

## 快速开始

最佳实践：在启动新项目前先安装 OpenArc。先让 OpenArc 在 repo 工作区内搭建好治理框架，再在这个结构上开始产品和实现开发。

让你的编程 agent 从 OpenArc 开始：

```text
Use OpenArc here.
Scan this repo with OpenArc and tell me what to do first.
Initialize OpenArc governance for this repository.
Use OpenArc clarification-gate for this new requirement before implementation.
Create a lightweight spec and implementation plan.
Migrate this workspace to OpenArc conventions.
Review this repo for governance drift.
```

从 OpenArc 仓库根目录或解压后的 OpenArc 包中执行：

```bash
python3 scripts/openarc.py scan <repo-root>
```

如果 OpenArc 作为目标仓库里的 `plugins/openarc` 子目录存在，则执行：

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

## 在 Codex 中安装

Codex 从 marketplace snapshot 安装插件；只复制文件并不会安装或启用 OpenArc。

### 首次本地安装

把插件同步到唯一目标目录。命令中的尾部斜杠和 `--delete` 可避免目录嵌套与旧文件残留。

从 OpenArc 仓库根目录执行：

```bash
mkdir -p ~/plugins/openarc
rsync -a --delete --delete-excluded --exclude '.git/' ./ ~/plugins/openarc/
```

如果 OpenArc 位于 monorepo 或目标仓库的 `plugins/openarc`：

```bash
mkdir -p ~/plugins/openarc
rsync -a --delete --delete-excluded --exclude '.git/' plugins/openarc/ ~/plugins/openarc/
```

把下面条目一次性加入 `~/.agents/plugins/marketplace.json` 的 `plugins` 数组：

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

一次性注册 marketplace 根目录，然后执行真正的插件安装：

```bash
codex plugin marketplace list
codex plugin marketplace add ~
codex plugin add openarc@local-codex-plugins
```

如果 `local-codex-plugins` 已在列表中，跳过 `marketplace add`。

同时校验插件包和安装状态：

```bash
python3 ~/plugins/openarc/scripts/openarc.py doctor ~/plugins/openarc
codex plugin list --marketplace local-codex-plugins
```

安装后重启 Codex，然后尝试：

```text
Use OpenArc here.
```

### 升级已有本地安装

先用上面同一条 `rsync` 命令同步新版本，再刷新 Codex 的已安装 snapshot，并核对显示的版本：

```bash
codex plugin remove openarc@local-codex-plugins
codex plugin add openarc@local-codex-plugins
codex plugin list --marketplace local-codex-plugins
```

## 在 Claude Code 中安装

OpenArc 已包含 Claude Code 插件 manifest：`.claude-plugin/plugin.json`，并复用同一套 `skills/` 目录。

从 OpenArc 仓库根目录执行：

```bash
claude --plugin-dir .
```

如果 OpenArc 位于 monorepo 或目标仓库的 `plugins/openarc`：

```bash
claude --plugin-dir ./plugins/openarc
```

如果已复制为独立包 `~/plugins/openarc`：

```bash
claude --plugin-dir ~/plugins/openarc
```

然后尝试带命名空间的入口 skill：

```text
/openarc:openarc
```

如果 OpenArc 通过 Claude Code plugin source 发布，使用 Claude Code 的 `/plugin` 流程安装，启用后重启 Claude Code。

## 在 Cursor 中安装

Cursor 不能直接安装 Codex 或 Claude Code 插件。OpenArc 提供 Cursor 适配文件。

默认安装 Cursor Project Rule。从 OpenArc 仓库根目录执行：

```bash
mkdir -p <target-repo>/.cursor/rules
cp integrations/cursor/openarc.mdc <target-repo>/.cursor/rules/openarc.mdc
```

如果 OpenArc 位于目标仓库的 `plugins/openarc`：

```bash
mkdir -p .cursor/rules
cp plugins/openarc/integrations/cursor/openarc.mdc .cursor/rules/openarc.mdc
```

只有目标仓库不存在 `AGENTS.md` 时，才可选使用项目级指令适配文件：

```bash
cp -n integrations/cursor/AGENTS.md <target-repo>/AGENTS.md
```

如果 OpenArc 位于目标仓库的 `plugins/openarc`：

```bash
cp -n plugins/openarc/integrations/cursor/AGENTS.md ./AGENTS.md
```

如果 `AGENTS.md` 已存在，`cp -n` 会保持原文件不变；应把必要的 OpenArc 规则合并到现有文件，而不是覆盖它。

然后在 Cursor Agent 中输入：

```text
Use OpenArc here.
```

优先使用 `.cursor/rules/openarc.mdc`。只有明确需要一个共享的项目级指令文件时才使用 `AGENTS.md`。

## 插件结构

```txt
plugins/openarc/
  .codex-plugin/
    plugin.json
  .claude-plugin/
    plugin.json
  skills/
  templates/
  examples/
  integrations/
  assets/
  scripts/
  README.md
  CONTRIBUTING.md
  CHANGELOG.md
  LICENSE
```

Codex 插件 manifest 位于 `.codex-plugin/plugin.json`。Claude Code 插件 manifest 位于 `.claude-plugin/plugin.json`。Skills 位于 `skills/`，Cursor 适配文件位于 `integrations/cursor/`，可复用文档模板位于 `templates/`。

## Skill 列表

OpenArc 被拆分为多个职责明确的 skills，避免 agent 每次加载不必要的上下文：

| Skill | 使用场景 |
| --- | --- |
| `openarc` | 用户泛泛要求使用 OpenArc，或需要选择正确流程。 |
| `clarification-gate` | 在 PRD、spec、plan 或实现前澄清目标、非目标、约束和目标文档。 |
| `repository-governance` | 扫描仓库、识别事实来源文档、创建或修补 agent guide。 |
| `product-governance` | 通过固定澄清流程创建或维护 `docs/PRD.md`。 |
| `spec-workflow` | 当行为、验收标准或兼容性需要持久合同时创建和维护功能规格文档。 |
| `planning-engine` | 当执行顺序、迁移、回滚或验证需要结构时创建轻量计划。 |
| `design-governance` | 维护 `docs/DESIGN.md` 中面向实现的设计规则。 |
| `brand-governance` | 维护 `docs/BRAND.md` 中的身份、语气和表达规则。 |
| `assets-governance` | 已有资产或明确要求整理时，可选组织 `docs/assets/` 下的资产。 |
| `implementation-workflow` | 按风险选择直接或文档化实现，并指导验证和文档同步。 |
| `version-governance` | 判断变更属于 patch、minor 还是 major，并提出版本建议。 |
| `release-workflow` | 管理分支、commit、PR 和发布说明准备。 |
| `workspace-migration` | 将已有工作区迁移到 OpenArc 规范，避免破坏性重写。 |
| `open-source-maintenance` | 准备插件或被治理仓库的开源维护材料。 |
| `change-archive-governance` | 维护 `docs/CHANGELOG_AI.md`、`docs/archive/`，让历史记录可追溯但不挤占上下文。 |

## 组件模式治理

OpenArc 帮助团队避免 AI 构建界面里常见的“一个新需求，一个新组件”问题。

设计治理层提供的是一个可复用组件循环：

- 新组件出现前，会先检查既有设计规则和组件
- 已覆盖约 70%-80% 场景的组件会被复用或扩展
- 新组件只用于复用会导致既有组件不清晰、脆弱或过度泛化的场景
- 可复用组件模式会沉淀到 `docs/DESIGN.md`
- 一次性组件决策保留在本次变更上下文中，避免设计指南膨胀

`docs/DESIGN.md` 应记录稳定可复用模式，而不是把代码库里的每个组件都列一遍。

## 仓库治理基础文件

OpenArc 使用普通仓库文件作为持久记忆。Agent 只读取相关内容，辅助扫描会先把仓库识别为 `script`、`library`、`app`、`plugin`、`docs` 或 `unknown`，再推荐治理文件。

使用时采用以下 canonical 路径：

- `AGENT.md` 或 `AGENTS.md`
- `docs/CODE_STYLE.md`
- `docs/specs/*.md`：功能规格
- `docs/plans/*.md`
- `docs/TASKS.md`：唯一活跃 task ledger
- `docs/CHANGELOG_AI.md`
- `docs/archive/`

相互独立的条件界面：

- `docs/PRD.md`：产品或 app 仓库需要时使用。
- `docs/DESIGN.md`：UI、前端、桌面端、移动端或组件工作需要时使用。
- `docs/BRAND.md`：公开品牌、身份、营销、命名或文案工作需要时使用，不由 UI 信号自动触发。

`docs/assets/*` 是可选项，只在已有资产或用户明确要求整理资产时使用。`unknown` profile 只要求 `README.md` 和一个 agent guide，不默认推断 app、UI、品牌、spec、plan、task 或 archive 治理。

纯脚本、CLI、自动化、库和文档型仓库默认不需要设计或品牌脚手架。

对于公开或开源仓库，OpenArc 也可能检查发布与维护文件：

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `LICENSE`

已有文件优先。OpenArc 倾向于保留现有意图，并以小步修补的方式调整，而不是重写已有仓库约定。

## 交付路径

OpenArc 使用能安全承载当前工作的最小路径：

- 直接实现：范围和验证清晰的日常低风险改动。
- Spec：行为、验收标准或兼容性需要持久合同时，写入 `docs/specs/*.md`。
- Plan：执行顺序、迁移、回滚或验证风险需要结构时，写入 `docs/plans/*.md`。
- Tasks：只有活跃的多步骤协作才写入唯一的 `docs/TASKS.md`。

这些路径独立选择；一次变更不需要依次经过所有文档。

## 变更记忆与归档治理

OpenArc 将 AI 参与的软件开发视为长期协作。

`docs/CHANGELOG_AI.md` 保留近期 AI 变更，使其保持可见、可行动。

`docs/archive/` 保存更早的历史上下文，避免每次会话都加载旧内容。

这既保留可追溯性，也保护上下文预算。

推荐保留模型：

- `docs/CHANGELOG_AI.md` 聚焦最近 10-20 条 AI 参与变更
- 更早条目进入 `docs/archive/`
- 历史信息保留可追溯性，而不是为了节省上下文被删除
- 归档内容主要用于排查回归、追溯架构历史或理解过去 AI 决策

## 辅助脚本

OpenArc 提供一个无外部依赖的小脚本：

```bash
python3 plugins/openarc/scripts/openarc.py scan <repo-root>
python3 plugins/openarc/scripts/openarc.py scan <repo-root> --format json
python3 plugins/openarc/scripts/openarc.py doctor <plugin-root>
```

`scan` 会识别 repo profile，并把治理项分为 `required`、`relevant`、`optional`。Required 是最小 profile 基线，relevant 取决于仓库信号或当前工作，optional 缺失不会让仓库变成不健康。`unknown` profile 只要求 `README.md` 和一个 agent guide；UI 与品牌信号独立判断，assets 始终可选。

`doctor` 用于发布插件变更前校验 manifest、公开文件、模板、平台适配文件和 skill frontmatter。

## 澄清关卡

OpenArc 对宽泛、模糊、高风险或全新工作先澄清；范围与验证清晰的日常改动可以直接实现。Clarification Gate 的目标，是让 PRD、spec、plan、代码风格、设计和品牌文档基于仓库证据和已确认决策，而不是用空泛表述补齐未知信息。

当 repo profile 或用户请求需要新的 PRD、spec、plan、代码风格决策、设计指南或品牌指引时，流程是：

1. 发现仓库已有信号：README、包信息、应用界面、代码风格配置、文档、文案、设计变量、素材和近期规格文档。
2. 区分已知事实、未知信息、矛盾点和高风险假设。
3. 只询问仓库无法回答的 0-5 个关键问题；证据充足时不提问。
4. 每个问题都给出推荐答案和取舍。
5. 当 readiness 为 `ready` 且实现已经获授权时，同一轮直接继续，不再要求用户回复“继续”。
6. 将已确认决策写入最小的现有目标：PRD、`docs/specs/*.md`、plan、`docs/TASKS.md`、changelog、code style、design 或 brand。
7. 保留仍未解决的模糊点，而不是用泛泛文字掩盖。

OpenArc 默认不创建 ADR。只有当决策难以回滚、缺少上下文会显得意外、且确实存在真实取舍时，才建议 ADR。

## 版本策略

OpenArc 默认使用 semantic versioning：

- Patch：错别字、文案、小 bug、只改文档的优化、非行为性清理。
- Minor：向后兼容的新功能、新文档章节、新模板、新可选流程。
- Major：破坏性变更、治理模型变更、不兼容 API/schema、公共命令重命名、行为移除。

只有 release-visible 变更才需要判断版本等级、提出版本号，并在发布前请用户确认。

## 迁移策略

OpenArc 的迁移策略是保守的：

- 先盘点，再编辑。
- 将已有文件映射到 OpenArc 目标结构。
- 能原地 patch 就不移动。
- 移动、重命名、归档或删除前先确认。
- 通过链接或说明保留旧约定背后的意图。
- 迁移后验证链接和格式。

## 模板

模板位于 `templates/`：

- `AGENT.template.md`
- `CODE_STYLE.template.md`
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

示例位于 `examples/`。

## 参与贡献

欢迎参与 OpenArc 的开源共建。如果你有改进建议、问题修复、迁移案例或更好的 AI 协作流程，欢迎提交 issue 或 PR。

## License

OpenArc 使用 MIT License。见 [LICENSE](LICENSE)。
