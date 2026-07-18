def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0 # 최대 alp, cop 요구 값 탐색
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    INF = float('inf')
    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    
    answer = dp[max_alp][max_cop]
    return answer

'''
알고력, 코딩력을 얻는 최단시간을 return

problems = [alp_req, cop_req, alp_rwd, cop_rwd, cost]

----------------------------------------------------------
1. 1의 시간을 사용해 alp를 +1 올린다
2. 1의 시간을 사용해 cop를 +1 올린다
3. cost의 시간을 사용해 alp_rwd, cop_rwd 만큼 올린다

'''