from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
Map = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    Map.append(arr)

    if 2 in arr:
        start = (i, arr.index(2))

distance = [[-1 for _ in range(m)] for _ in range(n)]
que = deque()
que.append(start)
distance[start[0]][start[1]] = 0

for i in range(n):
    for j in range(m):
        if Map[i][j] == 0:
            distance[i][j] = 0

while que:
    i, j = que.popleft()
    for k in range(-1, 2, 2):
        if 0 <= i+k < n and distance[i+k][j] == -1:
            if Map[i+k][j] == 1:
                distance[i+k][j] = distance[i][j] + 1
                que.append((i+k, j))
        
        if 0 <= j+k < m and distance[i][j+k] == -1:
            if Map[i][j+k] == 1:
                distance[i][j+k] = distance[i][j] + 1
                que.append((i, j+k))

for i in distance:
    print(*i)
