# Sideload Skill - Surgical Context Injection

| name | description |
| --- | --- |
| sideload | Compresses and outputs the core context of any PAI skill for injection into other LLM sessions. USE WHEN you need to teach a new AI agent about a specific PAI skill quickly. |

## The Key Insight
Massive documentation is a token hog. **Sideload** extracts only the "Essence" of a skill—the routing, the tools, and the core workflows—into a high-density markdown block.

## Usage

### Sideload a Skill
```bash
pai run Sideload skill "Fabric"
```

### Full PAI Sideload
```bash
pai run Sideload full
```

## How it Works
It reads the `SKILL.md` and `tools/` directory of the target skill and generates a "Context Packet" that is optimized for LLM ingestion.

## Strategic Value
- **Token Efficiency**: Reduces a 2000-line skill doc to 100 lines of actionable instructions.
- **Cross-Stack Portability**: Effortlessly move between Gemini, Claude, and Droid by "Sideloading" the PAI knowledge.
- **Instant Competence**: Give a "blank slate" agent immediate mastery over a domain.
