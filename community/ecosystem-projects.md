# Ecosystem Projects

The Argoproj consists of four core projects that implement the main use-cases. In addition to the core project repositories the [argoproj](https://github.com/) organization hosts repositories of core project dependencies and ecosystem projects.

* Core project dependencies are either shared code libraries (such as [gitops-engine](https://github.com/argoproj/gitops-engine),
[pkg](https://github.com/argoproj/pkg) or [argo-ui](https://github.com/argoproj/argo-ui) ) or repositories that host release/deployments
artifacts ( such as [argo-helm](https://github.com/argoproj/argo-helm), or [homebrew-tap](https://github.com/argoproj/homebrew-tap) ). 

* The ecosystem projects implement experimental features or opinionated use cases that are useful for the sub-set of users.

This document describes in which projects qualify to be an ecosystem project and the process of adding a new one.

## Eligibility

The ecosystem project must enhance one of the existing core projects as opposed to focusing on a totally new area not related to Argo.

**Experimental Feature**

The project might be an experiment implementation of a new feature that eventually will be merged into one of the core projects. A good example
is https://github.com/argoproj-labs/applicationset project that simplifies managing Argo CD applications. The functionality is developed in
a separate repository to increase development velocity and simplify onboarding early adopters.

Once project is mature enough it will be merged into the core project repository.


**Opinionated Enhancement**

The project might provide an implementation of an opinionated feature that is useful for a sub-set of core project users and should be distributed separately.
The good examples are:

* [argocd-operator](https://github.com/argoproj-labs/argocd-operator) - a Kubernetes operator for managing set of Argo CD.
* [argocd-notifications](https://github.com/argoproj-labs/argocd-notifications) - integrates Argo CD with various notification services such as Slack, SMTP etc.
* [argocd-image-updater](https://github.com/argoproj-labs/argocd-image-updater) - automates Docker registry monitoring and updates image tags in Argo CD applications when new image version get pushed.

## Process

**Initial Phase**

If the project is still in the development phase and you are looking for feedback/early adopters then
it is recommended to move your project repository to https://github.com/argoproj-labs organization.
The [argoproj-labs](https://github.com/argoproj-labs)  is specifically created to showcase, share,
and collaborate on Argo related projects. To initiate migration create a new issue
[here](https://github.com/argoproj-labs/community/issues/new) and work with Argoproj maintainers.

**Project Proposal Issue**

Once you are confident that the project is mature and ready for production create a new
[issue](https://github.com/argoproj/argoproj/issues/new?template=project-onboarding.md) in
[argoproj/argoproj](https://github.com/argoproj/argoproj) repository and answer questions
listed in the issue template.

**Steering Committee Review**

The project proposal will be reviewed during the next steering committee meeting. Once the proposal
is approved Argoproj maintainers will work on moving the repository and assist with project
infrastructure setup (such as Github team, Docker registry etc).
