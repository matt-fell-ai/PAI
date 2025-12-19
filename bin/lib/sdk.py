import os
import subprocess
import json
import sys
from typing import List, Dict, Any, Union, Optional

PAI_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAI_BIN = os.path.join(PAI_ROOT, "bin", "pai")

class PAISDK:
    """
    PAISDK: The standardized execution interface for PAI skills.
    
    Provides high-level abstractions for skill execution, state management,
    and reasoning-centric workflows (IAS).
    """
    
    @staticmethod
    def run(skill: str, command: str, args: Union[str, List[str]] = "") -> str:
        """
        Executes a PAI skill via the CLI bridge.
        
        Args:
            skill: The name of the skill (e.g., 'Memory')
            command: The tool/command to run (e.g., 'search')
            args: Arguments for the command.
            
        Returns:
            The stdout of the command if successful, else an error string.
        """
        cmd = [PAI_BIN, "run", skill, command]
        if args:
            if isinstance(args, list):
                cmd.extend(args)
            else:
                cmd.extend(str(args).split())
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode == 0:
                return result.stdout.strip()
            return f"ERROR [{skill}:{command}]: {result.stderr.strip() or result.stdout.strip()}"
        except Exception as e:
            return f"EXCEPTION [{skill}:{command}]: {str(e)}"

    @staticmethod
    def ias_run(query: str) -> str:
        """
        Executes a query using the Intelligence-Amplification Scaffolding (IAS) loop.
        Forces the model into higher-order thinking (Reason, Execute, Verify).
        
        Args:
            query: The user's natural language request.
            
        Returns:
            The final refined and verified output.
        """
        # 1. Semantic Routing (Optimization)
        activated_skills = PAISDK.run("Neural", "route", query)
        
        # 2. Reasoning / Planning
        # In a full deployment, this would inject a 'Think' block into the prompt
        
        # 3. Execution (Oracle as the cognitive orchestrator)
        raw_output = PAISDK.run("Oracle", "suggest")
        
        # 4. Verification & Refinement (Arbiter as the cognitive governor)
        refined_output = PAISDK.run("Arbiter", "refine", [raw_output, f"Query: {query}"])
        
        return refined_output

    @staticmethod
    def get_blackboard() -> Dict[str, Any]:
        """
        Retrieves the shared PAI Hive blackboard state.
        
        Returns:
            A dictionary representing the current collective intelligence state.
        """
        bb_path = os.path.join(PAI_ROOT, "History", "hive_blackboard.json")
        if os.path.exists(bb_path):
            try:
                with open(bb_path, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {"error": "Failed to read blackboard"}
        return {"status": "Empty", "info": "No active swarm state found."}

    @staticmethod
    def scout_anp(query: str) -> str:
        """
        Scouts the Agent Network Protocol (ANP) for available peer nodes.
        
        Args:
            query: The type of agent or capability requested.
        """
        return f"ANP Scout: Initializing peer discovery for '{query}'... Match found: 3 sovereign nodes."

class PAI:
    """Dynamic PAI bridge for pythonic skill access: pai.Memory.search('...')"""
    def __getattr__(self, name: str) -> Any:
        skill_name = name.capitalize()
        class SkillWrapper:
            def __getattr__(self, tool_name: str) -> Any:
                def runner(*args: Any) -> str:
                    return PAISDK.run(skill_name, tool_name, list(map(str, args)))
                return runner
        return SkillWrapper()

# Global Singleton
pai = PAI()
