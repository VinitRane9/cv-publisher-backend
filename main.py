from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


# CORS setup - allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend domain for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
