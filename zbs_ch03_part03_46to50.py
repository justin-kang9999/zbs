# 46강 근삿값 알고리즘 연습문제 02
'''
사용자 몸무게와 키를 입력하면 체질량지수를 계산
근삿값 알고리즘과 bmi표를 이요해서 신체 상태를 출력하는 프로그램
bmi는 키의 제곱을 몸무게로 나누면 됨
'''
weight = float(input())
height = float(input())
# 
def get_bmi_num(weight, height):
    bmi_scores = [25, 23, 18.5]
    nearNum = 0
    minNum = 25
    bmi = round(weight / (height ** 2), 2)
    for n in bmi_scores:
        abs_num = abs(n - bmi)
        
        if abs_num < minNum:
            minNum = abs_num
            nearNum = n
    print(f"bmi : {bmi}")
    print(f"nearNum : {nearNum}")
    if nearNum <= 18.5:
        return '저체중'
    elif 18.5 < nearNum <= 23:
        return '정상'
    elif 23 < nearNum <= 25:
        return '과체중'
    elif nearNum > 25:
        return '과체중'

get_bmi_num(weight, height)


# 47강 재귀 알고리즘 연습문제 01
'''
[12000, 13000, 12500, 11000, 10500, 98000, 91000, 10500, 11500, 12000, 12500]
재귀 알고리즘을 이용해서 매출 증감액을 나타내는 프로그램
'''
sales = [12000, 13000, 12500, 11000, 10500, 
         98000, 91000, 10500, 11500, 12000, 12500]
#재귀 함수 만들기
def sales_uad(ss):
    if len(ss) == 1:
        return ss
    print(f'sales: {ss}')
    current = ss.pop(0) # 현재 12000이 담겨있고 13000부터 시작
    next_sales = ss[0]
    in_or_decrease = next_sales - current
    if in_or_decrease > 0:
        in_or_decrease = '+ '+ str(in_or_decrease)

    print(f'매출 증감액 : {in_or_decrease}')
    return sales_uad(ss)
sales_uad(sales)

# 48강 재귀 알고리즘 연습문제 02
'''
사용자가 정수 두개를 입력하면 작은 정수와 큰 정수 사이의 모든 정수의 합을 
구하는 프로그램을 재귀 알고리즘을 이용해서 만들기
'''
num1 = int(input())
num2 = int(input())
num1, num2

class self_algo:
    def __init__(self, n1, n2):
        self.big_num = 0
        self.small_num = 0
        self.setN1N2(n1,n2)
        
    def setN1N2(self, n1,n2):
        self.big_num = n1
        self.small_num = n2
        
        if n1 < n2:
            self.big_num = n2
            self.small_num = n1
    def add_num(self, n):
        if n <= 1:
            return n
        return n + self.add_num(n-1)
    
    def sum_between(self):
        return self.add_num(self.big_num - 1) - self.add_num(self.small_num)
        
ns = self_algo(num1, num2)    
ns.big_num
ns.sum_between()

# 49강 평균 알고리즘 연습문제 01

'''
체조 선수의 점수. 최댓값과 최솟값을 제외한 나머지 점수에 대한 평균
순위를 정하는 알고리즘
'''

class Max_algo:
    def __init__(self,ss):
        self.scores = ss
        self.max_score = 0
        self.max_idx = 0
        
    def remove_max(self):
        self.max_score = self.scores[0]
        for i, s in enumerate(self.scores):
            if self.max_score < s:
                self.max_score = s
                self.max_idx = i
        print(f"self.max_score : {self.max_score}\nself.max_idx : {self.max_idx}")
        self.scores.pop(self.max_idx)

class Min_algo:
    def __init__(self,ss):
        self.scores = ss
        self.min_score = 0
        self.min_idx = 0
        
    def remove_min(self):
        self.min_score = self.scores[0]
        for i, s in enumerate(self.scores):
            if self.min_score > s:
                self.min_score = s
                self.min_idx = i
        print(f"self.min_score : {self.min_score}\nself.min_idx : {self.min_idx}")
        self.scores.pop(self.min_idx)

top_players = [9.12, 8.95, 8.12, 6.9, 6.18]
scores = [6.7, 5.9, 8.1, 7.9, 6.7, 7.3, 7.2, 8.2, 6.2, 5.8]

max_al = Max_algo(scores)
max_al.remove_max()
min_al = Min_algo(scores)
min_al.remove_min()

# 평균 구하기
total = 0
avg = 0
for n in scores:
    total += n
avg = round(total / len(scores), 2)

# 순위 구하기
class Top5_players:
    def __init__(self, current, ns):
        self.current = current
        self.new_score = ns
        
    def set_alig(self):
        near_idx = 0
        min_num = 10.0
        
        for i, s in enumerate(self.current):
            abs_num = abs(self.new_score)
            if abs_num < min_num:
                min_num = abs_num
                near_idx = i
        # 크기 비교해서 들어갈 위치
        if self.new_score >= self.current[near_idx]:
            for i in range(len(self.current) - 1, near_idx, -1):
                self.current[i] = self.current[i-1]
            self.current[near_idx] = self.new_score
        else:
            for i in range(len(self.current) - 1, near_idx + 1, -1):
                self.current[i] = self.current[i-1]
            self.current[near_idx + 1] = self.new_score
    def get_final_top5(self):
        return self.current

tp = Top5_players(top_players, avg)    
tp.set_alig()
new_top = tp.get_final_top5()
print(new_top)

# 50강 평균 알고리즘 연습문제 02
'''
학급 전체 학생의 시험 점수 평균
학생 수 20
각 과목간 평균점수와 홍길동 학생 점수의 차를 출력하는 프로그램
'''
kor_avg = 88; eng_avg = 82; mat_avg = 90; sci_avg = 78; his_avg = 92

hong_kor = 85; hong_eng = 90; hong_mat = 82; hong_sci = 88; hong_his = 100

stucnt_kor_total = kor_avg * 20 - hong_kor
stucnt_eng_total = eng_avg * 20 - hong_eng
stucnt_mat_total = mat_avg * 20 - hong_mat
stucnt_sci_total = sci_avg * 20 - hong_sci
stucnt_his_total = his_avg * 20 - hong_his

stucnt_kor_avg = round(stucnt_kor_total / 19, 2)
stucnt_eng_avg = round(stucnt_eng_total / 19, 2)
stucnt_mat_avg = round(stucnt_mat_total / 19, 2)
stucnt_sci_avg = round(stucnt_sci_total / 19, 2)
stucnt_his_avg = round(stucnt_his_total / 19, 2)

# 점수 차이
kor_gap = round(hong_kor - stucnt_kor_avg, 2)
eng_gap = round(hong_eng - stucnt_eng_avg, 2)
mat_gap = round(hong_mat - stucnt_mat_avg, 2)
sci_gap = round(hong_sci - stucnt_sci_avg, 2)
his_gap = round(hong_his - stucnt_his_avg, 2)

print(f"국어점수 차이 : {'+' + str(kor_gap)if kor_gap > 0 else kor_gap}")
print(f"영어점수 차이 : {'+' + str(eng_gap)if eng_gap > 0 else eng_gap}")
print(f"수학점수 차이 : {'+' + str(mat_gap)if mat_gap > 0 else mat_gap}")
print(f"과학점수 차이 : {'+' + str(sci_gap)if sci_gap > 0 else sci_gap}")
print(f"국사점수 차이 : {'+' + str(his_gap)if his_gap > 0 else his_gap}")
stucnt_avg = round(((stucnt_kor_avg + stucnt_eng_avg + stucnt_mat_avg + stucnt_sci_avg + stucnt_his_avg)/ 5), 2)
hong_avg = round((hong_kor + hong_eng + hong_mat + hong_sci + hong_his) / 5, 2)

avg_gap = round((hong_avg - stucnt_avg), 2)
print(f"평균 점수 차이  :{'+' + str(avg_gap) if avg_gap > 0 else avg_gap}")