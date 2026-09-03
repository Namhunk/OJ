# 1 <= begin <= end <= 1,000,000,000
# end - begin <= 5,000
from math import ceil
def solution(begin, end):
    answer = []
    
    MAX_SIZE = 10**7 # 숫자의 최대
    for x in range(begin, end+1): # 5,000 범위
        if x < 2: # 1인 경우 0으로
            answer.append(0)
            continue
        
        k_min = max(2, -(-x // MAX_SIZE))
        best_n = 0
        i = 1
        
        while i * i <= x: # 절반까지
            if x % i == 0:
                for k in (i, x // i): # 두 대칭 값들을 넣어봄
                    if k >= k_min:
                        n = x // k
                        if n > best_n:
                            best_n = n
            
            i += 1
        answer.append(best_n)
        

    return answer


'''
begin ~ end 사이에 깔려있는 블록의 숫자 배열을 return

2차원 배열이 있다고 할 때 index (1, 1)부터 시작

1행에서는 1x2번쨰 부터 +1 만큼 이동하며 1로 채움
2행에서는 2x2번째 부터 +2 만큼 이동하며 2로 채움
.
.
.
n행에서는 nx2번째 부터 +n 만큼 이동하며 n으로 채움




'''