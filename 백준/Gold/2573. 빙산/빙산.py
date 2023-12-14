from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
year = 0
while True:
    cnt = 0
    ice = deque()
    visited = [[True]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] and arr[i][j]:
                ice.append((i, j))
                cnt += 1
                visited[i][j] = False
                que = deque()
                que.append((i, j))
                while que:
                    x, y = que.popleft()
                    for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= x+r < n and 0 <= y+c < m and arr[x+r][y+c] and visited[x+r][y+c]:
                            visited[x+r][y+c] = False
                            que.append((x+r, y+c))
                            ice.append((x+r, y+c))

    if cnt != 1: break
    else:
        year += 1
        while ice:
            x, y = ice.popleft()
            for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c] and not arr[x+r][y+c] and arr[x][y]:
                    arr[x][y]  = arr[x][y] - 1

print(year if cnt != 0 else 0)