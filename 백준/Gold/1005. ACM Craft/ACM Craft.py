import sys
from collections import deque

def Topological(W):
    que = deque()
    dp = [0] * (N+1)
    for i in range(1, N+1):
        if not indegree[i]:
            dp[i] = time[i]
            que.append(i)
    
    while que:
        now = que.popleft()
        if now == W: return dp[now]
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + time[i], dp[i])

            if not indegree[i]:
                que.append(i)
    
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())

    time = [0] + list(map(int, sys.stdin.readline().strip().split()))
    indegree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().strip().split())
        graph[X].append(Y)
        indegree[Y] += 1
    
    W = int(sys.stdin.readline().strip())
    print(Topological(W))