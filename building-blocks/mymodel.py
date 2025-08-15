from strands.models.anthropic import AnthropicModel
import os
from dotenv import load_dotenv

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