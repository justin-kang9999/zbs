# 01 선형 검색
'''
알고리즘
어떠한 문제를 풀기 위해 정해진 일련의 절차나 방법을 공식화한 형태로 표현한 것
선형 검색 알고리즘
선형으로 나열 되어 있는 데이터를 순차적으로 검색하면서 원하는 값을 찾음

'''

datas = [ 3, 2, 5, 7, 9, 1, 0, 8, 6, 4]

#search_data = int(input("찾으려는 숫자를 입력"))
search_data = 9

search_data_idx = -1 #존재하지 않는 숫자를 위해 -1이라는 가상의 값을 가지게 함
n = 0
while True:
    if n == len(datas):
        search_data_idx = -1
        break
    elif datas[n] == search_data:
        search_data_idx = n
        break
    n += 1
    
print("찾으려는 숫자 : {}".format(search_data))
print("찾으려는 숫자의 위치 : {}".format(search_data_idx))

'''
보초법
만약 찾는 데이터를 순서대로 찾았는데 끝까지 갔는데도 없다면?
마지막 인덱스에 찾으려는 값을 추가해서 찾는 과정을 간략화 하는 것
중간에 찾으면 찾는 값이 리스트 내에 있음, 없다면 맨 끝자락에 추가되었으므로
-1 값을 출력
'''
# 보초법
datas = [ 3, 2, 5, 7, 9, 1, 0, 8, 6, 4]
search_data = 15 # 리스트에 없는 숫자
search_data_idx = -1
datas.append(search_data)
n = 0
while True:
    if datas[n] == search_data:
        if n != len(datas) -1: # 맨 끝의 데이터가 아니면
            search_data_idx = n # 찾았고 그 자리수는 n
        break
    n += 1
# 만약 찾으려는 숫자가 없다면 while문에서 탈출하고 기존에 선언했던 -1값이 들어감   
print("찾으려는 숫자 : {}".format(search_data))
print("찾으려는 숫자의 위치 : {}".format(search_data_idx))
# 찾으려는 숫자가 리스트 내에 없기 때문에 -1을 반환함

# 02 선형 검색 실습
'''
1. 리스트 내에서 가장 앞에 있는 숫자 7을 검색하고 위치를 출력하자
2. 리스트 내에서 모든 숫자 7을 검색하고 각각 위치와 검색 갯수를 출력하자
'''
# 1번
#보초법 활용
nums = [4, 7, 10, 2, 4, 7,0, 2, 7, 3, 9]
search_data = 7

search_data_idx = -1
datas.append(search_data)
n = 0
while True:
    if datas[n] == search_data:
        if n != len(datas) -1:
            search_data_idx = n
        break
    n += 1
# 만약 찾으려는 숫자가 없다면 while문에서 탈출하고 기존에 선언했던 -1값이 들어감   
print("찾으려는 숫자 : {}".format(search_data))
print("찾으려는 숫자의 위치 : {}".format(search_data_idx))

# 2번
nums = [4, 7, 10, 2, 4, 7,0, 2, 7, 3, 9]

search_data = 7
search_data_idxs = [] # 모두 찾기 때문에 리스트에 저장
datas.append(search_data)
nums.append(search_data)
n = 0
while True:
    if nums[n] == search_data:
        if n != len(nums) - 1:
            search_data_idxs.append(n)
        else: 
            break
        
    n += 1
    
print("찾으려는 숫자 : {}".format(search_data))
print("찾으려는 숫자의 위치 : {}".format(search_data_idxs))
print("검색 횟수 : {}".format(len(search_data_idxs)))

# 함수화
def search_num(tmp_nums):
    search_data = int(input("찾으려는 숫자를 입력"))
    search_data_idxs = []
    tmp_nums.append(search_data)
    n = 0
    search_data_idx = -1
    while True:
        if nums[n] == search_data:
            if n != len(nums) - 1:
                search_data_idxs.append(n)
            else: 
                break
            
        n += 1
        
    print("찾으려는 숫자 : {}".format(search_data))
    print("찾으려는 숫자의 위치 : {}".format(search_data_idxs))
    print("검색 횟수 : {}".format(len(search_data_idxs)))

# 03 이진 검색
'''
이진 검색
정렬되어 있는 자료 구조에서 중앙값과의 크고 작음을 통해서 데이터를 검색
데이터가 정렬 되어 있다는 가정하에 이진 검색을 함
데이터가 정렬이 안되어 있다면 일단 정렬 시킨 후 이진검색 활용
처음에 중앙값을 구하고 크고 작음을 비교해서 
중앙값보다 크다면 중앙값보다 큰 쪽에서 다시 중앙값을 구해서 다시 크기비교
중앙값보다 작다면 중앙값보다 작은 쪽에서 다시 중앙값을 구해서 다시 크기비교

'''
#이진검색


'''
처음에 찾으려는 인덱스 값, 끝 인덱스 값, 중앙 인덱스값 
중앙 인덱스의 값까지 기본으로 주어짐
'''
#search_data = int(input)
datas = [i for i in range(1,12)]
datas
search_data = 7
start_idx = 0
end_idx = len(datas) - 1
mid_idx = (start_idx + end_idx) // 2
mid_val = datas[mid_idx]
search_result_idx = -1
while search_data <= datas[len(datas) - 1] and search_data >= datas[0]:
    #우연히 그 값인경우
    if search_data == datas[len(datas) - 1]:
        search_result_idx = len(datas) - 1
        break 
    
    # 찾는 값이 중앙값보다 큰 경우
    if search_data > mid_val:
        start_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_val = datas[mid_idx]
        
    # 찾는 값이 중앙값보다 작은 경우
    elif search_data < mid_val:
        end_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_val = datas[mid_idx]
        
    # 찾는 값이 중앙값과 같은 경우
    elif search_data == mid_val:
        search_result_idx = mid_idx
        break
print("찾는 값의 위치 : {}".format(search_result_idx)) 

# 함수화

def binary_searching(datas):
    search_data = int(input)
    start_idx = 0
    end_idx = len(datas) - 1
    mid_idx = (start_idx + end_idx) // 2
    mid_val = datas[mid_idx]
    search_data_idx = -1
    while search_data <= datas[len(datas) - 1] and search_data >= datas[0]:
        # 우연히 찾는 값이 딱 그 값인 경우
        if search_data == datas(len(datas) - 1):
            search_data_idx = len(datas) - 1
            break
        # 찾는 값이 중앙값보다 클 경우
        if search_data > mid_val:
            start_idx = mid_idx; mid_idx = (start_idx + end_idx) // 2
            mid_val = datas[mid_idx]
            # print(f'mid_idx : {mid_idx}')
            # print(f'mid_val : {mid_val}')
        
        elif search_data < mid_val:
            end_idx = mid_idx;start_idx = mid_idx; mid_idx = (start_idx + end_idx) // 2
            mid_val = datas[mid_idx]
            # print(f'mid_idx : {mid_idx}')
            # print(f'mid_val : {mid_val}')
        # 찾는 데이터가 중앙값과 같을 때 = 즉 답을 찾았을 때
        elif search_data == mid_val:
            search_data_idx = mid_idx
        break   
        print("찾은 값의 위치 : {} ".format(search_data_idx)) 

# 04 이진 검색 실습
'''
실습
이진검색 방법으로 
리스트를 오름차순으로 정렬 한 후 7을 검색하고 위치 인덱스를 출력하자
'''
nums = [4, 10, 22, 5, 0, 17, 7, 11, 9, 61, 88]
#정렬
nums.sort()
nums

search_data = 61
search_result_idx = -1

start_idx = 0 
end_idx = len(nums) - 1
mid_idx = (start_idx + end_idx) //2
mid_val = nums[mid_idx]

while search_data <= nums[len(nums) - 1] and search_data >= nums[0]:
    #우연히 그 값인경우
    if search_data == nums[len(nums) - 1]:
        search_data_idx = len(nums) - 1
        break 
    
    # 찾는 값이 중앙값보다 큰 경우
    if search_data > mid_val:
        start_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_val = nums[mid_idx]
        
    # 찾는 값이 중앙값보다 작은 경우
    elif search_data < mid_val:
        end_idx = mid_idx
        mid_idx = (start_idx + end_idx) // 2
        mid_val = nums[mid_idx]
        
    # 찾는 값이 중앙값과 같은 경우
    elif search_data == mid_val:
        search_result_idx = mid_idx
        break
print("찾는 값의 위치 : {}".format(search_result_idx))

# 05 순위
'''
수의 크고 작음을 이용해서 수의 순서를 정하는 것을 순위라고 함

'''
#순위 연습
import random
nums = random.sample(range(50,101),20)
nums
#0을 20 개 만드는 방법 1
# ranks = [0] * 20
# ranks
# 다른 방법
ranks = [0 for i in range(20)]
ranks

for idx, num01 in enumerate(nums):
    # 순위 비교를 위한 중복 for문
    for num02 in nums:
        #만약 num01이 num02보다 작다면 rank[idx]에 1을 더해서 점점 숫자를 늘려나감
        if num01 < num02:
            ranks[idx] += 1
print(nums)
print(ranks)

for idx, num in enumerate(nums):
    print("num : {0}\t rank : {1}".format(num, ranks[idx] + 1))

# 06 순위 실습
'''
실습 문제
학급 학생 20명, 중간/ 기말고사 성적을 이용해서 각각의 순위를 구하고
중간고사 대비 기말고사 순위 변화를 출력하는 프로그램을 만들어보자
시험성적은 난수를 이용한다 50~100점 사이
'''

# 중간/ 기말 순위 비교 편차 클래스를 만듦
class Rank_deviation:
    def __init__(self, mss, ess):
        #중간 기말 성적
        self.mid_stu_sco = mss
        self.end_stu_sco = ess
        #중간/ 기말 순위
        self.mid_ranks = [0 for i in range(len(mss))]
        self.end_ranks = [0 for i in range(len(mss))]
        #편차 
        self.rank_deviation = [0 for i in range(len(mss))]
        
    def set_rank(self, ss, rs):
        for idx, sco1 in enumerate(ss):
            for sco2 in ss:
                if sco1 < sco2:
                    rs[idx] += 1
    #중간/ 기말 순위 갖고오기 set은 순위 만들기, get은 순위 가져오기              
    def set_mid_rank(self):
        self.set_rank(self.mid_stu_sco, self.mid_ranks)
    def get_mid_rank(self):
        return self.mid_ranks
    
    def set_end_rank(self):
        self.set_rank(self.end_stu_sco, self.end_ranks)
    def get_end_rank(self):
        return self.end_ranks
    
    #편차
    def print_ranks_deviation(self):
        for idx, mrank in enumerate(self.mid_ranks):
            deviation = mrank - self.end_ranks[idx]
            #중간보다 오른 경우
            if deviation > 0:
                deviation = '↑ ' + str(abs(deviation))
            # 중간보다 떨어진 경우
            elif deviation < 0:
                deviation = '↓ ' + str(abs(deviation))
            # 그대로인 경우
            else:
                deviation = '= ' + str(abs(deviation))
            print("중간고사 순위 : {0}\t 기말고사 순위 : {1}\t 편차 : {2}".format(mrank + 1, self.end_ranks[idx] + 1, deviation))
                
# 성적 생성
import random
mid_scores = random.sample(range(50,101),20)

end_scores = random.sample(range(50,101),20)


# 만든 클래스 사용을 위한 변수 선언, 중간 기말 성적을 넣어서 초기화
rnk = Rank_deviation(mid_scores, end_scores)        
# 중간고사 순위 정하기
rnk.set_mid_rank()
# 중간고사 순위를 가져와서 보기
rnk.get_mid_rank()
# 기말고사 순위 정하기
rnk.set_end_rank()   
# 기말고사 순위를 가져와서 보기
rnk.get_end_rank()
# 편차 확인
rnk.print_ranks_deviation()

# 07 버블정렬
'''
정렬 첫 번째 시간
버블 정렬
처음부터 끝까지 인접하는 인덱스의 값을 순차적으로 비교하면서 큰 숫자를
가장 끝으로 옮기는 알고리즘

10, 2, 7 ,21, 0 이라는 아이템을 가진 리스트가 있으면
10과 2를 비교해서 10이 더 크니 10의 순서를 바꿈
2, 10, 7, 21, 0
10과 7을 비교해서 10이 더 크니 10의 순서를 바꿈
2, 7, 10, 21, 0
10과 21을 비교해서 21이 더 크니깐 10은 그대로 순서 고정
2, 7 , 10, 21, 0
21과 0을 비교해서 21이 크니 순서를 바꿈
2, 7, 10, 0, 21

이런식으로 계속해서 비교해나가면서 가장 큰 수를 맨 끝으로 옮기는 방법
# 자리를 바꾸는 전통적인 방법
# tmp = nums[j]
# nums[j] = nums[j + 1]
# nums[j + 1] = tmp
'''
# 버블정렬 연습
nums = [10, 2, 7 ,21, 0]
length = len(nums) -1
print("순서가 정리 안 된 nums : {0}".format(nums))
for i in range(length):
    for j in range(length - i):
        #21과 0 비교한 경우를 생각
        if nums[j] > nums[j+1]:
            #자리를 바꿔줌
            #파이썬에서 사용가능한 방법
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
        
print("순서가 정리 된 nums : {0}".format(nums))



# 08 버블정렬 실습
# 버블정렬 함수화
def bubble_sort(ns, deepCopy = True):
    # 깊은 복사와 얕은 복사를 생각해서 deepCopy 명령어를 사용해 깊은 복사를 한 것.
    # 기본은 딥카피를 함, 그래서 원본 데이터를 유지하면서 작업을 하는 것으로
    import copy
    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns = ns
    length = len(cns) -1

    for i in range(length):
        for j in range(length - i):
            #21과 0 비교한 경우를 생각
            if cns[j] > cns[j+1]:
                #자리를 바꿔줌
                #파이썬에서 사용가능한 방법
                cns[j], cns[j + 1] = cns[j + 1], cns[j]
            #print("정리중 : {}".format(cns))
    return cns
'''
학급에 20명, 학생들을 키 순서로 줄세워보자. 학생들의 키는 170-185 난수생성
중복도 있다.
'''
import random
stu_hei = []
# for i in range(20):
#     stu_hei.append(random.randint(170,186))
stu_hei = [random.randint(170, 186) for i in range(20)]
stu_hei
sorted_hei = bubble_sort(stu_hei)
sorted_hei



