from collections import deque
import sys

n = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())

graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

depth = [-1] * (n+1)
depth[p1] = 0

que = deque()
que.append(p1)

while que:
    v = que.popleft()
    for i in sorted(graph[v]):
        if depth[i] < 0:
            depth[i] = depth[v] + 1
            que.append(i)

print(depth[p2])