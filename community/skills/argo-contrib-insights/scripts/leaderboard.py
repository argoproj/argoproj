#!/usr/bin/env python3
"""
READ-ONLY contrib-experience leaderboard for the Argo project.

Pulls Top Reviewers + Top Mergers directly from the LF Insights widget
API (same backend that powers the public insights.linuxfoundation.org
contributors page), so the numbers in the meeting notes match the
dashboard a maintainer can click through to.

Window: Friday 00:00 UTC → Thursday 23:59 UTC (the Argo contrib-experience
meeting runs every Thursday). Default: the next-or-current Thursday.

The endpoint is unauthenticated — no cookie, no bearer. The script
makes 4 GETs total (2 repos × {reviewed, merged}) plus writes nothing
to disk; output is Markdown on stdout.
"""
from __future__ import annotations

import argparse
import html as html_lib
import json
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

DEFAULT_REPOS = [
    "https://github.com/argoproj/argo-cd",
    "https://github.com/argoproj/argo-rollouts",
]
DEFAULT_TOP = 10
MEETING_WEEKDAY = 3  # Mon=0 … Thu=3 … Sun=6
PROJECT_SLUG = "argo"
WIDGET_URL = (
    "https://insights.linuxfoundation.org/api/widget/contributors/"
    "contributor-leaderboard"
)
# The LF Insights "contributors" dashboard — both headings link here;
# the user selects the activity type from the on-page drop-down.
INSIGHTS_PAGE = (
    "https://insights.linuxfoundation.org/project/argo/contributors"
    "?timeRange=custom"
    "&repos=argoproj-argo-cd,argoproj_argo-cd,argoproj-argo-rollouts,argoproj_argo-rollouts"
    "&start={start}&end={end}&auth=success"
)

# LF Insights' activity-type IDs for the two leaderboards we need.
ACTIVITY_REVIEWED = "pull_request-reviewed"
ACTIVITY_MERGED = "pull_request-merged"

REPO_LABELS = {
    "https://github.com/argoproj/argo-cd": "Argo CD",
    "https://github.com/argoproj/argo-rollouts": "Argo Rollouts",
}

GITHUB_SEARCH_URL = "https://api.github.com/search/issues"
# "Stale" = open issues that haven't been updated in the past year. Using a
# label like `Stale` would be noisier (rollouts doesn't use that label at
# all) and misses issues the stale bot never got to.
STALE_WINDOW_DAYS = 365


def repo_slug(repo_url: str) -> str:
    """`https://github.com/argoproj/argo-cd` → `argoproj/argo-cd`."""
    return repo_url.rstrip("/").removeprefix("https://github.com/")


def github_search_count(query: str) -> int:
    """Return `total_count` from GitHub REST search/issues. Anonymous."""
    url = GITHUB_SEARCH_URL + "?" + urllib.parse.urlencode({"q": query, "per_page": 1})
    req = urllib.request.Request(url, headers={
        "User-Agent": "argo-contrib-insights",
        "Accept": "application/vnd.github+json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        return int(payload.get("total_count", 0))
    except Exception as exc:
        print(f"github search failed for `{query}`: {exc}", file=sys.stderr)
        return 0


def github_issue_search_url(slug: str, qualifiers: str) -> str:
    """Build the clickable `github.com/<repo>/issues?q=…` URL that mirrors a
    `search/issues` API query. Used so each number in the Weekly GitHub
    Stats section is a hyperlink to its underlying search."""
    q = f"repo:{slug} {qualifiers}".strip()
    # Strip the leading repo qualifier — the /issues page is already scoped.
    q_without_repo = qualifiers.strip()
    return f"https://github.com/{slug}/issues?" + urllib.parse.urlencode(
        {"q": q_without_repo}
    )


def fetch_github_stats(repo_url: str, start: str, end: str,
                       stale_before: str) -> dict:
    """Return the Weekly GitHub Stats numbers + their search URLs.

    Each metric gets two numbers (open / closed) but a *single* clickable
    URL that shows the state-agnostic list, so a reader can land on the
    full set and sort/filter from there. Matches the meeting-doc format.

    The stale snapshot is intentionally *not* window-scoped: the meeting
    cares about the current size of the backlog, not what grew last week.
    """
    slug = repo_slug(repo_url)
    rng = f"created:{start}..{end}"
    count = github_search_count
    url = lambda q: github_issue_search_url(slug, q)
    return {
        "issues_open":   count(f"repo:{slug} is:issue {rng} is:open"),
        "issues_closed": count(f"repo:{slug} is:issue {rng} is:closed"),
        "issues_url":    url(f"is:issue {rng}"),
        "prs_open":      count(f"repo:{slug} is:pr {rng} is:open"),
        "prs_closed":    count(f"repo:{slug} is:pr {rng} is:closed"),
        "prs_url":       url(f"is:pr {rng}"),
        "stale_issues":  count(f"repo:{slug} is:issue is:open updated:<{stale_before}"),
        "stale_url":     url(f"is:issue is:open updated:<{stale_before}"),
    }


def fetch_leaderboard(repo_url: str, activity: str,
                      start: str, end: str, limit: int) -> list[dict]:
    """GET one leaderboard page from LF Insights. Returns rows as-is."""
    params = {
        "project": PROJECT_SLUG,
        "platform": "github",
        "activityType": activity,
        "repos": repo_url,
        "startDate": start,
        "endDate": end,
        "offset": 0,
        # Ask for a few extra rows so a longer meeting-week window still fills
        # the Top-N even if the first page contains an unexpected entry.
        "limit": max(limit, 20),
        "includeCollaborations": "false",
    }
    url = WIDGET_URL + "?" + urllib.parse.urlencode(params)
    # The server returns an empty page for the default `Python-urllib/*`
    # User-Agent — send a browser string so we get real data back.
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        print(f"error fetching {activity} for {repo_url}: {exc}", file=sys.stderr)
        return []
    return payload.get("data", [])


def meeting_week(now_dt: datetime) -> tuple[datetime, datetime]:
    """Return (friday, thursday) UTC for the current meeting week.

    If today is Thursday, that's the end; otherwise Thursday is the next
    one. This matches how LF Insights encodes the dashboard window.
    """
    days_until_thu = (MEETING_WEEKDAY - now_dt.weekday()) % 7
    thu = (now_dt + timedelta(days=days_until_thu)).replace(
        hour=23, minute=59, second=59, microsecond=0,
    )
    fri = (thu - timedelta(days=6)).replace(hour=0, minute=0, second=0)
    return fri, thu


def parse_date(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def format_pct(v: float) -> str:
    """LF Insights returns float percentages (e.g. 23.94). The meeting
    doc uses rounded ints — match that."""
    return f"{round(v)}"


def render_entries(rows: list[dict], top: int) -> list[str]:
    if not rows:
        return ["  - _No activity in this window._"]
    lines = []
    for row in rows[:top]:
        name = row.get("name") or (row.get("githubHandleArray") or ["?"])[0]
        n = row.get("contributions", 0)
        pct = format_pct(row.get("percentage", 0))
        lines.append(f"  - {name} {n} - {pct}%")
    return lines


def render_section(title: str, drop_down_label: str, link_url: str,
                   per_repo: list[tuple[str, list[dict]]], top: int) -> str:
    heading = f"[**{title}**]({link_url})" if link_url else f"**{title}**"
    out = [f'{heading} (Choose "{drop_down_label}" in the activity drop-down):']
    for repo_url, rows in per_repo:
        label = REPO_LABELS.get(repo_url, repo_url)
        out.append(f"- **{label}:**")
        out.extend(render_entries(rows, top))
    return "\n".join(out)


# ---- Weekly GitHub stats (Markdown + HTML) --------------------------------

STATS_HEADING = "Weekly GitHub Stats"
STATS_SUBTITLE = "Extracted with insight-generator"
LFX_HEADING = "Weekly LFX Insights Stats"


def render_stats_markdown(per_repo: list[tuple[str, dict]]) -> str:
    out = [f"**{STATS_HEADING}** ({STATS_SUBTITLE})"]
    for repo_url, s in per_repo:
        label = REPO_LABELS.get(repo_url, repo_url)
        out.append(f"- **{label}:**")
        out.append(
            f"  - Created Issues: [{s['issues_open']} open / "
            f"{s['issues_closed']} closed]({s['issues_url']})"
        )
        out.append(
            f"  - Created PRs: [{s['prs_open']} open / "
            f"{s['prs_closed']} closed]({s['prs_url']})"
        )
        out.append(
            f"  - Stale Issues: [{s['stale_issues']}]({s['stale_url']})"
        )
    return "\n".join(out)


def _a(url: str, text: str) -> str:
    return f'<a href="{html_lib.escape(url)}">{html_lib.escape(str(text))}</a>'


def render_stats_html(per_repo: list[tuple[str, dict]]) -> str:
    heading = (
        f'<strong>{html_lib.escape(STATS_HEADING)}</strong> '
        f'({html_lib.escape(STATS_SUBTITLE)})'
    )
    parts = [f'<li>{heading}<ul>']
    for repo_url, s in per_repo:
        label = html_lib.escape(REPO_LABELS.get(repo_url, repo_url))
        parts.append(f'<li><strong>{label}:</strong><ul>')
        issues = _a(s["issues_url"],
                    f"{s['issues_open']} open / {s['issues_closed']} closed")
        prs = _a(s["prs_url"],
                 f"{s['prs_open']} open / {s['prs_closed']} closed")
        stale = _a(s["stale_url"], s["stale_issues"])
        parts.append(f'<li>Created Issues: {issues}</li>')
        parts.append(f'<li>Created PRs: {prs}</li>')
        parts.append(f'<li>Stale Issues: {stale}</li>')
        parts.append('</ul></li>')
    parts.append('</ul></li>')
    return "".join(parts)


def render_lfx_wrapper_markdown(inner_sections: list[str]) -> str:
    """Wrap Top Reviewers + Top Mergers under a single bullet heading."""
    body = []
    for section in inner_sections:
        # Indent each line of the inner section by two spaces so it nests
        # one level deeper under the LFX wrapper bullet.
        for line in section.splitlines():
            body.append("  " + line if line else line)
    return f"**{LFX_HEADING}**\n" + "\n".join(body)


def render_lfx_wrapper_html(inner_section_items: list[str]) -> str:
    """Wrap already-formatted `<li>…</li>` section items under one bullet."""
    inner = "".join(inner_section_items)
    return (
        f'<li><strong>{html_lib.escape(LFX_HEADING)}</strong>'
        f'<ul>{inner}</ul></li>'
    )


# ---- HTML (clipboard output) ----------------------------------------------

def render_html_section(title: str, drop_down_label: str, link_url: str,
                        per_repo: list[tuple[str, list[dict]]], top: int) -> str:
    """Return one `<li>…</li>` for Top Reviewers or Top Mergers.

    The 3-level nesting (section → repo → contributor) is what Google Docs
    needs to render the bullet hierarchy from the meeting template.
    """
    parts = [
        f'<li><a href="{html_lib.escape(link_url)}"><strong>'
        f'{html_lib.escape(title)}</strong></a> '
        f'(Choose &ldquo;{html_lib.escape(drop_down_label)}&rdquo; '
        f'in the activity drop-down):',
        '<ul>',
    ]
    for repo_url, rows in per_repo:
        label = html_lib.escape(REPO_LABELS.get(repo_url, repo_url))
        parts.append(f'<li><strong>{label}:</strong><ul>')
        if not rows:
            parts.append('<li><em>No activity in this window.</em></li>')
        for row in rows[:top]:
            name = row.get("name") or (row.get("githubHandleArray") or ["?"])[0]
            n = row.get("contributions", 0)
            pct = format_pct(row.get("percentage", 0))
            parts.append(f'<li>{html_lib.escape(str(name))} {n} - {pct}%</li>')
        parts.append('</ul></li>')
    parts.append('</ul></li>')
    return "".join(parts)


def render_html(sections: list[str]) -> str:
    body = "".join(sections)
    return (
        '<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>'
        f'<ul>{body}</ul></body></html>'
    )


def copy_html_to_clipboard(html: str) -> bool:
    """Put `html` on the macOS clipboard with the HTML MIME type.

    Uses AppleScript's `«data HTML…»` syntax, which Google Docs / Word read
    as rich text on paste. Silently returns False on non-macOS or if the
    `osascript` binary isn't on PATH — the Markdown output still goes to
    stdout, so nothing is lost.
    """
    if not shutil.which("osascript"):
        return False
    hex_blob = html.encode("utf-8").hex()
    try:
        subprocess.run(
            ["osascript", "-e", f"set the clipboard to «data HTML{hex_blob}»"],
            check=True, capture_output=True,
        )
        return True
    except subprocess.CalledProcessError as exc:
        print(f"clipboard copy failed: {exc.stderr.decode().strip()}",
              file=sys.stderr)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pull Top Reviewers + Top Mergers for the Argo project "
                    "from LF Insights, scoped to the Fri→Thu meeting week.",
    )
    parser.add_argument(
        "--thursday", type=str, default=None,
        help="Thursday that ends the reporting week (YYYY-MM-DD). "
             "Defaults to the next-or-current Thursday from today.",
    )
    parser.add_argument(
        "--top", type=int, default=DEFAULT_TOP,
        help=f"Leaderboard size (default: {DEFAULT_TOP}).",
    )
    parser.add_argument(
        "--repo", action="append", default=None,
        help="Full GitHub URL of a repo (https://github.com/<org>/<name>). "
             "Repeatable. Defaults to argo-cd + argo-rollouts.",
    )
    parser.add_argument(
        "--no-clip", action="store_true",
        help="Skip copying the HTML version onto the macOS clipboard "
             "(default: copy, so you can Cmd-V straight into the meeting doc).",
    )
    args = parser.parse_args()

    repos = args.repo or DEFAULT_REPOS
    if args.thursday:
        thu = parse_date(args.thursday).replace(hour=23, minute=59, second=59)
        if thu.weekday() != MEETING_WEEKDAY:
            print(f"warning: --thursday {args.thursday} is not a Thursday "
                  f"({thu.strftime('%A')}); window is still 7 days ending "
                  f"that date.", file=sys.stderr)
        fri = (thu - timedelta(days=6)).replace(hour=0, minute=0, second=0)
    else:
        fri, thu = meeting_week(datetime.now(timezone.utc))

    date_fmt = "%Y-%m-%d"
    start = fri.strftime(date_fmt)
    end = thu.strftime(date_fmt)
    stale_before = (thu - timedelta(days=STALE_WINDOW_DAYS)).strftime(date_fmt)
    link_url = INSIGHTS_PAGE.format(start=start, end=end)

    print(
        f"# Argo contrib leaderboard — "
        f"{fri.strftime('%a %Y-%m-%d')} → {thu.strftime('%a %Y-%m-%d')}"
    )
    print()

    reviewed_by_repo = []
    merged_by_repo = []
    stats_by_repo = []
    for repo_url in repos:
        label = REPO_LABELS.get(repo_url, repo_url)
        print(f"→ Fetching {label} leaderboards…", file=sys.stderr)
        reviewed_by_repo.append(
            (repo_url, fetch_leaderboard(repo_url, ACTIVITY_REVIEWED,
                                         start, end, args.top))
        )
        merged_by_repo.append(
            (repo_url, fetch_leaderboard(repo_url, ACTIVITY_MERGED,
                                         start, end, args.top))
        )
        print(f"→ Fetching {label} GitHub stats…", file=sys.stderr)
        stats_by_repo.append(
            (repo_url, fetch_github_stats(repo_url, start, end, stale_before))
        )

    # Order mirrors the meeting-doc template: GitHub Stats first (quick
    # pulse-check numbers), then the LFX Insights block wrapping the two
    # contributor leaderboards.
    reviewers_md = render_section(
        "Top Reviewers", "Reviewed a pull request",
        link_url, reviewed_by_repo, args.top,
    )
    mergers_md = render_section(
        "Top Mergers:", "Merged a pull request",
        link_url, merged_by_repo, args.top,
    )

    print(render_stats_markdown(stats_by_repo))
    print()
    print(render_lfx_wrapper_markdown([reviewers_md, mergers_md]))

    if not args.no_clip:
        html = render_html([
            render_stats_html(stats_by_repo),
            render_lfx_wrapper_html([
                render_html_section("Top Reviewers", "Reviewed a pull request",
                                    link_url, reviewed_by_repo, args.top),
                render_html_section("Top Mergers:", "Merged a pull request",
                                    link_url, merged_by_repo, args.top),
            ]),
        ])
        if copy_html_to_clipboard(html):
            print("\n✓ Copied to clipboard — Cmd-V straight into the meeting doc.",
                  file=sys.stderr)


if __name__ == "__main__":
    main()
