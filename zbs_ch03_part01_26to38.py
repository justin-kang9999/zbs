# 26 리스트와 튜플
'''
리스트와 튜플의 차이점
튜플은 리스트와 달리 아이템 추가 변경 삭제가 불가하다
튜플은 선언시 괄호 생략이 가능하다
리스트와 튜플은 자료형 변환이 가능하다
'''
from sys import flags


students = '홍길동', '박찬호', '이용규', '강호동'
type(students)
students = list(students)
type(students)
students = tuple(students)
type(students)

'''
튜플을 이용한 점수표에서 최저 및 최고 점수를 삭제한 후 총점과 평균을 출력해보자

'''
player_score = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
player_score = list(player_score)
player_score.sort()
player_score
player_score.pop(0)
player_score.pop(len(player_score)- 1)
player_score

sum = 0
avg = 0
for score in player_score:
    sum += score

player_score = tuple(player_score)
sum = round(sum, 1)
avg = sum / len(player_score)
print("총점 : {0}\n평균 : {1}".format(sum, avg))

# 27 튜플 아이템 정렬
'''
튜플은 수정이 불가능 하기 때문에 정렬을 하려면 리스트로 변환 후 정렬을 하자
sorted() 함수를 이용하면 튜플도 정렬 할 수 있다.
sorted() 함수를 이용하면 리스트로 변환해서 정렬을 해주므로 다시 튜플화 하면 된다.
'''
students = '홍길동', '박찬호', '이용규', '강호동'
students = list(students)
students.sort()
students = tuple(students)
students
#반대로 정렬
students = list(students)
students.sort(reverse= True)
students = tuple(students)
students
# sorted()
students = '홍길동', '박찬호', '이용규', '강호동'
students = sorted(students)

tuple(students)
'''
실습 27강과 같음
튜플로 정의된 함수표에서 최저 및 최고 점수를 삭제한 후 총점과 평균을 출력해보자

'''
player_score = (9.5, 8.9, 9.2, 9.8, 8.8, 9.0)
player_score = sorted(player_score)
player_score
player_score.pop(0)
player_score.pop(len(player_score)- 1)
player_score

sum = 0
avg = 0
for score in player_score:
    sum += score

player_score = tuple(player_score)
sum = round(sum, 1)
avg = sum / len(player_score)
print("총점 : {0}\n평균 : {1}".format(sum, avg))

# 28 튜플과 for 문 01
'''
for 문을 이용하면 튜플의 아이템을 자동으로 참조할 수 있다.
'''
cars = '그랜저', '소나타', '말리부', '카니발', '소렌토'
for i in range(len(cars)):
    print(cars[i])
for car in cars:
    print(car)
    
'''
for 문을 이용하면 튜플의 아이템을 자동으로 참조할 수 있다.
튜플 내부에 또다른 튜플의 아이템을 조회할 수도 있다.
'''
students_cnt = (1,19), (2,20), (3,22), (4, 18), (5, 21)
for num, cnt in students_cnt:
    print("{0}학급의 학생 수 : {1}".format(num, cnt))
    
# 실습 학급별 학생수, 전체 학생 수, 평균 학생 수
sum = 0   
avg = 0
students_cnt = (1,19), (2,20), (3,22), (4, 18), (5, 21)
for num, cnt in students_cnt:
    print("{0}학급의 학생 수 : {1}".format(num, cnt))
    sum += cnt
print("전체 학생의 수 : {0}".format(sum))
print("학급당 평균 학생의 수 : {0}".format(sum / len(students_cnt)))

# 29 튜플과 for 문 02
'''
for문과 if문을 이용할 수 있다.
'''
min_score = 60
scores = (('국어', 58), ('영어', 77), ('수학', 89), 
          ('과학', 99), ('국사', 50))

for item in scores:
    if item[1] < min_score:
        print("과락 과목 : {0}\n점수: {1}".format(item[0],item[1]))
# 두개 뽑아서 하기
for subj, score in scores:
    if score < min_score:
        print("과락 과목 : {0}\n점수: {1}".format(subj, score))
# 실습
min_score = 60
kor, eng, mat, sci, his = map(int, input().split())
scores = (('국어', kor), ('영어', eng), ('수학', mat), 
          ('과학', sci), ('국사', his))
# contiunue문 활용
for subj, score in scores:
    if score >= min_score: continue
    print("과락 과목 : {0}\n점수: {1}".format(subj, score))
    
# 표와 튜플을 이용해서 학급 학생수가 가장 작은 학급과 가장 많은 학급을 출력해보자
students_cnt = (1,18), (2,19), (3,23), (4, 21), (5, 20), (6, 22), (7, 17)
class_cnt = []
for num, cnt in students_cnt:
    class_cnt.append(cnt)
min(class_cnt)
print("가장 적은 학급 : {}\n학생 수 : {}".format( class_cnt.index(min(class_cnt))+1, min(class_cnt)))
print("가장 많은 학급 : {}\n학생 수 : {}".format( class_cnt.index(max(class_cnt))+1, max(class_cnt)))

# 다른 방법
students_cnt = (1,18), (2,19), (3,23), (4, 21), (5, 20), (6, 22), (7, 17)
min_class_no, max_class_no, min_class_cnt, max_class_cnt = 0, 0, 0, 0

for num, cnt in students_cnt:
    if min_class_cnt == 0 or min_class_cnt > cnt:
        min_class_no = num
        min_class_cnt = cnt
    if max_class_cnt < cnt:
        max_class_no = num
        max_class_cnt = cnt

print("가장 적은 학급 : {}\n학생 수 : {}".format(min_class_no, min_class_cnt))
print("가장 많은 학급 : {}\n학생 수 : {}".format( max_class_no, max_class_cnt))

# 30 튜플과 while 문 01
'''
while 문을 이용한 조회
while 문을 이용하면 다양한 방법으로 아이템 조회가 가능하다
'''
cars = '그랜저', '소나타', '말리부', '카니발', '소렌토'
#1번 방법
n = 0
while n < len(cars):
    print(cars[n])
    n += 1
#2번 방법 flag = True를 이용한 방법
n = 0
flag = True
while flag:
    print(cars[n])
    n += 1
    if n == len(cars):
        flag = False
#3번 방법 while True와 브레이크를 사용하는 방법
n = 0

while True:
    print(cars[n])
    n += 1
    if n == len(cars):
        break

# 학급, 인원수 조회

students_cnt = (1,19), (2,20), (3,22), (4, 18), (5, 21)
n = 0
while True:
    print("{0}학급의 학생 수 : {1}".format(students_cnt[n][0], students_cnt[n][1]))
    n += 1
    if n == len(students_cnt):
        break

'''
실습 튜플을 이용해서 학급별 학생수와 전체 학생 수 
그리고 평균 학생수를 출력해보자

'''
students_cnt = (1,18), (2,19), (3,23), (4, 21), (5, 20), (6, 22), (7, 17)
sum = 0
avg = 0
n = 0
flag =True
while flag:
    class_no = students_cnt[n][0]
    cnt = students_cnt[n][1]
    print("{0}학급의 학생 수 : {1}".format(class_no, cnt))
    sum += cnt
    n +=1
    if n == len(students_cnt):
        flag = False
avg = sum / len(students_cnt)
print("총 학생 수 : {0}\n평균 학생 수 : {1}".format(sum, avg))

# 31 튜플과 while 문 02
'''
while문과 if문을 이용해서 과락과목 출력하기
'''

min_score = 60
scores = (('국어', 58), ('영어', 77), ('수학', 89), 
          ('과학', 99), ('국사', 50))
n = 0

while n < len(scores):
    if scores[n][1] < min_score:
        print("과락 과목 : {0}\n점수: {1}".format(scores[n][0],scores[n][1]))
    n += 1
    
n = 0

while n < len(scores):
    if scores[n][1] >= min_score:
        n += 1
        continue
    print("과락 과목 : {0}\n점수: {1}".format(scores[n][0],scores[n][1]))
    n += 1
    
min_score = 60
kor, eng, mat, sci, his = map(int, input().split())
scores = (('국어', kor), ('영어', eng), ('수학', mat), 
          ('과학', sci), ('국사', his))
n = 0 
while n < len(scores):
    if scores[n][1] < min_score:
        print("과락 과목 : {0}\n점수: {1}".format(scores[n][0],scores[n][1]))
    n += 1


# 실습
students_cnt = (1,18), (2,19), (3,23), (4, 21), (5, 20), (6, 22), (7, 17)
n = 0
min_class_no, max_class_no, min_class_cnt, max_class_cnt = 0, 0, 0, 0

while n < len(students_cnt):
        if min_class_cnt == 0 or min_class_cnt > students_cnt[n][1]:
            min_class_no = students_cnt[n][0]
            min_class_cnt = students_cnt[n][1]

        if max_class_cnt < students_cnt[n][1]:
            max_class_no = students_cnt[n][0]
            max_class_cnt = students_cnt[n][1]
        n += 1
print("가장 적은 학급 : {}\n학생 수 : {}".format(min_class_no, min_class_cnt))
print("가장 많은 학급 : {}\n학생 수 : {}".format( max_class_no, max_class_cnt))

# 32 딕셔너리
'''
딕셔너리는 키와 값을 이용해서 자료를 관리한다
{}를 이용해서 선언하고 키: 값 형태로 아이템을 정의한다
'''
# 선언하기
stu_dict = {'s1':'홍길동', 's2' : '박찬호', 's3' : '이용규', 
            's4' : '박승철', 's5' : '김지은'}
# 키:값 순이기 때문에 키 값을 기준으로 길이를 셈
len(stu_dict)
stu_dict.values()
stu_dict['s1']

'''
실습 나의 정보를 딕셔너리에 저장하고 출력해보자
'''
my_info = {'이름' : '박경진', '전공' : 'computer', 
           '메일' : 'jin@naver.com', '학년' : 3,
           '주소' : '대한민국 서울',
           '취미' : ['요리', '여행']}
print(my_info)

# 33 딕셔너리 조회
'''
딕셔너리 조회
딕셔너리 키를 이용해서 값을 조회한다
존재하지 않는 키를 이용한 조회시 에러가 발생한다
dict.get(key)를 이용해서 값을 조회할 수 있다
get()은 key가 없어도 에러가 발생하지 않는다
'''
stu_dict = {'s1':'홍길동', 's2' : '박찬호', 's3' : '이용규', 
            's4' : '박승철', 's5' : '김지은'}
stu_dict['s1']
stu_dict['s6']
stu_dict.get('s1')
stu_dict.get('s6')

my_info = {'이름' : '박경진', '전공' : 'computer', 
           '메일' : 'jin@naver.com', '학년' : 3,
           '주소' : '대한민국 서울',
           '취미' : ['요리', '여행']}
my_info['이름']
my_info['전공']
my_info['메일']
my_info['학년']
my_info['주소']
my_info['취미']
my_info.get('이름')
my_info.get('전공')
my_info.get('메일')
my_info.get('학년')
my_info.get('주소')
my_info.get('취미')

# 34 딕셔너리 추가
my_info = {}
my_info['이름'] = '박경진' 
my_info['전공'] = 'computer', 
my_info['메일'] = 'jin@naver.com', 
my_info['학년'] = 3,
my_info['주소']= '대한민국 서울',
my_info['취미'] = ['요리', '여행']
my_info

'''
추가하려는 키가 이미 있다면 기존 value가 변경된다.
실습 0~10까지 각각 정수에 대한 팩토리얼을 딕셔너리에 추가해보자
'''
# 팩토리얼을 위한 math 모듈 사용
import math
# 빈 dict 만듦
facto_dict = {}
# 키 값을 추가하기 위한 for문
for i in range(11):
    facto_dict[i] = math.factorial(i)
facto_dict

# 강의에서 알려준 방법 
facto_dict = {}
for i in range(11):
    if i == 0:
        facto_dict[i] = 1
    else:
        for j in range(1, (i+1)):
            facto_dict[i] = facto_dict[i-1] * j
facto_dict

# 35 딕셔너리 수정

'''
딕셔너리 수정은 
dict[key] = value 형태로 수정한다
'''
my_info = {}
my_info['이름'] = '박경진' 
my_info['전공'] = 'computer', 
my_info['메일'] = 'jin@naver.com'
my_info['학년'] = 3,
my_info['주소']= '대한민국 서울',
my_info['취미'] = ['요리', '여행']
#전공을 스포츠로,학년을 4학년으로 수정
my_info['전공'] = 'sports'
my_info['학년'] = 4
my_info

'''
시험 점수가 60점 미만이면 f(재시험)으로 값을 변경해보자.
'''
scores_dict = {'kor' : 88, 'eng' : 55, 'mat' : 85, 'sci' : 57, 'his' : 82}
min_score = 60
fstr = "F(재시험)"
if scores_dict['kor'] < min_score: 
    scores_dict['kor'] = fstr
if scores_dict['eng'] < min_score: 
    scores_dict['eng'] = fstr
if scores_dict['mat'] < min_score: 
    scores_dict['mat'] = fstr
if scores_dict['sci'] < min_score: 
    scores_dict['sci'] = fstr
if scores_dict['his'] < min_score: 
    scores_dict['his'] = fstr
scores_dict

'''
실습
하루에 몸무게와 신장이 각각 -0.3, 0.001씩 변한다고 할 때, 30일 후의
몸무게와 신장의 값을 저장하고 bmi 값도 출력하는 프로그램을 만들어보자
'''
my__body_info = {'이름' : '길동', '몸무게': 83,
                 '신장' : 1.8}
my_bmi = round(my__body_info['몸무게'] / (my__body_info['신장'] ** 2), 2)

# 30일 후까지 매일 변화를 확인하기 위해서 반복문을 활용함
#while문
date = 0
while True:
    date += 1
    my__body_info['몸무게'] = round((my__body_info['몸무게'] - 0.3), 2)
    my__body_info['신장'] = round((my__body_info['신장'] + 0.001), 4)
    print("몸무게 : {0}, 신장 : {1}\nbmi : {2}".format(my__body_info['몸무게'], my__body_info['신장'], my_bmi))
    if date >= 30:
        break
my_bmi
# 36 keys()와 values()
'''
key()를 통해 전체 key를 조회 가능
values()를 통해 전체 값을 조회 가능
items() 키값과 밸류값을 합쳐서 가져옴
리스트 안에 튜플값이 저장된 형태로 가져옴
'''
mem_info = {'이름' : '홍길동', '메일' : 'gildong@gmail.com',
            '학년' : 3, '취미' : ['농구', '게임']}
ks = mem_info.keys()
ks
vs = mem_info.values()
vs
its = mem_info.items()
its

'''
리스트로 변환하기
키, 값, 아이템 등 갖고온 값은 완벽한 리스트가 아니라 list()에 씌워줘야함
'''
ks = list(ks)
vs = list(vs)
its = list(its)

# for 문을 통한 조회
for idx , key in enumerate(ks):
    print(idx, key)
for idx, value in enumerate(vs):
    print(idx, value)
for idx, items in enumerate(its):
    print(idx, items)

for key in mem_info.keys():
    print("{} : {}".format(key, mem_info[key]))

'''
실습 학생의 시험 점수가 60 미만이면 재시험으로 값을 변경하는 코드를 
만들어보자
'''
scores_dict = {'kor' : 88, 'eng' : 55, 'mat' : 85, 'sci' : 57, 'his' : 82}
min_score = 60
fstr = "F(재시험)"
f_dict = {}
for key in scores_dict:
    if scores_dict[key] < min_score:
        scores_dict[key] = fstr
        f_dict[key] = fstr
print(scores_dict)
print(f_dict)

# 37 딕셔너리 삭제
'''
del과 key를 이용해서 딕셔너리의 아이템을 삭제할 수 있다. 
'''
# del을 이용한 삭제
mem_info = {'이름' : '홍길동', '메일' : 'gildong@gmail.com',
            '학년' : 3, '취미' : ['농구', '게임']}
# 메일 삭제
del mem_info['메일']
mem_info
#취미 삭제
del mem_info['취미']
mem_info

#pop()을 이용한 삭제 삭제된 값을 변수를 줘서 받을 수 있음
mem_info = {'이름' : '홍길동', '메일' : 'gildong@gmail.com',
            '학년' : 3, '취미' : ['농구', '게임']}
mem_info.pop('이름')
mem_info

# 실습 딕셔너리에 저장된 점수 중 최저 및 최고 점수를 삭제하는 프로그램을 만들어보기
min_score = 10 ; min_score_key = ''
max_score = 10 ; max_score_key = ''
scores_dict02 = {'score1':8.9, 'score2':8.1, 'score3':8.5,
                 'score4':9.8, 'score5':8.8}
for key in scores_dict02.keys():
    if scores_dict02[key] < min_score:
        min_score = scores_dict02[key]
        min_score_key = key
    if scores_dict02[key] > max_score:
        max_score = scores_dict02[key]
        max_score_key = key
del scores_dict02[min_score_key]
del scores_dict02[max_score_key]
scores_dict02

# 38 딕셔너리 유용한 기능
'''
in, len, clear
in
키 존재 유무 판단, True, False로 반환함
len
딕셔너리의 길이를 알 수 있다
clear
모든 아이템을 삭제한다
'''
#clear()
my_info = {'이름' : '홍길동', '나이' : 30, 
           '연락처' : '010-1234-4567', 
           '주민등록번호' : '990101-1234567',
           '주소' : '대한민국 서울'}
my_info.clear()
my_info
'''
실습
개인정보에 연락처와 주민등록번호가 있다면 삭제하는 코드를 짜보자
'''
del_items = ['연락처', '주민등록번호']
my_info = {'이름' : '홍길동', '나이' : 30, 
           '연락처' : '010-1234-4567', 
           '주민등록번호' : '990101-1234567',
           '주소' : '대한민국 서울'}
for item in del_items:
    if item in my_info:
        del my_info[item]


print(my_info)
