# 학번: 10101 / 이름: 홍길동 / 주제: 퍼스널 컬러 맞춤 화장품 추천 앱
import streamlit as st

# (1) 시작: 사용자가 앱에 접속함
st.title("💄 10대 맞춤 퍼스널 컬러 화장품 추천 앱")
st.write("나이와 피부톤에 맞는 화장품과 가격대, 소비자 만족도를 확인해 보세요!")  # [직접 수정] 앱 설명 문구 추가

# (2) 리스트 선언: [직접 수정] 10대 학생들의 용돈 수준을 고려해 '가격대' 항목을 리스트에 추가함
warm_tone_cosmetics = [
    ["파운데이션 17호", "92% (자연스러운 톤업)", "18,000원"],
    ["코랄 블러셔", "95% (생기 있는 발색)", "12,000원"],
    ["브릭 레드 립스틱", "89% (지속력 우수)", "15,000원"],
    ["피치 아이섀도우", "94% (데일리로 적합)", "22,000원"],
    ["톤업 선크림", "96% (순한 성분)", "14,000원"]  # [직접 수정] 새 데이터 1개 추가
]

# (3) 입력받기: selectbox와 slider 활용
cosmetic_name = st.selectbox(
    "화장품을 선택하세요",
    ["파운데이션 17호", "코랄 블러셔", "브릭 레드 립스틱", "피치 아이섀도우", "톤업 선크림", "쿨핑크 립틴트"]
)
skin_color = st.selectbox("피부색을 선택하세요", ["웜톤", "쿨톤", "뉴트럴톤"])
user_age = st.slider("나이를 선택하세요", 10, 80, 17)

# (4) 함수 정의: check_list
def check_list(name, skin_color, age):
    # (5) 선택구조 (if - elif - else)
    # [직접 수정] 13세 이하 어린 학생일 경우 색조 대신 선크림을 권유하는 조건을 직접 추가함
    if age <= 13:
        st.warning("13세 이하 학생에게는 색조 화장품보다 순한 '톤업 선크림'을 먼저 추천합니다!")
    elif age <= 17 and name == "파운데이션 17호" and skin_color == "웜톤":
        for item in warm_tone_cosmetics:
            if item[0] == name:
                st.success(f"추천 결과: '{name}'의 소비자 만족도는 **{item[1]}**이며, 가격은 **{item[2]}**입니다!")
    elif skin_color == "웜톤":
        st.info("웜톤 피부를 선택하셨네요! 아래 표에서 추천 화장품의 만족도와 가격을 확인해 보세요.")
    else:
        st.warning("현재는 웜톤 전용 추천 서비스입니다. 피부색을 '웜톤'으로 선택해 보세요!")

    # (6) 반복구조: [직접 수정] 표에 '가격대(item[2])' 열이 함께 출력되도록 수정함
    st.subheader("📋 웜톤 추천 화장품 목록")
    table_text = "| 화장품 이름 | 소비자 만족도 | 가격대 |\n| :--- | :--- | :--- |\n"
    
    for item in warm_tone_cosmetics:
        table_text += f"| {item[0]} | {item[1]} | {item[2]} |\n"
        
    st.markdown(table_text)

# 버튼 클릭 시 함수 실행
if st.button("결과 확인하기"):
    check_list(cosmetic_name, skin_color, user_age)
