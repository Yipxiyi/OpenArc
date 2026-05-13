---
name: version-governance
description: Use when a user proposes changes that may require patch, minor, or major version changes, release notes, changelog updates, or version confirmation.
---

# Version Governance

Use this skill when classifying change size or proposing the next version.

## Default Rule

Use semantic versioning:

- Patch: typo fixes, copy edits, docs-only refinements, small bug fixes, dependency patch updates, non-behavioral cleanup.
- Minor: backward-compatible features, new optional workflows, new templates, new docs sections, non-breaking config additions.
- Major: breaking changes, removed behavior, renamed public commands, incompatible schema/API changes, governance model changes.

## Workflow

1. Detect current version from `package.json`, plugin manifest, changelog, release tags, or existing specs.
2. Classify the requested change as patch, minor, or major.
3. Explain the reason in one sentence.
4. Propose the exact next version.
5. Ask the user to confirm the version before release work or public changelog updates.
6. After confirmation, update the manifest/package metadata and `CHANGELOG.md`.

## Examples

- `0.1.0` plus copy-only docs fix -> `0.1.1`.
- `0.1.0` plus a new migration skill -> `0.2.0`.
- `0.2.3` plus a changed governance file layout that breaks old repos -> `1.0.0` or next major.

## Rules

- Do not silently publish a version bump.
- If multiple changes differ in severity, use the highest required bump.
- If the repo already has versioning rules, use them unless the user asks to adopt OpenArc defaults.
- Record the confirmed version in the relevant spec, plan, release notes, or changelog.
