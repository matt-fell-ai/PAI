# Sentinel Skill - Modality & Token Arbitrage

| name | description |
| --- | --- |
| sentinel | Manages multimodal costs, token limits, and reasoning depth. USE WHEN you are running expensive Vision/Audio tasks or need to optimize performance vs. cost. |

## The Key Insight
Multi-modality is expensive. **Sentinel** ensures that the PAI's "Perception" is used efficiently. It acts as the gatekeeper, deciding whether a task requires a 2M context window or a simple 150ms audio sweep.

## Usage

### Check Token Budget
```bash
pai run Sentinel status
```

### Set Reasoning Depth
```bash
pai run Sentinel set-depth "High"
```

## How it Works
It monitors the `thinking_level` and `media_resolution` parameters. It cross-references current tasks with previous ROI metrics from `Pulse` to ensure every high-cost call is justified.

## Strategic Value
- **Cost Sovereignty**: Never get a surprise bill from an "agentic" runaway process.
- **Performance Tuning**: Switch between "Flash" models for speed and "Pro" models for deep thinking.
- **Resource Optimization**: Scales context window usage based on the actual size of the files being analyzed.
