# 25 하노이의 탑
'''
퍼즐게임의 일종. 세 개의 기둥을 이용해서 다른 기둥을 옮기면 되고 제약조건이 존재
제약조건
한번에 한개의 원판만 옮길 수 있다
큰 원판이 작은 원판위에 있어서는 안된다
123 순으로 원판 세개가 쌓여있다면 3번째 기둥에 옮기려면

1번 원판: 3에서 2(으)로 이동
3번 원판: 1에서 3(으)로 이동
1번 원판: 2에서 1(으)로 이동
2번 원판: 2에서 3(으)로 이동
1번 원판: 1에서 3(으)로 이동

1234 순으로 원판 4개가 쌓여 있다고 하고 3 번째 기둥에 옮기려면
123번을 2번기둥에다 놓음, 4번을 3번째 기둥에 옮김
12번을 1번 기둥에다 놓음, 3번을 3번째 기둥에 옮김
1번을 2번째 기둥에 옮기고 2번을 3번째 기둥에 옮김
1번을 3번째 기둥에 옮김
'''

# 26 하노이의 탑 실습
'''
재귀함수를 이용해서 하노이의 탑을 구현해보자
'''
def move_disc(disCnt, fromBar, toBar, viaBar):
    if disCnt == 1:
        print(f"{disCnt}disc: {fromBar}에서 {toBar}(으)로 이동")
    else:
        # disCnt -1 개들을 경유 기둥으로 이동
        move_disc(disCnt - 1, fromBar, viaBar, toBar)
        # disCnt를 목적 기둥으로 이동
        print(f"{disCnt}disc: {fromBar}에서 {toBar}(으)로 이동")
        # disCnt -1 개들을 도착 기둥으로 이동
        move_disc(disCnt -1, viaBar, toBar, fromBar)

move_disc(3,1,3,2)
move_disc(4,1,3,2)

# 27 병합정렬
'''
재귀 함수를 이용함.
자료구조를 분할하고 각각의 분열된 자료구조를 정렬한 후 다시 병합하여
정렬
[8,1,4,3, 2,5,10,6] 이란 리스트가 있다면
일단 반을 쪼개고 다시 반을 쪼개고 다시 쪼개고 해서 하나씩 분할함

병합하면서 정렬
다 쪼개진 것을 자기 옆에 있는 것과 비교해서 순서를 정해서 뭉치고
다시 옆에 것과 비교해서 정렬하고 다시 옆 덩어리를 정렬해서 뭉치고

병합정렬은 재귀함수를 이용하면 간단히 표현이 가능함

'''
def msort(ns):
    # 1이 될때까지 분할하는 단계
    if len(ns) < 2:
        return ns
    #중간 값을 위해서 2로 나눔
    mid_idx = len(ns) // 2
    # 좌우 나누기 위한 변수, 재귀함수가 사용됨
    leftNums = msort(ns[0:mid_idx])
    rightNums = msort(ns[mid_idx:len(ns)])
    #병합단계
    merge_nums = []
    left_idx, right_idx = 0, 0
    #병합을 위한 반복문
    while left_idx < len(leftNums) and right_idx < len(rightNums):
        #비교해서 자리 바꿈 하는 부분
        if leftNums[left_idx] < rightNums[right_idx]:
            merge_nums.append(leftNums[left_idx])
            left_idx += 1
        #반대의 경우
        else:
            merge_nums.append(rightNums[right_idx])
            right_idx += 1
    merge_nums = merge_nums + leftNums[left_idx:]
    merge_nums = merge_nums + rightNums[right_idx:]
    
    return merge_nums
nums = [8,1,4,3, 2,5,10,6]
print(msort(nums))

# 28 병합정렬 실습
'''
1~100 난수 10개 생성, 다음 요구사항을 만족하는 모듈
병합정렬 알고리즘을 이용한 난수 정렬 모듈 구현
위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션을 추가
'''
# 병합정렬 모듈 만들기
# 기본 오름차순인 모듈
def msort(ns):
    
    # 1이 될때까지 분할하는 단계
    if len(ns) < 2:
        return ns
    #중간 값을 위해서 2로 나눔
    mid_idx = len(ns) // 2
    # 좌우 나누기 위한 변수, 재귀함수가 사용됨
    leftNums = msort(ns[0:mid_idx])
    rightNums = msort(ns[mid_idx:len(ns)])
    #병합단계
    merge_nums = []
    left_idx, right_idx = 0, 0
    #병합을 위한 반복문
    while left_idx < len(leftNums) and right_idx < len(rightNums):
        #비교해서 자리 바꿈 하는 부분
        if leftNums[left_idx] < rightNums[right_idx]:
            merge_nums.append(leftNums[left_idx])
            left_idx += 1
        #반대의 경우
        else:
            merge_nums.append(rightNums[right_idx])
            right_idx += 1
    merge_nums = merge_nums + leftNums[left_idx:]
    merge_nums = merge_nums + rightNums[right_idx:]
    
    return merge_nums


# 1~100 난수 10개 만들기

import random
rNums = random.sample(range(1, 101), 10)

msort(rNums)

# 오름차순 내림차순 기능을 추가
def msort(ns, asc=True):
    
    # 1이 될때까지 분할하는 단계
    if len(ns) < 2:
        return ns
    #중간 값을 위해서 2로 나눔
    mid_idx = len(ns) // 2
    # 좌우 나누기 위한 변수, 재귀함수가 사용됨
    # 옵션이 생기면 재귀함수를 쓸 때 문제가 생기므로 asc까지 고려해야함
    leftNums = msort(ns[0:mid_idx], asc=asc)
    rightNums = msort(ns[mid_idx:len(ns)], asc=asc)
    #병합단계
    merge_nums = []
    left_idx, right_idx = 0, 0
    #병합을 위한 반복문
    while left_idx < len(leftNums) and right_idx < len(rightNums):
        # 오름차순인지 내림차순인지 결정하는 부분 
        if asc == True:
            #비교해서 자리 바꿈 하는 부분
            if leftNums[left_idx] < rightNums[right_idx]:
                merge_nums.append(leftNums[left_idx])
                left_idx += 1
            #반대의 경우
            else:
                merge_nums.append(rightNums[right_idx])
                right_idx += 1
        else:
            if leftNums[left_idx] > rightNums[right_idx]:
                merge_nums.append(leftNums[left_idx])
                left_idx += 1
            #반대의 경우
            else:
                merge_nums.append(rightNums[right_idx])
                right_idx += 1
            
            
    merge_nums = merge_nums + leftNums[left_idx:]
    merge_nums = merge_nums + rightNums[right_idx:]
    
    return merge_nums

# 기본인 오름차순
msort(rNums)
msort(rNums, asc= False)

# 29 퀵정렬
'''
기준값보다 작은 값과 큰값으로 분리한 후 다시 합치는 방식
반복을 하기 때문에 재귀함수를 사용함
'''

# 재귀함수를 사용한 퀵정렬하는 함수
#오름차순 기준
def qsort(ns):
    if len(ns) < 2:
        return ns
    
    #기준값
    mid_idx = len(ns) // 2
    mid_val = ns[mid_idx]
    
    # 기준값보다 작은 수들, 같은 수, 큰 수들을 담은 리스트를 각각 생성
    small_nums, same_nums, big_nums = [] , [], []
    
    #비교를 위한 for문
    for n in ns:
        if n < mid_val:
            small_nums.append(n)
        elif n == mid_val:
            same_nums.append(n)
        else:
            big_nums.append(n)
    #각각 재귀함수를 통해서 정렬하도록
    return qsort(small_nums) + same_nums + qsort(big_nums) 

nums = [8, 1, 4, 3, 2 , 5, 4, 10, 6,8]
qsort(nums)

# 30 퀵정렬 실습
'''
1~100 난수 10개 생성, 다음 요구사항을 만족하는 모듈
퀵정렬 알고리즘을 이용한 난수 정렬 모듈 구현
위의 모듈에 오름차순과 내림차순을 선택할 수 있는 옵션을 추가
'''
def qsort(ns, asc = True):
    #반복을 탈출하기 위한 제약
    if len(ns) < 2:
        return ns
    
    #기준값
    mid_idx = len(ns) // 2
    mid_val = ns[mid_idx]
    
    # 기준값보다 작은 수들, 같은 수, 큰 수들을 담은 리스트를 각각 생성
    small_nums, same_nums, big_nums = [] , [], []
    
    #비교를 위한 for문
    for n in ns:
        if n < mid_val:
            small_nums.append(n)
        elif n == mid_val:
            same_nums.append(n)
        else:
            big_nums.append(n)
    #각각 재귀함수를 통해서 정렬하도록
    #오름차순인 경우
    if asc:
        return qsort(small_nums, asc=asc) + same_nums + qsort(big_nums,asc=asc) 
    else: # 내림차순이므로 순서를 바꿔줌
        return qsort(big_nums,asc=asc) + same_nums + qsort(small_nums, asc=asc)

import random
rNums = random.sample(range(1, 101), 10)
print(rNums) 
# 오름차순
qsort(rNums)
#내림차순
qsort(rNums, asc=False)