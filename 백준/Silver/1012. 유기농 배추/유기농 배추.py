from collections import deque
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    ground = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[True for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        ground[y][x] = 1
    
    s = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                visited[i][j] = False
                if ground[i][j] == 1:
                    que = deque()
                    que.append((i, j))
                    s += 1
                    while que:
                        x, y = que.popleft()
                        for k in range(-1, 2, 2):
                            if 0 <= x+k < n and visited[x+k][y] and ground[x+k][y] == 1:
                                visited[x+k][y] = False
                                que.append((x+k, y))
                            
                            if 0 <= y+k < m and visited[x][y+k] and ground[x][y+k] == 1:
                                visited[x][y+k] = False
                                que.append((x, y+k))
    
    print(s)