# Discovery Skill - Exploration & Integration

| name | description |
| --- | --- |
| discovery | Explores the environment, network, and available APIs to identify new integration opportunities. USE WHEN you are in a new environment or need to find a tool to solve a problem. |

## The Key Insight
A PAI is only as good as the tools it can reach. **Discovery** is the "scout" for your infrastructure. It doesn't just use tools; it finds them. It identifies local services, cloud APIs, and even other AI agents it can collaborate with.

## Usage

### Scan Environment
```bash
pai run Discovery scan
```

### Search for Tool
```bash
pai run Discovery find "pdf parser"
```

### API Discovery
```bash
pai run Discovery api <url>
```

## How it Works
It uses `ls`, `which`, and `curl` to map out the current machine's capabilities. It can also perform web searches (via `WebSearch`) to find the best open-source tool or API for a specific task.

## Strategic Value
- **Zero-Touch Adaptation**: Automatically configures the PAI when moved to a new server or OS.
- **Dependency Map**: Visualizes how skills depend on external binaries (git, bun, python).
- **Opportunity Detection**: "I see you have Docker installed; should I add a ContainerManagement skill?"
