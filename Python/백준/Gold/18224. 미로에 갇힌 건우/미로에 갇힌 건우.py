from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[[[0]*m for _ in range(2)] for _ in range(n)] for _ in range(n)]
visited[0][0][0][0] = 1
if visited[n-1][n-1][0][0]: print(1, 'sun'); exit()
que = deque([(0, 0, 0, 0)])
while que:
    x, y, sky, cnt = que.popleft()
    for r, c in move:
        dx, dy = x+r, y+c

        if not sky:
            if cnt + 1 < m:
                if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy][sky][cnt + 1] and not arr[dx][dy]:
                    if (dx, dy) == (n-1, n-1): print(visited[x][y][sky][cnt], 'sun'); exit()
                    visited[dx][dy][sky][cnt + 1] = visited[x][y][sky][cnt]
                    que.append((dx, dy, sky, cnt + 1))
            else:
                if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy][1][0] and not arr[dx][dy]:
                    if (dx, dy) == (n-1, n-1): print(visited[x][y][sky][cnt], 'moon'); exit()
                    visited[dx][dy][1][0] = visited[x][y][sky][cnt]
                    que.append((dx, dy, 1, 0))
        else:
            while 0 <= dx < n and 0 <= dy < n and arr[dx][dy]:
                dx += r
                dy += c
            
            if cnt + 1 < m:
                if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy][sky][cnt + 1] and not arr[dx][dy]:
                    if (dx, dy) == (n-1, n-1): print(visited[x][y][sky][cnt], 'moon'); exit()
                    visited[dx][dy][sky][cnt + 1] = visited[x][y][sky][cnt]
                    que.append((dx, dy, sky, cnt + 1))
            else:
                if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy][0][0] and not arr[dx][dy]:
                    if (dx, dy) == (n-1, n-1): print(visited[x][y][sky][cnt] + 1, 'sun'); exit()
                    visited[dx][dy][0][0] = visited[x][y][sky][cnt] + 1
                    que.append((dx, dy, 0, 0))

print(-1)