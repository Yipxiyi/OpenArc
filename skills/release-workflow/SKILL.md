---
name: release-workflow
description: Use when cutting or merging branches, making commits, opening pull requests, preparing release notes, or triggering GitHub release updates in an OpenArc-governed repository.
---

# Release Workflow

Use this skill when the user wants standardized branch, commit, PR, merge, or GitHub release work.

## Preconditions

Before changing git state:

1. Inspect current branch and working tree.
2. Identify user changes and do not overwrite them.
3. Confirm the target base branch.
4. Use `version-governance` when the change affects release version.
5. Run relevant validation before PR or release.

## Branch Rules

Default branch name:

```txt
<type>/<version-or-ticket>-<short-slug>
```

Allowed types:

- `feature`
- `fix`
- `docs`
- `refactor`
- `chore`
- `release`
- `migration`

Examples:

- `feature/0.2.0-workspace-migration`
- `fix/0.2.1-prd-clarification-flow`
- `release/0.2.0`

## Commit Rules

Use conventional commits:

```txt
<type>(<scope>): <summary>
```

Examples:

- `feat(openarc): add workspace migration skill`
- `docs(brand): clarify brainstorming flow`
- `fix(release): require validation before pr`

Keep commits focused. Do not mix unrelated changes.

## PR Rules

PR body should include:

- Summary
- Version impact
- Validation
- Risks
- Rollback
- Release notes

Use `templates/RELEASE.template.md` for release-facing content when useful.

Update `CHANGELOG.md` for user-visible changes before opening the PR.

## GitHub Release Update

After the PR is ready, trigger the repository's release update mechanism:

1. Prefer the repo's existing GitHub Actions workflow, release-drafter config, semantic-release setup, or documented release script.
2. If a workflow exists, trigger it with the confirmed version and release notes.
3. If no release automation exists, create or update a draft GitHub release only after the user confirms.
4. Never publish a final release without explicit user confirmation unless the repo automation already defines that behavior.

## Merge Rules

- Merge only after required checks pass or the user explicitly accepts the risk.
- Use the repository's preferred merge strategy.
- After merge, verify release automation ran or report why it did not.

## Final Report

Report:

- Branch
- Commit(s)
- PR URL
- Confirmed version
- Validation
- Changelog entry
- Release update trigger/result
- Any blockers
