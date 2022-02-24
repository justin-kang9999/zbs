# 18 - 21 seaborn 
from matplotlib import font_manager
f_path = "C:\WINDOWS\FONTS\malgun.ttf"
font_manager.FontProperties(fname=f_path).get_name()
from matplotlib import rc
rc("font", family='Malgun Gothic')
import matplotlib.pyplot as plt
import seaborn as sns
# 마이너스로 한글이 깨지는 것을 방지하기 위함
from matplotlib import rc
plt.rcParams["axes.unicode_minus"] = False
#rc("font", family='Malgun Gothic')
plt.rcParams['font.family'] = 'Malgun Gothic'

%matplotlib inline

# 사용하는 모듈 불러오기
import pandas as pd
import numpy as np
# seaborn은 import 하는 것만으로도 효과를 줌
x = np.linspace(0, 14, 100)
y1 = np.sin(x)
y2 = 2 * np.sin(x + 0.5)
y3 = 3 * np.sin(x + 1.5)
y4 = 4 * np.sin(x + 1.5)

# 시각화
plt.figure(figsize= (10, 6))
plt.plot(x, y1, x, y2, x, y3, x, y4)
plt.show()
# white 스타일
sns.set_style("white") # 그리드가 없어지고 흰화면만
plt.figure(figsize= (10, 6))
plt.plot(x, y1, x, y2, x, y3, x, y4)
sns.despine() # 테두리가 왼쪽, 아랫쪽만 남도록
plt.show()

# dark 스타일
sns.set_style("dark")
plt.figure(figsize= (10, 6))
plt.plot(x, y1, x, y2, x, y3, x, y4)
plt.show()

# whitegrid 스타일
sns.set_style("whitegrid")
plt.figure(figsize= (10, 6))
plt.plot(x, y1, x, y2, x, y3, x, y4)
plt.show()

# despine 적용
plt.figure(figsize= (10, 6))
plt.plot(x, y1, x, y2, x, y3, x, y4)
sns.despine(offset= 10) # 왼쪽 아랫쪽 붙어있어야 하는 테두리가 떨어짐
plt.show()
# 실습 tips 데이터 활용
tips = sns.load_dataset("tips")
tips.head(5)
# boxplot 그려보기
plt.figure(figsize=(8,6))
sns.boxplot(x=tips["total_bill"])
plt.show()

# boxplot에 컬럼 지정하기
plt.figure(figsize=(8,6))
sns.boxplot(x="day", y= "total_bill", data=tips)
plt.show()
# boxplot은 컬럼을 지정하고 구분 할 수 있다
plt.figure(figsize=(8,6))
sns.boxplot(x="day", y= "total_bill", hue="smoker" , data=tips, palette="Set3")
plt.show()
# swarmplot 데이터의 분포를 보여줌
plt.figure(figsize=(8,6))
sns.swarmplot(x="day", y= "total_bill", data=tips, color=".5")
plt.show()
# boxplot과 swarmplot 한번에 보이도록
# boxplot에 컬럼 지정하기
plt.figure(figsize=(8,6))
sns.boxplot(x="day", y= "total_bill", data=tips)
sns.swarmplot(x="day", y= "total_bill", data=tips, color=".25")

plt.show()
# total bill과 tip 사이의 관계 파악
sns.set_style("darkgrid")
sns.lmplot(x="total_bill", y="tip", data=tips, size=7)
plt.show()

# hue 옵션을 사용
sns.set_style("darkgrid")
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips, size=7)
plt.show()
# flights 데이터 셋
flights = sns.load_dataset("flights")
flights.head(5)

# pivot 옵션 이용하기
flights = flights.pivot("month", "year", "passengers")
flights.head(5)

# heatmap을 이용해 전체적 경향을 알아보기
plt.figure(figsize=(10, 8))
sns.heatmap(flights, annot=True, fmt="d")
plt.show()

# 컬러 색상을 다르게

plt.figure(figsize=(10, 8))
sns.heatmap(flights, annot=True, fmt="d", cmap="YlGnBu")
plt.show()
sns.set(style="ticks")
# iris 데이터셋도 존재함
iris = sns.load_dataset("iris")
iris.head(5)
# 다수의 컬럼을 비교하는 pairplot
sns.pairplot(iris)
plt.show()

# pairplot에서도 hue 옵션을 사용할 수 있다
sns.pairplot(iris, hue="species")
plt.show()
#원하는 것만 pairplot 할 수 있다
sns.pairplot(
    iris, x_vars=["sepal_width", "sepal_length"], y_vars=["petal_width", "petal_length"]
)
plt.show()
#anscombe 데이터셋
anscombe = sns.load_dataset("anscombe")
anscombe.head(5)
#lmplot으로 확인해보기
sns.set_style("darkgrid")
#데이터 셋에서 "I"인 것만 갖고와서 시각화
#ci 옵션은 신뢰구간
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"), 
           ci=None, size=7)
plt.show()
#데이터 셋에서 "I"인 것만 갖고와서 시각화2
# 마커(점) 사이즈 조정
# order 옵션 : 다항식 회귀 추정을 위해 사용
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           order=1,
           ci=None, scatter={"s" : 80}, size=7)
plt.show()
#데이터 셋에서 "II"인 것만 갖고와서 시각화
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=1,
           ci=None, scatter={"s" : 80}, size=7)
plt.show()

#데이터 셋에서 "II"인 것만 갖고와서 시각화02
# order = 2를 사용하면 곡선으로 표현됨
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"), 
           order=2,
           ci=None, scatter={"s" : 80}, size=7)
plt.show()
#데이터 셋에서 "III"인 것만 갖고와서 시각화

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           ci=None, scatter={"s" : 80}, size=7)
plt.show()

# 경향성에서 강하게 벗어난 것을 확인하려면
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter={"s" : 80}, size=7)
plt.show()

# 22- 23 범죄현황 데이터 시각화
# 데이터 불러오기
crime_anal_norm = pd.read_csv("../data/20220224_ crime_anal_norm.csv", encoding="utf-8")
crime_anal_norm.head()
#seaborn의 pairplot을 통해 강도 살인 폭력에 대한 상관관계 찾아보기
sns.pairplot(crime_anal_norm, vars=["강도", "살인", "폭력"], kind="reg", size=3)
# 인구수, cctv와 살인, 강도와의 관계도 
def draw_plot():
    sns.pairplot(
        crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars=["살인", "강도"], 
        kind="reg", height=4
    )
    plt.show()
draw_plot()

#인구수, cctv와 살인/폭력 검거율의 관계도 
def draw_plot02():
    sns.pairplot(
        crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars=["살인검거율", "폭력검거율"], 
        kind="reg", height=4
    )
    plt.show()
draw_plot02()
#인구수, cctv와 절도/강도 검거율의 관계도 
def draw_plot03():
    sns.pairplot(
        crime_anal_norm, x_vars=["인구수", "CCTV"], y_vars=["절도검거율", "강도검거율"], 
        kind="reg", height=4
    )
    plt.show()
draw_plot03()
# 검거율만 갖고 히트맵 
# 검거율의 대표값인 검거를 기준으로 정렬
def draw_graph():
    target_col = ["강간검거율", "강도검거율", "살인검거율", "절도검거율",
                  "폭력검거율", "검거"]
    crime_anal_norm_sort = crime_anal_norm.sort_values(by="검거", ascending=False)
    plt.figure(figsize=(10, 10))
    sns.heatmap(
        crime_anal_norm_sort[target_col],
        annot= True,
        fmt= "f",
        linewidths=0.5,
        cmap="RdPu"
    )
    plt.title("범죄 검거 비율(정규화된 검거의 합으로 정렬)")
    plt.show()
draw_graph()
# 범죄 발생 건수로 히트맵 
# 대표값인 범죄를 기준으로 정렬
def draw_graph02():
    target_col = ["강간", "강도", "살인", "절도",
                  "폭력", "범죄"]
    crime_anal_norm_sort = crime_anal_norm.sort_values(by="범죄", ascending=False)
    plt.figure(figsize=(10, 10))
    sns.heatmap(
        crime_anal_norm_sort[target_col],
        annot= True,
        fmt= "f",
        linewidths=0.5,
        cmap="RdPu"
    )
    plt.title("범죄비율(정규화된 건수를 기준으로 정렬)")
    plt.show()
draw_graph02()
#저장
crime_anal_norm.to_csv("../data/20220224_crime_in_seoul_final.csv"
                       ,sep="," , encoding="utf-8")

# 24-28 강 Folium 지도 시각화
'''
- Folium : 지도 시각화 도구
- 현재 가장 많이 사용됨
- 설치 방법 : conda install -c conda-forge folium
'''

import folium
import json
# 위도와 경도 알려주면 그 위치 지도를 보여줌
m = folium.Map(location=[45.5236, -122.6750])
m
#지도를 html로 저장 가능하다
m.save("../data/index.html")
#get_ipython().run_line_magic("ls", "../data/")


# 스타일을 tiles 옵션으로 지정
m = folium.Map(location=[45.5236, -122.6750], tiles="Stamen Toner", zoom_start=13)
# 마커 추가
my_map = folium.Map(location=[45.372, -121.6972], zoom_start=13, tiles="Stamen Terrain")
folium.Marker([45.3288, -121.6625], popup="<i>Mt. Hood Meadow</i>").add_to(my_map)
folium.Marker([45.3311, -121.7113], popup="<b>Timberline Lodge</b>").add_to(my_map)
m
# 아이콘
m = folium.Map(
    location= [37.544564958079896, 127.05582307754338], # 성수역
    zoom_start=14,
    tiles="OpenStreetMap"
)
# 아이콘 기본
folium.Marker((37.54712311308356, 127.04721916917774),
              icon=folium.Icon(color="red", info="info-sigh")).add_to(m)
# 아이콘 색상 적용
folium.Marker(
    location= [37.544564958079896, 127.05582307754338],
    popup= "<b>Subway</b>",
    tooltip="<i>성수역</i>",
    icon=folium.Icon(color="red",
                     icon_color="pink",
                     icon="cloud")).add_to(m)

# 아이콘 커스머아징
folium.Marker(
    location= [37.54035903907497, 127.06913328776446], #건대입구
    popup= "건대입구",
    tooltip="Icon custom",
    icon=folium.Icon(color="purple",
                     icon_color="green",
                     icon="android",
                     angle=50,
                     prefix="fa")#fa 대신 glyphicon 넣어서 사용해도 됨
).add_to(m)
m


### folium.ClickForMarker()
'''
- 지도위 클릭 했을 때 마커 생성
- folium.ClickForMarker() popup 따로 설정 안하면 위도 경도 표시가 된다
'''
### folium.LatLngPopup()

### folium.Circle(), folium.CircleMarker()
# 마커생성
m = folium.Map(
    location= [37.544564958079896, 127.05582307754338], # 성수역
    zoom_start=14,
    tiles="OpenStreetMap"
)
m.add_child(folium.ClickForMarker(popup="ClickForMarker"))
#folium.LatLngPopup()

m = folium.Map(
    location= [37.544564958079896, 127.05582307754338], # 성수역
    zoom_start=14,
    tiles="OpenStreetMap"
)
m.add_child(folium.LatLngPopup()) #옵션이 없음
#folium.Circle()
m = folium.Map(
    location= [37.544564958079896, 127.05582307754338], # 성수역
    zoom_start=14,
    tiles="OpenStreetMap"
)
m.add_child(folium.Circle())
#folium.Circle()
m = folium.Map(
    location= [37.544564958079896, 127.05582307754338], # 성수역
    zoom_start=14,
    tiles="OpenStreetMap"
)
folium.Circle(
    location=[37.544564958079896, 127.05582307754338],
    radius= 100,
    fill=True, # 색상 채우기 기본은 false
    color ="green",
    fill_color="red",
    popup="Circle Popup",
    tooltip="Circle Tooltip"
).add_to(m)
m
# folium.CircleMarker()
m = folium.Map(
    location= [37.544564958079896, 127.05582307754338], # 성수역
    zoom_start=14,
    tiles="OpenStreetMap"
)
folium.CircleMarker(
    location=[37.544564958079896, 127.05582307754338],
    radius= 100,
    fill=True, # 색상 채우기 기본은 false
    color ="green",
    fill_color="red",
    popup="Circle Popup",
    tooltip="Circle Tooltip"
).add_to(m)
m
### folium.Choropleth()
import json
#실업률 데이터 불러오기
state_data = pd.read_csv("../data/02_crime/02. US_Unemployment_Oct2012.csv")
state_data.head(2)
m= folium.Map([43, -102], zoom_start=3)
folium.Choropleth(
    geo_data="../data/02_crime/02. us-states.json", # 경계선 좌표값이 담긴 파일
    data=state_data, # 데이터프레임
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="BuPu",
    fill_opacity=1,
    line_opacity=1,
    legend_name="Unemployment rate(%)"
).add_to(m)
m
### 아파트 유형 지도 시각화

df = pd.read_csv("../data/02_crime/02. 서울특별시 동작구_주택유형별 위치 정보 및 세대수 현황_20210825.csv", encoding="cp949")
df.head(2)
# 기본 전처리
#원본 데이터에서 nan값 삭제
df = df.dropna()
df.info()
#인덱스 초기화
df = df.reset_index(drop=True)
# columns에서 한칸씩 띄워져 있는 컬럼이름이 있으므로 재설정
df= df.rename(columns={"연번 " :"연번", "분류 " : "분류"})
# 연번 컬럼을 삭제
del df["연번"]

# 각 위도 경도를 지도에 마커로 찍어줄 것
# 기본 지도
m = folium.Map(
    location=[37.50589466533131, 126.93450729567374],
    zoom_start=13
)
for idx, row in df.iterrows():
    # 위도경도 갖고오기
    lat, lng = row.위도, row.경도
    # 마커 찍기
    folium.Marker(
        location=[lat, lng],
        popup=row.주소,
        tooltip=row.분류,
        icon=folium.Icon(
            icon="home",
            color= "lightred" if row.세대수 >= 199 else "lightblue",
            icon_color = "darkred" if row.세대수 >=199 else "darkblue"
        )
    ).add_to(m)
    # circl() 사용
    folium.Circle(
        location=[lat, lng],
        radius = row.세대수 * 0.5,
        fill=True,
        color= "pink" if row.세대수 >= 518 else "green",
        fill_color= "pink" if row.세대수 >= 518 else "green"
    ).add_to(m)
m
# 29 - 30강 서울시 범죄 현황 지도 시각화

# 서울시 구별로 경계가 표시된 json파일 불러오기

crime_anal_norm = pd.read_csv("../data/02_crime/02. crime_in_Seoul_final.csv", 
                              index_col=0, encoding="utf-8")

geo_path = "../data/02_crime/02. skorea_municipalities_geo_simple.json"
geo_str = json.load(open(geo_path, encoding="utf-8"))
# 지도
my_map = folium.Map(
    location = [37.5502, 126.982],
    zoom_start = 11,
    tiles = "Stamen Toner"
)


# 살인발생건수 지도 시각화
# 경계 그리기, 살인을 기준으로 시각화
folium.Choropleth(
    geo_data = geo_str, # 경계선 좌표값이 담긴 데이터
    data = crime_anal_norm["살인"],
    columns = [crime_anal_norm.index, crime_anal_norm["살인"]],
    key_on = "feature.id",
    fill_color = "PuRd",
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = "정규화된 살인 발생 건수"    
).add_to(my_map)
my_map
# 성범죄 기준으로 시각화
folium.Choropleth(
    geo_data = geo_str, 
    data = crime_anal_norm["강간"],
    columns = [crime_anal_norm.index, crime_anal_norm["강간"]],
    key_on = "feature.id",
    fill_color = "PuRd",
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = "정규화된 강간 발생 건수"    
).add_to(my_map)
my_map
# 5대범죄 발생건수 지도 시각화
folium.Choropleth(
    geo_data = geo_str, 
    data = crime_anal_norm["범죄"],
    columns = [crime_anal_norm.index, crime_anal_norm["범죄"]],
    key_on = "feature.id",
    fill_color = "PuRd",
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = "정규화된 5대 범죄 발생 건수"    
).add_to(my_map)
my_map
#인구대비 범죄 발생 건수
tmp_criminal = crime_anal_norm["범죄"] / crime_anal_norm["인구수"]

my_map = folium.Map(
    location = [37.5502, 126.982],
    zoom_start = 11,
    tiles = "Stamen Toner"
)

folium.Choropleth(
    geo_data = geo_str, 
    data = tmp_criminal ,
    columns = [crime_anal_norm.index, tmp_criminal],
    key_on = "feature.id",
    fill_color = "PuRd",
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = "인구대비 범죄 발생 건수"    
).add_to(my_map)
my_map
# 경찰서별 정보를 범죄 발생과 함께 정리
crime_anal_station = pd.read_csv("../data/02_crime/02. crime_in_Seoul_raw.csv",
                                 encoding="utf-8"
)
crime_anal_station.head()
# 정규화
col = ["살인검거", "강도검거", "강간검거", "절도검거", "폭력검거"]
tmp = crime_anal_station[col] / crime_anal_station[col].max()
crime_anal_station["검거"] = np.mean(tmp, axis=1) #여기서 numpy에서 axis = 1하면 행(가로), pandas에서는 열(세로)

# 경찰서 위치 마커 표시
my_map = folium.Map(
    location = [37.5502, 126.982],
    zoom_start = 11,
)

for idx, rows in crime_anal_station.iterrows():
    folium.Marker(
        location = [rows["lat"], rows["lng"]]
    ).add_to(my_map)
my_map
    
# 경계선 표시, 검거율에 따른 circle marker 표시

my_map = folium.Map(
    location = [37.5502, 126.982],
    zoom_start = 11,
)
# 경계선 표시 
folium.Choropleth(
    geo_data = geo_str,
    data = crime_anal_norm["범죄"],
    columns = [crime_anal_norm.index, crime_anal_norm["범죄"]],
    key_on = "feature.id",
    fill_color = "PuRd",
    fill_opacity = 0.7,
    line_opacity = 0.2,
).add_to(my_map)

# 검거에 값을 곱한뒤 원의 넓이를 적용함
for idx, rows in crime_anal_station.iterrows():
    folium.CircleMarker(
        location = [rows["lat"], rows["lng"]],
        radius = rows["검거"] * 50,
        popup = rows["구분"] + " : " + "%.2f" % rows["검거"],
        color = "#3186cc",
        fill = True, 
        fill_color = "#3186cc"
    ).add_to(my_map)
my_map
    

# 31 - 32강 서울시 범죄현황 장소별 분석
# 추가 검증
crime_loc_raw = pd.read_csv("../data/02_crime/02. crime_in_Seoul_location.csv",
                            thousands=",", encoding="euc-kr")
crime_loc_raw.head(2)
crime_loc_raw.info()
crime_loc_raw.범죄명.unique()

crime_loc = crime_loc_raw.pivot_table(
    crime_loc_raw, index="장소", columns="범죄명",
    aggfunc=[np.sum]
)
crime_loc.columns = crime_loc.columns.droplevel([0,1])
crime_loc.tail(2)
# 정규화
col = ["살인", "강도", "강간", "절도", "폭력"]
crime_loc_norm = crime_loc / crime_loc.max()
crime_loc_norm
crime_loc_norm["종합"] = np.mean(crime_anal_norm, axis=1)
crime_loc_norm.tail(2)
# 시각화

# 내림차순으로 정렬
crime_loc_norm_sort = crime_loc_norm.sort_values("종합", ascending=False)

# 함수화
def draw_graph():
    plt.figure(figsize=(10,10))
    sns.heatmap(
        crime_loc_norm_sort,
        annot=True,
        fmt="f",
        linewidths= 0.5,
        cmap="RdPu")
    plt.title("범죄 발생 장소")
    plt.show()
draw_graph()