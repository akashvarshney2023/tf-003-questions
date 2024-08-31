#  Version Control System (VCS) in Terraform Cloud

## Which of the following is not a correct statement about version control system (VCS) in Terraform Cloud?

- [ ] Terraform Cloud can automatically initiate Terraform runs when changes are committed to the specified branch in VCS.
- [ ] Terraform Cloud makes code review easier by automatically predicting how pull requests will affect infrastructure.
- [ ] GitHub and Bitbucket VCS providers are supported by Terraform Cloud.
- [ ] One VCS provider can be configured at a time in Terraform Cloud.

### Answer Explanation

- **Terraform Cloud can automatically initiate Terraform runs when changes are committed to the specified branch in VCS:** This statement is correct. Terraform Cloud integrates with VCS providers to trigger runs automatically when code changes are detected.

- **Terraform Cloud makes code review easier by automatically predicting how pull requests will affect infrastructure:** This statement is **not correct**. Terraform Cloud does not predict the effects of pull requests on infrastructure. It can trigger Terraform runs based on commits but does not analyze or predict changes in the pull request phase.

- **GitHub and Bitbucket VCS providers are supported by Terraform Cloud:** This statement is correct. Terraform Cloud supports both GitHub and Bitbucket for version control integration.

- **One VCS provider can be configured at a time in Terraform Cloud:** This statement is correct. Terraform Cloud supports configuring a single VCS provider per workspace.

### Summary

The incorrect statement about VCS in Terraform Cloud is that **Terraform Cloud makes code review easier by automatically predicting how pull requests will affect infrastructure.** This feature is not currently supported by Terraform Cloud.
