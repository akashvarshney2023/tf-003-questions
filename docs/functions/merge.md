# Terraform `merge` 

The `merge` function in Terraform is used to combine two or more maps into a single map. This function is particularly useful when you need to consolidate configuration data from multiple sources into a single map for use in your Terraform configurations.

## Table of Contents
- [Introduction](#introduction)
- [Syntax](#syntax)
- [Parameters](#parameters)
- [Return Value](#return-value)
- [Basic Example](#basic-example)
- [Handling Key Conflicts](#handling-key-conflicts)
- [Practical Use Case](#practical-use-case)
- [Conclusion](#conclusion)

## Introduction
Terraform is an Infrastructure as Code (IaC) tool that allows you to define and manage infrastructure resources using configuration files. When working with maps (key-value pairs), you might find situations where you need to combine multiple maps into one. The `merge` function helps you achieve this.

## Syntax
The `merge` function has the following syntax:

```hcl
merge(map1, map2, ...)
```

## Parameters
- `map1`, `map2`, ...: Two or more maps to be merged.

## Return Value
- The `merge` function returns a single map containing all key-value pairs from the input maps.

## Basic Example

Let's start with a basic example to illustrate the use of the `merge` function.

### Input Maps
Consider you have two maps:

```hcl
variable "map1" {
  default = {
    "key1" = "value1"
    "key2" = "value2"
  }
}

variable "map2" {
  default = {
    "key3" = "value3"
    "key4" = "value4"
  }
}
```

### Merging the Maps
To merge these maps into a single map, you can use the `merge` function:

```hcl
output "merged_map" {
  value = merge(var.map1, var.map2)
}
```

### Output
When you apply this configuration, the output will be:

```hcl
merged_map = {
  "key1" = "value1"
  "key2" = "value2"
  "key3" = "value3"
  "key4" = "value4"
}
```

## Handling Key Conflicts
When merging maps, key conflicts can occur if the same key exists in more than one map. In such cases, the value from the last map in the argument list will be used.

### Example with Key Conflicts
Consider the following maps:

```hcl
variable "map1" {
  default = {
    "key1" = "value1"
    "key2" = "value2"
  }
}

variable "map2" {
  default = {
    "key2" = "new_value2"
    "key3" = "value3"
  }
}
```

### Merging the Maps with Key Conflicts
Using the `merge` function:

```hcl
output "merged_map_with_conflict" {
  value = merge(var.map1, var.map2)
}
```

### Output
The output will be:

```hcl
merged_map_with_conflict = {
  "key1" = "value1"
  "key2" = "new_value2"
  "key3" = "value3"
}
```
In this case, `key2` from `map2` overrides the `key2` from `map1`.

## Practical Use Case

### Merging Environment Variables
Suppose you have a base set of environment variables and environment-specific overrides:

#### Base Variables
```hcl
variable "base_env_vars" {
  default = {
    "ENV"   = "production"
    "DEBUG" = "false"
  }
}
```

#### Environment-Specific Overrides
```hcl
variable "dev_env_vars" {
  default = {
    "ENV"   = "development"
    "DEBUG" = "true"
  }
}
```

### Merging the Environment Variables
You can merge the base and environment-specific variables to get the final set of environment variables:

```hcl
output "final_env_vars" {
  value = merge(var.base_env_vars, var.dev_env_vars)
}
```

### Output
The `final_env_vars` output will be:

```hcl
final_env_vars = {
  "ENV"   = "development"
  "DEBUG" = "true"
}
```
In this case, the environment-specific variables override the base variables.

## Conclusion
The `merge` function in Terraform is a powerful tool for combining multiple maps into a single map. This is particularly useful for consolidating configuration data and making it easier to manage in your Terraform configurations. By understanding and utilizing the `merge` function, you can write more efficient and maintainable Terraform code.
