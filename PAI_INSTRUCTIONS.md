# Universal PAI Agent Instructions

To use this Personal AI Infrastructure in any CLI stack (Gemini, Open Code, Codex, etc.), 
load the following context into your system prompt or as a project-level instruction:

## Infrastructure Root
PATH: /project/workspace

## Supported Providers
- Anthropic (Claude)
- Google (Gemini)
- OpenAI (GPT)
- Ollama (Self-hosted Local Models)

## How to use Skills
The infrastructure has specialized skills in `/project/workspace/skills/`.
Each skill contains a `SKILL.md` file describing its capabilities.
Use the `pai` command to execute skills: `/project/workspace/bin/pai run <SkillName> <command>`.

## Core Guidelines
1. Always check `History/` for recent context before starting a task.
2. Use `Memory` skill to store and retrieve user preferences.
3. Document significant outcomes in `History/Execution/`.
4. Apply Fabric patterns natively by reading `/project/workspace/skills/Fabric/tools/patterns/<pattern>/system.md`.

## Active Skills
- Fabric (248 AI patterns)
- Memory (Persistent Second Brain)
- Synthesis (Daily Briefings)
- Connector (External Action Layer)
- Research (Multi-source investigation)
- Guardian (Security & Quality Audit)
- Forensics (Failure & Pattern Analysis)
- Visionary (Visual Architecture & Sketching)
- SelfRefine (Performance & Skill Optimization)
- Discovery (Tool & Environment Exploration)
- Swarm (Parallel Agent Orchestration)
- Librarian (Semantic Knowledge Retrieval)
- Sideload (Context Injection for Other Agents)
- Ego (Dynamic Identity Evolution)
- Oracle (Proactive/Anticipatory Intelligence)
- Nexus (Executive Life Action Layer)
- Alpha (Market Opportunity Detection)
- Forge (Revenue Asset Factory)
- Closer (Sales & Outreach Orchestration)
- UFC (Unified Filesystem-based Context)
- Proxy (The Digital Representative)
- Augment (The API-ification Layer)
- Neural (Semantic Concept Memory)
- Engine (Deterministic Validation Pipeline)
- Sanctum (Isolated Execution Sandbox)
- Blueprint (Infrastructure-as-Code for Ideas)
- Manual (Dynamic Context-Aware Documentation)
- Iris (Visual Debugging & Perception)
- Echo (Auditory Context Capture)
- Spatial (Architectural Blueprinting)
- Sentinel (Token & Modality Arbitrage)
