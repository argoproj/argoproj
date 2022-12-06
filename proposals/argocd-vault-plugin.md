Welcome to Argo Project Onboarding!

Before submitting the ticket please ensure you understand which [projects](../../community/ecosystem-projects.md) could be added to the Argo community and what the open decision-making process looks like.

Once you are ready, please help the reviewer understand your project better by
answering the following questions in your onboarding proposal:

- [x] What is your project repository Github URL? - **https://github.com/IBM/argocd-vault-plugin**
- [x] Do you wish to host your project repository https://github.com/argoproj-labs or https://github.com/argoproj? - **https://github.com/argoproj-labs**
- [x] Does your project focus on enhancing or providing additional features to one of the existing [core
 projects](https://github.com/argoproj/argoproj#what-is-argoproj) ? If yes, which of the core projects is your proposed project related to? - **https://github.com/argoproj/argo-cd**
- [x] Is it endorsed by any of the Argo subproject maintainers? Please mention sponsors from the subproject. - **@sbose78**
- [x] How does it align with the goals of the Argo community? - **argocd-vault-plugin adds an unofficial secret management plugin that can be used in tandem with Argo CD or could be used independently as part of an Argo Workflow.**

  #### For Example

  By loading argocd-vault-plugin as as custom plugin..
  ```
  data:
    configManagementPlugins: |-
      - name: argocd-vault-plugin
        generate:
          command: ["argocd-vault-plugin"]
          args: ["generate", "./"]
  ```
  and then specifiying that plugin in your Argo CD Application..
  ```
  apiVersion: argoproj.io/v1alpha1
  kind: Application
  metadata:
    name: your-application-name
  spec:
    destination:
      name: ''
      namespace: default
      server: 'https://kubernetes.default.svc'
    source:
      path: .
      plugin:
        name: argocd-vault-plugin
      repoURL: http://your-repo/
      targetRevision: HEAD
    project: default
  ```
  you are able to check in a file to Git that looks like this..
  ```
  kind: Secret
  apiVersion: v1
  metadata:
    name: example-secret
    annotations:
      avp.kubernetes.io/path: "path/to/secret"
  type: Opaque
  data:
    password: <password-vault-key>
  ```
  You set the `path` to your secret in Vault or other secret management tool. And then when Argo CD syncs, it will pull that value and inject into the placeholder `<password-vault-key>`. With the result being..
  ```
  kind: Secret
  apiVersion: v1
  metadata:
    name: example-secret
    annotations:
      avp.kubernetes.io/path: "path/to/secret"
  type: Opaque
  data:
    password: my-password # value that was injected
  ```
- [x] Who will maintain the project going forward? - **@werne2j and @jkayani**
- [x] What is your project license? - **Apache-2.0 License**
