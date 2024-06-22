from fastapi import APIRouter, Body, HTTPException

from schema.query_input import QueryRequest
from schema.query_output import QueryResponse
from db.query import search_database


router = APIRouter()


@router.post("/search/", response_model=list[QueryResponse])
async def search(data: QueryRequest = Body()):
    try:
        results = search_database(data.query, data.top_k)

        return [
            QueryResponse(
                id=match['id'],
                metadata=match.get('metadata', {})
            ) for match in results['matches']
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
