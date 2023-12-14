from collections import deque
import sys

r, c = map(int, sys.stdin.readline().strip().split())
arr = [list(' '.join(sys.stdin.readline().strip()).split()) for _ in range(r)]
sx, sy = 0, 0
dx, dy = 0, 0

que = deque()
path = [[-1]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'D': dx, dy = i, j
        if arr[i][j] == 'S': sx, sy = i, j; path[i][j] = 0
        if arr[i][j] == '*': path[i][j] = 0; que.append((i, j))
        if arr[i][j] == 'X': path[i][j] = 0

que.append((sx, sy))

while que:
    x, y = que.popleft()
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x+i < r and 0 <= y+j < c and path[x+i][y+j] < 0:
            if arr[x][y] == '*' and arr[x+i][y+j] == '.':
                path[x+i][y+j] = 0
                arr[x+i][y+j] = '*'
                que.append((x+i, y+j))
            
            if arr[x][y] != '*':
                path[x+i][y+j] = path[x][y] + 1
                que.append((x+i, y+j))

print('KAKTUS' if path[dx][dy] < 0 else path[dx][dy])