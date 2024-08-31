# Characteristics of Infrastructure as Code (IaC) Tools

## Which characteristic of an IaC tool ensures the same infrastructure state, if the same code is applied multiple times?

- [ ] Consistent
- [ ] Repeatable
- [x] Idempotent
- [ ] Predictable

### Answer Explanation

- **Idempotent:** In the context of Infrastructure as Code, idempotency ensures that applying the same code multiple times results in the same infrastructure state. This means that no matter how many times you run the same configuration, the outcome will remain consistent, without unintended changes or side effects.

- **Consistent:** While consistency is important, it generally refers to the stable behavior and output of the tool rather than the ability to maintain the same state across multiple applications of the code.

- **Repeatable:** Repeatability ensures that the same configuration can be applied repeatedly with the same result, but it does not specifically guarantee the same state across multiple applications.

- **Predictable:** Predictability refers to the ability to anticipate the outcomes of running the code, but it does not inherently guarantee that the same state will be achieved with repeated applications of the code.

### Summary

The characteristic of an IaC tool that ensures the same infrastructure state if the same code is applied multiple times is **idempotent**.
