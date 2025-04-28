# from langgraph.graph import StateGraph
# from app.graph.nodes.search_node import search_node
# from app.graph.nodes.summarize_node import summarize_node
# from app.graph.nodes.question_node import question_node

# # 1. State 정의
# class ExplorerState(dict):
#     topic: str = None
#     search_results: list = None
#     summary: str = None
#     questions: str = None

# # 2. StateGraph 초기화
# graph = StateGraph(ExplorerState)

# # 3. 노드 등록
# graph.add_node("search", search_node)
# graph.add_node("summarize", summarize_node)
# graph.add_node("question", question_node)

# # 4. 흐름 정의
# graph.set_entry_point("search")
# graph.add_edge("search", "summarize")
# graph.add_edge("summarize", "question")
# graph.set_finish_point("question")

# # 5. 그래프 빌드
# explorer_flow = graph.compile()

from langgraph.graph import StateGraph
from app.graph.nodes.search_node import search_node
from app.graph.nodes.summarize_node import summarize_node
from app.graph.nodes.question_node import question_node

# 1. State 정의
class ExplorerState(dict):
    topic: str = None
    search_results: list = None
    summary: str = None
    questions: str = None
    full_response: str = None

# 2. StateGraph 초기화
graph = StateGraph(ExplorerState)

# 3. 노드 등록
graph.add_node("search", search_node)
graph.add_node("summarize", summarize_node)
graph.add_node("question", question_node)

# 4. full_response를 생성하는 추가 노드 생성
def combine_node(inputs):
    """
    검색 결과 + 요약 + 추가 질문을 보기 좋게 결합하여 full_response를 만드는 노드
    """
    search_results = inputs.get("search_results", [])
    summary = inputs.get("summary", "")
    questions = inputs.get("questions", "")

    # 검색 결과 포맷팅
    search_text = ""
    for idx, result in enumerate(search_results, 1):
        title = result.get('title', '')
        url = result.get('url', '')
        search_text += f"{idx}. {title} - {url}\n"

    # 질문 포맷팅 (리스트일 경우 한 줄씩 예쁘게)
    question_text = ""
    if isinstance(questions, list):
        for idx, q in enumerate(questions, 1):
            question_text += f"{idx}. {q}\n"
    elif isinstance(questions, str):
        question_text = questions  # 이미 str이면 그대로

    # full_response 결합
    full_response = f"🔎 검색 결과:\n{search_text}\n📝 요약:\n{summary}\n\n❓ 추가 질문:\n{question_text}"

    return {"full_response": full_response}

# combine_node를 LangGraph에 등록
graph.add_node("combine", combine_node)

# 5. 흐름 정의
graph.set_entry_point("search")
graph.add_edge("search", "summarize")
graph.add_edge("summarize", "question")
graph.add_edge("question", "combine")  # 이제 combine이라는 노드가 존재하니까 연결 가능
graph.set_finish_point("combine")

# 6. 그래프 빌드
explorer_flow = graph.compile()
