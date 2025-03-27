from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Allow CORS (for frontend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get OpenAI API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Fix: Initialize OpenAI client properly
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Request model
class ChatRequest(BaseModel):
    message: str

# Chatbot endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message

    # ✅ Fix: Use the correct OpenAI v1.0+ syntax
    response = client.chat.completions.create(
        model="gpt-4o",  # ✅ Use "gpt-4o" (check your available models)
        messages=[
            {"role": "system", "content": "You are a helpful real estate assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content.strip()
    return {"reply": bot_reply}