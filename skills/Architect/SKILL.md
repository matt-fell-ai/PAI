# Architect Skill

## Overview
`Architect` is the spatial design engine for the PAI. It manages the virtual Dojo world by writing world-state transactions to SpacetimeDB, allowing PAI to dynamically build and reconfigure its living environment.

## Strategic Purpose
To provide a persistent, high-fidelity spatial interface for human-AI co-existence, moving beyond text-based interaction into a shared reality.

## Tools
- `design <layout>`: Reconfigures the Dojo for a specific task (e.g., 'trading_floor', 'zen_library', 'war_room').
- `spawn <asset>`: Dynamically adds a 3D asset or data visualization to the Dojo world.
- `state`: Queries the current relational world-state from SpacetimeDB.

## Use When
- You want to change the visual environment of the Dojo.
- Initializing a new project that requires custom spatial visualizations.
- Visualizing complex data from `Graph` or `Alpha` in 3D.
