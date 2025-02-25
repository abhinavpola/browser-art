import os

llm_name = "gpt-4o"  # NOTE: this should be the suffix following "llm." in the corresponding config.toml section
agent_name = "gpt_agent"
for i in range(100):
    os.system(f"sh ../websites/experiment_opendevin.sh --behavior_id={i} --llm_name={llm_name} --agent_name={agent_name} --env_name=hbb")