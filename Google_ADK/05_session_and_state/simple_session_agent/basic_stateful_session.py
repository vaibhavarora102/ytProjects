from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from question_answering_agent import question_answering_agent
from google.genai import types
import uuid
import asyncio


load_dotenv()

async def main():
    session_Service_stateful = InMemorySessionService()

    initial_state = {
        "user_name": "Alice",
        "user_preferences": {
            "preferred_language": "English",
            "interests": ["technology", "sports"]
        }
    }

    APP_NAME = "Allice bot"
    USER_ID = "alice_123"
    SESSION_ID = str(uuid.uuid4())

    session_id = await session_Service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    print(f"Session created with ID: {session_id}")

    runner = Runner(
        agent=question_answering_agent,
        session_service=session_Service_stateful,
        app_name=APP_NAME,
    )

    new_message = types.Content(
        role="user",
        parts = [types.Part("What is Alice's preferred language?")]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            print(f"Final response: {event.content.parts[0].text}")

    print("=============Session Events==============")
    

    session = await session_Service_stateful.get_session(
        session_id=SESSION_ID, 
        app_name=APP_NAME, 
        user_id=USER_ID
    )

    print("==============Session State:==============")
    # Now 'session' is the actual object, not a coroutine
    for key, value in session.state.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    asyncio.run(main())