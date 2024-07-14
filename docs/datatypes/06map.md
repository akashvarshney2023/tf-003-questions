#  Map Data Type

The `map` data type represents a collection of key-value pairs where keys are strings and values can be any type.

## Syntax

```hcl
variable "example_map" {
  type = map(string)
  default = {
    "key1" = "value1"
    "key2" = "value2"
  }
}
```

## Example

```hcl
variable "instance_tags" {
  type = map(string)
  default = {
    "Name" = "MyInstance"
    "Environment" = "Production"
  }
}

output "tags" {
  value = var.instance_tags
}
```

## Explanation

- `type = map(string)` specifies a map where all values are strings.
- `default` sets the map with two key-value pairs.

The output will be:

```hcl
tags = {
  "Name" = "MyInstance"
  "Environment" = "Production"
}
```
