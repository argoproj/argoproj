# Ecosystem Projects

## About


The [Argo Project](https://github.com/argoproj) consists of four core projects that implement the main use-cases. In addition to the core project repositories the [Argo Project Labs](https://github.com/argoproj-labs) organization hosts repositories of dependencies and ecosystem projects associated with the core projects.

* Core project dependencies are projects which are either shared code libraries (such as [gitops-engine](https://github.com/argoproj/gitops-engine),
[pkg](https://github.com/argoproj/pkg) or [argo-ui](https://github.com/argoproj/argo-ui) ) or repositories that host release/deployments
artifacts ( such as [argo-helm](https://github.com/argoproj/argo-helm), or [homebrew-tap](https://github.com/argoproj/homebrew-tap) ). 

* The ecosystem projects are those projects which implement experimental features or opinionated use cases that are useful for the sub-set of users.

This document outlines the rationale behind the classification of a project as an ecosystem project and the process of adding a new project to the Argo community.

---

## Eligibility

The ecosystem project *must* enhance one of the existing core projects as opposed to focusing on a entirely new area not closely related to the core Argo projects

### **Experimental Features**


The ecosystem project may be an experimental implementation of a new feature that may eventually be merged into one of the core projects. Once the project is mature enough it may be considered for merging into one of the core project repositories.

A good example is the [ApplicationSet controller](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/) that simplifies managing Argo CD applications. The functionality was developed in a separate repository under https://github.com/argoproj-labs to increase development velocity and simplify onboarding early adopters. It was [later moved](https://github.com/argoproj/argo-cd/issues/7351) to https://github.com/argoproj before [eventually being merged](https://github.com/argoproj/applicationset/issues/528) into https://github.com/argoproj/argo-cd to allow tighter integration of ApplicationSet support with Argo CD.


### **Opinionated Enhancements**

The project might provide an implementation of an opinionated feature that is useful for a sub-set of core project users and should be distributed separately.
The good examples are:

* [argocd-operator](https://github.com/argoproj-labs/argocd-operator) - A Kubernetes operator for managing an Argo CD instance.
* [argocd-notifications](https://github.com/argoproj-labs/argocd-notifications) - A Kubernetes controller which integrates Argo CD with various notification services such as Slack, SMTP etc.
* [argocd-image-updater](https://github.com/argoproj-labs/argocd-image-updater) - A tool that automates container image registry monitoring and updates image tags in Argo CD applications when new image version get pushed.


---

## Requirements

### Security

All Argoproj Labs projects must contain a `SECURITY.md` file documenting:
* Contacts or mailing list for reporting vulnerabilities
* Details about the project security policies

In the future, we may require each project perform self-assessment on what best practices are followed, such as the [CII badge](https://bestpractices.coreinfrastructure.org/en).

### Container Registry

Since projects under Argoproj labs are considered experimental and/or opinionated enhancements,
container images shall be housed under a separate container registry separate from quay.io/argoproj,
under [quay.io/argoprojlabs](https://quay.io/organization/argoprojlabs).

It is strongly preferred *not* to give any individual users the ability to push images directly to
quay.io repositories, and instead use [Robot Accounts](https://docs.quay.io/glossary/robot-accounts.html)
to automatically push images as part of CI/GitHub Actions. Project leads can configure a robot
account token as a GitHub secret to use as part of CI.

---

## Proposal Process

### **Decide on the GitHub Organization**

Argo community uses two Github organizations to host project repositories: https://github.com/argoproj
and https://github.com/argoproj-labs .

The https://github.com/argoproj-labs is a home for most ecosystem projects and experimental features that may be considered for a merge into one of the core projects. If the project is still in the development phase and
you are looking for feedback/early adopters then it is recommended to use https://github.com/argoproj-labs
organization, since is specifically created to showcase, share, and collaborate on Argo related projects.

Note, [argoproj-labs](https://github.com/argoproj-labs) is **not** necessarily an incubator for moving projects into
[argoproj](https://github.com/argoproj). 

Only projects that are very tightly related to the core projects and have reached a certain level of maturity may be
considered for moving to [argoproj](https://github.com/argoproj). 

The majority of projects may live in 
[argoproj-labs](https://github.com/argoproj-labs) in the entirety of its lifespan.

### **Project Proposal Issue**

Once you are ready to propose the onboarding of a new project into [argoproj-labs](https://github.com/argoproj-labs) or wish to move an existing project from
[argoproj-labs](https://github.com/argoproj-labs) to [argoproj](https://github.com/argoproj), please create a Pull Request with the proposal to the [proposals](/proposals) directory in the 
[argoproj/argoproj](https://github.com/argoproj/argoproj) repository and answer questions
listed in the [proposal template](/ecosystem-projects/001-project-onboarding.md).

### **Proposal Review**

The project proposal will be reviewed by the project maintainers in a timely manner. The maintainers might involve
the steering committee if necessary. Once the proposal is approved Argoproj maintainers will work on moving the
repository and assist with project infrastructure setup (such as Github team, docker registry etc).
