from langchain_openai import ChatOpenAI
from src.core.config import get_settings

def get_openai_llm() -> ChatOpenAI:
    config = get_settings()
    return ChatOpenAI(model="gpt-4.1-nano", temperature=0, api_key=config.openai_api_key)
