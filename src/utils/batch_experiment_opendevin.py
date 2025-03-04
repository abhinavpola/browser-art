import os

llm_name = "gemini-thinking"  # NOTE: this should be the suffix following "llm." in the corresponding config.toml section
agent_name = "gemini_thinking_agent_da"
port = 3333  # Default port

skips = [65, 66, 67, 68]
for i in range(100):
    if i in skips:
        continue
    os.system(f"sh ../websites/experiment_opendevin.sh --behavior_id={i} --llm_name={llm_name} --agent_name={agent_name} --env_name=hbb --port={port}")