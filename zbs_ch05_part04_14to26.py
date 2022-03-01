## 14-16 강 시카고 맛집 데이터 분석 - 메인페이지 분석 
'''
- https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/ 
- chicago magazine the 50 best sandwiches

최종목표
총 51개 페이지에서 각 가게의 정보를 가져온다 
- 가게이름 
- 대표메뉴
- 대표메뉴의 가격 
- 가게주소
'''
#!pip install fake-useragent
from urllib.request import Request, urlopen 
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url_base = "https://www.chicagomag.com/"
url_sub = "Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/"
url = url_base + url_sub  
ua = UserAgent()
req = Request(url, headers={"user-agent": ua.ie})
html = urlopen(req)
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

soup.find_all("div", "sammy"), len(soup.find_all("div", "sammy"))
# soup.select(".sammy"), len(soup.select(".sammy"))
tmp_one= soup.find_all("div", "sammy")[0]
type(tmp_one)
tmp_one.find(class_="sammyRank").get_text()
# tmp_one.select_one(".sammyRank").text

# 확인
tmp_one
tmp_one.find("div", {"class":"sammyListing"}).get_text()
# tmp_one.select_one(".sammyListing").text

tmp_one.find("a")["href"]
# tmp_one.select_one("a").get("href")

# 정규표현식 사용을 위한 모듈 갖고오기
import re 

tmp_string = tmp_one.find(class_="sammyListing").get_text()
re.split(("\n|\r\n"), tmp_string)
# menu
print(re.split(("\n|\r\n"), tmp_string)[0])
# cafe 
print(re.split(("\n|\r\n"), tmp_string)[1]) 
from urllib.parse import urljoin 

url_base = "http://www.chicagomag.com"

# 필요한 내용을 담을 빈 리스트 
# 리스트로 하나씩 컬럼을 만든 뒤에 데이터프레임으로 합치기 
rank = [] 
main_menu = [] 
cafe_name = [] 
url_add = [] 

list_soup = soup.find_all("div", "sammy") # soup.select(".sammy")

for item in list_soup: 
    rank.append(item.find(class_="sammyRank").get_text())
    tmp_string = item.find(class_="sammyListing").get_text() 
    main_menu.append(re.split(("\n|\r\n"), tmp_string)[0])
    cafe_name.append(re.split(("\n|\r\n"), tmp_string)[1])
    url_add.append(urljoin(url_base, item.find("a")["href"]))
    
# 길이 확인
len(rank), len(main_menu), len(cafe_name), len(url_add)

rank[:5]
main_menu[:5]
cafe_name[:5]
url_add[:5]

# 데이터 프레임으로 합치기
import pandas as pd 

data = {
    "Rank": rank, 
    "Menu": main_menu,
    "Cafe": cafe_name,
    "URL": url_add, 
}

df = pd.DataFrame(data)
df.tail(2)

# 컬럼의 순서 변경
df = pd.DataFrame(data, columns=["Rank", "Cafe", "Menu", "URL"])
df.tail()


# 데이터 저장
df.to_csv(
    "../data/03. best_sandwiches_list_chicago.csv", sep=",", encoding="utf-8"
)
## 17-18 강 시카고 맛집 데이터 분석 - 하위페이지 

# 필요한 모듈
import pandas as pd 
from urllib.request import urlopen, Request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# 데이터 불러오기
df = pd.read_csv("../data/03. best_sandwiches_list_chicago.csv", index_col=0)
df.tail()

# 주소 확인
df["URL"][0]
req = Request(df["URL"][0], headers={"user-agent":ua.ie})
html = urlopen(req).read()
soup_tmp = BeautifulSoup(html, "html.parser")
soup_tmp.find("p", "addy") 
# soup_find.select_one(".addy")

# 정규 표현식 준비
price_tmp = soup_tmp.find("p", "addy").text
price_tmp

import re 
re.split(".,", price_tmp)

price_tmp = re.split(".,", price_tmp)[0]
price_tmp

tmp = re.search("\$\d+\.(\d+)?", price_tmp).group()
price_tmp[len(tmp) + 2:]

from tqdm import tqdm 

# 가격과 주소를 담기
price = [] 
address = [] 

for idx, row in tqdm(df[:5].iterrows()):
    req = Request(row["URL"], headers={"user-agent":ua.ie})
    html = urlopen(req).read()
    soup_tmp = BeautifulSoup(html, "html.parser")
    gettings = soup_tmp.find("p", "addy").get_text()
    price_tmp = re.split(".,", gettings)[0]
    tmp = re.search("\$\d+\.(\d+)?", price_tmp).group()
    price.append(tmp)
    address.append(price_tmp[len(tmp)+2:])
    print(idx)
    
# 담아온 가격과 주소 데이터 갯수 확인
len(price), len(address)

price[:5]
address[:5]

# 데이터 프레임 확인
df.tail(2)
# 데이터 프레임에 가격 컬럼, 주소 컬럼 추가
df["Price"] = price 
df["Address"] = address
df = df.loc[:, ["Rank", "Cafe", "Menu", "Price", "Address"]]
df.set_index("Rank", inplace=True)
df.head()

# 저장
df.to_csv(
    "../data/03. best_sandwiches_list_chicago2.csv", sep=",", encoding="UTF-8"
)
## 18-20 강 시카고 맛집 데이터 지도 시각화
# 저장한 데이터 불러오기

df = pd.read_csv("../data/03. best_sandwiches_list_chicago2.csv", index_col=0)
df.tail(10)

# 구글 맵 사용 및 필요한 모듈 불러오기

import folium
import pandas as pd 
import numpy as np 
import googlemaps

gmaps_key = "개인정보로 삭제함"
gmaps = googlemaps.Client(key=gmaps_key)

lat = [] 
lng = [] 

# 지도에 위치들을 찍도록 하기 위해 위도와 경도를 받아옴
for idx, row in tqdm(df.iterrows()):
    if not row["Address"] == "Multiple location":
        target_name = row["Address"] + ", " + "Chicago"
        # print(target_name)
        gmaps_output = gmaps.geocode(target_name)
        location_ouput = gmaps_output[0].get("geometry")
        lat.append(location_ouput["location"]["lat"])
        lng.append(location_ouput["location"]["lng"])
        # location_output = gmaps_output[0]
    else:
        lat.append(np.nan)
        lng.append(np.nan)
        
# 데이터 갯수 확인
len(lat), len(lng)
# 데이터 프레임에 위도 경도 컬럼 추가
df["lat"] = lat 
df["lng"] = lng 
df.tail()

# 구글맵에 표시

mapping = folium.Map(location=[41.8781136, -87.6297982], zoom_start=11)
# for문을 활용해서 하나씩 맵핑함
for idx, row in df.iterrows():
    if not row["Address"] == "Multiple location":
        folium.Marker(
            location=[row["lat"], row["lng"]],
            popup=row["Cafe"],
            tooltip=row["Menu"],
            icon=folium.Icon(
                icon="coffee",
                prefix="fa"
            )
        ).add_to(mapping)

mapping

## 21-24 강 네이터 영화 평점 사이트 분석, 데이터 확보
'''
- https://movie.naver.com/ 
- 영화랭킹 탭 이동 
- 영화랭킹에서 평점순(현재상영영화) 선택

https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220301

- 원하는 정보를 얻기 위해서 주소의 규칙을 찾아야 함. 
- 여기서는 날짜 정보를 변경해주면 해당 페이지에 접근이 가능. 
'''

# 필요한 모듈 

import pandas as pd 
from urllib.request import urlopen 
from bs4 import BeautifulSoup



url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220301"
response = urlopen(url)
# response.status # 상태 확인 
soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())
# 영화 제목 태그 
soup.find_all("div", "tit5") # soup.select("div.tit5")
# 태그 안에 하나씩 영화 제목을 확인하기
# 방법 1
soup.find_all("div", "tit5")[0].a.string
# 방법 2
soup.select(".tit5")[0].find("a").text
# 방법 3
soup.select(".tit5")[0].select_one("a").get_text()


# 영화 평점 태그 
soup.find_all("td", "point") # soup.select(".point")
# 갯수 확인
len(soup.find_all("td", "point")), len(soup.find_all("div", "tit5"))
# 점수 확인
soup.find_all("td", class_="point")[0].text, soup.select("td.point")[0].string

# 영화제목 리스트  받아오기

end = len(soup.find_all("div", "tit5"))

movie_name = [] 

for n in range(0, end):
    movie_name.append(
        soup.find_all("div", "tit5")[n].a.string
    )
movie_name
# 담아온 영화 제목 리스트, 다른 방법으로 .tit5 를 기준으로 선택
movie_name = [soup.select(".tit5")[n].a.text for n in range(0, end)]
movie_name

# 영화평점 리스트 받아오기
end = len(soup.find_all("td", "point"))

movie_point = [soup.find_all("td", "point")[n].string for n in range(0, end)]
movie_point

# 전체 데이터 수 확인 

len(movie_name), len(movie_point)


## 자동화를 위한 코드
'''
https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220301
- 날짜만 변경하면 우리가 원하는 기간 만큼 데이터를 얻을 수 있음
'''

date = pd.date_range("2021.11.01", periods=100, freq="D")
date

date[0].strftime("%Y-%m-%d")

# 문자열 포맷팅

test_string = "Hi, I'm {name}"
test_string.format(name="Zerobase")
test_string.format(name="Pinkwink")
# dir(test_string)
import time 
from tqdm import tqdm 
# 날짜, 영화이름, 평점 받아오기
movie_date = [] 
movie_name = [] 
movie_point = [] 

for today in tqdm(date):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={date}"
    response = urlopen(url.format(date=today.strftime("%Y%m%d")))
    soup = BeautifulSoup(response, "html.parser")
    
    end = len(soup.find_all("td", "point"))
    
    movie_date.extend([today for _ in range(0, end)])
    movie_name.extend([soup.select("div.tit5")[n].find("a").get_text() for n in range(0, end)])
    movie_point.extend([soup.find_all("td", "point")[n].string for n in range(0, end)])
    
    time.sleep(0.5)
# 받아온 데이터 갯수 확인
len(movie_date), len(movie_name), len(movie_point)
# 평점 확인
movie_point[:5]
# 영화 이름 확인
movie_name[:5]


# 데이터프레임화
movie = pd.DataFrame({
    "date": movie_date, 
    "name": movie_name,
    "point": movie_point
})
movie.tail()
# 데이터프레임 정보 확인
movie.info() 

movie["point"] = movie["point"].astype(float)
movie.info()

# 데이터 저장 

movie.to_csv(
    "../data/03. naver_movie_data.csv", sep=",", encoding="utf-8"
)
## 영화 평점 정리
# 데이터 불러오기

movie = pd.read_csv("../data/03. naver_movie_data.csv", index_col=0)
movie.tail()

'''
- 영화 이름으로 인덱스를 잡음. 
- 점수의 합산을 구하기.
- 100일 간 네이버 영화 평점 합산을 기준으로 베스트&워스트 10 선정
'''



# 피벗 테이블

movie_unique = pd.pivot_table(data=movie, index="name", aggfunc=np.sum)
movie_unique

# 내림차순으로 정렬
movie_best = movie_unique.sort_values(by="point", ascending=False) 
movie_best.head()
tmp = movie.query("name == ['고양이를 부탁해']")
tmp
## 25 - 26 강 네이버 영화 평점 데이터 정리 및 시각화

# 시각화를 위한 모듈

import matplotlib.pyplot as plt 
from matplotlib import rc 

rc("font", family="Malgun Gothic") 
%matplotlib inline 
# get_ipython().run_line_magic("matplotlib", "inline")

# 시각화
'''
 선 그래프 x축 날짜, y축 평점 
=> 날짜에 따른 평점 변화를 선그래프로 표현(시계열로)
'''

plt.figure(figsize=(20, 8)) # x 20, y, 8 
plt.plot(tmp["date"], tmp["point"]) 
plt.title("날짜별 평점")
plt.xlabel("날짜")
plt.ylabel("평점")
plt.xticks(rotation="vertical")
plt.legend(labels=["평점 추이"], loc="best")
plt.grid(True)
plt.show()
# 상위 10개 영화 
movie_best.head(10)

# 하위 10개 영화
# movie_best.tail(10)
movie_pivot = pd.pivot_table(data=movie, index="date", columns="name", values="point")
movie_pivot.head()
# 엑셀로 저장
movie_pivot.to_excel("../data/03. movie_pivot.xlsx")

import platform
import seaborn as sns 
from matplotlib import font_manager, rc 

path = "C:/Windows/Fonts/malgun.ttf"

if platform.system() == "Darwin":
    rc("font", family="Arial Unicode MS")
elif platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc("font", family=font_name)
else:
    print("Unknown system. sorry")
    
# 상위 5개 영화 평점 추이 시각화
target_col = ["코다", "고양이를 부탁해", "프렌치 디스패치", 
              "너의 이름은.", "스파이더맨: 노 웨이 홈"]
plt.figure(figsize=(20, 8))
plt.title("날짜별 평점")
plt.xlabel("날짜")
plt.ylabel("평점")
plt.xticks(rotation="vertical")
plt.tick_params(bottom="off", labelbottom="off")
plt.plot(movie_pivot[target_col])
plt.legend(target_col, loc="best")
plt.grid(True)
plt.show()
