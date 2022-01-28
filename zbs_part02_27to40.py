# 27 양자택일 조건문 (if~else문)
'''
if ~ else 문 : 조건식 결과에 따라 둘 중 하나가 실행됨

'''

from tkinter import N


pass_score = 80
my_score = int(input("점수 입력 : "))
if my_score >= pass_score :
    print("패스")
else:
    print("페일")
    
'''
pass 키워드
아직 조건문에서 실행할 코드를 작성을 못했을 때 pass를 쓰면 넘어감
에러가 발생하지 않음
 
'''
#나이가 65세 이상이면 교통요금 무료를 적용하는 프로그램

senior_age = 65
pass_age = int(input("만나이 입력 : "))
if pass_age >= senior_age:
    print("무료 대상 승객입니다.")
else:
    print("유료 대상 승객입니다.")

#소수점 첫번째 자리에서 반올림하는 프로그램
float_num = float(input("소수를 입력 : "))
if float_num - int(float_num) >= 0.5:
    print("올림 : {}".format(int(float_num + 1)))
else:
    print("버림 : {}".format(int(float_num)))

# 28 if ~ else문과 조건식
'''
조건식 결과에 따른 실행만 하는 경우
A if action else B -> action이 참이면 A 실행 아니면 B실행

조건식 결과를 변수에 할당하는 경우
result = '가능' if user_point >= min_able_point else '불가능'
print( '포인트 사용 가능 여부 : {}'.format(result))

조건식 vs if ~ else 문
조건식 if ~ else문: 모든 조건식(삼항연산자)은 if ~ else 문으로 변경할 수 있다
반대로 모든 if ~else 문이 조건식으로 변경할 수 있는 것은 아니다
실행문이 간단해야 조건식으로 바꿀 수 있음
'''
user_point = 10
min_able_point = 100
result = '가능' if user_point >= min_able_point else '불가능'
print(result)
if user_point >= min_able_point:
    print("포인트 사용 가능")
else: 
    print("포인트 사용 불가능")
'''
비올 확률 입력 55% 이상이면 우산 챙기세요 그렇지 않으면 양산을 챙기세요
조건식이랑 if-else 문으로 둘 다 작성해보자
'''
rain_per = int(input(" 비올 확률을 숫자만 입력해주세요 : "))
min_rain_per = 55
#조건식
print("우산 챙기세요") if rain_per >= min_rain_per else print("양산 챙기세요")

#if~else문
if rain_per >= min_rain_per:
    print("우산 챙기세요")
else:
    print("양산 챙기세요")

'''
실습
다음 요구사항을 해결하기 위해서 조건식과 if~else 문 중 알맞은 구문을
사용해보자
요구사항
1. 최저기온 입력
2. 최고기온 입력
3. 일교차가 11이상인 경우 출력내용
일교차: n도
'감기조심하세요'
4. 일교차가 11도 미만인 경우 출력내용
일교차: n도
'산책하기 좋은 날씨입니다 

'''
low_tem = int(input('최저기온 입력 : '))
high_tem = int(input('최고기온 입력 : '))
hig_low_refer = 11
#if else 문을 활용
if high_tem - low_tem >= hig_low_refer:
    print("일교차 : {0}도\n감기 조심 하세요.".format(high_tem - low_tem))
else:
    print("일교차 : {0}도\n산책하기 좋은 날씨네요.".format(high_tem - low_tem))

# 29 다자택일
'''
if elif문 여러가지 조건식 결과에 따라 실행문이 결정됨

'''
exam_score = int(input("시험점수 입력 : "))
grades = ''
if exam_score >= 90:
    grades = 'A'
elif exam_score >= 80:
    grades = 'B'
elif exam_score >= 70:
    grades = 'C'
elif exam_score >= 60:
    grades = 'D'
else:
    grades = 'F'

print("성적 : {0}\t학점 : {1}".format(exam_score, grades))


"계절을 입력하면 영어로 번역되는 프로그램을 입력해보자"
print("계절 : 봄, 여름, 가을, 겨울")
season_eng = {'봄':'spring', '여름':'summer', '가을': 'fall', '겨울':'winter'}
season_kor = input("계절 입력 : ")
if season_kor in season_eng.keys():
        print(season_eng[season_kor])
        
'''
키오스크에서 메뉴를 선택하면 영수증이 출력되는 프로그렘

'''
print('1.카페라떼(3.5)\n2.에스프레소(2.5)\n3.아메리카노(3.0)\n4.곡물라떼(4.0)\n5.밀크티(4.3)')
choose_menu = int(input("메뉴선택 번호를 입력해주세요: "))
if choose_menu == 1:
    print('-------------------------------')
    print('메뉴 : 카페라떼\n가격 : 3,500원')
    print('-------------------------------')
elif choose_menu == 2:
    print('-------------------------------')
    print('메뉴 : 에스프레소\n가격 : 2,500원')
    print('-------------------------------')
elif choose_menu == 3:
    print('-------------------------------')
    print('메뉴 : 아메리카노\n가격 : 3,000원')
    print('-------------------------------')
elif choose_menu == 4:
    print('-------------------------------')
    print('메뉴 : 곡물라떼\n가격 : 4,000원')
    print('-------------------------------')
elif choose_menu == 5:
    print('-------------------------------')
    print('메뉴 : 밀크티\n가격 : 4,300원')
    print('-------------------------------')

# 30 다자택일 조건문 사용시 주의할 점
'''
- 조건식 순서가 중요하다
점수같은 경우 내림차순 순으로
만약 순서가 바뀌면 a를 받지 못함
- 조건의 범위를 명시한다

순서가 바뀌더라도 범위가 확실하다면 효율적이지는 않겠지만 잘 찾아낸다

'''
'''
실습 자동차 배기량에 따라 세금을 부과한다고 할 때 다음 표를 보고,
배기량을 입력하면 세금이 출력되는 프로그램을 만들어보자

'''
car_d = int(input("배기량을 숫자로만 입력해주세요 : "))
if car_d < 1000:
    print('세금 : 100,000원')
elif car_d < 2000 and car_d >= 1000:
        print('세금 : 200,000원')
elif car_d < 3000 and car_d >= 2000:
        print('세금 : 300,000원')
elif car_d < 4000 and car_d >= 3000:
        print('세금 : 400,000원')
elif car_d < 5000 and car_d >= 4000:
        print('세금 : 500,000원')
elif car_d >= 5000:
        print('세금 : 600,000원')
        
# 31 중첩 조건문
'''
조건문 안에는 또다른 조건문이 있을 수 있다.
'''

exam_score = int(input("시험점수 입력 : "))
grades = ''
if exam_score < 60:
    print('재시험 대상입니다')
else:
    if exam_score >= 90:
        grades ='A'
    elif exam_score >= 80:
        grades = 'B'
    elif exam_score >= 70:
        grades = 'C'
    elif exam_score >= 60:
        grades = 'D'
print(grades)

'''
출퇴근시 이용하는 교통수단에 따라 세금을 감면해주는 정책을 세우려고한다
의사코드
출퇴근 대상인가?
출퇴근 대상자라면
도보, 자전거 -> 세금 감면 5%
버스, 지하철 세금감면 3%
자가용 -> 추가 세금 1%
출퇴근 대상자가 아니면
세금 감면 대상자가 아닙니다

'''
sel_num = int(input("출퇴근 대상자인가요? 1.Yes\t 2.No "))
if sel_num ==1:
    print('교통 수단을 다음 중에서 선택하세요')
    trans = int(input("1.도보,자전거\n 2.버스, 지하철\n3. 자가용 "))
    if trans == 1:
        print('세금감면 5%')
    if trans == 2:
        print('세금감면 3%')
    if trans == 3:
        print('추가세금 1%')
else:
    print('잘못 입력했습니다')   

# 32 반복문   

'''
반복문은 특정 실행을 반복하는 것
반복문을 사용하면 프로그래밍이 간결하고 유지보수가 쉽다
대량으로 메일/ 문자발송, 인사말 반복, 음원 반복 재생
구구단 출력, 팩토리얼, 기상 알람, 영단어 반복 학습 도구
게임 반복 실행, 타이머 등등등에 사용됨

반복문 종류
횟수에 의한 반복
for문
조건에 의한 반복
while 문
'''

# 33 횟수에 의한 반복 for 문
'''
for ~ in 키워드 반복횟수(반복 범위):
    실행문
    
'''
#Hello python을 5번 출력하는 코드를 작성하자
for i in range(5):
    print("Hello python")    
    
#사용자가 입력한 숫자에 맞는 구구단을 출력하는 코드를 작성하자
gugu = int(input("몇 단의 구구단을 보고싶나요? 숫자로만 입력해주세요 : "))
for i in range(9):
    result = gugu * (i + 1)
    print("{0} * {1} = {2}".format(gugu, (i + 1), result))
    
# 34 반복범위 설정 range() 함수

'''
range() 기본 사용 방법
for i in range(시작숫자, 끝숫자, 단계):
시작숫자부터 끝숫자-1까지 단계만큼 증가하면서
예) for i in range(1, 10): 이라면 1부터 9까지를 뜻함
예) for i in range(1, 10, 2): 이라면 1부터 9까지 2씩 증가하면서 진행
출력결과 -> 1,3,5,7,9
예) for i in range(10, 1, -1): 10부터 0까지 1씩 빼가면서 진행
매개변수 생략
for i in range(11): 0~10까지, 시작이 0이면 생략이 가능하다.
'''
for i in range(10, 1, -1):
    print(i)
#반복 시작과 끝을 입력하면 1씩 증가하는 반복문
start_num = int(input("반복 시작 숫자 입력 : "))
end_num = int(input("반복 끝 숫자 입력 : "))
for i in range(start_num, end_num):
    print(i)
#반복 시작과 끝을 입력하면 2씩 증가하는 반복문
for i in range(start_num, end_num, 2):
    print(i)
# 1부터 100까지 3의 배수인 정수만 출력하는 코드 작성
for i in range (1, 101):
    if i % 3 == 0:
        print(i)
list03 = []
for i in range (1, 101):
    if i % 3 == 0:
        list03.append(i)
print(list03)

# 35 조건에 의한 반복문 while문
'''
조건에 만족하면 반복이 실행됨. 그렇지 않으면 중단함
주로 while문이 사용됨
while n <= end_num: => n <= end_num 이것은 조건식
    print(n)
    n += 1
밑에 print(n)과 n+=1은 실행문
'''
n = 0
while n <= end_num:
    print(n)
    n += 1
    
n = 1
while n < 10:
    result = 7 *n
    print('{0} * {1} = {2}'.format(7,n,result))
    n += 1

'''
while 문 사용 방법
pass 사용
while n> 10:
    pass => 나중에 코딩하겠다
'''
'''
while문을 사용하자
1~100까지 정수 중 2의 배수와 3의 배수를 구분해서 출력하자
'''
n = 1
while n < 101:
    if n % 2 == 0:
        print('{0}은 2의 배수이다'.format(n))
    if n % 3 == 0:
        print('{0}은 3의 배수이다'.format(n))
    n += 1
    
# while 문을 이용해서 사용자가 이용한 구구단을 입력하자
gugu = int(input("몇 단의 구구단을 보고싶나요? 숫자로만 입력해주세요 : "))
n = 1
while n < 10:
    result = gugu * n
    print('{0} * {1} = {2}'.format(gugu,n,result))
    n += 1
    
# 36 for문과 while문 비교
'''
for문이 적합한 경우
횟수에 의한 반복이면 for문이 더 적합
while문이 적합한 경우
조건에 의한 반복이라면 while문이 for문보다 적합하다.
'''

# 7의 배수의 합이 50이상이 최초의 정수 출력 for문을 이용
sum = 0
max_int = 0
for i in range(1, 101):
    if i % 7 == 0 and sum <= 50:
        sum += i
        max_int = i
    print("i : {}".format(i))
print("7의 배수의 합이 50이상이 최초의 정수 : {0}".format(max_int))

# 7의 배수의 합이 50이상이 최초의 정수 출력 while문을 이용- > 더 불편
n = 1
while n < 101:
    if n % 7 == 0 and sum <= 50:
        sum += n
        max_int = n
    print("i : {}".format(i))
    break
print("7의 배수의 합이 50이상이 최초의 정수 : {0}".format(max_int))

'''
자동차 바퀴가 한번 구를 때마다 0.15mm씩 마모가 된다고 한다.
현재 바퀴 두깨가 30mm이고 최소 운행 가능 바퀴 두께가 20mm라고 할 때
앞으로 구를 수 있는 횟수
'''
current_thick = 30
rotation_cnt = 0
remove_thick = 0.15

while current_thick >= 20:
    rotation_cnt += 1
    current_thick -= remove_thick
    safe_ratation_cnt = rotation_cnt - 1
print("운행 가능 횟수 : {}".format(safe_ratation_cnt))

# 37 무한루프
'''
무한 반복 실행
반복문을 빠져나올 수 없는 경우를 무한루프
while문에서 조건식의 결과가 항상 True인 경우 무한반복이 됨
논리형 데이터를 사용해서 무한 반복을 실행할 수 있다.
'''
flag = True
num = 0
sum = 0
while flag:
    num += 1
    sum += num
    print("{0}까지의 합은 {1}입니다.".format(num, sum))
    if sum >= 100:
        flag = False
'''
# 하루 독감으로 병원에 내방하는 환자수가 50명에서 100명 사이일 때,
누적 독감 환자수가 최소 10,000명을 넘는 날짜를 구해보자
'''
import random
sum = 0
date = 1
flag = True

while flag:
    patient_cnt = random.randint(50, 100)
    sum += patient_cnt
    date += 1
    print("{0}일차\t 오늘 내방 환자 수 : {1}\t 누적 환자수 : {2}".format(date, patient_cnt, sum))
    
    if sum >= 10000:
        flag = False
        
# 38 반복문 제어 continue
'''
continue
반복 실행 중 continue를 만나면 실행을 생략하고 다음 반복실행문으로 넘어간다
'''
# 7의 배수만 뽑기
for i in range(100):
    # 7의 배수가 아니면 생략
    if i % 7 != 0:
        continue
    # 7의 배수면 출력
    print("{0}은(는) 7의 배수입니다".format(i))

'''
else
실행문은 반복문이 종료된 후 실행된다
'''
#7의 배수 갯수만 구할 때
cnt = 0
for i in range(100):
    # 7의 배수가 아니면 생략
    if i % 7 != 0:
        continue
    # 7의 배수면 출력
    print("{0}은(는) 7의 배수입니다".format(i))
    cnt +=1
else:
    print('99까지 정수 중 7의 배수는 {0}개'.format(cnt))

'''
1부터 100까지 3과 7의 공배수와 최소공배수를 구해보자
'''
min_num = 0
for i in range(1, 101):
    if i % 3 != 0 or i % 7 != 0:
        continue
    
    print("공배수 : {0}".format(i))
    
    if min_num == 0:
        min_num = i
else:
    print("최소공배수 : {0}".format(min_num))
    
# 39 반복문 제어 break
'''
반복 실행 중 break를 만나면 반복문을 빠져나온다

'''
num = 0
while True:
    print("Hello World")
    num += 1
    if num >= 5:
        break

# 1부터 100까지 정수를 더할 때 합계가 100이 넘는 최초의 정수

sum = 0
search_num = 0
for i in range(100):
    sum += i
    if sum > 100:
        search_num = i
        break
print("search_num : {0}".format(search_num))

# 10!을 계산하는 과정에서 결과값이 50을 넘었을 때 숫자를 구하자
result = 1
num = 0
for i in range(1, 11):
    result *= i
    
    if result > 50:
        num = i
        break
print("num : {0}, result : {1}".format(num, result))

'''
새끼 강아지 체중이 2.2kg가 넘으면 이유식을 중단하려고 한다.
하루한번 이유식을 먹을 때 체중이 0.07 kg만큼 증가한다고 할 때
이유식 중단을 하려면 몇 번째 날인지 구하자 
현재 0.8kg
'''
#g으로 바꿔서 계산
limit_weight = 2200
current_weight = 800
date = 1
while True:
    date += 1
    current_weight += 70
    if current_weight >= limit_weight:
        break
    
print("{0}번째 날에 이유식을 그만줘도 됩니다".format(date))

# 40 중첩 반복문

'''
반복문 안에 반복문을 선언
'''
#별이 하나씩 늘어나는 코드 작성
for i in range(1,10):
    for j in range(i):
        print("*", end = " ")
    print()

# 반대로 별이 많았다가 적어지도록 코드를 작성해보자
for i in range(10,0, -1):
    for j in range(i):
        print("*", end = " ")
    print()

#구구단 전체를 출력해보자
for i in range(1,10):
    for j in range(2, 10):
        result = i *j
        print("{0} * {1} = {2}\t".format(j, i, result), end =" ")