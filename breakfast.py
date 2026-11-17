import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env (if present) before initializing LangChain
load_dotenv()

# Verify required keys are loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found. Set it in your environment variables or .env file.")

if os.getenv("LANGSMITH_TRACING", "").lower() == "true" and not os.getenv("LANGSMITH_API_KEY"):
    raise ValueError("LANGSMITH_TRACING is enabled, but LANGSMITH_API_KEY is missing.")

# Initialize the ChatOpenAI model (LangSmith traces this automatically when env vars are set)
llm = ChatOpenAI(model="gpt-4o-mini")

prompt = (
    "Give me exactly 5 healthy, high-protein vegetarian breakfast ideas. "
    "Format the output as a numbered list from 1 to 5, one line per item, "
    "with no introductory text or concluding remarks."
)

reply = llm.invoke(prompt)
print(reply.content)