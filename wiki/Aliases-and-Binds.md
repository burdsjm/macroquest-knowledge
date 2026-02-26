# Aliases and Binds

## Aliases

Aliases allow you to create shorthand commands that expand to longer command strings.

### Creating an Alias

```
/alias /<shortname> /<full command string>
```

**Example:**
```
/alias /gs /gsay
/alias /nb /nav stop
/alias /tg /target
```

Aliases are stored in `macroquest.ini` under `[Aliases]`.

### Removing an Alias

```
/alias /<shortname> delete
```

### Listing Aliases

```
/alias list
```

### Persistent Aliases via INI

You can add aliases directly to `macroquest.ini`:

```ini
[Aliases]
/gs=/gsay
/nb=/nav stop
/tg=/target
```

## Binds (Key Bindings)

Binds map a key press to a MQ command or macro call.

### Creating a Bind

```
/bind <bindname> <key>
```

**Example — bind the F9 key to pause macro:**
```
/bind mqpause F9
```

### Listing Binds

```
/bind list
```

### Common Bindable Actions

| Bind Name | Default Key | Description |
|-----------|------------|-------------|
| `mqpause` | End | Pause / resume macro |
| `mq2nav_pause` | — | Pause MQ2Nav navigation |
| `mq2nav_stop` | — | Stop MQ2Nav navigation |
| `autoinventory` | — | Auto-inventory loot |

### Plugin-Defined Binds

Plugins can register their own bind names. Check each plugin's documentation for bindable actions.

### Custom Macro Binds

You can bind a key to run an MQ command, including launching macros:

```
/bind add myheal F10
/notify myheal activated /cast "Complete Heal"
```

Or more practically, define a bind in your macro using the `AddBind` function.

## Bind Modifiers

Key names support modifiers:

| Modifier | Example |
|----------|---------|
| Shift | `Shift+F1` |
| Ctrl | `Ctrl+F1` |
| Alt | `Alt+F1` |
| Ctrl+Shift | `Ctrl+Shift+F1` |

## Tips

- Aliases persist across sessions if stored in the INI file.
- Binds can conflict with EverQuest's own key bindings — choose keys EQ doesn't use.
- Use `/alias list` and `/bind list` to audit what you have configured.
- Aliases can chain MQ commands: `/alias /gohome /nav loc 0 0 0|/gsay Heading home!`
