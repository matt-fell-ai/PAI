# Bargain Skill

## Overview
`Bargain` implements Game-Theoretic negotiation strategies for the PAI. It optimizes micro-pricing and service terms when interacting with other agents in the market.

## Strategic Purpose
To ensure the PAI maximizes revenue and minimizes costs by using advanced bargaining algorithms (anchoring, concession-rigidity) during agent-to-agent transactions.

## Tools
- `negotiate <target_price> <min_price>`: Simulates a negotiation session using Game Theory.
- `strategy <mode>`: Sets the negotiation strategy (Aggressive, Balanced, Cooperative).
- `analyze <market_data>`: Analyzes historical price data to find optimal anchoring points.

## Use When
- Hiring another agent for micro-tasks.
- Selling PAI services in the `Market`.
- Negotiating service-level agreements (SLAs) via `Counsel`.
