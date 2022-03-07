## 01 - 06 강 시계열 데이터 분석 frbprophet

- 설치가 먼저 필요함
# !pip install fbprophet
# !pip install pandas-datareader 
from fbprophet import Prophet
from pandas_datareader import data
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
%matplotlib inline 

#코랩이어서
plt.rc('font', family='NanumBarunGothic') 

# 한글폰트 설치
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf
'''
함수 기초
def 예약어(들어갈 변수):
  return 값
전역변수
- global 변수를 def 내에서 사용하고 싶다면 global로 선언
'''
# 함수 기초
def test_def(a, b):
    return a + b

# 전역변수(global)
a = 1 

def edit_a(i):
    # 지역변수(local)
    global a 
    a = i 

edit_a(3)
a
- def 내에서 변수와 밖에서의 변수는 같은 이름이어도 다르다.

- 수학 기호 쓰는 방법

$$ y = asin(2\pi ft + t_0) + b $$
# sin 삼각함수 그래프 그리는 함수
def plotSinWave(amp, freq, endTime, sampleTime, startTime, bias):
    """
    내용작성
    plot sine wave 
    y = a sin(2 pi f t + t_0) + b
    """
    time = np.arange(startTime, endTime, sampleTime)
    result = amp * np.sin(2 * np.pi * freq * time + startTime) + bias 
    
    plt.figure(figsize=(12, 6))
    plt.plot(time, result)
    plt.grid(True)
    plt.xlabel("time")
    plt.ylabel("sin")
    plt.title(str(amp) + "*sin(2*pi" + str(freq) + "*t+" + str(startTime) + ")+" + str(bias))
    plt.show()
# 변수를 꼭 넣어야만 그려짐
plotSinWave(2, 1, 10, 0.01, 0.5, 0)
# 들어가는 변수가 많아서 수정하기
def plotSinWave(**kwargs):
    """
    plot sine wave 
    y = a sin(2 pi f t + t_0) + b
    기본값을 넣어서 변수를 안넣더라도 작동이 되도록
    """
    endTime = kwargs.get("endTime", 1)
    sampleTime = kwargs.get("sampleTime", 0.01)
    amp = kwargs.get("amp", 1)
    freq = kwargs.get("freq", 1)
    startTime = kwargs.get("startTime", 0)
    bias = kwargs.get("bias", 0)
    figsize = kwargs.get("figsize", (12, 6))
    
    time = np.arange(startTime, endTime, sampleTime)
    result = amp * np.sin(2 * np.pi * freq * time + startTime) + bias 
    
    plt.figure(figsize=(12, 6))
    plt.plot(time, result)
    plt.grid(True)
    plt.xlabel("time")
    plt.ylabel("sin")
    plt.title(str(amp) + "*sin(2*pi" + str(freq) + "*t+" + str(startTime) + ")+" + str(bias))
    plt.show()
plotSinWave()
### 내가 만든 함수 import
- drawSinWave.py
%%writefile ./drawSinWave.py

import numpy as np 
import matplotlib.pyplot as plt 

def plotSinWave(**kwargs):
    """
    plot sine wave 
    y = a sin(2 pi f t + t_0) + b
    """
    endTime = kwargs.get("endTime", 1)
    sampleTime = kwargs.get("sampleTime", 0.01)
    amp = kwargs.get("amp", 1)
    freq = kwargs.get("freq", 1)
    startTime = kwargs.get("startTime", 0)
    bias = kwargs.get("bias", 0)
    figsize = kwargs.get("figsize", (12, 6))
    
    time = np.arange(startTime, endTime, sampleTime)
    result = amp * np.sin(2 * np.pi * freq * time + startTime) + bias 
    
    plt.figure(figsize=(12, 6))
    plt.plot(time, result)
    plt.grid(True)
    plt.xlabel("time")
    plt.ylabel("sin")
    plt.title(str(amp) + "*sin(2*pi" + str(freq) + "*t+" + str(startTime) + ")+" + str(bias))
    plt.show()
    
if __name__ == "__main__":
    print("hello world~!!")
    print("this is test graph!!")
    plotSinWave(amp=1, endTime=2)
# 그래프 한글 설정

%%writefile ./set_matplotlib_hangul.py

import platform
import matplotlib.pyplot as plt 
from matplotlib import font_manager, rc

path = "c:/Windows/Fonts/malgun.ttf"

if platform.system() == "Darwin":
    print("Hangul OK in your MAC!!!")
    rc("font", family="Arial Unicode MS")
elif platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    print("Hangul OK in your Windows!!!")
    rc("font", family=font_name)
else:
    print("Unknown system.. sorry~~~")
    plt.rc('font', family='NanumBarunGothic') 
    
plt.rcParams["axes.unicode_minus"] = False 
import set_matplotlib_hangul
plt.title("한글")
## 07 - 08 강 fbprophet 기초


time = np.linspace(0, 1, 365*2)
result = np.sin(2*np.pi*12*time)
ds = pd.date_range("2018-01-01", periods=365*2, freq="D")
df = pd.DataFrame({"ds": ds, "y": result})
df.head()
df["y"].plot(figsize=(10, 6));
from fbprophet import Prophet

m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df);
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
m.plot(forecast);
time = np.linspace(0, 1, 365*2)
result = np.sin(2*np.pi*12*time) + time 

ds = pd.date_range("2018-01-01", periods=365*2, freq="D")
df = pd.DataFrame({"ds": ds, "y": result})

df["y"].plot(figsize=(10, 6));
# 예측한 값 시각화 
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
m.plot(forecast);
time = np.linspace(0, 1, 365*2)
result = np.sin(2*np.pi*12*time) + time + np.random.randn(365*2)/4

ds = pd.date_range("2018-01-01", periods=365*2, freq="D")
df = pd.DataFrame({"ds": ds, "y": result})

df["y"].plot(figsize=(10, 6));
# 다시 학습
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
m.plot(forecast);
## 09 - 10 강 웹 유입량 데이터 분석
- https://pinkwink.kr/

#모듈
import pandas as pd 
import pandas_datareader as web 
import numpy as np 
import matplotlib.pyplot as plt 

from fbprophet import Prophet
from datetime import datetime 

%matplotlib inline 
# 기존 로컬에서 작업할 때 방법
# pinkwink_web = pd.read_csv(
#     "../data/05_PinkWink_Web_Traffic.csv",
#     encoding="utf-8",
#     thousands=",",
#     names=["date", "hit"],
#     index_col=0
# )

# 구글 코랩 이용시
from google.colab import drive
drive.mount('/content/drive')
# 구글 드라이브 내 데이터 경로 설정
dataset_path = '/content/drive/MyDrive/zero_base/data/05_forecast/05_PinkWink_Web_Traffic.csv'
# csv 파일 읽기
pinkwink_web = pd.read_csv(dataset_path,
    encoding="utf-8",
    thousands=",",
    names=["date", "hit"],
    index_col=0
)

# null  값은 안갖고 오도록
pinkwink_web = pinkwink_web[pinkwink_web["hit"].notnull()]
# 확인
pinkwink_web.head()
# 날짜별 방문자 수 전체 데이터 그려보기 
pinkwink_web["hit"].plot(figsize=(12, 4), grid=True);
# trend 분석을 시각화하기 위한 x축 값을 만들기 
time = np.arange(0, len(pinkwink_web)) #범위를 arrange 형태로
traffic = pinkwink_web["hit"].values # 값 갖고오기
# 1차원 배열로 0 부터 끝까지, 
fx = np.linspace(0, time[-1], 1000)
# 에러를 계산할 함수 
# 트렌드를 찾고나면 실제와 예측값 차이를 확인하기 위함
def error(f, x, y):
    return np.sqrt(np.mean((f(x) - y) ** 2))
# 1차원으로 학습
fp1 = np.polyfit(time, traffic, 1)
# 통과시킨 변수명
f1 = np.poly1d(fp1)

# 2차원으로 학습
f2p = np.polyfit(time, traffic, 2)
f2 = np.poly1d(f2p)

# 3차원으로 학습
f3p = np.polyfit(time, traffic, 3)
f3 = np.poly1d(f3p)

# 15차원으로 학습
f15p = np.polyfit(time, traffic, 15)
f15 = np.poly1d(f15p)

# 에러 확인
print(error(f1, time, traffic))
print(error(f2, time, traffic))
print(error(f3, time, traffic))
print(error(f15, time, traffic))
# 차트 그려보기
plt.figure(figsize=(12, 4))
# 산점도
plt.scatter(time, traffic, s=10)
# 학습시킨 데이터들을 선으로
plt.plot(fx, f1(fx), lw=4, label='f1')
plt.plot(fx, f2(fx), lw=4, label='f2')
plt.plot(fx, f3(fx), lw=4, label='f3')
plt.plot(fx, f15(fx), lw=4, label='f15')

plt.grid(True, linestyle="-", color="0.75")
plt.legend(loc=2)
plt.show()
# 데이터 프레임으로 만들기

df = pd.DataFrame({"ds": pinkwink_web.index, "y": pinkwink_web["hit"]})
df.reset_index(inplace=True)
df["ds"] = pd.to_datetime(df["ds"], format="%y. %m. %d.")
del df["date"]
df.head()


m = Prophet(yearly_seasonality=True, daily_seasonality=True)
# 학습
m.fit(df);
# 60일에 해당하는 데이터 예측 
future = m.make_future_dataframe(periods=60)
future.tail()
# 예측 결과는 상한/하한의 범위를 포함해서 얻어진다 
forecast = m.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail()
m.plot(forecast);
m.plot_components(forecast);

## 11 - 12 강 주식 데이터 분석
#### 1. yahoo finance 이용
- https://finance.yahoo.com/quote/035420.KS/history?p=035420.KS&guccounter=1
!pip install yfinance
# 데이터 갖고 오기 위한 모듈
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# 웹 크롤링을 위함
url = "https://finance.yahoo.com/quote/035420.KS/history?p=035420.KS&guccounter=1"
req = Request(url, headers={"User-Agent": "Chrome"})
page = urlopen(req).read()
soup = BeautifulSoup(page, "html.parser")
table = soup.find("table")
# 야후 파이낸스에선 read_html이 잘 먹힘
df_raw = pd.read_html(str(table))[0] # 스트링형태로 갖고와야함
df_raw.head()
# fbprophet을 사용하는 형식에 맞춰준 뒤, 맨 마지막 NaN 값이 있어서 제외 
df_tmp = pd.DataFrame({"ds": df_raw["Date"], "y": df_raw["Close*"]})
df_target = df_tmp[:-1] # NaN값 삭제함
# fb 프로펫에 넣기 좋은 형태로 하는 만들어가는 중
df_target.head()
# harcopy 한 뒤에, 날짜를 fbprophet이 요구하는 형태로 변형
df = df_target.copy()
df["ds"] = pd.to_datetime(df_target["ds"], format="%b %d, %Y") # 형태
df.head()

# 결측치 제거
for i in range(len(df['y'])):
  if df['y'][i] == '-' or df['y'][i] == '501 Dividend':
    df['y'][i] = df['y'][i-1]
df['y'].unique()


# 데이터형 변환 object => float 

df["y"] = df["y"].astype("float")
df.info()
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df);
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail()
# 시각화
plt.figure(figsize=(12, 6))
plt.plot(df["ds"], df["y"], label="real")
plt.grid(True)
plt.show()
# 주제별로 시각화
m.plot_components(forecast);
# !pip install yfinance
# 기아자동차 분석
# 기아 자동차의 종목코드를 가지고 기간을 입력한다
import yfinance as yf
from pandas_datareader import data 

yf.pdr_override()
# 기간 설정
start_date = "2010-03-01"
end_date = "2018-02-28"
KIA = data.get_data_yahoo("000270.KS", start_date, end_date) # 주식 종목코드, 시작기간, 끝기간
# 실제 가격 추이
KIA["Close"].plot(figsize=(12, 6), grid=True);
# accuracy 확인을 위한 데이터 
KIA_trunc = KIA[:"2017-11-30"]
KIA_trunc.head()
# forecast를 위한 준비 
df = pd.DataFrame({"ds": KIA_trunc.index, "y":KIA_trunc["Close"]}) #ds는 날짜,
df.reset_index(inplace=True)
del df["Date"]
df.head()
# 학습
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df);
# 예측
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail()
# 예측값을 갖고 그래프 비교
m.plot(forecast);
m.plot_components(forecast);
KIA["Close"]
# 시각화
plt.figure(figsize=(12, 6))
plt.plot(KIA.index, KIA["Close"], label="real") # 실제데이터
plt.plot(forecast["ds"], forecast["yhat"], label="forecast") # 예측
plt.grid(True)
plt.legend()
plt.show()
# 대한항공 분석
# 003490 대한항공 

start_date = "2010-03-01"
end_date = "2018-02-28"
KoreaAir = data.get_data_yahoo("003490.KS", start_date, end_date)
KoreaAir.tail()
KoreaAir["Close"].plot(figsize=(12, 6), grid=True);
# accuracy 데이터 분리 
KoreaAir_trunc = KoreaAir[:"2017-11-30"]
KoreaAir_trunc.tail()
# forecast를 위한 준비 
df = pd.DataFrame({"ds": KoreaAir_trunc.index, "y": KoreaAir_trunc["Close"]})
df.reset_index(inplace=True)
del df["Date"]
df.head()
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df)
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail()
m.plot(forecast);
m.plot_components(forecast);
# 실제와 예측값 비교 그래프 
plt.figure(figsize=(12, 6))
plt.plot(KoreaAir.index, KoreaAir["Close"], label="real")
plt.plot(forecast["ds"], forecast["yhat"], label="forecast")
plt.grid(True)
plt.legend()
plt.show()
# 조금 특이한 경우

# Logistic 성장형 그래프를 가진 데이터에 대한 forecast 

dataset_path02 = '/content/drive/MyDrive/zero_base/data/05_forecast/05_example_wp_R2.csv.csv'
#df = pd.read_csv("../data/05_example_wp_R2.csv", index_col=0)
df = pd.read_csv(dataset_path02, index_col=0)
df["y"].plot(figsize=(12, 4), grid=True);
df["cap"] = 8.5
df.tail()
# 학습
m = Prophet(growth="logistic", daily_seasonality=True)
m.fit(df);
# 예측
future = m.make_future_dataframe(periods=1826) #기간은 1826일
future["cap"] = 8.5 
#예측
forecast = m.predict(future)
# 그래프를 그려서 확인
m.plot(forecast);

## 13 - 14 강 비트코인 데이터 분석

- https://bitcoincharts.com/charts/bitstampUSD#rg60ztgSzm1g10zm2g25zv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import time 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from fbprophet import Prophet

%matplotlib inline 
# url 불러오기
url = "https://bitcoincharts.com/charts/bitstampUSD#rg730ztgSzm1g10zm2g25zv"
driver = webdriver.Chrome("../driver/chromedriver")
driver.get(url)
# 스크롤 
xpath = '//*[@id="content_chart"]/div/div[2]/a'
variable = driver.find_element_by_xpath(xpath)
driver.execute_script("return arguments[0].scrollIntoView();", variable)
variable.click()
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", "data")
table
driver.quit()
# 데이터프레임화
df = pd.read_html(str(table))
bitcoin = df[0]
bitcoin.head()
# 원래 있던 파일 삭제
!rm -rf "../data/05_bitcoin_history.csv"
# 다시 저장
bitcoin.to_csv("../data/05_bitcoin_history.csv", sep=",")
bitcoin = pd.read_csv("../data/05_bitcoin_history.csv", index_col=0)
bitcoin.tail()
# 분석하고 싶은 항목(Close)만 가지고, Prophet 적용 

df = pd.DataFrame({"ds": bitcoin["Timestamp"], "y": bitcoin["Close"]})
m = Prophet(yearly_seasonality=True, daily_seasonality=True)
m.fit(df);
# 향후 30일간의 forecast
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
m.plot(forecast);

# 트렌드 및 주제별 분석
m.plot_components(forecast);
