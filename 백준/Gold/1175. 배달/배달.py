from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
move = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
visited = [[[[-1]*4 for _ in range(4)] for _ in range(m)] for _ in range(n)]

dic = {}
sx, sy = -1, -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S': sx, sy = i, j
        if arr[i][j] == 'C': dic[(i, j)] = len(dic)

p = set()
visited[sx][sy][0] = [0]*4
que = deque([(sx, sy, 0, -1)])
while que:
    x, y, cnt, b = que.popleft()
    for i in range(4):
        r, c  = move[i]

        if 0 <= x+r < n and 0 <= y+c < m and arr[x+r][y+c] != '#' and i != b:
            if arr[x+r][y+c] == 'C':
                if cnt & (1 << dic[(x+r, y+c)]):
                    if visited[x+r][y+c][cnt][i] < 0:
                        visited[x+r][y+c][cnt][i] = visited[x][y][cnt][b] + 1
                        que.append(((x+r, y+c, cnt, i)))
                else:
                    if cnt + (1 << dic[(x+r, y+c)]) == 3: print(visited[x][y][cnt][b] + 1); exit()
                    if visited[x+r][y+c][cnt + (1 << dic[(x+r, y+c)])][i] < 0:
                        visited[x+r][y+c][cnt + (1 << dic[(x+r, y+c)])][i] = visited[x][y][cnt][b] + 1
                        que.append((x+r, y+c, cnt + (1 << dic[(x+r, y+c)]), i))
            else:
                if visited[x+r][y+c][cnt][i] < 0:
                    visited[x+r][y+c][cnt][i] = visited[x][y][cnt][b] + 1
                    que.append((x+r, y+c, cnt, i))

print(-1)