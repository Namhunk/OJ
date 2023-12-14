from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0 for _ in range(n+1)]
cnt = 1
que = deque()
que.append(r)

while que:
    v = que.popleft()
    if not visited[v]:
        visited[v] = cnt
        cnt += 1
        for i in sorted(graph[v]):
            que.append(i)

for i in visited[1:]:
    print(i)