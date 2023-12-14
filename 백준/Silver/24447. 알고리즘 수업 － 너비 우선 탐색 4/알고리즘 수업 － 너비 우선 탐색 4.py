from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n+1)
depth = [-1] * (n+1)

visited[r] = 1
depth[r] = 0

que = deque()
que.append(r)
cnt = 2

while que:
    v = que.popleft()
    for i in sorted(graph[v]):
        if not visited[i] and depth[i] < 0:
            visited[i] = cnt
            cnt += 1
            depth[i] = depth[v] + 1

            que.append(i)

s = 0
for i in range(1, n+1):
    s += (visited[i] * depth[i])

print(s)