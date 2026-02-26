# macroquest-knowledge

A text knowledge base of [MacroQuest](https://macroquest.org) documentation, built for linking to GPT and other AI models.

## Contents

The `docs/` directory contains the complete MacroQuest documentation mirrored from the official
[macroquest/docs](https://github.com/macroquest/docs) repository in plain Markdown format:

| Directory | Description |
|-----------|-------------|
| `docs/reference/top-level-objects/` | 65+ TLO (Top Level Object) definitions — `Me`, `Target`, `Spawn`, `Spell`, `Group`, etc. |
| `docs/reference/data-types/` | 90+ data type definitions — `spawn`, `spell`, `item`, `character`, etc. |
| `docs/reference/commands/` | 140+ slash command and macro command references |
| `docs/reference/general/` | Body types, animations, spawn search parameters |
| `docs/macros/` | Macro scripting guides — variables, flow control, events, subroutines |
| `docs/macros/gallery/` | 30+ example macros |
| `docs/lua/` | Lua scripting guides — events, actors, spawn searching |
| `docs/plugins/` | Core and community plugin documentation |
| `docs/main/` | Getting started, building, features, configuration |
| `docs/ai_helpers/` | Pre-built AI prompts for Claude and other models |

## Updating the Knowledge Base

To refresh the docs from the upstream repository, run:

```bash
python3 scripts/fetch_docs.py
```

This downloads all Markdown files from [macroquest/docs](https://github.com/macroquest/docs)
on GitHub into the `docs/` directory.  No authentication required.

## Using with AI Models

Point your AI model, GPT, or RAG pipeline at the `docs/` directory (or a subdirectory).
The files are plain Markdown and are straightforward to parse or chunk.

For a pre-built Claude system prompt, see `docs/ai_helpers/claude/`.
