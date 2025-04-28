from fastapi import FastAPI
from pydantic import BaseModel
from app.utils.google_search import google_search

app = FastAPI()  

class SearchRequest(BaseModel):
    topic: str

@app.post("/search")
async def search_topic(request: SearchRequest):
    try:
        results = google_search(request.topic)
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
