# Any Data Type

The `any` data type represents a value of any type. It provides the most flexibility but lacks type safety.

## Syntax

```hcl
variable "example_any" {
  type = any
  default = "Any type is allowed"
}
```

## Example

```hcl
variable "flexible_variable" {
  type = any
  default = {
    key = "value"
  }
}

output "any_value" {
  value = var.flexible_variable
}
```

## Explanation

- `type = any` allows for any data type.
- `default` sets the variable to a map with one key-value pair.

The output will be:

```hcl
any_value = {
  "key" = "value"
}
```