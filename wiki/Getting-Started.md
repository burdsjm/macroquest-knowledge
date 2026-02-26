# Getting Started with MacroQuest

## Prerequisites

- A working EverQuest installation (Live, Emu, or private server)
- Windows OS (MacroQuest is Windows-only)
- Basic familiarity with the Windows file system

## Installation

### MQ Next (Recommended)

1. Download the latest release from the [MacroQuest GitHub releases page](https://github.com/macroquest/macroquest/releases).
2. Extract the archive to a folder **outside** of your EverQuest directory (e.g. `C:\MacroQuest\`).
3. Run `MacroQuest.exe` **before** launching EverQuest.
4. Log in to EverQuest — MQ will inject automatically when it detects the game process.

### MQ2 (Legacy)

1. Download the MQ2 build for your server type.
2. Extract to a dedicated folder.
3. Run `MacroQuest2.exe` before launching EverQuest.

## First Run

After injecting, you should see a splash/console window and hear a chime in-game.  
Type `/mqversion` in-game to confirm MQ is loaded.

Common startup checks:
- `/plugins` — lists loaded plugins
- `/ini` — shows the current INI configuration
- `/help` — displays built-in help

## Safety Notes

> ⚠️ **MacroQuest modifies game memory and may violate the game's Terms of Service.** Use only on private/emulated servers unless you accept the risk of a Live account ban.

- Never share your account credentials with MQ configuration files.
- Keep MQ and all plugins up to date to avoid crashes from game patches.
- Use caution with untrusted macros or plugins downloaded from unknown sources.
- Avoid running MQ on the same machine as other accounts you do not want flagged.

## Terminology

| Term | Meaning |
|------|---------|
| **MQ / MQ2 / MQNext** | MacroQuest versions — MQ2 is legacy, MQNext is current |
| **Plugin** | A compiled `.dll` that extends MQ functionality |
| **Macro** | A `.mac` script that automates in-game actions |
| **TLO** | Top Level Object — a root data object exposed by MQ (e.g. `${Me}`, `${Target}`) |
| **Spawn** | Any entity in the game world (player, NPC, pet, etc.) |
| **INI** | Windows `.ini` configuration file used by MQ and plugins |
| **Hook** | A point where MQ intercepts game function calls |
| **Detour** | An in-memory function redirect used by MQ to intercept EQ calls |

## Next Steps

- [Commands Reference](Commands-Reference.md) — learn essential slash commands
- [Macros Basics](Macros-Basics.md) — start writing your first macro
- [Plugins](Plugins.md) — discover what plugins are available
