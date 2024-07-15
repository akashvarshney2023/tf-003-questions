# Terraform `zipmap` 

The `zipmap` function in Terraform is used to create a map from two lists, where one list provides keys and the other provides values. This function is particularly useful when you need to dynamically generate maps based on lists of data.

## Table of Contents
- [Introduction](#introduction)
- [Syntax](#syntax)
- [Parameters](#parameters)
- [Return Value](#return-value)
- [Basic Example](#basic-example)
- [Handling Unequal Lists](#handling-unequal-lists)
- [Practical Use Case](#practical-use-case)
- [Conclusion](#conclusion)

## Introduction
Terraform is an Infrastructure as Code (IaC) tool that allows you to define and manage infrastructure resources using configuration files. The `zipmap` function helps you construct maps by pairing corresponding elements from two lists: one for keys and one for values.

## Syntax
The `zipmap` function has the following syntax:

```hcl
zipmap(list_of_keys, list_of_values)
```

## Parameters
- `list_of_keys`: The list that provides keys for the resulting map.
- `list_of_values`: The list that provides values for the resulting map.

## Return Value
- The `zipmap` function returns a map where each element is a key-value pair from the corresponding elements of `list_of_keys` and `list_of_values`.

## Basic Example

Let's start with a basic example to illustrate the use of the `zipmap` function.

### Input Lists
Consider you have two lists:

```hcl
variable "keys_list" {
  default = ["key1", "key2", "key3"]
}

variable "values_list" {
  default = ["value1", "value2", "value3"]
}
```

### Creating a Map with `zipmap`
To create a map using `zipmap` from these lists:

```hcl
output "result_map" {
  value = zipmap(var.keys_list, var.values_list)
}
```

### Output
When you apply this configuration, the output will be:

```hcl
result_map = {
  "key1" = "value1"
  "key2" = "value2"
  "key3" = "value3"
}
```

## Handling Unequal Lists
If the input lists are of different lengths, Terraform will use elements from the shorter list until it runs out of elements. Extra elements in the longer list are ignored.

### Example with Unequal Lists
Consider the following lists:

```hcl
variable "keys_list" {
  default = ["key1", "key2"]
}

variable "values_list" {
  default = ["value1", "value2", "value3"]
}
```

### Creating a Map with `zipmap` (Unequal Lists)
Using `zipmap` with unequal lists:

```hcl
output "result_map_unequal" {
  value = zipmap(var.keys_list, var.values_list)
}
```

### Output
The output will be:

```hcl
result_map_unequal = {
  "key1" = "value1"
  "key2" = "value2"
}
```
In this case, the third element in `values_list` ("value3") is ignored because `keys_list` has only two elements.

## Practical Use Case

### Generating Resource Tags
Suppose you have a list of resource names and corresponding tags, and you want to generate a map of resource names to tags for use in your Terraform configurations:

#### Input Lists
```hcl
variable "resource_names" {
  default = ["server1", "server2", "server3"]
}

variable "resource_tags" {
  default = [
    { "Environment" = "Production", "Owner" = "Alice" },
    { "Environment" = "Development", "Owner" = "Bob" },
    { "Environment" = "Testing", "Owner" = "Charlie" },
  ]
}
```

### Creating Tags Map with `zipmap`
You can use `zipmap` to generate a map of resource names to tags:

```hcl
output "resource_tags_map" {
  value = zipmap(var.resource_names, var.resource_tags)
}
```

### Output
The `resource_tags_map` output will be:

```hcl
resource_tags_map = {
  "server1" = { "Environment" = "Production", "Owner" = "Alice" }
  "server2" = { "Environment" = "Development", "Owner" = "Bob" }
  "server3" = { "Environment" = "Testing", "Owner" = "Charlie" }
}
```

## Conclusion
The `zipmap` function in Terraform is a versatile tool for creating maps dynamically from lists of keys and values. This functionality is valuable for generating configuration data and managing infrastructure resources efficiently. By understanding and utilizing the `zipmap` function, you can enhance your Terraform configurations and streamline your Infrastructure as Code practices.
