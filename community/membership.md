# Community Membership

This document outlines the various responsibilities of contributor roles in
Argoproj. The Argo project is currently subdivided into four main subprojects:

* [Argo Workflows](https://github.com/argoproj/argo-workflows)
* [Argo CD](https://github.com/argoproj/argo-cd)
* [Argo Events](https://github.com/argoproj/argo-events)
* [Argo Rollouts](https://github.com/argoproj/argo-rollouts)

Responsibilities for roles are scoped to these subprojects.

| Roles        | Responsibilities| Requirements  | Defined by|
| -------------|:---------------|:-------------|:-------------|
| member       | active contributor in the community | sponsored by 2 approvers or leads. multiple contributions to the project. | Argoproj GitHub org member|
| reviewer     | review contributions from other members | sponsored by a lead. history of review and authorship in a subproject | OWNERS file reviewer entry|
| approver     | approve accepting contributions     | sponsored by a lead. highly experienced and active reviewer + contributor to a subproject  | OWNERS file approver entry |
| lead         | set direction and priorities for a subproject | demonstrated responsibility and excellent technical judgement for the subproject |  OWNERS file owner entry |



## New contributors

New contributors should be welcomed to the community by existing members,
helped with PR workflow, and directed to relevant documentation and
communication channels.



## Established community members

Established community members are expected to demonstrate their adherence to the
principles in this document, familiarity with project organization, roles,
policies, procedures, conventions, etc., and technical and/or writing ability.
Role-specific expectations, responsibilities, and requirements are enumerated
below.



## Member

Members are continuously active contributors in the community. They can have issues and PRs 
assigned to them. Members are expected to remain active contributors to the community. Members are
given the [Triage](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-permission-levels-for-an-organization) GitHub role to Argoproj repositories, in order to
facilitate issue management and moderate discussions.

Defined by: Member of the Argoproj GitHub organization

### Requirements

- Enabled [two-factor authentication] on their GitHub account
- Have made multiple contributions to the project or community.  Contribution may include, but is not limited to:
    - Authoring or reviewing PRs on GitHub
    - Filing or commenting on issues on GitHub
    - Contributing to SIG, subproject, or community discussions (e.g. meetings, Slack, email discussion
      forums, Stack Overflow)
- Actively contributing to 1 or more subprojects.
- Sponsored by 2 approvers or leads. **Note the following requirements for sponsors**:
    - Sponsors must have close interactions with the prospective member - e.g. code/design/proposal review, coordinating
      on issues, etc.
    - Sponsors must be approvers in at least 1 OWNERS file either in any of the four main subprojects in the [Argoproj org].
      - An approver in the [Argoproj org] may sponsor someone for the [Argoproj org]
      or any of the related [Argoproj GitHub organizations]; as long as it's a project they're involved with.
      - A sponsor who is an approver in any of the related [Argoproj GitHub organizations]
      but not in the [Argoproj org] can only sponsor someone for the orgs they are associated with.
    - Sponsors must be from multiple member companies to demonstrate integration across community.
- **[Open an issue][membership request] against the argoproj/argoproj repo**
   - Ensure your sponsors are @mentioned on the issue
   - Complete every item on the checklist ([preview the current version of the template][membership template])
   - Make sure that the list of contributions included is representative of your work on the project.
- Have your sponsoring reviewers reply confirmation of sponsorship: `+1`
- Once your sponsors have responded, your request will be reviewed by the project leads. Any missing information will be requested.

### Responsibilities and privileges

- Have the ability to moderate GitHub discussions
- Have the ability to triage GitHub issues through labeling
- Responsive to issues and PRs assigned to them
- Responsive to mentions of subprojects they are members of
- Active owner of code they have contributed (unless ownership is explicitly transferred)
  - Code is well tested
  - Tests consistently pass
  - Addresses bugs or issues discovered after code is accepted
- Members are welcome and encouraged to review PRs and proposals.
- They can be assigned to issues and PRs, and people can ask members for reviews with a `/cc @username`.

**Note:** members who frequently contribute code are expected to proactively
perform code reviews and work towards becoming a primary *reviewer* for the
subproject that they are active in.



## Reviewer

Reviewers are able to review code for quality and correctness on some part of a
subproject. They are knowledgeable about both the codebase and software
engineering principles.

**Defined by:** *reviewers* entry in an OWNERS file in a repo owned by the
Argoproj project.

Reviewer status is scoped to a part of the codebase.

**Note:** Acceptance of code contributions requires at least one approver in
addition to the assigned reviewers.

While these guidelines are going to be used for setting contribution expectations, 
the maintainers will recognize the impact of an individual's contribution while 
making a decision on promotion an individual to a "reviewer."

### Requirements

The following apply to the part of codebase for which one would be a reviewer in
an `OWNERS` file.

- Member for at least 3 months
- Active community participation (meetings, slack, stack overflow) and interact with issues for at least 1 month.
- Reviewer for or author of at least 5 substantial PRs to the codebase, with the
  definition of substantial subject to the lead's discretion (e.g.
  refactors, enhancements rather than grammar correction or one-line pulls).
- Knowledgeable about the codebase
- Sponsored by a subproject lead
  - With no objections from other leads
  - Done through PR to update the OWNERS file
- May either self-nominate, be nominated by an approver in the subproject

### Responsibilities and privileges

The following apply to the part of codebase for which one would be a reviewer in
an `OWNERS` file.

- Respond to new PRs and Issues by asking clarifying questions
- Organize the backlog by applying labels, milestones, assignees, and projects
- Code reviewer status may be a precondition to accepting large code contributions
- Responsible for project quality control via code reviews
  - Focus on code quality and correctness, including testing and factoring
  - May also review for more holistic issues, but not a requirement
- Expected to be responsive to review requests
- Assigned PRs to review related to subproject of expertise
- Assigned test bugs related to subproject of expertise



## Approver

Code approvers are able to both review and approve code contributions as well as 
help subproject leads triage issues and with project management.

While code review is focused on code quality and correctness, approval is focused on
holistic acceptance of a contribution including: backwards / forwards
compatibility, adhering to API and flag conventions, subtle performance and
correctness issues, interactions with other parts of the system, etc.

**Defined by:** *approvers* entry in an OWNERS file in a repo owned by the
Argoproj project.

Approver status is scoped to a part of the codebase.

### Requirements

The following apply to the part of codebase for which one would be an approver
in an `OWNERS` file.

- Reviewer for at least 3 months
- Reviewer for or author of at least 10 substantial PRs to the codebase, with the
  definition of substantial subject to the lead's discretion (e.g.
  refactors, enhancements rather than grammar correction or one-line pulls).
- Sponsored by a subproject lead
  - With no objections from other leads
  - Done through PR to update the OWNERS file

### Responsibilities and privileges

The following apply to the part of codebase for which one would be an approver
in an `OWNERS` file.

- Approver status may be a precondition to accepting large code contributions
- Demonstrate sound technical judgement
- Responsible for project quality control via code reviews
  - Focus on holistic acceptance of contribution such as dependencies with other features, backwards / forwards
    compatibility, API and flag definitions, etc
- Expected to be responsive to review requests (inactivity may result in suspension until active again)
- Mentor contributors and reviewers
- May approve and merge code contributions for acceptance



## Lead

Subproject Leads are the technical authority for a subproject in the Argo
project.  They *MUST* have demonstrated both good judgement and responsibility
towards the health of that subproject.  Subproject leads *MUST* set technical
direction and make or approve design decisions for their subproject - either
directly or through delegation of these responsibilities.

**Defined by:** *owners* entry in subproject `OWNERS` files

### Requirements

The process for becoming an subproject lead should be defined in the SIG
charter of the SIG owning the subproject.  Unlike the roles outlined above, the
Leads of a subproject are typically limited to a relatively small group of
decision makers and updated as fits the needs of the subproject.

The following apply to the subproject for which one would be an lead.

- Deep understanding of the technical goals and direction of the subproject
- Deep understanding of the technical domain of the subproject
- Sustained contributions to design and direction by doing all of:
  - Authoring and reviewing proposals
  - Initiating, contributing and resolving discussions (emails, GitHub issues, meetings)
  - Identifying subtle or complex issues in designs and implementation PRs
- Directly contributed to the subproject through code and reviews, including contributions demonstrating strong technical understanding and implementation complexity.

### Responsibilities and privileges

The following apply to the subproject for which one would be an lead.

- Make and approve technical design decisions for the subproject.
- Set technical direction and priorities for the subproject.
- Define milestones and releases.
  - Decides on when PRs are merged to control the release scope.
- Mentor and guide approvers, reviewers, and contributors to the subproject.
- Escalate reviewer and maintainer concerns (i.e. responsiveness, availability, and general contributor community health) to the maintainers group. 
- Ensure continued health of subproject
  - Adequate test coverage to confidently release
  - Tests are passing reliably (i.e. not flaky) and are fixed when they fail
- Ensure a healthy process for discussion and decision making is in place.
- Work with other subproject leads to maintain the project's overall health and success holistically
- Promote and foster the community (e.g. hosting meetings, workshops, partner engagements, collaborations)



## Inactive members

_Members are continuously active contributors in the community._

A core principle in maintaining a healthy community is encouraging active
participation. It is inevitable that people's focuses will change over time and
they are not expected to be actively contributing forever.

However, being a member of one of the Argoproj GitHub organizations comes with
an [elevated set of permissions]. These capabilities should not be used by those
that are not familiar with the current state of the Argo project.

Therefore members with an extended period away from the project with no activity
will be removed from the Argoproj Github Organizations and will be required to
go through the org membership process again after re-familiarizing themselves
with the current state.


### How inactivity is measured

Inactive members are defined as members of one of the Argoproj Organizations
with no significant contributions within the last 12 months. Contributions are
measured using the CNCF [DevStats project], GitHub activity history, and other media
by which a history of contributions can be reliably determined.

If an actively contributing member is accidentally removed this way, they may open an
issue to quickly be re-instated.

After an extended period away from the project with no activity,
removed members would need to re-familiarize themselves with the current state
before being able to contribute effectively.


## Change in membership roles

A change in membership role may be approved by consensus of the Argo Project leads and approvers. By convention, role changes are discussed in a meeting with Argo Project approvers before being finalized. Role changes are generally reviewed on a quarterly basis.


## Appointment of Subproject Leads

Leads serve a unique and critical role in the direction and organization of each subproject. Each subproject will generally have two co-leads, who share responsibility. There is no fixed term for leads and they often serve until they retire or, in rare cases, are replaced by [voting](GOVERNANCE.md). Leads are encouraged to give other qualified members of the community an opportunity to serve. Former leads are welcome to nominate themselves again in the future.

When a new lead needs to be chosen for a subproject, the availability of the role must be announced in advance to the Argo maintainer community. Any qualified maintainer may nominate themselves for the role. The final decision for the appointment of a new lead will be made by consensus of existing Argo Project leads and approvers.

The announcement should be posted in the #argo-maintainers Slack channel by an existing lead. The announcement should follow this model:

```
Argoproj leadership is considering adding a lead for the <project> subproject. If you would like to nominate yourself or 
someone else, please open an issue in this repo: https://github.com/argoproj/argoproj/issues

If you have any feedback about the current nominee(s), please comment on the issue nominating them.
```

This announcement should be posted at least two weeks before any vote is held to actually appoint a new lead.

Key factors in the selection of new subproject leads are:
- History of participation and leadership in the Argo project and user communities.
- Demonstrated high standards for personal and professional conduct.
- Leads should reflect and represent the diversity of the Argo Community 
- Sustained technical contributions to the subproject including demonstrating strong technical understanding and implementation complexity.

## Argoproj Ecosystem

There are related [Argoproj GitHub organizations], such as [argoproj-labs].
If you are a Argoproj org member, you are implicitly eligible
for membership in related orgs, and can request membership when it becomes
relevant, by creating a PR directly or [opening an issue][membership request]
against the argoproj/argoproj repo, as above.

However, if you are a member of any of the related
[Argoproj GitHub organizations] but not of the [Argoproj org],
you will need explicit sponsorship for your membership request.

### Actively used GitHub Organizations

| Name | Description |
| :--: | :---------: |
| [argoproj](https://github.com/argoproj) | Core Argo Projects and supporting projects |
| [argoproj-labs](https://github.com/argoproj-labs) | Experimental and ecosystem projects |


[Argoproj GitHub organizations]: #actively-used-github-organizations
[Argoproj org]: https://github.com/argoproj
[argoproj-labs]: https://github.com/argoproj-labs
[membership request]: https://github.com/argoproj/argoproj/issues/new?template=membership.md&title=REQUEST%3A%20New%20membership%20for%20%3Cyour-GH-handle%3E
[membership template]: https://github.com/argoproj/argoproj/blob/master/.github/ISSUE_TEMPLATE/membership.md
[two-factor authentication]: https://help.github.com/articles/about-two-factor-authentication
[elevated set of permissions]: #Responsibilities-and-privileges
[Devstats project]: https://argo.devstats.cncf.io/
