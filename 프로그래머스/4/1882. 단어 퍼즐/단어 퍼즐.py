def solution(strs, t):
    N = len(t)
    strs = set(strs)
    
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        for k in range(1, 6):  # 단어 최대 길이 5
            if i - k < 0:
                continue
            s = i - k
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[s] + 1)
    
    answer = -1 if dp[-1] == float('inf') else dp[-1]
    return answer