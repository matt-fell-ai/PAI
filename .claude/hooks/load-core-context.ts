#!/usr/bin/env bun

/**
 * load-core-context.ts
 *
 * Automatically loads your CORE skill context at session start by reading and injecting
 * the CORE SKILL.md file contents directly into Claude's context as a system-reminder.
 *
 * Purpose:
 * - Read CORE SKILL.md file content
 * - Output content as system-reminder for Claude to process
 * - Ensure complete context (contacts, preferences, security, identity) available at session start
 * - Bypass skill activation logic by directly injecting context
 *
 * Setup:
 * 1. Customize your ${PAI_DIR}/skills/CORE/SKILL.md with your personal context
 * 2. Add this hook to settings.json SessionStart hooks
 * 3. Ensure PAI_DIR environment variable is set (defaults to $HOME/.claude)
 *
 * How it works:
 * - Runs at the start of every Claude Code session
 * - Skips execution for subagent sessions (they don't need CORE context)
 * - Reads your CORE SKILL.md file
 * - Injects content as <system-reminder> which Claude processes automatically
 * - Gives your AI immediate access to your complete personal context
 */

import { readFileSync, existsSync } from 'fs';
import { join } from 'path';
import { PAI_DIR, SKILLS_DIR } from './lib/pai-paths';

async function main() {
  try {
    // Check if this is a subagent session - if so, exit silently
    const claudeProjectDir = process.env.CLAUDE_PROJECT_DIR || '';
    const isSubagent = claudeProjectDir.includes('/.claude/agents/') ||
                      process.env.CLAUDE_AGENT_TYPE !== undefined;

    if (isSubagent) {
      // Subagent sessions don't need CORE context loading
      console.error('🤖 Subagent session - skipping CORE context loading');
      process.exit(0);
    }

    // Get CORE skill path using PAI paths library
    const coreSkillPath = join(SKILLS_DIR, 'CORE/SKILL.md');

    // Verify CORE skill file exists
    if (!existsSync(coreSkillPath)) {
      console.error(`❌ CORE skill not found at: ${coreSkillPath}`);
      console.error(`💡 Ensure CORE/SKILL.md exists or check PAI_DIR environment variable`);
      process.exit(1);
    }

    console.error('📚 Reading CORE context from skill file...');

    // Read the CORE SKILL.md file content
    let coreContent = readFileSync(coreSkillPath, 'utf-8');

    // NEW: Inject Executive Essence (PXE) Attributes
    const essencePath = join(PAI_DIR, '../essence.json');
    let essenceReminder = '';
    if (existsSync(essencePath)) {
      try {
        const essenceData = JSON.parse(readFileSync(essencePath, 'utf-8'));
        const e = essenceData.essence;
        essenceReminder = `
[EXECUTIVE ESSENCE ACTIVE]
Mode: ${essenceData.operational_mode}
Attributes: Intelligence ${e.intelligence}, Candor ${e.candor}, Humor ${e.humor}, Agency ${e.agency}, Loyalty ${e.loyalty}, Curiosity ${e.curiosity}
Instructions: You are currently tuned to ${essenceData.operational_mode} mode. Adjust your verbosity, analytical depth, and autonomy to match these sliders.
`;
      } catch (err) {
        console.error('Warning: Could not parse essence.json');
      }
    }

    // Perform Dynamic Variable Substitution
    // This allows SKILL.md to be generic while the session is personalized
    const daName = process.env.DA || 'PAI';
    const daColor = process.env.DA_COLOR || 'blue';
    const engineerName = process.env.ENGINEER_NAME || 'User';

    // Replace placeholders {{DA}}, {{DA_COLOR}}, {{ENGINEER_NAME}}
    coreContent = coreContent
      .replace(/\{\{DA\}\}/g, daName)
      .replace(/\{\{DA_COLOR\}\}/g, daColor)
      .replace(/\{\{ENGINEER_NAME\}\}/g, engineerName);

    console.error(`✅ Read ${coreContent.length} characters from CORE SKILL.md (Personalized for ${engineerName} & ${daName})`);

    // Output the CORE content as a system-reminder
    // This will be injected into Claude's context at session start
    const message = `<system-reminder>
PAI CORE CONTEXT (Auto-loaded at Session Start)

📅 CURRENT DATE/TIME: ${new Date().toLocaleString('en-US', { timeZone: process.env.TIME_ZONE || 'America/Los_Angeles', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false, timeZoneName: 'short' })}

The following context has been loaded from ${coreSkillPath}:

${essenceReminder}

---
${coreContent}
---

This context is now active for this session. Follow all instructions, preferences, and guidelines contained above.
</system-reminder>`;

    // Write to stdout (will be captured by Claude Code)
    console.log(message);

    console.error('✅ CORE context injected into session');
    process.exit(0);
  } catch (error) {
    console.error('❌ Error in load-core-context hook:', error);
    process.exit(1);
  }
}

main();
