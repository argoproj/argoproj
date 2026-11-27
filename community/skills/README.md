# Argo community skills

[Claude Code](https://claude.com/claude-code) skills that help with Argo community work.

| Skill | What it does |
|---|---|
| [`argo-contrib-insights`](argo-contrib-insights/) | Generates the weekly contrib-experience meeting stats for argo-cd and argo-rollouts: created/stale issue and PR counts from GitHub, plus top reviewers and mergers from LFX Insights. |

## Installing

The `argo-community` plugin bundles every skill in this directory. Its marketplace manifest lives in `community/skills/.claude-plugin/`, so add the marketplace by URL:

```
/plugin marketplace add https://raw.githubusercontent.com/argoproj/argoproj/main/community/skills/.claude-plugin/marketplace.json
/plugin install argo-community@argoproj
```

To pick up new or updated skills later, run `/plugin marketplace update argoproj`.

## Using the skills

Once the plugin is installed, Claude uses a skill on its own when your request matches it. For example, "give me the numbers for the contrib-experience meeting" runs `argo-contrib-insights`. You can also run a skill directly as `/argo-community:<skill-name>`.

Each skill's folder has a README with its options and example output.

## Adding a skill

Create `community/skills/<skill-name>/SKILL.md`, plus any scripts it needs and a README.md for people. Add a row to the table above. The plugin picks up every skill directory under `community/skills/` automatically. Bump `version` in `community/skills/.claude-plugin/plugin.json` so existing installs get the update.
