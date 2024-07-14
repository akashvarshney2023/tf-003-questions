# Boolean Data Type

The `bool` data type represents a boolean value, either `true` or `false`.

## Syntax

```hcl
variable "example_bool" {
  type = bool
  default = true
}
```

## Example

```hcl
variable "enable_feature" {
  type = bool
  default = false
}

output "feature_status" {
  value = var.enable_feature
}
```

## Explanation

- `type = bool` enforces that the variable is a boolean.
- `default` assigns `false` to `enable_feature`.

The output will be:

```hcl
feature_status = false
```
```