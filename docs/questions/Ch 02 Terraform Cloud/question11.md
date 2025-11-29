# Terraform Cloud Execution Modes

## In Terraform Cloud, which execution mode allows Terraform to run locally on your machine while storing state in Terraform Cloud?

- [ ] Remote
- [x] Local
- [ ] Agent
- [ ] Hybrid

### Answer Explanation

Terraform Cloud supports different execution modes:

- **Remote**: The default mode. Terraform runs on Terraform Cloud's infrastructure.
- **Local**: Terraform runs on your local machine (where you run `terraform plan` or `terraform apply`), but the state is stored and managed by Terraform Cloud. This is often referred to as the "cloud" backend with "local" execution.
- **Agent**: Terraform runs on isolated, private agents that you host.

- **Hybrid**: This is not a standard execution mode name in this context.

### Summary

The **Local** execution mode allows you to run Terraform operations locally while using Terraform Cloud for state management.
