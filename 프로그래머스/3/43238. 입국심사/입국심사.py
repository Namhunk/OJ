# 1 <= n <= 1,000,000,000
# 
def solution(n, times):
    l, r = 0, max(times) * n
    answer = r
    while l < r:
        m = (l + r) // 2
        
        curr = 0
        for t in times:
            curr += m // t
        
        if curr < n:
            l = m+1
        else:
            r = m
    
    answer = min(answer, l)
    return answer

"""
각 심사관 마다
각 n명을 검사할 때 최소 시간


"""