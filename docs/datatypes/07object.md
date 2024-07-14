# Object Data Type

The `object` data type represents a complex type that can contain multiple named attributes.

## Syntax

```hcl
variable "example_object" {
  type = object({
    name    = string
    age     = number
    enabled = bool
  })
  default = {
    name    = "John Doe"
    age     = 30
    enabled = true
  }
}
```

## Example

```hcl
variable "server_config" {
  type = object({
    hostname = string
    port     = number
    ssl      = bool
  })
  default = {
    hostname = "example.com"
    port     = 443
    ssl      = true
  }
}

output "server_details" {
  value = var.server_config
}
```

## Explanation

- `type = object({...})` defines an object with specific attributes.
- `default` sets the object with values for each attribute.

The output will be:

```hcl
server_details = {
  "hostname" = "example.com"
  "port"     = 443
  "ssl"      = true
}
```