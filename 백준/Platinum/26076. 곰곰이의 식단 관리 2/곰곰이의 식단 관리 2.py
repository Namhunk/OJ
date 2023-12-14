from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

visited = [[float('inf')]*m for _ in range(n)]
que = deque()
for j in range(1, m):
    if arr[0][j]:
        visited[0][j] = 0
        que.appendleft((0, j))
    
    else:
        visited[0][j] = 1
        que.append((0, j))

for i in range(1, n-1):
    if arr[i][m-1]:
        visited[i][m-1] = 0
        que.appendleft((i, m-1))
    
    else:
        visited[i][m-1] = 1
        que.append((i, m-1))

ans = 2
while que:
    x, y = que.popleft()

    for r, c in move:
        if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c] == float('inf'):
            visited[x+r][y+c] = visited[x][y] + (arr[x+r][y+c]^1)

            if arr[x+r][y+c]:
                que.appendleft((x+r, y+c))
            
            else:
                que.append((x+r, y+c))

for i in range(1, n):
    ans = min(ans, visited[i][0])

for j in range(1, m-1):
    ans = min(ans, visited[n-1][j])

print(ans)