# 1 <= len(a) <= 500,000
from collections import Counter
def solution(a):
    N = len(a)
    
    if N < 2: return 0
    
    freq = Counter(a)
    answer = 0
    for k in freq.keys():
        if freq[k]*2 <= answer:
            continue
        
        cnt = 0
        idx = 0
        while idx < N-1:
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            
            cnt += 1
            idx += 2
        
        answer = max(answer, cnt*2)
    return answer

"""
아래 조건을 만족하는 수열을 찾기
1. 길이 2N
2. 앞에서 부터 2개 씩 묶었을 때 교집합이 존재
3. 2번에서 2값은 서로 달라야 함

스타 수열의 길이 최댓값

-------------------------------------
각 숫자들의 개수를 count 함
개수가 가장 많은 숫자부터 스타수열을 구하려는 시도를 함



[1, 2, 2, 2, 1, 3, 3, 3, 1]


"""