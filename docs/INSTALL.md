# Install OpenArc

OpenArc can be loaded by Codex, Claude Code, or Cursor. The repository contains both the plugin package and the Codex marketplace manifest that points to its pinned GitHub release.

## Get the source

```bash
git clone https://github.com/Yipxiyi/OpenArc.git
cd OpenArc
python3 scripts/openarc.py doctor .
```

Continue only when the last command reports `OpenArc doctor: PASS`.

## Codex

### Install a pinned release

```bash
codex plugin marketplace add Yipxiyi/OpenArc --ref v0.7.0
codex plugin add openarc@openarc
codex plugin list --marketplace openarc
```

Success means `openarc@openarc` is listed as installed and enabled at version `0.7.0`. Codex materializes the installed package under `~/.codex/plugins/cache/openarc/openarc/0.7.0`.

Restart Codex, then ask:

```text
Use OpenArc to audit this repository read-only.
```

The marketplace is pinned to the release tag. Installation therefore remains reproducible even when `main` moves forward.

### Upgrade a pinned release

Pinned marketplaces do not follow new tags automatically. Remove the installed snapshot and old marketplace, then add the new release ref:

```bash
codex plugin remove openarc@openarc
codex plugin marketplace remove openarc
codex plugin marketplace add Yipxiyi/OpenArc --ref v0.7.1
codex plugin add openarc@openarc
codex plugin list --marketplace openarc
```

Replace `v0.7.1` with the release you intend to install. Verify the version before restarting Codex.

### Local development

Use a local marketplace only when testing an unpublished checkout. Keep one managed copy at `~/plugins/openarc`:

```bash
mkdir -p ~/plugins/openarc
rsync -a --delete --delete-excluded --exclude '.git/' ./ ~/plugins/openarc/
```

If OpenArc is vendored at `plugins/openarc`, run this from the host repository instead:

```bash
mkdir -p ~/plugins/openarc
rsync -a --delete --delete-excluded --exclude '.git/' plugins/openarc/ ~/plugins/openarc/
```

The destination is a managed copy; `--delete` removes stale files from earlier versions.

If `~/.agents/plugins/marketplace.json` does not exist, create its parent directory and add the complete document below:

```bash
mkdir -p ~/.agents/plugins
```

```json
{
  "name": "local-codex-plugins",
  "interface": {
    "displayName": "Local Codex Plugins"
  },
  "plugins": [
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
  ]
}
```

Register the home directory as the marketplace root, then install OpenArc:

```bash
codex plugin marketplace add ~
codex plugin add openarc@local-codex-plugins
```

If `local-codex-plugins` already exists, preserve its manifest, add only the OpenArc object above to its `plugins` array, and skip `marketplace add`. Check first with:

```bash
codex plugin marketplace list
```

Verify the unpublished package and installed snapshot:

```bash
python3 ~/plugins/openarc/scripts/openarc.py doctor ~/plugins/openarc
codex plugin list --marketplace local-codex-plugins
```

Success means:

- `doctor` reports `PASS`.
- `openarc@local-codex-plugins` is listed as installed and enabled with the expected version.
- Codex has materialized the same version under `~/.codex/plugins/cache/local-codex-plugins/openarc/`.

Restart Codex, then ask:

```text
Use OpenArc to audit this repository read-only.
```

Refresh a local-development snapshot after changing the checkout:

```bash
git pull --ff-only
rsync -a --delete --delete-excluded --exclude '.git/' ./ ~/plugins/openarc/
codex plugin remove openarc@local-codex-plugins
codex plugin add openarc@local-codex-plugins
python3 ~/plugins/openarc/scripts/openarc.py doctor ~/plugins/openarc
codex plugin list --marketplace local-codex-plugins
```

Restart Codex after the upgrade.

## Claude Code

### One session

`--plugin-dir` loads OpenArc for the current session only:

```bash
claude --plugin-dir .
```

For a vendored or managed copy, use its directory instead:

```bash
claude --plugin-dir ./plugins/openarc
claude --plugin-dir ~/plugins/openarc
```

Then invoke `/openarc:openarc`.

### Persistent install

A persistent install requires OpenArc to be available from a Claude Code plugin marketplace. In an interactive Claude Code session, run `/plugin`, add or select that marketplace, install OpenArc, and restart Claude Code. The repository's `--plugin-dir` path is not a persistent installation.

## Cursor

Cursor uses the adapter files rather than the Codex or Claude manifests. Copy the project rule without overwriting an existing rule:

```bash
mkdir -p <target-repo>/.cursor/rules
cp -n integrations/cursor/openarc.mdc <target-repo>/.cursor/rules/openarc.mdc
```

From a host repository with vendored OpenArc:

```bash
mkdir -p .cursor/rules
cp -n plugins/openarc/integrations/cursor/openarc.mdc .cursor/rules/openarc.mdc
```

Prefer the project rule. Add the optional root guide only when the target has no `AGENTS.md`:

```bash
cp -n integrations/cursor/AGENTS.md <target-repo>/AGENTS.md
```

If either destination already exists, compare and merge the relevant rules manually; never replace project-specific instructions wholesale. Then ask Cursor Agent: `Use OpenArc here.`

## Helper commands

From the OpenArc repository root:

```bash
python3 scripts/openarc.py scan <repo-root>
python3 scripts/openarc.py scan <repo-root> --format json
python3 scripts/openarc.py doctor .
```

From a host repository with OpenArc vendored at `plugins/openarc`:

```bash
python3 plugins/openarc/scripts/openarc.py scan .
python3 plugins/openarc/scripts/openarc.py doctor plugins/openarc
```

See [Framework reference](REFERENCE.md) for scan semantics, canonical paths, skills, and templates.
