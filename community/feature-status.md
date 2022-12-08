# Feature Status

This document describes the different status a given feature can have
in Argo projects.

## Overview

Argo umbrella projects are maintained by the open-source community.
This means that features are provided by different companies with
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

- Alpha
- Beta
- Stable

### Alpha

Alpha means that a feature is in its early stage and is considered as
experimental. It can be removed from future releases followed from a
deprecation stage. This is a useful status to use when there are
uncertainties about a new feature and maintainers want to get feedback
from the community. Alpha features are usually behind feature flags
disabled by default. Users are expected to understand the risks of
enabling Alpha features in production environment.

### Beta

Beta features are usually enabled by default and are not considered as
experimental. Beta features are considered in its early maturity
stage. This means that common use cases are functional but there are
known uncovered edge cases. Edge cases will be tracked as issues and
are expected to be voted. In most cases, highly voted issues will take
higher priority. Beta features may not be backwards compatible with
previous releases while in this status.

### Stable

Stable features are tested and validated with a variety of use cases.
Stable features are considered mature and are expected to be backwards
compatible. Issues will be tracked as bugs and depending on the impact
a patch with the fix might be released.

## The promotion process

Features can be introduced in Argo projects in Alpha or Beta statuses.
After a feature is introduced with a specific status it can then be
promoted to the next one.

The transition from one status to the other respect the following
rules:

1. Alpha features can transition to Beta.
1. If for some reason an Alpha feature fails to be promoted, it will
eventually be removed from the code base.
1. Beta features can only transition to Stable.

The diagram bellow represents the possible transitions features can
have:

```
                    ┌───────┐
  New Feature'─────►│ Alpha ├───► Removed
                    └───┬───┘
                        │
                        ▼
                     ┌──────┐
  New Feature"──────►│ Beta │
                     └──┬───┘
                        │
          ┌────────┐    │
          │ Stable │◄───┘
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

Feature status was introduced as a framework to provide transparency
and allow setting up expectations for Argo users. It should be used to
support the decision making process about whether or not a given
feature is feasible to be leveraged by a company or individual. Argo
projects depend on the user base to provide valuable feedback and
submit bugs with good information so features and be promoted to a
more mature stage.

## What it means for Argo contributors

If you are contributing with new feature in one of the Argo projects,
please consider classifying it in one of the statuses described in
this document. The current status should be indicated next to every
feature in our official documentation.

The format of a feature status should be: `Current Status: <status>
(Since <version>)`

Example:

``` ## Server-Side Apply Current Status: Beta (Since v2.5.0) ```


[1]:
https://docs.google.com/document/d/1xkoFkVviB70YBzSEa4bDnu-rUZ1sIFtwKKG1Uw8XsY8/edit?pli=1#
