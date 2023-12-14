import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    guest = list(map(int, sys.stdin.readline().strip().split()))
    
    for i in range(2, len(guest)):
        indegree[guest[i]] += 1
        graph[guest[i-1]].append(guest[i])

que = deque()
ans = []
for i in range(1, N+1):
    if not indegree[i]:
        que.append(i)
        ans.append(i)

while que:
    now = que.popleft()
    
    for i in graph[now]:
        indegree[i] -= 1
        
        if not indegree[i]:
            que.append(i)
            ans.append(i)

if len(ans) != N: print(0)
else:
    for i in ans:
        print(i)