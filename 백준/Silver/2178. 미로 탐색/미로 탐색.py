from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, " ".join(sys.stdin.readline().strip()).split())))

visited = [[True for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not miro[i][j]:
            visited[i][j] = False
que = deque()
que.append((0, 0))
visited[0][0] = False
while que:
    i, j = que.popleft()
    for k in range(-1, 2, 2):
        if 0 <= i+k < n and visited[i+k][j]:
            visited[i+k][j] = False
            miro[i+k][j] = miro[i][j] + 1
            que.append((i+k, j))
        
        if 0 <= j+k < m and visited[i][j+k]:
            visited[i][j+k] = False
            miro[i][j+k] = miro[i][j] + 1
            que.append((i, j+k))

print(miro[-1][-1])