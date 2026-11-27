# argo-contrib-insights

Generates the stats section for the weekly Argo contrib-experience meeting (every Thursday), covering argo-cd and argo-rollouts:

- **Weekly GitHub Stats**: issues and PRs created during the week (split into open and closed) and the number of stale issues. Each count links to the matching GitHub search.
- **Weekly LFX Insights Stats**: top reviewers and top mergers, using the same numbers as the [LFX Insights](https://insights.linuxfoundation.org/project/argo/contributors) dashboard.

The week runs from Friday 00:00 UTC to Thursday 23:59 UTC.

## Requirements

- Python 3 (standard library only).
- Outbound HTTPS to `api.github.com` and `insights.linuxfoundation.org`. No tokens or logins are needed.
- macOS, for the automatic clipboard copy. On other systems you still get the Markdown output.

## Using it in Claude Code

After [installing the plugin](../README.md#installing), ask Claude for the numbers in plain language, for example:

- "Give me the numbers for the contrib-experience meeting."
- "Who were the top reviewers in argo-cd this week?"
- "Pull last week's contrib stats, top 5 only."

You can also run the skill directly:

```
/argo-community:argo-contrib-insights
```

Claude runs the script, shows you the Markdown, and copies a formatted version to your clipboard. Paste it into the meeting notes Google Doc with Cmd-V: the nested bullets, bold headings and links come through intact.

## Running the script without Claude

```bash
python3 community/skills/argo-contrib-insights/scripts/leaderboard.py
```

| Option | Description |
|---|---|
| `--thursday YYYY-MM-DD` | The Thursday that ends the reporting week. Defaults to today if it is Thursday, otherwise the next Thursday. Use it to regenerate an earlier week. |
| `--top N` | Number of people in each leaderboard (default `10`). |
| `--repo URL` | Full GitHub URL of a repo to report on. Repeatable. Defaults to argo-cd and argo-rollouts. |
| `--no-clip` | Don't copy the formatted version to the clipboard. |

Markdown goes to stdout and progress messages go to stderr, so `> stats.md` gives you clean output.

## Example output

The names and numbers below are made up.

```markdown
**Weekly GitHub Stats** (Extracted with insight-generator)
- **Argo CD:**
  - Created Issues: [12 open / 5 closed](https://github.com/argoproj/argo-cd/issues?q=...)
  - Created PRs: [20 open / 18 closed](https://github.com/argoproj/argo-cd/issues?q=...)
  - Stale Issues: [2400](https://github.com/argoproj/argo-cd/issues?q=...)
- **Argo Rollouts:**
  - ...

**Weekly LFX Insights Stats**
  [**Top Reviewers**](https://insights.linuxfoundation.org/...) (Choose "Reviewed a pull request" in the activity drop-down):
  - **Argo CD:**
    - Jane Doe 24 - 30%
    - John Smith 17 - 21%
  - **Argo Rollouts:**
    - ...
  [**Top Mergers:**](https://insights.linuxfoundation.org/...) (Choose "Merged a pull request" in the activity drop-down):
  - ...
```

## How the numbers are counted

- **Created Issues / Created PRs**: items created during the week. The open/closed split uses each item's current state.
- **Stale Issues**: open issues not updated in the past 365 days. This is a snapshot of the backlog today, not limited to the week.
- **Top Reviewers / Top Mergers**: LFX Insights "Reviewed a pull request" and "Merged a pull request" activity counts, with LFX's own bot filtering and name matching. Each entry shows the person's name, their count and their share of the total.

If a source can't be reached, the script keeps going: a missing leaderboard shows "_No activity in this window._" and a failed GitHub count shows `0`, with a note on stderr.
