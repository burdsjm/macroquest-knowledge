# Plugins

## Curated commonly used plugin list (docs.macroquest.org)

> Use `/plugin list` to inspect current state, and prefer `/plugin <name> load noauto` while testing so you don't unintentionally persist changes to `MacroQuest.ini`.

| Plugin | Capability added | Optional vs commonly required | Key command examples | Caveats / dependencies |
|---|---|---|---|---|
| `mq2eqbc` | Cross-character chat/control bridge so one client can coordinate commands and messaging with others. | Optional, but commonly required for multibox command routing. | `/plugin mq2eqbc load`<br>`/bccmd connect`<br>`/bc //assist`<br>`/bct Cleric //cast 1` | Requires EQBC server/session setup before broadcast commands are useful; command fan-out can create accidental spam if aliases are broad. |
| `mq2melee` | Automated melee skill/disc usage and combat behavior toggles. | Optional, but very common for melee classes. | `/plugin mq2melee load`<br>`/melee plugin=1`<br>`/melee stickbreak=on` | Settings are class/role sensitive; aggressive defaults can conflict with manual control or other combat automation plugins. |
| `mq2moveutils` | Movement helpers and camp/stick/follow primitives for macro/plugin workflows. | Optional, but commonly required by movement-heavy workflows. | `/plugin mq2moveutils load`<br>`/stick 10`<br>`/moveto loc 123 456`<br>`/makecamp` | Can fight with manual movement input; ensure scripts clean up (`/stick off`, `/makecamp off`) on failure paths. |
| `mq2advpath` | Path recording/playback and path-based following. | Optional; common in teams that automate travel. | `/plugin mq2advpath load`<br>`/record mypath`<br>`/play mypath`<br>`/afollow spawn Tank` | Best results when nav data/path assumptions are current; path playback can fail in changed geometry or scripted zone states. |
| `mq2cast` | Higher-level spell casting helpers (mem/cast/interruption utilities). | Optional, but commonly used in caster automation/macros. | `/plugin mq2cast load`<br>`/casting "Complete Heal"`<br>`/interrupt`<br>`/memorize "Spell Name" gem1` | Spell-gem and timing assumptions vary by class/latency; validate interrupt/recast behavior after patch day. |
| `mq2twist` | Bard song twisting/sequencing controls. | Optional; effectively required for bard twist automation. | `/plugin mq2twist load`<br>`/twist 1 2 3 4`<br>`/sing 1`<br>`/stoptwist` | Bard-only value; can conflict with manual song control or other bard automation if both issue cast/song commands. |
| `mq2map` (core `map` plugin) | Extended map overlays, filters, labels, and interaction commands. | Optional, but very commonly used for awareness/debugging. | `/plugin map load`<br>`/mapshow npc`<br>`/mapfilter target on`<br>`/highlight id 1234` | High marker/filter density can reduce clarity/performance; keep filters intentional per activity. |
| `mq2hud` (core `hud` plugin) | Configurable on-screen HUD elements (text/data overlays). | Optional; common for status-at-a-glance UI setups. | `/plugin hud load`<br>`/loadhud MyHUD.cfg`<br>`/classhud`<br>`/zonehud` | Depends on valid HUD config syntax and paths; noisy HUDs can hurt readability/performance on lower-end setups. |
| `mq2autologin` (core `autologin`) | Login profile automation and character/server switching helpers. | Optional; commonly required in multi-account workflows. | `/plugin autologin load`<br>`/loginchar <profile>`<br>`/switchchar <name>`<br>`/switchserver <server>` | Credential/profile management must be kept accurate; be careful with unattended reconnect behavior on unstable sessions. |
| `mq2itemdisplay` (core `itemdisplay`) | Enhanced item window metadata/notes and item-related helpers. | Optional, but common for loot/planning workflows. | `/plugin itemdisplay load`<br>`/inote add "keep for tradeskills"` | Primarily UI/inspection value; ensure notes/workflow assumptions are synced across characters if you rely on them operationally. |

## Per-plugin subpage convention

Create one page per major plugin, for example:

- `Plugin-MyPlugin`

Recommended sections:

1. Overview
2. Install/load
3. Configuration
4. Common commands
5. Troubleshooting
6. Compatibility notes

## Operational tips

- Load only what you need.
- Note startup dependencies/order.
- Track plugin-specific crashes in [[Troubleshooting]].
