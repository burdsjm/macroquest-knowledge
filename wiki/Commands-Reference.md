# Commands Reference

Use this page as a quick command index with practical examples. Keep entries concise here and move deep, command-specific edge cases to dedicated wiki pages when they become large.

## Session/control

| Command | Purpose | Example | Caveats |
|---|---|---|---|
| `/mqpause` | Pauses or unpauses MacroQuest command execution. | `/mqpause on` | Stops MQ command processing until resumed; easy to forget during troubleshooting. |
| `/timed` | Queues a command to run after a delay in ticks. | `/timed 50 /echo 5 seconds elapsed` | Delay is in EQ ticks (about 0.1s each), not seconds. |
| `/squelch` | Runs a command while suppressing command output text. | `/squelch /plugin list` | Only suppresses output; command still executes and side effects still apply. |

## Targeting

| Command | Purpose | Example | Caveats |
|---|---|---|---|
| `/target` | Targets a spawn by name or targetable expression. | `/target a_goblin` | Requires a valid in-zone spawn match; ambiguous names can select unexpected targets. |
| `/mqtarget` | Advanced target selection using MacroQuest search filters. | `/mqtarget npc radius 50` | Filter syntax must be valid search-spawn syntax; poor filters may retarget frequently in crowded zones. |

## Macro lifecycle

| Command | Purpose | Example | Caveats |
|---|---|---|---|
| `/macro` | Starts a macro file, optionally with arguments. | `/macro assist.mac MainTank` | Only one macro runs at a time per client; macro file must exist in your macro path. |
| `/endmacro` | Stops the currently running macro. | `/endmacro` | Immediate stop can leave stateful workflows half-finished (camp, movement, UI assumptions, etc.). |
| `/delay` | Pauses macro execution for a fixed time or condition. | `/delay 30s ${Me.CombatState.NotEqual[COMBAT]}` | Intended for macro flow; excessive long delays can make scripts appear hung. |

## Plugin management

| Command | Purpose | Example | Caveats |
|---|---|---|---|
| `/plugin` | Loads, unloads, and lists MacroQuest plugins. | `/plugin mq2eqbc load` | Plugin filename/build must match your installed release; unload can fail if plugin is in active use. |
| `/plugin` | Lists currently loaded plugins. | `/plugin list` | Output may be noisy on busy setups; combine with `/squelch` if used inside scripts. |

## Config/profile

| Command | Purpose | Example | Caveats |
|---|---|---|---|
| `/profile` | Manages MacroQuest profile sets for startup/load behavior. | `/profile load raid` | Profile names are local configuration artifacts; mismatched names fail silently in some workflows. |
| `/ini` | Reads or writes INI settings from command line/macros. | `/ini "${MacroQuest.Path[config]}\\custom.ini" Settings AssistOn 1` | Writes are immediate and persistent; validate path and section/key names before automation loops. |
| `/alias` | Creates or removes custom slash-command aliases. | `/alias pull /mqtarget npc radius 80` | Aliases can shadow expected commands if named carelessly; document team-standard aliases. |

## Source links

- **Session/control:**
  - https://docs.macroquest.org/reference/commands/mqpause/
  - https://docs.macroquest.org/reference/commands/timed/
  - https://docs.macroquest.org/reference/commands/squelch/
- **Targeting:**
  - https://docs.macroquest.org/reference/commands/target/
  - https://docs.macroquest.org/reference/commands/mqtarget/
- **Macro lifecycle:**
  - https://docs.macroquest.org/reference/commands/macro/
  - https://docs.macroquest.org/reference/commands/endmacro/
  - https://docs.macroquest.org/reference/commands/delay/
- **Plugin management:**
  - https://docs.macroquest.org/reference/commands/plugin/
- **Config/profile:**
  - https://docs.macroquest.org/reference/commands/profile/
  - https://docs.macroquest.org/reference/commands/ini/
  - https://docs.macroquest.org/reference/commands/alias/

## Maintenance rule

Whenever command behavior changes after an update:

1. Update this page summary.
2. Add detailed notes to dedicated command pages when the section outgrows this index.
