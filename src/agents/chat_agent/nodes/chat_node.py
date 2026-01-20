# from src.agents.chat_agent.tools.date_time import get_current_date_and_time
# from src.agents.chat_agent.states.chat_agent_state  import ChatAgentState
# from langchain.prompt.chat 
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import os

from itertools import chain
from src.agents.chat_agent.tools.date_time import get_current_date_and_time
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState
from langchain_core.prompts.chat import ChatPromptTemplate
from src.agents.chat_agent.tools.web_search_tool import search_the_web
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from src.agents.chat_agent.tools.date_time import get_current_date_and_time

load_dotenv(override=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

template = """
You are a hindi chat.assistant. answer only in bengali irrespective of language.
Message History:
{message_history}
"""

def chat(state: ChatAgentState) -> ChatAgentState:
    """

    """
    prompt_template = ChatPromptTemplate.from_template(template=template)
    
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API_KEY,
    )
    model = model.bind_tools(
        tools=[
            get_current_date_and_time,
            search_the_web
        ]
    )
    
    chain = prompt_template | model
    
    answer = chain.invoke({
        "message_history": state["message"]
    })
    
    # model.bind_tools(tools=[get_current_date_and_time])
    # answer = model.invoke(state["message"])
    return{
        "message" : [answer]
    }

