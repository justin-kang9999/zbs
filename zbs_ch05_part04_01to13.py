# 03.Web Data
## 01 - 04 강 Beautiful Soup 기초

# 사용하는 모듈 불러오기
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
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
# 파일 오픈
page = open("../data/03_web_data/03. test_first.html", "r").read()
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

# head 태그 확인 
soup.haed
# body 태그 확인
soup.body

# find() 
# p 태그 확인, 처음 발견한 p 태그만 출력
# 방법 1
soup.p
# 방법 2
soup.find("p")

# find_all(): 여러 개의 태그를 반환, list 형태로 반환
soup.find_all("p")


# 옵션 달 수도 있음
# 파이썬 예약어 
# class, id, def, list, str, int, tuple...
soup.find("p", class_="inner-text second-item")

soup.find("p", {"class" : "outer-text first-item"}).text.strip()
# 다중조건
soup.find("p", {"class" : "inner-text first-item", "id" : "first"})
# find_all()
# 반환 한 것이 리스트 형태로 표현 됨 
soup.find_all("p")
# 특정 태그 확인
soup.find_all(class_="outer-text")
# 리스트 형태로 갖고오기 때문에 글자만 갖고오려면 인덱스를 이용해 잘라서 갖고와야함
soup.find_all(id="pw-link")[0].text
soup.find_all("p")[1].string
soup.find_all("p")[1].get_text()
#soup.find_all("p", class_="inner-text second-item")

# for문을 이용해서 p 태그 리스트에서 텍스트 속성만 출력
for each_tag in soup.find_all("p"):
    print("=" * 50)
    print(each_tag.text)
# a 태그에서 href 속성값에 있는 값 추출, 즉 주소값을 추출
links = soup.find_all("a")
#방법 1
links[0].get("href")
#방법 2
links[1]["href"]
# for 문을 이용한 주소값 추출
for each in links:
    href = each.get("href") # each["href"]로 바로 해도 됨
    text = each.get_text()
    print(text + " => " + href)
    
url = "https://finance.naver.com/marketindex/"
response = requests.get(url) 
# requests.get(), requests.post() 두가지 방법
# response.text, response.content
soup = BeautifulSoup(response.text, "html.parser") 
print(soup.prettify())
# soup.find_all("li", "on")
# id => # 
# class => . 
exchangeList = soup.select("#exchangeList > li")
len(exchangeList), exchangeList
title = exchangeList[0].select_one(".h_lst").text
exchange = exchangeList[0].select_one(".value").text
change = exchangeList[0].select_one(".change").text
'''
특정을 해야함. 띄어쓰기가 있으면 클래스 설정값이 두개가 있다고 생각
변동이 없었다면 unpdown 변수에 보합이라고 받아와야하나 
태그값이 .head_info 두개이므로 기존과는 다른 값인 보함을 가져오게 됨

'''
# 변동이 없어서 보합인 경우
#updown = exchangeList[0].select_one(".head_info.head_info > .blind").text
# 변동이 있는 경우
updown = exchangeList[0].select_one(".head_info.point_dn > .blind").text
# link 
# 필요한 것들
title, exchange, change, updown
# find_all을 사용할 경우
findmethod = soup.find_all("ul", id="exchangeList")
findmethod[0].find_all("span", "value")
baseUrl = "https://finance.naver.com"
baseUrl + exchangeList[0].select_one("a").get("href")

# 4개 데이터 수집 title, exchange, change, updown

exchange_datas = [] 
baseUrl = "https://finance.naver.com"
# for문을 통해서 데이터를 가져오기
for item in exchangeList:
    data = {
        "title": item.select_one(".h_lst").text,
        "exchnage": item.select_one(".value").text,
        "change": item.select_one(".change").text,
        "updown": item.select_one(".head_info.point_dn > .blind").text,
        "link": baseUrl + item.select_one("a").get("href")
    }
    exchange_datas.append(data)
# 데이터프레임으로 표현하기
df = pd.DataFrame(exchange_datas)

#저장
df.to_excel("./naverfinance.xlsx", encoding="utf-8")

## 10 - 11강 - 위키백과 문서 정보 가져오기 
import urllib
from urllib.request import urlopen, Request

html = "https://ko.wikipedia.org/wiki/{search_words}"
# https://ko.wikipedia.org/wiki/여명의_눈동자

# 글자를 URL로 인코딩 여명의_눈동자가 깨지기 때문에 포맷팅을 했는데, 이를 요청하는 단계를 만듦
req = Request(html.format(search_words=urllib.parse.quote("여명의_눈동자"))) 
response = urlopen(req)
soup = BeautifulSoup(response, "html.parser")
print(soup.prettify())
# for문을 통해서 ul태그 내용들 갖고오기
n = 0 

for each in soup.find_all("ul"):
    print("=>" + str(n) + "========================")
    print(each.get_text())
    n += 1
    
#15번째 줄에 주요 등장인물이 나와 있음을 확인
# 등장 인물 역 갖고오기
soup.find_all("ul")[15].text.strip().replace("\xa0", "").replace("\n", "")

## 12 - 13강 list 데이터형 복습
'''
- list형은 대괄호로 만든다
'''
colors = ["red", "blue", "green"]
#인덱스로 불러내기
colors[0], colors[1], colors[2]
b = colors
b
b[1] = "black"
b
# colors 리스트도 바뀌어 있는 것을 확인
colors
# copy()명령어를 이용
c = colors.copy()
c[1] = "yellow"
c
#colors는 안바뀐것을 확인
colors
# in 이용해서 for문 활용
for color in colors: 
    print(color)
# in 이용해서 if문 활용
if "white" in colors:
    print("True")
movies = ["라라랜드", "먼 훗날 우리", "어벤저스", "다크나이트"]
print(movies)
# append() 활용 리스트의 맨 뒤에 추가
movies.append("타이타닉")
movies
# pop() 활용 리스트 제일 뒤부터 자료를 하나씩 삭제 
#movies.pop()
movies
# extend() 제일 뒤에 자료를 추가
movies.extend(["위대한쇼맨", "인셉션", "터미네이터"])
movies

# remove() 자료를 삭제 
movies.remove("어벤저스")
movies

# 슬라이싱 [n:m:t] n부터 m까지 출력하는데 t만큼 띄어서 
print(movies[:5:2])
favorite_movies = movies[3:5]
favorite_movies
# insert() 원하는 위치에 자료를 삽입
favorite_movies.insert(1, 9.60)
favorite_movies
favorite_movies.insert(3, 9.50)
favorite_movies
# 리스트안에 리스트 넣는 것도 가능하다
favorite_movies.insert(5, ["레오나르도 디카프리오", "조용하"])
favorite_movies
# isinstance 자료형 True/False 타입으로 반환해줌
isinstance(favorite_movies, list)

for each_item in favorite_movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            # 리스트안의 아이템이 리스트 형태인 경우
            print("nested_item", nested_item)
    else:
        # 아닌경우
        print("each_item", each_item)