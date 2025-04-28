import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def question_node(inputs):
    """
    추가 질문 생성 노드
    요약 결과를 바탕으로 추가 질문을 생성한다.
    """
    summary = inputs.get('summary')
    if not summary:
        raise ValueError("Summary is missing for question generation.")
    
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name="gpt-3.5-turbo",
        temperature=0.5
    )
    
    prompt = f"""
요약된 내용을 바탕으로 사용자가 더 깊이 탐구할 수 있도록 유도하는 추가 질문 3개를 만들어주세요.
요약: {summary}
"""
    response = llm.predict(prompt)
    
    return {"questions": response}
