import os
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.anthropic import AnthropicModel
from strands_tools import calculator, current_time, python_repl

# Load environment variables from .env file
load_dotenv()

@tool
def letter_counter(word: str, letter: str) -> int:
    """Counts the occurrences of a letter in a word."""
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")
    return word.lower().count(letter.lower())

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

agent = Agent(model=model, tools=[calculator, letter_counter, current_time, python_repl])
message = """
I have 4 requests:

1. What is the time right now?
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓
4. Output a script that does what we just spoke about!
    Use your python tools to confirm that the script works before outputting it
"""

agent(message)