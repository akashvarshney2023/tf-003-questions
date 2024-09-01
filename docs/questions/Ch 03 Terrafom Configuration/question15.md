# Understanding Terraform Dependency Lock File

## **Terraform remembers the compatible version of dependencies such as providers and modules through a dependency lock file. What is the name of that file?**

- [x] **.terraform.lock.hcl**
- [ ] **.terraform.lock.tf**
- [ ] **.dependency.lock.hcl**
- [ ] **.dependency.lock.tf**

### Answer Explanation

- **.terraform.lock.hcl:** This is the correct file name for the dependency lock file in Terraform. It records the exact versions of providers and modules used in your Terraform configuration to ensure consistent and repeatable infrastructure deployments.

- **.terraform.lock.tf:** This file name is incorrect. Terraform does not use `.tf` extensions for lock files.

- **.dependency.lock.hcl:** This is not the correct file name. Terraform uses `.terraform.lock.hcl` for locking dependencies.

- **.dependency.lock.tf:** This file name is also incorrect. The correct extension for the dependency lock file is `.hcl`.

### Summary

The correct name of the file used by Terraform to lock dependency versions is **`.terraform.lock.hcl`**.
