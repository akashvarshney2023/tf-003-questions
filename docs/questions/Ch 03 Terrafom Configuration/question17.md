# Terraform Dependency Graph Building

## **Terraform builds a dependency graph from the Terraform configurations. Which is NOT a correct step of building a Graph?**

- [ ] **Resources are mapped to provisioners if they have any defined.**
- [ ] **Resources are mapped to providers.**
- [ ] **Resources nodes are added to the graph from the configuration.**
- [x] **Resources are not added to the graph that are no longer present in the configuration but are present in the state file.**

### Answer Explanation

- **Resources are mapped to provisioners if they have any defined:** This is a correct step. Terraform maps resources to provisioners defined in the configuration as part of building the graph.

- **Resources are mapped to providers:** This is a correct step. Resources are associated with providers in the graph based on the configuration.

- **Resources nodes are added to the graph from the configuration:** This is a correct step. Terraform includes resources defined in the configuration into the graph.

- **Resources are not added to the graph that are no longer present in the configuration but are present in the state file:** This is **NOT** a correct step. Resources that are present in the state file but no longer in the configuration are still part of the dependency graph. Terraform uses the state file to reconcile the actual infrastructure with the configuration.

### Summary

The statement **"Resources are not added to the graph that are no longer present in the configuration but are present in the state file"** is NOT a correct step in building the dependency graph.
