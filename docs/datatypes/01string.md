
# String Data Type

The `string` data type represents a sequence of characters. It is used to store textual data.

## Syntax

```hcl
variable "example_string" {
  type = string
  default = "Hello, World!"
}

```

## Example

```hcl
variable "greeting" {
  type = string
  default = "Hello, Terraform!"
}

output "greeting_message" {
  value = var.greeting
}
```

## Explanation

- `type = string` specifies that the variable is expected to be a string.
- `default` assigns a default value of `"Hello, Terraform!"` to the variable.

When this configuration is applied, the output will be:

```hcl
greeting_message = "Hello, Terraform!"
```
