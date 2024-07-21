
# Terraform Tutorial and Exam Preparation

Welcome to the Terraform Tutorial and Exam Preparation Guide! This repository is designed to help Terraform developers and enthusiasts learn Terraform from scratch and prepare for the Terraform Associate (003) certification exam.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Terraform Basics](#terraform-basics)
  - [What is Terraform?](#what-is-terraform)
  - [Key Concepts](#key-concepts)
  - [Writing Your First Configuration](#writing-your-first-configuration)
- [Advanced Topics](#advanced-topics)
  - [State Management](#state-management)
  - [Modules](#modules)
  - [Workspaces](#workspaces)
  - [Provisioners](#provisioners)
- [Terraform Associate (003) Exam](#terraform-associate-003-exam)
  - [Exam Overview](#exam-overview)
  - [Sample Questions and Explanations](#sample-questions-and-explanations)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This guide provides comprehensive tutorials and resources for learning Terraform, an open-source infrastructure as code (IaC) tool by HashiCorp. Whether you're a beginner or an experienced user, you'll find valuable content to enhance your Terraform skills and prepare for the Terraform Associate certification exam.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Terraform](https://www.terraform.io/downloads.html)
- A code editor (e.g., Visual Studio Code)
- Basic understanding of cloud services (e.g., AWS, Azure, GCP)

### Installation

Follow these steps to install Terraform on your system:

1. Download the appropriate version for your operating system from the [official Terraform website](https://www.terraform.io/downloads.html).
2. Unzip the downloaded file and move the `terraform` binary to a directory included in your system's PATH.
3. Verify the installation by running `terraform --version` in your terminal.

## Terraform Basics

### What is Terraform?

Terraform is an open-source tool for building, changing, and versioning infrastructure safely and efficiently. It allows you to define infrastructure as code using a declarative configuration language.

### Key Concepts

- **Providers**: Plugins that interact with APIs of cloud providers and other services.
- **Resources**: The components that make up your infrastructure.
- **State**: A persistent data store to track your infrastructure's current state.
- **Plan**: A preview of what Terraform will do when you apply the configuration.
- **Apply**: The process of executing the changes required to reach the desired state.

### Writing Your First Configuration

1. Create a new directory for your Terraform configuration files.
2. Create a file named `main.tf` and add the following content:

    ```hcl
    provider "azurerm" {
      features {}
    }

    resource "azurerm_resource_group" "rg_tutorial" {
      name     = "rg-terraform-tutorial"
      location = "West Europe"
    }
    ```

3. Initialize the configuration with `terraform init`.
4. Generate and review an execution plan with `terraform plan`.
5. Apply the changes with `terraform apply`.

This configuration will create a resource group named "rg-terraform-tutorial" in the "West Europe" location on Azure. The `name` follows a common naming convention: prefixing with "rg" to denote it's a resource group, followed by a descriptive name. Adjust the `location` value as needed for your specific environment.

## Advanced Topics

### State Management

Learn how to manage and store Terraform state files securely and efficiently, including best practices for remote state storage.

### Modules

Understand how to create reusable and composable Terraform modules to simplify your configurations.
> WOP
### Workspaces

Explore the use of Terraform workspaces to manage multiple environments within the same configuration.
> WOP
### Provisioners

Discover how to use provisioners to execute scripts and automate tasks as part of the resource creation process.
> WOP

### Terraform Associate (003) Exam

[Check out Questions ](./questions/001.md) 
#

## Additional Resources

- [Official Terraform Documentation](https://www.terraform.io/docs)
- [Terraform Best Practices](https://www.hashicorp.com/resources/terraform-best-practices)
- [Community Forums](https://discuss.hashicorp.com/c/terraform)

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License
