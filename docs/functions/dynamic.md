
# Terraform `dynamic`

## Introduction

The `dynamic` block in Terraform is used to construct repeatable nested blocks within a resource or module configuration dynamically. This feature is useful when you need to generate multiple nested blocks based on a variable or condition. It allows you to avoid repetitive code and manage complex configurations more effectively.

## Syntax

```hcl
dynamic "block_type" {
  for_each = list_or_map
  content {
    # Configuration for the nested block
  }
}
```

### Parameters

- **`block_type`**: The type of nested block to be created (e.g., `tags`, `ingress`, etc.).
- **`for_each`**: A list or map that specifies the number of nested blocks to create. Each element of the list or map will generate a separate block.
- **`content`**: The configuration for the nested block. This can include any attributes that are normally valid within that block type.

## Example Usage

Here are some examples to illustrate how the `dynamic` block can be used in different scenarios.

### Basic Example

Suppose you want to dynamically create multiple `tags` for an AWS EC2 instance based on a list.

```hcl
variable "tags" {
  type = list(map(string))
  default = [
    {
      key   = "Environment"
      value = "Production"
    },
    {
      key   = "Application"
      value = "MyApp"
    }
  ]
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  dynamic "tags" {
    for_each = var.tags
    content {
      key   = tags.value["key"]
      value = tags.value["value"]
    }
  }
}
```

In this example, the `dynamic "tags"` block creates multiple `tags` nested blocks based on the `tags` variable. Each tag is configured with a key and value as specified in the variable.

### Conditional Blocks

You can also use the `dynamic` block to create nested blocks conditionally.

```hcl
variable "enable_feature" {
  type    = bool
  default = true
}

resource "aws_security_group" "example" {
  name = "example-sg"

  dynamic "ingress" {
    for_each = var.enable_feature ? [1] : []
    content {
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

In this example, the `dynamic "ingress"` block is only created if `var.enable_feature` is `true`. If the variable is `false`, no `ingress` blocks are created.

### Using Maps

You can use maps to dynamically generate complex nested configurations.

```hcl
variable "network_configs" {
  type = map(object({
    cidr_block = string
    name       = string
  }))
  default = {
    "subnet1" = {
      cidr_block = "10.0.1.0/24"
      name       = "Subnet 1"
    },
    "subnet2" = {
      cidr_block = "10.0.2.0/24"
      name       = "Subnet 2"
    }
  }
}

resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"

  dynamic "subnet" {
    for_each = var.network_configs
    content {
      cidr_block = subnet.value.cidr_block
      tags = {
        Name = subnet.value.name
      }
    }
  }
}
```

In this example, the `dynamic "subnet"` block creates multiple `subnet` blocks based on the `network_configs` map. Each subnet is configured with a CIDR block and a tag.

## Common Use Cases

- **Dynamic Tagging**: Create multiple tags or other nested blocks based on a variable list.
- **Conditional Blocks**: Include or exclude blocks based on conditions or variable values.
- **Complex Configurations**: Generate complex nested structures dynamically without repeating code.

## Summary

The `dynamic` block in Terraform allows you to generate nested blocks dynamically based on variables or conditions. This feature helps in managing complex configurations more effectively and avoiding repetitive code. By using the `dynamic` block, you can create flexible and maintainable Terraform configurations.

For more information, refer to the [official Terraform documentation](https://www.terraform.io/docs/configuration/blocks.html#dynamic-blocks).
