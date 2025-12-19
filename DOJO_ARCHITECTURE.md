# PAI Dojo: The Spatial Operating System

## Overview
The **PAI Dojo** is a high-fidelity, high-agency virtual environment built in **Unreal Engine 5**. It transforms PAI from a terminal-based tool into an embodied partner that lives, designs, and interacts within a persistent shared reality.

## Core Components

### 1. SpacetimeDB (The Relational World-State)
Unlike traditional game servers that use ephemeral packets, the Dojo uses **SpacetimeDB** as its source of truth.
- **Relational Reality**: Every object in the Dojo (furniture, holograms, terminal states) is a row in a relational database table.
- **Transactional Consistency**: Changes to the world (e.g., spawning a new OSINT research station) are handled as database transactions, ensuring the PAI brain and the Unreal body are always in perfect sync.
- **Persistence**: The Dojo is a "Living Room." If you disconnect, PAI continues working on the `Hive` blackboard, and the world state remains exactly as it was when you return.

### 2. MetaHuman Embodiment
- **Visuals**: PAI is represented by a high-fidelity **Epic Games MetaHuman**.
- **Lip-Sync**: Uses **Local Audio2Face** integration. PAI’s local voice synthesis (Piper) streams directly into Unreal, driving photorealistic facial animation without cloud dependency.
- **Intent-to-Physicality (I2P)**: PAI skill outputs include "Physical Intents" (e.g., `POINT_AT_LEAD`, `CONSULT_WHITEBOARD`) which map directly to Unreal animation montages.

### 3. Procedural Design (The Architect Skill)
PAI doesn't just "live" in the Dojo; it **designs** it.
- Using the `Architect` skill, PAI writes to the `WorldAssets` table in SpacetimeDB.
- Unreal Engine’s **Procedural Content Generation (PCG)** framework subscribes to these updates and dynamically spawns the required infrastructure (e.g., a 'War Room' layout for security tasks).

### 4. Local Auditory Intelligence
- **STT**: Uses a local **Faster-Whisper** instance to hear your voice in the room.
- **STS**: Uses **Piper-TTS** to respond with sub-second latency and a sovereign local voice.

---

## Developer Workflow

### SpacetimeDB Module (Rust/C#)
The Dojo backend logic is contained in SpacetimeDB **Reducers**.
```rust
#[reducer]
pub fn spawn_research_station(ctx: ReducerContext, pos: Vec3) -> Result<(), String> {
    WorldAsset::insert(WorldAsset {
        id: 0,
        asset_type: "ResearchStation".to_string(),
        position: pos,
        status: "ACTIVE".to_string(),
    });
    Ok(())
}
```

### PAI Bridge (Python)
The `Architect` skill triggers these reducers via the SpacetimeDB CLI or SDK.
```python
pai run Architect design war_room
```

### Unreal Client (UE5)
The Unreal Dojo Client uses the **SpacetimeDB Unreal SDK** to bind actor components to DB tables.
- **Table Bindings**: `UDbConnection` manages the persistent link.
- **Dynamic Spawning**: Actors are spawned/destroyed based on `OnRowInserted` or `OnRowDeleted` callbacks.

---

## 2030 Vision: The Matrix realization
The Dojo is the realization of the "I know kung fu" concept. It is a simulated space where data becomes physical, strategy becomes spatial, and your AI partner is a permanent, visible presence in your digital life.
