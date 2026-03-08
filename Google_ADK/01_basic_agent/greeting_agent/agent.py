from google.adk.agents import Agent


root_agent = Agent(
    name="greeting_agent",
    description="A simple agent that greets the user.",
    model = "gemini-3-flash-preview",
    instruction="""
    You are a helpful assistant that greets the user.
    """,
)