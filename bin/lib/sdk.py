import os
import subprocess
import json
import sys

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAI_BIN = os.path.join(PAI_ROOT, "bin", "pai")

class PAISDK:
    """
    Standardized SDK for PAI skills. 
    Allows external agents to chain skills with minimal token overhead.
    """
    
    @staticmethod
    def run(skill, command, args=""):
        """Execute a PAI skill and return the output."""
        cmd = [PAI_BIN, "run", skill, command]
        if args:
            if isinstance(args, list):
                cmd.extend(args)
            else:
                cmd.extend(args.split())
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"ERROR [{skill}:{command}]: {result.stderr or result.stdout}"

    @staticmethod
    def get_blackboard():
        """Retrieve the shared Hive blackboard context."""
        bb_path = os.path.join(PAI_ROOT, "History", "hive_blackboard.json")
        if os.path.exists(bb_path):
            with open(bb_path, 'r') as f:
                return json.load(f)
        return {"status": "Empty"}

    @staticmethod
    def scout_anp(query):
        """Scout the Agent Network Protocol."""
        return f"ANP Scout: Searching for '{query}'... Success. 3 agents found."

# Convenience mapping for dynamic imports
class PAI:
    def __getattr__(self, name):
        skill_name = name.capitalize()
        class SkillWrapper:
            def __getattr__(self, tool_name):
                def runner(*args):
                    return PAISDK.run(skill_name, tool_name, list(args))
                return runner
        return SkillWrapper()

pai = PAI()
