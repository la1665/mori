from pydantic import BaseModel


class QueryResponse(BaseModel):
    id: str
    metadata: dict
