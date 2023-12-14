import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    indegree[B] += 1
    graph[A].append(B)

finish = []
que = deque()
for i in range(1, N+1):
    if not indegree[i]:
        que.append(i)
        finish.append(i)

while que:
    now = que.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        
        if not indegree[i]:
            que.append(i)
            finish.append(i)

print(*finish)