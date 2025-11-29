# Authenticating with Terraform Cloud

## Which command is used to interactively obtain an API token for Terraform Cloud/Enterprise?

- [ ] `terraform auth`
- [x] `terraform login`
- [ ] `terraform init -login`
- [ ] `terraform cloud login`

### Answer Explanation

- **`terraform login`**: This is the correct command. It initiates an interactive flow (usually opening a web browser) to authenticate with Terraform Cloud or Terraform Enterprise and obtain an API token, which is then stored locally in the credentials file.

- **`terraform auth`**, **`terraform cloud login`**: These are not valid Terraform commands.
- **`terraform init`**: This command initializes the working directory but does not handle interactive user authentication for Terraform Cloud.

### Summary

The command **`terraform login`** is used to authenticate with Terraform Cloud/Enterprise.
