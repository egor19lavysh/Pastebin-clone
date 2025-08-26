from fastapi import FastAPI
from src.paste import router as paste_router
from src.infrastucture.database import init_mongo
from contextlib import asynccontextmanager



app = FastAPI()

app.include_router(paste_router)

@app.on_event("startup")
async def init_db():
    try:
        await init_mongo()
        print("MongoDB started")
    except Exception as e:
        print(e)