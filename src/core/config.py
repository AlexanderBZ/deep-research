from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    openai_api_key: str = Field(alias='openai_api_key')
    tavily_api_key: str = Field(alias='tavily_api_key')
    

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    """
    Get the settings
    """
    return Settings()