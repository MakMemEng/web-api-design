import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import user
from routers import book

app = FastAPI()
app.include_router(user.router)
app.include_router(book.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app)
