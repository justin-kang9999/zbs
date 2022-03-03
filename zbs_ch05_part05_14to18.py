## 14 강 selenium 예제 iframe (네이버 금융 이용)
'''
- iframe
    - html 안에 또 다른 html이라 생각하면 됨
'''
# 필요한 모듈

import pandas as pd 
import time 
from selenium import webdriver
# 주소 불러오기
url = "https://finance.naver.com/marketindex/"
# 윈도우는 꼭꼭 .exe 붙이기
driver = webdriver.Chrome("../driver/chromedriver.exe") 
driver.get(url)
# 환전 고시 환율 갖고오기
contents = driver.find_elements_by_css_selector("#exchangeList > li > a")
contents[0].find_element_by_css_selector(".value").text
# 주요뉴스 제목 
news = driver.find_elements_by_css_selector("#content > div.section_news > div > ul > li:nth-child(1) > p > a")
news[0].text
# 밑 페이지에 있는 매매기준율 usd 말고도 다른 것도 갖고오기
# 안가져와짐. iframe이 html에서 찾아볼 수 있음을 확인
driver.find_elements_by_css_selector("body > div > table > tbody > tr")

## iframe
# selenium을 이용한 방법

# iframe 태그 지정
# 방법 1
iframe = driver.find_element_by_css_selector("#frame_ex1")
# 방법 2
#driver.find_element_by_id("frame_ex1")
# iframe 태그 이동
driver.switch_to.frame(iframe)
# 환전 고시 환율 다시 실행하면 안됨. iframe 태그를 갖고 왔기 때문에
contents = driver.find_elements_by_css_selector("#exchangeList > li > a")
contents[0].find_element_by_css_selector(".value").text

driver.find_element_by_css_selector(".sale").text
# 가져와지지 않았던 매매기준율 코드 다시 실행해보기
contents = driver.find_elements_by_css_selector("body > div > table > tbody > tr")
contents[0].find_element_by_css_selector(".sale").text
# for 문을 이용해서 각각 통화 갖고오기

datas = [] 

for content in contents:
    # 통화
    title = content.find_element_by_css_selector(".tit > a").text
    # 가격
    sale = content.find_element_by_css_selector(".sale").text
    # 링크
    link = content.find_element_by_css_selector(".tit > a").get_attribute("href")
    datas.append({
        "title": title, 
        "sale": sale,
        "link": link
    })
    time.sleep(2)
df = pd.DataFrame(datas)
# 데이터를 엑셀로 저장
df.to_excel("./sel_naver_finance.xlsx", encoding="utf-8")
df


# 종료
driver.quit()

## request를 이용한 방법 
# 필요한 모듈
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.naver"
response = requests.get(url)
response
response.content

soup = BeautifulSoup(response.content, "html.parser")
# 눈으로 확인하기 위해 prettyfiy() 명령어 사용
print(soup.prettify())
# 환율 확인
soup.select_one(".sale").text
# 부모태그를 갖고와서 usd 환율 갖고오기
contents = soup.select("tbody > tr") # 부모 태그 
contents[2].select_one(".sale").text

for content in contents:
    print(content.select_one(".sale").text)
    
## 15 강 selenium 예제 - headless
'''
- 웹브라우저를 띄우지 않고 데이터 수집을 해보기
'''
import pandas as pd 
import time 
from selenium import webdriver
# 웹브라우저 안띄우고 작업하기
options = webdriver.ChromeOptions()
options.add_argument("headless")
# 확인을 위한 프린트 기능 추가
print("selenium headless.. 1")

# 주소 불러오기
url = "https://finance.naver.com/marketindex/"
driver = webdriver.Chrome("../driver/chromedriver.exe", options=options) 
driver.get(url)
# 최대화 기능 추가
driver.maximize_window()
print("selenium headless.. 2")
# 화면 스크롤 하단 이동
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
print("selenium headless.. 3")

# iframe 태그 지정 
iframe = driver.find_element_by_css_selector("#frame_ex1")
# iframe 태그 이동
driver.switch_to.frame(iframe)
time.sleep(3)
print("selenium headless.. 4")
# 가져와지지 않았던 매매기준율 코드 다시 실행해보기
contents = driver.find_elements_by_css_selector("body > div > table > tbody > tr")
contents[0].find_element_by_css_selector(".sale").text
print("selenium headless.. 5")
# 환율정보 갖고오기

# for 문을 이용해서 각각 통화 갖고오기

datas = [] 

for content in contents[:3]:
    # 통화
    title = content.find_element_by_css_selector(".tit > a").text
    # 가격
    sale = content.find_element_by_css_selector(".sale").text
    # 링크
    link = content.find_element_by_css_selector(".tit > a").get_attribute("href")
    datas.append({
        "title": title, 
        "sale": sale,
        "link": link
    })
    time.sleep(3)
    print("selenium headless.. for for for")
driver.quit()
df = pd.DataFrame(datas)
# 데이터를 엑셀로 저장
df.to_excel("../sel_naver_finance.xlsx", encoding="utf-8")
df

print("Selenium quit!")
## 16 - 18 강 selenium 예제 - wait
'''
지금까지 배운 것들
- selenium_basic_1 => iframe 
- selenium_basic_2 => headless 
이제 배울 내용
- selenium_basic_3 => wait

- time.sleep(5): 물리적으로 5초 동안 멈추고 기다림
- implicityly_wait(10)
    - 전체 페이지 로딩을 최대 10초 간 기다리고, 10초 안에 페이지 로딩이 완료되면 다음 코드 실행
    - 한 번만 실행하면, 전역(global)로 실행이 가능. 
- explicitly wait 
    - 지정한 태그만 로딩이 완료되면, 다음 코드 실행

'''

'''
- 무신사 스토어를 이용해보기
- https://store.musinsa.com/app/
- 인기 => 후드 집업 
- 단독상품, 세일상품 조건을 선택
- 최소~최대 금액 입력
- 여기서 선택한 조건들 : 후드집업으로 들어가서, 단독상품, 세일 상품, 최소-최대금액 입력
- 옷 이름, 가격, 할인율, 링크, 이미지

'''

# 필요한 모듈
import pandas as pd 
import time 
from selenium import webdriver

# explicitly wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
# 1. 페이지 접근 
# 2. 주소 검색 탭 선택 
# 3. 검색어(구) 입력 
# 4. 검색 결과 리스트 가져오기(뷰티풀숲)
# 5. 
'''
url = "https://store.musinsa.com/app/"
driver = webdriver.Chrome("../driver/chromedriver.exe") 
# 웹 페이지 전체가 로딩 될 때까지 10초간 대기하고, 
# 10초안에 로딩이 완료되면 다음 코드를 실행
driver.implicitly_wait(10) 
driver.get(url)
# 로그인 버튼 클릭 방법 1 
driver.find_element_by_css_selector("#default_top > div.header-member > button").click()
# 로그인 버튼 클릭 방법 2
# driver.find_element_by_css_selector("body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > button").click()
# 아이디 입력 
driver.find_element_by_css_selector("body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > input:nth-child(2)").send_keys("개인정보라서 삭제")
# 패스워드 입력
driver.find_element_by_css_selector("body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > input:nth-child(3)").send_keys("개인정보라서 삭제")

# alert 
'''
아이디나 비밀번호가 틀립니다 라고 나올 때 그 팝업창을 제거하도록
'''
# 방법 1
driver.switch_to.alert.accpet()
# 방법 2
# alert = driver.switch_to.alert
# alert.accpet()
# 후드집업칸으로 들어가도록
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located((By.CSS_SELECTOR, "#default_top > div.header-member > button"))).click()
# explicitly wait 기능을 이용
#  아이디(wait)
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > input:nth-child(2)"))).send_keys("개인정보라서 삭제")

# 패스워드(wait)
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > input:nth-child(3)"))).send_keys("개인정보라서 삭제")

# 로그인 버튼 클릭(wait)
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "body > div.musinsa-wrapper.wrapper-member.devicePC > div > form > button"))).click()
# 인기 => 후드 집업으로 가기
best_link = driver.find_element_by_css_selector\
    ("#ui-id-2 > ul:nth-child(1) > li:nth-child(1) > a")\
        .get_attribute("href")
best_link
# 인기 => 후드 집업 링크 => 새 탭으로 열기 
driver.execute_script("window.open('{}')".format(best_link))
# 후드 집업 탭으로 이동 
driver.switch_to.window(driver.window_handles[1])
# 단독 상품 
# driver.find_element_by_css_selector("#btn_exclusive").click()

WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "#btn_exclusive"))).click()

# 세일 상품 
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "#btn_sale"))).click()


# 최소 ~ 최대 금액 설정  
# 최소금액
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "#minPrice"))).send_keys("10000")
# 최대금액
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "#maxPrice"))).send_keys("100000")
# 클릭해서 최소-최대금액 설정함
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located\
    ((By.CSS_SELECTOR, "#btn_price_search"))).click()
# 부모 태그 확인

outers = driver.find_elements_by_css_selector("#searchList > li")
len(outers)

# 자식 태그 
# 옷 이름 확인
outers[39].find_element_by_css_selector\
    ("p.list_info > a").get_attribute("title")
# 옷 가격 확인
outers[39]\
    .find_element_by_css_selector("p.price").text.split(" ")[1][:-1]

# 할인율
outers[39]\
    .find_element_by_css_selector(".icon_new").text.split(" ")[1][:-1]
# 세부 링크 가져오기
outers[39].find_element_by_css_selector("p.list_info > a").get_attribute("href")
# 이미지 

try: 
    print(outers[39].find_element_by_css_selector("img").get_attribute("src"))
except:
    print(outers[39].find_element_by_css_selector("img").get_attribute("data-original"))

outers[10].find_element_by_css_selector("img").get_attribute("src")
outers[13].find_element_by_css_selector("img").get_attribute("data-original")
# 무신사 폴더 만들기
# !mkdir musinsa 

import requests
# html 코드 확인
res = requests.get(outers[0].find_element_by_css_selector("img").get_attribute("src"))
res.content[:5]
# write_binary
with open("./musinsa/outer.png", "wb") as f: 
    f.write(res.content)
# 사이트 끄기
driver.quit()
## 18 강 selenium 예제 - 17강 무신사 스토어 이어서
# 전체 데이터 크롤링 

from tqdm import tqdm_notebook

datas = [] 

for outer in tqdm_notebook(outers[:3]):
    # 옷이름
    title = outer.find_element_by_css_selector("p.list_info > a").get_attribute("title")
    # 가격
    price = outer.find_element_by_css_selector("p.price").text.split(" ")[1][:-1]
    # 할인율
    sale = outer.find_element_by_css_selector(".icon_new").text.split(" ")[1][:-1]
    # 상세 링크
    link = outer.find_element_by_css_selector("p.list_info > a").get_attribute("href")
    # 이미지
    img = outer.find_element_by_css_selector("img").get_attribute("src")
    datas.append({
        "title": title, 
        "price": price, 
        "sale": sale, 
        "link": link,
        "img": img
    })
driver.quit()
df = pd.DataFrame(datas)
df
# 종료
driver.quit()

# 이미지 다운로드 

for idx, rows in tqdm_notebook(df.iterrows()):
    thumb_link = rows["img"]
    response = requests.get(thumb_link)
    # 파일 이름을 저장하는데 이름 형태 지정
    name = str(idx) + "_" + rows["title"]
    with open("./musinsa/{}.png".format(name), "wb") as f: 
        f.write(response.content)

# py 형식으로 만들기 %%writefile이 최상단에 있어야함
# %%writefile ./musinsa.py

import pandas as pd 
import time 
import requests
from selenium import webdriver
# explicitly wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 잘 진행되는지 확인하도록 print() 활용
print("#1. selenium get url")
# 헤드리스옵션으로 브라우저를 열지 않게
options = webdriver.ChromeOptions()
options.add_argument("headless")
url = "https://store.musinsa.com/app/"
driver = webdriver.Chrome("../driver/chromedriver.exe", options=options) 
# 웹 페이지 전체가 로딩 될 때까지 10초간 대기하고, 
# 10초안에 로딩이 완료되면 다음 코드를 실행
driver.implicitly_wait(10) 
driver.get(url)
# 잘 진행되는지 확인하도록 print() 활용
print("#2. maximize window")
# 화면 최대화 
driver.maximize_window()
# 잘 진행되는지 확인하도록 print() 활용
print("#3. best item")
# 인기 => 후드 집업 
best_link = driver.find_element_by_css_selector("#ui-id-2 > ul:nth-child(1) > li:nth-child(1) > a").get_attribute("href")
# 인기 => 후드 집업 링크 => 새 탭으로 열기 
driver.execute_script("window.open('{}')".format(best_link))
# 후드 집업 탭으로 이동 
driver.switch_to_window(driver.window_handles[1])
print("#4. tab open ok! I'm waiting..")
time.sleep(3)

print("#5. item option check")
# 단독 상품 
# driver.find_element_by_css_selector("#btn_exclusive").click()
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn_exclusive"))).click()
# 세일 상품 
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn_sale"))).click()
# 최소 ~ 최대 금액 설정  
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located((By.CSS_SELECTOR, "#minPrice"))).send_keys("10000")
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located((By.CSS_SELECTOR, "#maxPrice"))).send_keys("100000")
WebDriverWait(driver, 5).\
until(EC.presence_of_element_located((By.CSS_SELECTOR, "#btn_price_search"))).click()

print("#6. item option check done! I'm waiting")
time.sleep(3)

print("#7. outers crawling start")
# 부모 태그 
outers = driver.find_elements_by_css_selector("#searchList > li")

# 전체 데이터 크롤링 
datas = [] 
for idx, outer in enumerate(outers[:30]):
    title = outer.find_element_by_css_selector("p.list_info > a").get_attribute("title")
    price = outer.find_element_by_css_selector("p.price").text.split(" ")[1][:-1]
    sale = outer.find_element_by_css_selector(".icon_new").text.split(" ")[1][:-1]
    link = outer.find_element_by_css_selector("p.list_info > a").get_attribute("href")
    img = outer.find_element_by_css_selector("img").get_attribute("data-original")
    print(img)
    datas.append({
        "title": title, 
        "price": price, 
        "sale": sale, 
        "link": link,
        "img": img
    })
    print("#8. idx: {}, title: {}".format(idx, title))
driver.quit()
df = pd.DataFrame(datas)
# 엑셀저장
df.to_excel("./musinsa/musinsa.xlsx", encoding="utf-8")
print("#9. crawling Done! driver quit & excel save")

print("#10. img download")
# 이미지 다운로드 
for idx, rows in df.iterrows():
    thumb_link = rows["img"]
    response = requests.get(thumb_link)
    name = str(idx) + "_" + rows["title"]
    with open("./musinsa/{}.png".format(name), "wb") as f: 
        f.write(response.content)
# 모든 작업이 끝남
print("#11. img download done!")
print("#12. Good Job!")

# 삭제
# !rm -rf musinsa/
# 다시 만들기
# !mkdir musinsa/
# 실행해서 크롤링해보기
# !python musinsa.py