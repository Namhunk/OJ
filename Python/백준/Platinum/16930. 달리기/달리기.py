from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
sx, sy, ex, ey = map(lambda x: int(x)-1, sys.stdin.readline().strip().split())

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[-1]*m for _ in range(n)]
visited[sx][sy] = 0

que = deque([(sx, sy)])
while que:
    x, y = que.popleft()
    for r, c in move:
        if 0 <= x+r < n and 0 <= y+c < m:
            if visited[x+r][y+c] != -1 and visited[x+r][y+c] <= visited[x][y]: continue
        for mul in range(1, k+1):
            if 0 <= x+r*mul < n and 0 <= y+c*mul < m and visited[x+r*mul][y+c*mul] < 0:
                if (x+r*mul, y+c*mul) == (ex, ey): print(visited[x][y]+1); exit()
                if arr[x+r*mul][y+c*mul] == '#': break
                visited[x+r*mul][y+c*mul] = visited[x][y] +1 
                que.append((x+r*mul, y+c*mul))

print(-1)