# Actuate Skill - Physical & IoT Interface

| name | description |
| --- | --- |
| actuate | Interfaces with the physical world through IoT devices, HomeAssistant, or webhooks. USE WHEN you need to control hardware, check environmental sensors, or trigger physical actions. |

## The Key Insight
Intelligence must manifest in reality. **Actuate** gives PAI "Hands." It allows your digital partner to adjust your work environment (lighting, temperature) or trigger physical alerts based on strategic events.

## Usage

### Trigger Device
```bash
pai run Actuate trigger "office_lights" "--state ON"
```

### Sensor Status
```bash
pai run Actuate status "room_temp"
```

## How it Works
It utilizes a "Gateway" pattern to send authenticated requests to local IoT hubs (HomeAssistant) or global webhook services (IFTTT). All device keys are managed by the `Vault`.

## Strategic Value
- **Focus Optimization**: Automatically enters "Deep Work" mode by adjusting physical environment.
- **Physical Safety**: Alerts you via local hardware if a high-stakes security event is detected by `Specter`.
- **Reality Loop**: Bridges the gap between "Digital Strategy" and "Physical Being."
