# Echo Skill - Auditory Context Capture

| name | description |
| --- | --- |
| echo | Processes native audio recordings to extract structured context, tasks, and "User Truths". USE WHEN you have meeting recordings, verbal notes, or voice messages to ingest into the PAI. |

## The Key Insight
Conversation is the highest-bandwidth form of human thought. **Echo** turns verbal complexity into structured infrastructure. It doesn't just transcribe; it "Diarizes" and extracts the strategic intent behind what was said.

## Usage

### Ingest Audio
```bash
pai run Echo ingest "strategy_meeting.mp3"
```

### Verbal Note
```bash
pai run Echo note "voice_memo.wav"
```

## How it Works
It uses Gemini 3.0's native audio fusion architecture. It processes raw audio waves alongside project history, identifying when a speaker mentions a "Task Unit" or a new "UFC Project" requirement.

## Strategic Value
- **Hands-Free Context**: Record an idea while walking and have it scaffolded by the time you reach your desk.
- **Strategic Continuity**: Captures the "Why" behind decisions made in meetings.
- **Automatic Tasking**: Turns "We should do X" into an actual entry in your `History/Execution/`.
