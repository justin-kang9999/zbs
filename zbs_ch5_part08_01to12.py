# 07. Population 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# import set_matplotlib_hangul
from matplotlib import font_manager
f_path = "C:\WINDOWS\FONTS\malgun.ttf"
font_manager.FontProperties(fname=f_path).get_name()
from matplotlib import rc
rc("font", family='Malgun Gothic')
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings(action="ignore")
%matplotlib inline 
# 데이터 불러오기
population = pd.read_excel("../data/07_population/07_population_raw_data.xlsx", header = 1)
# nan 값을 채워주기
population.fillna(method="pad", inplace=True)
population
# fillna 연습

datas = {
    "A": np.random.randint(1, 45, 8), 
    "B": np.random.randint(1, 45, 8),
    "C": np.random.randint(1, 45, 8),
}

datas
fillna_df = pd.DataFrame(datas)
fillna_df
# nan 값 강제로 주기

fillna_df.loc[2:4, ["A"]] = np.nan
fillna_df.loc[3:5, ["B"]] = np.nan
fillna_df.loc[4:7, ["C"]] = np.nan
fillna_df
# pad 옵션을 이용해서 채우기
'''
기본은 value = 이거
pad 옵션을 주면 앞에 있는 데이터 값을 채워준 것
'''
fillna_df.fillna(method="pad")
# 데이터 정보 확인
population.info()
## 전처리
# 컬럼 이름 변경 

population.rename(
    columns={
        "행정구역(동읍면)별(1)": "광역시도",
        "행정구역(동읍면)별(2)": "시도",
        "계": "인구수"
    }, inplace=True
)

# 소계 제거 
population = population[population["시도"] != "소계"]
# population.head()

population.tail()
# copy시 warning 을 나오게 하지 말아달라
population.is_copy = False 

population.rename(
    columns={"항목": "구분"}, inplace=True 
)
population.head()
# loc의 경우 행, 열 순으로 구분지어짐 loc[행, 열]
population.loc[population["구분"] == "총인구수 (명)", "구분"] = "합계"
population.loc[population["구분"] == "남자인구수 (명)", "구분"] = "남자"
population.loc[population["구분"] == "여자인구수 (명)", "구분"] = "여자"
population.head(3)
# 소멸 지역을 조사를 위한 데이터

# 나이컬럼을 합침
# 청년층
population["20-39세"] = (
    population["20 - 24세"] + population["25 - 29세"] + population["30 - 34세"] + population["35 - 39세"]
)

# 노년층
population["65세이상"] = (
    population["65 - 69세"] + population["70 - 74세"] + population["75 - 79세"] + population["80 - 84세"] + population["85 - 89세"] + population["90 - 94세"] + population["95 - 99세"] + population["100+"]
)
# 확인
population.tail()
# pivot_table 
# 인덱스만 설정하면 기본값이 평균값으로 되어서 데이터 들어감
pop = pd.pivot_table(
    data=population,
    index=["광역시도", "시도"], 
    columns=["구분"],
    values=["인구수", "20-39세", "65세이상"]
)

pop
# 소멸 비율 계산
# 가임기 여성 / 노년층 / 2

pop["소멸비율"] = pop["20-39세", "여자"] / (pop["65세이상", "합계"] / 2)
pop.tail()
# 소멸위기지역 컬럼 생성 
# 1.0보다 낮으면 소멸 위기지역 True
pop["소멸위기지역"] = pop["소멸비율"] < 1.0 
pop

# 소멸위기지역 조회 시도, 컬럼을 기준으로
pop[pop["소멸위기지역"] == True].index.get_level_values(1)
# 광역시도, 시도가 다 컬럼으로 들어옴
pop.reset_index(inplace=True)
pop.head()

pop.columns.get_level_values(0)[5]
# 이중컬럼으로 되어 있는 것을 그냥 컬럼으로 만들기
# 위 아래 컬럼을 더하는 것으로 합치는 for문
tmp_columns = [
    pop.columns.get_level_values(0)[n] + pop.columns.get_level_values(1)[n]
    for n in range(0, len(pop.columns.get_level_values(0)))
]

pop.columns = tmp_columns
pop.head()
## 3. 지도 시각화를 위한 지역별 ID 만들기
# 현재까지 정보 확인
pop.info()
pop["시도"].unique()
si_name = [None] * len(pop)
si_name
# 기초 자치단체 내 구 정리하기
'''
- 만들고자 하는 ID의 형태 
    - 서울 중구 
    - 서울 서초
    - 통영
    - 남양주 
    - 포항 북구 
    - 인천 남동 
    - 안양 만안 
    - 안양 동안 
    - 안산 단원
    ... 등등등
'''
tmp_gu_dict = {
    "수원": ["장안구", "권선구", "팔달구", "영통구"],
    "성남": ["수정구", "중원구", "분당구"],
    "안양": ["만안구", "동안구"],
    "안산": ["상록구", "단원구"],
    "고양": ["덕양구", "일산동구", "일산서구"],
    "용인": ["처인구", "기흥구", "수지구"],
    "청주": ["상당구", "서원구", "흥덕구", "청원구"],
    "천안": ["동남구", "서북구"],
    "전주": ["완산구", "덕진구"],
    "포항": ["남구", "북구"],
    "창원": ["의창구", "성산구", "진해구", "마산합포구", "마산회원구"],
    "부천": ["오정구", "원미구", "소사구"],
}
pop["시도"].unique()
# 원하는 모양
text1 = "서울특별시"
text2 = "종로구"

print(text1[:2] + " " + text2[:-1])
# 지도 id 만들기 : 서울 중구, 이런식으로 합치기
# (1) 일반 시 이름과 세종시, 광역시도 일반 구 정리
for idx, row in pop.iterrows():
    # 마지막글자 3글자인 광역시, 특별시, 자치시 이런 경우
    if row["광역시도"][-3:] not in ["광역시", "특별시", "자치시"]:
        si_name[idx] = row["시도"][:-1] # 임실군이면 임실만 나오도록
    
    elif row["광역시도"] == "세종특별자치시":
        si_name[idx] = "세종"
    
    else:
        # 서울 중구 이런식으로
        if len(row["시도"]) == 2:
            si_name[idx] = row["광역시도"][:2] + " " + row["시도"]
        else: # 두글자가 아닌경우가 훨씬 많으므로 마지막 글자인 구를 빼고 더하도록
            si_name[idx] = row["광역시도"][:2] + " " + row["시도"][:-1]
# (2) 행정구 정리
for idx, row in pop.iterrows():
    if row["광역시도"][-3:] not in ["광역시", "특별시", "자치시"]:
        for keys, values in tmp_gu_dict.items():
            if row["시도"] in values:
                if len(row["시도"]) == 2:
                    si_name[idx] = keys + " " + row["시도"]
                    
                elif row["시도"] in ["마산합포구", "마산회원구"]:
                    si_name[idx] = keys + " " + row["시도"][2:-1] #합포, 회원 이런 것을 떼어오기 위함
                
                else:
                    si_name[idx] = keys + " " + row["시도"][:-1]
# (3) 고성군
'''
고성의 경우 강원도에도 있고 경상남도에도 있으므로 구분하기 위함
'''
for idx, row in pop.iterrows():
    if row["광역시도"][-3:] not in ["광역시", "특별시", "자치시"]:
        if row["시도"][:-1] == "고성" and row["광역시도"] == "강원도": 
            si_name[idx] = "고성(강원)"
        elif row["시도"][:-1] == "고성" and row["광역시도"] == "경상남도": 
            si_name[idx] = "고성(경남)"
si_name
pop["ID"] = si_name
pop
# 필요없는 컬럼 삭제
del pop["20-39세남자"]
del pop["65세이상남자"]
del pop["65세이상여자"]
pop.head()
## 4. 지도 그리기(카르토그램)
# 데이터 불러오기
draw_korea_raw = pd.read_excel("../data/07_population/07_draw_korea_raw.xlsx")
draw_korea_raw
# 스택
draw_korea_raw_stacked = pd.DataFrame(draw_korea_raw.stack())
draw_korea_raw_stacked
# 인덱스 초기화
draw_korea_raw_stacked.reset_index(inplace=True)
draw_korea_raw_stacked
# 커럼 재설정
draw_korea_raw_stacked.rename(
    columns={
        "level_0": "y",
        "level_1": "x",
        0: "ID"
    }, inplace=True
)
draw_korea_raw_stacked
draw_korea = draw_korea_raw_stacked
# 경계선 그리기
BORDER_LINES = [
    [(5, 1), (5, 2), (7, 2), (7, 3), (11, 3), (11, 0)], # 인천
    [(5, 4), (5, 5), (2, 5), (2, 7), (4, 7), (4, 9), (7, 9), (7, 7), (9, 7), (9, 5), (10, 5), (10, 4), (5, 4)], # 서울
    [(1, 7), (1, 8), (3, 8), (3, 10), (10, 10), (10, 7), (12, 7), (12, 6), (11, 6), (11, 5), (12, 5), (12, 4), (11, 4), (11, 3)], # 경기도
    [(8, 10), (8, 11), (6, 11), (6, 12)], # 강원도
    [(12, 5), (13, 5), (13, 4), (14, 4), (14, 5), (15, 5), (15, 4), (16, 4), (16, 2)], # 충청북도
    [(16, 4), (17, 4), (17, 5), (16, 5), (16, 6), (19, 6), (19, 5), (20, 5), (20, 4), (21, 4), (21, 3), (19, 3), (19, 1)], # 전라북도
    [(13, 5), (13, 6), (16, 6)], 
    [(13, 5), (14, 5)], # 대전시 # 세종시
    [(21, 2), (21, 3), (22, 3), (22, 4), (24, 4), (24, 2), (21, 2)], # 광주
    [(20, 5), (21, 5), (21, 6), (23, 6)], # 전라남도
    [(10, 8), (12, 8), (12, 9), (14, 9), (14, 8), (16, 8), (16, 6)], # 충청북도
    [(14, 9), (14, 11), (14, 12), (13, 12), (13, 13)], # 경상북도
    [(15, 8), (17, 8), (17, 10), (16, 10), (16, 11), (14, 11)], # 대구
    [(17, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10), (21, 10)], # 부산
    [(16, 11), (16, 13)],
    [(27, 5), (27, 6), (25, 6)]
]
draw_korea["ID"][13].split()[1]
# 테스트 함수 만들기
def plot_text_simple(draw_korea):
    for idx, row in draw_korea.iterrows():
        if len(row["ID"].split()) == 2:
            dispname = "{}\n{}".format(row["ID"].split()[0], row["ID"].split()[1])
        elif row["ID"][:2] == "고성":
            dispname = "고성"
        else:
            dispname = row["ID"]
            
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 9.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2


        plt.annotate(
            dispname,
            (row["x"] + 0.5, row["y"] + 0.5),
            weight="bold",
            fontsize=fontsize,
            linespacing=linespacing,
            ha="center", # 수평 정렬
            va="center", # 수직 정렬 
        )
# plot_text_simple(draw_korea)
def simpleDraw(draw_korea):
    plt.figure(figsize=(8, 11))
    
    plot_text_simple(draw_korea)
    
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c="black", lw=1.5)
    
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.tight_layout()
    plt.show()
simpleDraw(draw_korea)
pop.head()
draw_korea.head()
## 검증작업

set(draw_korea["ID"].unique()) - set(pop["ID"].unique())

# 검증을 했더니 중복되는 것들이 나옴
set(pop["ID"].unique()) - set(draw_korea["ID"].unique())

tmp_list = list(set(pop["ID"].unique()) - set(draw_korea["ID"].unique()))
# 제거하는 for문
for tmp in tmp_list:
    pop = pop.drop(pop[pop["ID"] == tmp].index)
print(set(pop["ID"].unique()) - set(draw_korea["ID"].unique()))

## merge 
# 좌표값이 추가된 것을 확인
pop = pd.merge(pop, draw_korea, how="left", on="ID")
pop.head()

#### 그림을 그리기 위한 데이터를 계산하는 함수 
'''
- 색상을 만들 때, 최소값을 흰색 
- blockedMap: 인구현황(pop) 
- targetData: 그리고 싶은 컬럼
'''
# 인구소멸 위험도가 높으면 진한 색상으로 
def get_data_info(targetData, blockedMap):
    # 연산하는 변수
    whitelabelmin = (
        max(blockedMap[targetData]) - min(blockedMap[targetData])
    ) * 0.25 + min(blockedMap[targetData])
    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])
    
    mapdata = blockedMap.pivot_table(index="y", columns="x", values=targetData)

    return mapdata, vmax, vmin, whitelabelmin
# 영점
def get_data_info_for_zero_center(targetData, blockedMap):
    whitelabelmin = 5 
    tmp_max = max(
        [np.abs(min(blockedMap[targetData])), np.abs(max(blockedMap[targetData]))]
    )
    vmin, vmax = -tmp_max, tmp_max
    mapdata = blockedMap.pivot_table(index="y", columns="x", values=targetData)
    return mapdata, vmax, vmin, whitelabelmin
# 위에서 연습으로 만들었던 함수 그대로 갖고 옴
def plot_text(targetData, blockedMap, whitelabelmin):
    for idx, row in blockedMap.iterrows():
        if len(row["ID"].split()) == 2:
            dispname = "{}\n{}".format(row["ID"].split()[0], row["ID"].split()[1])
        elif row["ID"][:2] == "고성":
            dispname = "고성"
        else:
            dispname = row["ID"]
            
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 9.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        # 색깔 지정을 위한 변수 추가
        annocolor = "white" if np.abs(row[targetData]) > whitelabelmin else "black"
        
        plt.annotate(
            dispname,
            (row["x"] + 0.5, row["y"] + 0.5),
            weight="bold",
            color=annocolor,
            fontsize=fontsize,
            linespacing=linespacing,
            ha="center", # 수평 정렬
            va="center", # 수직 정렬 
        )
# 카르토그램을 위한 시각화 하는 함수 - 최종
def drawKorea(targetData, blockedMap, cmapname, zeroCenter=False):
    #제로 센터인 경우
    if zeroCenter:
        masked_mapdata, vmax, vmin, whitelabelmin = get_data_info_for_zero_center(targetData, blockedMap)
    
    #제로 센터가 아닌 경우
    if not zeroCenter:
        masked_mapdata, vmax, vmin, whitelabelmin = get_data_info(targetData, blockedMap)
    # 시각화    
    plt.figure(figsize=(8, 11))
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor="#aaaaaa", linewidth=0.5)
    
    plot_text(targetData, blockedMap, whitelabelmin)
    
    # 경계선 그리기
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c="black", lw=1.5)
    
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.tight_layout()
    cb = plt.colorbar(shrink=0.1, aspect=10)
    cb.set_label(targetData) # 컬럼을 기준으로 라벨 붙이기
    plt.show()
pop.head()

# 인구수 합계를 넣은 경우
drawKorea("인구수합계", pop, "Blues")

pop

pop["소멸위기지역"] = [1 if con else 0 for con in pop["소멸위기지역"]]
drawKorea("소멸위기지역", pop, "Reds")

pop.head()

pop["여성비"] = (pop["인구수여자"] / pop["인구수합계"] - 0.5) * 100
drawKorea("여성비", pop, "RdBu", zeroCenter=True)

pop["2030여성비"] = (pop["20-39세여자"] / pop["20-39세합계"] - 0.5) * 100
drawKorea("2030여성비", pop, "RdBu", zeroCenter=True)

# folium을 이용해서 지도 시각화 
import folium
import json 

pop_folium = pop.set_index("ID")
pop_folium.head()

geo_path = "../data/07_population/07_skorea_municipalities_geo_simple.json"
geo_str = json.load(open(geo_path, encoding="utf-8"))

# 인구수합계 지도 시각화

mymap = folium.Map(location=[36.2002, 127.054], zoom_start=7)
mymap.choropleth(
    geo_data=geo_str,
    data=pop_folium["인구수합계"],
    key_on="feature.id",
    columns=[pop_folium.index, pop_folium["인구수합계"]],
    fill_color="YlGnBu"
)

mymap

# 소멸위기지역 지도 시각화
mymap = folium.Map(location=[36.2002, 127.054], zoom_start=7)
mymap.choropleth(
    geo_data=geo_str,
    data=pop_folium["소멸위기지역"],
    key_on="feature.id",
    columns=[pop_folium.index, pop_folium["소멸위기지역"]],
    fill_color="PuRd"
)
# 수도권 밖일수록 소멸위기지역인 못이 많아짐
mymap

# 결과물 데이터 저장 

draw_korea.to_csv("../data/07_draw_korea.csv", encoding="utf-8", sep=",")
