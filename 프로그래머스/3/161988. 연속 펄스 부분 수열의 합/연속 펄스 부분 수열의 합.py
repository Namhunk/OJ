def solution(sequence):
    n = len(sequence)
    
    ans1 = f(1, sequence)
    ans2 = f(-1, sequence)

    answer = max(ans1, ans2)
    return answer

def f(sign, sequence):
    best = -float('inf')
    curr = 0
    
    for i in sequence:
        val = i * sign
        curr = max(val, curr+val)
        best = max(best, curr)
        sign *= -1
    
    return best
    
"""
1. 다음 값이 현재 까지의 합 보다 큰 경우

"""