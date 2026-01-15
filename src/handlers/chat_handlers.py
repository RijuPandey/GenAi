from src.agents.chat_agent.graph import create_chat_agent_graph
from langchain.messages import HumanMessage, AnyMessage
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

graph =create_chat_agent_graph()
def chat_handler(thread_id: str, message: str) -> ChatAgentState:
    """
    Recieves a message from user and sends it after modification.
    
    Args: 
        message (str): The message sent by the user.
        
    Returns:
        dict[str, str]: A dictionary containing the modified message.
    
    """


    
    return graph.invoke(
        input ={ 
            "message": [HumanMessage(content=message)]
        },
        config={
            "configurable":{
                "thread_id": thread_id
            }
        }
    )
def get_all_threads_handler() -> list[str]:
    """
    """
    all_checkpoints = graph.checkpointer.list(config={})
    
    threads = set()
    
    for checkpoint in all_checkpoints:
        threads.add(checkpoint.config["configurable"]["thread_id"])
    
    return list(threads)
    
def chat_history_handler(thread_id: str) :
    """

    """
    return graph.checkpointer.get(
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )["channel_values"]
        