from collections import deque
import sys

m, n = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[True] * m for _ in range(n)]

que = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            visited[i][j] = False
        
        if arr[i][j] == 1:
            visited[i][j] = False
            que.append((i, j))

while que:
    x, y = que.popleft()
    for k in range(-1, 2, 2):
        if 0 <= x+k < n and visited[x+k][y]:
            visited[x+k][y] = False
            arr[x+k][y] = arr[x][y] + 1
            que.append((x+k, y))
        if 0 <= y+k < m and visited[x][y+k]:
            visited[x][y+k] = False
            arr[x][y+k] = arr[x][y] + 1
            que.append((x, y+k))
cnt = 0
for i in arr:
    if 0 in i:
        cnt = -1
        break

    cnt = max(cnt, max(i))

print(cnt if cnt < 0 else cnt -1)