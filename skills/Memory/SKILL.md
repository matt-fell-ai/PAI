# Memory Skill - The Second Brain

| name | description |
| --- | --- |
| memory | Long-term persistent storage for user preferences, facts, and session context. USE WHEN you need to remember something for future sessions or retrieve previously stored information. |

## The Key Insight
Most AI agents start every session with a blank slate. **Memory** gives the PAI a persistent state. By explicitly storing and retrieving facts, the agent becomes more personalized and effective over time.

## Usage

### Storing a Fact
```bash
pai run Memory store "I prefer using absolute paths for all tool calls."
```

### Retrieving Facts (Search)
```bash
pai run Memory search "paths"
```

### Listing All Memory
```bash
pai run Memory list
```

## How it Works
The memory is stored in `${PAI_DIR}/memory.json`. It is a simple collection of timestamped entries with optional tags.

## Strategic Value
- **Identity Consistency**: Remembers your coding style, tone, and personal mission.
- **Workflow Continuity**: Picks up where you left off on complex, multi-day projects.
- **Fact Cache**: Stores hard-to-find documentation or API keys (securely managed).
