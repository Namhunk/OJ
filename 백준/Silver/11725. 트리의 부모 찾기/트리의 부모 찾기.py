from collections import deque
import sys

n = int(sys.stdin.readline().strip())
graph = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i].append(j)
    graph[j].append(i)

tree = [-1] * (n+1)
tree[1] = 0
que = deque()
que.append(1)
while que:
    node = que.popleft()
    for i in graph[node]:
        if tree[i] < 0:
            tree[i] = node
            que.append(i)

print(*tree[2:], sep= '\n')
