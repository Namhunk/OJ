from collections import deque
import sys

arr, w, ans = [sys.stdin.readline().strip() for _ in range(8)], set(), 0
move = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for i in range(8):
    for j in range(8):
        if arr[i][j] == '#': w.add((i, j))

visited = set()

que = deque([(7, 0)])
while que and not ans:
    for _ in range(len(que)):
        x, y = que.popleft()
        if (x, y) in w: continue
        if x == 0 and y == 7: ans = 1; break

        for r, c in move:
            if 0 <= x+r < 8 and 0 <= y+c < 8 and not (x+r, y+c) in visited and not (x+r, y+c) in w:
                visited.add((x+r, y+c))
                que.append((x+r, y+c))
        
    if w: visited = set()
    n_w = set()

    for x, y in w:
        if x < 7:
            n_w.add((x+1, y))
        
    w = n_w

print(ans)