from fastapi import FastAPI

import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/identify")
async def identify():
    return {"message": f"I am process {os.getpid()} on {os.uname().nodename}"}

@app.get("/app1")
async def app1():
    return {"message": f"I am app 1 on {os.environ.get('SERVICE_ID')}"}

@app.get("/app2")
async def app2():
    return {"message": f"I am app 2 on {os.environ.get('SERVICE_ID')}"}

@app.get("/admin")
async def app2():
    return {"message": f"I am admin on {os.environ.get('SERVICE_ID')}"}
