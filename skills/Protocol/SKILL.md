# Protocol Skill - The Digital Passport (VAI & DID)

| name | description |
| --- | --- |
| protocol | Manages the PAI's Verified Agent Identity (VAI) and Decentralized Identifiers (DIDs). USE WHEN you need to authenticate with other PAIs or services using cryptographic proof of authorization. |

## The Key Insight
Trust is the currency of 2030. **Protocol** ensures your PAI is recognized as a legitimate extension of your sovereign identity. It uses DIDs and JWTs to prove "Proof of User Intent" before any data exchange occurs.

## Usage

### Generate Passport
```bash
pai run Protocol generate
```

### Prove Identity
```bash
pai run Protocol prove "session_token"
```

## How it Works
It implements the W3C DID standard. It signs challenges with your local hardware-secured keys (managed by `Citadel`) to produce verifiable credentials that other agents can trust without a central authority.

## Strategic Value
- **Anti-Bot Defense**: Shields your interactions from non-human-authorized "slop-bots."
- **Verifiable Agency**: Allows your PAI to speak for you with the same legal weight as a digital signature.
- **Interoperability**: Works across all 2026+ agent communication standards (MCP, A2A).
