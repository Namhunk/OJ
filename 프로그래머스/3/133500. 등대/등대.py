import sys
sys.setrecursionlimit(10**7)

def solution(n, lighthouse):
    global visit, graph, dp
    graph = [[] for _ in range(n+1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    dp = [[0, 0] for _ in range(n+1)] # 0: 끈 경우, 1: 킨 경우
    visit = [False] * (n+1)
    dfs(1)
    
    answer = min(dp[1][0], dp[1][1])
    return answer

def dfs(x):
    global visit
    visit[x] = True
    
    dp[x][1] = 1
    dp[x][0] = 0
    
    for nx in graph[x]:
        if visit[nx]: continue
        dfs(nx)
        
        dp[x][0] += dp[nx][1]
        dp[x][1] += min(dp[nx][0], dp[nx][1])
    
    