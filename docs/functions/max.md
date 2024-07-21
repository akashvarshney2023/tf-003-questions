# Terraform `max()`

## Introduction

The `max()` function in Terraform is used to find the maximum value from a given set of numbers. This function is useful when you need to determine the highest value among a list of numbers in your Terraform configurations.

## Syntax

```hcl
max(number1, number2, ...)
```

### Parameters

- **`number1, number2, ...`**: A series of numbers (either integers or floating-point) among which the maximum value is to be determined.

### Returns

- **`number`**: The highest value from the provided numbers.

## Example Usage

Here are some examples to illustrate how the `max()` function can be used in different scenarios.

### Basic Example

Suppose you want to find the maximum value between 10, 20, and 30.

```hcl
output "max_value" {
  value = max(10, 20, 30)
}
```

In this example, the output will be `30` as it is the highest value among the provided numbers.

### Using `max()` with Variables

You can also use the `max()` function with variables to make your configuration more dynamic.

```hcl
variable "number1" {
  type    = number
  default = 15
}

variable "number2" {
  type    = number
  default = 25
}

output "max_value" {
  value = max(var.number1, var.number2)
}
```

In this example, the output will be `25`, which is the maximum value between `var.number1` and `var.number2`.

### Using `max()` with Expressions

You can use the `max()` function with expressions that return numerical values. For instance:

```hcl
locals {
  values = [5, 15, 25, 35]
}

output "max_value" {
  value = max(local.values...)
}
```

Here, `local.values...` uses the splat operator to pass the list of values to the `max()` function. The output will be `35`, the maximum value in the list.

## Common Use Cases

- **Determining the maximum capacity**: Use `max()` to ensure that the resource is allocated the highest required capacity among various conditions.
- **Setting limits**: Find the maximum value to set appropriate limits or constraints in your Terraform configurations.

## Summary

The `max()` function in Terraform is a straightforward but powerful tool for finding the maximum value among a set of numbers. Whether used directly with literals, variables, or expressions, it helps in making dynamic and efficient infrastructure configurations.

For more information, refer to the [official Terraform documentation](https://registry.terraform.io/providers/hashicorp/null/latest/docs/functions/max).
