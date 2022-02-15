# 41 강 최솟값 알고리즘 연습문제 01
'''
최솟값 알고리즘이용
최솟값과 최솟값 갯수
리스트는 1~50 난수 30개
중복 허용
'''
import random
from traceback import print_tb
nums = random.sample(range(1, 50), 30)
print(nums)
def min_ag(nums):
    minNum = nums[0]
    minNum_cnt = 0
    for i, n in enumerate(nums):
        if minNum > n:
            minNum = n
    
    for j in nums:
        if minNum == j:
            minNum_cnt += 1
    print("min_num : {0}\nmin_num_cnt : {1}".format(minNum, minNum_cnt))

min_ag(nums)

# 42 강 최솟값 알고리즘 연습문제 02
'''
학급 전체 학생 시험 정수에 대한 평균과 최솟값
평균과 최솟값의 편차를 구하는 프로그램을 최솟값 알고리즘을 이용해서 만들어보자
전체 학생 시험 점수
[100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68, 50, 95, 89, 69, 98]
'''
scores = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 
          73, 88, 70, 68, 50, 95, 89, 69, 98]
def get_scores(scores):
    total_score = 0
    avg = 0
    minNum = scores[0]
    #평균 구하기
    for i in scores:
        total_score += i
    #최솟값 구하기 
        if minNum > i:
            minNum = i
    avg = round(total_score / len(scores), 2)
    avgmin = round((avg - minNum),2)
    print("평균값: {}, 최솟값 : {}\n 편차 :{}".format(avg, minNum, avgmin))

get_scores(scores)

# 43 강 최빈값 알고리즘 연습문제 01
'''
최빈값 알고리즘을 이용해서 나이 분포를 간단한 그래프로 출력하는 모듈 만들기
최댓값을 이용해서 0을 기본으로 리스트를 만들어서 카운트

'''

import random
age = [random.randint(30, 60) for i in range(40)]
age
# 최댓값 알고리즘
def max_ag(nums):
    maxNum = 0
    maxNumIdx = 0
    maxNum_cnt = 0
    for i, n in enumerate(nums):
        if maxNum < n:
            maxNum = n
            maxNumIdx = i
    
    for j in nums:
        if maxNum == j:
            maxNum_cnt += 1
    print("max_num : {0}\nmax_num_cnt : {1}".format(maxNum, maxNum_cnt))

max_ag(age)

# 빈도수 
def set_index(nums):
    # 빈도수를 위한 리스트 만들기
    indexes = [0 for i in range(max(nums)+1)]
    # 나이 빈도수에 따라 더해주도록
    for j in nums:
        indexes[j] += indexes[j] + 1
    # 그래프 출력   
    maxNum = 0
    maxNumIdx = 0
    maxNum_cnt = 0
    for i, n in enumerate(nums):
        if maxNum < n:
            maxNum = n
            maxNumIdx = i
    
    for j in nums:
        if maxNum == j:
            maxNum_cnt += 1
    n = 1
    while True:
        
        print(f'[{n :0>3}] {max(nums)}세 빈도수')
        print('+' * maxNum_cnt)
        nums.remove(max(nums))
        indexes[maxNum] = 0
        n += 1
        if len(nums) == 0:
            break
        
set_index(age)

# 44 강 최빈값 알고리즘 연습문제 02

'''
최빈값 알고리즘을 이용해서 
로또 모든 회차의 각각 번호에 대한 빈도수를 출력
'''
class Lotto_mode:
    def __init__(self,ln):
        self.lottoNums = ln
        self.mode_list = [0 for n in range(1,47)]
    def get_lotto_num(self):
        for round_nums in self.lottoNums:
            for num in round_nums: 
                self.mode_list[num] = self.mode_list[num] + 1
        return self.mode_list
    # 빈도수 출력 함수
    def print_mode(self):
        if sum(self.mode_list) == 0:
            return None
        for i, n in enumerate(self.mode_list):
            if i !=0:
                    print(f'번호 : {i:>2} 빈도 : {n}, {"*" *n}')
            
            
import random
lotto_nums = []
tmp = []
for i in range(180):
    num = random.randint(1,45)
    tmp.append(num)
    if len(tmp) == 6:
        lotto_nums.append(tmp)
        tmp = []
len(lotto_nums)
ln = Lotto_mode(lotto_nums)
m_list = ln.get_lotto_num()
print(m_list)
ln.print_mode()

# 45 강 근삿값 알고리즘 연습문제 01
'''
근사값 알고리즘을 이용해서 수심을 입력하면 수온을 출력하는 모듈
'''
class Near_algo:
    def __init__(self, d):
        self.temps = {0:24, 5:22, 10:20, 15:16, 20:13, 25:10, 30:6}
        self.depth = d
        self.nearNum = 0
        self.minNum = 24
    def get_near_numbers(self):
        for n in self.temps.keys():
            abs_num = abs(n - self.depth)
            if abs_num < self.minNum:
                self.minNum = abs_num
                self.nearNum = n
        return self. temps[self.nearNum]

depth = int(float(input()))
nag = Near_algo(depth)
temp = nag.get_near_numbers()
print(f"물온도 : {temp}")