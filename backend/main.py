import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

build_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "build")
build_path = os.path.abspath(build_path)

app.mount("/static", StaticFiles(directory=os.path.join(build_path, "static")), name="static")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(build_path, "index.html"))

app.include_router(router, prefix="/api")


# def main():

#     filepath = "./memory/conversation_logs.txt"

#     try:
#         messages = read_logs(filepath)
#     except FileNotFoundError:
#         messages = []
    

#     state: ChatState = {"messages" : messages}

#     graph = build_chatbot_graph()

#     print("I am FranzAI\n\n What should we talk about today? You can stop the chat with 'exit', 'quit', 'goobye', or 'bye'")
    
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
#             write_logs(filepath, state["messages"][-max_history:])
#             break

#         state["messages"].append(HumanMessage(content=user_input))

#         state = graph.invoke(state)

#         ai_response = state["messages"][-1].content
#         print(f"\nFranzAI: {ai_response}\n")

# if __name__ == "__main__":
#     main()
