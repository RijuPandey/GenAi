from typing import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

class ChatAgentState(TypedDict):
    """
    """
    message: Annotated[list[AnyMessage], operator.add]

# from typing_extensions import TypedDict, Annotated
# from langchain.messages import AnyMessage
# import operator

# class ChatAgentState(TypedDict):
#     """
#     """
#     messages: Annotated[list[AnyMessage], operator.add]