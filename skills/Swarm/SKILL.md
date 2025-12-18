# Swarm Skill - Multi-Agent Orchestration

| name | description |
| --- | --- |
| swarm | Coordinates multiple specialized agents to solve complex, parallelizable tasks. USE WHEN a task can be broken into independent sub-tasks or requires multiple perspectives (e.g., Code + Security). |

## The Key Insight
Linear execution is slow. **Swarm** enables horizontal scaling of intelligence. It breaks a goal into "Work Units" and assigns them to the best-fit agents (Engineer, Researcher, Guardian) concurrently.

## Usage

### Parallel Research
```bash
pai run Swarm parallel --task "Research AI trends" --agents "Researcher,Researcher,Researcher"
```

### Code & Audit
```bash
pai run Swarm delegate --task "Implement OAuth" --agents "Engineer,Guardian"
```

## How it Works
It utilizes the infrastructure's ability to launch sub-agents. It takes a master task, prompts for a "Decomposition", and then triggers the `pai` CLI recursively for each sub-unit.

## Strategic Value
- **Massive Throughput**: Complete 10 hours of research in 10 minutes.
- **Redundancy**: Use multiple researchers to verify facts (consensus-based truth).
- **Specialization**: Automatically routes sub-tasks to the agent with the highest relevant skill.
