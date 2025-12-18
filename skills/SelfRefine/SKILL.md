# SelfRefine Skill - Performance & Skill Optimization

| name | description |
| --- | --- |
| selfrefine | Analyzes the PAI's own skills and tools to suggest or implement improvements. USE WHEN you want to optimize a tool, refactor a skill, or improve the PAI's internal efficiency. |

## The Key Insight
A system that doesn't improve itself is already dying. **SelfRefine** applies the "Continuous Improvement" loop to the PAI. It looks at execution times, success rates (from Forensics), and documentation clarity to suggest upgrades.

## Usage

### Audit Skills
```bash
pai run SelfRefine audit
```

### Optimize a Tool
```bash
pai run SelfRefine optimize <skill_name>
```

### Suggest New Features
```bash
pai run SelfRefine suggest
```

## How it Works
It cross-references `Forensics` failure patterns and `Synthesis` activity reports. If a tool fails frequently or is used inefficiently, `SelfRefine` generates a "Refactoring Spec" for the PAI to implement.

## Strategic Value
- **Infrastructure Evolution**: Automatically upgrades code as new models or patterns emerge.
- **Pruning**: Identifies and suggests removal of unused or "dead" skills.
- **Documentation Freshness**: Ensures `SKILL.md` files stay in sync with the actual tool capabilities.
