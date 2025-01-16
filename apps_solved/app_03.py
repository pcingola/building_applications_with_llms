"""
This is a simple chatbot with history
"""

import os
import dotenv
import chainlit as cl

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate


MODEL = 'llama3.2:3b-instruct-fp16'
HISTORY = 'history'


# Read fro `.env` file
dotenv.load_dotenv()
OLLAMA_URL = os.getenv('OLLAMA_URL')
print(f"Using Ollama server: {OLLAMA_URL if OLLAMA_URL else 'local'}")


@cl.on_chat_start
async def on_chat_start():
    # Reset history
    cl.user_session.set(HISTORY, [])


@cl.on_message
async def on_message(message: cl.Message):
    # Get user mesaage and history
    history = cl.user_session.get(HISTORY)
    user_message = message.content
    # All messages = history + current message
    messages = list(history) if history else []
    messages.append(user_message)
    print(f"Messages: {messages}")
    # Create the LLM object
    llm = ChatOllama(model=MODEL, base_url=OLLAMA_URL)
    # Invoke the LLM
    ret = llm.invoke(messages)
    msg = cl.Message(content=ret.content)
    await msg.send()
    # Update history and store it
    messages.append(ret.content)
    cl.user_session.set(HISTORY, messages)
