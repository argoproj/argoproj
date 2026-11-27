# Argo community skills

[Claude Code](https://claude.com/claude-code) skills that help with Argo community work.

| Skill | What it does |
|---|---|
| [`argo-contrib-insights`](argo-contrib-insights/) | Generates the weekly contrib-experience meeting stats for argo-cd and argo-rollouts: created/stale issue and PR counts from GitHub, plus top reviewers and mergers from LFX Insights. |

## Installing

The `argo-community` plugin bundles every skill in this directory. Its marketplace manifest lives in `community/.claude-plugin/`, so add the marketplace by URL:

```
/plugin marketplace add https://raw.githubusercontent.com/argoproj/argoproj/main/community/.claude-plugin/marketplace.json
/plugin install argo-community@argoproj
```

To pick up new or updated skills later, run `/plugin marketplace update argoproj`.

## Adding a skill

Create `community/skills/<skill-name>/SKILL.md` (plus any scripts it needs). The plugin picks up every directory under `community/skills/` automatically. Bump `version` in `community/.claude-plugin/plugin.json` so existing installs get the update.
