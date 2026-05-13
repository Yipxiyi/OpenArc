# OpenArc

<p align="center">
  <a href="#english"><strong>English</strong></a> ·
  <a href="#中文说明"><strong>中文</strong></a>
</p>

<a id="english"></a>

## English

OpenArc is an AI-native operational foundation for vibe-coded projects.

It helps developers initialize and sustain repositories where coding agents remain the primary implementation driver over time. OpenArc is not a replacement for Codex, Claude Code, OpenClaw, Cursor, or future AI coding runtimes. It gives those agents a lightweight repository memory and governance layer.

## What OpenArc Solves

- Architectural drift
- Inconsistent documentation
- Context fragmentation
- Unstable AI iteration
- Repository chaos
- Weak implementation traceability
- Oversized AI context from old project history

## What OpenArc Enables

- Sustainable AI-driven development
- Long-term repository continuity
- Structured vibe coding
- Scalable AI collaboration
- Spec-driven iteration
- Lightweight governance
- Safer migration of existing workspaces
- Recent AI change memory with archive-based history

## Design Principles

- Lightweight over bureaucratic
- Patch-friendly over rewrite-heavy
- Repository-aware over framework-specific
- AI-first over human-only documentation
- Explicit source of truth over scattered intent
- Long-term maintainability over one-off prompting
- Small active context, preserved historical traceability

## Quick Start

Use OpenArc when a repository needs structure before or during AI-driven implementation.

Common prompts:

```text
Use OpenArc here.
Scan this repo with OpenArc and tell me what to do first.
Initialize OpenArc governance for this repository.
Create a lightweight spec and implementation plan.
Migrate this workspace to OpenArc conventions.
Review this repo for governance drift.
```

If you have the plugin files checked out locally, the fastest first pass is:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
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
| `release-workflow` | Cutting or merging branches, committing, opening PRs, and preparing release notes. |
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

Use `doctor` before publishing plugin changes. It checks the manifest, required public files, required templates, and skill frontmatter.

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
- Confirm version impact through `version-governance`.
- Verify README, manifest, and license metadata agree.

## Future Work

Planned improvements include:

- More real-world migration examples.
- Example PR descriptions generated by `release-workflow`.
- Optional visual assets after the final project identity is decided.
- Additional validation coverage for template completeness and README links.

## License

OpenArc is released under the MIT License. See [LICENSE](LICENSE).

---

<a id="中文说明"></a>

## 中文说明

OpenArc 是一个面向 vibe coding 项目的 AI 原生治理基础层。

它帮助开发者初始化并长期维护以 AI coding agent 为主要实现驱动力的仓库。OpenArc 不替代 Codex、Claude Code、OpenClaw、Cursor 或未来的 AI 编程运行时；它提供的是轻量级的仓库记忆与治理层。

## OpenArc 解决什么问题

- 架构漂移
- 文档不一致
- 上下文碎片化
- AI 迭代不稳定
- 仓库持续混乱
- 实现过程缺少可追溯性
- 旧历史挤占 AI 上下文预算

## OpenArc 带来什么能力

- 可持续的 AI 驱动开发
- 长期仓库连续性
- 结构化 vibe coding
- 可扩展的 AI 协作
- spec-driven iteration
- 轻量治理
- 更安全的已有工作区迁移
- 近期 AI 变更记忆与 archive 历史留存

## 设计原则

- 轻量优先，不做官僚流程
- patch 优先，不做重写导向
- 仓库感知优先，不绑定具体框架
- AI-first，而不是只服务人工阅读
- 明确 source of truth，减少散落意图
- 长期可维护优先，不依赖一次性 prompt
- 活跃上下文尽量小，历史信息仍可追溯

## 快速开始

当仓库需要在 AI 实现前或实现过程中建立结构时，使用 OpenArc。

常用提示词：

```text
Use OpenArc here.
Scan this repo with OpenArc and tell me what to do first.
Initialize OpenArc governance for this repository.
Create a lightweight spec and implementation plan.
Migrate this workspace to OpenArc conventions.
Review this repo for governance drift.
```

如果你本地已有插件文件，最快的第一步是：

```bash
python3 plugins/openarc/scripts/openarc.py scan .
```

## 在 Codex 中安装

本地 Codex 安装时，将插件放到 `~/plugins/openarc`，并注册到 `~/.agents/plugins/marketplace.json`。

从仓库目录执行：

```bash
mkdir -p ~/plugins
cp -R plugins/openarc ~/plugins/openarc
```

然后把下面条目加入 `~/.agents/plugins/marketplace.json` 的 `plugins` 数组：

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

校验本地安装：

```bash
python3 ~/plugins/openarc/scripts/openarc.py doctor ~/plugins/openarc
```

注册后重启 Codex，然后尝试：

```text
Use OpenArc here.
```

## 插件结构

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

插件 manifest 位于 `.codex-plugin/plugin.json`。Skills 位于 `skills/`，可复用文档模板位于 `templates/`。

## Skill 列表

OpenArc 被拆分为多个 focused skills，避免 agent 每次加载不必要的上下文：

| Skill | 使用场景 |
| --- | --- |
| `openarc` | 用户泛泛要求使用 OpenArc，或需要选择正确 workflow。 |
| `repository-governance` | 扫描仓库、识别 source-of-truth 文档、创建或修补 agent guide。 |
| `product-governance` | 通过固定澄清流程创建或维护 `docs/PRD.md`。 |
| `spec-workflow` | 创建和维护带版本的 feature specs。 |
| `planning-engine` | 在写代码前创建轻量 implementation plan。 |
| `design-governance` | 维护 `docs/DESIGN.md` 中面向实现的设计规则。 |
| `brand-governance` | 维护 `docs/BRAND.md` 中的身份、语气和表达规则。 |
| `assets-governance` | 组织 `docs/assets/` 下的资产。 |
| `implementation-workflow` | 指导增量实现、验证和文档更新。 |
| `version-governance` | 判断变更属于 patch、minor 还是 major，并提出版本建议。 |
| `release-workflow` | 管理分支、commit、PR 和 release notes 准备。 |
| `workspace-migration` | 将已有工作区迁移到 OpenArc 规范，避免破坏性重写。 |
| `open-source-maintenance` | 准备插件或被治理仓库的开源维护材料。 |
| `change-archive-governance` | 维护 `docs/CHANGELOG_AI.md`、`docs/archive/` 和上下文预算友好的历史记忆。 |

## 仓库治理基础文件

OpenArc 会在需要时使用这些文件：

- `AGENT.md` 或 `AGENTS.md`
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

已有文件优先。OpenArc 应保留现有意图，并以 patch 方式谨慎调整，而不是重写已有仓库约定。

## 变更记忆与归档治理

OpenArc 将 AI-assisted development 视为长期协作。

`docs/CHANGELOG_AI.md` 保留近期 AI 变更，使其保持可见、可行动。

`docs/archive/` 保存更早的历史上下文，避免每次会话都加载旧内容。

这既保留可追溯性，也保护上下文预算。

推荐规则：

- `docs/CHANGELOG_AI.md` 只保留最近 10-20 条 AI-assisted entries
- 更早条目移动到 `docs/archive/`
- 不为了减少上下文而删除历史信息
- 只有在排查回归、追溯架构历史或理解过去 AI 决策时才读取 archive

## 辅助脚本

OpenArc 提供一个无外部依赖的小脚本：

```bash
python3 plugins/openarc/scripts/openarc.py scan <repo-root>
python3 plugins/openarc/scripts/openarc.py scan <repo-root> --format json
python3 plugins/openarc/scripts/openarc.py doctor <plugin-root>
```

`scan` 用于识别缺失的治理文件，并给出下一步推荐 workflow。

`doctor` 用于发布插件变更前检查 manifest、公开文件、模板和 skill frontmatter。

## 默认澄清流程

创建 `docs/PRD.md`、`docs/DESIGN.md` 或 `docs/BRAND.md` 时，不要用泛泛的猜测填空。

固定流程：

1. 发现仓库已有信号：README、package metadata、app screens、docs、copy、design tokens、assets 和 recent specs。
2. 草拟一个简短 assumptions table，区分 knowns、unknowns、contradictions 和 risky guesses。
3. 只针对关键缺口问用户聚焦问题。
4. 将已确认答案写入目标文档。
5. 检查 PRD、DESIGN、BRAND、specs 和 assets 之间的冲突。
6. 对仍不明确的关键决策请求确认。
7. 核心意图明确后再创建或 patch 文档。

## 版本策略

OpenArc 默认使用 semantic versioning：

- Patch：错别字、文案、小 bug、docs-only refinement、非行为性清理。
- Minor：向后兼容的新功能、新文档 section、新模板、新可选 workflow。
- Major：破坏性变更、治理模型变更、不兼容 API/schema、公共命令重命名、行为移除。

对用户提出的变更，agent 应判断变更等级，提出版本号建议，并在 release work 前请用户确认。

## 迁移策略

OpenArc 的迁移策略是保守的：

- 先盘点，再编辑。
- 将已有文件映射到 OpenArc 目标结构。
- 能原地 patch 就不移动。
- 移动、重命名、归档或删除前先确认。
- 通过链接或说明保留 legacy intent 的可发现性。
- 迁移后验证链接和格式。

## 模板

模板位于 `templates/`：

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

示例位于 `examples/`。

## 开发

校验修改过的 skill：

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py plugins/openarc/skills/<skill-name>
```

校验 plugin manifest：

```bash
python3 -m json.tool plugins/openarc/.codex-plugin/plugin.json
```

开 PR 前：

- 保持 skill 内容简洁。
- 避免多个 skill 重复写同一套 workflow。
- 用户可见变更需要更新 `CHANGELOG.md`。
- 运行 `python3 plugins/openarc/scripts/openarc.py doctor plugins/openarc`。
- 通过 `version-governance` 确认版本影响。
- 检查 README、manifest 和 license metadata 是否一致。

## 后续方向

计划中的改进包括：

- 更多真实迁移案例。
- 由 `release-workflow` 生成的 PR 描述示例。
- 在项目身份明确后补充可选视觉资产。
- 增加对模板完整性和 README 链接的校验覆盖。

## License

OpenArc 使用 MIT License。见 [LICENSE](LICENSE)。
