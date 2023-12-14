from collections import deque
import sys

arr = [[-1]*9 for _ in range(10)]
visited = [[True]*9 for _ in range(10)]

r1, c1 = map(int, sys.stdin.readline().strip().split())
r2, c2 = map(int, sys.stdin.readline().strip().split())
move = [(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)]
arr[r1][c1] = 0
visited[r1][c1] = False
que = deque()
que.append((r1, c1))

while que:
    x, y = que.popleft()
    for r, c in move:
        if 0 <= x+r < 10 and 0 <= y+c < 9 and visited[x+r][y+c]:
            tf = 1
            if r < 0 and c < 0:
                for i in range(1, 3):
                    if (r2, c2) == (x+r+i, y+c+i): tf = 0; break
            
            elif r > 0 and c < 0:
                for i in range(1, 3):
                    if (r2, c2) == (x+r-i, y+c+i): tf = 0; break
            
            elif r > 0 and c > 0:
                for i in range(1, 3):
                    if (r2, c2) == (x+r-i, y+c-i): tf = 0; break
            
            elif r < 0 and c > 0:
                for i in range(1, 3):
                    if (r2, c2) == (x+r+i, y+c-i): tf = 0; break
            
            if tf:
                visited[x+r][y+c] = False
                arr[x+r][y+c] = arr[x][y] + 1
                que.append((x+r, y+c))

print(arr[r2][c2])