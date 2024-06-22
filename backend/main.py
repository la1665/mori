from fastapi import FastAPI
from routers.search import router as search_router
# from schema.query_input import QueryRequest
# from schema.query_output import QueryResponse
# from database import query

app = FastAPI()


# @app.post("/search/", response_model=list[QueryResponse])
# async def search(data: QueryRequest = Body()):
#     try:
#         results = query.search_database(data.query, data.top_k)

#         return [
#             QueryResponse(
#                 id=match['id'],
#                 metadata=match.get('metadata', {})
#             ) for match in results['matches']
#         ]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


app.include_router(search_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
