from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

cnt = 0
size = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            arr[i][j] = 0
            s = 0
            cnt += 1
            que = deque()
            que.append((i, j))
            while que:
                s += 1
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if 0 <= x+k < n and arr[x+k][y]:
                        arr[x+k][y] = 0
                        que.append((x+k, y))
                    if 0 <= y+k < m and arr[x][y+k]:
                        arr[x][y+k] = 0
                        que.append((x, y+k))
            
            size = max(size, s)

print(cnt, size, sep= "\n")