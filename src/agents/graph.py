from src.agents.state import State
from src.agents.planner import planner
from src.agents.plan_review import plan_approval
from src.agents.researcher import researcher
from src.agents.synthesizer import synthesizer
from langgraph.graph import StateGraph, START, END

def build_graph() -> StateGraph:
    builder = StateGraph(State)

    builder.add_node("planner", planner)
    builder.add_node("plan_approval", plan_approval)
    builder.add_node("researcher", researcher)
    builder.add_node("synthesizer", synthesizer)


    builder.add_edge(START, "planner")
    builder.add_edge("planner", "plan_approval")
    builder.add_edge("plan_approval", "researcher")
    builder.add_edge("researcher", "synthesizer")
    builder.add_edge("synthesizer", END)

    graph = builder.compile()

    return graph