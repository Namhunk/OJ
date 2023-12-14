import sys

sys.setrecursionlimit(10**6)
def dfs(r, cnt):
    depth[r] = cnt
    for i in sorted(graph[r]):
        if depth[i] < 0:
            dfs(i, cnt + 1)

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n+1)
depth = [-1] * (n+1)
cnt = 1
dfs(r, 0)

stack = [r]
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = cnt
        cnt += 1
        for i in sorted(graph[v], reverse= True):
            stack.append(i)

ans = 0
for i in range(1, n+1):
    ans += (visited[i] * depth[i])

print(ans)