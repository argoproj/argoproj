# Security Policy for Argo projects

Versions:
* v1.2 (2022-03-22) - Add Argoproj-labs disclaimer
* v1.1 (2021-08-08) - Update contacts
* v1.0 (2020-04-30) - Initial version

## Preface

The security policy in `argoproj/argoproj` acts as a proxy policy for the Argo
sub-projects
[Argo Workflows](https://github.com/argoproj/argo-workflows),
[Argo Events](https://github.com/argoproj/argo-events),
[Argo Rollouts](https://github.com/argoproj/argo-rollouts) and
[Argo CD](https://github.com/argoproj/argo-cd),

For more specific policies, please refer to the following documents in their
respective code repositories:

* [Security Policy for Argo Workflows](https://github.com/argoproj/argo-workflows/blob/master/SECURITY.md)
* [Security Policy for Argo Events](https://github.com/argoproj/argo-events/blob/master/SECURITY.md)
* [Security Policy for Argo Rollouts](https://github.com/argoproj/argo-rollouts/blob/master/docs/security.md)
* [Security Policy for Argo CD](https://github.com/argoproj/argo-cd/blob/master/SECURITY.md)

### Argoproj Labs

The [Argoproj Labs](https://github.com/argoproj-labs) projects are a set community maintained projects (housed under a single GitHub organization) and do not fall under the scope of CNCF. They are independently maintained and typically have a separate set of members and maintainers from the [Argoproj maintainers](MAINTAINERS.md). Labs project have  **_not_** undergone the same security reviews, membership requirements, and have different security practices than the four Argo sub-projects. All labs projects are required to have a `SECURITY.md` documenting their security policies as well as listing their security contacts for reporting vulnerabilities. 

## Reporting Vulnerabilities

In general, we kindly ask you for responsible disclosure of any security
vulnerabilities you may have found in one of our projects. Please do not create
a GitHub issue, but instead contact us via e-mail at the following address:

* cncf-argo-security@lists.cncf.io

For reporting vulnerabilities to projects under Argoproj Labs, please visit the project's `SECURITY.md` policy to reach the correct contacts.

We also kindly ask you to allow us some time for analysing the report and react
on it. We will get in contact with you as soon as possible.

## Public Disclosure

Please refer to the sub-projects' dedicated security policies (see above) for
specific details on how we handle reported vulnerabilities, public disclosure,
crediting and other information.
