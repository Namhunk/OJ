# 1 <= len(strs) <= 100
# 1 <= t <= 20,000
def solution(strs, t):
    answer = 0
    n = len(t)
    size = 5
    
    strs = set(strs)
    
    INF = float('inf')
    dp = [INF] * (n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for l in range(1, min(size, i)+1):
            if dp[i-l] == INF: continue
            
            if t[i-l: i] in strs:
                dp[i] = min(dp[i], dp[i-l]+1)
    
    answer = dp[n] if dp[n] != INF else -1
    return answer

'''
1. 단어조각 strs, 완성 문장 t가 주어짐
2. 단어 조각으로 t를 만들기 위해 사용해야하는 단어조각 개수의 최솟값
3. 같은 조각을 k번 사용하거나 다른조각을 사용
4. 모든 조각의 길이는 1 ~ 5
-----------------------------------------------------------------

'''