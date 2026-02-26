# Data Types and TLO

This page documents high-value MacroQuest top-level objects (TLOs) that appear in day-to-day scripts and loops.

## Commonly used TLOs

### `Me`

- **Type returned**: `character`
- **High-value members/methods**:
  - `${Me.Name}`
  - `${Me.Level}`
  - `${Me.Class.ShortName}`
  - `${Me.PctHPs}`
  - `${Me.PctMana}`
  - `${Me.PctEndurance}`
  - `${Me.CombatState}`
  - `${Me.Casting.ID}`
  - `${Me.Buff[<name|id>]}`
  - `${Me.XTarget}`
- **Example**:
  - `/if (${Me.PctHPs}<40) /multiline ; /echo Low HP ; /call EmergencyHeal`
- **Safe-check variant**:
  - `/if (${Me.Buff[Spirit of Wolf].ID}) /echo SOW is active`
- **Pitfalls**:
  - `Casting`, `Buff[]`, and similar members may be empty when not active; chaining without a guard fails.
  - Resource values can change between loop iterations, so avoid assuming a prior check is still true after delays.

### `Target`

- **Type returned**: `spawn` (or NULL when no target)
- **High-value members/methods**:
  - `${Target.ID}`
  - `${Target.Name}`
  - `${Target.CleanName}`
  - `${Target.Type}`
  - `${Target.Level}`
  - `${Target.Distance}`
  - `${Target.LineOfSight}`
  - `${Target.PctHPs}`
  - `${Target.Aggressive}`
  - `${Target.Buff[<name|id>]}`
- **Example**:
  - `/if (${Target.Type.Equal[NPC]} && ${Target.PctHPs}<20) /stand`
- **Safe-check variant**:
  - `/if (${Target.ID} && ${Target.Distance}<100 && ${Target.LineOfSight}) /attack on`
- **Pitfalls**:
  - `Target` can clear during zoning, corpse transitions, charm breaks, or rapid retargeting.
  - Deep access like `${Target.Buff[Foo].Duration}` can fail unless both target and buff exist.

### `Spawn[...]`

- **Type returned**: `spawn` from a query selector
- **High-value members/methods**:
  - `${Spawn[<search>].ID}`
  - `${Spawn[<search>].Name}`
  - `${Spawn[<search>].CleanName}`
  - `${Spawn[<search>].Type}`
  - `${Spawn[<search>].Distance}`
  - `${Spawn[<search>].Distance3D}`
  - `${Spawn[<search>].HeadingTo}`
  - `${Spawn[<search>].LineOfSight}`
  - `${Spawn[<search>].PctHPs}`
  - `${SpawnCount[<search>]}`
- **Example**:
  - `/if (${SpawnCount[npc radius 60 zradius 30]} > 2) /echo Multiple mobs nearby`
- **Safe-check variant**:
  - `/if (${Spawn[npc radius 80 targetable].ID}) /squelch /target id ${Spawn[npc radius 80 targetable].ID}`
- **Pitfalls**:
  - Search expressions can return NULL at any tick; always check `.ID` before additional members.
  - Repeating the same expensive query many times in one loop is slow; cache IDs or counts.

### `Group`

- **Type returned**: `group`
- **High-value members/methods**:
  - `${Group}`
  - `${Group.Members}`
  - `${Group.Leader.Name}`
  - `${Group.MainTank.Name}`
  - `${Group.MainAssist.Name}`
  - `${Group.Puller.Name}`
  - `${Group.Member[1].Name}`
  - `${Group.Member[1].PctHPs}`
  - `${Group.Member[1].Distance}`
  - `${Group.AnyoneMissing}`
- **Example**:
  - `/for i 1 to ${Group.Members}`
  - `  /if (${Group.Member[${i}].PctHPs}<60) /echo ${Group.Member[${i}].Name} needs healing`
  - `/next i`
- **Safe-check variant**:
  - `/if (${Group} && ${Group.Member[${i}].Name.NotEqual[NULL]}) /echo ${Group.Member[${i}].Name}`
- **Pitfalls**:
  - Group slots can be empty/reordered while inviting, zoning, or disbanding.
  - Named roles (`MainTank`, `MainAssist`) may be unset and should be treated as optional.

### `Zone`

- **Type returned**: `zone`
- **High-value members/methods**:
  - `${Zone.ID}`
  - `${Zone.Name}`
  - `${Zone.ShortName}`
  - `${Zone.Type}`
  - `${Zone.Gravity}`
  - `${Zone.SkyType}`
  - `${Zone.SafeY}`
  - `${Zone.SafeX}`
  - `${Zone.SafeZ}`
  - `${Zone.PlayerCount}`
- **Example**:
  - `/if (${Zone.ShortName.Equal[guildlobby]}) /echo In lobby logic block`
- **Safe-check variant**:
  - `/if (${Zone.ID} && ${Zone.PlayerCount}>0) /echo Zone is active`
- **Pitfalls**:
  - During zoning, values can be stale for a short period; gate logic until in-zone state is stable.
  - Cross-zone assumptions (paths, safe points, navigation mesh) must be revalidated after zone changes.

### `Window[...]`

- **Type returned**: `window` (UI element reference)
- **High-value members/methods**:
  - `${Window[<name>]}`
  - `${Window[<name>].Open}`
  - `${Window[<name>].Visible}`
  - `${Window[<name>].Enabled}`
  - `${Window[<name>].Child[<childname>]}`
  - `${Window[<name>].Child[<childname>].Text}`
  - `${Window[<name>].Child[<childname>].Tooltip}`
  - `${Window[<name>].X}`
  - `${Window[<name>].Y}`
  - `${Window[<name>].W}`
- **Example**:
  - `/if (${Window[MerchantWnd].Open}) /echo Merchant window is open`
- **Safe-check variant**:
  - `/if (${Window[GiveWnd]} && ${Window[GiveWnd].Open}) /notify GiveWnd GVW_Give_Button leftmouseup`
- **Pitfalls**:
  - UI windows may not exist for a skin/client state; verify existence before child access.
  - Child control names are exact and can vary between game updates or custom UIs.

## Defensive patterns

Use these reusable guards before deep member access in fast loops:

- **Guard target before chained reads**:
  - `/if (${Target.ID}) /varset tHP ${Target.PctHPs}`

- **Guard query results once, then reuse**:
  - `/declare addID int local ${Spawn[npc radius 80 targetable].ID}`
  - `/if (${addID}) /squelch /target id ${addID}`

- **Guard group slot access in loops**:
  - `/for i 1 to ${Group.Members}`
  - `  /if (${Group.Member[${i}].Name.NotEqual[NULL]} && ${Group.Member[${i}].Distance}<100) /echo ${Group.Member[${i}].Name}`
  - `/next i`

- **Split deep chains into validated steps**:
  - `/declare tid int local ${Target.ID}`
  - `/if (${tid}) {`
  - `  /declare hasSlow int local ${Target.Buff[Slow].ID}`
  - `  /if (!${hasSlow}) /call CastSlow`
  - `}`

- **Post-zone stabilization gate**:
  - `/if (${Zone.ID} && ${Me.ID} && !${Me.Casting.ID}) /call RunZoneLogic`

These patterns reduce null/invalid access errors and make loop behavior deterministic when combat state, UI state, and zone state are changing quickly.
