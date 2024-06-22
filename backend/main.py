from fastapi import FastAPI
from routers.search import router as search_router


app = FastAPI()
app.include_router(search_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
