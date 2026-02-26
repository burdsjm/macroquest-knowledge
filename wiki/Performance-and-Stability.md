# Performance and Stability

Tips for running MacroQuest with minimal overhead and maximum reliability.

## General Principles

1. **Only load plugins you use.** Every loaded plugin adds hooks that run on every game frame.
2. **Keep macros and scripts running only when needed.** Long-running idle loops consume resources.
3. **Use adequate delays.** Tight loops without delays can spike CPU and destabilize the client.
4. **Keep MQ up to date.** Outdated builds can crash after EQ patches.

## Plugin Performance

### Audit Loaded Plugins

```
/plugins
```

Remove any plugins from `macroquest.ini → [Plugins]` that you don't actively need.

### OnPulse Impact

Every plugin's `OnPulse` hook runs every game frame (~60 FPS). A plugin doing heavy work in `OnPulse` can tank performance. Signs of a misbehaving plugin:
- CPU usage spikes when the plugin is loaded
- FPS drops noticeably in-game

To identify: unload plugins one at a time while monitoring CPU/FPS.

## Macro Performance

### Use Adequate Delays

A macro with no delay will spin as fast as possible:

```
; BAD — tight loop with no delay
/while (TRUE) {
  /echo checking...
}
```

```
; GOOD — 250ms pause per iteration
/while (TRUE) {
  /echo checking...
  /delay 25
}
```

For most automation tasks, a delay of `/delay 10` (about 1 second) is sufficient.

### Minimize TLO Evaluations in Loops

TLO reads involve parsing and memory lookups. Cache values you read repeatedly:

```
; Less efficient — reads TLO every iteration
/while (${Me.PctHPs} > 20) {
  /delay 10
}

; Slightly more efficient for complex conditions — declare once
/declare hp int local
/varset hp ${Me.PctHPs}
/while (${hp} > 20) {
  /delay 10
  /varset hp ${Me.PctHPs}
}
```

## Lua Performance

### Use `mq.delay()` in Main Loops

```lua
-- BAD — busy loop
while true do
  -- logic
end

-- GOOD — yields control each iteration
while running do
  mq.doevents()
  -- logic
  mq.delay(100)   -- 100ms pause
end
```

### Avoid Blocking the Game Thread

Long synchronous operations in Lua block the game frame. Use delays with condition functions:

```lua
-- BAD — sleeps for a fixed 10s even if done sooner
mq.delay(10000)

-- GOOD — exits as soon as condition is true
mq.delay(10000, function() return not mq.TLO.Me.Casting() end)
```

## Stability Best Practices

### Update Regularly

- Update MQ and all plugins after each EQ patch.
- Breaking changes are common after patches; running an outdated MQ risks crashes.

### Keep Navmeshes Current

Outdated MQ2Nav meshes can cause crashes or hangs during pathfinding. Regenerate or download updated meshes after major zone changes.

### Avoid Untrusted Plugins

A plugin DLL has full access to the EQ process. Only install plugins from trusted sources (official MQ GitHub, well-known community sources).

### Back Up INI Files

Before major updates, copy your `macroquest.ini`, `MQ2Map.ini`, and other plugin INI files. Updates can sometimes reset settings.

### Run MQ Before EQ

Always start MacroQuest before launching EverQuest. Injecting after login can sometimes cause instability.

### One MQ Instance Per EQ Instance

Do not share a single MQ install across multiple simultaneous EQ clients. Each client should have its own MQ process or use the multi-instance feature.

## Memory and Resource Tips

- The MQ2Map plugin adds overhead proportional to zone spawn count. In very large zones, this can increase memory and CPU usage.
- MQ2Nav mesh loading takes a few seconds on zone. This is normal.
- Lua scripts with `mq.imgui.init` register a render callback that runs every frame — keep the ImGui callback fast.

## Crash Recovery

If EQ crashes while MQ is running:
1. Kill any lingering `MacroQuest.exe` processes.
2. Delete `crashdump/` files if disk space is a concern.
3. Check the MQ console log (written to `logs/` folder) for the last events before crash.
4. If crashes are reproducible, try disabling plugins or updating to the latest build.
5. Report persistent crashes with steps to reproduce on the [MQ GitHub Issues](https://github.com/macroquest/macroquest/issues) page.

## See Also

- [Troubleshooting](Troubleshooting.md)
- [Plugins](Plugins.md)
- [Macros Basics](Macros-Basics.md)
