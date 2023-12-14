from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [-1 for _ in range(n+1)]

que = deque()
que.append(r)
visited[r] = 0

while que:
    v = que.popleft()
    for i in sorted(graph[v]):
        if visited[i] < 0:
            visited[i] = visited[v] + 1
            que.append(i)

print(*visited[1:], sep= '\n')
