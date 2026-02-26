# Plugin Development

## Overview

MacroQuest plugins are Windows DLLs written in C++ that integrate with the MQ plugin API. They can add commands, TLOs, event hooks, and ImGui windows.

## Prerequisites

- Visual Studio 2022 (or later) with C++ Desktop Development workload
- CMake 3.20+
- A clone of [macroquest/macroquest](https://github.com/macroquest/macroquest)

## Project Setup

MQ Next uses CMake. The easiest way to create a plugin is to add it inside the MQ source tree.

### Directory Structure

```
macroquest/
  plugins/
    MyPlugin/
      CMakeLists.txt
      MQ2MyPlugin.cpp
```

### CMakeLists.txt

```cmake
add_mq_plugin(MQ2MyPlugin MQ2MyPlugin.cpp)
```

### Build

```bash
cmake --preset windows-release
cmake --build build/windows-release --target MQ2MyPlugin
```

The resulting `MQ2MyPlugin.dll` is placed in the MQ `plugins/` output folder.

## Plugin Skeleton

```cpp
// MQ2MyPlugin.cpp
#include <mq/Plugin.h>

// Plugin metadata
PLUGIN_VERSION(1.0);

// Called when MQ loads the plugin
PLUGIN_API void InitializePlugin()
{
    DebugSpewAlways("MQ2MyPlugin::InitializePlugin");
    // Register commands, TLOs, hooks here
}

// Called when MQ unloads the plugin
PLUGIN_API void ShutdownPlugin()
{
    DebugSpewAlways("MQ2MyPlugin::ShutdownPlugin");
    // Unregister everything registered in Initialize
}
```

## Registering a Command

```cpp
static void MyCommand(PSPAWNINFO pChar, char* szLine)
{
    WriteChatf("MyPlugin: you typed: %s", szLine);
}

PLUGIN_API void InitializePlugin()
{
    AddCommand("/myplugin", MyCommand);
}

PLUGIN_API void ShutdownPlugin()
{
    RemoveCommand("/myplugin");
}
```

## Registering a TLO

```cpp
#include <mq/Plugin.h>

// Define a data type
class MQ2MyType : public MQ2Type
{
public:
    enum MyMembers { MyValue = 1 };

    MQ2MyType() : MQ2Type("MyType")
    {
        ScopedTypeMember(MyMembers, MyValue);
    }

    bool GetMember(MQVarPtr VarPtr, const char* Member,
                   char* Index, MQTypeVar& Dest) override
    {
        MQTypeMember* pMember = FindMember(Member);
        if (!pMember) return false;

        switch (static_cast<MyMembers>(pMember->ID))
        {
        case MyValue:
            Dest.Set(42);
            Dest.Type = pIntType;
            return true;
        }
        return false;
    }
};

MQ2MyType* pMyType = nullptr;

// TLO function
bool MyTLO(const char* szIndex, MQTypeVar& Ret)
{
    Ret.Type = pMyType;
    return true;
}

PLUGIN_API void InitializePlugin()
{
    pMyType = new MQ2MyType();
    AddMQ2Data("MyTLO", MyTLO);
}

PLUGIN_API void ShutdownPlugin()
{
    RemoveMQ2Data("MyTLO");
    delete pMyType;
    pMyType = nullptr;
}
```

Usage in macros: `${MyTLO.MyValue}` → `42`

## Pulse Hook (per-frame)

```cpp
PLUGIN_API void OnPulse()
{
    // Called every game frame — keep this fast!
    if (GetGameState() != GAMESTATE_INGAME) return;

    // Your per-frame logic here
}
```

## Zoning Hooks

```cpp
PLUGIN_API void OnBeginZone()
{
    WriteChatf("MQ2MyPlugin: Zoning out...");
}

PLUGIN_API void OnEndZone()
{
    WriteChatf("MQ2MyPlugin: Zone complete.");
}
```

## Chat Event Hook

```cpp
PLUGIN_API DWORD OnWriteChatColor(const char* Line, DWORD Color, DWORD Filter)
{
    if (ci_find_substr(Line, "tells you") != -1)
    {
        WriteChatf("MQ2MyPlugin: Someone told you something!");
    }
    return 0;
}
```

## ImGui Window

```cpp
#include <imgui/imgui.h>

static bool showWindow = true;

PLUGIN_API void OnUpdateImGui()
{
    if (!showWindow) return;

    ImGui::Begin("My Plugin Window", &showWindow);
    ImGui::Text("Hello from MQ2MyPlugin!");
    if (ImGui::Button("Click Me"))
    {
        WriteChatf("Button clicked!");
    }
    ImGui::End();
}
```

## Available Hooks Summary

| Hook | When Called |
|------|-------------|
| `InitializePlugin` | Plugin loaded |
| `ShutdownPlugin` | Plugin unloaded |
| `OnPulse` | Every game frame |
| `OnBeginZone` | About to zone |
| `OnEndZone` | Zone load complete |
| `OnWriteChatColor` | Chat message displayed |
| `OnAddSpawn` | Spawn added to zone |
| `OnRemoveSpawn` | Spawn removed from zone |
| `OnAddGroundItem` | Ground item appears |
| `OnRemoveGroundItem` | Ground item removed |
| `OnUpdateImGui` | ImGui render frame |
| `OnMacroStart` | Macro started |
| `OnMacroStop` | Macro stopped |

## Tips

- Keep `OnPulse` lightweight — it runs every frame.
- Always call `RemoveCommand`/`RemoveMQ2Data` in `ShutdownPlugin`.
- Use `DebugSpewAlways` for development logging; it appears in the MQ console.
- Use `WriteChatf` for user-visible messages.
- Test with a debug build first to get useful crash information.

## See Also

- [Plugins](Plugins.md)
- [Data Types and TLO](Data-Types-and-TLO.md)
- [MQ Source on GitHub](https://github.com/macroquest/macroquest)
