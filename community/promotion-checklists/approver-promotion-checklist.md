The following steps should be completed when someone is promoted to an approver role:

- [ ] Invite to #argo-approvers Slack channel
- [ ] Update [argoproj/.project `maintainers.yaml`](https://github.com/argoproj/.project/blob/main/maintainers.yaml): add the person to the subproject `*-approvers` group (e.g. `argocd-approvers`).

> **Note:** For a promotion to a **scoped** approver role (approval limited to one or more areas of a subproject, e.g. `argocd-approvers-docs`, `argocd-approvers-ui`), do **not** update `maintainers.yaml`. Scoped approver groups are not tracked in `maintainers.yaml`; instead, add the person to the corresponding scoped GitHub team(s) manually.
