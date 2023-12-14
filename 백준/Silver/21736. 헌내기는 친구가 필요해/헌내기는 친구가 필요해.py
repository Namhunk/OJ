import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
arr = []
visited = [[True]*m for _ in range(n)]
now = [0, 0]

for i in range(n):
    row = list(sys.stdin.readline().strip())
    arr.append(row)
    if 'I' in row:
        for j in range(m):
            if row[j] == 'I': 
                now[0], now[1] = i, j
                visited[i][j] = False

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
que = deque([now])

ans = 0
while que:
    x, y = que.popleft()
    
    for r, c in move:
        if 0 <= x+r < n and 0 <= y+c < m and visited[x+r][y+c]:
            if arr[x+r][y+c] != 'X':
                visited[x+r][y+c] = False
                if arr[x+r][y+c] == 'P': ans += 1
                que.append((x+r, y+c))

print('TT' if not ans else ans)