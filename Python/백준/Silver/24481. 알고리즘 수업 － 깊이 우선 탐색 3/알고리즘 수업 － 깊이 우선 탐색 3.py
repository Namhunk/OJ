import sys

sys.setrecursionlimit(10**6)

def dfs(r, cnt):
    visited[r] = cnt
    for i in sorted(graph[r]):
        if visited[i] < 0:
            dfs(i, cnt + 1)

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    
    graph[i].append(j)
    graph[j].append(i)

visited = [-1] * (n+1)

dfs(r, 0)

for i in visited[1:]:
    print(i)