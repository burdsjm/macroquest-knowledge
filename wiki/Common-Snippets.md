# Common Snippets

Ready-to-use copy-paste recipes for MacroQuest macros and Lua scripts.

---

## Macro Snippets (`.mac`)

### Check If Target Exists

```
/if (!${Target.ID}) {
  /echo No target selected
  /return
}
```

### Cast a Spell and Wait

```
/cast "Spell Name"
/delay 5
/delay 100 !${Me.Casting}
```

### Wait for Mana

```
/sit
/delay 600 ${Me.PctMana} >= 90
/stand
```

### Meditate to Full Mana

```
Sub MedToFull
  /if (${Me.PctMana} >= 100) /return
  /sit
  /delay 1200 ${Me.PctMana} >= 99
  /stand
/return
```

### Target Nearest NPC

```
/target npc next
```

### Target by Name

```
/target "Guard Gavin"
/delay 20 ${Target.ID}
```

### Navigate to Target

```
/nav target
/delay 500 !${Navigation.Active}
```

### Navigate to Location

```
/nav loc -500 200 -15
/delay 500 !${Navigation.Active}
```

### Buff If Missing

```
/if (!${Me.Buff[Haste].ID}) {
  /cast "Haste"
  /delay 50 !${Me.Casting}
}
```

### Loot All Corpses Nearby

```
Sub LootCorpses
  /declare corpseID int local ${Spawn[corpse radius 30].ID}
  /while (${corpseID}) {
    /target id ${corpseID}
    /delay 10 ${Target.ID}
    /loot
    /delay 30
    /autoinventory
    /delay 10
    /varset corpseID ${Spawn[corpse radius 30 !id ${corpseID}].ID}
  }
/return
```

### Check Zone Name

```
/if (${Zone.ShortName.Equal[commons]}) {
  /echo I am in West Commons
}
```

### Say Something in Group

```
/gsay Pulling ${Target.Name} -- be ready!
```

### Print All Group Member HP

```
Sub PrintGroupHP
  /declare i int local 1
  /while (${i} <= ${Group.Members}) {
    /echo ${Group.Member[${i}].Name}: ${Group.Member[${i}].PctHPs}%
    /varcalc i ${i}+1
  }
/return
```

### Pause Until Out of Combat

```
/delay 600 !${Me.Combat}
```

### Interval Timer Using `/timer`

```
/declare CastTimer timer local 0
Sub Main
  /while (TRUE) {
    /doevents
    /if (${CastTimer} == 0) {
      /cast "Regen"
      /delay 50 !${Me.Casting}
      /varset CastTimer 600    ; ~60 seconds
    }
    /delay 1
  }
/return
```

---

## Lua Snippets

### Print Character Info

```lua
local mq = require('mq')
print(string.format('%s | Level %d | HP: %d%%',
  mq.TLO.Me.Name(),
  mq.TLO.Me.Level(),
  mq.TLO.Me.PctHPs()))
```

### Cast and Wait

```lua
local mq = require('mq')
local function castAndWait(spell)
  mq.cmdf('/cast "%s"', spell)
  mq.delay(500)
  mq.delay(10000, function() return not mq.TLO.Me.Casting() end)
end
castAndWait('Complete Heal')
```

### Wait for Mana

```lua
local mq = require('mq')
mq.cmd('/sit')
mq.delay(60000, function() return mq.TLO.Me.PctMana() >= 90 end)
mq.cmd('/stand')
```

### Buff Check

```lua
local mq = require('mq')
local function hasBuff(name)
  return mq.TLO.Me.Buff(name).ID() ~= nil
end

if not hasBuff('Haste') then
  mq.cmd('/cast "Haste"')
  mq.delay(5000, function() return not mq.TLO.Me.Casting() end)
end
```

### Navigate to Target

```lua
local mq = require('mq')
mq.cmd('/nav target')
mq.delay(30000, function() return not mq.TLO.Navigation.Active() end)
```

### Simple Main Loop

```lua
local mq = require('mq')
local running = true
mq.bind('/stopit', function() running = false end)

while running do
  mq.doevents()
  -- your logic here
  mq.delay(250)
end
```

### Send Command to All Group Members (DanNet)

```lua
local mq = require('mq')
mq.cmd('/dnet group /stand')
mq.delay(500)
```

### ImGui Toggle Window

```lua
local mq    = require('mq')
local imgui = require('ImGui')
local open  = true

mq.imgui.init('SnippetWindow', function()
  open, _ = imgui.Begin('Snippet Window', open)
  if open then
    imgui.Text(string.format('HP: %d%%', mq.TLO.Me.PctHPs()))
  end
  imgui.End()
end)

while open do
  mq.doevents()
  mq.delay(100)
end
```

---

## See Also

- [Macros Basics](Macros-Basics.md)
- [Macro Patterns](Macro-Patterns.md)
- [Lua](Lua.md)
- [Data Types and TLO](Data-Types-and-TLO.md)
