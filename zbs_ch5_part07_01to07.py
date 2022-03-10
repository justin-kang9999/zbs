## 01 강 네이버 API 등록
- 네이버 개발자 센터 
- https://developers.naver.com/main/
- Application 
    - 어플리케이션 등록
    - 어플리케이션 이름 ds_study 
    - 사용 API 
        - 검색
        - 데이터랩(검색어트렌드)
        - 데이터랩(쇼핑인사이트)
    - 환경추가 
        - WEB 설정 
        - http://localhost
    - Clienct ID: H2_6lcavpVyHW8211rUq
    - Clienct Secret: D1XBjnKTe9
    - https://developers.naver.com/apps/#/myapps/H2_6lcavpVyHW8211rUq/overview 


    - 내 등록 
    - client id: vfqYG7gJZrMbEA_OOShE
    - client secret : bIiAieUidU
## 02 강 네이버 검색 API 사용하기
- https://developers.naver.com/docs/serviceapi/search/blog/blog.md#%EB%B8%94%EB%A1%9C%EA%B7%B8 # 개발 가이드 

- urllib: http 프로토콜에 따라서 서버의 요청/응답을 처리하기 위한 모듈 
- urllib.request: 클라이언트의 요청을 처리하는 모듈 
- urllib.parse: url 주소에 대한 분석 
# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
response, response.getcode(), response.code, response.status
# 글자로 읽을 경우에는 decode.("utf-8") 설정 
print(response_body.decode("utf-8"))
## 검색: 책(book)
# 네이버 검색 API예제는호출방법이 동일하므로 blog검색만 대표로 예제
# 네이버 검색 Open API 예제
import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
## 검색: 영화(movie)
# 네이버 검색 API예제는 호출방법이 동일
# 네이버 검색 Open API 예제
import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
## 검색: 카페(cafearticle)

import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/cafearticle?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
## 검색: 쇼핑(shop)

import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
## 검색: 백과사전(encyc)

import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/encyc?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
## 3. 상품 검색 
'''
- "몰스킨"
'''
import os
import sys
import urllib.request

client_id = "H2_6lcavpVyHW8211rUq"
client_secret = "D1XBjnKTe9"

encText = urllib.parse.quote("몰스킨")
url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
from PIL import Image
Image.open("../data/06. molskin plan.png")
'''
encText = urllib.parse.quote("몰스킨")
url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
'''
# 함수화
def gen_search_url(api_node, search_text, start_num, disp_num):
    base = "https://openapi.naver.com/v1/search"
    node = "/" + api_node + ".json"
    param_query = "?query=" + urllib.parse.quote(search_text)
    param_start = "&start=" + str(start_num)
    param_disp = "&display=" + str(disp_num)
    
    return base + node + param_query + param_start + param_disp
gen_search_url("shop", "TEST", 10, 3)
import json 
import datetime 

def get_result_onpage(url):
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    print("[%s] Url Request Success" % datetime.datetime.now())
    return json.loads(response.read().decode("utf-8"))
datetime.datetime.now()
url = gen_search_url("shop", "몰스킨", 1, 5)
one_result = get_result_onpage(url)
one_result
one_result["items"][0]["title"]
one_result["items"][0]["link"]
one_result["items"][0]["lprice"]
one_result["items"][0]["mallName"]
one_result["items"][0]

import pandas as pd 
# 함수화
def get_fields(json_data):
    title = [each["title"] for each in json_data["items"]]
    link = [each["link"] for each in json_data["items"]]
    lprice = [each["lprice"] for each in json_data["items"]]
    mall_name = [each["mallName"] for each in json_data["items"]]
    # 갖고온 데이터를 데이터프레임으로 만들기
    result_pd = pd.DataFrame({
        "title": title, 
        "link": link, 
        "lprice": lprice, 
        "mall": mall_name,   
    }, columns=["title", "lprice", "link", "mall"])
    return result_pd

get_fields(one_result)
# 태그 삭제 함수화
def delete_tag(input_str):
    input_str = input_str.replace("<b>", "")
    input_str = input_str.replace("</b>", "")
    return input_str 
import pandas as pd 

def get_fields(json_data):
    title = [delete_tag(each["title"]) for each in json_data["items"]]
    link = [each["link"] for each in json_data["items"]]
    lprice = [each["lprice"] for each in json_data["items"]]
    mall_name = [each["mallName"] for each in json_data["items"]]
    
    result_pd = pd.DataFrame({
        "title": title, 
        "link": link, 
        "lprice": lprice, 
        "mall": mall_name,   
    }, columns=["title", "lprice", "link", "mall"])
    return result_pd
url = gen_search_url("shop", "몰스킨", 1, 5)
json_result = get_result_onpage(url)
pd_result = get_fields(json_result)
pd_result
result_mol = [] 

for n in range(1, 1000, 100):
    url = gen_search_url("shop", "몰스킨", n, 100)
    json_result = get_result_onpage(url)
    pd_result = get_fields(json_result)
    
    result_mol.append(pd_result)
    
result_mol = pd.concat(result_mol)

result_mol.info()

result_mol.reset_index(drop=True, inplace=True)
result_mol.info()


result_mol.tail()
result_mol.info()

# 데이터 타입 수정
result_mol["lprice"] = result_mol["lprice"].astype("float")
result_mol.info()
# 엑셀로 보내기
# !pip install xlsxwriter
writer = pd.ExcelWriter("../data/06_molskin_diary_in_naver_shop.xlsx", engine="xlsxwriter")
result_mol.to_excel(writer, sheet_name="Sheet1")

workbook = writer.book 
worksheet = writer.sheets["Sheet1"]
worksheet.set_column("A:A", 4)
worksheet.set_column("B:B", 60)
worksheet.set_column("C:C", 10)
worksheet.set_column("D:D", 10)
worksheet.set_column("E:E", 50)
worksheet.set_column("F:F", 10)

worksheet.conditional_format("C2:C1001", {"type": "3_color_scale"})
writer.save()
# 저장
!ls "../data/06_molskin_diary_in_naver_shop.xlsx"
# 시각화
import set_matplotlib_hangul
plt.figure(figsize=(15, 6))
sns.countplot(
    result_mol["mall"], 
    data=result_mol, 
    palette="RdYlGn",
    order=result_mol["mall"].value_counts().index
)
plt.xticks(rotation=90)
plt.show()
