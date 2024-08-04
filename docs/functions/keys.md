# Terrafrm `keys`

The `keys` function in Terraform is a powerful tool for working with maps. This function extracts a list of keys from a given map, which can be useful for various operations, such as iteration and conditional logic.

## Syntax

```hcl
keys(map)
```

- **`map`**: The map from which the keys are to be extracted.

## Description

The `keys` function takes a map as input and returns a list of its keys. This list contains the keys in the order they were defined in the map. If the map is empty, the function returns an empty list.

## Example

Consider the following map in your Terraform configuration:

```hcl
variable "example_map" {
  type = map(string)
  default = {
    "name"     = "example"
    "type"     = "demo"
    "version"  = "1.0"
  }
}
```

You can use the `keys` function to get a list of keys from this map:

```hcl
locals {
  map_keys = keys(var.example_map)
}
```

In this case, `local.map_keys` will be:

```hcl
["name", "type", "version"]
```

## Practical Use Cases

### Iteration

You can use `keys` in combination with other functions to iterate over map keys. For example, to iterate over each key in a map:

```hcl
resource "example_resource" "example" {
  for_each = toset(keys(var.example_map))
  
  key = each.key
  value = var.example_map[each.key]
}
```

### Conditional Logic

You can use `keys` in conditional expressions to check for the presence of specific keys:

```hcl
locals {
  has_version = contains(keys(var.example_map), "version")
}

resource "example_resource" "example" {
  count = local.has_version ? 1 : 0
  
  name = var.example_map["name"]
}
```

In this example, the `example_resource` will only be created if the `"version"` key exists in `var.example_map`.

## Notes

- The `keys` function is read-only; it does not modify the map itself.
- The order of keys returned by `keys` is not guaranteed to be in any specific order.

## Conclusion

The `keys` function is an essential tool for working with maps in Terraform. It allows you to easily extract and manipulate the keys of a map, which can be especially useful for dynamic resource creation and conditional logic.

For more details, refer to the [Terraform documentation](https://www.terraform.io/docs/configuration/functions/keys.html).
