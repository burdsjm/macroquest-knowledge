# Macros Basics

## Building blocks

- Subroutines
- Variables and scope
- Conditionals
- Loops and waits
- Events and parsing

## Starter macro workflow

1. Define objective (single, testable behavior).
2. Write a tiny command loop.
3. Add guardrails (distance, HP threshold, timeout).
4. Add debug echoes.
5. Refactor into reusable subroutines.

## Minimal macro: hello + loop + stop condition

**Assumptions**
- You are in game with MacroQuest loaded.
- You can run `/macro basics_example`.

```mq2
| basics_example.mac
#turbo 40

Sub Main
  /declare i int local 0                   | variable declaration (macro variable)
  /declare maxIterations int local 5       | explicit stop criterion

  /echo [Basics] Hello from macro startup. | /echo command

  /while (${i} < ${maxIterations})         | loop construct (/while)
    /echo [Basics] Tick ${i}               | visible loop output
    /delay 1s                              | wait command (/delay)
    /varcalc i ${i}+1                      | numeric update
  /endwhile                                | loop terminator

  /echo [Basics] Done after ${i} iterations.
  /endmacro                                | explicit macro lifecycle stop
/return
```

**Stop criteria**
- Stops after `maxIterations` iterations.
- Also stops immediately if you manually run `/endmacro`.

**Expected output behavior**
- One startup line, five tick lines, and one completion line in MQ chat/output.

**Source links**
- `/macro`: https://docs.macroquest.org/reference/commands/macro/
- `/echo`: https://docs.macroquest.org/reference/commands/echo/
- `/delay`: https://docs.macroquest.org/reference/commands/delay/
- `/endmacro`: https://docs.macroquest.org/reference/commands/endmacro/

## Guarded action example (precondition re-check after waits)

**Assumptions**
- You are using a valid spell gem index in `${Me.Gem[1]}`.
- You have a valid offensive target before the action starts.

```mq2
| guarded_cast.mac
Sub Main
  /if (!${Target.ID}) {
    /echo [Guard] No target. Stopping.
    /endmacro
  }

  /if (${Target.Distance} > 100) {
    /echo [Guard] Target too far to start. Stopping.
    /endmacro
  }

  /echo [Guard] Preconditions met. Waiting for cast window...
  /delay 2s ${Me.SpellReady[${Me.Gem[1]}]}  | wait until ready, but time can pass

  | Re-check ALL critical assumptions after wait:
  /if (!${Target.ID}) {
    /echo [Guard] Target changed/lost during wait. Abort safely.
    /endmacro
  }

  /if (${Target.Distance} > 100) {
    /echo [Guard] Target moved out of range during wait. Abort safely.
    /endmacro
  }

  /echo [Guard] Safe to act now.
  /cast 1
/return
```

**Stop criteria**
- Stops on missing target or out-of-range target both before and after wait.
- Stops if manually ended via `/endmacro`.

**Expected output behavior**
- Prints guard status lines and either exits safely or reaches `/cast 1` once conditions still hold.

**Source links**
- `/delay`: https://docs.macroquest.org/reference/commands/delay/
- `/cast`: https://docs.macroquest.org/reference/commands/cast/
- `/endmacro`: https://docs.macroquest.org/reference/commands/endmacro/

## Reliability principles

- Always include escape conditions.
- Assume target can change unexpectedly.
- Re-check preconditions after every wait.
- Keep macro state explicit and debuggable.

## Next

- [[Macro-Patterns]]
- [[Data-Types-and-TLO]]
