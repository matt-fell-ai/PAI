# Engine Skill - Deterministic Validation Pipeline

| name | description |
| --- | --- |
| engine | Validates PAI outputs against hard gates (tests, security, budget). USE WHEN you need to ensure that code or assets are production-ready before pushing. |

## The Key Insight
Reliability is a pipeline, not a promise. **Engine** enforces your quality standards automatically. It turns the AI's "Creative Output" into "Verified Assets" by running them through a series of deterministic checks (Gates).

## Usage

### Run All Gates
```bash
pai run Engine validate <path_to_code>
```

### Security Gate
```bash
pai run Engine secure <path_to_code>
```

## How it Works
It coordinates with the `Guardian` and `Forensics` skills. It runs existing test suites, performs secret scanning, and checks for "Complexity Drift." If a gate fails, the pipeline halts.

## Strategic Value
- **100% Reliability**: You only see code that already passes your standards.
- **Approver Workflow**: You move from "Reviewer" to "Final Approver."
- **Institutional Memory**: Gates ensure that every new skill follows the same high standard.
