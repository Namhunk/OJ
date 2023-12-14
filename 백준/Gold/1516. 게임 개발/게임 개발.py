import sys
from collections import deque

def topological():
    dp = [0] * (N+1)
    que = deque()

    for i in range(1, N+1):
        if not indegree[i]:
            dp[i] = time[i]
            que.append(i)
    
    while que:
        now = que.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + time[i], dp[i])

            if not indegree[i]:
                que.append(i)
    
    return dp

N = int(sys.stdin.readline().strip())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [0]

for i in range(1, N+1):
    data = list(map(int, sys.stdin.readline().strip().split()))
    
    time.append(data[0])
    for j in data[1:len(data)-1]:
        graph[j].append(i)
        indegree[i] += 1

ans = topological()
for i in ans[1:]:
    print(i)