# Macros Basics

## Building blocks

- Subroutines
- Variables and scope
- Conditionals
- Loops and waits
- Events and parsing

## Starter macro workflow

1. Define objective (single, testable behavior).
2. Write a tiny command loop.
3. Add guardrails (distance, HP threshold, timeout).
4. Add debug echoes.
5. Refactor into reusable subroutines.

## Reliability principles

- Always include escape conditions.
- Assume target can change unexpectedly.
- Re-check preconditions after every wait.
- Keep macro state explicit and debuggable.

## Next

- [[Macro-Patterns]]
- [[Data-Types-and-TLO]]
