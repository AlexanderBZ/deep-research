from pydantic import BaseModel

class PlanRequest(BaseModel):
    query: str