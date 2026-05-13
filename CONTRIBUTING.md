# Contributing To OpenArc

OpenArc is meant to stay lightweight. Contributions should improve agent behavior without turning the plugin into process-heavy project management software.

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
5. Validate the changed skill.

Validation:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py plugins/openarc/skills/<skill-name>
python3 plugins/openarc/scripts/openarc.py doctor plugins/openarc
```

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

The maintainer should confirm the proposed version before release work.

## Pull Request Checklist

- [ ] Manifest JSON is valid.
- [ ] Changed skills pass validation.
- [ ] `openarc.py doctor` passes.
- [ ] README reflects user-facing changes.
- [ ] CHANGELOG includes the change.
- [ ] LICENSE metadata remains consistent.
- [ ] No temporary files or duplicate docs were added.
