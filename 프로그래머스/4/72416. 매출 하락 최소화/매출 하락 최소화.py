import sys
INF = sys.maxsize
def solution(sales, links):
    N = len(sales)
    sales = [0] + sales
    graph = [[] for _ in range(N+1)]
    for a, b in links:
        graph[a].append(b)
    
    dp = [[0, 0] for _ in range(N+1)]
    
    def dfs(x):
        dp[x][0] = sales[x]
        if not graph[x]:
            return
        
        SUM = 0
        has_child = False
        extra = INF
        for nx in graph[x]:
            dfs(nx)
            
            if dp[nx][0] < dp[nx][1]:
                SUM += dp[nx][0]
                has_child = True
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

"""