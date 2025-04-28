import streamlit as st
import requests

st.set_page_config(page_title="🌟 AI 지식 탐험가", page_icon="🌟")

st.title('🌟 AI 지식 탐험가')
st.write('주제를 입력하면 관련 정보를 탐험합니다!')

topic = st.text_input('탐험할 주제를 입력하세요')

if st.button('탐험 시작'):
    if topic:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/explore",
                json={"topic": topic}
            )
            if response.status_code == 200:
                data = response.json()
                
                # 요약 출력
                st.subheader("📝 요약 결과")
                st.success(data.get("summary", "요약이 생성되지 않았습니다."))

                st.divider()

                # 검색 결과 출력
                st.subheader(f"🔎 '{topic}'에 대한 탐험 결과")
                for result in data.get("search_results", []):
                    with st.container():
                        st.markdown(f"### {result['title']}")
                        st.write(result["snippet"])
                        st.markdown(f"[자세히 보기]({result['url']})")
                        st.divider()

                # 추가 질문 출력
                st.subheader("❓ 추가 탐구 질문")
                st.info(data.get("questions", "추가 질문이 생성되지 않았습니다."))
                
            else:
                st.error(f"서버 에러: {response.status_code}")
        except Exception as e:
            st.error(f"요청 중 오류 발생: {e}")
    else:
        st.warning('주제를 입력해 주세요!')
