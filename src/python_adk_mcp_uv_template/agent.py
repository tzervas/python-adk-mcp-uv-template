import yaml
from google.adk.agents import Agent

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

config = load_config()
agent = Agent(
    name=config["adk"]["agent_name"],
    tools=[sample_tool],
    config={
        "model": config["adk"]["model"],
        "max_tokens": config["adk"]["max_tokens"],
        "temperature": config["adk"]["temperature"],
    },
)
