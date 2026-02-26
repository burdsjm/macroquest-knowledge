# Macro Patterns

Reusable macro patterns inspired by common MQ scripting practice.

## Pulling loop

- Acquire eligible target.
- Validate path/range/aggro constraints.
- Execute pull ability.
- Return to camp and hand off to assist logic.

## Buff maintenance loop

- Iterate configured buff list.
- Check duration threshold.
- Cast/refresh with cooldown and mana gates.
- Skip while in combat when configured.

## Healing loop

- Priority queue by role and HP threshold.
- Emergency branch first, then efficiency branch.
- Debounce repeated casts to avoid spam.

## State machine approach

Use explicit states for reliability:

- `IDLE`
- `PREP`
- `ENGAGE`
- `RECOVER`
- `ERROR`

Store current state in one variable and log transitions.
