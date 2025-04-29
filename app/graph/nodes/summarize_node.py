from app.utils.summarizer import summarize_texts

def summarize_node(inputs):
    """
    요약 노드
    검색 결과(search_results) 리스트를 받아 요약 텍스트를 반환한다.
    """
    search_results = inputs.get('search_results')
    if not search_results:
        raise ValueError("Search results are missing for summarization.")
    
    snippets = [item['snippet'] for item in search_results]
    summary = summarize_texts(snippets)
    
    return {"summary": summary}

