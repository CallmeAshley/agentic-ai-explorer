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

# 2. StateGraph 초기화
graph = StateGraph(ExplorerState)

# 3. 노드 등록
graph.add_node("search", search_node)
graph.add_node("summarize", summarize_node)
graph.add_node("question", question_node)

# 4. 흐름 정의
graph.set_entry_point("search")
graph.add_edge("search", "summarize")
graph.add_edge("summarize", "question")
graph.set_finish_point("question")

# 5. 그래프 빌드
explorer_flow = graph.compile()
