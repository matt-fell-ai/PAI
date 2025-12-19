# Sanctity Skill - ZKP-based Privacy Protection

| name | description |
| --- | --- |
| sanctity | Uses Zero-Knowledge Proofs (ZKP) to share insights with other agents without revealing raw sensitive data. USE WHEN you need to collaborate while protecting your "Soul" or private history. |

## The Key Insight
Data sharing is a liability; insight sharing is an asset. **Sanctity** ensures that when your PAI talks to others, it never "leaks" your private life. It proves *that* it knows something without showing *how* it knows it.

## Usage

### Prove Knowledge
```bash
pai run Sanctity prove "user_is_owner" "--target peer_agent_id"
```

### Cleanse Output
```bash
pai run Sanctity cleanse "collaboration_notes.md"
```

## How it Works
It utilizes ZK-STARKs to generate proofs of knowledge. It "Wraps" PAI-to-PAI communication in a privacy layer that strips out PII (Personally Identifiable Information) while maintaining semantic logic.

## Strategic Value
- **Zero-Leak Collaboration**: Work with unknown agents safely.
- **Privacy Sovereignty**: You maintain absolute control over your raw data while still benefiting from the network.
- **Regulatory Compliance**: Automatically adheres to future privacy-preserving laws.
