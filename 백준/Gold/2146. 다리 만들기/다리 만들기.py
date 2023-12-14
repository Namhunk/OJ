from collections import deque
import sys

def land_cnt(i, j):
    global cnt
    que = deque([(i, j)])
    visited[i][j] = False
    arr[i][j] = cnt

    while que:
        x, y = que.popleft()
        for r, c in udlr:
            if 0 <= x+r < n and 0 <= y+c < n and arr[x+r][y+c] and visited[x+r][y+c]:
                visited[x+r][y+c] = False
                arr[x+r][y+c] = cnt
                que.append((x+r, y+c))

def distance(num):
    global ans
    dist = [[-1]*n for _ in range(n)]
    que = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                que.append((i, j))
                dist[i][j] = 0

    while que:
        x, y = que.popleft()
        for r, c in udlr:
            if 0 <= x+r < n and 0 <= y+c < n:
                if arr[x+r][y+c] and arr[x+r][y+c] != num:
                    ans = min(ans, dist[x][y])
                    return

                if not arr[x+r][y+c] and dist[x+r][y+c] < 0:
                    dist[x+r][y+c] =  dist[x][y] + 1
                    que.append((x+r, y+c))


n = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[True]*n for _ in range(n)]
cnt = 0
ans = float('inf')

for i in range(n):
    for j in range(n):
        if visited[i][j] and arr[i][j]:
            cnt += 1
            land_cnt(i, j)

for i in range(1, cnt):
    distance(i)

print(ans)