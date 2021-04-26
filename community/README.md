# Argoproj Community

Welcome to the Argo Community!

Argo is an open, community driven project to make it easy to use Kubernetes for getting useful work done.  This document describes the organizational structure of the Argo Community including the roles, responsibilities and processes that govern Argo projects and community.

The Argo community has two regular meetings:

* Argo Workflows and Argo Events
  * Meets monthly, 3rd Wednesday of every month 10:00 AM Pacific Time
  * [Agenda & Meeting Notes](https://docs.google.com/document/d/1DKR4VQ-04DJfHOh6S6-cbQw6MiWppC0k7afORiiy6XQ/edit)

* Argo CD and Argo Rollouts
  * Meets monthly, 1st Wednesday of every month 10:00 AM Pacific Time
  * [Agenda & Meeting Notes](https://docs.google.com/document/d/1ttgw98MO45Dq7ZUHpIiOIEfbyeitKHNfMjbY5dLLMKQ/edit)

Most of the community discussions happen in the Argo Slack organization. Please join the organization [here](https://argoproj.github.io/community/join-slack)

## Projects

Argo is organized into a set of projects. Each project has at least one lead. The leads are responsible for driving the project, publishing a roadmap, organizing community meetings, publishing meeting notes, and reporting on the current status of the project.

The projects are:

* [Argo Workflows](https://github.com/argoproj/argo) - Container-native Workflow Engine
* [Argo CD](https://github.com/argoproj/argo-cd) - Declarative GitOps Continuous Delivery
* [Argo Events](https://github.com/argoproj/argo-events) - Event-based Dependency Manager
* [Argo Rollouts](https://github.com/argoproj/argo-rollouts) - Progressive Delivery with support for Canary and Blue Green deployment strategies

## Community Meetings

Approvers and leads for each project are responsible for organizing regular community meetings to provide status updates and solicit feedback.

* Meeting agendas should be published at least one week prior to the meeting.
* Community members should be able to attend the meetings remotely.
* Meeting notes summarizing the meeting and any decisions made should be published
within 24 hours of the meeting.
* Meeting recordings should be published within one week of the meeting.

## Contributing to Argo

Read and abide by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

Argo Project uses the DCO.
* https://github.com/apps/dco/

Please signoff your contributions by doing ONE of the following:
* Use `git commit -s ...` with each commit to add the signoff or
* Manually add a `Signed-off-by: Your Name <your.email@example.com>` to each commit message.

The email address must match your primary GitHub email. You do NOT need cryptographic (e.g. gpg) signing.
* Use `git commit -s --amend ...` to add a signoff to the latest commit, if you forgot.

To automatically signoff on every commit, copy the `community/dco-signoff-hook/prepare-commit-msg` file to the `.git/hooks` directory in your repo or if you already have such a hook, merge the contents into your existing hook.

## Project Governance

Goverance doc [here](GOVERNANCE.md)
