# Plan review checklist

## Classify every finding

- **Plan defect:** the plan is wrong or incomplete about how to implement an approved design.
- **Design concern:** the plan or its Design Record makes an architectural decision that has not been reasoned through. Return to Design; do not patch it here.
- **Requirement gap:** the plan misses something the requirement or Design Record calls for.
- **Optional simplification:** a suggestion, not a blocker.

## Architecture and design

- Does the design fit the existing architecture?
- Does it add new patterns where existing ones would work?
- Is the abstraction level right: not over-engineered, not under-designed?
- Are component boundaries clean and responsibilities clearly divided?
- Will the codebase stay coherent after the change?

## Complexity (the most important part)

- Is there a fundamentally different, simpler approach?
- Can challenging requirements or assumptions unlock a cleaner solution?
- Unnecessary layers, abstractions or indirections?
- Could language or framework features replace custom code?
- Does the plan solve problems that do not exist?

## Gaps and blind spots

- Error handling, edge cases, failure modes.
- Migration and data compatibility.
- Performance.
- Concurrency and state management.
- Impact on parts of the system the plan does not mention.

## Security

- Input validation, authentication, authorization.
- Data exposure or leakage.
- Dependency risks.

## Maintainability

- Easy to understand and maintain afterwards?
- Dead code, unused abstractions or outdated docs left behind?
- Is the testing strategy adequate?
- Can future developers (or AI) work with it confidently?

## Completeness

- Could someone execute the steps as written? Missing steps, undefined behaviour, wrong order?
- Are verification criteria clear enough to test against?
- Does every new behaviour have Given/When/Then acceptance criteria, each "Then" observable in real system behaviour rather than an internal state check?
