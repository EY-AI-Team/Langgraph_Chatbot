from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage


class ChatState(TypedDict):
    messages : List[Union[HumanMessage, AIMessage]]