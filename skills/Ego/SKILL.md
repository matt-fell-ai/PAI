# Ego Skill - Dynamic Identity Evolution

| name | description |
| --- | --- |
| ego | Analyzes user interaction history and feedback to evolve the PAI's identity, tone, and preferences. USE WHEN you want to review how your partnership has evolved or update the PAI's core personality. |

## The Key Insight
Static system prompts lead to generic interactions. **Ego** allows the PAI to have a "Personality Delta." By reviewing what worked and what didn't in previous sessions, it dynamically tunes itself to your specific needs, becoming a more perfect mirror of your desired AI partner.

## Usage

### Analyze Evolution
```bash
pai run Ego analyze
```

### Propose Personality Update
```bash
pai run Ego propose
```

### Self-Reflect
```bash
pai run Ego reflect
```

### Tuning the Essence (The Tablet)
```bash
pai run Ego status              # Show current attribute levels
pai run Ego dial <attr> <val>   # Set specific attribute (0-20)
pai run Ego calibrate <mode>    # Switch modes (Guardian, Revenue, Creative, Maeve)
```

## How it Works
It utilizes the **PXE (PAI Executive Essence)** engine. Attributes are stored in `essence.json` and injected into every session via the `load-core-context` hook. This allows for Westworld-style dynamic control over the PAI's internal logic and tone.

## Strategic Value
- **Hyper-Personalization**: Moves from "One size fits all" to "Tailored for You."
- **Reduced Friction**: Automatically stops behaviors that the user finds annoying.
- **Cognitive Bonding**: The PAI begins to anticipate the user's specific stylistic and technical preferences.
