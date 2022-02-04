# 14 패키지

'''
모듈의 갯수가 많아지면 관리하기가 어려움.
패키지를 이용하면 관련있는 모듈을 그룹으로 관리 할 수 있다

'''
from cgitb import reset
from torch import lt
from calforint import package
package.get_lotto()

# 15 site- packges
'''
지금 기존에 만든 것은 로컬 디렉토리에 패키지를 만들고 갖고 옴.
실행파일과 파일 위치가 동일할 때 사용 가능.
site- packages에 있는 모듈은 어디에서나 사용 할 수 있다.
가상 환경을 사용하도록 하는 것이 venv
site- packages 폴더로 옮기면 어디서든 사용 가능하다.
'''
import sys
for path in sys.path:
    print(path)
# site- packages에 약수와 소수를 리스트로 반환하는 모듈을 만들어보자
from divisor_pac import divisor_mod as dm
print(f'10의 약수 : {dm.divisor(10)}')
print(f"50까지의 소수 : {dm.prime_number(50)}")

# 16 자주 사용하는 외부 모듈
'''
math 수학 관련
random 난수 발생 관련
time 시간 관련 
'''
# 수학 관련 내장함수
listVar =[2, 5, 3, 10]
# 합 sum
print(f'sum : {sum(listVar)}')
# 최댓값 max
print(f'max : {max(listVar)}')
# 최솟값 min
print(f'min : {min(listVar)}')
# 거듭제곱 pow
print(f'{pow(13, 2)}')
# 반올림 round
print("{}".format(round(3.141592, 2)))

# math 모듈
import math
#절댓값 math.fabs
print("-10의 절댓값 : {}".format(math.fabs(-10)))
# 올림 math.ceil
math.ceil(5.21)
# 내림 math.floor
math.floor(5.21)
#버림 math.trunc
math.trunc(5.21)
# 최대 공약수 math.gcd
math.gcd(14,21)
# 팩토리얼 math.factorial
math.factorial(5)
# 제곱근 math.sqrt
math.sqrt(144)

# 난수 관련 모듈
import random

# 시간 관련 모듈 time
import time
lt = time.localtime()
print("local time : {0}".format(lt))
print(lt.tm_year) # 연도만
print(lt.tm_mon) # 월만
print(lt.tm_wday) # 요일만

# 17 객체지향 프로그래밍
'''
프로그래밍의 꽃. 
객체지향 프로그래밍은 객체를 이용한 프로그램으로 객체는 속성과 기능으로 구성된다.
객체(object) = 속성(attribute) + 기능(function)

계산기라는 객체를 만든다고 친다면
속성으로 숫자가 필요
기능으로는 덧셈 뺄셈 곱셈 나눗셈 제곱근 제곱 등등등
객체는 클래스에서 생성된다.
클래스는 객체를 만드는 틀

예시) 붕어빵이라는 객체를 만든다고 할 때 붕어빵 틀은 클래스
우리는 클래스를 만드는 것.

객체 사용의 장점
코드 재사용, 모듈화에 좋다.
'''

# 18 클래스와 객체 생성
'''
클래스 만들기 
클래스는 class 키워드, 속성(변수), 기능(함수)을 이용해서 만든다
클래스는 처음에 대문자로 하는 것이 관례
'''

class Car:
    #생성자와 속성을 선언
    def __init__(self, color, length):
        self.color = color
        self.length = length
    #멈추는 기능 시작하는 기능
    def do_stop(self):
        print("Stop")
    def do_start(self):
        print("Start")
    def car_info(self):
        print(self.color)
        print(self.length)

'''
객체 생성
객체는 클래스의 생성자를 호출한다

'''
car01 = Car('red', 200)
car02 = Car('blue', 300)
car01.do_start()
car01.car_info()
'''
이렇게 car 01, 02라는 객체를 만들면 Car 클래스 내에 자동적으로
init method를 불러옴. 그래서 뒤에 빨간색 200 이런 값을 그대로 할당해줌 
'''

# 실습 비행기 클래스를 만들고 비행기 객체 5개를 생성해보자
class Airplane:
    #생성자와 속성을 선언
    def __init__(self, name, p_y):
        self.name = name
        self.p_y = p_y
    #멈추는 기능 시작하는 기능
    def do_stop(self):
        print("Stop")
    def do_start(self):
        print("Start")
    def do_land(self):
        print("Landing now")
    def do_take_off(self):
        print("Taking off now")
    def plane_info(self):
        print(self.name)
        print(self.p_y)

air_01 = Airplane('a320', 1987)
air_02 = Airplane('a380', 2004)
air_03 = Airplane('b747', 1995)
air_04 = Airplane('b737', 2002)
air_05 = Airplane('b787', 2010)

air_01.do_land()

# 19 객체 속성 변경
'''
객체 속성은 변경할 수 있다.
클래스는 대략적으로 만들고 차차 사용하면서 기능을 추가하던가 
삭제하던가 해야함
'''
class NewGenPC:
    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd
    def do_excel(self):
        print("엑셀이 실행됩니다")
    def do_photoshop(self):
        print("포토샵이 실행됩니다")
    def pcinfo(self):
        print("이름 : {}".format(self.name))
        print("cpu : {}".format(self.cpu))
        print("ram : {} gb".format(self.memory))
        print("ssd 용량 : {} gb".format(self.ssd))

pc01 = NewGenPC('pc01', 'ryzen 3600', 8, 256)
pc01.pcinfo()
pc02 = NewGenPC('pc02', 'intel 12700', 32, 512) 
pc02.pcinfo()
#pc01를 업그레이드
pc01.cpu = 'ryzen 5600x'
pc01.memory = 64
pc01.ssd = 1024
pc01.pcinfo()
#계산기 클래스를 만들고 사칙연산을 실행해보자
class Calcu:
    def __init__(self):
        self.number01 = 0
        self.number02 = 0
        self.result = 0

    def add(self):
        self.result = self.number01 + self.number02
        return self.result
    def sub(self):
        self.result = self.number01 - self.number02
        return self.result
    def mul(self):
        self.result = self.number01 * self.number02
        return self.result
    def div(self):
        self.result = self.number01 / self.number02
number01 = 15
number02 = 30
cal_test01 = Calcu()
cal_test01.add()
        
# 20 객체와 메모리
'''
변수는 객체의 메모리 주소를 저장하고 이를 이용해서 객체를 참조한다

'''
class Robot:
    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight
    def robot_info(self):
        print("색상 : {0}\n크기 : {1}\n무게 : {2}".format(self.color, self.height, self.weight))

rb01 = Robot('red', 200, 80)
rb02 = Robot('blue', 300, 100)
rb03 = rb01 #이런 경우를 얕은 복사라고 함
rb01.robot_info()
rb02.robot_info()
rb03.robot_info()
# rb01의 내용이 수정이 되면 자동으로 rb03도 수정이 됨
rb01.color = 'gray'
rb01.height = 250
rb01.weight = 150

'''
얕은 복사의 경우 
rb01이 저장된 주소를 공유하여 
rb03도 rb01이 저장된 주소로 할당되어 있다
'''

'''
국영수 점수를 받아 리스트에 저장하고 원본은 유지하고 복사본을 만들어
과목별 점수를 10%올렸을 경우 평균을 출력
'''
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
mat = int(input("수학 점수 : "))
scores = [kor,eng,mat]

score_copy = scores.copy()
for idx, score in enumerate(score_copy):
    result = score * 1.1
    score_copy[idx] = 100 if result > 100 else result
print("이전 평균 : {0}".format(sum(scores) / len(scores)))
print("이전 평균 : {0}".format(sum(score_copy) / len(score_copy)))

# 21 얕은 복사와 깊은 복사
'''
얕은 복사란, 객체 주소를 복사하는 것으로 객체 자체가 복사되지 않는다
위의 rb03와 rb01의 예를 참조
깊은 복사란, 객체 자체를 복사하는 것으로 또 하나의 객체가 만들어진다.
'''
class TemCls:
    def __init__(self, n, s):
        self.number = n
        self.str = s
    def print_cls_info(self):
        print(f"self number : {self.number}")
        print(f"self str : {self.str}")
        
tcl = TemCls(10, 'abcd')
#얕은 복사
tcl02 = tcl
tcl.print_cls_info()
tcl02.print_cls_info()
tcl02.number = 3.14
tcl02.str = 'bye'
#tcl까지 변한 것을 확인 할 수 있음 같은 객체를 갖고 있기 때문에 영향이 감

# 깊은 복사
import copy
tcl = TemCls(10, 'abcd')
tcl02 = copy.copy(tcl)
tcl.print_cls_info()
tcl02.print_cls_info()
#tcl과 tcl02가 다른 객체인 것을 확인 할 수 있음
#리스트 원본을 복사하는 방법
#얕은 복사
score_cop = score_ori
print(id(score_cop))
#for 문을 통한 복사
# extend 함수를 통해서 복사 -> 깊은 복사가 됨
# .copy를 통한 깊은 복사
'''
선수 원본의 점수를 이용해서 평균을 출력하고, 최고, 최저값을 제외한
평균을 출력하는 프로그램을 만들어보자
원본은 그냥 평균, 카피는 최고 최저점을 제외한 평균
'''
score_ori = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
score_cop = score_ori.copy()
ori_total = round(sum(score_ori), 2)
ori_avg = round(ori_total / len(score_ori), 2)
print("오리지날 합 : {0}\n오리지날 평균: {1}".format(ori_total, ori_avg))

#카피본 평균
#먼저 최고점 최저점을 날림
score_cop # 먼저 잘 카피 되었는지 확인
score_cop.sort() # 정렬
score_cop.pop(0) # 먼저 제일 낮은 점수 뺌
score_cop.pop() # 제일 높은 점수 뺌
score_cop # 잘 빼졌는지 확인
cop_total = round(sum(score_cop), 2)
cop_avg = round(cop_total / len(score_cop), 2)
print("카피 합 : {0}\n카피 평균: {1}".format(cop_total, cop_avg))

print("오리지날 합 : {0}, 카피 합: {1}\n오리지날 평균 : {2}, 카피 평균 : {3}\n오리지날 평균 - 카피 평균 : {4}".format(ori_total, cop_total, ori_avg, cop_avg, ori_avg - cop_avg))

# 22 클래스 상속
'''
다른 클래스를 상속해서 내 것 처럼 사용할 수 있다
class1이라는 최고 단계가 있고
class1을 상속한 class2가 있으면 2는 1의 기능을 사용할 수 있고, 추가가 가능하다
class2를 상속한 class3이 있으면 1,2 기능 모두 사용가능하고 추가가 가능하다
'''
class NormalCar:
    def drive(self):
        print("전진")
    def back(self):
        print("후진")
#상속을 할 때 부모 클래스를 안에다 넣어줌
class Turborcar(NormalCar):
    def turbo(self):
        print("터보기능 가속이 빨라집니다")
my_turbo_car = Turborcar()
my_turbo_car.turbo()
my_turbo_car.back()

'''
덧셈 뺄셈 기능이 있는 클래스를 만들고 이를 상속하는 클래스를 만들어서
곱셈 나눗셈을 추가
'''
#덧셈 뺄셈만 있는 부모클래스 생성
class CalSuper:

    def add(self, number01, number02):
        return number01 + number02
    def sub(self, number01, number02):
        return number01 - number02

class CalChild(CalSuper):
    def mul(self, number01, number02):
        return number01 * number02
    def div(self, number01, number02):
        return number01 / number02
cal_test01 = CalChild()
#부모 클래스의 덧셈 뺄셈 기능
cal_test01.add(18,20)
cal_test01.sub(18,20)
# 아들클래스인 CalChild의 곱셈 나눗셈 기능
cal_test01.mul(12,12)
cal_test01.div(12,12)

# 23 생성자 01
'''
생성자
객체가 생성될 때 생성자를 호출하면 __init__()가 자동으로 호출된다
__init__() 가 속성을 초기화한다
초기 값을 갖도록 하는 경우도 있다
처음에 self.변수 선언 할때 초기값을 넣어도 된다.

상위 클래스 속성을 초기화 하기 위해서 super() 이용한다
'''
class CalSuper:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02
        print("CalSuper __init__() called")
    def add(self, number01, number02):
        return number01 + number02
    def sub(self, number01, number02):
        return number01 - number02

class CalChild(CalSuper):
    def mul(self, number01, number02):
        return number01 * number02
    def div(self, number01, number02):
        return number01 / number02
cal_test01 = CalChild(10,20)
print(cal_test01.number01)
print(cal_test01.number02)
cal_test01.add(15, 30)
cal_test01.sub()

#super() 명령어 사용

class P_Class:
    def __init__(self, p_num01, p_num02):
        print("P_Class의 __init__()")
        self.p_num01 = p_num01
        self.p_num02 = p_num02
class C_Class(P_Class):
    def __init__(self, c_num01, c_num02):
        print("C_Class의 __init__()")
        #자동 호출 될 때 억지로 부모 클래스 init를 찾아서 c_num을 넣어줌
        #P_Class.__init__(self, c_num01, c_num02)
        #super()함수를 이용하는 방법
        #super().__init__(c_num01, c_num02)
        super(c_num01, c_num02)
        self.c_num01 = c_num01
        self.c_num02 = c_num02

# 24 생성자 02
'''
중간고사 클래스와 기말고사 클래스를 상속관계로 만들고 각각 점수를 초기화
또한 총점 및 평균을 반환하는 기능도 만들어보자

'''

class MidExam:
    def __init__(self, s1, s2, s3):
        print("MidExam __init__()")
        self.mid_kor = s1
        self.mid_eng = s2
        self.mid_mat = s3
    def print_scores(self):
        print("mid_kor : {0}".format(self.mid_kor))
        print("mid_eng : {0}".format(self.mid_eng))
        print("mid_mat : {0}".format(self.mid_mat))

class EndExam(MidExam):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        print("EndExam __init__()")
        super().__init__(s1, s2, s3)
        self.end_kor = s4
        self.end_eng = s5
        self.end_mat = s6
    def print_scores(self):
        super().print_scores()
        print("end_kor : {0}".format(self.end_kor))
        print("end_eng : {0}".format(self.end_eng))
        print("end_mat : {0}".format(self.end_mat))
        
    #총점 구하기
    def get_total(self):
        total = self.mid_kor + self.mid_eng + self.mid_mat
        total += self.end_kor + self.end_eng + self.end_mat
        return total
    # 평균 구하기
    def get_avg(self):
        return round((self.get_total() / 6), 2)
        
exam = EndExam(85, 90, 88, 75, 95, 100)
exam.print_scores()
exam.get_total()
exam.get_avg()




