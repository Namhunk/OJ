from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

melt = [[True]*m for _ in range(n)]
air, chese = deque([(0, 0)]), deque()

visited = [[True]*m for _ in range(n)]
air, chese = deque([(0, 0)]), deque()

ans = 0

while True:
    while air:
        x, y = air.popleft()
        if not arr[x][y]: visited[x][y] = False
        for r, c in udlr:
            if 0 <= x+r < n and 0 <= y+c < m and  not arr[x][y] and visited[x+r][y+c]:
                if not arr[x+r][y+c]:
                    visited[x+r][y+c] = False
                    air.append((x+r, y+c))
                else:
                    chese.append((x+r, y+c))
    
    if chese:
        ans += 1
        while chese:
            cnt = 0
            x, y = chese.popleft()
            for r, c in udlr:
                if 0 <= x+r < n and 0 <= y+c < m and arr[x][y] and  not arr[x+r][y+c] and not visited[x+r][y+c]:
                    cnt += 1
            
            if cnt >= 2:
                arr[x][y] = 0
                air.append((x, y))
    else: break
print(ans)