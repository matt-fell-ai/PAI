# Manual Skill - Dynamic Infrastructure Guide

| name | description |
| --- | --- |
| manual | Provides dynamic, up-to-date documentation and "How-To" guides for the PAI. USE WHEN you need help using a skill, setting up a workflow, or understanding the system. |

## The Key Insight
Static documentation is often stale. **Manual** uses the PAI's own source code and `Neural` memory to generate custom instructions. It doesn't just show you "A" guide; it shows you "Your" guide, based on your OS and installed tools.

## Usage

### Get Help on a Skill
```bash
pai run Manual help <skill_name>
```

### How-To Guide
```bash
pai run Manual how-to "Make money with Alpha"
```

### System Overview
```bash
pai run Manual overview
```

## How it Works
It scans the `SKILL.md` files and `tools/` directories across the infrastructure. It uses `Neural` to find the most relevant patterns and synthesizes a concise, actionable guide for the user's specific query.

## Strategic Value
- **Zero Friction**: No need to browse through folders of markdown.
- **Accurate Info**: Documentation is always in sync with the actual code.
- **On-Demand Training**: Teaches the user how to be a high-level PAI operator.
