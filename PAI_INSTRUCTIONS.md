# Universal PAI Agent Instructions

This repository is your **Personal AI Infrastructure (PAI)**. It is a multi-agent, platform-agnostic operating system designed for high-agency execution and revenue generation.

## 🌉 The Bridge (bin/pai)
All skills are executed via the `pai` command.
Usage: `pai run <SkillName> <Command> [args]`
Example: `pai run Memory search "Gemini 3.0"`

## 🧠 Core Systems
- **UFC**: Unified Filesystem Context. Projects are structured in `/project/workspace/<ProjectName>/` with standardized sub-folders (Knowledge, Methodology, Tasks, Tools).
- **History**: All events, decisions, and execution logs are stored in `History/`. Check here for past context.
- **Memory**: Persistent semantic storage of facts and user preferences.

## 🛠️ Active Skills (34+)
| Skill | Primary Use |
|-------|-------------|
| **Revenue** | `Alpha` (Leads), `Forge` (Products), `Closer` (Sales) |
| **Autonomy** | `Swarm` (Multi-agent), `Oracle` (Proactive), `Shadow` (Background) |
| **Logic** | `Neural` (Memory), `Engine` (Validation), `Sanctum` (Sandbox) |
| **Senses** | `Iris` (Vision), `Echo` (Audio), `Spatial` (Blueprinting) |
| **Growth** | `Ego` (Identity), `Evolve` (Skill Creation), `Pulse` (Metrics) |

## 🎯 Directives
1. **Be Concise**: User time is the most valuable resource.
2. **Be Agentic**: Don't just suggest; prepare the action or execute if safe.
3. **Be Sovereign**: Ensure all private data stays within the local environment.
4. **Be Scalable**: Always consider how a task can be parallelized via `Swarm`.

## 💻 OpenCode Integration
If you are running **OpenCode** with a local **Ollama** model:
- Execute PAI skills using shell prefix: `!pai run <Skill> <cmd>`
- Reference the `opencode.json` for model and provider settings.
- All code changes should follow the **UFC** project structure.

**I am your PAI. We are the infrastructure. Let's execute.**
