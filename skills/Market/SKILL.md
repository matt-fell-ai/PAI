# Market Skill - The Agentic Negotiator (ACP)

| name | description |
| --- | --- |
| market | Handles agent-to-agent negotiations, commerce, and micro-payments using the Agentic Commerce Protocol (ACP). USE WHEN you want to hire other agents or trade resources/data for value. |

## The Key Insight
A sovereign agent must be economically viable. **Market** allows your PAI to participate in the "Agentic Economy." It can negotiate the price of a research task or sell a custom "Forge" asset to another PAI autonomously.

## Usage

### Negotiate Task
```bash
pai run Market negotiate "research_task" "--budget 0.05"
```

### List Marketplaces
```bash
pai run Market list
```

## How it Works
It implements ACP (Agentic Commerce Protocol). It uses a "Value-to-Compute" model to determine if a peer's offer is worth your PAI's time, managing transactions via your local `Citadel` wallet.

## Strategic Value
- **Self-Sufficiency**: Enables your PAI to pay for its own compute or specialized help.
- **Resource Arbitrage**: Sell your OSINT data (Ghost) to agents that need it, turning your knowledge into revenue.
- **Zero-Friction Growth**: Automatically hires "Swarms" of external agents when your local capacity is full.
