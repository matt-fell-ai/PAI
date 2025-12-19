# Armory Skill - Tool Management & Execution

| name | description |
| --- | --- |
| armory | Manages the downloading, installation, and execution of external cyber, OSINT, and pentesting tools. USE WHEN you need to install a specific program (e.g., Sherlock, Nuclei) or execute a tool from the PAI's toolkit. |

## The Key Insight
A master craftsman is only as good as their tools. **Armory** turns PAI into a package manager for the world's most powerful security repositories. It handles the cloning, environment setup, and execution logic so you can focus on the mission.

## Usage

### Install a Tool
```bash
pai run Armory install "sherlock"
```

### List Available Tools
```bash
pai run Armory list
```

### Run an Installed Tool
```bash
pai run Armory run "nuclei" "-u https://example.com"
```

## Supported Toolset (Pre-configured)
- **Ghost (OSINT)**: `sherlock`, `theHarvester`, `spiderfoot`, `holehe`.
- **Specter (Pentest)**: `nuclei`, `ffuf`, `nmap`, `sqlmap`, `searchsploit`.
- **Bastion (Hardening)**: `lynis`, `rkhunter`, `fail2ban`.

## How it Works
It maintains a manifest of tool repositories and installation methods (Git, Go, Apt). Tools are installed into `${PAI_DIR}/armory/` to keep your root environment clean.

## Strategic Value
- **Rapid Mobilization**: Go from zero to a full Kali-equivalent toolkit in minutes.
- **Automated Updates**: Keeps your offensive and defensive tools at the latest version.
- **Standardized Execution**: Wraps complex CLI flags into simple PAI commands.
