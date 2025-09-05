import os
from dotenv import load_dotenv

base_dir = os.path.dirname(__file__)
env_path = os.path.join(base_dir, ".env")
load_dotenv(env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

max_history = 20

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in environment")