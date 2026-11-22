import sys
from collections import deque

n = int(sys.stdin.readline().strip())

rank = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
max_rank = 0
time = [0]
dp = [0] * (n+1)

for i in range(1, n+1):
    r, t = map(int, sys.stdin.readline().strip().split())

    rank[r].append(i)
    time.append(t)
    max_rank = max(max_rank, r)

for i in range(2, max_rank+1):
    for j in rank[i-1]:
        for k in rank[i]:
            graph[j].append(k)
            indegree[k] += 1

que = deque()
for i in rank[1]:
    que.append(i)
    dp[i] = time[i]

while que:
    now = que.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + time[i] + (now-i)**2, dp[i])

        if not indegree[i]:
            que.append(i)

print(max(dp))
