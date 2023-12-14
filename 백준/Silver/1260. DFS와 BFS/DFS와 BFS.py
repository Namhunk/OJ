from collections import deque
import sys

def dfs(v):
    v_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if v_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    que = deque()
    que.append(v)
    v_bfs[v] = 1
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if v_bfs[i] == 0 and graph[v][i] == 1:
                que.append(i)
                v_bfs[i] = 1
    
n, m, v = map(int, sys.stdin.readline().strip().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    graph[i][j] = 1
    graph[j][i] = 1

v_dfs = [0] * (n+1)
v_bfs = [0] * (n+1)

dfs(v)
print()
bfs(v)
