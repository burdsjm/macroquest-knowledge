# Glossary

- **Aggro**: The current threat relationship between NPCs and players, often used to decide when to tank, heal, mez, or disengage.
  - *Where you'll see this:* [[Combat-Concepts]], [[Macros-Basics]]

- **Alias**: A user-defined shorthand command that expands into one or more MacroQuest commands.
  - *Where you'll see this:* [[Getting-Started]], [[Commands]]

- **Bind**: A key-to-command mapping used to trigger MacroQuest commands, macros, or Lua snippets from input.
  - *Where you'll see this:* [[Commands]], [[Getting-Started]]

- **Event**: In MacroQuest macros, an asynchronous text trigger (for example from chat or system output) that is matched and handled by an event subroutine.
  - *Where you'll see this:* [[Macros-Basics]], [[Macro-Events-and-Binds]]

- **Pulse / tick / update loop**: The recurring execution cycle where scripts/plugins perform periodic checks and actions; each pass should be lightweight to avoid lag.
  - *Where you'll see this:* [[Macros-Basics]], [[Lua]], [[Plugins]]

- **Fail-safe**: A conservative fallback action that stops or de-escalates automation when assumptions break (for example, bad target, zoning, low health, or missing resources).
  - *Where you'll see this:* [[Best-Practices]], [[Macros-Basics]], [[Lua]]

- **Guard**: A precondition check that must pass before an action runs (for example, "only cast if target is valid and in range").
  - *Where you'll see this:* [[Macros-Basics]], [[Lua]], [[Best-Practices]]

- **Macro**: A script written in MacroQuest macro language, typically organized into a `Sub Main` entry point plus helper subroutines and event handlers.
  - *Where you'll see this:* [[Macros-Basics]], [[Macro-Reference]]

- **Macro subroutine conventions**: Common structure and naming patterns for macro code (for example `Sub Main`, `Sub Event_*`, and helper `Sub`s), used to keep flow readable and maintainable.
  - *Where you'll see this:* [[Macros-Basics]], [[Macro-Reference]]

- **Member**: A property-like field on a data object/TLO that returns a value without invoking behavior.
  - *Where you'll see this:* [[Data-Types-and-TLO]], [[Macro-Reference]]

- **Method**: A callable function on a data object/TLO that performs an operation and may accept arguments.
  - *Where you'll see this:* [[Data-Types-and-TLO]], [[Macro-Reference]]

- **Module**: A reusable Lua or script component intended to be imported/required by other scripts.
  - *Where you'll see this:* [[Lua]], [[Project-Structure]]

- **Plugin**: A compiled extension that adds commands, TLOs, data types, or runtime features to MacroQuest.
  - *Where you'll see this:* [[Plugins]], [[Data-Types-and-TLO]]

- **Plugin lifecycle**: The load, initialization, active runtime, and unload phases of a plugin, including command/TLO registration and cleanup.
  - *Where you'll see this:* [[Plugins]], [[Plugin-Development]]

- **State machine**: A control-flow pattern where behavior is split into explicit states and transitions based on conditions/events.
  - *Where you'll see this:* [[Macros-Basics]], [[Best-Practices]]

- **TLO (Top-Level Object)**: The root object namespace (for example `${Me}`, `${Target}`, `${Zone}`) used as an entry point into MacroQuest data queries.
  - *Where you'll see this:* [[Data-Types-and-TLO]], [[Macros-Basics]]

- **TLO vs member vs method**: A TLO is the root object, members are value fields on that object, and methods are callable operations on that object.
  - *Where you'll see this:* [[Data-Types-and-TLO]], [[Macro-Reference]]

- **Timeout**: A maximum wait duration for a condition/event before the script takes alternate action (retry, skip, or fail-safe).
  - *Where you'll see this:* [[Macros-Basics]], [[Best-Practices]], [[Lua]]
