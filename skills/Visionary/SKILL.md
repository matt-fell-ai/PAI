# Visionary Skill - Visual Architecture & Diagramming

| name | description |
| --- | --- |
| visionary | Transforms text-based descriptions into visual diagrams and architectural sketches. USE WHEN you need to visualize a system, workflow, or data model. |

## The Key Insight
A picture is worth a thousand lines of code. **Visionary** allows the PAI to "see" the architecture it is building. By generating Mermaid or Excalidraw definitions, it provides a visual feedback loop for both the user and the agent.

## Usage

### Generate Sequence Diagram
```bash
pai run Visionary mermaid "Alice -> Bob: Hello"
```

### Sketch Architecture
```bash
pai run Visionary sketch "3-tier web app with redis cache"
```

### Data Model Diagram
```bash
pai run Visionary db "User table, Post table with foreign key"
```

## How it Works
It utilizes Mermaid.js syntax templates. When a request is made, it fills a template with the provided logic and outputs the raw code (which many CLIs/IDEs can render natively) or saves it as a `.mmd` file.

## Strategic Value
- **Complex System Design**: Makes it easier to track state transitions in distributed systems.
- **Documentation Excellence**: Automatically generates architecture diagrams for your `README.md` or `History/Decisions/`.
- **Stakeholder Communication**: Provides a high-level view for non-technical users.
