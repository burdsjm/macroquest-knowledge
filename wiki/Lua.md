# Lua Scripting in MacroQuest

MQ Next includes a built-in Lua runtime. Lua scripts provide a more modern, expressive alternative to `.mac` macros.

## Running a Lua Script

Place `.lua` files in the `lua/` subfolder of your MQ installation:

```
/lua run myscript
/lua run myscript arg1 arg2
```

Stop a running script:
```
/lua stop myscript
```

List running scripts:
```
/lua list
```

## Script Entry Point

A Lua script is just a `.lua` file. Execution starts at the top level:

```lua
local mq = require('mq')

mq.cmd('/echo Hello from Lua!')
```

## The `mq` Module

The `mq` module is the primary interface to MacroQuest.

```lua
local mq = require('mq')
```

### Sending Commands

```lua
mq.cmd('/echo Hello World')
mq.cmdf('/echo My name is %s', mq.TLO.Me.Name())
```

### Accessing TLOs

All TLOs are available under `mq.TLO.*` and must be **called as functions** (with `()`) to get their value:

```lua
local name   = mq.TLO.Me.Name()
local pctHP  = mq.TLO.Me.PctHPs()
local target = mq.TLO.Target.Name()

print(string.format('%s is at %d%% health', name, pctHP))
```

### Delays

```lua
mq.delay(1000)            -- wait 1000 ms
mq.delay(5000, function() return mq.TLO.Me.PctHPs() > 80 end)
-- wait up to 5 seconds OR until HP > 80%
```

### Events / Callbacks

```lua
mq.event('LowHP', 'Your health is low#*#', function()
  mq.cmd('/echo Healing myself!')
  mq.cmd('/cast "Complete Heal"')
end)

-- In your main loop, call this to process pending events:
mq.doevents()
```

## ImGui UI (in-game windows)

```lua
local mq      = require('mq')
local imgui   = require('ImGui')

local open = true

local function drawUI()
  open, _ = imgui.Begin('My Window', open)
  if open then
    imgui.Text('Hello from ImGui!')
    if imgui.Button('Cast Haste') then
      mq.cmd('/cast "Haste"')
    end
  end
  imgui.End()
end

mq.imgui.init('MyWindow', drawUI)

while open do
  mq.doevents()
  mq.delay(100)
end
```

## Main Loop Pattern

```lua
local mq = require('mq')

local running = true

-- Register a bind to stop the script
mq.bind('/stopscript', function() running = false end)

while running do
  mq.doevents()

  local pct = mq.TLO.Me.PctHPs()
  if pct < 50 then
    mq.cmd('/cast "Complete Heal"')
    mq.delay(5000, function() return not mq.TLO.Me.Casting() end)
  end

  mq.delay(250)
end
```

## Requiring Other Lua Files

Place shared libraries in `lua/` and require them:

```lua
local utils = require('myutils')   -- loads lua/myutils.lua
```

## Common Patterns

### Safe Cast

```lua
local function safeCast(spellName)
  if mq.TLO.Me.Casting() then return end
  if not mq.TLO.Target.ID() then return end
  mq.cmdf('/cast "%s"', spellName)
  mq.delay(500)
  mq.delay(10000, function() return not mq.TLO.Me.Casting() end)
end
```

### Buff Check

```lua
local function needsBuff(buffName)
  return not mq.TLO.Me.Buff(buffName).ID()
end

if needsBuff('Haste') then
  safeCast('Haste')
end
```

### Wait for Navigation

```lua
mq.cmd('/nav target')
mq.delay(30000, function() return not mq.TLO.Navigation.Active() end)
```

## Lua vs Macros

| Feature | `.mac` Macros | Lua |
|---------|--------------|-----|
| Syntax | MQ-specific | Standard Lua 5.4 |
| Libraries | Limited | Full Lua stdlib + MQ modules |
| ImGui | No | Yes |
| Coroutines | No | Yes |
| Error handling | Limited | `pcall` / `xpcall` |
| Performance | Adequate | Better for complex logic |
| Community scripts | Many | Growing rapidly |

## See Also

- [Macro Patterns](Macro-Patterns.md)
- [Data Types and TLO](Data-Types-and-TLO.md)
- [Common Snippets](Common-Snippets.md)
