# Iterating Over Subnet CIDR Blocks in Terraform

## **You want to deploy multiple subnets within a VPC in AWS and are looking for a for loop-like expression to iterate over a list of subnet CIDR blocks. Which feature of Terraform configuration can you use?**

- [ ] **terraform import**
- [ ] **dynamic blocks**
- [ ] **splat expression**
- [x] **dynamic blocks**

### Answer Explanation

- **terraform import:** This command is used to import existing resources into Terraform management. It does not support looping or iterating over lists.

- **dynamic blocks:** This feature in Terraform allows you to create repeating blocks within a resource or module dynamically based on a list or map. It's ideal for iterating over a list of subnet CIDR blocks to create multiple subnets.

- **splat expression:** Splat expressions are used to access multiple attributes from a list or map but are not used for creating or iterating over resource blocks.

- **dynamic backend:** This refers to configuring different backends dynamically based on variables or other conditions. It does not pertain to iterating over lists or creating multiple resources.

### Summary

**Dynamic blocks** are the correct feature to use when you need to iterate over a list of subnet CIDR blocks to deploy multiple subnets within a VPC in AWS. They provide a way to dynamically generate multiple blocks of configuration based on input data.
