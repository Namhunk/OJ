from collections import deque
import sys

m, n = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
sx, sy, sd = map(int, sys.stdin.readline().strip().split())
ex, ey, ed = map(int, sys.stdin.readline().strip().split())
sx -= 1; sy -= 1; sd -= 1; ex -= 1; ey -= 1; ed -= 1

visited = [[[-1]*4 for _ in range(n)] for _ in range(m)]
directions = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
visited[sx][sy][sd] = 0

que = deque([(sx, sy, sd)])
while que:
    x, y, d = que.popleft()
    if (x, y, d) == (ex, ey, ed): break

    r1, c1 = directions[d]
    for k in range(1, 4):
        r, c = r1*k, c1*k
        if 0 <= x+r < m and 0 <= y+c < n:
            if arr[x+r][y+c]: break
            if visited[x+r][y+c][d] < 0:
                visited[x+r][y+c][d] = visited[x][y][d] + 1
                que.append((x+r, y+c, d))
    for i in range(4):
        r2, c2 = directions[i]
        if visited[x][y][i] < 0:
            visited[x][y][i] = visited[x][y][d] + max(abs(r2-r1), abs(c2-c1))
            que.append((x, y, i))

print(visited[ex][ey][ed])