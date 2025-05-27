import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("북한의 건축물, 관광지 및 군사 기지 지도")

# 데이터 분류별 저장
buildings = [
    {
        "name": "주체사상탑",
        "location": [39.0304, 125.7634],
        "description": "북한 주체사상의 상징인 탑. 1982년 건립.",
    },
    {
        "name": "금수산태양궁전",
        "location": [39.0436, 125.7887],
        "description": "김일성과 김정일의 시신이 안치된 영묘.",
    },
    {
        "name": "류경호텔",
        "location": [39.0315, 125.7557],
        "description": "105층 고층 미완공 호텔.",
    },
    {
        "name": "5.1 경기장",
        "location": [39.0444, 125.7646],
        "description": "세계 최대 규모의 경기장.",
    },
    {
        "name": "만수대기념비",
        "location": [39.0324, 125.7489],
        "description": "김일성·김정일 동상이 있는 기념비.",
    },
    {
        "name": "과학기술전당",
        "location": [39.0511, 125.7627],
        "description": "과학 기술 전시관 및 도서관.",
    },
    {
        "name": "조선중앙역",
        "location": [39.0111, 125.7522],
        "description": "평양 중심 철도역.",
    },
]

tourist_sites = [
    {
        "name": "금강산",
        "location": [38.6592, 128.2132],
        "description": "북한의 대표적인 절경 산. 관광 개발 지역.",
    },
    {
        "name": "묘향산",
        "location": [40.0064, 126.3162],
        "description": "유서 깊은 산과 보현사 사찰이 있는 관광지.",
    },
    {
        "name": "백두산",
        "location": [41.8025, 128.0556],
        "description": "한반도 최고봉. 천지 호수가 유명.",
    },
]

military_bases = [
    {
        "name": "원산 해군기지",
        "location": [39.1522, 127.4433],
        "description": "동해안에 위치한 북한 해군 주둔 기지.",
    },
    {
        "name": "평양 방공기지",
        "location": [39.0450, 125.7800],
        "description": "수도 방어를 위한 미사일 및 레이더 기지.",
    },
    {
        "name": "무수단리 미사일 발사장",
        "location": [40.8551, 129.6666],
        "description": "장거리 미사일 시험장.",
    },
]

# 지도 생성
m = folium.Map(location=[39.03, 125.76], zoom_start=6)

# 마커 추가 함수
def add_markers(data, icon_color):
    for item in data:
        popup_content = f"<b>{item['name']}</b><br>{item['description']}"
        folium.Marker(
            location=item["location"],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=icon_color, icon="info-sign")
        ).add_to(m)

# 각 분류별 마커 추가
add_markers(buildings, "red")
add_markers(tourist_sites, "blue")
add_markers(military_bases, "black")

# 지도 출력
st_folium(m, width=800, height=600)
