# 09 삽입 정렬
'''
버블 정렬과는 다른 개념으로
정렬되어 있는 자료 배열과 비교해서 정렬 위치를 찾는 개념
5 10 2 1 0 이란 아이템을 담은 리스트가 있을 때
5와 10을 비교 했을 때 정렬이 되어 있음.
2와 5, 10을 비교해서 들어갈 자리를 찾음.
잠깐 2를 다른 곳에다 두고 2의 인덱스에 10을 넣음
5 10 10 1 0 ...2 
2를 기존 10 자리에다 넣음
5 2 10 1 0
다시 5와 2를 비교함
2 5 10 1 0
같은 방법으로 1과 2 5 10을 비교
1 2 5 10
같은 방법으로 0과 1 2 5 10 비교
0 1 2 5 10
'''
# 삽입 정렬 연습
nums = [5, 10, 2, 1, 0]

# 오름차순을 기준으로 정렬한 경우
for i01 in range(1, len(nums)):
    i02 = i01 - 1
    c_num = nums[i01]
    
    while nums[i02] > c_num and i02 >= 0:
        nums[i02 + 1] =nums[i02] # 한단계씩 뒤로 밀려나가므로
        i02 -= 1
    nums[i02 + 1] = c_num
    print(nums)
    
#내림차순으로 정렬
nums = [0, 5, 2, 10, 1]
for i01 in range(1, len(nums)):
    i02 = i01 - 1
    c_num = nums[i01]
    while nums[i02] < c_num and i02 >= 0:
        nums[i02 + 1] =nums[i02] # 한단계씩 뒤로 밀려나가므로
        i02 -= 1
    nums[i02 + 1] = c_num
    print(nums)
# 함수화
# 오름차순 딥카피 안함
# def ascending_i_sort(nums):
#     for i01 in range(1, len(nums)):
#         i02 = i01 - 1
#         c_num = nums[i01]
    
#     while nums[i02] > c_num and i02 >= 0:
#         nums[i02 + 1] =nums[i02] # 한단계씩 뒤로 밀려나가므로
#         i02 -= 1
#     nums[i02 + 1] = c_num
#     print(nums)
#     return nums

# ascending_i_sort(nums)   
    
# 10 삽입 정렬 실습
'''
1~1000까지 난수 100개 생성해서 요구사항을 만족하는 모듈을 만들어보자
요구사항 1) 생성된 난수들을 오름 또는 내림 차순으로 정렬하는 알고리즘 구현
요구사항 2) 생성된 난수 중 최대 최솟값을 반환하는 함수를 구현
'''
# 클래스 만듦
class Sort_nums():
    def __init__(self, ns, asc= True):
        self.nums = ns
        self.isAsc = asc # 속성 체크
    def is_ascending(self, flag):
        self.isAsc = flag
    def set_sort(self):
        for i1 in range(1, len(self.nums)):
            i2 = i1 - 1
            c_num = self.nums[i1]
            # 오름차순인지 확인
            if self.isAsc:
                while self.nums[i2] > c_num and i2 >= 0:
                    self.nums[i2 +1] = self.nums[i2]
                    i2 -= 1
            else: # 반대인 내림차순인 경우
                while self.nums[i2] < c_num and i2 >= 0:
                    self.nums[i2 +1] = self.nums[i2]
                    i2 -= 1
            self.nums[i2 + 1] = c_num
    #정렬된 배열을 갖고 올 수 있도록 하는 함수
    def get_sorted_numbers(self):
        return self.nums
    #최솟값
    def get_min_number(self):
        #먼저 오름차순인지 내림차순인지 확인
        if self.isAsc:
            return self.nums[0] # 오름차순이면 배열 순서상 제일 첫번째
        else:
            return self.nums[len(self.nums)-1] # 내림차순이면 제일 마지막
    # 최댓값
    def get_max_number(self):
        #먼저 오름차순인지 내림차순인지 확인
        if self.isAsc:
            return self.nums[len(self.nums)-1] # 오름차순이면 배열 순서상 제일 마지막
        else:
            return self.nums[0] # 내림차순이면 제일 첫번째
    
# 난수 생성
import random

nums = random.sample(range(1, 1000), 100)
print("정렬 안된 nums : {}".format(nums))
# 클래스 이용을 위한 객체 생성
sn = Sort_nums(nums)  
# 클래스에서 기본값이 오름차순이므로 따로 설정 안함
sn.set_sort()
sorted_num = sn.get_sorted_numbers()
print("오름차순으로 정렬 된 nums : {}".format(sorted_num))

# 내림차순으로 해보기
sn.is_ascending(False)
sn.set_sort()
sorted_num = sn.get_sorted_numbers()
print("내림차순으로 정렬 된 nums : {}".format(sorted_num))

#최솟값, 최댓값
print("최솟값 : {}".format(sn.get_min_number()))
print("최댓값 : {}".format(sn.get_max_number()))

# 11 선택 정렬
'''
가장 작은 데이터를 찾아서 자리를 바꾸는 방법
주어진 리스트 중에 최솟값을 찺아 그 값을 맨 앞에 위치한 값과 교체하는 방식
nums = [4, 2, 5, 1, 3] 이라는 리스트에서
4가 기준이라 치면 2랑 비교해서 2가 더 작으므로 기준이 2로 바뀐다
2,5 비교해서 2가 계속 기준
2,1 비교해서 1이 더 작으므로 기준이 1로 바뀜
1, 3 비교해서 1이 계속 기준
첫번째인 4와 1과 자리를 바꿈
1,2,5,4,3
1은 정렬이 되었으므로 1을 빼고 다시 2,5,4,3에서 같은 방식으로 비교
1,2,3,4,5
같은 방식에서 4,5 비교하면 이미 정렬 되어 있으므로 기존 배열 그대로 나옴
1,2,3,4,5
'''
# 선택 정렬 연습
nums = [4, 2, 5, 1, 3]
for i in range(len(nums) - 1):
    #처음 기준이 되는 인덱스, for문을 한번 돌면서 최솟값, 기준이 되는 min_idx를 찾음
    min_idx = i
    # 최솟값을 찾기 위한 for 문
    for j in range(i+1, len(nums)): # 기준이 i이므로 시작점을 i+1
        if nums[min_idx] > nums[j]: # 만약 기준이 되는 min_idx번째 값이 더 크다면
            min_idx = j # 기준이 되는 min_idx는 j로 바뀜
            
    nums[i], nums[min_idx] = nums[min_idx], nums[i] # 값까지 바꿈
    
print(nums)

# 12 선택 정렬 실습
'''
선택정렬 알고리즘을 이용해서 학생 20명의 시험점수를 오름차순, 내림차순으로
정렬하는 모듈, 시험점수는 50부터 100점까지
'''
# 선택정렬 함수화 깊은 복사 하기
def select_num(ns, asc= True):
    
    if asc:
        #오름차순
        for i in range(len(ns) - 1):
            min_idx = i
            for j in range(i +1, len(ns)):
                if ns[min_idx] > ns[j]: # 클 때 자리를 바꿈
                    min_idx = j
            ns[i], ns[min_idx] = ns[min_idx], ns[i]
    else:
        #내림차순
        for i in range(len(ns) - 1):
            min_idx = i
            for j in range(i +1, len(ns)):
                if ns[min_idx] < ns[j]: # 작을 때 자리를 바꿈
                    min_idx = j
            ns[i], ns[min_idx] = ns[min_idx], ns[i]
    return ns

# 학생 점수 만들기
import random
import copy
scores = random.sample(range(50, 100), 20)
# 오름차순
result = select_num(copy.deepcopy(scores))
result
# 내림차순
result = select_num(copy.deepcopy(scores), asc= False)
result

# 13 최댓값
'''
자료구조에서 가장 큰 값을 찾는다.
이미 파이썬 내장 함수중에 존재하지만 찾는 방식을 알아보기 위함
'''
nums = [-2, -4, 5, 7, 10, 0, 8, 20, -11]
class Max_al:
    def __init__(self, ns):
        self.nums = ns
        self.maxNum = 0
        
    def get_max_num(self):
        self.maxNum = self.nums[0]
        # 반복문을 돌려서 비교를 해봐서 maxnum이 계속 바뀌는 식으로
        for n in self.nums:
            if self.maxNum < n:
                self.maxNum = n
        return self.maxNum
ma = Max_al(nums)
maxNum = ma.get_max_num()
print(maxNum)
        
# 14 최댓값 실습
'''
 리스트에서 아스키 코드가 갖는 가장 큰 값을 알고리즘을 만들어보자
'''
#아스키코드를 찾기 위한
class Max_algo:
    def __init__(self, cs):
        self.chars = cs
        self.maxChar = 0 # 초기화
        
    def get_max_char(self):
        self.maxChar = self.chars[0]
        # 반복문을 돌려서 비교를 해봐서 maxnum이 계속 바뀌는 식으로
        for c in self.chars:
            if ord(self.maxChar) < ord(c):
                self.maxChar = c
        return self.maxChar
chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
ma = Max_algo(chars)
maxChar = ma.get_max_char()
print(maxChar)
        

# 15 최솟값
'''
자료구조에서 가장 작은 값을 찾는다.
이미 파이썬 내장 함수중에 존재하지만 찾는 방식을 알아보기 위함
'''

class Min_al:
    def __init__(self, ns):
        self.nums = ns
        self.minNum = 0
        
    def get_min_num(self):
        self.minNum = self.nums[0]
        # 반복문을 돌려서 비교를 해봐서 maxnum이 계속 바뀌는 식으로
        for n in self.nums:
            if self.minNum > n:
                self.minNum = n
        return self.minNum

nums = [-2, -4, 5, 7, 10, 0, 8, 20, -11] 
ma = Min_al(nums)
minNum = ma.get_min_num()
print(minNum)
    
    
# 16 최솟값 실습
'''
 리스트에서 아스키 코드가 갖는 가장 작은 값을 알고리즘을 만들어보자
'''
#아스키코드를 찾기 위한
class Min_algo:
    def __init__(self, cs):
        self.chars = cs
        self.minChar = 0 # 초기화
        
    def get_min_char(self):
        self.minChar = self.chars[0]
        # 반복문을 돌려서 비교를 해봐서 maxnum이 계속 바뀌는 식으로
        for c in self.chars:
            if ord(self.minChar) > ord(c):
                self.minChar = c
        return self.minChar
chars = ['c', 'x', 'Q', 'A', 'e', 'P', 'p']
ma = Min_algo(chars)
minChar = ma.get_min_char()
print(minChar)












