from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(" ".join(sys.stdin.readline().strip()).split()) for _ in range(n)]
path = [[0]*m for _ in range(n)]
io = []
for i in range(n):
    if i == 0 or i == n-1:
        for j in range(m):
            if arr[i][j] == '.': io.append((i, j))
    else:
        if arr[i][0] == '.': io.append((i, 0))
        if arr[i][m-1] == '.': io.append((i, m-1))

que = deque()
que.append(io[0])
path[io[0][0]][io[0][1]] = 1
while que:
    x, y = que.popleft()
    for k in range(-1, 2, 2):
        if 0 <= x+k < n and arr[x+k][y] == '.' and not path[x+k][y]:
            path[x+k][y] = path[x][y] + 1
            que.append((x+k, y))

        if 0 <= y+k < m and arr[x][y+k] == '.' and not path[x][y+k]:
            path[x][y+k] = path[x][y] + 1
            que.append((x, y+k))

visited = [[True]*m for _ in range(n)]
visited[io[1][0]][io[1][1]] = False
q = deque()
q.append(io[1])
while q:
    x, y = q.popleft()
    for k in range(-1, 2, 2):
        if 0 <= x+k < n and 0 < path[x+k][y] < path[x][y] and visited[x+k][y]:
            visited[x+k][y] = False
            q.append((x+k, y))
        if 0 <= y+k < m and 0 < path[x][y+k] < path[x][y] and visited[x][y+k]:
            visited[x][y+k] = False
            q.append((x, y+k))
for i in range(n):
    for j in range(m):
        if visited[i][j] and arr[i][j] == '.':
            arr[i][j] = '@'

for i in arr:
    print(''.join(i))