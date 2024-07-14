# Set Data Type

The `set` data type represents an unordered collection of unique values.

## Syntax

```hcl
variable "example_set" {
  type = set(string)
  default = ["value1", "value2", "value1"]
}
```

## Example

```hcl
variable "unique_regions" {
  type = set(string)
  default = ["us-east-1", "us-west-2", "us-east-1"]
}

output "unique_available_regions" {
  value = var.unique_regions
}
```

## Explanation

- `type = set(string)` specifies a set of strings.
- `default` sets the set with unique values, with duplicates removed.

The output will be:

```hcl
unique_available_regions = [
  "us-east-1",
  "us-west-2",
]
```