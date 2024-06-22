from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.search import router as search_router


app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "file:///Users/amir/Code/mori/frontend/index.html"
    # Add more origins if needed
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
