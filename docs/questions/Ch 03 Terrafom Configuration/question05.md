# Terraform Workflow for Deploying New Infrastructure

## **What is the workflow for deploying new infrastructure with Terraform?**

- [ ] **terraform plan to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure.**
- [ ] **Write a Terraform configuration, run terraform show to view proposed changes, and terraform apply to create new infrastructure.**
- [ ] **terraform import to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure.**
- [x] **Write a Terraform configuration, run terraform init, run terraform plan to view planned infrastructure changes, and terraform apply to create new infrastructure.**

### Answer Explanation

- **terraform plan to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure:** This option is incorrect because `terraform plan` does not import infrastructure but instead previews changes to the infrastructure based on the current state and configuration.

- **Write a Terraform configuration, run terraform show to view proposed changes, and terraform apply to create new infrastructure:** This option is incorrect because `terraform show` is used to show the state or plan in detail, but it is not the primary command for viewing proposed changes.

- **terraform import to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure:** This option is incorrect because `terraform import` is used to import existing resources into the state file, not as part of the standard workflow for creating new infrastructure.

- **Write a Terraform configuration, run terraform init, run terraform plan to view planned infrastructure changes, and terraform apply to create new infrastructure:** This is the correct answer. The standard workflow involves:
  - Writing the Terraform configuration.
  - Running `terraform init` to initialize the working directory containing Terraform configuration files.
  - Running `terraform plan` to preview the changes that will be made.
  - Running `terraform apply` to execute the changes and create the new infrastructure.

### Summary

The correct workflow for deploying new infrastructure with Terraform is to **write a Terraform configuration, run `terraform init`, run `terraform plan` to view planned infrastructure changes, and `terraform apply` to create new infrastructure**.
