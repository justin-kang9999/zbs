# 17 최빈값
'''
데이터에서 빈도수가 가장 많은 데이터를 최빈값이라고 한다
제일 큰 값을 찾아서 그 갯수만큼 0으로 된 리스트를 만듦
인덱스로 접근해서 빈도를 더함
'''

# 클래스로 만듦
class Max_al:
    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0
    def setMaxIdxNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0
        
        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i
    def getMaxNum(self):
        return self.maxNum
    def getMaxNumIdx(self):
        return self.maxNumIdx
nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
mns = Max_al(nums)
mns.setMaxIdxNum()
max_n = mns.getMaxNum()
indexes = [0] * max_n
len(indexes)

for n in nums:
    indexes[n] += 1
indexes
mns = Max_al(indexes)
mns.setMaxIdxNum()
max_num = mns.getMaxNum()
max_idx = mns.getMaxNumIdx()
print("즉, {1}의 데이터가 가장 많이 등장.\n그 횟수는 {0}".format(max_num, max_idx))

# 18 최빈값 실습
'''
최빈값 알고리즘을 이용해서 다음 학생 100명의 점수를 시각화 하자
'''
# 최댓값 알고리즘부터 
class Max_al:
    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        self.maxNumIdx = 0
    def setMaxIdxNum(self):
        self.maxNum = self.nums[0]
        self.maxNumIdx = 0
        
        for i, n in enumerate(self.nums):
            if self.maxNum < n:
                self.maxNum = n
                self.maxNumIdx = i
    def getMaxNum(self):
        return self.maxNum
    def getMaxNumIdx(self):
        return self.maxNumIdx
nums = [1, 3, 7, 6, 7, 7, 7, 12, 12, 17]
mns = Max_al(nums)
mns.setMaxIdxNum()
max_n = mns.getMaxNum()
indexes = [0] * max_n
len(indexes)

for n in nums:
    indexes[n] += 1
indexes
mns = Max_al(indexes)
mns.setMaxIdxNum()
max_num = mns.getMaxNum()
max_idx = mns.getMaxNumIdx()

from audioop import minmax
import random

from numpy import average
scores = []
for i in range(100):
    rn = random.randint(71, 100)
    if rn != 100: rn = rn - (rn % 5)
    scores.append(rn)
    
max_algo = Max_al(scores)
max_algo.setMaxIdxNum()
max_num = max_algo.getMaxNum()
max_num
#인덱스 리스트 작성
indexes = [0 for i in range(max_num + 1)]
len(indexes)

# 인덱스 리스트에 빈도 저장
for n in scores:
    indexes[n] = indexes[n] +1
indexes
# 빈도수 
n = 1
while True:
    max_algo = Max_al(indexes)
    max_algo.setMaxIdxNum()
    max_num = max_algo.getMaxNum()
    max_idx = max_algo.getMaxNumIdx()
    
    if max_num == 0:
        break
    print(f"{n}. {max_idx}, 빈도수 {max_num}\t", end = "")
    print('+' * max_num)
    
    indexes[max_idx] = 0
    n += 1    
    
# 19 근삿값
'''
근사값이란 
특정 값에 가장 가까운 값을 뜻함
즉 절댓값이 가장 작은 것을 찾음
'''
import random
nums = random.sample(range(0, 50), 20)

#input_num = int(input())
input_num = 11

nearNum = 0
minNum = 50 # 실습을 위해서 50이 최고인 것을 알기 때문에 아는 것이지만 모를 때를 생각해야함

for n in nums:
    abs_num = abs(n - input_num)
#    print(abs_num)
    if abs_num < minNum:
        minNum = abs_num
        nearNum = n
print("가장 가까운 숫자 : {}".format(nearNum))

# 20 근삿값 실습

'''
근삿값 알고리즘을 이용해서 시험 점수를 입력하면 학점이 출력되는
프로그램. 평균 점수에 따른 학점 기준 점수는 
근삿값
95 - a
85 - b
75 - c
65 - d
55 - f
'''

scores = []
kor = int(input("kor 점수 입력 "))
scores.append(kor)
eng = int(input("eng 점수 입력 "))
scores.append(eng)
mat = int(input("mat 점수 입력 "))
scores.append(mat)
sci = int(input("sci 점수 입력 "))
scores.append(sci)
his = int(input("his 점수 입력 "))
scores.append(his)
scores
total_score = sum(scores)
total_score
avg = total_score / len(scores)
avg
# 학점을 위한 근삿값 알고리즘 함수
def get_near_num(an):
    bascores = [95, 85, 75, 65, 55]
    nearNum = 0
    minNum = 100
    for n in bascores:
        abs_num = abs(n - an)
        
        if abs_num < minNum:
            minNum = abs_num
            nearNum = n
    if nearNum == 95:
        return 'A'
    elif nearNum == 85:
        return 'B'
    elif nearNum == 75:
        return 'C'
    elif nearNum == 65:
        return 'D'
    elif nearNum <= 55:
        return 'F'
grade = get_near_num(avg)
grade

# 21 평균
'''
여러 수나 양의 중간 값을 갖는 수를 평균이라고 한다
'''
import random
nums = random.sample(range(0, 100), 10)
total = 0
for n in nums:
    total += n
avg = total / len(nums)
nums
avg   
# 50 이상 90 이하의 평균이라 치면
import random
nums = random.sample(range(0, 100), 10)
abl_num = []
total = 0
for n in nums:
    if n >= 50 and n <= 90:
        total += n
        abl_num.append(n)
avg = total / len(abl_num)
nums
abl_num
round(avg, 2)   
#정수들의 평균
nums = [ 4, 5.12, 0, 6, 7, 8.34, 9.1, 3, 3.159, 1, 11, 12.789]
abl_num = []
total = 0
for n in nums:
    #정수는 뒤에 소숫점 아래 숫자가 없으므로 빼면 0이 나올 것임을 이용해서
    if n - int(n) == 0:
        abl_num.append(n)
        total += n
total
avg = total / len(abl_num)
abl_num
round(avg, 2) 
#반대로 실수들의 평균
nums = [ 4, 5.12, 0, 6, 7, 8.34, 9.1, 3, 3.159, 1, 11, 12.789]
abl_num = []
total = 0
for n in nums:
    #실수는 빼면 0.~은 남으니깐 뺀 결과가 0이 아니면 실수인 것으로
    if n - int(n) != 0:
        abl_num.append(n)
        total += n
total
avg = total / len(abl_num)
abl_num
round(avg, 2) 

# 22 평균 실습
scores = [8.9, 7.6, 8.2, 9.1, 8.8, 8.1, 7.9, 9.4, 7.2, 8.7]
top_player = [9.12, 8.95, 8.12, 7.9, 7.88]
# 평균을 구하고 전체 순위에서 비교해서 자기 자리를 찾아가도록
total = 0
for i in scores:
    total += i
avg = round(total / len(scores), 2)
total
avg
# 순위를 찾아서 top_player에 들어가도록
class Top5players:
    def __init__(self, cs, ns):
        self.current_scores = cs
        self.new_scores = ns
    #정렬 근사값 알고리즘을 이용한
    def set_align_score(self):
        near_idx = 0
        near_score = 0
        min_num = 10.0
        for i, s in enumerate(self.current_scores):
            abs_num = abs(self.new_scores - s)
            if abs_num < min_num:
                min_num = abs_num
                near_idx = i
                near_score = s
        #절대값으로만 비교했기 때문에 부호를 붙여서 작은지 큰지를 확인해야함
        #먼저 크거나 작은 경우
        if self.new_scores >= self.current_scores[near_idx]:
            # 거꾸로 들어가서 비교
            for i in range(len(self.current_scores)- 1, near_idx , -1):
                self.current_scores[i] = self.current_scores[i - 1]
        else:
            for i in range(len(self.current_scores)- 1, near_idx + 1 , -1):
                self.current_scores[i] = self.current_scores[i-1] 
    # 정렬된 리스트를 반환해주는 함수
    def get_final_top(self):
        return self.current_scores
    
tp = Top5players(top_player, avg)
tp.set_align_score()
top5_scores = tp.get_final_top()
top5_scores

# 23 재귀
'''
재귀 알고리즘이란 
나 자신을 다시 호출하는 것을 재귀라고 함.
'''
# 반복문 대신 재귀 함수를 이용한 예
def recusion(num):
    if num > 0:
        print("*" * num)
        return recusion(num - 1)
    else:
        return 1

recusion(15)
# 재귀 함수를 이용한 팩토리얼 구하기
def factorial(num):
    if num > 0:
        return num * factorial(num - 1)
    else:
        return 1
factorial(5)

# 24 재귀 실습
'''
재귀 알고리즘을 이용한 최대 공약수 계산
유클리드 호재법
두 자연수 n1, n2에 대하여 n1>n2인 경우 n1을 n2로 나눈 나머지를 r이라고 할 때
n1,n2의 최대 공약수는 n2와 r의 최대 공약수와 같다
'''
#  for문을 돌려서 최대공약수 구해보기
def gc_devide(n1, n2):
    maxNum = 0
    for i in range(1, n1 +1):
        if n1 % i == 0 and n2 % i == 0:
            maxNum = i
    return maxNum
gc_devide(82, 32)

#재귀함수를 이용해서 나머지를 갖고 계속해서 나누는 것이라고 생각하면 됨
def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2, n1 % n2)
    
gcd (82, 32)

























