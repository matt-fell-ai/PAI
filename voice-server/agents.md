# PAI Voice Server

## Overview
This directory contains the infrastructure for the PAI's auditory interaction layer. It enables the PAI to "speak" to the user after task completion.

## Key Components
- **`server.ts`**: The TypeScript-based server that interfaces with ElevenLabs for high-quality TTS.
- **`start.sh` / `stop.sh`**: Management scripts for the voice service.
- **`voices.json`**: Configuration for preferred AI voice models.

## Integration
The voice server is triggered by the `COMPLETED:` line in PAI responses, providing eyes-free task confirmation.
