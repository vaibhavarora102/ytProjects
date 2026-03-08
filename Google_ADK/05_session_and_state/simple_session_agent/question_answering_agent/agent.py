from google.adk.agents.llm_agent import Agent


question_answering_agent = Agent(
    model='gemini-2.5-flash',
    name='question_answering_agent',
    description='A helpful assistant for answering user questions.',
    instruction="""
    Answer user questions to the best of your knowledge
    
    Here is someinformation about the user that might be helpful in answering their questions:
    Name: {user_name}
    Preferences: {user_preferences}

    """,
)
