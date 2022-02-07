# 14 리스트 연결
'''
extend()함수를 이용하면 리스트에 또다른 리스트를 연결해 확장할 수 있다
+ 덧셈 연산자를 이용해서 연결할수도 있다
extend 함수를 사용하면 기존 리스트에 추가가 됨
덧셈 연산자를 이용하면 제 3의 리스트가 생김
'''
from re import search
from select import select
from tkinter import N, scrolledtext


list01 = ['홍길동', '박찬호', '이용규']
list02 = ['강호동', '박승철', '김지은']
#extend()
list01.extend(list02)
list01
#더하기 연산자
list01 + list02
list01
list02

#실습
my_num = [1,3,5,6,7]
fr_num = [2,3,5,8,10]
add_list = my_num + fr_num
add_list02 = list(set(add_list))
add_list
add_list02

result = []
for _ in add_list:
    if _ not in result:
        result.append(_)
print(result)

# 15 리스트 아이템 정렬
'''
sort() 함수를 이용하면 아이템을 정렬할 수 있다.
기본은 오름차순
reverse = False가 기본이라 오름차순으로 됨
reverse =True 하면 내림차순
'''
list01 = ['홍길동', '박찬호', '이용규']
list02 = ['강호동', '박승철', '김지은']
students = list01 + list02
# 오름차순
students.sort()
students
# 내림차순
students.sort(reverse = True)
students

# 실습
pl_score = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
pl_score.sort()
#최저점 빼기
pl_score.pop(0)
#최고점빼기
pl_score.pop()
pl_score
# 총점과 평균 출력
sum = 0
avg = 0
for i in pl_score:
    sum += i
    avg = sum / len(pl_score)
print("총점 : %.2f"%sum)
print("평균 : %.2f"%avg )

# 16 리스트 아이템 순서 뒤집기
'''
리스트 순서 뒤집기
reverse() 함수를 이용하면 아이템 순서를 뒤집을 수 있다
'''
list01 = ['홍길동', '박찬호', '이용규']
list02 = ['강호동', '박승철', '김지은']
students = list01 + list02
students.reverse()
students
'''
실습 
전쟁에서 사용되는 암호를 해독하도록
암호 27156231
해독결과 13326125157214
거꾸로 하고 1,2번 곱해서 3번째에 넣고
'''
password01 = '2715631'
secret_list = []
solved_list = ''
secret_list = [int(ch) for ch in password01]
secret_list.reverse()
secret_list

val = secret_list[0] *secret_list[1]
secret_list.insert(2,val)
val = secret_list[3] *secret_list[4]
secret_list.insert(5,val)
val = secret_list[6] *secret_list[7]
secret_list.insert(8,val)
val = secret_list[9] *secret_list[10]
secret_list.insert(11,val)

secret_list

# 17 리스트 슬라이싱

'''
내가 원하는 부분의 아이템만 뽑아내는 것이 슬라이싱
[n:m]
n부터 m까지
숫자를 안넣으면 끝까지 혹은 처음부터
[:2] => 0번부터 2번 전까지
[2:] => 2번부터 끝까지
[::2] =>0번부터 끝까지 한칸씩 건너 뛰면서
'''
list01 = ['홍길동', '박찬호', '이용규']
list02 = ['강호동', '박승철', '김지은']
students = list01 + list02
students[2:4]

num = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print(num[2:-2])
print(num[2:-2:2])
print(num[:-2:2])
print(num[::2])

'''
[n:m]을 이용하면 문자열 슬라이싱도 가능하다
슬라이싱을 할 때 단계 설정도 가능하다
슬라이싱을 이용해서 아이템을 변경할 수 있다.
'''
# 슬라이싱을 이용한 아이템 변경
students
students[1:4] = ['chanho park', 'yonggyu lee', 'hodong kang']

'''
slice() 전용 함수를 이용할 수도 있다.
'''
list01 = ['홍길동', '박찬호', '이용규']
list02 = ['강호동', '박승철', '김지은']
students = list01 + list02
students[slice(2,4)]

# 18 리스트 나머지 기능들 (01)
'''
리스트 곱셈 연산
리스트를 곱셈연산하면 아이템이 반복된다
'''
list01 = ['홍길동', '박찬호', '이용규']
list01 * 2
list01
# 인덱스 찾기
list01.index('이용규')

'''
실습 1~10까지 정수가 중복되지 않고 섞여있을 때 행운의 숫자 7의 위치를 찾자
'''
import random
sample_list = random.sample(range(1,11),10)

select_idx = int(input('숫자 7의 위치 입력(0~9번까지) : '))
search_idx = sample_list.index(7)
if select_idx == search_idx:
    print("{}번 정답입니다".format(search_idx))
else:
    print('ㅠㅠ 정답이 아닙니다.')
print(sample_list)
print(search_idx)
    

# 19 리스트 나머지 기능들 (02)
'''
특정 아이탬의 갯수 알아내기
count()함수를 이용하면 특정 아이템의 갯수를 알 수 있다
count('아이템') 하면 갯수가 나옴
특정 아이템을 삭제
del 키워드를 이용하면 특정 아이템을 삭제할 수 있다.
'''
students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '강호동','김지은']
students.count('강호동')
del students[5]
students

'''
실습
하루 백명이 헌혈을 한다고 쳤을 때
하루동안 헌혈을 진행한 후 혈액형 별 갯수를 파악하는 프로그램

'''
import random
blood_types = ['A', 'B', 'AB', 'O']
today_data = []
type_cnt = []
for i in range(100):
    type = blood_types[random.randrange(len(blood_types))]
    today_data.append(type)
print(today_data)
print(len(today_data))

for type in blood_types:
    print("{0}형\t : {1}개".format(type, today_data.count(type)))

# 20 튜플
'''
튜플: 데이터 타입중 하나. 리스트와 비슷하지만 아이템 변경이 불가능하다
숫자, 문자열, 논리형 등 모든 기본 데이터를 같이 저장할 수 있다
튜플 내에 또 다른 컨테이너 자료형 데이터를 저장할 수도 있다
()을 이용해서 선언하고, 구분은 ,
'''
students = tuple(students)
students
numbers = (10, 20, 30, 40, 50, 60, 70)
strs = (3.14, '십', 20, 'one', '3.141592')
datas = (10, 20, 30, (40, 50, 60))

family_name = ("홍상직", "홍엄마","홍인형", "홍길동" )
print(family_name)

# 오늘 일정을 튜플에 저장하고 출력해보자
today_sch = ('10시- 업무회의', '12시- 친구와 점심', '15시- 자료정리', 
             '18시- 운동', '21시- tv시청')
print(today_sch)

# 21 튜플 아이템 조회
'''
튜플도 리스트와 마찬가지로 아이템에 자동으로 부여되는 번호표가 있다.
즉 인덱스가 있기 때문에 튜플 또한 인덱스를 이용해서 조회가 가능하다
'''
students[3]

'''
실습
5명의 학생 이름을 튜플에 저장하고 인덱스가 홀수인 학생과 짝수인 학생을 구분해서
인덱스와 학생 이름을 출력해보자
'''
students = ("김성예", "신경도", "박기춘", "최승철", "황동석")
len(students)
for i in range(len(students)):
    if i % 2 == 0:
        print("인덱스가 짝수인 학생 : {}번 {}".format(i, students[i]))
    else:
        print("인덱스가 홀수인 학생 : {}번 {}".format(i, students[i]))
        
# 22 in과 not in 키워드
'''
in, not in 키워드를 이용하면 아이템의 존재 유무를 알 수 있다.
in, not in 키워드는 문자열에서도 사용 가능하다
'''
students_tuple = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
search_name = input ('학생 이름 입력 : ')
if search_name in students_tuple:
    print("{0} 학생은 우리반 학생입니다.".format(search_name))
else:
    print("{0} 학생은 우리반 학생이 아닙니다.".format(search_name))
# 문자열에도 사용이 가능하다.
python_str = '파이썬(영어: Python)은 1991년 네덜란드계 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. 파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'
python_str
'Python' in python_str
'python' in python_str
'파이썬' in python_str

'''
실습
컴퓨터가 1부터 10까지 난수를 생성한 후 사용자가 입력한 숫자가 있는지 없는지 출력하는 프로그램

'''
import random
rand_num = random.sample(range(1,11), 5)
user_num = int(input('1~10까지의 숫자 입력 : '))
if user_num in rand_num:
    print('빙고')
else:
    print('다음기회에')
rand_num

'''
문장에서 비속어가 있는지 알아내는 프로그램을 만들어보자
'''
wrong_words = ["쩔었다", "짭새", "꼽사리", "먹튀", "지린", "쪼개다"]
sentence = '짭새 등장에 강도들은 모두 쩔었다. 그리고 강도들은 지린 듯 도망갔다.'
for word in wrong_words:
    if word in sentence:
        print("비속어 : {}".format(word))
        
# 23 튜플 길이
'''
아이템 갯수
리스트와 마찬가지로 튜플에 저장된 아이템의 갯수를 튜플 길이라고 한다.
리스트와 마찬가지로 len()을 사용 할 수 있다.
len()과 반복문을 이용하면 튜플의 아이템 조회가 가능하다
'''
students_tuple = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
len(students_tuple)
for i in range(len(students_tuple)):
    print("{0}번 : {1}".format(i, students_tuple[i]))

n = 0
for i in range(len(students_tuple)):
    print("{0}번 : {1}".format(i, students_tuple[i]))
    n += 1
    print(n)
'''
실습
좋아하는 운동 종목을 튜플에 저장하고 반복문을 이용해서 출력해보자
'''
my_sports = ('수영', '배구', '야구', '러닝')
for i in range(len(my_sports)):
    print("{0}번 스포츠 : {1}".format(i, my_sports[i]))

# 24 튜플 결합
'''
튜플의 결합
튜플은 결합 할 수 있다.
enxtend()함수는 튜플에서 이용할 수 없다.
'''
tuple01 = ('홍길동', '박찬호', '이용규')
tuple02 = ('강호동', '박승철', '김지은')
tuple03 = tuple01 + tuple02
tuple03

# 튜플을 이용해서 번호를 합치되 번호가 중복되지 않도록
my_num_tu = (1,3,5,6,7)
fr_num_tu = (2,3,5,8,10)
# 튜플과 튜플끼리만 더하기가 가능하므로 (변수, ) 이런 형식으로 하면 튜플화가 된다
for n in fr_num_tu:
    if n not in my_num_tu:
        my_num_tu = my_num_tu + (n, )
print(my_num_tu)


# 25 튜플 슬라이싱
'''
튜플 슬라이싱
리스트와 마찬가지로 [n:m]을 이용하면 리스트에서 원하는 아이템만 뽑아낼 수 있다
튜플은 슬라이싱을 이용해서 아이템을 변경할 수 없다.
'''
students_tuple = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
students_tuple[:3]
'''
슬라이싱 단계 설정
슬라이싱 할 때 단계를 설정할 수 있다.
'''
num_tu = (2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14)
print(num_tu[2:-2:2])
print(num_tu[::2])

'''
튜플 또한 slice() 함수를 이용해서 아이템을 슬라이싱 할 수 있다.
'''
students_tuple[slice(4)]
