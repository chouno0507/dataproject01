import streamlit as st
import folium
from streamlit_folium import st_folium

# 제목
st.title("북한의 대표적인 건축물 지도")

# 북한 주요 건축물 데이터
buildings = [
    {"name": "주체사상탑", "location": [39.0304, 125.7634]},
    {"name": "금수산태양궁전", "location": [39.0436, 125.7887]},
    {"name": "류경호텔", "location": [39.0315, 125.7557]},
    {"name": "5.1 경기장 (메이데이 스타디움)", "location": [39.0444, 125.7646]},
    {"name": "만수대기념비", "location": [39.0324, 125.7489]},
    {"name": "과학기술전당", "location": [39.0511, 125.7627]},
    {"name": "조선중앙역", "location": [39.0111, 125.7522]},
]

# 지도의 중심 위치는 평양으로 설정
m = folium.Map(location=[39.03, 125.76], zoom_start=13)

# 마커 추가
for b in buildings:
    folium.Marker(
        location=b["location"],
        popup=b["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# Folium 지도를 Streamlit에 렌더링
st_folium(m, width=700, height=500)
