# Number Data Type

The `number` data type represents numeric values, both integers and floating-point numbers.

## Syntax

```hcl
variable "example_number" {
  type = number
  default = 42
}
```

## Example

```hcl
variable "instance_count" {
  type = number
  default = 3
}

output "number_of_instances" {
  value = var.instance_count
}
```

## Explanation

- `type = number` ensures the variable must be a number.
- `default` sets a default value of `3` for `instance_count`.

The output will be:

```hcl
number_of_instances = 3
```
```