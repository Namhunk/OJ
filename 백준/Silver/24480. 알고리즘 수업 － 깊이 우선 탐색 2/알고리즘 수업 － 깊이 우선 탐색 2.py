import sys

n, m, r = map(int, sys.stdin.readline().strip().split())
graph = {i: [] for i in range(n+1)}

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n+1)
cnt = 1

stack = [r]
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = cnt
        cnt += 1
        for i in sorted(graph[v]):
            stack.append(i)

for i in visited[1:]:
    print(i)