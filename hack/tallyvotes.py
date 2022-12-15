#!/usr/bin/env python

import json
import pprint
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage tallyvotes.py <PR_URL>")
    sys.exit(1)

pr_url = sys.argv[1]
pr_url_parts = pr_url.split('/')
org_repo = pr_url_parts[3] + "/" + pr_url_parts[4]
pr_num = pr_url_parts[-1]

maintainers_url = "https://raw.githubusercontent.com/argoproj/argoproj/master/MAINTAINERS.md"
maintainers = subprocess.check_output("curl --silent "+maintainers_url+" | grep -e '^|.*github.com' | grep Yes | awk -F'[' '{print $2}' | awk -F']' '{print $1}'", shell=True).split()

maintainer_votes = {}
for maintainer in maintainers:
    maintainer_votes[maintainer] = 0
community_votes = {}

pr_meta = json.loads(subprocess.check_output("gh pr view "+pr_num+" -R "+org_repo+" --comments --json comments,reviews", shell=True))
comments = pr_meta['comments'] + pr_meta['reviews']

# First deduplicate the votes (in case a maintainer voted twice).
# The last comment overrides previous comments.
for comment in comments:
    author_login = comment['author']['login']
    if author_login in maintainer_votes:
        if "+1" in comment['body']:
            maintainer_votes[author_login] = 1
        elif "-1" in comment['body']:
            maintainer_votes[author_login] = -1
    else:
        if "+1" in comment['body']:
            community_votes[author_login] = 1
        elif "-1" in comment['body']:
            community_votes[author_login] = -1

# Now tally up the votes
totals = {
    'maintainers': {
        'yay': 0,
        'nay': 0,
        'abstain': 0,
        'total': 0,
    },
    'community': {
        'yay': 0,
        'nay': 0,
        'abstain': 0,
        'total': 0,
    },
}

for subtotal, votes in [(totals['maintainers'], maintainer_votes), (totals['community'], community_votes)]:
    for author, vote in votes.items():
        subtotal['total'] += 1
        if vote > 0:
            subtotal['yay'] += 1
        elif vote < 0:
            subtotal['nay'] -= 1
        else:
            subtotal['abstain'] += 1

vote_fmt = "{:20}{}"
print(vote_fmt.format("MAINTAINER", "VOTE"))
print(vote_fmt.format("----------", "----"))
for key, value in maintainer_votes.items():
    print(vote_fmt.format(key, value))
print('')

print(vote_fmt.format("COMMUNITY-USER", "VOTE"))
print(vote_fmt.format("--------------", "----"))
for key, value in community_votes.items():
    print(vote_fmt.format(key, value))
print('')

summary_fmt = '{:15}{:>5}{:>5}{:>9}{:>7}'
print(summary_fmt.format('SUMMARY', 'YAY', 'NAY', 'ABSTAIN', 'TOTAL'))
print(summary_fmt.format('-------', '---', '---', '-------', '-----'))
print(summary_fmt.format('MAINTAINERS', totals['maintainers']['yay'], totals['maintainers']['nay'], totals['maintainers']['abstain'], totals['maintainers']['total']))
print(summary_fmt.format('COMMUNITY-USER', totals['community']['yay'], totals['community']['nay'], '-', totals['community']['total']))
