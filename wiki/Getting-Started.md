# Getting Started

This page is a practical onboarding runbook with every behavior tied to official MacroQuest docs.

## 1) Prerequisite checklist

Before you install or run anything, confirm:

- [ ] **You are in a supported client/server context.** MacroQuest docs describe Live/Test workflows and a separate Emu workflow (`eqlib` branch + build config), and note that MQ is supported on *some* emulated servers. See: [Building MacroQuest](https://docs.macroquest.org/main/building/) and [EQEmu](https://docs.macroquest.org/main/other-applications/eqemu/).
- [ ] **You have the runtime launcher available.** MacroQuest starts by running `MacroQuest.exe` (the launcher/injector). See: [MacroQuest Launcher](https://docs.macroquest.org/main/macroquest-launcher/).
- [ ] **If you build from source, required build/runtime prerequisites are installed first.** Docs require Visual Studio (including `MSVC v143 - VS2022 c++ x86/x64 build tools`) and Git before building. See: [Building MacroQuest](https://docs.macroquest.org/main/building/).
- [ ] **You understand stop/unload behavior up front.** Docs define `/unload` as unloading MacroQuest and `/endmacro` as stopping the current macro. See: [/unload](https://docs.macroquest.org/reference/commands/unload/) and [/endmacro](https://docs.macroquest.org/reference/commands/endmacro/).

## 2) Install/update path summary (official docs)

Choose the path that matches how you run MQ:

### Path A: Run an existing build

1. Start `MacroQuest.exe` to inject/start MQ. See: [MacroQuest Launcher](https://docs.macroquest.org/main/macroquest-launcher/).
2. You can start it before or after EverQuest; docs note that if started after EQ, injection may take a few seconds to appear in-game. See: [Main Getting Started](https://docs.macroquest.org/main/).

### Path B: Build from source, then run

1. Install prerequisites (Visual Studio toolchain + Git). See: [Building MacroQuest](https://docs.macroquest.org/main/building/).
2. Clone/update source and submodules. See the **Check Out the Latest Source Code** and **Updating an Existing Checkout** sections: [Building MacroQuest](https://docs.macroquest.org/main/building/).
3. Build for the correct target (Live/Test x64 or Emu Win32), then run `MacroQuest.exe` from build output. See: [Building MacroQuest](https://docs.macroquest.org/main/building/).

## 3) First-run verification (in-game)

Run these in an EQ client where MQ was injected:

1. **Check command pipeline works**
   - Command: `/echo MQ is loaded`
   - Expected: text is echoed to the MQ console/chat output as documented for `/echo`. See: [/echo](https://docs.macroquest.org/reference/commands/echo/).

2. **Check plugin system responds**
   - Command: `/plugin list`
   - Expected: a list of currently loaded plugins (per `/plugin` description). See: [/plugin](https://docs.macroquest.org/reference/commands/plugin/).

3. **(Optional) Validate plugin load/unload cycle safely**
   - Commands:
     - `/plugin mq2fps load noauto`
     - `/plugin mq2fps unload noauto`
   - Expected: plugin can be loaded/unloaded in-session, and `noauto` avoids writing persistence to `[Plugins]` in `MacroQuest.ini`. See: [/plugin](https://docs.macroquest.org/reference/commands/plugin/) and [MacroQuest.ini](https://docs.macroquest.org/main/macroquest.ini/).

## 4) Minimal safe starter setup

Keep your first session intentionally conservative.

### A) Basic plugin load checks

- Use `/plugin list` to review what is already active. See: [/plugin](https://docs.macroquest.org/reference/commands/plugin/).
- If testing any plugin, prefer explicit load/unload while learning:
  - `/plugin <name> load noauto`
  - `/plugin <name> unload noauto`
- The `noauto` flag is useful for testing because docs state normal plugin loads persist to `MacroQuest.ini`. See: [/plugin](https://docs.macroquest.org/reference/commands/plugin/).

### B) One emergency stop bind

Create a panic bind that immediately stops macros:

```text
/custombind add panicstop
/custombind set panicstop /endmacro
/bind panicstop ctrl+shift+pause
```

- `/custombind` creates a command bind, and `/bind` assigns the key combo. See: [/custombind](https://docs.macroquest.org/plugins/core-plugins/custombinds/custombind/) and [/bind](https://docs.macroquest.org/reference/commands/bind/).
- `/endmacro` stops the currently running macro. See: [/endmacro](https://docs.macroquest.org/reference/commands/endmacro/).

### C) Disable automation quickly

If behavior is not what you expect:

1. Stop active macro: `/endmacro` ([docs](https://docs.macroquest.org/reference/commands/endmacro/)).
2. Unload the specific plugin under test: `/plugin <name> unload noauto` ([docs](https://docs.macroquest.org/reference/commands/plugin/)).
3. Unload MQ entirely for that EQ session: `/unload` ([docs](https://docs.macroquest.org/reference/commands/unload/)).

## If this fails

Go straight to [[Troubleshooting]] for a fast triage checklist.
