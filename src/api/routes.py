from fastapi import APIRouter
from src.agents.state import State
from src.agents.graph import build_graph
from src.api.schemas import PlanRequest

router = APIRouter()

@router.get("/health")
def health_check():
    return {"message": "running..."}

@router.post("/research")
def plan(request: PlanRequest):
    initial_state: State = {
        "messages": [request.query],
        "plan": "",
        "feedback": "",
        "research": "",
        "final_report": ""
    }

    graph = build_graph()
    result = graph.invoke(initial_state)
    return {"plan": result["plan"], "research": result["research"], "final_report": result["final_report"], "messages": result["messages"]}