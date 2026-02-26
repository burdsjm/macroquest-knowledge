# Performance and Stability

## Core principles

- Keep loops efficient.
- Minimize repeated expensive checks.
- Load only required plugins.
- Use clear state transitions to avoid thrashing.

## Performance checklist

- [ ] Loop intervals tuned and justified
- [ ] Repeated expressions cached where practical
- [ ] Non-critical logging reduced in steady state
- [ ] Plugin footprint reviewed

## Stability checklist

- [ ] Recovery path for failed casts/actions
- [ ] Timeout for movement/target waits
- [ ] Safe fallback state on errors
- [ ] Manual override/stop key always available
