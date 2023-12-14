from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().strip().split())
arr = [[list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)] for _ in range(h)]
visited = [[[True] * m for _ in range(n)] for _ in range(h)]

que = deque()
for a in range(h):
    for b in range(n):
        for c in range(m):
            if arr[a][b][c] == -1:
                visited[a][b][c] = False
            
            if arr[a][b][c] == 1:
                visited[a][b][c] = False
                que.append((a, b, c))

while que:
    z, x, y = que.popleft()
    for k in range(-1, 2, 2):
        if 0 <= z+k < h and visited[z+k][x][y] and arr[z+k][x][y] == 0:
            visited[z+k][x][y] = False
            arr[z+k][x][y] = arr[z][x][y] + 1
            que.append((z+k, x, y))

        if 0 <= x+k < n and visited[z][x+k][y] and arr[z][x+k][y] == 0:
            visited[z][x+k][y] = False
            arr[z][x+k][y] = arr[z][x][y] + 1
            que.append((z, x+k, y))

        if 0 <= y+k < m and visited[z][x][y+k] and arr[z][x][y+k] == 0:
            visited[z][x][y+k] = False
            arr[z][x][y+k] = arr[z][x][y] + 1
            que.append((z, x, y+k))

cnt = 0
for i in arr:
    for j in i:
        if 0 in j:
            cnt = -1
            break
        cnt = max(cnt, max(j)-1)
    
    if cnt < 0:
        break


print(cnt)