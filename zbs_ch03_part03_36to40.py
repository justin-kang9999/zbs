# 36 강 연습문제 정렬 알고리즘 02 삽입정렬 
'''
숫자로 이루어진 삽입 정렬 알고리즘을 이용해서 
오름차순, 내림차순으로 정렬하는 모듈을 만들어보자
'''

nums = map(int, input().split())
nums =list(nums)
def solution(nums, asc = True):
#오름차순
    if asc == True:
        for i01 in range(1, len(nums)):
            i02 = i01 - 1
            c_num = nums[i01]
            
            while nums[i02] > c_num and i02 >= 0:
                nums[i02 + 1] =nums[i02] # 한단계씩 뒤로 밀려나가므로
                i02 -= 1
            nums[i02 + 1] = c_num
            print(nums)
    
    else:
        for i01 in range(1, len(nums)):
            i02 = i01 - 1
            c_num = nums[i01]
            
            while nums[i02] < c_num and i02 >= 0:
                nums[i02 + 1] =nums[i02] # 한단계씩 뒤로 밀려나가므로
                i02 -= 1
            nums[i02 + 1] = c_num
            print(nums)
    if asc == True:
        print(f"오름차순으로 정리 결과 : {nums}")
    else:
        print(f"내림차순으로 정리 결과 : {nums}")
        
solution(nums, asc=True)
solution(nums, asc=False)

# 37 강 연습문제 정렬 알고리즘 03 선택정렬
'''
선택정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈
정렬 과정도 출력
'''
nums = map(int, input().split())
nums =list(nums)

def select_num(nums, asc= True):
    print(f"정리 안된 배열 : {nums}")
    if asc == True:
        #오름차순
        for i in range(len(nums) - 1):
            min_idx = i
            for j in range(i +1, len(nums)):
                if nums[min_idx] > nums[j]: # 클 때 자리를 바꿈
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            print(nums)
    else:
        #내림차순
        for i in range(len(nums) - 1):
            min_idx = i
            for j in range(i +1, len(nums)):
                if nums[min_idx] < nums[j]: # 작을 때 자리를 바꿈
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            print(nums)
    if asc == True:
        print(f"오름차순으로 정렬 된 배열: {nums}")
    else:
        print(f"내림차순으로 정렬 된 배열: {nums}")
select_num(nums,asc = True)        
select_num(nums,asc = False)

# 38 강 연습문제 정렬 알고리즘 04 병합정렬
'''
병합정렬 알고리즘을 이용해서 오름차순과 내림차순으로 정렬하는 모듈을 만들어보자
정렬 과정도 출력
'''
nums = map(int, input().split())
nums =list(nums)

def merge_num(nums, asc = True):
    print(f"정리 안된 배열 : {nums}")
    if len(nums) < 2:
        return nums
    #중간 값을 위해서 2로 나눔
    mid_idx = len(nums) // 2
    # 좌우 나누기 위한 변수, 재귀함수가 사용됨
    # 옵션이 생기면 재귀함수를 쓸 때 문제가 생기므로 asc까지 고려해야함
    leftNums = merge_num(nums[0:mid_idx], asc=asc)
    rightNums = merge_num(nums[mid_idx:len(nums)], asc=asc)
    #병합단계
    merge_nums = []
    left_idx, right_idx = 0, 0
        #병합을 위한 반복문
        
    while left_idx < len(leftNums) and right_idx < len(rightNums): 
        if asc == True:
        #비교해서 자리 바꿈 하는 부분
            if leftNums[left_idx] < rightNums[right_idx]:
                merge_nums.append(leftNums[left_idx])
                left_idx += 1
                print(nums)
            #반대의 경우
            else:
                merge_nums.append(rightNums[right_idx])
                right_idx += 1
                print(nums)
        else:
            if leftNums[left_idx] > rightNums[right_idx]:
                merge_nums.append(leftNums[left_idx])
                left_idx += 1
                print(nums)
            #반대의 경우
            else:
                merge_nums.append(rightNums[right_idx])
                right_idx += 1   
                print(nums)
    merge_nums = merge_nums + leftNums[left_idx:]
    merge_nums = merge_nums + rightNums[right_idx:]
    print(f"정렬된 배열 : {merge_nums}")
    return merge_nums
    

merge_num(nums)
merge_num(nums, asc= False)

# 39 강 최댓값 알고리즘 연습문제 01
'''
최댓값 알고리즘을 이용해 숫자로 이루어진 리스트에서
최댓값과 채댓값의 갯수를 찾는 모듈
1~50까지 난수 30개, 중복이 허용
'''
import random
nums = random.sample(range(1, 50), 30)
print("정렬 안된 nums : {}".format(nums))

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

max_ag(nums)

# 40 강 최댓값 알고리즘 연습문제 02
'''
학급 전체 학생의 시험 점수에 대한 평균과 최댓값을 구하고 평균과 최댓값의
편차를 출력하는 프로그램을 최댓값 알고리즘을 이용해서 만들어보자
'''
students_score = [100, 64, 94, 66, 75, 58, 99, 76, 96, 74, 54, 73, 88, 70, 68,
                 50, 95, 89, 69, 98]

def get_scores(nums):
    maxNum = 0
    maxNumIdx = 0
    total_score = sum(nums)
    avg_score = total_score // len(nums)
    
    for i, n in enumerate(nums):
        if maxNum < n:
            maxNum = n
            maxNumIdx = i
    
    print(f"평균 : {avg_score}, 최고 점수 : {maxNum}")
    print("평균, 최댓값과의 편차 : {}".format(maxNum - avg_score))

get_scores(students_score)
    

