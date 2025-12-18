# Sanctum Skill - Isolated Execution Sandbox

| name | description |
| --- | --- |
| sanctum | Executes untrusted or experimental code in an isolated environment. USE WHEN you want to test a new script, run a high-risk scraper, or experiment with third-party code. |

## The Key Insight
Safety allows for speed. **Sanctum** provides a "Zero-Trust" environment for your PAI. By running experimental code in isolation, you can explore higher-risk revenue strategies without endangering your primary PAI data or host machine.

## Usage

### Run Isolated
```bash
pai run Sanctum run <script.py>
```

### Clean Sandbox
```bash
pai run Sanctum purge
```

## How it Works
It utilizes Docker or a local virtual environment with restricted permissions. It mounts only the necessary files and ensures that any network activity is logged and throttled.

## Strategic Value
- **Fearless Experimentation**: Try new libraries or "Vibe" generated scripts immediately.
- **Data Protection**: Your `History/` and `.env` are physically unreachable from the sandbox.
- **Environmental Cleanliness**: Keeps your main machine free of "Dependency Bloat."
