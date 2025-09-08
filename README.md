# Langgraph_Chatbot
This is a langgraph chatbot. This uses langgrap, FastAPI, React, and Tailwind

PREREQUISITE:
1. This codebase uses GROQ as its llm model provider (mainly because it is free). You will need to procure your API key from GROQ website and create a .env file on project root folder with key name: GROQ_API_KEY="your api key"

Instructions:

1. Clone Repository to your local machine
2. Open Root folder in visual studio code
(backend setup)
3. If terminal in VS code is not open start one
4. make sure you are in the root folder
5. type python -m venv venv
6. once venv is created type .\venv\Scripts\Activate
7. you will know that virtual environment is working once terminal has a green (venv) on the start of the new line
8. Next type pip install -r requirements.txt -> This will install all python packages required for this process


(frontend setup)
1. make sure you have Node.js -> you can find it here: https://nodejs.org/en/download and download latest LTS version
2. now back to VS code type cd frontend in terminal
3. type npm install

(how to run)
1. in vs code terminal
2. make sure you are at the root folder
3. make sure venv is activated
4. type uvicorn backend.main:app --reload
5. type cd frontend
6. type npm run build
7. open browser
8. navigate to: http://127.0.0.1:8000

If there are any issues do let me know!

Also if you will use this, please provide your feedback and criticisms on the project and where I might be able to improve upon on the code!

If you want to collaborate my next projects are: building RAG agents, and Automation agents. Send me an email or message on teams so we can discuss!
