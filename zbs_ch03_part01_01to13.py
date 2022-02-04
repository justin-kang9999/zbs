# 01 자료구조란?
'''
컨테이너 자료형과 자료구조를 거의 같은 말로 씀
여러 개의 데이터가 묶여있는 자료형을 컨테이너 자료형이라 하고,
이러한 컨테이너 자료형의 데이터 구조를 자료구조라고 한다.
자료구조는 각각의 컨테이너 자료형에 따라 차이가 있으며, 파이썬의 대표적인
컨테이너 자료형으로는 리스트 튜플 딕셔너리 셋이 있다.
튜플은 수정이 불가능, 딕셔너리는 키와 밸류값으로 나뉘어져 있음
셋은 집합으로 중복이 불가능하다.

'''
#리스트
from asyncio import start_unix_server
from email import message
import enum
import numbers


students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
#튜플
jobs = ('의사', '속기사', '전기기사','감정평가사','회계사')
#dict
scores = {"kor" : 88, 'eng': 91, 'mat' : 95, 'sci' : 90, 'his' : 100}

# 02 리스트
'''
배열과 같이 여러 개의 데이터를 나열한 구조
[]를 이용해서 선언하고 데이터 구분은 ,를 이용한다
숫자, 문자 논리형 등 모든 데이터를 같이 저장할 수 있다
리스트에 또 다른 컨테이너 자료형 데이터를 저장할 수도 있다.
리스트 안에 요소가 아이템이라고 함
'''
#리스트
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
#실습 가족 이름을 리스트에 저장하고 출력
family_names = ['홍아빠', '홍엄마', ' 홍길동', '홍동생']
print(family_names)

#오늘 일정을 리스트에 저장하고 출력해보자
today_schedule = ['10시- 업무회의', '12시- 친구와 점심약속',
                  '3시 - 자료정리', '6시 - 운동', '9시 - tv시청']
print(today_schedule)

# 03 리스트 아이템 조회
'''
인덱스란 아이템에 자동으로 부여가 되는 번호표 
리스트 아이템은 인덱스를 이용해서 조회 가능하다
'''
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
for i in range(len(students)):
    print(students[i])
'''
5명의 학생 이름을 리스트에 저장하고 인덱스가 홀수인 짝생과
짝수(0도 포함)인 학생을 구분해서 인덱스와 학생 이름을 출력해보자
'''
students = ['박경수', '박찬호', '이용규', '유승철', '안우진']
for i in range(len(students)):
    if i % 2 == 0:
        print("인덱스가 짝수인 학생 : {0}번 {1}".format(i, students[i]))
    else:
        print("인덱스가 홀수인 학생 : {0}번 {1}".format(i, students[i]))
        
# 04 리스트 길이
'''
리스트의 길이란 리스트에 저장된 아이템의 갯수
len과 같은 함수는 레퍼런스 함수
len과 반복문을 이용하면 리스트의 아이템 조회가 가능
len 함수는 리스트의 갯수 뿐만 아니라 문자열의 길이도 알 수 있다.
'''
students = ['박경수', '박찬호', '이용규', '유승철', '안우진']
len(students)
#for 문을 이용한 방법
for i in range(len(students)):
    print("{0}번 : {1}".format(i , students[i]))
# while문을 이용한 조회 방법
n = 0
while n < len(students):
    print("{0}번 : {1}".format(n , students[n]))
    n += 1
# 문자열 길이 확인하기
len("hello Python")

# 좋아하는 운동 종목을 리스트에 저장하고 반복문을 이용해서 출력해보자
fav_sports = ['수영', '배구', '야구', '조깅']
for i in range(len(fav_sports)):
    print("{0}. {1}".format(i, fav_sports[i]))
# 내용만 뽑아서 조회하고 싶을 때
for item in fav_sports:
    print(item)


# 05 리스트와 for문 01
'''
for문을 이용하면 리스트의 아이템을 자동으로 참조할 수 있다.
'''
cars = ['그랜저', '소나타', 'gv60', '320d', '쏘렌토']
for i in range(len(cars)):
    print(cars[i])
for item in cars:
    print(item)
'''
for문을 이용하면 리스트의 아이템을 자동으로 참조할 수 있다
리스트 내부의 또다른 리스트의 아이템을 조회할 수도 있다
'''
# 리스트 내부의 리스트 조회
students_cnt = [[1,19], [2, 20], [3, 22], [4, 18], [5, 21]]
for class_no, cnt in students_cnt:
    print("{0}반의 학생 수 : {1}".format(class_no, cnt))
'''
학급별 학생 수와 전체 학생 수 그리고 평균 학생수를 출력해보자
'''
students_cnt = [[1,18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
sum_students = 0
avg_students = 0
for class_no, cnt in students_cnt:
    print("{0}반의 학생 수 : {1}".format(class_no, cnt))
    sum_students += cnt
    
print("전체 학생의 수 : {0}".format(sum_students))  
print("평균 학생의 수 : {0}".format(sum_students/ len(students_cnt)))  

# 06 리스트와 for문 02
'''
for문과 if문을 이용해서 과락 과목 출력하기
'''
min_score = 60
scores = [['국어', 58], ['영어', 77], ['수학', 89], ['과학', 99], ['국사', 50]]
for item in scores:
    if item[1] < min_score:
        print("과락 과목: {}, 점수 : {}".format(item[0], item[1]))
# 다른 방법
min_score = 60
scores = [['국어', 58], ['영어', 77], ['수학', 89], ['과학', 99], ['국사', 50]]
for subject, score in scores:
    if score < min_score:
        print("과락 과목: {}, 점수 : {}".format(subject, score))

#continue를 사용한 방법
min_score = 60
scores = [['국어', 58], ['영어', 77], ['수학', 89], ['과학', 99], ['국사', 50]]
for subject, score in scores:
    if score >= min_score: continue
    print("과락 과목: {}, 점수 : {}".format(subject, score))
    
'''
사용자가 국영수사과 점수를 입력하면 과락과목과 점수를 출력하는 프로그램을 만들어보자
'''
kor_score = int(input("국어 점수 입력 : "))
eng_score = int(input("영어 점수 입력 : "))
mat_score = int(input("수학 점수 입력 : "))
sci_score = int(input("과학 점수 입력 : "))
his_score = int(input("국사 점수 입력 : "))
min_score = 60
scores = [['국어', kor_score], ['영어', eng_score], ['수학', mat_score], ['과학', sci_score], ['국사', his_score]]
for subject, score in scores:
    if score < min_score:
        print("과락 과목: {}, 점수 : {}".format(subject, score))
'''
리스트를 이용해서 학급 학생수가 가장 작은 학급과 가장 많은 학급을 출력해보자
반 인원수만 뽑아서 리스트 인덱스 +1 해서 한 방법
'''
#반 인원수만 뽑아서 리스트 인덱스 +1 해서 한 방법
n_list =[]
students_cnt = [[1,18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
for i, n in students_cnt:
    n_list.append(n)
print("학생수가 가장 적은 반(학생수) : {0}반({1}명)".format(n_list.index(min(n_list)) + 1, min(n_list)))
print("학생수가 가장 많은 반(학생수) : {0}반({1}명)".format(n_list.index(max(n_list)) + 1, max(n_list)))

# 07 리스트와 while문 01
'''
while 문을 이용하면 다양한 방법으로 조회가 가능하다
'''
cars = ['그랜저', '소나타', 'gv60', '320d', '쏘렌토']
# 방법 1
n = 0
while n < len(cars):
    print(cars[n])
    n += 1
# 방법 2 while True를 이용한 방법
n = 0
flag = True
while flag:
    print(cars[n])
    n += 1
    if n == len(cars):
        flag = False
# 방법 3 break를 이용한 방법
n = 0
while True:
    print(cars[n])
    n += 1
    if n == len(cars):
        break
    
# 
students_cnt = [[1,19], [2, 20], [3, 22], [4, 18], [5, 21]]
n = 0
while n < len(students_cnt):
    print("{0}반의 학생 수 : {1}".format(students_cnt[n][0], students_cnt[n][1]))
    n += 1
# while문을 이용해 학급별 학생수와 전체 학생 수 그리고 평균 학생수 구하기
students_cnt = [[1,18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
sum_students = 0


n = 0
while n < len(students_cnt):
    class_no = students_cnt[n][0]
    cnt = students_cnt[n][1]
    print("{0}반의 학생 수 : {1}".format(class_no, cnt))
    sum_students += cnt
    n += 1
print("전체 학생의 수 : {0}".format(sum_students))  
print("평균 학생의 수 : {0}".format(sum_students/ len(students_cnt)))

# 08 리스트와 while문 02
'''
while문과 if문을 이용해서 과락과목 출력하기
'''
min_score = 60
scores = [['국어', 58], ['영어', 77], 
          ['수학', 89], ['과학', 99], ['국사', 50]]
n = 0
while n < len(scores):
    if scores[n][1] < min_score:
        print("과락 과목: {}, 점수 : {}".format(scores[n][0], scores[n][1]))
    n += 1

# continue 사용
min_score = 60
scores = [['국어', 58], ['영어', 77], 
          ['수학', 89], ['과학', 99], ['국사', 50]]
n = 0
while n < len(scores):
    if scores[n][1] >= min_score:
        n += 1 
        continue
    print("과락 과목: {}, 점수 : {}".format(scores[n][0], scores[n][1]))
    n += 1
    
#실습
kor_score = int(input("국어 점수 입력 : "))
eng_score = int(input("영어 점수 입력 : "))
mat_score = int(input("수학 점수 입력 : "))
sci_score = int(input("과학 점수 입력 : "))
his_score = int(input("국사 점수 입력 : "))
min_score = 60
scores = [['국어', kor_score], ['영어', eng_score], ['수학', mat_score], ['과학', sci_score], ['국사', his_score]]
n = 0
while n < len(scores):
    if scores[n][1] < min_score:
        print("과락 과목: {}, 점수 : {}".format(scores[n][0], scores[n][1]))
    n += 1
    
# 실습 2 while문을 이용해서 학급 학생수가 가장 작은 학급과 많은 학급을 출력
n = 0
n_list =[]
students_cnt = [[1,18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
while n < len(students_cnt):
    n_list.append(students_cnt[n][1])
    n += 1
print("학생수가 가장 적은 반(학생수) : {0}반({1}명)".format(n_list.index(min(n_list)) + 1, min(n_list)))
print("학생수가 가장 많은 반(학생수) : {0}반({1}명)".format(n_list.index(max(n_list)) + 1, max(n_list)))

# 다른 방법
n = 0
min_class, max_class, min_cnt, max_cnt = 0, 0, 0, 0
students_cnt = [[1,18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]
while n < len(students_cnt):
    if min_cnt == 0 or min_cnt > students_cnt[n][0]:
        min_class = students_cnt[n][0]
        min_cnt = students_cnt[n][1]
    if max_cnt < students_cnt[n][1]:
        max_class = students_cnt[n][0]
        max_cnt = students_cnt[n][1]
        
    n += 1
print("학생수가 가장 적은 반(학생수) : {0}반({1}명)".format(min_class, min_cnt))
print("학생수가 가장 많은 반(학생수) : {0}반({1}명)".format(max_class, max_cnt))

# 09 enumerate() 함수
'''
인덱스와 아이템을 한번에 사용할 수 있는
enumerate() 함수를 이용하면 아이템을 열거할 수 있다

'''
sports = ['농구', '수구', '축구', '마라톤', '테니스']
#기존 방법
for i in range(len(sports)):
    print('{} : {}'.format(i, sports[i]))
#enumerate를 사용한 방법
for idx, value in enumerate(sports):
    print('{} : {}'.format(idx, value))
#enumerate는 문자열에도 적용할 수 있다
str = 'hello python'
for idx, value in enumerate(str):
    print('{} : {}'.format(idx, value))
    
#가장 좋아하는 스포츠가 몇 번째에 있는지 출력하기
sports = ['농구', '수구', '축구', '마라톤', '테니스']
my_fav_sports = "수구"
best_sport_idx = 0
for idx, value in enumerate(sports):
    if value == my_fav_sports:
        best_sport_idx = idx + 1
print('제일 좋아하는 스포츠 : {0}, {1}번째에 있습니다'.format(my_fav_sports, best_sport_idx))

#사용자가 입력한 문자열에서 공백의 갯수를 출력
message01 = input('메시지 입력 : ')
cnt = 0
for idx, value in enumerate(message01):
    if value == ' ':
        cnt += 1
print("공백의 갯수 : {}".format(cnt))

# 10 리스트에 아이템 추가
'''
append() 함수를 이용하면 인덱스에 아이템을 추가할 수 있다
append 함수를 이용해 추가하면 마지막 인덱스에 아이템을 추가할 수 있다.
'''
students = ['박경수', '박찬호', '이용규', '유승철', '안우진']
students.append('류현진')
students

scores = [['국어', 88], ['영어', 91]]
scores.append(['수학', 96])
for subject, score in scores:
    
    print("과목 : {}\n점수 : {}".format(subject, score))
    
'''
가족 구성원 나이가 아래와 같을 때 
새로 태어난 동생을 리스트에 추가해보자
아빠 - 40
엄마 - 38
나 - 9
'''
my_family_age = [['아빠', 40], ['엄마', 38], ['나', 9]]
my_family_age.append(['동생', 1])
for name, age in my_family_age:
    print("{0}의 나이 : {1}".format(name, age))
    
    
# 11 리스트의 특정 위치에 아이템 추가
'''
insert() 함수를 이용하면 특정 위치에 아이템을 추가할 수 있다
'''
students = ['박경수', '박찬호', '이용규', '유승철', '안우진']
students[3]
students.insert(3 , '구자욱')
students[3]
students

words = [ 'I', 'a', 'boy']
words.insert(1, 'am')
words
for word in words:
    print("{0}".format(word), end = ' ')

'''
오름차순으로 정렬되어 있는 숫자들에 사용자가 입력한 정수를 추가하는 프로그램
단 추가후에도 오름차순이 유지되어야 한다
'''
numbers01 = [1, 3, 6, 11, 45, 54, 62, 74, 85]
input_num = int(input("숫자 입력 : ")) # 55를 넣었음
insert_idx = 0
for idx, number in enumerate(numbers01):
    print(idx, number)
    
    if insert_idx == 0 and input_num < number :
        insert_idx = idx
numbers01.insert(insert_idx, input_num)   
print(numbers01) 

# 12 리스트의 아이템 삭제
'''
pop() 함수: 마지막 인덱스에 해당하는 아이템을 삭제함
pop(n) : pop()함수에 숫자를 넣으면 n번 인덱스에 해당하는 아이템을 삭제함
'''
students = ['박경수', '박찬호', '이용규', '유승철', '안우진']
students.append('류현진')
students
students.pop()
students

'''
점수표에서 최고/ 최저 점수를 삭제해보자
'''
player_score = [9.5, 8.9, 9.2, 8.8, 9.0]
print("선수 점수 : {}".format(player_score))
min_idx, max_idx, min_score, max_score = 0, 0, 0, 0
#enumerate 함수를 이용
for idx, score in enumerate(player_score):
    #최솟값 구하기
    if idx == 0 or min_score > score:
        min_idx = idx
        min_score = score
    #최고 점수 구하기
    if max_score < score:
        max_idx = idx
        max_score = score

print("최저 점수 : {0}, 최저 점수를 준 인덱스 : {1}".format(min_score, min_idx))
print("최고 점수 : {0}, 최고 점수를 준 인덱스 : {1}".format(max_score, max_idx))
#최저점을 준 인덱스의 값을 내보냄
player_score.pop(min_idx)
# 최고점을 준 인덱스의 값을 내보냄
player_score.pop(max_idx)
player_score

# 13 리스트의 특정 아이템 삭제
'''
remove() 함수 : 특정 아이템을 삭제할 수 있다
remove() 함수는 한 개의 아이템에만 삭제가 가능하다 삭제하려는 데이터가 2개
이상이라면 while 문을 이용하자
'''
students = ['박경수', '박찬호', '이용규', '유승철', '안우진']
students.append('류현진')
students.insert(3, '류현진')
students
flag = True
while flag == True:
    if '류현진' in students:
        students.remove('류현진')
    else:
        flag = False
students

'''
사용자가 입력한 일정을 삭제하는 프로그램
'''
todo_list = ['마케팅회의', '회의록정리', '점심약속', '월간업무보고', 
             '치과방문', '마트장보기']
print("일정 : {}".format(todo_list))

remove_item = input("삭제대상 입력 띄어쓰기없이 : ")

todo_list.remove(remove_item)
print("일정 : {}".format(todo_list))

'''
실습
아래 시험 과목표에서 사용자가 입력한 과목을 삭제하는 프로그램을 만들어보자
'''
subjects = ['국어', '영어', '수학', '과학', '국사']
print("시험 과목표 : {}".format(subjects))
remove_subject = input("삭제과목 입력 띄어쓰기없이 : ")
while remove_subject in subjects:
    subjects.remove(remove_subject)
    
print("시험 과목표 : {}".format(subjects))



