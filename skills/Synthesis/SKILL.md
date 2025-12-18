# Synthesis Skill - Automated Insights

| name | description |
| --- | --- |
| synthesis | Analyzes the PAI History and Memory to generate periodic reports and insights. USE WHEN you need a summary of recent work, a daily briefing, or a "Delta" of what has changed. |

## The Key Insight
Data without synthesis is just noise. **Synthesis** transforms the raw logs of the `History/` system into actionable intelligence. It answers: "What did I actually achieve today?" and "What should be my focus tomorrow?"

## Usage

### Daily Briefing
```bash
pai run Synthesis daily
```

### Weekly Summary
```bash
pai run Synthesis weekly
```

### Project "Delta"
```bash
pai run Synthesis delta <project_name>
```

## How it Works
It scans `${PAI_DIR}/History/Sessions/` and `${PAI_DIR}/History/Learnings/` for the relevant timeframe, extracts key themes, and uses Fabric patterns (like `summarize` or `extract_wisdom`) to generate a concise report.

## Strategic Value
- **Focus Alignment**: Ensures you are working on what matters.
- **Cognitive Offloading**: You don't have to remember every detail of yesterday's session.
- **Progress Visualization**: Makes intangible work (coding, research) visible and measurable.
