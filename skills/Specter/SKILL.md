# Specter Skill - Autonomous Pentesting & Vuln Research

| name | description |
| --- | --- |
| specter | Orchestrates automated vulnerability scanning and security audits. USE WHEN you need to test a system for weaknesses, run a security scan, or research exploit payloads. |

## The Key Insight
Offense is the best defense. **Specter** acts as your red-team assistant. It maps attack surfaces, identifies outdated software versions, and suggests specific payloads for testing vulnerabilities—turning the PAI into a "Continuous Auditor."

## Usage

### Scan Surface
```bash
pai run Specter scan "192.168.1.1"
```

### Audit Code
```bash
pai run Specter audit "./src/api/"
```

## Strategic Value
- **Early Detection**: Find vulnerabilities in your own products (Forge assets) before they are exploited.
- **Expertise Accelerator**: Guides you through complex pentesting methodologies (OWASP, MITRE ATT&CK).
- **Automated Vigilance**: Can be scheduled to run background audits on your infrastructure.
