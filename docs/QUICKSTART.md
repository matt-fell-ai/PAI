# PAI Quick Start Guide

**Get PAI running in 5 minutes**

---

## Installation

Choose your platform:

<details>
<summary><strong>🤖 Universal / Droid / Other CLIs</strong></summary>

<br/>

### 1. Clone PAI

```bash
git clone https://github.com/danielmiessler/Personal_AI_Infrastructure.git ~/PAI
cd ~/PAI
```

### 2. Initialize the Universal Bridge

```bash
./bin/pai-init
```

This script:
- Checks for dependencies (Python, Git, Bun)
- Generates `PAI_INSTRUCTIONS.md` (for your AI's context)
- Sets up the `.env` file

### 3. Usage with Droid (Factory)

If you use Factory's Droid CLI, you can directly use the provided adapter:
- Point your Droid to `.factory/droids/PAI.md`
- Or copy the content of `PAI_INSTRUCTIONS.md` to your Droid's custom instructions.

### 4. Usage with Other CLIs (Gemini, Open Code, etc.)

Simply load the `PAI_INSTRUCTIONS.md` into the project context. This tells the AI how to use the `bin/pai` CLI and where to find skills.

</details>

<details>
<summary><strong>🍎 macOS (Claude Code)</strong></summary>

### 1. Clone PAI

```bash
git clone https://github.com/danielmiessler/PAI.git ~/PAI
```

### 2. Create Symlink

```bash
# Remove existing ~/.claude if present (backup first if needed)
[ -d ~/.claude ] && mv ~/.claude ~/.claude.backup
ln -s ~/PAI/.claude ~/.claude
```

This symlink approach lets you:
- Pull updates with `cd ~/PAI && git pull`
- Keep your customizations in `~/.claude` (via the symlink)
- Have Claude Code find skills at `~/.claude/skills/` correctly

### 3. Run the Setup Wizard

```bash
~/.claude/tools/setup/bootstrap.sh
```

The bootstrap script handles everything:
- **Shell check** — Recommends zsh or bash if you're using something else
- **Bun install** — Offers to install Bun if not found (PAI's package manager)
- **Claude Code check** — Reminds you to install Claude Code if missing
- **Setup wizard** — Launches the interactive configuration

### 4. Add Your API Keys

```bash
# Copy environment template
cp ~/.claude/.env.example ~/.claude/.env

# Edit with your API keys
nano ~/.claude/.env

# Required: ANTHROPIC_API_KEY
# Optional: ELEVENLABS_API_KEY for voice
```

### 5. Reload Your Shell

```bash
source ~/.zshrc
```

</details>

<details>
<summary><strong>Linux</strong></summary>

### 1. Clone PAI

```bash
git clone https://github.com/danielmiessler/PAI.git ~/PAI
```

### 2. Create Symlink

```bash
# Remove existing ~/.claude if present (backup first if needed)
[ -d ~/.claude ] && mv ~/.claude ~/.claude.backup
ln -s ~/PAI/.claude ~/.claude
```

This symlink approach lets you:
- Pull updates with `cd ~/PAI && git pull`
- Keep your customizations in `~/.claude` (via the symlink)
- Have Claude Code find skills at `~/.claude/skills/` correctly

### 3. Run the Setup Wizard

```bash
~/.claude/tools/setup/bootstrap.sh
```

The bootstrap script handles everything:
- **Shell check** — Recommends zsh or bash if you're using something else
- **Bun install** — Offers to install Bun if not found (PAI's package manager)
- **Claude Code check** — Reminds you to install Claude Code if missing
- **Setup wizard** — Launches the interactive configuration

### 4. Add Your API Keys

```bash
# Copy environment template
cp ~/.claude/.env.example ~/.claude/.env

# Edit with your API keys
nano ~/.claude/.env

# Required: ANTHROPIC_API_KEY
# Optional: ELEVENLABS_API_KEY for voice
```

### 5. Reload Your Shell

```bash
source ~/.bashrc  # or ~/.zshrc if using zsh
```

</details>

<details>
<summary><strong>Windows</strong></summary>

### 1. Clone PAI

```powershell
git clone https://github.com/danielmiessler/PAI.git $env:USERPROFILE\PAI
```

### 2. Create Symlink (Run PowerShell as Administrator)

```powershell
# Remove existing .claude if present (backup first if needed)
if (Test-Path "$env:USERPROFILE\.claude") { Rename-Item "$env:USERPROFILE\.claude" "$env:USERPROFILE\.claude.backup" }
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude" -Target "$env:USERPROFILE\PAI\.claude"
```

This symlink approach lets you:
- Pull updates with `cd ~/PAI; git pull`
- Keep your customizations in `~/.claude` (via the symlink)
- Have Claude Code find skills at `~/.claude/skills/` correctly

### 3. Run the Setup Wizard

```powershell
& "$env:USERPROFILE\.claude\tools\setup\bootstrap.ps1"
```

The bootstrap script handles everything:
- **Bun install** — Offers to install Bun if not found (PAI's package manager)
- **Claude Code check** — Reminds you to install Claude Code if missing
- **Setup wizard** — Launches the interactive configuration

### 4. Add Your API Keys

```powershell
# Copy environment template
Copy-Item "$env:USERPROFILE\.claude\.env.example" "$env:USERPROFILE\.claude\.env"

# Edit with your API keys (use your preferred editor)
notepad "$env:USERPROFILE\.claude\.env"

# Required: ANTHROPIC_API_KEY
# Optional: ELEVENLABS_API_KEY for voice
```

### 5. Reload Your Shell

Close and reopen PowerShell, or run:

```powershell
. $PROFILE
```

</details>

---

## Setup Wizard Options

The interactive wizard configures:

| Option | Description | Default |
|--------|-------------|---------|
| **PAI Directory** | Where to install | `~/.claude` |
| **Your Name** | Auto-detected from git config | — |
| **Your Email** | Auto-detected from git config | — |
| **Assistant Name** | Name your AI | `Assistant` |
| **Color Theme** | blue, purple, green, cyan, red | `blue` |
| **Voice Server** | Text-to-speech (macOS only) | Enabled |
| **Shell Profile** | Add environment variables | Yes |

### Non-Interactive Mode

For automation or scripting:

**macOS/Linux:**
```bash
cd ~/.claude/tools/setup
bun run setup.ts \
  --pai-dir ~/.claude \
  --name "Your Name" \
  --email you@example.com \
  --assistant-name "Nova" \
  --force
```

**Windows:**
```powershell
cd "$env:USERPROFILE\.claude\tools\setup"
bun run setup.ts `
  --pai-dir "$env:USERPROFILE\.claude" `
  --name "Your Name" `
  --email you@example.com `
  --assistant-name "Nova" `
  --force
```

### Dry Run

Preview changes without applying them:

```bash
bun run setup.ts --dry-run
```

---

## First Run

### Start Claude Code

```bash
claude
```

PAI loads automatically via the `SessionStart` hook.

### Try These Commands

```
"What skills are available?"
"Show me my stack preferences"
"What agents do I have access to?"
"Read the CONSTITUTION"
```

---

## Understanding PAI

### The Three Primitives

**1. Skills** (`.claude/skills/`)
- Self-contained AI capabilities
- Auto-activate based on your request
- Package routing, workflows, and documentation

**2. Agents** (`.claude/agents/`)
- Specialized AI personalities
- Engineer, researcher, designer, pentester, etc.
- Each has unique voice and capabilities

**3. Hooks** (`.claude/hooks/`)
- Event-driven automation
- Capture work, provide voice feedback, manage state
- Run automatically on session start/stop, tool use, etc.

### Where Everything Lives

```
~/.claude/
├── skills/
│   └── CORE/                 # Main PAI documentation
│       ├── CONSTITUTION.md   # System philosophy & architecture
│       ├── SKILL.md          # Main skill file (loaded at startup)
│       └── *.md              # Reference documentation
├── agents/                   # Agent configurations
├── hooks/                    # Event automation scripts
├── voice-server/             # Text-to-speech system (macOS)
└── .env                      # Your API keys (never commit!)
```

---

## Troubleshooting

<details>
<summary><strong>PAI Not Loading</strong></summary>

**Check hook configuration:**
```bash
cat ~/.claude/settings.json | grep SessionStart
```

**Manually load CORE skill:**
```
read ~/.claude/skills/CORE/SKILL.md
```

</details>

<details>
<summary><strong>Hooks Not Running</strong></summary>

Hooks require Bun to be installed and in your PATH.

**macOS/Linux:**
```bash
which bun
# Should show: ~/.bun/bin/bun or /opt/homebrew/bin/bun
```

**Windows:**
```powershell
Get-Command bun
# Should show the bun executable path
```

If Bun isn't found, reinstall it and restart your terminal.

</details>

<details>
<summary><strong>Hook Errors Mentioning "__HOME__"</strong></summary>

If you see errors like `No such file or directory: __HOME__/.claude/...`, the `PAI_DIR` variable wasn't configured correctly.

**Fix: Re-run the setup script**
```bash
bash ~/.claude/setup.sh
```

This automatically configures `PAI_DIR` with your actual home directory path.

**Manual fix (if setup script doesn't work):**
```bash
# Edit settings.json
nano ~/.claude/settings.json

# Find this line:
"PAI_DIR": "__HOME__/.claude"

# Replace with your actual path (examples):
# macOS: "PAI_DIR": "/Users/yourusername/.claude"
# Linux: "PAI_DIR": "/home/yourusername/.claude"
```

</details>

<details>
<summary><strong>Voice Server Not Working (macOS only)</strong></summary>

```bash
# Check voice server status
~/.claude/voice-server/status.sh

# Restart if needed
~/.claude/voice-server/restart.sh

# Check logs
tail ~/.claude/voice-server/logs/voice-server.log
```

</details>

<details>
<summary><strong>API Keys Not Working</strong></summary>

```bash
# Verify .env file exists
ls -la ~/.claude/.env

# Check format (no spaces around =)
# Correct: ANTHROPIC_API_KEY=sk-ant-...
# Wrong:   ANTHROPIC_API_KEY = sk-ant-...
```

</details>

---

## Next Steps

1. **Read CONSTITUTION.md** — Understand PAI philosophy
2. **Explore Skills** — See what's available in `~/.claude/skills/`
3. **Try Voice Feedback** — Start the voice server (macOS)
4. **Create Your First Skill** — Follow the skill structure guide

---

## Resources

- **Full Documentation:** `~/.claude/skills/CORE/`
- **Video Overview:** [PAI Video](https://youtu.be/iKwRWwabkEc)
- **GitHub Issues:** [Report Problems](https://github.com/danielmiessler/PAI/issues)
- **Discussions:** [Ask Questions](https://github.com/danielmiessler/PAI/discussions)

---

## Philosophy

PAI follows three principles:

1. **Command Line First** — Build CLI tools, wrap with AI
2. **Deterministic Code First** — Same input → Same output
3. **Prompts Wrap Code** — AI orchestrates, doesn't replace

**Start clean. Start small. Build out from there.**
