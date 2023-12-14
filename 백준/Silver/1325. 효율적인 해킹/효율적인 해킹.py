from collections import deque
import sys

def bfs(v):
    com = [False] * (n)
    com[v-1] = True
    que = deque()
    que.append(v)
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not com[i-1]:
                com[i-1] = True
                que.append(i)

    return com.count(True)

n, m = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[j].append(i)

cnt = [0] * (n+1)
for i in range(1, n+1):
    cnt[i] = bfs(i)

for i in range(1, n+1):
    if cnt[i] == max(cnt):
        print(i, end=" ")