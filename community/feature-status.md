# Feature Status

This document describes the different status a given feature can have in Argo projects.

## Overview

Argo umbrella projects are maintained by the open-source community. This means that features are provided by different companies with different use-cases. While certain features are battle tested by corporations with large infrastructure, this is not always the case. Feature status is a classification that can be used by Argo projects to clarify and set expectations about a given functionality. However, not every feature will have to be associated with a given status. Maintainers will use this classification as a framework and gradually associate features with the proper current status. When available, the current status will be informed in the documentation of that specific feature.

## Definition

Argo projects adopt the standard software life cycle terminology to define the different feature statuses:

- Alpha
- Beta
- Stable

### Alpha

Alpha means that a feature is in its early stage and is considered as experimental. It can be removed from future releases followed from a deprecation stage. This is a useful status to use when there are uncertainties about a new feature and maintainers want to get feedback from the community. Alpha features are usually behind feature flags disabled by default. Users are expected to understand the risks of enabling Alpha features in production environment.

### Beta

Beta features are usually enabled by default and are not considered as experimental. Beta features are considered in its early maturity stage. This means that common use cases are functional but there are known uncovered edge cases. Edge cases will be tracked as issues and are expected to be voted. In most cases, highly voted issues will take higher priority. Beta features may not be backwards compatible with previous releases while in this status.

### Stable

Stable features are tested and validated with a variety of use cases. Stable features are considered mature and are expected to be backwards compatible. Issues will be tracked as bugs and depending on the impact a patch with the fix might be released.

## The promotion process

```
                   ┌─────┐
 New Feature'─────►│Alpha├──────┐
                   └─────┘      │
                                │
                                │
                                ▼
                              ┌────┐
        New Feature"─────────►│Beta│
                              └─┬──┘
                                │
                                │
                                │
                                │
                   ┌──────┐     │
                   │Stable│◄────┘
                   └──────┘
```

## What it means for Argo users

## What it means for Argo contributors
