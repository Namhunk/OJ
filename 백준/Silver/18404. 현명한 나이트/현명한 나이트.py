from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
x, y = map(int, sys.stdin.readline().strip().split())

arr = [[-1 for _ in range(n+1)] for _ in range(n+1)]
move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
your = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

arr[x][y] = 0
que = deque()
que.append((x, y))

while que:
    a, b = que.popleft()
    for r, c in move:
        if 0 < a+r <= n and 0 < b+c <= n and arr[a+r][b+c] < 0:
            arr[a+r][b+c] = arr[a][b] + 1
            que.append((a+r, b+c))

for r, c in your:
    print(arr[r][c], end=" ")