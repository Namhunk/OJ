from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
before = [list(map(int, sys.stdin.readline().strip().strip().split())) for _ in range(n)]
after = [list(map(int, sys.stdin.readline().strip().strip().split())) for _ in range(n)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

check = False
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            data = before[i][j]
            before[i][j] = after[i][j]

            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for r, c in move:
                    if 0 <= x+r < n and 0 <= y+c < m:
                        if before[x+r][y+c] == data:
                            before[x+r][y+c] = before[x][y]
                            que.append((x+r, y+c))
            
            check = True
            break
    
    if check: break

print("YES" if before == after else "NO")