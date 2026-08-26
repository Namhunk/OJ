from math import factorial

def solution(n, k):
    k -= 1  
    candidates = list(range(1, n+1))  # 아직 안 뽑은 숫자들
    answer = []
    
    for i in range(n):
        m = n - i - 1  # 이번 자리 뽑고 나서 남는 자리 수
        idx = k // factorial(m)   # 이번 자리에 candidates 중 몇 번째 걸 뽑을지
        k = k % factorial(m)      # k를 갱신
        
        answer.append(candidates[idx])  # 뽑은 숫자를 답에 추가
        candidates.pop(idx)             # 뽑은 숫자는 후보에서 제거
    
    return answer