# Glossary

Definitions for MacroQuest terms, abbreviations, and EverQuest concepts commonly encountered when using MQ.

---

## A

**Alias**  
A shorthand command that expands to a longer command string. Created with `/alias`.

**Assist**  
Targeting the same enemy as another player. Used in groups so all DPS attack the same target. The "main assist" (MA) is the designated target caller.

## B

**Bind / Key Bind**  
A keyboard shortcut mapped to an MQ command or action. Created with `/bind`.

**Boxing**  
Playing multiple EverQuest characters simultaneously, usually on one machine or across multiple machines, often automated with MQ.

**Buff**  
A beneficial spell effect active on a character.

## C

**Camp**  
A fixed location a character returns to between fights. Set in macros using coordinates or `/makecamp`.

**Cast**  
The act of using a spell. In MQ: `/cast "Spell Name"`.

**Command**  
A slash-prefixed instruction typed in-game (e.g. `/echo`, `/nav target`).

## D

**DanNet**  
The MQ2DanNet plugin; provides peer-to-peer networking between multiple MQ instances for multi-boxing.

**Delay**  
A pause in macro execution. In macros: `/delay N [condition]`. In Lua: `mq.delay(ms)`.

**Detour**  
A technique used by MQ to intercept EQ game functions by redirecting function pointers in memory.

**DoEvents**  
Processing pending macro events (from `#event` declarations). In macros: `/doevents`. In Lua: `mq.doevents()`.

## E

**EQ / EverQuest**  
The MMORPG that MacroQuest is designed to work with.

**EQEmu / EQEmulator**  
An open-source EverQuest emulator server platform.

**Event**  
A macro mechanism that triggers a subroutine when a matching chat string is detected. Declared with `#event`.

## F

**FPS (Frames Per Second)**  
How often the game renders a frame. Low FPS can indicate performance problems, sometimes caused by MQ plugins.

## G

**Global Variable**  
A variable declared with scope `global` in a macro; visible to all subroutines in the running macro.

## H

**Hook**  
A point in the game where MQ intercepts normal game code execution to add custom behavior.

**HUD (Heads-Up Display)**  
Text overlaid on the game screen, often provided by MQ2HUD.

## I

**ImGui**  
A widely-used C++ immediate mode GUI library. MQ Next integrates ImGui so plugins and Lua scripts can render in-game windows.

**INI (file)**  
Windows `.ini` configuration file format, used extensively by MQ and its plugins for settings storage.

**Injection**  
The process by which MQ loads its DLL into the EQ process at runtime.

## L

**Lua**  
A lightweight scripting language. MQ Next has a built-in Lua runtime for writing scripts (`.lua` files).

**Local Variable**  
A variable declared with scope `local` in a macro; only visible within the current subroutine.

## M

**Macro**  
A `.mac` script file that automates in-game actions using the MQ scripting language.

**MA (Main Assist)**  
The designated player whose target all DPS should attack.

**Member**  
A property or method on a TLO or data type. Accessed with dot notation: `${Me.Name}`.

**MQ / MacroQuest**  
The third-party automation framework for EverQuest.

**MQ2**  
The legacy version of MacroQuest (older, less actively maintained).

**MQ Next / MQNext**  
The current, actively maintained version of MacroQuest (from the `macroquest/macroquest` repo).

**Mesh / Navmesh**  
A 3D navigation mesh file used by MQ2Nav to determine walkable paths in a zone (`.nmesh` files).

## N

**NPC (Non-Player Character)**  
Any game entity controlled by the server AI rather than a player.

**Navigation**  
Automated movement using pathfinding. Provided by the MQ2Nav plugin.

## O

**OnPulse**  
A plugin hook called every game frame. Used for per-frame logic in C++ plugins.

## P

**PC (Player Character)**  
A character controlled by a human player.

**Pet**  
A creature summoned to fight alongside a player.

**Plugin**  
A compiled `.dll` file that extends MQ with additional features.

**Pulse**  
One game tick/frame. MQ's `OnPulse` runs every pulse.

## S

**Spawn**  
Any entity present in the game world: PCs, NPCs, pets, corpses, ground items.

**Spawn ID**  
A unique integer identifier for each spawn in the current zone.

**State Machine**  
A macro/script architecture using a `State` variable to control which logic block runs. Recommended for complex automation.

**Subroutine**  
A named block of macro code, defined with `Sub Name` / `/return`.

## T

**TLO (Top Level Object)**  
A root data object exposed by MQ to macros and scripts (e.g. `${Me}`, `${Target}`, `${Zone}`).

**Timer**  
A macro variable type that counts down automatically. Useful for cooldown tracking.

**Type**  
A data type in the MQ type system (e.g. `spawn`, `spell`, `item`, `string`, `int`).

## W

**Wiki**  
This documentation collection.

## Z

**Zone**  
A discrete map area in EverQuest. Characters zone (travel) between zones.

**Zoning**  
The act of moving from one zone to another, involving a load screen.
