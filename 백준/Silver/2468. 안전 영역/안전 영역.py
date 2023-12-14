from collections import deque
import sys

n = int(sys.stdin.readline().strip())
arr = []
m = 0
for _ in range(n):
    l = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(l)
    m = max(m, max(l))

max_cnt = 0
for i in range(m, -1, -1):
    visited = [[True for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] <= i: visited[x][y] = False
    
    cnt = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                cnt += 1
                que = deque()
                que.append((x, y))
                while que:
                    a, b = que.popleft()
                    for k in range(-1, 2, 2):
                        if 0 <= a+k < n and visited[a+k][b]:
                            visited[a+k][b] = False
                            que.append((a+k, b))
                        if 0 <= b+k < n and visited[a][b+k]:
                            visited[a][b+k] = False
                            que.append((a, b+k))
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)