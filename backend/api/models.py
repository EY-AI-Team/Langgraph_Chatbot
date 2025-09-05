#Pydantic is a library for data validation and settings management
#it makes sure that the data this class receives is the correct one matching type and structure
#if not it will return error of 400 Bad Request
#BaseModel is a base class in Pydantic, it allows you to define fields and its types
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str