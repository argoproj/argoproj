Reviewers are maintainers, so promoting someone to reviewer adds them to the maintainer roster.

The following steps should be completed when someone is promoted to a reviewer role:

- [ ] Invite to the #argo-maintainers Slack channel
- [ ] Add the user to the appropriate subproject `*-maintainers` group (e.g. `argocd-maintainers`) in [argoproj/.project `maintainers.yaml`](https://github.com/argoproj/.project/blob/main/maintainers.yaml). The automation syncs the GitHub org team and provisions CNCF access; this supersedes manually editing the [CNCF maintainers CSV](https://github.com/cncf/foundation/blob/main/project-maintainers.csv).
- [ ] Add the new maintainer's row (name, GitHub ID, roles, affiliation) to the hand-maintained table in [MAINTAINERS.md](https://github.com/argoproj/argoproj/blob/master/MAINTAINERS.md). `maintainers.yaml` stays the source of truth for membership; this file is for display.
