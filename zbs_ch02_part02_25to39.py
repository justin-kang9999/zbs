# 25 다중 상속
'''
2개 이상의 클래스를 상속한다
'''
class Car01:
    def drive(self):
        print("운전중")
class Car02:
    def turbo(self):
        print("터보 작동중")
class Car03:
    def fly(self):
        print("나는중")
class Car(Car01, Car02, Car03):
    def __init__(self):
        pass
my_car = Car()
my_car.fly()
#베이직에는 덧셈 뺄셈 곱셈 나눗셈 사칙연산만
class Basic_cal:
    def add(self, n1, n2):
        return n1 + n2
    def sub(self, n1, n2):
        return n1 - n2
    def mul(self, n1, n2):
        return n1 * n2
    def div(self, n1, n2):
        return n1 / n2
# 개선된 버전에는 나머지, 몫, 제곱
class Developer_cal:
    def mod(self, n1, n2):
        return n1 % n2
    def flo(self, n1, n2):
        return n1 // n2
    def exp(self, n1, n2):
        return n1 ** n2
# 다 상속받은 클래스
class New_cal(Basic_cal, Developer_cal):
    def __init__(self):
        pass

cal = New_cal()
cal.add(19, 11)
cal.sub(19, 11)
cal.exp(12, 2)
cal.flo(6, 3) 
cal.mod(5, 2)   
#다중 상속은 남발하면 안됨, 헷갈릴 수 있음

# 26 오버라이딩
'''
하위 클래스에서 상위 클래스의 메서드를 재정의 함
로봇이라는 상위 클래스
뉴로봇이라는 하위 클래스
로봇의 총알 발사를 레이저 발사로 바꾸는 것
더이상 상위 것의 기능을 사용하지 않고 받아와서 비슷하게 바꿔서 사용
'''
#상위 로봇 클래스
class Robot:
    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w
    def fire(self):
        print("총알 발사")
class New_robot(Robot):
    def __init__(self, c, h, w):
        super().__init__(c, h, w)
    def fire(self):
        print("레이저 발사")
    def robot_info(self):
        print("색상 : {0}\n높이 : {1}\n무게 : {2}".format(self.color, self.height, self.weight))
my_robot = New_robot('blue', 200, 150)
my_robot.fire()
        
'''
삼각형 넓이를 계산하는 클래스 만들고 이를 상속하는 클래스에서
get_area()를 오버라이딩해서 출력결과가 다음과 같을 수 있도록 하는 클래스
'''
class Triangle_area:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def triangle_info(self):
        print("가로 : {0}\n세로 : {1}".format(self.width, self.height))
    def get_area(self):
        return round((self.width * self.height) / 2, 2)
class New_triangle_area(Triangle_area):
    def __init__(self, w, h):
        super().__init__(w, h)
    def get_area(self):
        return str(super().get_area()) + '㎠'
    
tri_ar = New_triangle_area(7, 5)
tri_ar.triangle_info()
tri_ar.get_area()
    
# 27 추상 클래스
'''
상위클래스에서 하위 클래스에 메서드 구현을 강제하는 것
예시) 더하기 함수를 만들고 pass 한채로 하위 클래스가 받으면 더하기 함수의
기능을 구현하도록 함
구현하지 않으면 에러가 뜸
'''
from abc import ABCMeta
from abc import abstractclassmethod

class Airplane(metaclass = ABCMeta):
    @abstractclassmethod
    def flight(self):
        pass
    
    def forward(self):
        print("전진")
    def backward(self):
        print("후진")

class Airliner(Airplane):
    def __init__(self, c):
        self.color = c
        
    def flight(self):
        print("시속 400 km/h로 비행")

arl = Airliner('red')
arl.flight()

class Fight_plane(Airplane):
    def __init__(self, c):
        self.color = c
    def flight(self):
        print("시속 700 km/h로 비행")
farl = Fight_plane('black')
farl.flight()
'''
추상클래스로 상위 클래스를 만들어서 강제를 하는 이유:
어떠한 기능을 상속해서 각자 입맞에 맞게 수정해서 사용해라
실습
계산기 추상 클래스를 만들고 이를 이용해서 새로운 계산기 클래스 만들기
추상클래스에는 덧셈 뺄셈 곱셈 나눗셈 기능이 선언되어야 함
'''
from abc import ABCMeta
from abc import abstractclassmethod
class Old_cal(metaclass = ABCMeta):
    @abstractclassmethod
    def add(self, n1, n2):
        pass
    @abstractclassmethod
    def sub(self, n1, n2):
        pass
    @abstractclassmethod
    def mul(self, n1, n2):
        pass
    @abstractclassmethod
    def div(self, n1, n2):
        pass
# 상속 받는 cal
class New_cal(Old_cal):
    #반드시 구체화 해야 할 기능들을 구현
    def add(self, n1, n2):
        return n1 + n2
    def sub(self, n1, n2):
        return n1 - n2
    def mul(self, n1, n2):
        return n1 * n2
    def div(self, n1, n2):
        return n1 / n2
    # 새 기능 구현
    def mod(self, n1, n2):
        return n1 % n2
    def flo(self, n1, n2):
        return n1 //n2

cal_test = New_cal()
cal_test.add(15, 13)

# 28 예외란
'''
예외란, 문법적인 문제는 없으나 실행중 발생하는 예상치 못한 문제

'''
#예시 : 0으로 나눌 때 예외가 발생됨
cal_test.div(15, 0)
'''
예외 관련 클래스는 Exception 클래스를 상속한다
들여쓰기 에러, 인덱스 에러 등등
'''
int('hello')
list = [i for i in range(1,7)]
list[6]

# 29 예외처리
'''
예상하지 못한 예외가 프로그램 전체에 영향이 없도록 처리하는 것이 예외처리
예외 발생 예상 구문을 try ~ except로 감싼다
'''
try:
    cal_test.div(15, 0)
except:
    print("예상치 못한 예외가 발생했습니다\n다른 프로그램 실행에는 문제가 없습니다")

cal_test.div(15, 1)
cal_test.div(15, 3)
cal_test.div(15, 5)

nums = []
n = 1
# 예외처리를 해서 예외가 발생해도 문제 업이 진행되는 것을 확인
while n < 6:
    try:
        num = int(input('숫자를 입력 : ' ))
    except:
        print("예외 발생")
    nums.append(num)
    n += 1
print(nums)

# 30 try ~ except ~ else
'''
try ~ except ~ else
예외가 발생하지 않은 경우 발생하는 구문
'''
nums = []
n = 1
while n < 6:
    try:
        num = int(input('숫자를 입력 : ' ))
    except:
        print("예외 발생")
        continue
    else: # 예외가 발생하지 않으면 실행한다
        if num % 2 == 0:
            nums.append(num)
            n += 1
        else:
            print("입력한 숫자는 홀수 입니다.", end= '')
            print('다시 입력 하세요')
            continue
'''
실습 사용자로부터 숫자 5개를 입력 받아 짝수 홀수 실수로 
구분해서 각각 리스트에 저장하는 프로그램을 만들어보자
'''    
even_list, odd_list, float_list = [], [], []
n = 1
while n < 6:
    try:
        num = float(input('숫자를 입력 : ' ))
    except:
        print("예외 발생\n다시입력하세요")
        continue
    else: # 예외가 발생하지 않으면 실행한다
        if num - int(num) != 0:
            print(" 실수 ")
            float_list.append(num)
        else:
            if num % 2 == 0:
                print(" 짝수 ")
                even_list.append(int(num))
                
            else:
                print(" 홀수 ")
                odd_list.append(int(num))
        n += 1
print("홀수 리스트 {0}\n짝수 리스트 {1}\n실수 리스트 {2}".format(odd_list, even_list, float_list))

# 31 finally
'''
finally 구문
try ~ except ~ else 구문을 사용한 뒤에
예외 발생과 상관 없이 항상 실행한다

'''
even_list, odd_list, float_list = [], [], []
n = 1
while n < 6:
    try:
        num = float(input('숫자를 입력 : ' ))
    except:
        print("예외 발생\n다시입력하세요")
        continue
    else: # 예외가 발생하지 않으면 실행한다
        if num - int(num) != 0:
            print(" 실수 ")
            float_list.append(num)
        else:
            if num % 2 == 0:
                print(" 짝수 ")
                even_list.append(int(num))
                
            else:
                print(" 홀수 ")
                odd_list.append(int(num))
        n += 1

    finally:
        print("input_data : {0}".format(num))

print("홀수 리스트 {0}\n짝수 리스트 {1}\n실수 리스트 {2}".format(odd_list, even_list, float_list))
'''
사용자로부터 숫자 5개를 입력받아 짝수 홀수 실수와 입력한 모든 데이터를 
각각 출력하는 프로그램을 만들어보자

'''
even_list, odd_list, float_list, data_list= [], [], [], []
n = 1
while n < 6:
    try:
        data = input('숫자를 입력 : ' )
        float_num = float(data)
    except:
        print("예외 발생\n다시입력하세요")
        continue
    else: # 예외가 발생하지 않으면 실행한다
        if float_num - int(float_num) != 0:
            print(" 실수 ")
            float_list.append(float_num)
        else:
            if float_num % 2 == 0:
                print(" 짝수 ")
                even_list.append(int(float_num))
                
            else:
                print(" 홀수 ")
                odd_list.append(int(float_num))
        n += 1

    finally:
        data_list.append(data)
        print("input_data : {0}\ninput_data들 리스트 : {1}".format(data,data_list))
print("홀수 리스트 {0}\n짝수 리스트 {1}\n실수 리스트 {2}".format(odd_list, even_list, float_list))

# 32 exception 클래스
'''
예외를 담당하는 exception 클래스
예) 0으로 나눌 수 없습니다, out of range, 신텍스에러 등등
raise 의도적으로 예외를 발생 시킬 수 있는 키워드
'''
n01 = 10
n02 = 0
try:
    n01 / n02
except Exception as e:
    print("예외 : {0}".format(e))
    
'''
실습 사용자가 문자 메시지를 보낼 때 10글자 이하면 sms로 발송하고
10글자를 초과하면 발송하는 프로그램을 예외처리해서 만들어보자
'''
def send_sns(msg):
    if len(msg) > 10:
        raise Exception('길이 초과 MMS로 전환 후 발송',1)
    else:
        print('SMS로 발송')
def send_mms(msg):
    if len(msg) <= 10:
        raise Exception('길이 미달 SMS로 전환 후 발송',1)
    else:
        print('MMS로 발송')
msg = input("메세지를 입력하세요 : ")
try:
    send_sns(msg)
    
except Exception as e:
    print("에러 : ".format(e.args[0])) # 배열 형식
    print("에러 : ".format(e.args[1]))
    
    if e.args[1] == 1:
        send_mms(msg)
    elif e.args[1] == 2:
        send_sns(msg)
        
# 33 사용자 exception 클래스
'''
사용자 예외 클래스
Exception 클래스를 상속해서 사용자만의 예외 클래스를 만들 수 있다
'''
#0은 사용 할 수 없다고 클래스를 만들기
class Not_Use_Zero_Exception(Exception):
    def __init__(self, n):
        super().__init__(f"{n}은 사용할 수 없습니다")
def div_cal(num01, num02):
    if num02 == 0:
        raise Not_Use_Zero_Exception(num02)
    else:
        print("{0} / {1} = {2}".format(num01, num02, num01 / num02))
num01 = int(input("첫번째 숫자 입력"))
num02 = int(input("두번째 숫자 입력"))

try:
    div_cal(num01, num02)
except Not_Use_Zero_Exception as e:
    print(e)
    
'''
실습
관리자 암호를 입력하고 다음 상태에 따라 예외 처리하는 클래스를 만들어보자
암호 길이가 5 미만인 경우
암호길이가 10을 초과하는 경우
암호가 잘못된 경우
'''
#사용자 클래스 제작
class Password_Too_Short_Excation(Exception):
    def __init__(self, w):
        super().__init__(f"{w}은 너무 짧습니다 5글자 미만입니다")
class Password_Too_Long_Excation(Exception):
    def __init__(self, w):
        super().__init__(f"{w}은 너무 깁니다 10글자를 초과했습니다")
class Password_Wrong_Excation(Exception):
    def __init__(self, w):
        super().__init__(f"{w}은 비밀번호가 틀렸습니다")
        
admin_pw = input("admin 비밀번호 입력 : ")
try:
    if len(admin_pw) < 5:
        raise Password_Too_Short_Excation(admin_pw)
    elif len(admin_pw) > 10:
        raise Password_Too_Long_Excation(admin_pw)
    elif admin_pw != 'admin1234':
        raise Password_Wrong_Excation(admin_pw)
    elif admin_pw == 'admin1234':
        print("로그인이 되었습니다")
except Password_Too_Short_Excation as e1:
    print(e1)
except Password_Too_Long_Excation as e2:
    print(e2)
except Password_Wrong_Excation as e3:
    print(e3)

# 34 텍스트 파일 쓰기
'''
텍스트 파일을 파이썬으로 이용해서 만들어보자
open(), read(), write(), close()를 이용한 텍스트 파일 다루기
텍스트 파일은 open() - read() 또는 write() - close()순서로 됨
\를 /로 바꿔줘야함
w는 파일이 없으면 새로 만들고 기존의 문자열을 다 없애버리고 새로 적어버림
'''
#write 함수를 이용해 파일에 문자열 쓰기

file = open('J:/zero_base_school/part02_python/34.txt','w')
strCnt = file.write("Hello Python~")
print(f'strCnt : {strCnt}')
file.close()
'''
시스템 시간과 일정을 텍스트 파일에 작성해보자
'''
import time
lt = time.localtime()
date_str = '[' + str(lt.tm_year) + '년 ' + \
    str(lt.tm_mon) +  '월 ' + \
    str(lt.tm_mday) + '일] '

today_schedule = input('오늘 일정 : ')

file = open('J:/zero_base_school/part02_python/34.txt','w')
strCnt = file.write(date_str + today_schedule)
print(f'strCnt : {strCnt}')
file.close()

# 35 텍스트 파일 읽기
'''
read() 함수
txt파일의 문자열을 읽음
'''
#파일을 읽을 때는 'r'을 사용함
file = open('J:/zero_base_school/part02_python/34.txt','r')
str = file.read()
print(f'str : {str}')
file.close()

import time
lt = time.localtime()
date_str = '[' + time.strftime("%Y-%m-%d %I:%M:%S %p") + ']'
today_schedule = input('오늘 일정 : ')

file = open('J:/zero_base_school/part02_python/34.txt','w')
strCnt = file.write(date_str + today_schedule)
print(f'strCnt : {strCnt}')
file.close()
    
    
'''
다음 텍스트 파일에서 Python을 파이썬으로 변경해서 다시 저장
파이썬으로 읽어서 수정하고 바꾸기
'''
#일단 읽어오기
file = open('J:/zero_base_school/part02_python/about_python.txt','r', encoding= 'UTF8')
str = file.read()
print(f'str : {str}')
#replace 함수를 통해 수정시도
#인수를 주어서 2개까지만 수정하도록
str = str.replace("Python", "파이썬", 2) 
print(f'str : {str}')
file.close()

# 수정하기
file = open('J:/zero_base_school/part02_python/about_python.txt','w', encoding= 'UTF8')
#변경된 내용을 넣어줌
file.write(str)
file.close()

# 36 텍스트 파일 열기
'''
다양한 방법으로 열 수 있음
w 쓰기 전용(파일이 있으면 덮어씌움)
a 쓰기 전용(파일이 있으면 덧붙임)
x 쓰기 전용(파일이 있으면 에러 발생)
r 읽기 전용(파일이 없으면 에러 발생)
'''
urltxt = 'J:/zero_base_school/part02_python'
#계속해서 파일에 작성할 수 있도록 함수 만들기
def write_prime_num(n):
    file = open(urltxt + 'prime_numbers.txt', 'a', encoding='UTF8')
    file.write(str(n))
    file.write('\n')
    file.close()



#소수 판별 함수
def is_prime(n):
    if n == 2 or n == 3: return True
    if n%2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True

input_number = int(input("0보다 큰 정수 입력 : "))
for number in range(2, input_number + 1):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break
    
    if (flag):
        write_prime_num(number)
file.close()
# 37 with ~ as 문
'''
with ~ as 문을 사용하면 파일 닫기를 생략할 수 있다
코드블럭이 끝나면 알아서 꺼짐
'''
# 이런 식을 
file = open('J:/zero_base_school/part02_python/about_python.txt','w', encoding= 'UTF8')
file.write(str)
file.close()

#with ~ as 구문을 이용하면
with open('J:/zero_base_school/part02_python/about_python.txt','a', encoding= 'UTF8') as f:
    f.write("현재 37강중")
    
'''
로또 번호 생성기 프로그램을 만들고 파일에 번호를 출력해보자

'''

import random
urltxt = 'J:/zero_base_school/part02_python/'
def write_lotto(nums):
    for idx, num in enumerate(nums):
        with open(urltxt + '037_lotto.txt', 'a', encoding='UTF8') as f:
            if idx < (len(nums) - 2):
                f.write(str(num) + ', ')
            elif idx == (len(nums) - 2):
                f.write(str(num))
            elif idx == (len(nums) - 1):
                f.write('\n')
                f.write('bonus: ' + str(num))
                f.write('\n')

# 38 writelines()
'''
writelines()는 리스트나 튜플 데이터를 파일에 쓰기위한 함수
for문을 사용하지 않아도 된다

'''
lang= ['c/c++', 'java', 'c#', 'python', 'go']
urltxt = 'J:/zero_base_school/part02_python/'
with open(urltxt + 'languages.txt', 'a', encoding='UTF8') as f:
    f.writelines(item + '\n' for item in lang)
    
'''
딕셔너리에 저장된 과목별 점수를 파일에 저장하는 코드를 작성하자
'''

score_dic = {'kor': 85, 'eng': 90, 'mat': 92, 'sci': 79, 'his': 82}
urltxt = 'J:/zero_base_school/part02_python/'
for key in score_dic.keys():
    with open(urltxt + 'score_dic.txt', 'a', encoding='UTF8') as f:
        f.write(key + '\t : ' + str(score_dic[key]) + '\n')
        
# score_dic를 모양 그대로 저장하는 방법, 리스트도 가능하다
score_dic = {'kor': 85, 'eng': 90, 'mat': 92, 'sci': 79, 'his': 82}
with open(urltxt + 'scores.txt', 'a', encoding='UTF8') as f:
    print(score_dic, file= f)
    
# 39 readlines(), readline()
'''
여러줄 읽기와 한줄 읽기
readlilnes() 모든 데이터를 읽어서 리스트 형태로 반환한다. 
눈에 보이지 않는 \n까지 나옴

readline() 한 행씩 읽어서 문자열로 반환한다

'''
#readlines
urltxt = 'J:/zero_base_school/part02_python/'
with open(urltxt + 'lans.txt', 'r', encoding='UTF8') as f:
    lan_list = f.readlines()
print(lan_list)
print(type(lan_list))
# 리스트를 보면 \n을 기준으로 구분함
#readline
urltxt = 'J:/zero_base_school/part02_python/'
with open(urltxt + 'lans.txt', 'r', encoding='UTF8') as f:
    line = f.readline()
    while line != '':
        print(line, end = '')
        line = f.readline()
'''
실습
파일에 저장된 과목별 점수를 파이썬에서 읽어, 딕셔너리에 저장하는 코드를 만들어보자
'''
scores = {}
urltxt = 'J:/zero_base_school/part02_python/'
with open(urltxt + 'score_dic02.txt', 'r', encoding='UTF8') as f:
    line = f.readline()
    while line != '':
        print(line, end = '')
        line = f.readline()
    #잘 읽혀지는 것을 확인함. 여기서 다시 dic를 만들어야 함

scores = {}
urltxt = 'J:/zero_base_school/part02_python/'
with open(urltxt + 'score_dic02.txt', 'r', encoding='UTF8') as f:
    line = f.readline()
    while line != '':
        tmp_list = line.split(':')
        scores[tmp_list[0]] = int(tmp_list[1].strip('\n')) # \n을 삭제함
        line = f.readline()

scores





