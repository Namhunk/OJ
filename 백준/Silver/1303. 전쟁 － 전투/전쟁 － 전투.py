from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[True for _ in range(n)] for _ in range(m)]
for _ in range(m):
    arr.append(list(" ".join(sys.stdin.readline().strip()).split()))

W, B = 0, 0
for i in range(m):
    for j in range(n):
        if visited[i][j]:
            visited[i][j] = False
            cnt = 0
            que = deque()
            que.append((i, j))
            while que:
                cnt += 1
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if 0 <= x+k < m and visited[x+k][y]:
                        if arr[x+k][y] == arr[i][j]:
                            visited[x+k][y] = False
                            que.append((x+k, y))
                        
                    if 0 <= y+k < n and visited[x][y+k]:
                        if arr[x][y+k] == arr[i][j]:
                            visited[x][y+k] = False
                            que.append((x, y+k))
            
            if arr[i][j] == 'W': W += cnt**2
            else: B += cnt**2

print(W, B)