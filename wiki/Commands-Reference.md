# Commands Reference

## Global Commands

These commands are available at all times while MQ is loaded.

### Core / Meta

| Command | Description |
|---------|-------------|
| `/mqversion` | Display the current MQ version |
| `/mqpause` | Pause / unpause the currently running macro |
| `/mqquit` | Stop the running macro and clean up |
| `/plugins` | List all loaded plugins |
| `/plugin <name> [unload]` | Load or unload a plugin |
| `/ini <section> <key> <value>` | Read or write INI values |
| `/help [filter]` | Display help for commands matching filter |
| `/echo <text>` | Print text to the MQ console |
| `/varset <name> <value>` | Set a variable value in a running macro |
| `/varcalc <name> <expression>` | Set a variable to the result of a math expression |

### Navigation

| Command | Description |
|---------|-------------|
| `/nav` | MQ2Nav navigation commands (requires MQ2Nav plugin) |
| `/nav target` | Navigate to current target |
| `/nav spawn <name>` | Navigate to a named spawn |
| `/nav loc <y> <x> <z>` | Navigate to a world coordinate |
| `/nav stop` | Stop active navigation |
| `/nav pause` | Pause active navigation |
| `/nav door` | Navigate to and open nearest door |

### Targeting

| Command | Description |
|---------|-------------|
| `/target <name or id>` | Target a spawn by name or spawn ID |
| `/target pc <name>` | Target a player character |
| `/target npc <name>` | Target an NPC |
| `/mqtarget <filter>` | Target matching spawn (extended filter) |

### Macro Control

| Command | Description |
|---------|-------------|
| `/macro <file>` | Run a macro from the `macros/` folder |
| `/endmacro` | End the running macro |
| `/call <subroutine>` | Call a subroutine within the macro |
| `/return [value]` | Return from a subroutine |
| `/delay <ticks> [condition]` | Pause execution for N ticks or until condition |

### Window / UI

| Command | Description |
|---------|-------------|
| `/mqui` | Toggle the MQ overlay/UI |
| `/ctrlshift` | Show debug toggle (varies by setup) |
| `/windows` | List open EQ windows |
| `/notify <window> <control> <event>` | Send a UI event to a game window |

### Chat / Output

| Command | Description |
|---------|-------------|
| `/say <text>` | Say text in-game |
| `/gsay <text>` | Say text in group channel |
| `/rs <text>` | Say text in raid channel |
| `/g <text>` | Guild chat |
| `/bc <text>` | Broadcast to all characters (requires plugin) |

## Useful Key Bindings (Defaults)

| Key | Action |
|-----|--------|
| `End` | Pause / resume macro |
| `F11` | Toggle MQ overlay (varies) |

## Tips

- Commands are case-insensitive.
- Commands from plugins are only available when the plugin is loaded.
- Use `/echo ${command_output}` to debug TLO expressions inline.
- See also [Aliases and Binds](Aliases-and-Binds.md) for creating shortcuts.
