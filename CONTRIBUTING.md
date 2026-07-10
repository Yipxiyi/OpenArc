# Contributing To OpenArc

OpenArc is meant to stay lightweight. Contributions should improve agent behavior without turning the plugin into process-heavy project management software.

For package structure and install behavior, see [the framework reference](docs/REFERENCE.md) and [installation guide](docs/INSTALL.md).

## Contribution Principles

- Prefer focused skills over one large instruction file.
- Keep skill bodies concise and routeable.
- Preserve existing repository intent.
- Prefer patch-based updates over rewrites.
- Add templates only when they reduce repeated work.
- Avoid framework lock-in.
- Update README and changelog for user-visible changes.

## Before You Change A Skill

1. Identify the user scenario the skill should support.
2. Check whether an existing skill can be patched instead of adding a new one.
3. Keep frontmatter descriptions focused on when the skill should trigger.
4. Avoid duplicating detailed workflow steps across multiple skills.
5. Run the repository validation gates below.

## Before You Add A Skill

A new skill is justified when:

- It has a distinct trigger.
- Loading it only when needed reduces context pollution.
- Existing skills would become too broad if expanded.
- Future agents are likely to reuse the workflow.

Do not add a skill for a one-off project preference.

## Versioning

Use OpenArc's default semantic versioning policy:

- Patch: typo fixes, copy edits, docs-only refinements, small bug fixes, non-behavioral cleanup.
- Minor: backward-compatible skills, templates, docs sections, or optional workflows.
- Major: breaking governance changes, removed behavior, renamed public workflows, incompatible schemas.

The maintainer must confirm the proposed version before release work. Keep these values aligned:

- `.codex-plugin/plugin.json` version
- `.claude-plugin/plugin.json` version
- release tag `v<version>`
- matching `CHANGELOG.md` section

Do not create a tag until the manifests and changelog are ready.

## Validation

Run these commands from the OpenArc repository root:

```bash
python3 scripts/openarc.py doctor .
python3 -m unittest discover -s tests -v
```

`doctor` checks manifests, version parity, required public files, skills, templates, adapters, and referenced assets. The test suite covers scan profiles and helper behavior.

[CI](.github/workflows/ci.yml) runs both commands for pull requests and pushes to `main`. The [release workflow](.github/workflows/release.yml) repeats them for `v*` tags and rejects a release when the tag, both manifest versions, or changelog section do not match.

## Pull Request Checklist

- [ ] Manifest JSON is valid.
- [ ] `python3 scripts/openarc.py doctor .` passes.
- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] README reflects user-facing changes.
- [ ] CHANGELOG includes the change.
- [ ] LICENSE metadata remains consistent.
- [ ] No temporary files or duplicate docs were added.
