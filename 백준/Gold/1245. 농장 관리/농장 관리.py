from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] > 0 and visited[i][j]:
            top = 1
            visited[i][j] = False
            que = deque()
            que.append((i, j))
            while que:
                x, y = que.popleft()
                for r, c in move:
                    if 0 <= x+r < n and 0 <= y+c < m:
                        if arr[x][y] < arr[x+r][y+c]:
                            top = 0
                        if visited[x+r][y+c] and arr[x][y] == arr[x+r][y+c]:
                            visited[x+r][y+c] = False
                            que.append((x+r, y+c))
            
            if top:
                cnt += 1

print(cnt)