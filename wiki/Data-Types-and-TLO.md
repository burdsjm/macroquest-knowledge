# Data Types and TLO

## What to document here

- Frequently used top-level objects.
- High-value members and methods.
- Type conversion gotchas.
- Null/empty checks and defensive access patterns.

## Suggested structure per TLO

### TLO Name

- **Type**:
- **Common members**:
- **Common methods**:
- **Example**:
- **Pitfalls**:

## Defensive expression patterns

- Check object existence before member access when possible.
- Avoid deep chained expressions without intermediate validation.
- Cache expensive lookups when repeatedly used in loops.
