from app.utils.google_search import google_search

def search_node(inputs):
    """
    검색 노드
    입력된 topic을 받아 구글 검색 결과를 반환한다.
    """
    topic = inputs.get('topic')
    if not topic:
        raise ValueError("Topic is missing for search.")
    
    search_results = google_search(topic)
    
    return {"search_results": search_results}
