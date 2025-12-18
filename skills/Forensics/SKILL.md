# Forensics Skill - Root Cause & Pattern Analysis

| name | description |
| --- | --- |
| forensics | Deep analysis of system logs, session history, and execution failures. USE WHEN a task fails repeatedly, or you need to understand the underlying patterns of your work. |

## The Key Insight
Debugging is often a search problem. **Forensics** treats your `History/Raw-Outputs/` as a crime scene. By analyzing the sequence of events leading to a failure, it can pinpoint exactly where the "cognitive disconnect" happened between the agent and the environment.

## Usage

### Analyze Last Failure
```bash
pai run Forensics debug
```

### Trace Tool Usage Patterns
```bash
pai run Forensics patterns
```

### Cognitive Audit
```bash
pai run Forensics audit
```

## How it Works
It parses the JSONL logs in `${PAI_DIR}/History/Raw-Outputs/` and cross-references them with `Execution/Bugs/`. It looks for:
1. **Recursion loops**: Same command failing multiple times.
2. **Context loss**: Large gaps in tool execution or sudden shifts in file focus.
3. **Environment drift**: Commands that used to work but now fail.

## Strategic Value
- **Self-Healing Infrastructure**: Identifies when a tool is broken and needs refactoring.
- **Improved Prompting**: Highlights which prompts consistently lead to errors.
- **Faster Recovery**: Skip the "what did I just do?" phase of debugging.
