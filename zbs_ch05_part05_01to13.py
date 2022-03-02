## 01 - 05 강 selenium 기초
# 설치, 크롬드라이버 다운받아서 설치
# !pip install selenium
#!pip install selenium
import selenium
from selenium import webdriver


driver = webdriver.Chrome("../driver/chromedriver.exe") # 크롬 드라이버 경로 지정 
driver.get("https://pinkwink.kr/") # get 명령으로 접근하고 싶은 주소 지정  
# 현재 브라우저 창 크기 확인
driver.get_window_size()
# 스크롤 가능한 높이(길이)
driver.get_window_rect()

# 자바스크립트 코드 실행
last_height = driver.execute_script("return document.body.scrollHeight")
last_height
# 화면 스크롤 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 스크린샷찍기
driver.save_screenshot("./last_height.png")

# 스크롤 상단으로 이동 
driver.execute_script("window.scrollTo(0, 0);")

  
'''
Selenium 태그 명령어 
css_selector와 bs4 beautifulsoup간 명령어 비교
find_element_by_css_selector => find, select_one 
find_elements_by_css_selector => find_all, select
'''
# 특정 태그 지점까지 스크롤
from selenium.webdriver import ActionChains

# some_tag = driver.find_element_by_xpath('//*[@id="paging"]/ul')
some_tag = driver.find_element_by_css_selector("#paging > ul") 
action = ActionChains(driver)
action.move_to_element(some_tag).perform()
# 입력 창에 글자 넣기 
# 화면에 보이지 않으면 에러가 남
some_tag = driver.find_element_by_id("gsc-i-id1")
some_tag.send_keys("data science")

# 바로 붙여서 사용 가능
# driver.find_element_by_id("gsc-i-id1").send_keys("data science")

# 브라우저 창 크기 조절 
# 현재 보이는 화면에서만 액션 가능
driver.set_window_size(1920, 1080)
# 화면 최대화 
driver.maximize_window() 
# 화면 최소화 
driver.minimize_window()
# 새로 입력하면 뒤에 추가로 붙음 
some_tag.send_keys("python")
# 초기화 후 검색어 입력 
some_tag.clear()
# 다시 검색어 입력
some_tag.send_keys("python")
# driver.back()
# driver.forward()
'''
pinkwink.kr 내에서 돋보기부분을 클릭해야 검색이 되므로 개발자 도구로 그 태그를 찾음
Xpath 와 css_selector 비교

'//': 최상위 엘리먼트
'*': 띄어쓰기 자손 태그 검색 => div form 
'/': 꺽쇠는 자식 태그 검색 => div > form
'td[2]': td 중에서 2번째 태그를 선택 => td:nth_child(2)
'''

# xpath 
# 자식태그중에서 td 코드 중에 클릭버튼이 있는 것
xpath = '//*[@id="___gcse_0"]/div/form/table/tbody/tr/td[2]/button'
some_tag = driver.find_element_by_xpath(xpath)
some_tag.click()
# css_selector 와 비교
# 자식태그중에서 td 코드 중에 클릭버튼이 있는 것 css_selector를 이용한 방법
css_selector = "#___gcse_0 > div > form > table > tbody > tr > td:nth-child(2) > button"
some_tag = driver.find_element_by_css_selector(css_selector).click()



# 현재 화면의 html 코드 가져오기 
#beautifulsoup를 이용
driver.page_source

from bs4 import BeautifulSoup

req = driver.page_source
soup = BeautifulSoup(req, "html.parser")

soup.select(".gsc-wrapper")
## 06 - 09 강 주유소 가격 분석- 데이터 얻어오기
#필요한 모듈

from selenium import webdriver
import time 
# 주소 불러오기
# 페이지 접근 
url = "https://www.opinet.co.kr/searRgSelect.do"
driver = webdriver.Chrome("../driver/chromedriver.exe") 
driver.get(url)
'''
- 사이트 구조 확인
- 목표 데이터
    - 브랜드
    - 가격
    - 셀프주유여부
    - 위치
    
문제점
- 해당 URL로 한 번에 접근이 안됨. 
- 메인페이지로 접속이 되고, 팝업창이 하나 나옴.
'''
# 팝업창 화면 전환 후 닫아주기 
driver.switch_to_window(driver.window_handles[-1])
# 접근 페이지 다시 요청 
driver.close()
driver.switch_to_window(driver.window_handles[-1])
def main_get():
    # 페이지 접근 
    url = "https://www.opinet.co.kr/searRgSelect.do"
    # windows .exe 하는 것을 잊지 말 것
    driver = webdriver.Chrome("../driver/chromedriver.exe")  
    driver.get(url)
    # 잠시 멈춰주기
    time.sleep(3)
    # 팝업창으로 전환 
    driver.switch_to.window(driver.window_handles[-1])
    
    # 팝업창 닫아주기
    driver.close()
    time.sleep(3)
    # 메인화면 창으로 전환 
    #driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.window(driver.window_handles[-1])
    # 접근 URL 다시 요청 
    driver.get(url)
main_get()
# 지역: 시/도 갖고오기

sido_list_raw = driver.find_element_by_id("SIDO_NM0")
sido_list_raw.text

# 여러개인 경우 .find_element대신 s를 붙여서 .find_elements_이렇게 해야함
sido_list = sido_list_raw.find_elements_by_tag_name("option")
len(sido_list), sido_list[17].text

# 불러오는 값과 속성값 데이터가 다름
sido_list[1].get_attribute("value")
# 속성 값을 갖고 오도록 for문
sido_names = [] 

for option in sido_list:
    sido_names.append(option.get_attribute("value"))
sido_names

# 한줄로 작성하기
# sido_names = [option.get_attribute("value") for option in sido_list]
# sido_names[:5]
# 리스트에 0번 인덱스가 빈내용이므로 1번 인덱스부터 불러오도록 함
sido_names = sido_names[1:]
sido_names
sido_names[0]
# 시/ 도 전환하기 0번 서울 ~16번 제주
sido_list_raw.send_keys(sido_names[0])
# 구 리스트

gu_list_raw = driver.find_element_by_id("SIGUNGU_NM0") # 부모 태그 
gu_list = gu_list_raw.find_elements_by_tag_name("option") # 자식 태그 

gu_names = [option.get_attribute("value") for option in gu_list]
gu_names = gu_names[1:]
gu_names[:5], len(gu_names)
# 구 칸 조작하기
gu_list_raw.send_keys(gu_names[23])
# 엑셀 저장을 위해 엑셀저장 버튼이 있ㄴ는 태그 찾아서 클릭 액션을 해서 저장되도록
driver.find_element_by_css_selector("#glopopd_excel").click()
# xpath를 사용하는 방법
#driver.find_element_by_xpath('//*[@id="glopopd_excel"]').click()
# 다른 방법
# element_get_excel = driver.find_element_by_id("glopopd_excel")
# element_get_excel.click()
import time 
from tqdm import tqdm_notebook
# 각 구마다 가격을 다운받아오도록 for문을 이용
for gu in tqdm_notebook(gu_names):
    element = driver.find_element_by_id("SIGUNGU_NM0")
    # 각 구 하나씩 넣어주기
    element.send_keys(gu)
    time.sleep(3) # 봇 활용을 피하기 위함
    # 엑셀로 저장
    element_get_excel = driver.find_element_by_id("glopopd_excel").click()
    time.sleep(3)
# 사이트 닫기
driver.close() 
## 10 - 11 강 주유소 가격 정보 정리하기

import pandas as pd 
from glob import glob 

# 파일 목록 한 번에 가져오기 
glob("../data/04_oil_price/지역/지역_*.xls")
# 파일명 저장 
stations_files = glob("../data/04_oil_price/지역/지역_*.xls")
stations_files[:5]
# 하나만 읽어보기 
tmp = pd.read_excel(stations_files[0], header=2) # 1,2번줄이 내용이 없으므로
tmp.tail(2)
tmp_raw = [] 
#파일을 하나씩 읽어오기
for file_name in stations_files:
    tmp = pd.read_excel(file_name, header=2)
    tmp_raw.append(tmp)
tmp_raw
# 데이터 프레임으로 변환하고 concat을 이용해서 합치기.
# 형식이 동일하고 연달아 붙이기만 하면 될 때는 concat 
stations_raw = pd.concat(tmp_raw)
stations_raw
stations_raw.info()
# 컬럼 확인
stations_raw.columns
# 데이터프레임화
stations = pd.DataFrame({
    "상호": stations_raw["상호"],
    "주소": stations_raw["주소"], 
    "가격": stations_raw["휘발유"],
    "셀프": stations_raw["셀프여부"],
    "상표": stations_raw["상표"]
})
stations.tail()
# 어느 구에 해당하는지
for eachAddress in stations["주소"]:
    print(eachAddress.split()[1])
# 구 컬럼을 만들기
stations["구"] = [eachAddress.split()[1] for eachAddress in stations["주소"]]
stations
# 제대로 가져왔는지, 25개 구인 것을 확인
stations["구"].unique(), len(stations["구"].unique())
# 25개 구가 아닌 경우 수정하는 방법
# stations[stations["구"] == "서울특별시"]
# stations.loc[stations["구"] == "서울특별시", "구"] = "성동구"
# stations[stations["구"] == "특별시"]
# stations.loc[stations["구"] == "특별시", "구"] = "도봉구"
# 가격 데이터형 변환 object => float 
# 가격 정보가 없는 주유소 때문에 에러가 뜸
stations["가격"] = stations["가격"].astype("float")
# 가격 정보 없는 주유소 확인
stations[stations["가격"] == "-"]
# 가격 정보가 있는 주유소만 사용하도록 걸러내기
stations = stations[stations["가격"] != "-"]
stations.tail()
# 가격 데이터형 변환 object => float 
stations["가격"] = stations["가격"].astype("float")
# 변환후 확인
stations.info()
# 인덱스 재정렬 
stations.reset_index(inplace=True)
stations.tail()
# 인덱스 삭제
# del stations["index"]
# del stations["level_0"]
stations.head()
stations.tail()
## 12 - 13 강 주유소 가격 정보 시각화
# 모듈 준비
import matplotlib.pyplot as plt 
import seaborn as sns 
import platform
from matplotlib import font_manager, rc 

# get_ipython().run_line_magic("matplotlib", "inline")
%matplotlib inline 

path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=path).get_name() 
rc("font", family=font_name)
# if platform.system() == "Darwin":
#     rc("font", family="Arial Unicode MS")
# elif platform.system() == "Windows":
    # font_name = font_manager.FontProperties(fname=path).get_name() 
    # rc("font", family=font_name)
# else:
#     print("Unkown system. sorry")

# boxplot 판다스에서 가져와서 해보기

stations.boxplot(column="가격", by="셀프", figsize=(12, 8))
# boxplot seaborn 이용

plt.figure(figsize=(12, 8))
sns.boxplot(x="셀프", y="가격", data=stations, palette="Set1")
plt.grid(True)
plt.show()
# boxplot seaborn 이용

plt.figure(figsize=(12, 8))
# 색상에 다른 셀프주유소인지 아닌지
sns.boxplot(x="상표", y="가격", hue="셀프", data=stations, palette="Set3")
plt.grid(True)
plt.show()
# 지도 시각화를 위한 모듈 불러오기
import json 
import folium
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
# 가장 비싼 주유소 10개 
stations.sort_values(by="가격", ascending=False).head(10)
# 가장 저렴한 주유소 10개 
stations.sort_values(by="가격", ascending=True).head(10)
import numpy as np 

# 피벗테이블 만들기. 각 구별 평균가
gu_data = pd.pivot_table(data=stations, index="구", values="가격", aggfunc=np.mean)
gu_data.head()
# 지도 시각화
geo_path = "../data/02_crime/02. skorea_municipalities_geo_simple.json"
geo_str = json.load(open(geo_path, encoding="utf-8"))

my_map = folium.Map(location=[37.5502, 126.982], zoom_start=10.5, tiles="Stamen Toner")
my_map.choropleth(
    geo_data=geo_str,
    data=gu_data,
    columns=[gu_data.index, "가격"],
    key_on="feature.id",
    fill_color="PuRd"
)

my_map