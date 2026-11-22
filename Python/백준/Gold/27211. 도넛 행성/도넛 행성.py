from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[True]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]: visited[i][j] = False

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            visited[i][j] = False
            cnt += 1
            que = deque()
            que.append((i, j))
            while que:
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if visited[(x+k+n)%n][y]:
                        visited[(x+k+n)%n][y] = False
                        que.append(((x+k+n)%n, y))
                    
                    if visited[x][(y+k+m)%m]:
                        visited[x][(y+k+m)%m] = False
                        que.append((x, (y+k+m)%m))

print(cnt)