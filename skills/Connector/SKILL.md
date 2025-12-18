# Connector Skill - External Integrations

| name | description |
| --- | --- |
| connector | Interface for external services (Slack, Google Calendar, GitHub, etc.). USE WHEN you need to pull data from or push actions to external platforms. |

## The Key Insight
A Personal AI shouldn't be trapped in the terminal. **Connector** provides the "hands" for your agent to interact with the outside world.

## Usage

### Check Messages (Slack/Email)
```bash
pai run Connector check
```

### Schedule an Event
```bash
pai run Connector schedule "Meeting with Bob at 3pm"
```

### GitHub Sync
```bash
pai run Connector sync-repo
```

## How it Works
It uses standard CLI tools (like `gh` for GitHub, `slack-cli`, or custom API scripts) to bridge the gap between the PAI and your SaaS tools.

## Strategic Value
- **Autonomous Scheduling**: The agent can manage your time based on project deadlines.
- **Communication Hub**: Aggregates messages from multiple platforms into a single stream for the PAI to process.
- **Repo Management**: Automatically creates issues or PRs based on the `History/Execution/` logs.
