import sys
from collections import deque

N = int(sys.stdin.readline().strip())

indegreee = [0] * (N+1)
graph = [[] for _ in range(N+1)]

dp = [0] * (N+1)
time = [0]
for i in range(1, N+1):
    task = list(map(int, sys.stdin.readline().strip().split()))
    time.append(task[0])
    
    for node in task[2: ]:
        graph[node].append(i)
        indegreee[i] += 1

que = deque()
for i in range(1, N+1):
    if not indegreee[i]:
        que.append(i)
        dp[i] = time[i]

while que:
    now = que.popleft()
    for i in graph[now]:
        indegreee[i] -= 1
        dp[i] = max(dp[now] + time[i], dp[i])
        if not indegreee[i]:
            que.append(i)

print(max(dp))