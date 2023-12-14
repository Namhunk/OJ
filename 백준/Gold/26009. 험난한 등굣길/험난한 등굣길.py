from collections import deque
import sys

def bfs(i, j):
    visited[i][j] = 0
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c] < 0:
                visited[x+r][y+c] = visited[x][y] + 1
                que.append((x+r, y+c))
                if (x+r, y+c) == (n-1, m-1): return visited[x+r][y+c]
    return 0

n, m = map(int, sys.stdin.readline().strip().split())
k = int(sys.stdin.readline().strip())
tp = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]

visited = [[-1]*m for _ in range(n)]
for ri, ci, di in tp:
    r = ri-1; c = ci -1
    que= deque()
    for i in range(-1, 2, 2):
        for d in range(di+1):
            if 0 <= r + (i*d) < n and visited[r+(i*d)][c] < 0:
                visited[r+(i*d)][c] = float('inf')
                que.append((r+(i*d), c))
            if 0 <= c+(i*d) < m and visited[r][c+(i*d)] < 0:
                visited[r][c+(i*d)] = float('inf') 
                que.append((r, c+(i*d)))
    while que:
        x, y = que.popleft()
        for i in range(-1, 2, 2):
            if 0 <= x+i < n and abs(x+i - r) + abs(y - c) <= d and visited[x+i][y] < 0:
                visited[x+i][y] = float('inf')
                que.append((x+i, y))
            
            if 0 <= y+i < m and abs(x - r) + abs(y+i - c) <= d and visited[x][y+i] < 0:
                visited[x][y+i] = float('inf')
                que.append((x, y+i))
if bfs(0, 0):
    print("YES")
    print(visited[n-1][m-1])
else:
    print("NO")