# Folium turorial

import pandas as pd

cctv_csv = pd.read_csv(r"C:\Users\hym49\Desktop\Python Workspace\Python\10days_analytics_challenge\서울시 용산구 (안심이) CCTV 설치 현황.csv", encoding = "cp949")

print(cctv_csv.head())

#데이터 프레임 NaN 값 대체
cctv_csv = cctv_csv.fillna(0.0)

# x좌표(경도), y좌표(위도) 리스트로 만들기
x = []
y = []

for i in range(len(cctv_csv["위도"])):
    if cctv_csv["위도"][i] == 0.0 or cctv_csv["경도"][i] == 0.0:
        pass
    else:
        x.append(cctv_csv["경도"][i])
        y.append(cctv_csv["위도"][i])

#지도 생성 및 마커 지정하기
import folium

map_osm = folium.Map(location=[y[20], x[20]], zoom_start=14)

for i in range(len(x)):
    folium.Marker([y[i],x[i]], popup='용산구 CCTV_%d' %i,
                  icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)

#범위 지정
folium.CircleMarker(location=[y[20],x[20]], popup='용산구 CCTV',
                    radius=300, color="#3186cc",
                    fill_color="#3186cc").add_to(map_osm)

#map 출력
map_osm.save("marked_map.html")


import folium
import pandas as pd
import json

geo_json = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"

datas = pd.read_csv("자치구별_총인구_2022년(추계인구).csv", encoding ="cp949", usecols=['자치구별(2)', '2022'])

seoul_counts = datas[["자치구별(2)", "2022"]]
seoul_counts.columns = ["name", "values"]
seoul_counts = seoul_counts.sort_values(by = "name")

m = folium.Map(
    location = [37.5502,126.982],
    tiles="OpenStreetMap",
    zoom_start = 11.2
)


folium.Choropleth(
    geo_data = geo_json,
    name = 'choropleth',
    data = seoul_counts,
    columns = ["name", "values"],
    key_on = "feature.properties.name",
    highlight = True,
    fill_color = "PuRd",
    fill_opacity = 0.5,
    line_opacity = 1
).add_to(m)

m.save("categorial_map.html")

#6-5 '서울 열린데이터광장'에서 '서울시 동 공무원(정원/구별) 통계'를 다운받아 범주별로 시각화시켜보세요.

import folium
import pandas as pd
import json

geo_json = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"

datas = pd.read_csv('동_공무원(정원)_2021.csv')

print(datas.columns)


datas = pd.read_csv('동_공무원(정원)_2021.csv', usecols=['동별(2)','소계'])

officer_counts = datas[['동별(2)', '소계']]
officer_counts.columns = ['name', 'values']
officer_counts = officer_counts.sort_values(by = 'name')

m = folium.Map(
    location = [37.5502, 126.982],
    tiles = 'openstreetmap',
    zoom_start = 11.2
)

folium.Choropleth(
    geo_data = geo_json,
    name = 'choropleth',
    data = officer_counts,
    columns = ['name', 'values'],
    key_on = 'feature.properties.name',
    highlight = True,
    fill_color = 'PuRd',
    fill_opacity = 0.5,
    line_opacity = 1
).add_to(m)

m.save("ex_categotial_map.html")