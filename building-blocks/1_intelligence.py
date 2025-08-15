from mymodel import model
from strands import Agent


agent = Agent(model=model)

# Calling Agent
response = agent("What is a Square?")
print(response)