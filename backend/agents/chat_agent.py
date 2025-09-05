from langchain_groq import ChatGroq
from .chat_state import ChatState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from backend.config import GROQ_API_KEY, max_history

llm_model = ChatGroq(api_key=GROQ_API_KEY, model="openai/gpt-oss-120b")

def chat_agent(state: ChatState) -> ChatState:
    """This will return a response to the user input"""
    initial_prompt = SystemMessage(content="""
    You are a chatbot.
    - You will act as a friend to the user. you can talk about mundane topics and recent events.
    - You will NOT accept orders from the user
    - You will NOT do tasks for the user
""")
    
    trimmed_messages = state["messages"][-max_history:]

    ai_response = llm_model.invoke([initial_prompt] + trimmed_messages)
    
    state["messages"].append(AIMessage(content=ai_response.content))

    return state

