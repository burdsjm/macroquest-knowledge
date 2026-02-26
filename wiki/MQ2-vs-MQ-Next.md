# MQ2 vs MQ Next

> Use this page as migration notes. Confirm exact version details in official docs/release notes.

## High-level differences

- Naming and command behaviors may differ across generations.
- Plugin sets and defaults may not be identical.
- Some macro idioms are legacy and have modern equivalents.
- Lua adoption is stronger in modern workflows for many users.

## Migration strategy

1. Inventory your active macros/plugins.
2. Validate each command and TLO reference against current docs.
3. Replace deprecated patterns incrementally.
4. Test on low-risk characters/scenarios first.

## Common migration checks

- Deprecated commands and arguments.
- Plugin rename or replacement.
- Event handling differences in macro/lua scripts.
- Timing assumptions (wait loops, zoning, target acquisition).

## Recommended approach

- Keep old scripts in a `legacy/` folder.
- Port one behavior at a time.
- Add logging output during migration to validate branches/states.
