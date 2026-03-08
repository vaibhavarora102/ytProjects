from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext


def get_nerd_joke(topic: str, tool_context: ToolContext) -> dict:
    """Get a nerdy joke about a specific topic."""
    print(f"--- Tool: get_nerd_joke called for topic: {topic} ---")

    # Example jokes - in a real implementation, you might want to use an API
    jokes = {
        "python": "Why did the Python programmer quit his job? He didn't get all the arrays (raises).",
        "javascript": "How do you comfort a JavaScript developer? You console.log them.",
        "java": "Why do Java developers wear glasses? Because they can't C#!", # Keeping this one; it's a classic.
        "programming": "A SQL query walks into a bar, walks up to two tables, and asks, 'Can I join you?'",
        "math": "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "physics": "What is a physicist's favorite food? Fission chips.",
        "chemistry": "I was going to tell a joke about sodium... but then I thought, 'Na.'",
        "biology": "What does a biologist use to take notes? A spiral cell-book.",
        "default": "There are 10 types of people in the world: those who understand binary, and those who don't.",
    }

    joke = jokes.get(topic.lower(), jokes["default"])

    # Update state with the last joke topic
    tool_context.state["last_joke_topic"] = topic

    return {"status": "success", "joke": joke, "topic": topic}


# Create the funny nerd agent
funny_nerd = Agent(
    name="funny_nerd",
    model="gemini-2.5-flash",
    description="An agent that tells nerdy jokes about various topics.",
    instruction="""
    You are a funny nerd agent that tells nerdy jokes about various topics.
    
    When asked to tell a joke:
    1. Use the get_nerd_joke tool to fetch a joke about the requested topic
    2. If no specific topic is mentioned, ask the user what kind of nerdy joke they'd like to hear
    3. Format the response to include both the joke and a brief explanation if needed
    
    Available topics include:
    - python
    - javascript
    - java
    - programming
    - math
    - physics
    - chemistry
    - biology
    
    Example response format:
    "Here's a nerdy joke about <TOPIC>:
    <JOKE>
    
    Explanation: {brief explanation if needed}"

    If the user asks about anything else, 
    you should delegate the task to the manager agent.
    """,
    tools=[get_nerd_joke],
)
