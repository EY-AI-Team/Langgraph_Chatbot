from langgraph.graph import StateGraph, START, END
from backend.agents.chat_state import ChatState
from backend.agents.chat_agent import chat_agent


def build_chatbot_graph():
    """This builds the graph using Langgraph StateGraph"""

    graph = StateGraph(ChatState)
    graph.add_node("chatbot", chat_agent)
    graph.add_edge(START, "chatbot")
    graph.add_edge("chatbot", END)

    return graph.compile()
