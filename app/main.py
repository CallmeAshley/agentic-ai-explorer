from fastapi import FastAPI
from pydantic import BaseModel
from app.utils.google_search import google_search
from app.utils.summarizer import summarize_texts
from app.graph.flow import explorer_flow

app = FastAPI()  # 이게 반드시 있어야 해!

class SearchRequest(BaseModel):
    topic: str

@app.post("/search")
async def search_topic(request: SearchRequest):
    try:
        results = google_search(request.topic)
        # 검색 결과 중 snippet만 뽑아서 리스트 생성
        snippets = [r["snippet"] for r in results]
        # LangChain으로 요약
        summary = summarize_texts(snippets)
        return {
            "results": results,
            "summary": summary
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/explore")
async def explore_topic(request: SearchRequest):
    try:
        # 주제를 기반으로 플로우 실행
        result = explorer_flow.invoke({"topic": request.topic})
        return result
    except Exception as e:
        return {"error": str(e)}