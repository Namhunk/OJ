def solution(sales, links):
    N = len(sales) # 전체 직원 수
    INF = float('inf')
    
    sales = [0] + sales # 직원 번호는 1번부터
    graph = [[] for _ in range(N+1)] # 각 팀장, 팀원의 관계
    for a, b in links:
        graph[a].append(b)
    
    dp = [[0, 0] for _ in range(N+1)] # 각 매출액 비용
    
    def dfs(x):
        dp[x][0] = sales[x] # 자신의 매출액
        if not graph[x]: # 자신이 밑에 팀원이 있는 경우만
            return
        
        SUM = 0 # 전체 합
        has_child = False
        extra = INF 
        for nx in graph[x]:
            dfs(nx) # 팀원의 비용을 구함
            
            if dp[nx][0] < dp[nx][1]:
                SUM += dp[nx][0]
                has_child = True # 팀원 포함
            else:
                SUM += dp[nx][1]
                extra = min(extra, dp[nx][0] - dp[nx][1])
                
        dp[x][0] = dp[x][0] + SUM # 현재 노드가 참석하는 경우 자식들의 자식이 참가
        
        if has_child:
            dp[x][1] = SUM
        else:
            dp[x][1] = SUM + extra
            
    dfs(1)
    return min(dp[1][0], dp[1][1])
        

"""
워크숍에 참석하는 직원들의 매출액 합의 최소

-------------------------------------------

- graph로 팀장, 팀원간의 관계를 표시
- dfs로 마지막 팀원 부터
- 팀에서 팀장 + 하위(팀장 or 팀원), 팀원
"""