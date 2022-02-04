# 01 함수
'''
내장함수 - 기본적으로 제공하는 함수
사용자함수- 사용자가 직접 선언
함수는 특정 기능을 재사용하기 위하여 사용

'''
# 덧셈을 하는 함수
def add_cal():
    n1 = int(input("n1 입력 : "))
    n2 = int(input("n2 입력 : "))
    print(f'n1 + n2 = {n1 + n2}')
add_cal()
add_cal()
add_cal()
add_cal()
add_cal()

# 02 함수 선언
'''
함수는 def 키워드, 함수명, :, 들여쓰기를 이용해서 선언한다
함수 호출
함수명과 '()'를 이용해서 함수를 호출한다
'''
#오늘 날씨를 출력하는 함수를 선언하고 세번 호출하기
def print_weather_info():
    print("오늘 날씨는 맑습니다. 기온은 25도 입니다")
print_weather_info()
print_weather_info()
print_weather_info()
print_weather_info()

#정수 두개를 입력하면 곱셈과 나눗셈 연산 결과를 출력하는 함수를 만들고 호출
def cal_fun():
    n1 = int(input("n1 입력 : "))
    n2 = int(input("n2 입력 : "))
    print(f'n1 * n2 = {n1 * n2}')
    print(f'n1 / n2 = {round(n1 / n2, 2)}')
cal_fun()

# 03 함수 내 또다른 함수 호출

'''
함수 내에서 또다른 함수를 호출 할 수 있다
pass를 통해서 실행문을 생략할 수 있다
'''
#구구단 출력함수가 연쇄적으로 호출되도록 하는 함수
def gugu02():
    for i in range(1,10):
        print('2 * {0} = {1}'.format(i, 2 * i))
    gugu03()    

def gugu03():
    for i in range(1,10):
        print('3 * {0} = {1}'.format(i, 3 * i))
    gugu04()    
    
def gugu04():
    for i in range(1,10):
        print('4 * {0} = {1}'.format(i, 4 * i))    
gugu02()

# 04 인수와 매개변수
'''
함수 호출 시 함수에 데이터를 전달 할 수 있다
인수와 매개 변수의 갯수는 일치해야한다.
매개변수의 갯수가 정해지지 않은 경우 *을 이용한다
'''
def print_number(*numbers):
    for number in numbers:
        print(number, end = ' ')
    print()
print_number()
print_number(1)
print_number(1, 2)
print_number(1, 2, 3)
print_number(1, 2, 3, 4)
print_number(1, 2, 3, 4, 5)

'''
국영수 점수를 입력받고 입력받은 점수를 이용해서 총점과 평균을 구하는 함수를
만들어보자
'''

def print_score(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3
    print(f'총점 : {sum}')
    print(f'평균 : {round(avg, 2)}')
    
kor_score = int(input("국어 점수 입력 : "))
eng_score = int(input("영어 점수 입력 : "))
mat_score = int(input("수학 점수 입력 : "))

print_score(kor_score, eng_score, mat_score)

# 05 데이터 반환
'''
return 키워드를 이용하면 함수 실행 결과를 호출부로 반환할 수 있다.
함수가 retrun을 만나면 실행을 종료한다
'''
def calc(n1, n2):
    result = n1 + n2
    return result

retrun_val = calc(20,10)
print("리턴 값 : {0}".format(retrun_val))

def div_num(n):
    odd_n = " 홀수"
    even_n = "짝수"
    if n % 2 == 0:
        result = even_n
    else:
        result = odd_n
    return result
retrun_val = div_num(20)
print("리턴 값 : {0}".format(retrun_val))     

'''
사용자가 길이 cm을 입력하면 mm값으로 환산하는 값으로 반환하는 함수
'''

def cm_to_mm(cm):
    result = cm * 10
    return result
length = float(input("cm단위로 길이를 입력 : "))
retrun_val = cm_to_mm(length)
print(f'리턴 값 : {retrun_val}mm')

'''
1부터 100까지 정수중에서 홀수인 난수를 변환하는 함수
'''
import random
from re import S

from numpy import average
def get_odd_rand_num():
    while True:
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break
    return rNum

print(f'리턴 값 : {get_odd_rand_num()}')

# 06 지역변수 전역변수
'''
전역변수 : 함수 밖에서 선언된 변수. 함수안에서는 수정 불가능
지역변수 : 함수 안에 선언된 변수. 함수 안에서만 사용 가능.
global 키워드
global을 사용하면 함수 안에서도 전역 변수의 값을 수정할 수 있따.
'''
num_out = 10
def print_num():
    global num_out
    num_out = 20
    print("리턴 값 : {0}".format(num_out))
print_num()

'''
사용자가 가로 세로 길이를 입력하면 삼각형과 사각형의 넓이를 
출력하는 함수를 만들어보자
'''
def pri_area():
    tri_area = wid * hei / 2
    sqr_area = wid * hei
    print("삼각형 넓이 : {0}".format(tri_area))
    print("사각형 넓이 : {0}".format(sqr_area))

wid = int(input("가로길이 입력"))
hei = int(input("세로길이 입력"))
pri_area()

# 방문객수를 카운트하는 함수를 만들어보자
total_visit = 0
def count_visit():
    global total_visit
    total_visit += 1
    print("누적 방문객 : {0}".format(total_visit))
count_visit()
count_visit()
count_visit()

# 07 중첩 함수
'''
함수안에 또다른 함수가 있는 형태
내부함수를 함수 밖에서 호출할 수 없다.
'''
# cal 함수를 선언하고 함수 안에서 덧셈 뺄셈 곱셈 나눗셈 함수를 선언
def cal(n1, n2, operator):
    print("1. 덧셈, 2. 뺄셈, 3. 곱셈, 4. 나눗셈, \n5. 1,2,3,4가 아닌 숫자 아무거나쓰면 종료")
    def add_cal():
        print("덧셈 연산 : {0}".format(round(n1 + n2 , 2)))
    def min_cal():
        print("뺄셈 연산 : {0}".format(round(n1 - n2 , 2)))
    def mul_cal():
        print("곱셈 연산 : {0}".format(round(n1 * n2 , 2)))
    def div_cal():
        print("나눗셈 연산 : {0}".format(round(n1 / n2 , 2)))
    if operator == 1:
        add_cal()
    elif operator == 2:
        min_cal()
    elif operator == 3:
        mul_cal()
    elif operator == 4:
        div_cal()
    else:
        print("종료가 되었습니다")
        
cal(3, 4, 2)

# 08 lamda 함수
'''
람다 키워드를 이용하면 함수 선언을 보다 간단하게 할 수 있다
lambda n1, n2 : n1 + n2
더하기를 이렇게 간단히  표현할 수 있음
'''
def add_cal():
    n1 = int(input("n1 입력 : "))
    n2 = int(input("n2 입력 : "))
    print(f'n1 + n2 = {n1 + n2}')
    
cal = lambda n1, n2 : n1 +n2
return_val = cal(10, 20)
print(return_val)

'''
삼각형, 사각형 원 넓이를 반환하는 람다 함수

'''
get_tri_area = lambda n1, n2 : n1  * n2 / 2
get_sqr_area = lambda n1, n2 : n1  * n2
get_cir_area = lambda n1 : (n1  ** 2) * 3.14
print("삼각형 넓이 : {}".format(get_tri_area(10, 20)))
print("사각형 넓이 : {}".format(get_sqr_area(10, 20)))
print("원 넓이 : {}".format(get_cir_area(5)))

# 09 모듈

'''
모듈 : 이미 만들어진 기능으로 쉽게 불러와서 사용할 수 있다.
내부모듈: 파이썬 설치 시 기본적으로 사용 가능한 모듈
외부모듈: 별도 설치 후 사용할 수 있는 모듈
사용자모듈: 사용자가 직접 만든 모듈
'''

#random 모듈을 이용해서 1~10까지 정수 중 난수를 발생
import random
r_num = random.randint(1,10)
print(r_num)
#random 모듈을 이용해서 1~100까지 정수 중 난수를 10개 발생
import random
r_num = random.sample(range(1,101),10)
print(r_num)

# 10 모듈 제작

'''
py 파일을 하나 만들어서 import로 가져올 수 있음
'''
import zbs_part03_10_modules.py as mod_10

zbs_part03_10_modules.get_lotto()
str = "치킨먹고싶다"
zbs_part03_10_modules.reverse_str()

# 11 모듈 사용
'''
import, from, as를 사용
import를 통해서 모듈을 불러오고 as를 통해 이름을 단축해서 사용할 수 있다.
from~ as 키워드를 통해서 모듈의 특정 기능을 사용할 수 있다..
'''

'''
국영수 점수를 입력받고 입력받은 점수를 이용해서 총점과 평균을 구하는 함수를
모듈화 해보자
'''

def print_score(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3
    print(f'총점 : {sum}')
    print(f'평균 : {round(avg, 2)}')
    
kor_score = int(input("국어 점수 입력 : "))
eng_score = int(input("영어 점수 입력 : "))
mat_score = int(input("수학 점수 입력 : "))

print_score(kor_score, eng_score, mat_score)
# 모듈화
scores = []
def add_score(s):
    scores.append(s)
def get_score():
    return scores
def get_total():
    total = 0
    for s in scores:
        total += S
    return total
def get_avg():
    avg = get_total() / len(scores)
    return avg

# 12 -13 실행(메인) 파일
'''
__name__을 통해서 전역변수를 사용할 수 있다.
파이썬을 실행시키면 기본적으로 제공해줌. py파일의 이름을 기본적으로 저장함
__name__ = '__main__' 실행파일인 경우에는 이렇게 메인이 저장 됨
파일이 많기 때문에
자기의 파일명이 아닌 main인 것을 찾아가면 프로그램의 시작, 실행파일이다.

'''
