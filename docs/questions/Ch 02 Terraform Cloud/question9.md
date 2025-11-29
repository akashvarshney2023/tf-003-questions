# Sentinel Enforcement Levels

## Which Sentinel enforcement level allows the policy to be overridden by an administrator?

- [ ] Advisory
- [x] Soft Mandatory
- [ ] Hard Mandatory
- [ ] Strict

### Answer Explanation

Sentinel policies can be configured with different enforcement levels:

- **Advisory**: The policy is checked, and if it fails, a warning is shown, but the run is allowed to proceed.
- **Soft Mandatory**: If the policy fails, the run is halted. However, an administrator (or user with appropriate permissions) can override the failure and proceed with the run.
- **Hard Mandatory**: If the policy fails, the run is halted and **cannot** be overridden.

- **Strict**: This is not a valid Sentinel enforcement level.

Therefore, **Soft Mandatory** is the level that allows for overrides.

### Summary

The **Soft Mandatory** enforcement level allows a policy failure to be overridden by an administrator.
