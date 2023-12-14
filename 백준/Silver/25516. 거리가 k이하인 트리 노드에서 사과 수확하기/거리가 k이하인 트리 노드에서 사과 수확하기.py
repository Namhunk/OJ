from collections import deque
import sys

n, k = map(int, sys.stdin.readline().strip().split())
graph = {i:[] for i in range(n)}
for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

apple = list(map(int, sys.stdin.readline().strip().split()))
depth = [-1] * n
depth[0] = 0
que = deque()
que.append(0)

s = apple[0]
while que:
    v = que.popleft()
    for i in graph[v]:
        if depth[v] + 1 > k:
            que.clear()
            break

        else:
            if depth[i] < 0:
                depth[i] = depth[v] + 1
                que.append(i)
                s += apple[i]

print(s)