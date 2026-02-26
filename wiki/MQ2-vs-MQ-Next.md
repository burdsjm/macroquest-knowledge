# MQ2 vs MQ Next

## Overview

| Feature | MQ2 (Legacy) | MQ Next (Current) |
|---------|-------------|-------------------|
| Repository | Various forks | [macroquest/macroquest](https://github.com/macroquest/macroquest) |
| Language | C++ (older standard) | C++17/20 |
| Build System | Visual Studio solution | CMake |
| Lua Support | Optional / patchy | Built-in (`mq::lua`) |
| ImGui Support | Limited | Full integration |
| Plugin API | Older callback style | Modernized API |
| Active Development | Minimal | Active |
| Documentation | Community wikis | [docs.macroquest.org](https://docs.macroquest.org/) |

## Key Differences

### Plugin Architecture

**MQ2** plugins used a flat set of exported C functions (e.g. `InitializePlugin`, `ShutdownPlugin`).  
**MQ Next** plugins use the same exported C functions but with a significantly expanded and more consistent API surface, plus access to modern C++ utilities.

### Data System (TLOs / Members)

Both versions expose Top Level Objects, but MQ Next has a cleaner type registration system.  
TLO names and member names are largely compatible but some members have been renamed or restructured.

### Lua

MQ Next ships with a built-in Lua runtime. You can run scripts with:

```
/lua run myscript
```

MQ2 had no official Lua support; some forks added it later.

### ImGui

MQ Next has full ImGui integration, enabling plugins to render in-game UI windows easily.  
MQ2 had limited or third-party ImGui support.

### Macro Compatibility

Most `.mac` macros written for MQ2 will run on MQ Next with little or no modification.  
Differences arise around:
- Deprecated TLO members that were renamed
- Plugin-specific commands that changed

## Migration Notes

### From MQ2 to MQ Next

1. **Reinstall fresh** — do not copy MQ2 plugin DLLs into MQ Next; they are not compatible.
2. **Macros** — test existing `.mac` files; most will work, but check for deprecated members.
3. **INI files** — MQ Next reads many of the same INI locations; verify paths haven't shifted.
4. **Plugin replacements** — many MQ2 plugins have MQ Next equivalents; check the [Plugins](Plugins.md) page.
5. **Lua scripts** — new in MQ Next; no migration needed, just start writing.

### Identifying Your Version

```
/mqversion
```

MQ Next reports a version string like `MacroQuest (version) Built: <date>`.

## Which Should I Use?

- If you are starting fresh: **use MQ Next**.
- If you are on a legacy server setup that only supports MQ2: stay with MQ2 but plan migration.
- MQ2 is no longer actively maintained and will fall further behind as EQ patches.
