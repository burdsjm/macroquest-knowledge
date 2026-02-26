# Lua

Use this page for Lua scripting patterns if your workflow includes Lua modules.

## When to use Lua

- More structured code organization.
- Better module reuse.
- Richer data handling compared to basic macro patterns.

## Suggested sections

- Runtime basics
- Event hooks/callbacks
- Interop with MQ commands and TLOs
- Project layout conventions
- Debug logging standards

## Minimal style guide

- Keep one responsibility per module.
- Validate external state before acting.
- Prefer explicit state tables over globals.
- Add trace logs for state transitions.
