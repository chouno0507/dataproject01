import streamlit as st
import folium
from streamlit_folium import st_folium

# 제목
st.title("북한의 대표적인 건축물 지도")

# 북한 주요 건축물 데이터 (이름, 위치, 설명 포함)
buildings = [
    {
        "name": "주체사상탑",
        "location": [39.0304, 125.7634],
        "description": "북한 주체사상의 상징인 탑. 높이 170m로, 1982년 김일성 70회 생일을 기념하여 건립됨."
    },
    {
        "name": "금수산태양궁전",
        "location": [39.0436, 125.7887],
        "description": "김일성과 김정일의 시신이 안치된 영묘. 원래는 금수산기념궁전으로 사용됨."
    },
    {
        "name": "류경호텔",
        "location": [39.0315, 125.7557],
        "description": "105층짜리 미완공 고층 호텔로 평양의 상징적인 건축물. 1987년 공사 시작."
    },
    {
        "name": "5.1 경기장 (메이데이 스타디움)",
        "location": [39.0444, 125.7646],
        "description": "세계 최대 규모의 경기장으로, 최대 수용인원은 150,000명. 다양한 대규모 행사 개최."
    },
    {
        "name": "만수대기념비",
        "location": [39.0324, 125.7489],
        "description": "김일성과 김정일의 대형 동상이 있는 장소로, 북한의 대표적인 정치 상징 공간."
    },
    {
        "name": "과학기술전당",
        "location": [39.0511, 125.7627],
        "description": "과학기술의 발전을 홍보하기 위한 전시 공간 및 도서관. 원자 모양을 본뜬 외관이 특징."
    },
    {
        "name": "조선중앙역",
        "location": [39.0111, 125.7522],
        "description": "평양의 주요 철도역. 클래식한 건축양식으로 유명하며, 교통 중심지 역할 수행."
    },
]

# 지도의 중심 위치는 평양
m = folium.Map(location=[39.03, 125.76], zoom_start=13)

# 마커 추가
for b in buildings:
    popup_content = f"<b>{b['name']}</b><br>{b['description']}"
    folium.Marker(
        location=b["location"],
        popup=folium.Popup(popup_content, max_width=300),
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# Folium 지도를 Streamlit에 렌더링
st_folium(m, width=700, height=500)
