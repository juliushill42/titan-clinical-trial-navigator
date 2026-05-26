from fastapi import FastAPI
from agent import Agent18
app = FastAPI(title="Clinical-Trial-Navigator")
agent = Agent18()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
