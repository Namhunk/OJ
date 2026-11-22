from collections import deque
import sys

m, n = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[True for _ in range(n)] for _ in range(m)]
for _ in range(m):
    arr.append(list(map(int, " ".join(sys.stdin.readline().strip()).split())))

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            visited[i][j] = False

for i in range(1):
    for j in range(n):
        if visited[i][j] and arr[i][j] == 0:
            que = deque()
            que.append((i, j))
            while que:
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if 0 <= x+k < m and visited[x+k][y] and arr[x+k][y] == 0:
                        visited[x+k][y] = False
                        que.append((x+k, y))
                    
                    if 0 <= y+k < n and visited[x][y+k] and arr[x][y+k] == 0:
                        visited[x][y+k] = False
                        que.append((x, y+k))
r = 0
for i in range(m-1, m):
    for j in range(n):
        if not visited[i][j] and not arr[i][j]: r = 1; break

print("NO" if not r else "YES")