# Terraform `regex()`

## Introduction

The `regex()` function in Terraform is used to match a string against a regular expression (regex) pattern. It is helpful for validating string formats, extracting substrings, and performing complex pattern matching within your Terraform configurations.

## Syntax

```hcl
regex(pattern, string)
```

### Parameters

- **`pattern`**: A string representing the regular expression pattern you want to match against.
- **`string`**: The input string that you want to test against the regex pattern.

### Returns

- **`string`**: Returns the substring from `string` that matches the `pattern`. If no match is found, it returns an empty string.

## Example Usage

Here are some examples to illustrate how the `regex()` function can be used in different scenarios.

### Basic Example

Suppose you want to extract the digits from a string.

```hcl
locals {
  input_string = "The number is 12345."
  regex_pattern = "\\d+"  # Regex pattern to match one or more digits
}

output "extracted_digits" {
  value = regex(local.regex_pattern, local.input_string)
}
```

In this example, the output will be `12345`, which is the substring that matches the pattern `\\d+` (one or more digits) in the `input_string`.

### Validating a Format

You can use the `regex()` function to validate if a string matches a specific format, such as an email address.

```hcl
locals {
  email = "example@domain.com"
  regex_pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"  # Regex pattern for email
}

output "is_valid_email" {
  value = regex(local.regex_pattern, local.email) != ""
}
```

In this example, `is_valid_email` will be `true` if the `email` string matches the regex pattern for a valid email address.

### Extracting Substrings

You can use `regex()` to extract specific parts of a string. For example, extracting the domain from a URL.

```hcl
locals {
  url = "https://www.example.com/path"
  regex_pattern = "^https?://([^/]+)"  # Regex pattern to capture the domain
}

output "extracted_domain" {
  value = regex(local.regex_pattern, local.url)
}
```

In this example, `extracted_domain` will be `www.example.com`, which is the domain extracted from the `url` string using the regex pattern.

## Common Use Cases

- **Validation**: Ensure strings conform to specific formats, such as emails, phone numbers, or custom formats.
- **Extraction**: Extract specific parts of a string based on a regex pattern.
- **Transformation**: Modify or process strings based on pattern matching.

## Summary

The `regex()` function in Terraform is a powerful tool for pattern matching and string manipulation. It allows you to match strings against regular expressions, validate formats, and extract substrings based on complex patterns. 

For more information, refer to the [official Terraform documentation](https://registry.terraform.io/providers/hashicorp/null/latest/docs/functions/regex).
