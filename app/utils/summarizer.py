import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 요약하는 함수
def summarize_texts(texts: list) -> str:
    # 여러 텍스트를 LangChain의 Document 형태로 변환
    documents = [Document(page_content=text) for text in texts]
    
    # OpenAI 모델 초기화 (gpt-3.5-turbo 사용)
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name="gpt-3.5-turbo",
        temperature=0.3
    )
    
    # Summarization Chain 로딩
    chain = load_summarize_chain(llm, chain_type="stuff")
    
    # 요약 실행
    summary = chain.run(documents)
    return summary
