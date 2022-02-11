# 31 연습문제 검색 알고리즘 01
'''
선형 알고리즘 이용
리스트는 1~20 10개 난수
검색과정을 로그로 출력
검색에 성공하면 해당 정수의 인덱스를 출력하고 
검색결과가 없다면 -1
'''
import random
numbers = random.sample(range(1,21),10)
search_num = int(input())
def search_algo(ns,sn):
    search_data_idx = -1
    print("리스트 : {}\n찾으려는 숫자 : ".format(ns,sn)) 
    n = 0
    #선형 검색을 위한 반복문
    while True:
        if n == len(ns): #끝까지 간 것
            search_data_idx = -1
            print("검색 실패")
            break
        elif ns[n] == sn:
            search_data_idx = n #찾으려는 값
            print("검색성공")
            print("검색 결과 해당 숫자가 있는 인덱스 : {}".format(search_data_idx))
            break
        print(n)
        n += 1
    return search_data_idx
    # print("찾으려는 숫자 : {}".format(sn))
    # print("찾으려는 숫자의 위치 : {}".format(search_data_idx))
    
result_idx = search_algo(numbers, search_num)

#다른 방법 
if result_idx == -1:
    print("결과를 찾을 수 없습니다")
    print(result_idx)
else:
    print("검색 결과")
    print("위치한 인덱스: {}".format(result_idx))
    print("찾은 숫자 : {}".format(search_num))


# 32 연습문제 검색 알고리즘 02
'''
이진 알고리즘 이용
리스트는 [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]
검색과정을 로그로 출력
검색에 성공하면 해당 정수의 인덱스를 출력하고 
검색결과가 없다면 -1
'''
bi_list = [1,2,4,6,7,8,10,11,13,15,16,17,20,21,23,24,27,28]
search_num = int(input())
#이진 검색 함수화
def bi_algo(datas,search_data):
    
    start_idx = 0
    end_idx = len(datas) - 1
    mid_idx = (start_idx + end_idx) // 2
    mid_val = datas[mid_idx]
    search_result_idx = -1
    print(f'mid_idx : {mid_idx}')
    print(f'mid_val : {mid_val}')
    while search_data <= datas[len(datas) - 1] and search_data >= datas[0]:
        #우연히 그 값인경우
        if search_data == datas[len(datas) - 1]:
            search_result_idx = len(datas) - 1
            print(f'mid_idx : {mid_idx}')
            print(f'mid_val : {mid_val}')
            break 
        
        # 찾는 값이 중앙값보다 큰 경우
        if search_data > mid_val:
            start_idx = mid_idx
            mid_idx = (start_idx + end_idx) // 2
            mid_val = datas[mid_idx]
            print(f'mid_idx : {mid_idx}')
            print(f'mid_val : {mid_val}')
            
        # 찾는 값이 중앙값보다 작은 경우
        elif search_data < mid_val:
            end_idx = mid_idx
            mid_idx = (start_idx + end_idx) // 2
            mid_val = datas[mid_idx]
            print(f'mid_idx : {mid_idx}')
            print(f'mid_val : {mid_val}')  
                      
        # 찾는 값이 중앙값과 같은 경우
        elif search_data == mid_val:
            search_result_idx = mid_idx
            print(f'mid_idx : {mid_idx}')
            print(f'mid_val : {mid_val}')
            break
    return search_result_idx 


result_idx = bi_algo(bi_list,search_num)

#다른 방법 
if result_idx == -1:
    print("결과를 찾을 수 없습니다")
    print(bi_list)
    print(result_idx)
else:
    print("검색 결과")
    print(bi_list)
    print("위치한 인덱스: {}".format(result_idx))
    print("찾은 숫자 : {}".format(search_num))

# 33 연습문제 순위 알고리즘 01
'''
아이템 순위를 출력, 순위에 따라 아이템을 정렬하는 모듈
리스트는 50~100 난수 20개
'''

import random
nums = random.sample(range(50,101),20)

def rank_algo(nums):
    ranks = [0] * len(nums)
    for idx, num01 in enumerate(nums):
        # 순위 비교를 위한 중복 for문
        for num02 in nums:
            #만약 num01이 num02보다 작다면 rank[idx]에 1을 더해서 점점 숫자를 늘려나감
            if num01 < num02:
                ranks[idx] += 1
    print(f"정리 안된 리스트 : {nums}")
    print(f'정리 안된 순위 : {ranks}')

    for i, n in enumerate(nums):
        print(f'숫자 : {n}\t rank: {ranks[i] + 1}')
    sorted_nums = [0] * len(nums)
    #정렬을 위한 for 문
    for idx, rank in enumerate(ranks):
        sorted_nums[rank] = nums[idx]
    return sorted_nums

snums = rank_algo(nums)
print(f'정리되기 전 리스트 : {nums}')
print(f'정리된 리스트 : {snums}')

# 34 연습문제 순위 알고리즘 02
'''
강의가 잘못됨
갑자기 49강 최솟값 나옴
pdf상 34강 문제
알파벳 문자들과 정수들에 대한 순위를 정하는 프로그램을 
순위 알고리즘으로 짜보자. 알파벳은 아스키 코드 값을 이용한다
'''

def ascii_rank_algo(nums):
    print(f'입력받은 리스트 : {nums}')
    #아스키 코드 값을 받도록
    for i, n in enumerate(nums):
        if type(n) == str:
            tmp = ord(n)
            nums.insert(i, tmp)
            nums.remove(n)
    print(f'아스키코드 값으로 처리 된 리스트 : {nums}')
    
    ranks = [0] * len(nums)
    for idx, num01 in enumerate(nums):
        # 순위 비교를 위한 중복 for문
        for num02 in nums:
            #만약 num01이 num02보다 작다면 rank[idx]에 1을 더해서 점점 숫자를 늘려나감
            if num01 < num02:
                ranks[idx] += 1
    print(f"정리 안된 리스트 : {nums}")
    print(f'정리 안된 순위 : {ranks}')

    for i, n in enumerate(nums):
        print(f'숫자 : {n}\t rank: {ranks[i] + 1}')
    sorted_nums = [0] * len(nums)
    #정렬을 위한 for 문
    for idx, rank in enumerate(ranks):
        sorted_nums[rank] = nums[idx]
    return sorted_nums

ascii_list = [32, 'a', 'z', 45, 'G', 39, 50, 'T', 't', 22, 31, 55, 's', 63, 59, 'E']

ascii_rank_algo(ascii_list)

# 35 연습문제 정렬 알고리즘 01
'''
버블정렬 알고리즘을 이용해 오름차순 내림차순으로 정렬하는 모듈 작성
정렬하는 과정도 출력하도록
'''
#오름차순 내림차순 다 가능한 버블 알고리즘 함수화
def bubble_sort(ns, deepCopy = True, asc = True):
    # 깊은 복사와 얕은 복사를 생각해서 deepCopy 명령어를 사용해 깊은 복사를 한 것.
    # 기본은 딥카피를 함, 그래서 원본 데이터를 유지하면서 작업을 하는 것으로
    import copy
    if deepCopy:
        cns = copy.copy(ns)
    else:
        cns = ns
    length = len(cns) -1
    #버블 알고리즘 구현 (기본이 오름차순)
    for i in range(length):
        for j in range(length - i):
            
            #오름차순 이라면
            if asc == True:
                if cns[j] > cns[j+1]:#큰지 작은지 생각해서
                    #자리를 바꿔줌
                    #파이썬에서 사용가능한 방법
                    cns[j], cns[j + 1] = cns[j + 1], cns[j]
                    print("정리중 : {}".format(cns))
            else:        
                if cns[j] < cns[j+1]:
                    #자리를 바꿔줌
                    #파이썬에서 사용가능한 방법
                    cns[j], cns[j + 1] = cns[j + 1], cns[j]
                    print("정리중 : {}".format(cns))
        print()# 반복 들어간 숫자의 정리가 끝날때마다 빈칸을 줘서 한칸 띄움
    print("정렬이 끝났습니다")
    return cns

import random
nums = random.sample(range(1,21), 10)
print(f'정렬 안된 리스트 : {nums}')

result = bubble_sort(nums,asc=True)
result02 = bubble_sort(nums,asc=False)
print(f'오름차순으로 정렬 된 리스트 : {result}')
print(f'내림차순으로 정렬 된 리스트 : {result02}')


