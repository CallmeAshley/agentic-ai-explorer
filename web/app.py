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
                "http://127.0.0.1:8000/search",
                json={"topic": topic}
            )
            if response.status_code == 200:
                data = response.json()
                if "results" in data:
                    st.success(f"🔍 '{topic}'에 대한 탐험 결과입니다!")
                    for result in data["results"]:
                        with st.container():
                            st.subheader(result["title"])
                            st.write(result["snippet"])
                            st.markdown(f"[자세히 보기]({result['url']})")
                            st.divider()  # 결과 카드 구분선
                else:
                    st.warning('검색 결과가 없습니다.')
            else:
                st.error(f"서버 에러: {response.status_code}")
        except Exception as e:
            st.error(f"요청 중 오류 발생: {e}")
    else:
        st.warning('주제를 입력해 주세요!')
