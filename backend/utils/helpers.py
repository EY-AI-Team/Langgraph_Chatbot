from typing import List, Union
from langchain_core.messages import HumanMessage, AIMessage
from backend.config import max_history

def read_logs(filepath: str) -> List[Union[HumanMessage, AIMessage]]:
    """This function reads the message logs and returns a List"""

    message_logs : List[Union[HumanMessage, AIMessage]] = []
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("You:"):
                message_logs.append(HumanMessage(content=line.replace("You:", "").strip()))
            elif line.startswith("FranzAI:"):
                message_logs.append(AIMessage(content=line.replace("FranzAI:", "").strip()))

    return message_logs

def write_logs(filepath: str, message_logs: List[Union[HumanMessage, AIMessage]]) -> bool:
    """This function writes the message logs in a text file"""
    success = False
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write("Start of conversation: \n")

            for message in message_logs:
                if isinstance(message, HumanMessage):
                    file.write(f"You: {message.content}\n")
                elif isinstance(message, AIMessage):
                    file.write(f"FranzAI: {message.content}\n")
            
            file.write("End of conversation")
        
        success = True
        
    except Exception as e:
        success = False
        print(f"Error writing logs: {str(e)}")
        return success
    
    return success
    