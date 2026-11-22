from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
hx, hy = map(int, sys.stdin.readline().strip().split())
ex, ey = map(int, sys.stdin.readline().strip().split())
hx -= 1; hy -= 1; ex -= 1; ey -= 1

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]

que = deque([(hx, hy, 0)])
visited[hx][hy][0] = 0

while que:
    x, y, w = que.popleft()
    if x == ex and y == ey: break
    for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x+r < n and 0 <= y+c < m:
            if not arr[x+r][y+c] and visited[x+r][y+c][w] < 0:
                visited[x+r][y+c][w] = visited[x][y][w] + 1
                que.append((x+r, y+c, w))
            
            elif arr[x+r][y+c] and visited[x+r][y+c][w] < 0 and not w:
                visited[x+r][y+c][w+1]  = visited[x][y][w] + 1
                que.append((x+r, y+c, w+1))

print(min(visited[ex][ey]) if -1 not in visited[ex][ey] else max(visited[ex][ey]))