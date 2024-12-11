from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import todos
from app.models.engine import create_db_and_tables

app = FastAPI()

create_db_and_tables()

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}