from collections import deque
import sys

h, w = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(h)]
move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

visited = [[0]*w for _ in range(h)]
que = deque()
for i in range(h):
    for j in range(w):
        if arr[i][j] == '.':
            visited[i][j] = 1
            que.append((i, j))

ans = 0
while que:
    ans += 1
    for _ in range(len(que)):
        x, y = que.popleft()
        for r, c in move:
            if 0 <= x+r < h and 0 <= y+c < w and arr[x+r][y+c] != '.':
                visited[x+r][y+c] += 1

                if int(arr[x+r][y+c]) <= visited[x+r][y+c]:
                    arr[x+r][y+c] = '.'
                    que.append((x+r, y+c))

print(ans-1)