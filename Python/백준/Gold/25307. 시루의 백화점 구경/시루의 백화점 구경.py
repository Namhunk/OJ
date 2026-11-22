from collections import deque
import sys

def bfs(sx, sy):
    visited[sx][sy] = 0
    que = deque([(sx, sy, 0)])
    while que:
        x, y, cnt = que.popleft()
        for r, c in move:
            if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c] < -1:
                if arr[x+r][y+c] == 2: return cnt+1
                visited[x+r][y+c] = -1
                que.append((x+r, y+c, cnt+1))
    return -1

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[-2]*m for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
que = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == -2: visited[i][j] = -1
        elif arr[i][j] == 3: visited[i][j] = 0; que.append((i, j))
        elif arr[i][j] == 4: sx, sy = i, j

while que:
    for _ in range(len(que)):
        x, y = que.popleft()
        for r, c in move:
            if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c] < 0 and visited[x][y] + 1 <= k:
                visited[x+r][y+c] = visited[x][y] + 1
                que.append((x+r, y+c))
                
print(bfs(sx, sy))