# Terraform `flatten` 

The `flatten` function in Terraform is used to transform a list of lists into a single flat list. This can be incredibly useful when working with complex data structures, simplifying them for further processing.

## Table of Contents
- [Introduction](#introduction)
- [Syntax](#syntax)
- [Parameters](#parameters)
- [Return Value](#return-value)
- [Basic Example](#basic-example)
- [Practical Use Case](#practical-use-case)
- [Conclusion](#conclusion)

## Introduction
Terraform is an Infrastructure as Code (IaC) tool that allows you to define and manage infrastructure resources using configuration files. Sometimes, when dealing with lists of resources or other structured data, you may encounter nested lists that you need to simplify. This is where the `flatten` function comes in handy.

## Syntax
The `flatten` function has the following syntax:

```hcl
flatten(list)
```

## Parameters
- `list`: The input list that contains nested lists.

## Return Value
- The `flatten` function returns a single list with all the elements of the nested lists.

## Basic Example

Let's start with a basic example to illustrate the use of the `flatten` function.

### Input List
Consider you have a list of lists:

```hcl
variable "nested_list" {
  default = [[1, 2], [3, 4], [5, 6]]
}
```

### Flattening the List
To flatten this list into a single list, you can use the `flatten` function:

```hcl
output "flat_list" {
  value = flatten(var.nested_list)
}
```

### Output
When you apply this configuration, the output will be:

```hcl
flat_list = [1, 2, 3, 4, 5, 6]
```

## Practical Use Case

### Combining Multiple Lists
Suppose you have multiple lists representing resources in different environments, and you want to combine them into a single list for processing:

#### Input Lists
```hcl
variable "dev_servers" {
  default = ["dev1", "dev2"]
}

variable "prod_servers" {
  default = ["prod1", "prod2"]
}

variable "test_servers" {
  default = ["test1", "test2"]
}
```

#### Flattening the Lists
You can use the `flatten` function to combine these lists:

```hcl
output "all_servers" {
  value = flatten([var.dev_servers, var.prod_servers, var.test_servers])
}
```

#### Output
The `all_servers` output will be a single list containing all servers from the different environments:

```hcl
all_servers = ["dev1", "dev2", "prod1", "prod2", "test1", "test2"]
```

## Conclusion
The `flatten` function in Terraform is a powerful tool for simplifying nested lists into a single list. This is particularly useful when consolidating data and making it easier to work with in your Terraform configurations. By understanding and utilizing the `flatten` function, you can write more efficient and maintainable Terraform code.
