# Argo Decision Log

This log file documents decisions for which there are no other lasting artifacts.

## Revise Argo CLA to follow CNCF guidelines

### Date

2020 Sep 19

### Context

Now that the Argo Project is a part of the CNCF, we should revise the Argo CLA to follow CNCF guidelines.

### Decision

For individual contributors, we will move from the current Argo Individual CLA to the DCO.
https://github.com/apps/dco/
https://developercertificate.org/

For corporate contributions, we will move from the current Argo Corporate CLA to the CNCF Corporate CLA.
https://github.com/cncf/cla/blob/master/corporate-cla.pdf

### Rationale

Most CNCF projects use the DCO for individual contributors. The DCO is viewed as a lighter more developer-friendly alternative to the individual CLA and provides strong attribution of contributions to the contributor.

While the DCO is sufficient for individual contributions, it is not a good mechanism for corporations to grant rights, including intellectual property rights, to an open source project. For example, the developer submitting a PR may not have rights to contribute work he performed for his employer or intellectual property rights that may be needed to use the contribution.

The DCO also does not provide any mechanism for coporations to document  which employees are allowed to contribute to a particular project.

In consequence, for the protection of the contributors and users of the Argo Community, we will continue to use a corporate CLA for corporate contributions.

### Dissenting Opinions

None.

### Approvers
* Ben Browning (Red Hat)
* Edward Lee (Intuit)
* Jesse Suen (Intuit)
* Lei Zhang (Alibaba)
* Mike Bowen (BlackRock)
* Mukulika Kapas (Intuit)
* Shoubhik Bose (Red Hat)
