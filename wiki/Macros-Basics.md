# Macros Basics

## What Is a Macro?

A MacroQuest macro is a plain-text script file (`.mac` extension) that automates in-game actions using a simple scripting language built into MQ. Macros are stored in the `macros/` subdirectory of your MQ installation.

## Running a Macro

```
/macro <filename>
```

The `.mac` extension is optional:
```
/macro myheal
/macro myheal.mac
```

## Stopping a Macro

```
/endmacro
```

Or press the `End` key (default pause bind).

## Basic Syntax

### Structure

Every macro must have a `main` subroutine as its entry point:

```
Sub Main
  /echo Hello, World!
/return
```

### Subroutines

```
Sub MySubroutine
  /echo I am a subroutine
/return

Sub Main
  /call MySubroutine
/return
```

### Variables

```
Sub Main
  /declare myVar string local "Hello"
  /echo ${myVar}
/return
```

Variable types: `string`, `int`, `float`, `bool`, `timer`

Scopes: `local` (subroutine only), `global` (whole macro)

### Conditions (If / Else)

```
Sub Main
  /declare hp int local ${Me.PctHPs}
  /if (${hp} < 50) {
    /echo Low health!
  } else {
    /echo Health is fine.
  }
/return
```

### Loops (While)

```
Sub Main
  /declare i int local 0
  /while (${i} < 5) {
    /echo Loop iteration ${i}
    /varcalc i ${i}+1
  }
/return
```

### Delay

```
/delay 10               ; wait 10 ticks (~1 second)
/delay 30s              ; wait 30 seconds
/delay 5 ${Me.Casting}  ; wait up to 5 ticks or until done casting
```

## Using TLOs in Macros

Top Level Objects (TLOs) provide access to game data:

```
/echo My name: ${Me.Name}
/echo My HP: ${Me.PctHPs}%
/echo Target: ${Target.Name}
/echo In combat: ${Me.Combat}
```

See [Data Types and TLO](Data-Types-and-TLO.md) for a full reference.

## Events

Events let your macro react to chat or game events:

```
#event LowHP "Your health is low#*#"

Sub Event_LowHP
  /echo EVENT: Health is low!
/return

Sub Main
  /declare running bool local TRUE
  /while (${running}) {
    /delay 1
    /doevents
  }
/return
```

## Comments

```
; This is a single-line comment
```

## Including Other Files

```
#include mylib.inc
```

## Example: Simple Buff Check

```
Sub Main
  /if (!${Me.Buff[Haste].ID}) {
    /echo I do not have Haste — casting it
    /cast "Haste"
    /delay 30 !${Me.Casting}
  } else {
    /echo Haste is active
  }
/return
```

## Next Steps

- [Macro Patterns](Macro-Patterns.md) — common automation loops
- [Data Types and TLO](Data-Types-and-TLO.md) — full TLO reference
- [Common Snippets](Common-Snippets.md) — copy-paste recipes
