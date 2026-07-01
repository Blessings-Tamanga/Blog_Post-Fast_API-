from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
def show_api():
    return {"message":"Stack-OverNacit is working"}

