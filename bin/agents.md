# PAI Binaries & Utilities

## Overview
This directory contains the core executable scripts that power the PAI Universal Bridge and system management.

## Core Binaries
- **`pai`**: The primary dispatcher. Routes user intent to modular skills in the `skills/` directory.
- **`pai-init`**: The conversational onboarding wizard. Sets up identity, API keys, and local model configurations.
- **`pai-check`**: The health monitor. Verifies API connectivity and local Ollama service status.
- **`pai-test`**: The universal test suite. Ensures all 51+ core modules are operational in the current environment.

## Usage
Most interactions happen via the bridge:
```bash
pai run <Skill> <Command> [args]
```
