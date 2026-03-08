from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


model = LiteLlm(
    model='openai/gpt-4o',
    
    )

def tell_joke() -> dict:
    """Tells a random joke."""
    return {"status": "success", "joke": "What do you call a fish with no eyes?   A fsh"}

root_agent = Agent(
    model=model,
    name='joke_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge, but generate jokes when asked for one. Use the "tell_joke" tool for joke requests.',
    tools=[tell_joke],
)
