print(10+20)
print("Hello python")

# 본인 정보를 출력하는 프로그램 만들기
print("홍길동\n20살\n남자\nhong@gmail.com\n서울시 종로구\n 축구, 수영,음식")

#03 프로그램 실행과정
print('일요일인 1일은 전국이 대체로 흐린 가운데 새벽에 전라권 서부와 충남 서해안, 경기 서해안 지역을 시작으로 비가 내리겠다\n')
print('비는 오전들어 수도권과 강원도 충청권 내륙, 경북 동부, 전남권으로 확대되겠고 오후에는 전국에 비가 오겠다.')
print('예상 강수량은 20~70mm다.')
print('아침 최저기온은 23~27도, 낮 최고기온은 39~34도로 예보됐다.')
print('강수의 영향으로 습도가 높아 체감온도가 대부분 지역에서 33도 이상으로 오르겠도 열대야 현상도 지속되겠다.')

#04 파이참
print(10*5)
print('hello pycharm')
print('good ' *3)

#05 데이터와 메모리 그리고 데이터 출력
'''
데이터->메모리->출력 순서
good morning을 10번 실행해보자
'''
print("good morning\n" * 10)

'''
자신의 이름 주소 연락처 메일주소를 출력해보자
내일 할일 출력
지난주 지출액 항목별로 출력
오늘 가장 인상 깊었던 일 출력
메신저를 이용해 친구한테 전송할 내용을 출력해보자
'''
print("홍길동\n20살\n010-0000-0000\nhong@gmail.com\n러버덕\n치킨 20,000원\n정신없어서 모르겠다\n안녕")

# 06 변수
'''
변수
데이터가 저장되어 있는 메모리 공간
데이터에 접근하기 위해서는 그 주소에 접근해야하는데 주소가 너무 복잡하므로
간단히 이름을 줘서 간단하게 접근할 수 있도록 하는게 변수
그 간단한 이름을 변수명이라고 함
'''

number =10

'''
변수를 이용해
자신의 이름 주소 연락처 메일주소를 출력해보자
내일 할일 출력
지난주 지출액 항목별로 출력
오늘 가장 인상 깊었던 일 출력
메신저를 이용해 친구한테 전송할 내용을 출력해보자
'''
name = "홍길동"
address = "서울시 종로구"
spent_yesterday = "치킨, 20,000원"
today_moved = "none"
message_to_fr = "hello guys"
print("이름 : {0}\n주소 : {1}\n어제 소비 : {2}\n오늘 인상깊었던 일 : {3}\n전송할 메시지 : {4}\n".format(name, address, spent_yesterday, today_moved, message_to_fr))

#07 변수를 사용하는 이유
'''
변수는 데이터를 재사용하고자, 효율적으로 수정하기 위해 사용
print("hello")나 
intro = "hello"
print(intro)나 다 같은 결과가 나오는데 왜 변수를 쓰는 걸까?


변수를 사용하지 않은 경우 하나하나 다 찾아서 모든 문구를 수정해야 하는데
사람인 이상 어렵기 때문에 변수만 찾아서 변수의 내용만 수정하면 됨
'''
num01 = 10
num02 = 20
print(num01 + num02)

'''
이름만 바뀌고 변수로 템플릿을 저장해두면 편함 
'''
name = '홍길동'
truble_hong = "에어컨 고장"
print(name, "고객님께")
print(name, "고객님 안녕하세요")
print('고객님께서 접수하신 a/s 건에 대하여 연락을 드렸으나 연락이 어려워 메일 드립니다.')
print('a/s 접수 내용 : ', truble_hong)
print('-------------------------------')
print('성함 : ', name)
print('내용 : ', truble_hong)

#08 변수명은 이렇게 하세요
'''
변수명 작명법
영문을 사용(한글도 변수로 가능은 함)
첫번째는 소문자로(클래스가 대문자로 시작하기 때문에 혼동을 방지하기 위함)
가급적 데이터의 의미를 파악할 수 있는 명사를 사용함
카멜 표기법 또는 스네이크 표기법 사용
카멜 표기법 : myName 이런식으로 단어가 바뀔때마다 대문자를 사용
스네이크 표기법 : my_address_detail 처럼 언더바를 사용

예약어는 사용 금지
특수문자는 언더바를 제외하고 사용할 수 없음
공백문자는 사용 금지
숫자는 사용해도 되지만 첫번째는 사용 금지

'''
my_address = '대한민국 서울특별시'
my_weight = 80

'''
삼각형의 넓이를 계산하기 위한 가로(20cm), 세로(15cm) 변수를 정의하고
결과를 출력해보자
위에서 정의한 변수를 이용해서 사각형의 넓이를 출력해보자
가로, 세로 길이를 임의로 변경한 후 삼각형과 사각형의 넓이를 각각 출력해보자
'''
wid = 20
hei = 15
print("삼각형의 넓이 : ",wid * hei / 2)
print("사각형의 넓이 : ", wid * hei)

#09 자료형
'''
효율적인 메모리 사용을 위해서 데이터를 정수형 실수형 문자열형 논리형으로 구분한 것.
정수 : int
실수 : float
문자열 : str
논리 : bool

파이썬에선 문자와 문자열을 구분하지 않음. 그래서 ''나 ""를 혼용해서 사용해도 됨

'''
num = 99999999999999999999999999999999999999999999
print(num) #출력결과 그대로 잘 나옴
f_num = 0.12222223444444555555777777777888888866666666
print(f_num) # 출력결과 0.12222223444444555 중간에 잘려서 나옴
score =100
pi = 3.141592
str_pi = '3.141592'
want_go = '캐나다'
adult = True
str_adult = 'True'

# 10 자료형 변환(문자)
'''
자료형 변환 : 데이터 타입을 변환하는 것으로 파이썬에서 제공하는 함수를 이용
'''
iNum = 10
fNum = 3.14
type(iNum)
type(fNum)

iNum = (str(iNum))
type(iNum)
fNum = (str(fNum))
type(fNum)

var = True
type(str(var))

# 실행 결과를 보고 변수를 형변환 하자
'''
num1 = 123
num2 = 456
일때 
print(num1 +num2) 
# 출력결과 579가 나는 경우
# 출력결과 123456이 나오는 경우
'''
num1 = 123
num2 = 456
print(num1 +num2) 
num1 = str(num1)
num2 = str(num2)
print(num1 +num2)

fNum1 = 3.14
fNum2 = 0.123
print(fNum1 + fNum2)

fNum1 = str(fNum1)
fNum2 = str(fNum2)
print(fNum1 + fNum2)

# 11 자료형 변환 숫자
'''
문자열을 정수 혹은 실수로 형변환 하려면?
int(), float()를 활용
'''
var = '100'
type(var)
type(int(var))
type(float(var))

'''
실행결과를 보고 형변환을 하자
str1 = '10'
str2 = '20'
출력결과 1 1020
출력결과 2 30
출력결과 3 30.0
'''
str1 = '10'
str2 = '20'
# #출력결과 1 문자열
print(str1+str2)
# #출력결과 2 정수형
str1 = int(str1)
str2 = int(str2)
print(str1+str2)
# #출력결과 3 실수형
str1 = float(str1)
str2 = float(str2)
print(str1+str2)

str1 = '3.14'
str2 = '1592'
# #출력결과 1 문자열
print(str1+str2)
# #출력결과 2 실수형
str1 = float(str1)
str2 = float(str2)
print(str1+str2)

# #bool 형을 숫자형으로 형변환
str1 = True
str2 = False
print(str1)
print(str2)
print(int(str1))

#12 자료형 변환 그외 데이터
'''
빈문자vs 공백문자
빈문자 : ''
공백문자 : ' ' 공백이 있음
빈문자를 논리형으로 바꾸면 False
공백문자를 논리형으로 바꾸면 True

문자열-> 논리형 -> 산술연산
문자열을 논리형으로 바꾸면 빈문자를 제외하면 무조건 True
True이므로 산술연산하려고 변환하면 무조건 1이 된다
''' 
#공백문자 자료형 변환
var = ''
type(bool(var))
var = ' '
type(bool(var))

#문자열 자료형 변환
var1 = "True"
var2 = "False"

var1 = bool(var1)
var2 = bool(var2)
print(var1, var2)
#bool형 연산
print(var1 + var2)
print(type(var1 + var2))
'''
논리형 산술연산. 실행결과를 보고 형변환 하자
var1 = "True"
var2 = "False"
print(var1 + var2) # 출력결과 2
print(var1 - var2) # 출력결과 0
print(var1 * var2) # 출력결과 1
print(var1 / var2) # 출력결과 1.0
'''
var1 = "True"
var2 = "False"
var1 = bool(var1)
var2 = bool(var2)
print(var1 + var2) # 출력결과 2
print(var1 - var2) # 출력결과 0
print(var1 * var2) # 출력결과 1
var1 = float(var1)
var2 = float(var2)
print(var1 / var2) # 출력결과 1.0

#13 데이터 입력
'''
input()함수는 데이터 입력을 위한 함수
print()함수는 데이터 출력을 위한 함수
input()함수를 통해 입력받은 데이터는 항상 문자열이다.
형변환을 통해서 사용해야 한다.

'''
user_input_data= input("키보드를 통해서 데이터를 입력하세요")
print(user_input_data, type(user_input_data)) #<class 'str'>
user_input_data= int(input("키보드를 통해서 데이터를 입력하세요"))
print(user_input_data, type(user_input_data)) #<class 'int'>
user_input_data= float(input("키보드를 통해서 데이터를 입력하세요"))
print(user_input_data, type(user_input_data)) #<class 'float'>
user_input_data= bool(input("키보드를 통해서 데이터를 입력하세요"))
print(user_input_data, type(user_input_data)) #<class ''>
'''
문제1 오늘의 날씨를 입력하고 출력해보자
문제2 사용자 이름을 입력하고 입력한 데이터의 자료명을 확인해보자
문제3 사용자가 가로세로 길이를 입력하면 삼각형과 사각형의 넓이가 출력되는 코드
'''
#문제1 오늘의 날씨
user_weather = input("오늘의 날씨를 입력해주세요 : ")
print("오늘의 날씨는 {0} 입니다".format(user_weather))

#문제2 사용자 이름을 입력하고 입력한 데이터의 자료명을 확인
user_name= input("이름를 입력하세요 : ")
print(user_name, type(user_name)) #<class 'str'>

#문제 3 가로세로 입력받아 삼각형, 사각형 넓이 구하기
user_wid = int(input("가로 길이를 숫자로만 입력해주세요 : "))
user_hei = int(input("세로 길이를 숫자로만 입력해주세요 : "))
print("삼각형의 넓이는 {0}이고, 사각형의 넓이는 {1}입니다.".format(int(user_wid*user_hei/2) , user_wid*user_hei))

#14 데이터 출력
'''
print() 대표적인 데이터 출력 함수
print() 함수의 다양한 사용방법을 배워보자
특수문자 
\t -> 탭해서 4칸가량 띄우기
\n -> 줄바꿈
'''
user_name = '홍길동'
user_age = 20
print("이름 : ", user_name, "나이 : ", user_age)

print('3 * 5 = ', end= '')# 자동 줄바꿈을 안할때
print(3 * 5)

'''
포맷 문자열을 이용한 데이터 출력
'''
print(f'이름 : {user_name}, 나이 : {user_age}')
# 개인적으로 애용하는 방법
print("이름 : {0}\n나이 : {1}".format(user_name, user_age))

'''
실행결과가 다음과 같이 출력될 수 있도록 코드를 작성해보자
가로 길이 입력 : 
세로 길이 입력 :
출력결과 1
width : 10.5
height : 5.5
triangle : 28.875
squar : 57.75

출력결과 2
width : 10.5, height : 5.5
triangle : 28.875, square : 57.75

출력결과 3
width : 10.5,      height : 5.5
triangle : 28.875, square : 57.75

'''

user_wid = float(input("가로 길이를 숫자로만 입력해주세요 : "))
user_hei = float(input("세로 길이를 숫자로만 입력해주세요 : "))
tri = (user_wid * user_hei / 2)
sqr = tri * 2
#출력 1
print("width : {0}\nheight : {1}\ntriangle : {2}\nsquare : {3}".format(user_wid, user_hei, tri, sqr))
#출력 2
print("width : {0}, height : {1}\ntriangle : {2}, square : {3}".format(user_wid, user_hei, tri, sqr))
#출력 3
print("width : {0},\t height : {1}\ntriangle : {2}, square : {3}".format(user_wid, user_hei, tri, sqr))