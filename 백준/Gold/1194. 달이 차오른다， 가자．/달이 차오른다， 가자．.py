from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[[-1]*(2**6) for _ in range(m)] for _ in range(n)]
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

sx, sy = -1, -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0': sx, sy = i, j; break

visited[sx][sy][0] = 0
que = deque([(sx, sy, 0)])
while que:
    x, y, keys = que.popleft()
    for r, c in move:
        if 0 <= x+r < n and 0 <= y+c < m and arr[x+r][y+c] != '#' and visited[x+r][y+c][keys] < 0:
            if arr[x+r][y+c] == '1': print(visited[x][y][keys] + 1); exit()

            elif arr[x+r][y+c] in 'abcdef':
                if keys & (1 << dic[arr[x+r][y+c].upper()]):
                    visited[x+r][y+c][keys] = visited[x][y][keys] + 1
                    que.append((x+r, y+c, keys))
                else:
                    visited[x+r][y+c][keys + (1 << dic[arr[x+r][y+c].upper()])] = visited[x][y][keys] + 1
                    que.append((x+r, y+c, keys + (1 << dic[arr[x+r][y+c].upper()])))
            
            elif arr[x+r][y+c] in 'ABCDEF':
                if keys & (1 << dic[arr[x+r][y+c]]):
                    visited[x+r][y+c][keys] = visited[x][y][keys] + 1
                    que.append((x+r, y+c, keys))
            
            else:
                visited[x+r][y+c][keys] = visited[x][y][keys] + 1
                que.append((x+r, y+c, keys))

print(-1)