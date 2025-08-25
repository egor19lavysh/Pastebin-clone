from fastapi import FastAPI


app = FastAPI()


@app.get("/ping")
def ping_app():
    return {"msg": "app started!"} 