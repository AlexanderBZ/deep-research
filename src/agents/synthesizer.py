from src.agents.state import State
from src.core.llm import get_openai_llm
from src.prompts.prompts import synthesizer_prompt_template
from langchain_core.messages import SystemMessage, AIMessage

def synthesizer(state: State) -> State:
    llm = get_openai_llm()

    result = llm.invoke(
        [
            SystemMessage(content=synthesizer_prompt_template),
            AIMessage(content=state["plan"]),
            AIMessage(content=state["research"]),           
        ]
    )

    return {"final_report": result.content}
