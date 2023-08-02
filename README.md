[![slack](https://img.shields.io/badge/slack-argoproj-brightgreen.svg?logo=slack)](https://argoproj.github.io/community/join-slack)

# Argoproj - Get stuff done with Kubernetes

![Argo Image](docs/assets/argo.png)

## News

Argo Project has moved from the CLA to the DCO.
* https://github.com/apps/dco/

Please signoff your contributions by doing ONE of the following:
* Use `git commit -s ...` with each commit to add the signoff or
* Manually add a `Signed-off-by: Your Name <your.email@example.com>` to each commit message.

The email address must match your primary GitHub email. You do NOT need cryptographic (e.g. gpg) signing.
* Use `git commit -s --amend ...` to add a signoff to the latest commit, if you forgot.

Argo CD Achieves SLSA Level 3. Please read the [SLSA Assessment Report](docs/software_supply_chain_slsa_assessment_chainguard_2023.pdf) for more.

To automatically signoff on every commit, copy the `community/dco-signoff-hook/prepare-commit-msg` file to the `.git/hooks` directory in your repo or if you already have such a hook, merge the contents into your existing hook.

## What is Argoproj?

Argoproj is a collection of tools for getting work done with Kubernetes.
* [Argo Workflows](https://github.com/argoproj/argo-workflows) - Container-native Workflow Engine
* [Argo CD](https://github.com/argoproj/argo-cd) - Declarative GitOps Continuous Delivery
* [Argo Events](https://github.com/argoproj/argo-events) - Event-based Dependency Manager
* [Argo Rollouts](https://github.com/argoproj/argo-rollouts) - Progressive Delivery with support for Canary and Blue Green deployment strategies

Also [argoproj-labs](https://github.com/argoproj-labs) is a separate GitHub org that we setup for community contributions related to the Argoproj ecosystem. Repos in argoproj-labs are administered by the owners of each project. Please reach out to us on the Argo slack channel if you have a project that you would like to add to the org to make it easier to others in the Argo community to find, use, and contribute back.

## Community Blogs and Presentations

Project specific community blogs and presentations are at
* [Argo Workflows](https://github.com/argoproj/argo-workflows/blob/master/README.md#community-blogs-and-presentations)
* [Argo CD](https://github.com/argoproj/argo-cd/blob/master/README.md#community-blogs-and-presentations)
* [Argo Events](https://github.com/argoproj/argo-events/blob/master/README.md#community-blogs-and-presentations)
* [Argo Rollouts](https://github.com/argoproj/argo-rollouts/blob/master/README.md#community-blogs-and-presentations)

## Adopters

Each Argo sub-project maintains its own list of adopters. Those lists are available in the respective project repositories:
* [Argo Workflows](https://github.com/argoproj/argo-workflows/blob/master/USERS.md)
* [Argo CD](https://github.com/argoproj/argo-cd/blob/master/USERS.md)
* [Argo Events](https://github.com/argoproj/argo-events/blob/master/USERS.md)
* [Argo Rollouts](https://github.com/argoproj/argo-rollouts/blob/master/USERS.md)

## Contributing

To learn about how to contribute to Argoproj, see our [contributing documentation](community/CONTRIBUTING.md).
Argo contributors must follow the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

For help contributing, visit the [#argo-contributors channel](https://cloud-native.slack.com/archives/C020XM04CUW) in CNCF Slack.

To learn about Argoproj governance, see our [community governance document](community/GOVERNANCE.md).

## Project Resources
* [Argo Community Meeting Calendar](https://calendar.google.com/calendar/embed?src=argoproj@gmail.com)
  * [ICS file](https://calendar.google.com/calendar/ical/argoproj%40gmail.com/public/basic.ics)
* Argo GitHub:  https://github.com/argoproj
* Argo website: https://argoproj.github.io
* Argo Slack:   https://argoproj.github.io/community/join-slack
