from fastapi import FastAPI
from database import create_db_and_tables
from models import Query
from routers import queries 
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app : FastAPI):
    create_db_and_tables()
    yield()

app = FastAPI(lifespan = lifespan)

app.include_router(queries.router)



