# Macro Patterns

Common patterns for building reliable MacroQuest macros.

## State Machine Pattern

The most robust macro architecture uses an explicit state variable to control flow. This prevents nested conditionals and makes it easy to add new states.

```
Sub Main
  /declare State string global "Idle"

  /while (TRUE) {
    /delay 1
    /doevents

    /if (${State.Equal[Idle]})     /call StateIdle
    /if (${State.Equal[Moving]})   /call StateMoving
    /if (${State.Equal[Fighting]}) /call StateFighting
    /if (${State.Equal[Looting]})  /call StateLooting
  }
/return

Sub StateIdle
  /if (${SpawnCount[npc radius 50]}) {
    /varset State Fighting
  }
/return

Sub StateMoving
  ; navigation logic
  /if (!${Navigation.Active}) {
    /varset State Idle
  }
/return

Sub StateFighting
  /if (!${Me.Combat}) {
    /varset State Looting
  }
  ; combat logic here
/return

Sub StateLooting
  ; loot logic
  /varset State Idle
/return
```

## Pulling Pattern

```
Sub PullTarget
  ; Verify we have a valid pull target
  /if (!${Target.ID}) /return

  /echo Pulling ${Target.Name}

  ; Move to pull range
  /nav target distance=30
  /delay 300 !${Navigation.Active}

  ; Open with a ranged/aggro ability
  /cast "Taunt"
  /delay 30 !${Me.Casting}

  ; Return to camp
  /nav loc ${Camp.Y} ${Camp.X} ${Camp.Z}
  /delay 500 !${Navigation.Active}
/return
```

## Buffing Loop Pattern

```
Sub BuffGroup
  /declare i int local 1

  /while (${i} <= ${Group.Members}) {
    /target ${Group.Member[${i}].Name}
    /delay 10 ${Target.ID}

    /if (!${Target.Buff[Haste].ID}) {
      /cast "Haste"
      /delay 50 !${Me.Casting}
    }

    /if (!${Target.Buff[Strength].ID}) {
      /cast "Strength"
      /delay 50 !${Me.Casting}
    }

    /varcalc i ${i}+1
  }

  /target ${Me.Name}
/return
```

## Healing Loop Pattern

```
#event LowHP "You are low on health#*#"

Sub Event_LowHP
  /echo Healing triggered by event
  /call CastHeal ${Me.Name}
/return

Sub CastHeal(HealTarget)
  /target ${HealTarget}
  /delay 10 ${Target.ID}
  /cast "Complete Heal"
  /delay 100 !${Me.Casting}
/return

Sub Main
  /while (TRUE) {
    /doevents

    ; Proactive heal check
    /if (${Me.PctHPs} < 60) /call CastHeal ${Me.Name}

    ; Group heal check
    /declare i int local 1
    /while (${i} <= ${Group.Members}) {
      /if (${Group.Member[${i}].PctHPs} < 50) {
        /call CastHeal ${Group.Member[${i}].Name}
      }
      /varcalc i ${i}+1
    }

    /delay 10
  }
/return
```

## Camp / Return-to-Camp Pattern

```
Sub SetCamp
  /declare CampX float global ${Me.X}
  /declare CampY float global ${Me.Y}
  /declare CampZ float global ${Me.Z}
  /echo Camp set at ${CampY} ${CampX} ${CampZ}
/return

Sub ReturnToCamp
  /if (${Math.Distance[${Me.Y},${Me.X}:${CampY},${CampX}]} > 20) {
    /nav loc ${CampY} ${CampX} ${CampZ}
    /delay 300 !${Navigation.Active}
  }
/return
```

## Mana Conservation Pattern

```
Sub WaitForMana(MinPct)
  /if (${Me.PctMana} < ${MinPct}) {
    /echo Waiting for mana (${Me.PctMana}% / need ${MinPct}%)
    /sit
    /delay 10 ${Me.PctMana} >= ${MinPct}
    /stand
  }
/return
```

Usage:
```
/call WaitForMana 80
```

## Safe Cast Pattern

Checks that a spell is ready, the target is valid, and you are not already casting:

```
Sub SafeCast(SpellName)
  /if (${Me.Casting}) /return
  /if (!${Target.ID}) /return
  /if (!${Me.Gem[${SpellName}]}) {
    /echo ${SpellName} is not memorized!
    /return
  }
  /cast "${SpellName}"
  /delay 5
  /delay 100 !${Me.Casting}
/return
```

## Tips

- Always use `/doevents` inside main loops to process `#event` handlers.
- Use `/delay 1` (minimum delay) in tight loops to avoid locking the client.
- Store camp coordinates globally so subroutines can reference them.
- State machines scale better than deeply nested if/else trees.
- See [Common Snippets](Common-Snippets.md) for ready-to-use fragments.
