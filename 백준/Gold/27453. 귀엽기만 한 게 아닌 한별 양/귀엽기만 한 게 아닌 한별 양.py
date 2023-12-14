from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
move = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
sx, sy, hx, hy = -1, -1, -1, -1

visited = [[[True]*4 for _ in range(m)] for _ in range(n)]
ngt = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S': sx, sy = i, j; ngt[i][j] = 0
        if arr[i][j] == 'H': hx, hy = i, j; ngt[i][j] = 0

        if arr[i][j].isnumeric(): ngt[i][j] = int(arr[i][j])

que = deque([(sx, sy, sx, sy, 0)])
tf = 0
while que and not tf:
    x, y, bx, by, cnt = que.popleft()
    for i in range(4):
        r, c = move[i]
        
        if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c][i] and ngt[x+r][y+c] != -1 and (bx, by) != (x+r, y+c):
            if (x+r, y+c) == (hx, hy): print(cnt + 1); exit()

            sum = ngt[bx][by] + ngt[x][y] + ngt[x+r][y+c]

            if sum <= k:
                visited[x+r][y+c][i] = False
                que.append((x+r, y+c, x, y, cnt + 1))

print(-1)