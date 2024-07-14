# List Data Type

The `list` data type represents an ordered sequence of values, all of which must be of the same type.

## Syntax

```hcl
variable "example_list" {
  type = list(string)
  default = ["apple", "banana", "cherry"]
}
```

## Example

```hcl
variable "regions" {
  type = list(string)
  default = ["us-east-1", "us-west-2"]
}

output "available_regions" {
  value = var.regions
}
```

## Explanation

- `type = list(string)` specifies a list of strings.
- `default` sets the list to `["us-east-1", "us-west-2"]`.

The output will be:

```hcl
available_regions = [
  "us-east-1",
  "us-west-2",
]
```
```