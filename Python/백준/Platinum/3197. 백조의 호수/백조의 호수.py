from collections import deque
import sys

def find_water():
    while water:
        x, y = water.popleft()
        arr[x][y] = '.'
        for r, c in move:
            if 0 <= x+r < n and 0 <= y+c < m and w_idx[x+r][y+c]:
                if arr[x+r][y+c] == '.': water.append((x+r, y+c))
                else: tmp_water.append((x+r, y+c))
                
                w_idx[x+r][y+c] = False

def find_swan():
    while swan:
        x, y = swan.popleft()
        if (x, y) == (ex, ey): return True
        
        for r, c in move:
            if 0 <= x+r < n and 0 <= y+c < m and s_idx[x+r][y+c]:
                if arr[x+r][y+c] == '.': swan.append((x+r, y+c))
                else: tmp_swan.append((x+r, y+c))

                s_idx[x+r][y+c] = False
    return False

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

w_idx = [[True]*m for _ in range(n)]
s_idx = [[True]*m for _ in range(n)]

water, tmp_water = deque(), deque()
swan, tmp_swan = deque(), deque()

ex, ey, ans = 0, 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            if not swan:
                swan.append((i, j))
                s_idx[i][j] = False
            else:
                ex, ey = i, j
            
            arr[i][j] = '.'
        
        if arr[i][j] == '.':
            water.append((i, j))
            w_idx[i][j] = False

while True:
    find_water()
    if find_swan(): break
    
    water = tmp_water
    swan = tmp_swan

    tmp_water = deque()
    tmp_swan = deque()
    ans += 1

print(ans)