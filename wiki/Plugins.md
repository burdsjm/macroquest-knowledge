# Plugins

Plugins are compiled `.dll` files that extend MacroQuest with additional commands, TLOs, and features.

## Managing Plugins

### Loading a Plugin

```
/plugin <PluginName>
```

Example:
```
/plugin MQ2Nav
```

### Unloading a Plugin

```
/plugin <PluginName> unload
```

### Listing Loaded Plugins

```
/plugins
```

### Auto-Loading Plugins

Add to `macroquest.ini` under `[Plugins]`:

```ini
[Plugins]
MQ2Nav=1
MQ2MoveUtils=1
MQ2Cast=1
```

## Core Plugin Catalog

### Navigation

| Plugin | Description |
|--------|-------------|
| **MQ2Nav** | Full mesh-based pathfinding. The standard navigation plugin. Commands: `/nav`. TLO: `${Navigation}`. Requires a navmesh for each zone. |

### Movement

| Plugin | Description |
|--------|-------------|
| **MQ2MoveUtils** | Movement utilities: `StickyMove`, `Heading`, `MakeCamp`. Commands: `/moveto`, `/circle`, `/makecamp`. |

### Casting / Combat

| Plugin | Description |
|--------|-------------|
| **MQ2Cast** | Reliable spell casting with interrupt detection and retries. Command: `/cast`. Preferred over raw `/cast` in macros. |
| **MQ2Melee** | Automates melee combat: combat abilities, disciplines, stances. |
| **MQ2Debuffs** | Auto-debuff and slow management. |

### Targeting / Assisting

| Plugin | Description |
|--------|-------------|
| **MQ2Assist** | Assists the main assist automatically. |
| **MQ2Target** | Advanced targeting filters and nearest-enemy logic. |

### UI / Display

| Plugin | Description |
|--------|-------------|
| **MQ2Map** | Adds a fully featured overhead map with spawn labeling. |
| **MQ2HUD** | Heads-Up Display; overlays customizable text on the screen. |
| **MQ2AutoGroup** | Automates grouping with designated players. |

### Communication / Boxing

| Plugin | Description |
|--------|-------------|
| **MQ2DanNet** | Peer-to-peer networking between multiple MQ instances. Enables multi-box communication without eqbc. |
| **MQ2EQBC** | EverQuest Box Client — older server-based multi-box communication. |
| **MQ2Relay** | Command relay between characters. |

### Inventory / Items

| Plugin | Description |
|--------|-------------|
| **MQ2Inventory** | Inventory management, bag organization. |
| **MQ2Loot** | Automated looting with filter rules. |
| **MQ2Exchange** | Swap items between inventory slots. |

### Tradeskills

| Plugin | Description |
|--------|-------------|
| **MQ2Craft** | Automates tradeskill combines. |

### Miscellaneous

| Plugin | Description |
|--------|-------------|
| **MQ2Rez** | Auto-accepts resurrections. |
| **MQ2AutoLogin** | Automates the EQ login process. |
| **MQ2TributeManager** | Manages tribute auto-activation. |
| **MQ2Twist** | Bard song twist automation. |

## Per-Plugin Notes

### MQ2Nav

- Requires a navmesh file (`*.nmesh`) in the `MQ2Nav/` folder for each zone.
- Meshes are generated using the MeshGenerator tool or downloaded from the community.
- Key TLO: `${Navigation.Active}`, `${Navigation.MeshLoaded}`

```
/nav target                   ; navigate to current target
/nav loc -200 100 -10         ; navigate to Y X Z
/nav spawn Freeport Guard     ; navigate to named NPC
/nav stop                     ; halt navigation
```

### MQ2MoveUtils

```
/moveto id 12345              ; move to spawn ID
/moveto loc -200 100          ; move to Y X
/makecamp                     ; set camp at current location
/makecamp return              ; return to camp
/circle                       ; circle around current position
```

### MQ2Cast

```
/cast "Spell Name"            ; cast by name
/cast 1                       ; cast gem slot 1
/interrupt                    ; interrupt current cast
```

### MQ2DanNet

```
/dnet tell <name> /echo hello ; send command to another character
/dnet group /stand            ; send command to all group members
/dobserve <name>              ; observe a TLO from another character
```

## See Also

- [Plugin Development](Plugin-Development.md)
- [Commands Reference](Commands-Reference.md)
- [Common Snippets](Common-Snippets.md)
