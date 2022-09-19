# Contributing to Argo Projects

This document explains the common procedures expected by contributors while submitting code to Argo projects.

## Code of Conduct

Please read and abide by the [CNCF Community Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)

## General workflow

Once a github issue is accepted and assigned to you, please follow general workflow in order to submit your contribution:
1. Fork the target repository under your github username.
2. Create a branch in your forked repository for the changes you are about to make.
3. Commit your changes in the branch you created in step 2. All commits need to be signed-off. Check the [legal](#legal) section bellow for more details.
4. Push your commits to your remote fork.
5. Create a Pull Request from your remote fork pointing to the HEAD branch (usually `master` branch) of the target repository.
6. Check the github build and ensure that all checks are green.

## Legal

Argo Project uses Developer Certificate of Origin ([DCO](https://github.com/apps/dco/)).

Please signoff your contributions by doing ONE of the following:
* Use `git commit -s ...` with each commit to add the signoff or
* Manually add a `Signed-off-by: Your Name <your.email@example.com>` to each commit message.

The email address must match your primary GitHub email. You do NOT need cryptographic (e.g. gpg) signing.
* Use `git commit -s --amend ...` to add a signoff to the latest commit, if you forgot.

To automatically signoff on every commit, copy the `community/dco-signoff-hook/prepare-commit-msg` file to the `.git/hooks` directory in your repo or if you already have such a hook, merge the contents into your existing hook.

*Note*: Some projects will provide specific configuration to ensure all commits are signed-off. Please check the project's documentation for more details.

## Tests

Make sure your changes are properly covered by automated tests. We aim to build an efficient test suite that is low cost to maintain and bring value to project. Prefer writing unit-tests over heavy end-to-end (e2e) tests. However, sometimes e2e tests are necessary. If you aren't sure, ask one of the maintainers about the requirements for your pull-request.
