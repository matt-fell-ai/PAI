# UFC Skill - Unified Filesystem-based Context

| name | description |
| --- | --- |
| ufc | Enforces a hierarchical single source of truth for projects. USE WHEN starting a new project, restructuring existing ones, or ensuring context alignment across agents. |

## The Key Insight
Scaffolding is more important than the model. **UFC** provides the structural "skeleton" for your knowledge. By forcing a consistent directory structure (`Knowledge/`, `Methodology/`, `Tools/`, `Tasks/`), it ensures that any AI agent can step into a project and immediately know exactly where everything is and *why* it exists.

## Usage

### Scaffold Project
```bash
pai run UFC scaffold "Project Name"
```

### Audit Alignment
```bash
pai run UFC audit
```

## How it Works
It creates and manages a standardized directory tree. It also generates a `CONTEXT.md` in each root that links to the project's specific `Methodology` and `User Truths` from the `CORE` skill.

## Strategic Value
- **Agent Interoperability**: Multiple agents (Engineer, Researcher) can work on the same project without context collision.
- **Zero-Onboarding**: New projects are born with a "Map."
- **Cognitive Efficiency**: You spend less time searching for files and more time building.
