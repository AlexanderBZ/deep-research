from src.agents.state import State
from langgraph.prebuilt import create_react_agent
from langchain_tavily import TavilySearch
from src.core.llm import get_openai_llm
from src.core.config import get_settings
from src.prompts.prompts import researcher_prompt_template

def researcher(state: State) -> State:
    settings = get_settings()
    tools = [TavilySearch(max_results=3, api_key=settings.tavily_api_key)]

    agent = create_react_agent(
        model=get_openai_llm(),
        tools=tools,
        prompt=researcher_prompt_template,
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": state["plan"]}]}
    )

    return {"research": result["messages"][-1].content, "messages": result["messages"]}