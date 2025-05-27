import streamlit as st
# app.py

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# 제목
st.title("서초구 고등학교 지도")

# 예시 고등학교 데이터 (실제 데이터로 교체 가능)
data = {
    "학교명": [
        "서울고등학교", "세화고등학교", "세화여자고등학교",
        "은광여자고등학교", "서초고등학교", "상문고등학교"
    ],
    "위도": [
        37.494719, 37.500752, 37.500341,
        37.481172, 37.490053, 37.487903
    ],
    "경도": [
        127.008409, 126.998940, 126.999859,
        127.018803, 127.026957, 127.020527
    ]
}

df = pd.DataFrame(data)

# 지도 초기화 (서초구 중심)
m = folium.Map(location=[37.49, 127.01], zoom_start=13)

# 학교 마커 추가
for idx, row in df.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=row["학교명"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 표시
folium_static(m)
