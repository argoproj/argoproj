# Feature Status

This document describes the different statuses a given feature can
have in Argo projects.

## Overview

Argo umbrella projects are maintained by the open-source community.
This means that features are provided by different organizations with
different use-cases. While certain features are battle tested by
corporations with large infrastructure, this is not always the case.
Feature status is a classification that can be used by Argo projects
to clarify and set expectations about a given functionality. However,
not every feature will have to be associated with a given status.
Maintainers will use this classification as a framework and gradually
associate features with the proper current status. When available, the
current status will be informed in the documentation of that specific
feature.

## Definition

Argo projects adopt the standard software life cycle terminology to
define the different feature statuses:

- _Alpha_
- _Beta_
- _Stable_

### Alpha

_Alpha_ means that a feature is in its early stage and is considered
as experimental which means that it can be removed from future
releases. This is an useful status to use when there are uncertainties
about a new feature and maintainers want to get feedback from the
community. _Alpha_ features are usually behind feature flags disabled
by default. Users are expected to understand the risks of enabling
_Alpha_ features.

### Beta

_Beta_ features are usually enabled by default and are not considered
as experimental. _Beta_ features are considered in its early maturity
stage. This means that common use cases are functional but there are
known uncovered edge cases. Edge cases will be tracked as issues and
are expected to be voted on. Votes take place by adding a thumbs up
emoji reaction in the main description of an issue. In most cases,
issues with more votes will take higher priority. _Beta_ features may
not be backwards compatible with previous releases of the feature
while in this status.

### Stable

_Stable_ features are tested and validated with various use cases, are
considered mature, and are expected to be backwards compatible. Issues
will be tracked as bugs and depending on the impact a patch with the
fix might be released.

## The promotion process

Features can be introduced in Argo projects in _Alpha_ or _Beta_
statuses. If a feature is not introduced with a particular status,
it is assumed to be stable. After a feature is introduced with a 
specific status it can then be promoted to the next one.

The transition from one status to the other respect the following
rules:

1. _Alpha_ features can transition to _Beta_.
1. If for some reason an _Alpha_ feature fails to be promoted, it will
eventually be removed from the code base.
1. _Beta_ features can transition to _Stable_.
1. If for some reason a _Beta_ feature fails to be promoted, it could
eventually be removed from the code base followed from at least one
release deprecation period.
1. If a serious issue is identified in a stable feature that justifies
it to be removed, it will follow at least two releases deprecation
period.

If a _Beta_ or _Stable_ feature is decided to be removed, it will
respect a deprecation period. The information will be available in the
release notes and in the official documentation for that given
feature.

The diagram bellow represents the possible transitions features can
have:

``` 
                 ┌───────┐
 New Feature'───►│ Alpha ├───► Removed
                 └───┬───┘
                     │
                     │
                     │
                     ▼
                  ┌──────┐
 New Feature"────►│ Beta ├───► Removed
                  └──┬───┘
                     │
                     │
                     ▼
                 ┌────────┐
                 │ Stable ├──► Removed
                 └────────┘
```

Promoting a feature is a responsibility shared between maintainers,
contributors and the user community. Any of those parties can request
a feature to be promoted. Ideally this can be done by creating an
issue or a discussion in the Github repository of the project
containing that feature. Promotion requests can be brought to
maintainers attention in our weekly [Argo Contributors Office
hours][1] meeting.

## What it means for Argo users

Feature status is a framework to provide transparency and allow
setting expectations for Argo users. It should be used to support the
decision making process about whether or not a given feature is
feasible to be leveraged by a company or individual. Argo projects
depend on the user base to provide valuable feedback and submit bugs
with good information so features can be promoted to a more mature
stage.

## What it means for Argo contributors

If you are contributing with new feature in one of the Argo projects,
please classify it with one of the statuses described in this
document. The current status should be indicated next to every feature
in our official documentation. The format of a feature status in the
documentation should be:

`Current Status: <status> (Since <version>)`

Since relates to the version it changed the status, _not_ the version
when the feature was first introduced in the codebase.

Example:

`## Server-Side Apply Current Status: Beta (Since v2.5.0)`

The status must also be informed in the title of the PR introducing
the feature so it can be available in the release notes.

The format of a feature status in the PR title should be:

`feat: <title> (<status>)`

Example:

`feat: My awesome new feature description (Alpha)`

Note: When a feature is promoted, remember to always update the
documentation so the current status is correctly informed to our
user base. It is also important to follow the PR title format
defined above.

[1]: https://docs.google.com/document/d/1xkoFkVviB70YBzSEa4bDnu-rUZ1sIFtwKKG1Uw8XsY8/edit?pli=1#
