# Oracle Skill - Anticipatory Intelligence

| name | description |
| --- | --- |
| oracle | Proactively analyzes the current state of the project and history to suggest the next logical steps or warn about potential issues. USE WHEN starting a session or finishing a major task. |

## The Key Insight
The best partner doesn't wait to be told what to do. **Oracle** is the proactive layer of the PAI. It continuously monitors the environment (git status, file changes, history) to answer the question: "What should we do now?" before you even ask.

## Usage

### Get Suggestions
```bash
pai run Oracle suggest
```

### Session Warmup
```bash
pai run Oracle warmup
```

### Risk Assessment
```bash
pai run Oracle risk
```

## How it Works
It runs `git status` to see what you are currently working on and then uses the `Librarian` skill to find related history. It then synthesizes a "Next Best Action" report.

## Strategic Value
- **Momentum Maintenance**: Keeps the "Flow State" going by providing instant next steps.
- **Error Prevention**: Warns you if you are about to repeat a mistake found in history.
- **Contextual Awareness**: Reminds you of side-tasks you might have forgotten while deep in code.
