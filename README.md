###Agentic AI Explorer
사용자가 입력한 주제에 따라
실시간으로 정보를 검색하고 요약하여 보여주는 AI 기반 탐험 서비스입니다.

##주요 기능
사용자가 입력한 주제 기반 실시간 검색 (SerpAPI 활용, 구글 검색)

FastAPI 백엔드 서버를 통한 검색 요청 처리

Streamlit 프론트엔드로 카드 형태의 검색 결과 시각화

깔끔한 프로젝트 구조 (app/utils, app/database, web/ 폴더 구성)

##설치 및 실행 방법
1. 레포지토리 클론
git clone https://github.com/본인계정/agentic-ai-explorer.git
cd agentic-ai-explorer

2. 
pip install -r requirements.txt

3. .env 파일 생성 후 SerpAPI API Key 설정
SERPAPI_API_KEY=본인의_SerpAPI_키

4. FastAPI 서버 및 Streamlit 웹앱 실행
uvicorn app.main:app --reload
streamlit run web/app.py

##사용 기술 (Tech Stack)
FastAPI : 검색 API 서버 구축
Streamlit : 사용자 인터페이스(UI) 개발
SerpAPI : 구글 검색 결과 수집
Python 3.10
