Welcome to Argo Project Onboarding!

Before submitting the ticket please ensure you understand which [projects](../../community/ecosystem-projects.md) could be added to the Argo community and what the open decision-making process looks like.

Once you are ready, please help the reviewer understand your project better by
answering the following questions in your onboarding proposal:

- [x] What is your project repository Github URL? - **https://github.com/ibm/argocd-interlace**
- [x] Do you wish to host your project repository https://github.com/argoproj-labs or https://github.com/argoproj? - **https://github.com/argoproj-labs**
- [x] Does your project focus on enhancing or providing additional features to one of the existing [core
 projects](https://github.com/argoproj/argoproj#what-is-argoproj) ? If yes, which of the core projects is your proposed project related to? - **https://github.com/argoproj/argo-cd**
   - ArgoCD Interlace focuses on enhancing ArgoCD capability from end-to-end software supply chain security viewpoint. It is specifically tailored towards securing ArgoCD GitOps ( i.e., ArgoCD internally builds manifest from source data in Git repository, and auto-sync it with target clusters.). Interlace achieve this by a)  GitOps Source material verification (content signature, commit sign off, etc.), b) Signing manifest generated from ArgoCD, c) producing verifiable transparent evidence records regarding manifest generation (such as the source files for the build, the command to produce the manifest for reproducibility). Interlace is still a pluggable component which does not interfere with existing ArgoCD GitOps.
   - ArgoCD Interlace was presented in the Argo Contributor Experience Office Hour (Dec 09, Dec 12/2021) 
- [ ] Is it endorsed by any of the Argo subproject maintainers? Please mention sponsors from the subproject. - **We seek to invite Argo Community subproject maintainers to endorse this project.**
- [x] How does it align with the goals of the Argo community? - **The goal of the Argo community is to make it easy to use Kubernetes for getting useful work done. ArgoCD Interlace supports this mission by creating new opportunity to enable securing applications deployed via ArgoCD GitOps from end-to-end software supply chain security viewpoint.**
- [x] Who will maintain the project going forward? - **@gajananan and @yuji-watanabe-jp  and the Argo community**
- [x] What is your project license? - **Apache-2.0 License**
