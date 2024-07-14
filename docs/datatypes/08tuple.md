#  Tuple Data Type

The `tuple` data type represents an ordered sequence of elements, where each element can have a different type.

## Syntax

```hcl
variable "example_tuple" {
  type = tuple([string, number, bool])
  default = ["example", 1, true]
}
```

## Example

```hcl
variable "server_info" {
  type = tuple([string, number, bool])
  default = ["server1", 8080, true]
}

output "info" {
  value = var.server_info
}
```

## Explanation

- `type = tuple([string, number, bool])` specifies a tuple with a string, number, and boolean.
- `default` sets the tuple with initial values.

The output will be:

```hcl
info = [
  "server1",
  8080,
  true,
]
```