from fastapi import FastAPI, HTTPException
from routes.router import router

app = FastAPI()
app.include_router(routes)

@app.get()
def get_health():
    return {"message":"API is working"}

