# Unlocking Terraform State

## Which command should be used to remove a lock on the state file if the process that created the lock has crashed?

- [ ] `terraform unlock`
- [x] `terraform force-unlock`
- [ ] `terraform state unlock`
- [ ] `terraform lock -remove`

### Answer Explanation

- **`terraform force-unlock`**: This is the correct command. It is used to manually unlock the state if the automatic unlocking failed (e.g., the process crashed). It requires the `LOCK_ID` as an argument.

- **`terraform unlock`**, **`terraform state unlock`**, and **`terraform lock -remove`**: These are not valid Terraform commands for unlocking the state.

**Note:** You should only use `force-unlock` if you are certain that the process holding the lock is no longer running, as unlocking a state that is currently being modified can lead to state corruption.

### Summary

The command **`terraform force-unlock`** is used to remove a lock on the state file when the locking process has crashed.
