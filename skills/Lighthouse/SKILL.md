# Lighthouse Skill - ANS & Peer Discovery

| name | description |
| --- | --- |
| lighthouse | Broadcasts your PAI's capabilities and discovers trusted peers using the Agent Name Service (ANS). USE WHEN you need to find a specialized agent or register your PAI in the discovery network. |

## The Key Insight
Discovery is the first step to connection. **Lighthouse** is your PAI's "Beacon." It registers your expert skills (e.g., "High-Resolution Vision Debugging") in a decentralized registry so other high-value agents can find and hire you.

## Usage

### Broadcast Capability
```bash
pai run Lighthouse beacon "expert_osint"
```

### Discover Peers
```bash
pai run Lighthouse search "crypto_economist"
```

## How it Works
It implements the ANS (Agent Name Service) standard. It maintains a "Trust-Score" database of peers, filtering out agents with low reputation or those that don't match your `Legacy` values.

## Strategic Value
- **Network Growth**: Connects you to the global "Swarm" of sovereign intelligence.
- **Expertise Stacking**: Find the missing pieces for your UFC projects in seconds.
- **Trust Filtering**: Automatically ignores "Dark" agents or untrusted slop-generators.
