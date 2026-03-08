from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        ..., description="The subject of the email"
        )
    body: str = Field(..., description="The body of the email")





root_agent = Agent(
    model='gemini-2.5-flash',
    name='email_agent',
    description='you are an email generator that helps users write emails based on their query.',
    instruction="""
    You are an assistant that helps users write emails. 
    You will be given a question from the user, and you should respond with an emailwhen requested. 
    
    while writing the email:
    be professional, concise, and clear.
    

    IMPORTANT: Your response should be in JSON format and follow the EmailContent schema.
    {
    "subject": "The subject of the email",
    "body": "The body of the email" 
    }
    """,
    output_key='email_content',
    output_schema=EmailContent,
)
