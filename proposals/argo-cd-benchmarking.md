---
name: argo-cd-benchmarking
about: argo-cd-benchmarking
title: "[PROJECT ONBOARDING] argo-cd-benchmarking"
labels: project onboarding
---

- [x] What is your project repository Github URL?
  - Will reside at a newly created repo: `https://github.com/argoproj-labs/argo-cd-benchmarking`
- [x] Do you wish to host your project repository https://github.com/argoproj-labs or https://github.com/argoproj ?
    - `argoproj-labs`
- [x] Does your project focus on enhancing or providing additional features to one of the existing [core projects](https://github.com/argoproj/argoproj#what-is-argoproj)? If yes, which of the core projects is your proposed project related to?
  - The project focuses on scalability benchmarking of Argo CD as described in [the scalability benchmarking proposal](https://github.com/argoproj/argo-cd/pull/12662). 
- [x] Is it endorsed by any of the Argo subproject maintainers? Please mention sponsors from the subproject.
  - @jannfis
  - @todaywasawesome
- [x] How does it align with the goals of the Argo community?
    - Users of Argo CD are interested to know how to scale Argo CD, what configuration tweaks and deployment options they have, and how far they can push resources. This repository will hold the benchmarking tooling need to pursue [the scalability benchmarking proposal](https://github.com/argoproj/argo-cd/pull/12662).
- [x] Who will maintain the project going forward?
    - SIG Scalability will start by owning the repository with maintaince delegated to the specific members, @andklee and @morey-tech.
    - Membership of the repository will not be limited to SIG Scalability members.
- [x] What is your project license?
  - Apache-2.0 (same as Argo CD).