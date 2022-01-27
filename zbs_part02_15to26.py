# 15 format()함수
from numpy import mat


user_name = "홍길동"
user_age = 20
print("user name : {0}\nuser age : {1}".format(user_name, user_age))

print('내 이름은 {0}이고, 나이는 {1}살 입니다. {0}이름은 아버님께서 지어주셨습니다'.format(user_name,user_age))

'''
형식문자를 이용한 데이터 출력
%s -> 문자열
%d -> 정수
%f -> 실수
소수점 출력 자릿수 정하기
%.nf -> 소수점 n번째 자리까지 표현
'''
print('user name : %s' % user_name)
print("user name : %s\nuser age : %d" % (user_name, user_age))

print('pi : %f' %3.141592)
print('pi : %d' %3.141592)
print('pi : %.0f' %3.141592)
print('pi : %.1f' %3.141592)
print('pi : %.2f' %3.141592)
print('pi : %.3f' %3.141592)
print('pi : %.4f' %3.141592)
print('pi : %.6f' %3.141592)

'''
실행결과가 다음과 같이 출력 될 수 있도록
반지름 입력 :3
원주율 입력 : 3.141592
출력
radius :3.0
pi : 3.141592
radius: 3.000000, pi : 3.141592 #(둘다 6자리)
radius: 3.00, pi : 3.14 #(둘다 2자리)

그런 뒤에 원의 넓이와 둘레 길이를 출력해보자
'''
r_01 = float(input("반지름 입력 : "))
p_01 = float(input("원주율 입력 : "))

print("radius : %.1f\npi : %.6f" %(r_01,p_01))
print("radius : %.6f, pi : %.6f" %(r_01,p_01))
print("radius : %.2f, pi : %.2f" %(r_01,p_01))

#원 둘레와 넓이 구하기

rou = r_01 * 2 * p_01 
are = (r_01 ** 2) * p_01
print("원의 둘레 : %.2f\n원의 넓이 : %.2f" %(rou,are))

r_01 * r_01 * p_01

# 16 산술 연산자 (덧셈, 뺄셈)
'''
result = data1 + data2 일때 =과 +가 연산자
 
 = + - & / 등등 다 연산자
 산술 연산자
 할당 연산자
 비교 연산자
 논리 연산자가 존재
 
'''
# 덧셈 연산
#정수 실수 연산
num1 = 3.14
num2 = 0.12
print("num1 + num2 = %.2f" %(num1+num2))

#문자간에도 연산이 가능한데 덧셈이 가능하다
#숫자와 문자를 이용한 덧셈은 불가능하다

#국, 영, 수 점수를 입력하고 합계를 출력해보자

kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
mat = int(input("수학 점수 입력 : "))
total_score = kor + eng + mat
print("국어점수 : {0}\n영어점수 : {1}\n수학점수 : {2}\n합계\t : {3}".format(kor, eng, mat, total_score))

#뺄셈 연산자
#정수 실수 이용한 뺄셈
num1 = 3
num2 = 1
print("합계 : {0}".format(num1 + num2))
fnum1 = 3.14
fnum2 = 0.12
print("합계 : %.2f" %(fnum1 + fnum2))

# 17 산술연산자 (곱셈, 나눗셈)

#정수, 실수를 이용한 곱셈
num1 = 3
fnum1 = 3.14
print(num1 * fnum1)
#문자열을 이용한 곱셈
str01 = 'hi'
print("결과 : {0}".format(str01 * 7))

# 정수, 실수를 이용한 나눗셈
num1 = 10
num2 = 3
result = num1 / num2
print("결과값 : %.2f" % (result))

#문자열은 나눗셈 못함

#0을 나누는 경우 무조건 0만 결과값이 나옴
#0으로 나오는 경우 0으로 나눌 수 없다는 에러가 뜸

#나눗셈 연산자
'''
나눗셈의 결과는 항상 float로 나온다.
'''

#국, 영, 수 점수를 입력하고 합계 평균까지를 출력해보자

kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
mat = int(input("수학 점수 입력 : "))
total_score = kor + eng + mat
print("국어점수 : {0}\n영어점수 : {1}\n수학점수 : {2}\n합계\t : {3}\n평균: {4} ".format(kor, eng, mat, total_score, total_score/3))
print("평균 2째자리까지 : %.2f" %(total_score/3))

# 18 산술연산자 (나머지와 몫)
'''
/ 기호를 사용해 나눔
// 기호는 정수만 나옴
% 나머지를 구할 때
나머지와 몫을 한번에 구하려면 divmod() 함수를 사용
'''
num1 = 10
num2 = 3
result = num1 / num2
print("num1 : {0}, num2 : {1}\nresult : {2}".format(num1, num2, result))
#divmod 함수를 사용
result = divmod(num1, num2) #결과의 자료형은 튜플
print('결과 : {0}\n몫 : {1}\n나머지 : {2}'.format(result, result[0], result[1]))
'''
전체 학생수를 입력
한 모둠에 속하는 학생 수를 입력
전체 모둠 수와 남는 학생 수 출력
'''
all_stu =int(input("전체 학생 수를 입력 : "))
gro_stu =int(input("한 모둠당 학생 수를 입력 : "))
group_cnt = all_stu // gro_stu
over_stu = all_stu % gro_stu
print("전체학생수 : {0}\n한 모둠 학생 수 : {1}\n모둠 수 : {2}\n남은 학생 수 : {3}".format(all_stu, gro_stu, group_cnt, over_stu))

'''
123개의 사과를 4개씩 직원들한테 나눠 주려고 함.
최대로 나눠 줄 수 있는 직원수와 남는 사과 갯수 출력
'''
employee = 123
apple = 4
result = divmod(employee, apple)
print("사과를 나누어 줄 수 있는 최대 직원 수 : {0}\n남는 사과의 갯수 : {1}".format(result[0], result[1]))

# 19 산술연산자 (거듭제곱)
'''
같은 수를 여러번 곱한 값을 구하는 것
** 기호를 사용함 
2 ** 3이라면 2^3과 같음 2의 3제곱

pow() 함수를 이용해서 거듭제곱을 구할 수 있음
2 ** 3, math.pow(2,3) 두개 다 같은 결과를 냄

제곱근 구하기
n의 m제곱근 공식
n ** (1/m)
루트2를 구하고 싶다면
2 ** (1/2) 이런식으로 표현가능함
함수 중에 squrt() 함수가 제곱근을 구해줌
다만 2제곱근만 나타냄. 3루트나 4루트 같은 경우는 공식을 이용해야함
squrt() 함수를 이용해서 구할 수 있다
'''
num1 = 2
num2 = 3
result = num1 ** num2
print("제곱 결과 : {0}".format(result))

# 제곱근
#2의 제곱근 
result = num1 ** (1/2)
print("제곱근 결과 : %.3f" % (result))
#2의 3 제곱근
num1 = 2
num2 = 3
result = num1 ** (1/num2)
print("제곱근 결과 : %.3f" % (result))

#sqrt() 2제곱근만 나타냄. 3루트나 4루트 같은 경우는 공식을 이용해야함
import math
result = math.sqrt(2)
print("제곱근 결과 : %.3f" % (result))

#pow()
import math
result = math.pow(2,3)
print("제곱의 결과 : %.d" % (result))

'''
아들이 엄마한테 용돈을 받는 데 첫 달에는 200원을 받고 매월 이전달의 2배씩 인상
12개월 째 되는 달에는 얼마나 받을까?
'''
first_month = 200
after_12month = int((first_month * 0.01 )** 12 * 100)
print('12개월 후 용돈 :{}원'.format(after_12month))
#만약 돈 금액이 커서 3자리씩 콤마를 찍어서 편하게 보려면?
str_result = format(after_12month, ',')
print(str_result, '원')
print(type(str_result))

# 20 복합연산자
'''

= : 할당(대입 연산자)
예) abb = 10 # 오른쪽의 10이라는 값이 왼쪽에 있는 abb에 할당이 된다

복합 연산자
+= : 더하고 할당
-= : 빼고 할당
*= : 곱셈 후 할당
/= : 나눗셈 후 할당
%= : 나머지 연산 후 할당
//= : 몫 연산 후 할당
**= : 거듭제곱 연산 후 할당

'''
num1 = 10
num2 = 20
num1 += num2
print(num1)
'''
1월 강수량 30
2월 강수량 45
3월 강수량 47
4월 강수량 55
5월 강수량 65
6월 강수량 100
7월 강수량 128
8월 강수량 209
9월 강수량 204
10월 강수량 186
11월 강수량 67
12월 강수량 25

각 1월부터 12월까지 누적 강수량을 보여주고 연간 누적 강수량, 
연평균 강수량을 보여주기
'''
#반복문을 이용해서 내가 한 방법
rainfall = [30, 45, 47, 55, 65, 100, 128, 209, 204, 186, 67, 25]

sum_rainfall = 0
for i in range(len(rainfall)):
    sum_rainfall += rainfall[i]
    print("{0}월의 누적 강수량 : {1}".format(i+1, format(sum_rainfall, ',')))
print('_'*25)
print("연간 누적 강수량 : {0}\n연평균 강수량 : {1}".format(format(sum_rainfall, ','), sum_rainfall/len(rainfall)))
    
# 21 비교연산자 (숫자비교)
'''
비교 연산자기 때문에 True/False로 나온다
>, <, ==, >=, <= 등등 이런 것이 비교 연산자
!= : 같지 않다는 뜻
'''
#한줄에 연달아서 변수 선언하는 방법
num1, num2 = 10,5#또는
num1= 10; num2 = 5
#숫자 연산자
result = num1 > num2
print(result)
result = num1 >= num2
print(result)
result = num1 < num2
print(result)
result = num1 <= num2
print(result)
result = num1 == num2
print(result)
result = num1 != num2 #같지 않다
print(result)

'''
숫자 두개를 입력 한 후 비교 연산 결과를 출력하는 코드를 작성하자

'''
#내가 한 방법
# input_num01 = int(input("첫 번째 숫자를 입력 :"))
# input_num02 = int(input("두 번째 숫자를 입력 :"))
def betwn():
    input_num01 = int(input("첫 번째 숫자를 입력 :"))
    input_num02 = int(input("두 번째 숫자를 입력 :"))
    print("{0} > {1} : 결과 {2}\n{0} >= {1} : 결과 {3}".format(input_num01,input_num02,input_num01 > input_num02,input_num01 >= input_num02))
    print("{0} < {1} : 결과 {2}\n{0} <= {1} : 결과 {3}".format(input_num01,input_num02,input_num01 < input_num02,input_num01 <= input_num02))
    print("{0} == {1} : 결과 {2}\n{0} != {1} : 결과 {3}".format(input_num01,input_num02,input_num01 == input_num02,input_num01 != input_num02))
betwn()

'''
자동차 전장과 전폭을 입력하면 자동차 기계가 세차 가능 여부를 출력하는
코드를 작성해보자
최대 전장 길이: 5200mm, 최대 전폭길이 :1985mm
'''
#함수 만들어서 구현하기
def wash_car():
    
    max_len =5200
    max_wid = 1985
    my_len = int(input(" 전장 길이를 mm단위로 입력해주세요 : "))
    my_wid = int(input(" 전폭 길이를 mm단위로 입력해주세요 : "))
    btw_len = max_len >= my_len
    btw_wid = max_wid >= my_wid
    if btw_len == True and btw_wid == True:
        able = "사용 가능"
        result = print("전장 가능 여부 : {0}\n전폭 가능 여부 : {1}\n사용 가능 여부 : {2}".format(btw_len, btw_wid, able))
    else:
        cannot = "사용 불가능"
        result = print("전장 가능 여부 : {0}\n전폭 가능 여부 : {1}\n사용 가능 여부 : {2}".format(btw_len, btw_wid, cannot))
    return result

wash_car()

# 22 비교연산자 (문자비교)
'''
문자 비교 : 아스키 코드를 이용한 비교연산
예시) 문자 A는 십진법으로 65, 문자 S는 십진법으로 83
이렇게 숫자를 비교하는 것
'''
char01 = 'A'
char02 = 'S'
print("{0} > {1} : 결과 {2}".format(char01,char02, (char01 > char02)))
#십진수로 변환하여 나오게 하려면
print("{0} > {1} : 결과 {2}".format(ord(char01),ord(char02), (char01 > char02)))

#문자열 비교: 문자열 자체가 같은지 다른지 비교 ==와 !=만 사용가능
str01 = 'Hello'
str02 = 'hello'
print("{0} == {1} : 결과 {2}".format(str01, str02, str01 == str02))
print("{0} != {1} : 결과 {2}".format(str01, str02, str01 != str02))

#알파벳을 입력하면 아스키 코드를 출력하는 코드를 작성하자
user_alphabet = input('알파벳을 입력해 주세요: ')
print('{0}은/는 아스키 코드로는 {1}입니다'.format(user_alphabet, ord(user_alphabet)))
#아스키코드를 입력하면 문자를 출력하는 코드를 작성하자
user_ascii = int(input('아스키 코드를 입력해 주세요: '))
print('아스키 코드 {0}은/는 문자로는 "{1}"입니다'.format(user_ascii, chr(user_ascii)))

'''
아이디와 패스워드를 입력한 후 비교 결과를 출력해보자
'''
sys_id = "admin@gmail.com"
sys_pw = "!q2W3e$R"
user_id = input("메일주소를 입력해 주세요 : ")
user_pw = input("비밀번호를 입력해 주세요 : ")
print("아이디 비교 결과 : {0}".format(sys_id == user_id))
print("비밀번호 비교 결과 : {0}".format(sys_pw == user_pw))
if (sys_id == user_id) == True and (sys_id == user_id) == True:
    print("로그인이 되었습니다.")
else:
    print("아이디나 비밀번호가 틀립니다")

# 23 논리연산자
'''
and or not 3개
and 모두가 True인 경우에만 T
or 둘 중 하나만 True에도 T
not 반대로 출력 
not 예시) True였다면 False를 출력, False라면 True를 출력

'''

#and
print("{0} and {1} : {2}".format(True, True, (True and True)))
print("{0} and {1} : {2}".format(True, False, (True and False)))
#or
print("{0} or {1} : {2}".format(True, True, (True or True)))
print("{0} or {1} : {2}".format(True, False, (False and False)))

#not 
print("not {0} : {1}".format(True, (not True)))
print("not {0} : {1}".format(False, (not False)))

'''
백신 접종 대상자는 20세 미만 또는 65세 이상자에 한합니다를 
논리 연산자를 이용해서 코딩해보자
'''
def vacc_age():
    age = int(input("만나이를 숫자만 입력해주세요: "))
    vaccine = (age < 20) or (age >= 65)
    if vaccine == True:
        result = print("백신 접종 대상자입니다")
    else:
        result = print("백신 접종 대상자가 아닙니다")
    return result

vacc_age()

'''
국, 영, 수 점수를 입력하고 평균이 70점 이상이면 True를 출력하는 코드를 작성해보자
단 과목별 점수가 최소 60점인 경우에 True를 출력한다
'''
def pf_score():
    kor_score = int(input("국어 점수를 숫자만 입력해 주세요: "))
    eng_score = int(input("영어 점수를 숫자만 입력해 주세요: "))
    mat_score = int(input("수학 점수를 숫자만 입력해 주세요: "))
    avg_score = (kor_score + eng_score + mat_score) / 3
    pf_kor = (kor_score >=60)
    pf_eng = (eng_score >=60)
    pf_mat = (mat_score >=60)
    pf_avg = (avg_score >= 70)
    print("국어점수 :{0}, 통과 결과 {1}".format(kor_score, pf_kor))
    print("영어점수 :{0}, 통과 결과 {1}".format(eng_score,pf_eng))
    print("수학점수 :{0}, 통과 결과 {1}".format(mat_score,(mat_score >=60)))
    print("평균 점수 : {0}, 통과 결과 : {1}".format(avg_score, pf_avg))
    print("과락 결과 : {0}\n최종 결과 : {1}".format(all([pf_kor, pf_eng, pf_mat]), all([pf_kor, pf_eng, pf_mat, pf_avg]) ))

pf_score()

# 24 operator 모듈
'''
누군가가 이미 구현해 놓은 기능들
import 모듈이름 을 통해 가져와서 사용 가능함
'''
'''
operator 모듈을 통해서 전에 만들었던 백신 접종 대상을 코딩해보자
'''
import operator
def vacc_age():
    age = int(input("만나이를 숫자만 입력해주세요: "))
    vaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65)) 
    if operator.eq(vaccine, True):
        result = print("백신 접종 대상자입니다")
    else:
        result = print("백신 접종 대상자가 아닙니다")
    return result

vacc_age()

'''
random과 operator 모듈을 사용해서 10부터 100 사이 난수 중 십의 자리와
일의 자리가 각각 3의 배수인지 판단하는 코드를 작성해보자
'''
import random
import operator
rand_int = random.randint(10,100)
num10 = operator.floordiv(rand_int , 10) #몫만 가져오는 함수
num1 = operator.mod(rand_int , 10) #나머지 구하는 함수
print("난수 : {0}".format(rand_int))
print("십의 자리 : {0}".format(num10))
print("십의 자리 : {0}".format(num1))
print("십의 자리는 3의 배수이다. : {0}" .format(operator.mod(num10, 3) == 0))
print("일의 자리는 3의 배수이다. : {0}" .format(operator.mod(num1, 3) == 0))

# 25 조건식
'''
어떤 조건에 따라 실행이 분기점이 되는 식
a if 조건 else b 이런식으로도 가능
if a 조건:
     실행할 코드
else: 
    b 실행
    

'''

#적설량을 입력하고 적설량이 300mm 이상이면 대설경보, 그렇지 않으면 대설경보 해제
def alt_snow():
    snowfall = int(input("현재 적설량을 mm단위로 적어주세요 :"))
    limit_snow = 300
    if snowfall >= limit_snow:
        result = print("적설량 : {0}\n{1}".format(snowfall, "대설경보 발령"))
    else:
        result = print("적설량 : {0}\n{1}".format(snowfall, "대설경보 해제"))
    return result
alt_snow()

'''
국영수 점수를 입력하면 조건식을 이용해 과목별 결과와 전체 결과를 출력하는 
코드작성

'''
kor_score = int(input("국어 점수를 숫자만 입력해 주세요: "))
eng_score = int(input("영어 점수를 숫자만 입력해 주세요: "))
mat_score = int(input("수학 점수를 숫자만 입력해 주세요: "))
total_score = (kor_score + eng_score + mat_score)
avg_score = (kor_score + eng_score + mat_score) / 3
print(('국어:pass') if kor_score >= 60 else print("국어:fail"))
print(('영어:pass') if eng_score >= 60 else print("영어:fail"))
print(('수학:pass') if mat_score >= 60 else print("수학:fail"))
print("총점 : %d\n평균 : %.2f" %(total_score, avg_score))

# 26 조건식 (if문)
'''
if문 단일조건
if else 양자택일
if elif 다자택일
들여쓰기가 중요
'''

#국영수 점수 입력, 평균 90이상이면 칭찬을 출력하는 코드
kor_score = int(input("국어 점수를 숫자만 입력해 주세요: "))
eng_score = int(input("영어 점수를 숫자만 입력해 주세요: "))
mat_score = int(input("수학 점수를 숫자만 입력해 주세요: "))
total_score = (kor_score + eng_score + mat_score)
avg_score = (kor_score + eng_score + mat_score) / 3
print('평균 : {0}'.format(avg_score))
if avg_score >= 90:
    print('참 잘했어요')
    
# 실내온도 입력 온도가 28 이상이면 냉방 작동 출력, 20 이하면 난방 작동

high_tem = 28
low_tem = 20 
input_tem = int(input('현재 실내 온도를 적어주세요 : '))

if input_tem >= high_tem:
    print("냉방 작동")
if input_tem <= low_tem:
    print("난방 작동")
    













