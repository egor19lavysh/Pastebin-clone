from fastapi import FastAPI
from src.paste import router as paste_router


app = FastAPI()

app.include_router(paste_router)