from src.agents.state import State
from src.core.llm import get_openai_llm
from langchain_core.messages import SystemMessage
from src.prompts.prompts import planner_prompt_template

def planner(state: State) -> State:
    llm = get_openai_llm()

    system_message = SystemMessage(
        content=planner_prompt_template
    )

    result = llm.invoke([system_message, *state["messages"]])
    content = result.content
    return {
        "plan": content,
        "messages": [result]
    }
