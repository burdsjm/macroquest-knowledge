# Macro Patterns

Reusable macro patterns inspired by common MQ scripting practice.

## Pulling loop

- Acquire eligible target.
- Validate path/range/aggro constraints.
- Execute pull ability.
- Return to camp and hand off to assist logic.

**Source links**
- `/mqtarget`: https://docs.macroquest.org/reference/commands/mqtarget/
- `/target`: https://docs.macroquest.org/reference/commands/target/
- `/delay`: https://docs.macroquest.org/reference/commands/delay/

## Buff maintenance loop

- Iterate configured buff list.
- Check duration threshold.
- Cast/refresh with cooldown and mana gates.
- Skip while in combat when configured.

**Source links**
- `/cast`: https://docs.macroquest.org/reference/commands/cast/
- `/delay`: https://docs.macroquest.org/reference/commands/delay/
- `/ini`: https://docs.macroquest.org/reference/commands/ini/

## Healing loop

- Priority queue by role and HP threshold.
- Emergency branch first, then efficiency branch.
- Debounce repeated casts to avoid spam.

**Source links**
- `/cast`: https://docs.macroquest.org/reference/commands/cast/
- `/delay`: https://docs.macroquest.org/reference/commands/delay/
- `/echo`: https://docs.macroquest.org/reference/commands/echo/

## State machine approach

Use explicit states for reliability:

- `IDLE`
- `PREP`
- `ENGAGE`
- `RECOVER`
- `ERROR`

Store current state in one variable and log transitions.

### Complete state-machine skeleton (copy/paste-ready)

**Assumptions**
- You will replace placeholder actions (targeting, combat, recovery) with your class logic.
- This macro is responsible for its own stop condition and timeout.

```mq2
| state_machine_skeleton.mac
#turbo 40

Sub Main
  /declare state string outer IDLE
  /declare nextState string local IDLE
  /declare loops int local 0
  /declare maxLoops int local 200          | hard stop safety

  /echo [SM] Start in state=${state}

  /while (${Macro.Name.NotEqual[NULL]} && ${loops} < ${maxLoops})
    /varcalc loops ${loops}+1
    /varset nextState ${state}

    /if (${state.Equal[IDLE]}) {
      /echo [SM] IDLE -> PREP (work found)
      /varset nextState PREP
    }
    /elseif (${state.Equal[PREP]}) {
      /if (!${Me.Combat}) {
        /echo [SM] PREP -> ENGAGE (ready)
        /varset nextState ENGAGE
      } else {
        /echo [SM] PREP -> ERROR (unexpected combat during prep)
        /varset nextState ERROR
      }
    }
    /elseif (${state.Equal[ENGAGE]}) {
      /if (${Me.PctHPs} < 35) {
        /echo [SM] ENGAGE -> RECOVER (low HP)
        /varset nextState RECOVER
      } elseif (!${Target.ID}) {
        /echo [SM] ENGAGE -> IDLE (target gone)
        /varset nextState IDLE
      } else {
        /echo [SM] ENGAGE -> ENGAGE (continue)
      }
    }
    /elseif (${state.Equal[RECOVER]}) {
      /if (${Me.PctHPs} > 70) {
        /echo [SM] RECOVER -> IDLE (stabilized)
        /varset nextState IDLE
      } else {
        /echo [SM] RECOVER -> RECOVER (healing)
      }
    }
    /elseif (${state.Equal[ERROR]}) {
      /echo [SM] ERROR -> IDLE (reset)
      /varset nextState IDLE
    }
    /else {
      /echo [SM] Unknown state='${state}' -> ERROR
      /varset nextState ERROR
    }

    /varset state ${nextState}
    /delay 2s                                | pacing + allows world state changes
  /endwhile

  /if (${loops} >= ${maxLoops}) /echo [SM] Stop: max loop safety reached.
  /echo [SM] End state=${state} loops=${loops}
  /endmacro
/return
```

**Stop criteria**
- Stops when `loops` reaches `maxLoops`.
- Stops manually with `/endmacro`.

**Expected output behavior**
- Emits transition logs on each pass (`[SM] CURRENT -> NEXT (reason)`).
- Ends with a summary line containing final state and loop count.

**Source links**
- `/macro`: https://docs.macroquest.org/reference/commands/macro/
- `/echo`: https://docs.macroquest.org/reference/commands/echo/
- `/delay`: https://docs.macroquest.org/reference/commands/delay/
- `/endmacro`: https://docs.macroquest.org/reference/commands/endmacro/
