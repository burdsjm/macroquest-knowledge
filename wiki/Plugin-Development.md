# Plugin Development

## Scope

This page tracks plugin development conventions and references to official MQ developer docs.

## Official docs link map

Use this as a quick routing index before implementing or revising plugin behavior:

- **Plugin system overview**: https://docs.macroquest.org/plugins/
- **Plugin command reference (`/plugin`)**: https://docs.macroquest.org/reference/commands/plugin/
- **Developer docs landing**: https://docs.macroquest.org/main/developing/
- **MacroQuest API reference**: https://docs.macroquest.org/reference/
- **Data types and TLOs**: https://docs.macroquest.org/reference/data-types/ and https://docs.macroquest.org/reference/top-level-objects/
- **Core plugin examples (patterns and command docs)**: https://docs.macroquest.org/plugins/core-plugins/
- **Community plugin examples (real-world command/config patterns)**: https://docs.macroquest.org/plugins/community-plugins/

## Minimal plugin lifecycle checklist

Use this checklist as a pre-merge gate for new plugins and significant refactors.

### 1) Load and bootstrap

- [ ] Plugin loads cleanly with `/plugin <name> load noauto`.
- [ ] Missing external prerequisites are detected early with actionable log output.
- [ ] Startup does not assume game state that may be unavailable at initial load.

### 2) Initialization safety

- [ ] One-time initialization is idempotent (safe if called twice by accident).
- [ ] Runtime hooks/registers are guarded against duplicate registration.
- [ ] Startup failures leave plugin in a recoverable state (can unload/reload without restart).

### 3) Command/TLO exposure

- [ ] Command names are documented and collision-checked against existing workflow commands.
- [ ] Command parser validates arguments and returns helpful usage text on invalid input.
- [ ] Any TLO/datatype additions document shape, nullability, and edge-state behavior.

### 4) Config handling

- [ ] Config file read path is explicit and documented.
- [ ] Defaults are applied when keys are absent (forward-compatible schema behavior).
- [ ] Writes are controlled (avoid high-frequency disk churn in hot paths).
- [ ] Config migration/version field is updated when schema changes.

### 5) Safe shutdown

- [ ] Plugin unload (`/plugin <name> unload noauto`) unregisters commands/hooks cleanly.
- [ ] In-progress behaviors (movement, casting, loops, timers) are canceled on shutdown.
- [ ] UI resources and allocated memory/handles are released deterministically.
- [ ] Re-load after unload is validated as part of smoke testing.

## Compatibility note format (version-specific behavior tracking)

When behavior changes between MQ builds or game patches, append a structured note block:

```md
### Compatibility Note: <plugin-name>
- MQ build(s): <e.g., 2025-02-14 stable, 2025-02-20 test>
- EQ client build: <date/string>
- Area affected: <command | TLO | hook | UI | performance>
- Previous behavior: <short factual description>
- New behavior: <short factual description>
- Impact: <who breaks / severity>
- Required action: <config change, command change, code fix, none>
- Validation: <commands/tests used to verify>
- References: <docs URL, issue link, commit hash>
```

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
