#python libraries
import os
#Langgchain HumanMessage represents the message of the user
from langchain_core.messages import HumanMessage
#API Router allows you to build endpoints in a modular way instead of placing all in main.py
from fastapi import APIRouter

#built modules
from backend.agents.chat_state import ChatState
from backend.agents.chat_agent import llm_model
from backend.graphs.chatbot_graph import build_chatbot_graph
from backend.utils.helpers import read_logs, write_logs
from backend.api.models import ChatRequest
from backend.config import max_history

#This creates the API Router object
router = APIRouter()

#This builds the file path:
#os.path.dirname(__file__) directory of the current file or where it is running
#, "..", "memory", "conversation_logs.txt") relative path basically os.path.dirname(__file__)<one level up from directory>\memory\conversation_logs.txt
filepath = os.path.join(os.path.dirname(__file__), "..", "memory", "conversation_logs.txt")

#calls the build_chatbot_graph() in chatbot_graph.py
graph = build_chatbot_graph()

#creates variable state as empty list
#Type hint of ChatState class meaning this follows the structure of TypedDict ChatState
state: ChatState = {"messages": []}

#This reads the conversation_logs.txt from filepath above, if not found empty list []
try:
    state["messages"] = read_logs(filepath)
except FileNotFoundError:
    state["messages"] = []

#This function is for health checking. this will show a json in the page {"status" : "ok", "msg" : "Backend running"}
#@router.get() is used to assign this function as a GET endpoint and is part of the router APIRouter object. "/" is the url endpoint
#basically an API
@router.get("/", tags=["health"])
async def root():
    return {"status" : "ok", "msg" : "Backend running"}

#This function calls the llm. sends the user message to the llm and returns response
#@router.post() is used to assign this function as a POST endpoint and is part of the router APIRouter object. "/chat" is the url endpoint
#basically an API
#This receives a request of typehint ChatRequest which is a BaseModel of Pydantic
@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    #this tells the function to use the global variable state declared above which is persistent
    global state
    #this sets the user_message from the function args request
    user_message = request.message
    #adds the user message as a Human message in state["messages"]
    state["messages"].append(HumanMessage(content=user_message))
    #This invokes the graph and passes the current state as well as the user input
    state = graph.invoke({"messages": state["messages"], "user": user_message})
    #This gets the latest message from state which is the AI response from the user message
    ai_reply = state["messages"][-1].content
    #This updates the conversation.txt log file
    write_logs(filepath, state["messages"][-max_history:])
    #This returns the ai response to the caller as json
    return {"reply": ai_reply}