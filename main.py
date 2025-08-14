import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator

# Load environment variables from .env file
load_dotenv()

model = AnthropicModel(
    client_args={
        "api_key": os.getenv("ANTHROPIC_API_KEY")
    },
    max_tokens=1028,
    model_id="claude-sonnet-4-20250514",
    params={
        "temperature": 0.7
    }
)

agent = Agent(model=model, tools=[calculator])
response = agent("What is the sum of 5 and 3?")
print(response)