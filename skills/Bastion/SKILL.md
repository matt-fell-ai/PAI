# Bastion Skill - System Hardening & Defense

| name | description |
| --- | --- |
| bastion | Provides guidance and automation for hardening systems, configuring firewalls, and enforcing security policies. USE WHEN you need to protect a server, secure a network, or apply defensive configurations. |

## The Key Insight
A "Citadel" is built from many "Bastions." This skill focuses on the technical implementation of defense. It translates "I want to be secure" into actual firewall rules, kernel hardening parameters, and access control lists.

## Usage

### Harden OS
```bash
pai run Bastion harden "linux-ubuntu"
```

### Apply Firewall
```bash
pai run Bastion firewall "strict-mode"
```

## Strategic Value
- **Deterministic Defense**: Reduces human error in complex security configurations.
- **Compliance Ready**: Helps you align your projects with industry standards (NIST, CIS).
- **Rapid Recovery**: Scaffolds "Safe-State" configurations if a Bastion is breached.
