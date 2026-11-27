---
name: argo-contrib-insights
description: Produce a Top Reviewers + Top Mergers leaderboard for argoproj/argo-cd and argoproj/argo-rollouts over the past 7 days, formatted for the weekly Argo contrib-experience meeting (every Thursday). Use this skill whenever the user asks for contributor stats, review/merge leaderboards, "who reviewed/merged the most PRs", meeting prep for the contrib-experience sync, Thursday meeting numbers, maintainer activity report, or anything similar — even if the words "leaderboard" or "skill" aren't used. Trigger on prompts like "pull top reviewers for this week", "numbers for contrib meeting", "who's been active in argo-cd this week", "weekly review stats", or "give me the Thursday report".
---

# Argo Contrib Experience Leaderboard

## What this skill does

Produces two meeting-agenda sections for **argoproj/argo-cd** and **argoproj/argo-rollouts** covering the **Friday → Thursday meeting week** (Fri 00:00 UTC → Thu 23:59 UTC). Output order matches the Argo contrib-experience doc template:

1. **Weekly GitHub Stats** (Extracted with insight-generator) — Created Issues, Created PRs (both as `N open / M closed`), and Stale Issues. Each line is a single hyperlink to the state-agnostic GitHub search page so a reader can click through and see the actual list. Open/closed split is based on each item's *current* state. Stale = open issues not updated in the past 365 days (snapshot, not window-scoped).
2. **Weekly LFX Insights Stats** wrapper, with two sub-sections nested under it:
   - **Top Reviewers** — contributors ranked by the LF Insights "Reviewed a pull request" activity count.
   - **Top Mergers** — contributors ranked by the LF Insights "Merged a pull request" activity count.

Leaderboard numbers come straight from the **LF Insights widget API** (`/api/widget/contributors/contributor-leaderboard`), so they match what a maintainer sees when clicking through to insights.linuxfoundation.org. GitHub Stats come from the **GitHub REST search API** (`/search/issues`) — anonymous, so no auth needed.

Each contributor renders as `<Real name> <count> - <pct>%`. Real names and percentages come from LF Insights — no GitHub lookups, no hardcoded aliases, no bot filtering (LF has already done it on their side).

Both section headings link to the LF Insights contributors dashboard scoped to the same window; the activity type (review vs. merge) is selected on-page via its drop-down.

**Output goes two places:**
1. Markdown to stdout (for chat / logging / piping).
2. Rich HTML onto the macOS clipboard — automatically — so you can **Cmd-V straight into the meeting Google Doc** and get a properly nested, hyperlinked, bold-headers bullet list. No manual list formatting, no fiddling with "paste as plain text".

Clipboard copy uses `osascript` + AppleScript's `«data HTML…»` type. On non-macOS, it silently degrades to Markdown-only; nothing is lost.

This skill is **read-only**: four unauthenticated `GET`s per run (2 repos × {reviewed, merged}). It writes no files.

## When to use it

The Argo contrib-experience meeting runs **every Thursday**. The intent is that the meeting host runs this on Thursday morning and pastes the output into the agenda. It's also fine to run it any other day — the window is always "past 7 days from now", not pinned to a specific weekday.

Trigger on any of:
- "pull top reviewers / top mergers"
- "numbers for Thursday" / "contrib experience meeting prep"
- "who's been active this week"
- "weekly review leaderboard for argo"

## Prerequisites

- Python 3 (stdlib only — the script uses `urllib`).
- Outbound HTTPS to `insights.linuxfoundation.org`.

No GitHub auth needed. No API key for LF Insights (the widget endpoint is public — the only quirk is that it rejects the default `Python-urllib` User-Agent, so the script sends a browser UA).

## How to run

The script lives next to this file:

```
<skill-dir>/scripts/leaderboard.py
```

Run it (no arguments needed for the default case):

```bash
python3 <skill-dir>/scripts/leaderboard.py
```

**Options** (rarely needed):

- `--thursday YYYY-MM-DD` — pin the end-of-week Thursday. Default: the next-or-current Thursday from today. Use this to regenerate last week's or an older week's leaderboard.
- `--top N` — leaderboard size (default: `10`).
- `--repo https://github.com/<org>/<name>` — override the default repos. Repeatable. Full GitHub URLs (not `org/name`), because that's how LF Insights identifies them. Defaults to argo-cd + argo-rollouts.
- `--no-clip` — skip the clipboard copy (default: copy). Useful when piping output somewhere and you don't want the HTML version taking over the clipboard.

The script prints Markdown to stdout. Everything else (progress, warnings) goes to stderr so a `>` redirect gives you clean paste-ready output if desired.

## Output format

For each repo the script emits **two tables** under a single `## <repo>` heading. The window and PR sample size are shown so the audience can sanity-check the numbers.

Example (shape only — numbers are illustrative):

```markdown
## argoproj/argo-cd — past 7 days (2026-09-24 → 2026-10-01)

Sampled 42 merged PRs and 118 review events.

### Top Reviewers

| Rank | Reviewer | Reviews |
|:---:|:---|---:|
| 1 | @alice | 24 |
| 2 | @bob | 17 |
| … | … | … |

### Top Mergers

| Rank | Merger | PRs merged |
|:---:|:---|---:|
| 1 | @carol | 9 |
| 2 | @dave | 6 |
| … | … | … |
```

If a repo had **zero** merges or **zero** reviews in the window, the script prints the heading, states that explicitly ("_No reviews in this window._"), and moves on — no empty tables. This keeps the meeting notes honest.

## Why LF Insights (and not GitHub)

The maintainer running this script wants numbers that match what everyone sees on the LF Insights dashboard. Rebuilding the same leaderboard off raw GitHub events is possible but doesn't quite line up: LF Insights folds in nuances (unique PRs with a review, draft/merge filtering, their own name-and-bot mapping) that are hard to replicate exactly, and the small discrepancies erode trust in the report. Sourcing directly from LF's widget API gives us the dashboard's exact numbers for free.

## How the data is fetched

**Leaderboards (LF Insights).** For each repo and each activity type the script issues a single unauthenticated GET against:

```
https://insights.linuxfoundation.org/api/widget/contributors/contributor-leaderboard
  ?project=argo
  &platform=github
  &activityType={pull_request-reviewed | pull_request-merged}
  &repos=https://github.com/argoproj/<repo>
  &startDate={fri}&endDate={thu}
  &offset=0&limit=20
  &includeCollaborations=false
```

The response's `data[]` is already ranked, bot-filtered, and name-resolved. We just render the top N.

**Weekly GitHub Stats (GitHub REST).** 5 anonymous GETs per repo against `https://api.github.com/search/issues`:

```
is:issue created:{fri}..{thu} is:open                 → Created Issues (open)
is:issue created:{fri}..{thu} is:closed               → Created Issues (closed)
is:pr    created:{fri}..{thu} is:open                 → Created PRs (open)
is:pr    created:{fri}..{thu} is:closed               → Created PRs (closed)
is:issue is:open updated:<{thu - 365 days}            → Stale Issues (snapshot)
```

Each number also renders as a hyperlink to the equivalent `github.com/<repo>/issues?q=…` search page — same qualifiers, so clicking lands on the actual list. Anonymous rate limit is 10 req/min for search, and the script uses 10 total (2 repos × 5), so a run completes well inside the window. If a query fails for any reason the number renders as `0` and a line is written to stderr — the rest of the report still prints.

## What to tell the user after running

1. **Say that you copied it to the clipboard** — the rich HTML version is already there, ready for Cmd-V into the Google Doc. Don't make the user re-copy from chat.
2. Show the Markdown output so they can sanity-check the numbers before pasting.
3. Note the exact date range the script used (shown in the top line).
4. If any repo returned "_No activity in this window_", call that out — useful signal, not a bug.

## Constraints

**Read-only.** The script issues 14 unauthenticated `GET`s total (4 to LF Insights for the leaderboards, 10 to GitHub for the weekly stats). It writes nothing to disk.

If LF Insights is unreachable, the affected section renders as "_No activity in this window._" — the script keeps going so the other sections still produce output. GitHub failures surface as `0` with a stderr note.
