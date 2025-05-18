from typing import Literal
from langgraph.types import interrupt, Command
from src.agents.state import State
from src.core.llm import get_openai_llm
from langchain_core.prompts import ChatPromptTemplate
from src.prompts.prompts import plan_review_prompt_template

def plan_approval(state: State) -> Command[Literal["planner", "researcher"]]:
    user_feedback = interrupt(
        {
            "question": "Do you approve of this plan?",
            "plan": state["plan"],
        }
    )

    state["feedback"] = user_feedback

    template = ChatPromptTemplate.from_messages(
        [
            ("system", plan_review_prompt_template),
            ("user", "Here is the plan: {plan}"),
            ("user", "Here is the user's feedback: {feedback}"),
        ]
    )

    llm = get_openai_llm()

    chain = template | llm.with_structured_output(Literal["planner", "researcher"])
    result = chain.invoke({"plan": state["plan"], "feedback": user_feedback})
    
    if result == "planner":
        return Command(goto="planner", state=state)
    else:
        return Command(goto="researcher", state=state)