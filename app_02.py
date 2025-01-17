"""
This is a simple chatbot that uses the LLM model to generate responses to user messages.
"""

import os
import dotenv
import chainlit as cl
from langchain_ollama import ChatOllama


MODEL = 'llama3.2:3b-instruct-fp16'


# Read fro `.env` file
dotenv.load_dotenv()
OLLAMA_URL = os.getenv('OLLAMA_URL')
print(f"Using Ollama server: {OLLAMA_URL if OLLAMA_URL else 'local'}")


@cl.on_message
async def on_message(message: cl.Message):
    # Get user mesaage
    user_message = message.content
    # Create the LLM object
    # ADD YOUR CODE HERE
    #
    # Invoke the LLM
    # ADD YOUR CODE HERE
    #
    # Return the response
    # msg = cl.Message(content=ret.content)
    # await msg.send()

