from collections import deque
import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    i, j = map(int, sys.stdin.readline().strip().split())
    arr[i-1][j-1] = 1

size = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            arr[i][j] = 0
            s = 0
            que = deque()
            que.append((i, j))
            while que:
                s += 1
                x, y = que.popleft()
                for a in range(-1, 2, 2):
                    if 0 <= x+a < n and arr[x+a][y]:
                        arr[x+a][y] = 0
                        que.append((x+a, y))
                    
                    if 0 <= y+a < m and arr[x][y+a]:
                        arr[x][y+a] = 0
                        que.append((x, y+a))
            size = max(size, s)

print(size)