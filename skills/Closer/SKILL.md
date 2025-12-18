# Closer Skill - Sales & Outreach Orchestration

| name | description |
| --- | --- |
| closer | Handles the "last mile" of the revenue funnel: outreach, pitching, and client relationship management. USE WHEN you have an asset to sell or a lead to contact. |

## The Key Insight
Building is only half the battle; selling is the other. **Closer** handles the social orchestration. It drafts personalized outreach, generates pitch decks (via Visionary), and tracks follow-ups in the PAI's history.

## Usage

### Draft Cold Outreach
```bash
pai run Closer pitch --lead "John Doe" --product "Automation Script"
```

### Generate Proposal
```bash
pai run Closer proposal --client "Acme Corp" --task "Infrastructure Audit"
```

### Track Follow-up
```bash
pai run Closer followup --lead "Jane Smith"
```

## How it Works
It uses the `Memory` and `Librarian` skills to personalize messages based on previous interactions. It integrates with `Nexus` to send Slack/Email messages or schedule calls.

## Strategic Value
- **Higher Conversion**: Personalized, value-driven outreach beats generic spam.
- **Relentless Persistence**: Never forgets a follow-up.
- **Unified Pipeline**: Connects the technical work directly to the social transaction.
