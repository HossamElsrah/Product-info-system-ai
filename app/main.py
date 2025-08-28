from fastapi import FastAPI
from pydantic import BaseModel
from crew.crew import product_crew

app = FastAPI()

class ProductRequest(BaseModel):
    product_name: str

@app.post("/research")
async def start_research(request: ProductRequest):
    result = product_crew.kickoff(inputs={'product_name': request.product_name})
    return {"final_report": result}