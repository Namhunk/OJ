from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
Map = [list(" ".join(sys.stdin.readline().strip()).split()) for _ in range(n)]
arr = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'L':
            visited = [[True]*m for _ in range(n)]
            visited[i][j] = False
            t = [[0] * m for _ in range(n)]
            cnt = 0
            que = deque()
            que.append((i, j))
            while que:
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if 0 <= x+k < n and visited[x+k][y] and Map[x+k][y] == 'L':
                        t[x+k][y] = t[x][y] + 1
                        visited[x+k][y] = False
                        que.append((x+k, y))
                    
                    if 0 <= y+k < m and visited[x][y+k] and Map[x][y+k] == 'L':
                        t[x][y+k] = t[x][y] + 1
                        visited[x][y+k] = False
                        que.append((x, y+k))
                
            
            arr[i][j] = t[x][y]

num = 0
for i in arr:
    num = max(num, max(i))

print(num)