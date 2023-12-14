from collections import deque
import sys

m, n, k = map(int, sys.stdin.readline().strip().split())
arr = [[1 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 0

cnt = 0
size = []

for i in range(m):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = 0
            cnt += 1
            s = 0
            que = deque()
            que.append((i, j))
            while que:
                s += 1
                x, y = que.popleft()
                for a in range(-1, 2, 2):
                    if 0 <= x+a < m and arr[x+a][y]:
                        arr[x+a][y] = 0
                        que.append((x+a, y))
                    if 0 <= y+a < n and arr[x][y+a]:
                        arr[x][y+a] = 0
                        que.append((x, y+a))
            size.append(s)

print(cnt)
print(*sorted(size))