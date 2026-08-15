# 1 <= n <= 100
# 1 <= m <= 7
# 1 <= P <= 40  (비율)

from itertools import product
def solution(users, emoticons):
    answer = []
    
    n = len(users)
    m = len(emoticons)
    
    discount_rates = [10, 20, 30, 40]
    discount_cases = list(product(discount_rates, repeat=m))
    
    for discount_case in discount_cases:
        count = 0
        income = 0
        
        for u_rate, u_price in users:
            purchased = 0
            
            for i in range(m):
                if u_rate <= discount_case[i]:
                    purchased += emoticons[i] - emoticons[i] * discount_case[i] * 0.01
            
            if purchased >= u_price:
                count += 1
            else:
                income += purchased
        
        answer.append((count, income))
    
    answer.sort(reverse=True)
    return answer[0]

'''
카톡 사용자 n명의 구매 기준을 담은 2차원 정수 배열 users,
이모티콘 m개의 정가를 담은 1차원 정수 배열 emotions 가 주어짐
이때 행사 목적을 최대한으로 달성했을 때의 가입 수, 매출 핵

목표
1. 가입자 수
2. 판매액
---------------------------------------------------------
각 할인율은 10%, 20%, 30%, 40%

'''