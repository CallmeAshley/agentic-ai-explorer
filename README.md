## Agentic AI Explorer
사용자가 입력한 주제에 따라 실시간으로 정보를 검색하고 요약하여 보여주는 AI 기반 탐험 서비스입니다.  
검색 결과를 기반으로 추가적인 질문을 자동 생성하여, 사용자가 주제에 대해 더욱 깊이 탐구할 수 있도록 유도합니다.  


### 주요 기능
주제 기반 실시간 검색: SerpAPI를 이용해 구글 검색 결과 수집

FastAPI 백엔드: 검색 요청 처리 및 데이터 제공

Streamlit 프론트엔드: 카드 형태로 검색 결과 및 요약 출력

LangChain 통합: 검색 결과 텍스트 요약

LangGraph 플로우 설계: 검색 → 요약 → 추가 질문 생성까지 자동화된 에이전트 구성

RAG(Retrieval-Augmented Generation) 적용: 검색 결과를 기반으로 요약 및 추가 질문을 결합한 응답 생성

### 설치 및 실행 방법
1. 레포지토리 클론
git clone https://github.com/본인계정/agentic-ai-explorer.git  
cd agentic-ai-explorer

2. pip install -r requirements.txt

3. .env 파일 생성 후 API 키 설정  
   SERPAPI_API_KEY=your_serpapi_key  
   OPENAI_API_KEY=your_openai_api_key

4. FastAPI 서버 및 Streamlit 웹앱 실행  
uvicorn app.main:app --reload  
streamlit run web/app.py

### 사용 기술 (Tech Stack)
FastAPI: 검색 및 요청 처리를 위한 백엔드  
Streamlit: 결과를 시각적으로 표현하는 프론트엔드  
SerpAPI: 구글 검색 결과 수집을 위한 API  
LangChain: 검색 결과 요약을 위한 툴  
LangGraph: 에이전트 기반 워크플로우 설계를 위한 프레임워크 (검색 → 요약 → 질문 생성)  
Python: 프로그래밍 언어  
