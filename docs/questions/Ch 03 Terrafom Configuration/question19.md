# Variable Definition Precedence

## If a variable is defined in multiple places, which of the following has the highest precedence?

- [ ] `terraform.tfvars` file
- [ ] Environment variable `TF_VAR_name`
- [x] `-var` or `-var-file` command line argument
- [ ] Default value in configuration

### Answer Explanation

Terraform loads variables from multiple sources, and they are processed in a specific order of precedence. The order from highest to lowest is:

1.  **Command-line flags**: Arguments passed via `-var` or `-var-file` have the highest precedence.
2.  **`*.auto.tfvars` or `*.auto.tfvars.json`**: Files ending in `.auto.tfvars` or `.auto.tfvars.json`.
3.  **`terraform.tfvars` or `terraform.tfvars.json`**: The default variable definitions file.
4.  **Environment variables**: Variables starting with `TF_VAR_`.
5.  **Default values**: The default value defined in the variable block in the configuration.

Therefore, the **`-var` or `-var-file` command line argument** overrides all other sources.

### Summary

The **`-var` or `-var-file` command line argument** has the highest precedence when defining variables in Terraform.
