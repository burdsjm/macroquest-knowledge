# Troubleshooting

## MQ Does Not Inject / Start

**Symptom:** MQ console opens but the game does not show the MQ chime or `/mqversion` returns nothing.

**Causes and fixes:**
- **EQ is not running yet** — start MQ first, then launch EQ.
- **Wrong EQ version/path** — verify `macroquest.ini` has the correct `[MacroQuest]` → `EQPath` pointing to your EQ folder.
- **Anti-virus blocking injection** — add the MQ folder to your AV exclusions.
- **Running as a different user** — run both EQ and MQ as the same Windows user (both as Administrator, or both as normal user).
- **Wrong server type** — ensure you have the correct MQ build for your server (Live vs Emu).

## Crash on Zone / Load

**Symptom:** EQ crashes immediately or on zone.

**Fixes:**
1. Disable all plugins: edit `macroquest.ini` and remove all entries from `[Plugins]`.
2. Re-enable plugins one at a time to identify the culprit.
3. Update MQ and all plugins to the latest build.
4. Delete `MQ2Map.ini` or other plugin INI files if the plugin fails after a clean install.
5. Verify navmesh files are up to date (for MQ2Nav crashes).

## Macro Errors / Not Running

**Symptom:** Macro stops with an error, or `/macro` does nothing.

**Common errors:**

| Error | Likely Cause |
|-------|-------------|
| `Unknown command` | Plugin providing that command is not loaded |
| `Could not find subroutine Main` | Missing `Sub Main` in the macro file |
| `Parse error at line N` | Syntax error — check braces, quotes, and variable names |
| `Variable already declared` | Redeclaring a variable that already exists in scope |
| `Type mismatch` | Assigning a string to an int variable, etc. |

**Debugging tips:**
- Add `/echo` statements to trace execution.
- Use `/mqpause` to pause and inspect state.
- Check the MQ console for red error text.

## Navigation Not Working (MQ2Nav)

**Symptom:** `/nav target` does nothing or character walks a few steps and stops.

**Fixes:**
- Check `${Navigation.MeshLoaded}` — if `FALSE`, you are missing a navmesh for this zone.
- Download or generate a navmesh for the zone and place it in the `MQ2Nav/meshes/` folder.
- If the mesh is loaded but pathfinding fails, try `/nav target distance=10` to ensure you're not asking for an unreachable point.
- Type `/nav reload` to force-reload the navmesh.

## Plugin Will Not Load

**Symptom:** `/plugin MQ2Something` returns "Plugin not found" or similar.

**Fixes:**
- Ensure the `.dll` is in the MQ `plugins/` folder.
- Check the plugin is built for the correct MQ version (MQ Next vs MQ2).
- Look in the MQ console for DLL load errors (missing CRT, wrong architecture).
- Ensure prerequisites (e.g. MQ2Nav requires a navmesh) are satisfied.

## High CPU Usage

**Symptom:** EQ or MQ console is pegging CPU.

**Fixes:**
- Identify the culprit plugin: unload plugins one by one and watch CPU.
- Macros with tight loops (`/while (TRUE) { /delay 1 }`) should have a small delay; use `/delay 5` or more.
- Lua scripts: use `mq.delay(100)` instead of no delay in the main loop.

## Chat / Event Not Firing

**Symptom:** `#event` in a macro or `mq.event` in Lua does not trigger.

**Fixes:**
- Ensure `/doevents` (macros) or `mq.doevents()` (Lua) is called inside the main loop.
- The event pattern is case-sensitive — verify it matches exactly what is displayed in chat.
- Use `/echo` to confirm the text you see in chat matches your pattern.
- The `#*#` wildcard matches any text; use it for variable parts of the message.

## Spell Cast Fails

**Symptom:** `/cast "Spell Name"` has no effect.

**Fixes:**
- Verify the spell name exactly as it appears in your spellbook (case-sensitive).
- Check you have the spell memorized: `${Me.Gem["Spell Name"].ID}`
- Ensure you are in range and the target is valid.
- Consider using [MQ2Cast](Plugins.md#mq2cast) for more reliable casting.

## MQ Overlay / UI Not Showing

**Symptom:** ImGui windows from plugins or Lua do not appear.

**Fixes:**
- Press the default overlay toggle key (check your keybinds).
- Ensure the plugin/script calling ImGui is actually loaded and running.
- Restart MQ.

## Useful Diagnostic Commands

```
/mqversion              ; confirm MQ is loaded and get version
/plugins                ; list loaded plugins
/memspells              ; display memorized spells
/target                 ; inspect current target details
/echo ${Me.PctHPs}      ; test TLO access
/echo ${Zone.Name}      ; confirm current zone
```

## Getting Help

- [MacroQuest GitHub Issues](https://github.com/macroquest/macroquest/issues)
- [MacroQuest Discord](https://discord.gg/macroquest)
- [EQEmulator Forums](https://forums.eqemulator.net/)
