from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
dic = {(i, j): [] for i in range(1, n+1) for j in range(1, n+1)}
for _ in range(m):
    x, y, a, b = map(int, sys.stdin.readline().strip().split())
    dic[(x, y)].append((a, b))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[0]*2 for _ in range(n+1)] for _ in range(n+1)]
visited[1][1] = [1, 1]

ans = 1
que = deque([(1, 1)])
while que:
    x, y = que.popleft()
    for a, b in dic[(x, y)]:
        if not visited[a][b][1]:
            visited[a][b][1] = 1
            ans += 1
            for r, c in move:
                if 0 < a+r <= n and 0 < b+c <= n and visited[a+r][b+c][0]:
                    que.append((a+r, b+c))

    for r, c in move:
        if 0 < x+r <= n and 0 < y+c <= n and not visited[x+r][y+c][0] and visited[x+r][y+c][1]:
            que.append((x+r, y+c))
            visited[x+r][y+c][0] = 1

print(ans)