from src.agents.state import State
from src.core.llm import get_openai_llm
from langchain_core.messages import SystemMessage
from src.prompts.prompts import planner_prompt_template
from langchain_core.prompts import ChatPromptTemplate

def planner(state: State) -> State:
    user_feedback = state["feedback"]

    template = ChatPromptTemplate.from_messages(
        [
            ("system", planner_prompt_template),
            ("user", "Please take into account the user's feedback: {feedback}"),
        ]
    )

    llm = get_openai_llm()

    chain = template | llm

    result = chain.invoke({"feedback": user_feedback})
    plan = result.content

    return {
        "plan": plan,
        "messages": [result]
    }
