# Terraform `alltrue()` Function Tutorial

## Introduction

The `alltrue()` function in Terraform is used to evaluate whether all elements in a given list of Boolean values are `true`. It is useful for ensuring that all conditions or checks in your Terraform configuration are satisfied.

## Syntax

```hcl
alltrue(list)
```

### Parameters

- **`list`**: A list of Boolean values (`true` or `false`) that you want to evaluate.

### Returns

- **`bool`**: Returns `true` if all elements in the list are `true`. Otherwise, it returns `false`.

## Example Usage

Here are some examples to illustrate how the `alltrue()` function can be used in different scenarios.

### Basic Example

Suppose you have a list of Boolean values and you want to check if all of them are `true`.

```hcl
locals {
  boolean_list = [true, true, true]
}

output "all_true" {
  value = alltrue(local.boolean_list)
}
```

In this example, the output will be `true` since all values in `local.boolean_list` are `true`.

### Using `alltrue()` with Conditions

You can use the `alltrue()` function to evaluate a list of conditions.

```hcl
variable "condition1" {
  type    = bool
  default = true
}

variable "condition2" {
  type    = bool
  default = false
}

locals {
  conditions = [var.condition1, var.condition2]
}

output "all_conditions_true" {
  value = alltrue(local.conditions)
}
```

In this example, the output will be `false` because `var.condition2` is `false`, making not all elements in `local.conditions` `true`.

### Using `alltrue()` in Conditional Logic

You can use `alltrue()` to control resource creation or configuration based on multiple Boolean conditions.

```hcl
locals {
  check1 = true
  check2 = true
  check3 = false
}

resource "example_resource" "example" {
  count = alltrue([local.check1, local.check2, local.check3]) ? 1 : 0
}
```

In this example, the resource `example_resource` will only be created if all checks in the list are `true`. Since `local.check3` is `false`, the resource will not be created.

## Common Use Cases

- **Validation**: Ensure that multiple conditions or checks are met before proceeding with resource creation or configuration.
- **Conditional Resource Creation**: Control the creation of resources based on the evaluation of multiple Boolean values.

## Summary

The `alltrue()` function in Terraform is a useful tool for evaluating whether all elements in a list of Boolean values are `true`. It helps in making decisions based on multiple conditions and can be used in various scenarios to enforce requirements in your Terraform configurations.

For more information, refer to the [official Terraform documentation](https://registry.terraform.io/providers/hashicorp/null/latest/docs/functions/alltrue).
