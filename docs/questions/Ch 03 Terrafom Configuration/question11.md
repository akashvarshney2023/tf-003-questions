# Terraform Files to Exclude from Git Commits

## **Which Terraform files should be excluded from Git commit by adding them in `.gitignore` file? (select two)**

- [ ] **output.tf**
- [x] **terraform.tfstate**
- [x] **terraform.tfvars**
- [ ] **variables.tf**

### Answer Explanation

- **terraform.tfstate:** This file contains the current state of your infrastructure and is crucial for Terraform to manage your resources. It includes sensitive information and should not be committed to version control.

- **terraform.tfvars:** This file is used to pass variables to your Terraform configuration, often containing sensitive data such as passwords or API keys. It should be excluded from version control to avoid exposing sensitive information.

- **output.tf:** This file defines the outputs of your Terraform configuration. It generally contains non-sensitive information and can be safely committed to version control.

- **variables.tf:** This file defines input variables for your Terraform configuration. It usually contains non-sensitive, configurable data and can be safely committed to version control.

### Summary

Files such as `terraform.tfstate` and `terraform.tfvars` should be excluded from Git commits by adding them to the `.gitignore` file to protect sensitive information and maintain security.
