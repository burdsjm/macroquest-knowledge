# Plugin Development

## Scope

This page tracks plugin development conventions and references to official MQ developer docs.

## Development workflow

1. Define plugin objective and API surface.
2. Scaffold plugin structure.
3. Implement minimal command/TLO exposure.
4. Add logging and configuration handling.
5. Test in safe scenarios before release.

## Engineering standards

- Keep plugin responsibilities small and composable.
- Fail gracefully when game state is missing/invalid.
- Avoid blocking operations in critical loops.
- Version your config schema.

## Documentation checklist

- [ ] Commands
- [ ] Settings
- [ ] Dependencies
- [ ] Compatibility matrix
- [ ] Known issues
