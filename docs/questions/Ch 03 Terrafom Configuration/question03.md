
# Identifying the Type of Block in a Terraform Configuration

## **What is the type of the block in the below Terraform configuration?**

```hcl
resource "aws_instance" "example" {
  ami           = "abc123"
  instance_type = "t2.micro"
}
```

- [x] resource
- [ ] aws_instance
- [ ] t2.micro
- [ ] instance_type

### Answer Explanation

- **resource:** The block type in this Terraform configuration is `resource`. In Terraform, the `resource` block is used to define a specific piece of infrastructure. It specifies the resource type (in this case, `aws_instance`) and gives it a unique name (`example`).

- **aws_instance:** This is the type of resource being created, not the type of block.

- **t2.micro:** This is a value assigned to the `instance_type` argument within the `resource` block.

- **instance_type:** This is a property within the `resource` block and not the type of the block itself.

### Summary

The block type in the provided Terraform configuration is **resource**.
