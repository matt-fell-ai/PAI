# Neural Skill - Semantic Context Memory

| name | description |
| --- | --- |
| neural | Advanced semantic retrieval and concept matching across PAI history. USE WHEN you need to find conceptually related solutions or patterns, even if keywords don't match. |

## The Key Insight
Keywords are fragile; concepts are robust. **Neural** moves the PAI beyond string matching. It analyzes the "Intent" behind your past work, allowing the agent to say: "I see you're building a state machine; here is how you handled similar complexity in your 2024 Auth project."

## Usage

### Concept Search
```bash
pai run Neural search "How do I handle complex state?"
```

### Pattern Retrieval
```bash
pai run Neural pattern "OAuth flow"
```

## How it Works
In this universal version, it implements a weighted conceptual index. It maps your `History/` into a local conceptual graph, enabling "Fuzzy" discovery of your personal best practices and user truths.

## Strategic Value
- **Intelligence compounding**: The PAI actually gets "smarter" as the history grows.
- **Cross-pollination**: Applies architectural patterns from one domain (e.g., Security) to another (e.g., UI).
- **Reduced Redundancy**: Prevents you from asking the same "How to" questions multiple times.
