# Data Types and Top Level Objects (TLOs)

## What Are TLOs?

**Top Level Objects (TLOs)** are the root data objects that MacroQuest exposes to macros and Lua scripts. They are accessed using the `${}` syntax in macros or `mq.TLO.*` in Lua.

## Accessing TLO Data

**In macros:**
```
/echo ${Me.Name}
/echo ${Target.PctHPs}
/echo ${Zone.Name}
```

**In Lua:**
```lua
local mq = require('mq')
print(mq.TLO.Me.Name())
print(mq.TLO.Target.PctHPs())
```

> Note: In Lua, TLO members are functions and must be called with `()`.

## Core TLOs

### `${Me}` — Your Character

| Member | Type | Description |
|--------|------|-------------|
| `Me.Name` | string | Character name |
| `Me.Level` | int | Character level |
| `Me.Class` | string | Character class name |
| `Me.PctHPs` | int | Current HP percentage |
| `Me.PctMana` | int | Current mana percentage |
| `Me.PctEndurance` | int | Current endurance percentage |
| `Me.HP` | int | Current hit points |
| `Me.MaxHP` | int | Maximum hit points |
| `Me.Mana` | int | Current mana |
| `Me.MaxMana` | int | Maximum mana |
| `Me.X` | float | X coordinate |
| `Me.Y` | float | Y coordinate |
| `Me.Z` | float | Z coordinate (height) |
| `Me.Heading` | string | Facing direction |
| `Me.Combat` | bool | Is in combat |
| `Me.Casting` | string | Spell currently being cast |
| `Me.Buff[name]` | buff | Active buff by name |
| `Me.Gem[name/slot]` | spell | Memorized spell |
| `Me.Inventory[slot]` | item | Inventory item |
| `Me.Standing` | bool | Is standing |
| `Me.Sitting` | bool | Is sitting |
| `Me.Moving` | bool | Is moving |
| `Me.Grouped` | bool | Is in a group |
| `Me.Invis` | bool | Is invisible |

### `${Target}` — Current Target

| Member | Type | Description |
|--------|------|-------------|
| `Target.ID` | int | Spawn ID (0 if no target) |
| `Target.Name` | string | Target's name |
| `Target.Type` | string | Spawn type: PC, NPC, Corpse, etc. |
| `Target.Level` | int | Target's level |
| `Target.PctHPs` | int | Target's HP percentage |
| `Target.Distance` | float | Distance to target |
| `Target.Distance3D` | float | 3D distance to target |
| `Target.Buff[name]` | buff | Target's active buff |
| `Target.Class` | string | Target's class |

### `${Spawn[filter]}` — Find a Spawn

Locate any spawn in the zone by filter:

```
${Spawn[npc Skeleton]}          ; first NPC named Skeleton
${Spawn[pc Jimbob]}             ; PC named Jimbob
${Spawn[id 12345]}              ; spawn by ID
${Spawn[npc radius 50]}         ; first NPC within 50 units
```

| Member | Description |
|--------|-------------|
| `Spawn.ID` | Spawn ID |
| `Spawn.Name` | Name |
| `Spawn.Distance` | Distance from you |
| `Spawn.Type` | PC / NPC / Corpse |
| `Spawn.PctHPs` | HP percentage |

### `${SpawnCount[filter]}` — Count Spawns

```
${SpawnCount[npc radius 50]}    ; number of NPCs within 50 units
${SpawnCount[npc]}              ; total NPCs in zone
```

### `${Group}` — Group Information

| Member | Description |
|--------|-------------|
| `Group.Members` | Number of group members (excluding you) |
| `Group.Member[n]` | nth group member spawn |
| `Group.Leader` | Group leader spawn |

### `${Zone}` — Current Zone

| Member | Description |
|--------|-------------|
| `Zone.Name` | Long zone name |
| `Zone.ShortName` | Short zone identifier (e.g. `gfaydark`) |
| `Zone.ID` | Numeric zone ID |
| `Zone.Safe` | Safe coordinates (struct with X/Y/Z) |

### `${Math}` — Math Utilities

```
${Math.Abs[-5]}            ; 5
${Math.Calc[3+4*2]}        ; 11
${Math.Distance[y1,x1:y2,x2]}  ; 2D distance between points
${Math.Rand[100]}          ; random int 0-99
```

### `${String}` — String Utilities

```
${String[Hello World].Length}
${String[hello].Upper}
${String[HELLO].Lower}
${String[Hello World].Left[5]}   ; Hello
```

### `${Navigation}` — MQ2Nav

| Member | Description |
|--------|-------------|
| `Navigation.Active` | Is navigation currently running |
| `Navigation.Paused` | Is navigation paused |
| `Navigation.MeshLoaded` | Is the navmesh loaded |

### `${Cursor}` — Item on Cursor

| Member | Description |
|--------|-------------|
| `Cursor.Name` | Name of item on cursor |
| `Cursor.ID` | Item ID |

## Data Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer number | `${Me.Level}` → `60` |
| `float` | Floating point | `${Me.X}` → `-234.50` |
| `string` | Text | `${Me.Name}` → `"Adventurer"` |
| `bool` | True / False | `${Me.Combat}` → `TRUE` |
| `spell` | Spell data object | `${Me.Gem[1]}` |
| `item` | Item data object | `${Me.Inventory[pack1]}` |
| `spawn` | Spawn data object | `${Target}` |
| `buff` | Active buff object | `${Me.Buff[Haste]}` |

## Type Members Chain

TLO members can be chained:

```
; Get the name of the first spell in gem slot 1
${Me.Gem[1].Name}

; Distance to the group leader
${Group.Leader.Distance}

; Does my target have a buff named "Regen"?
${Target.Buff[Regen].ID}
```

If any member in the chain is null/invalid, the expression returns an empty string or `0`, so always check `.ID` or `.Name` before assuming a result is valid.

## See Also

- [Macros Basics](Macros-Basics.md)
- [Macro Patterns](Macro-Patterns.md)
- [Lua](Lua.md)
