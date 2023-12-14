from collections import deque
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().strip().split())
    arr = [list(' '.join(sys.stdin.readline().strip().split())) for _ in range(h)]

    que_fires, que_sg = deque(), deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*': que_fires.append((i, j))
            if arr[i][j] == '@': que_sg.append((i, j))
    
    escape = False
    ans = 0
    while que_sg and (not escape):
        ans += 1

        if que_fires:
            for _ in range(len(que_fires)):
                x, y = que_fires.popleft()
                for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= x+r < h and 0 <= y+c < w and arr[x+r][y+c] == '.':
                        arr[x+r][y+c] = '*'
                        que_fires.append((x+r, y+c))
        
        if que_sg:
            for _ in range(len(que_sg)):
                x, y = que_sg.popleft()
                if (x in [0, h-1]) or (y in [0, w-1]):
                    escape = True
                    break

                for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= x+r < h and 0 <= y+c < w and arr[x+r][y+c] == '.':
                        arr[x+r][y+c] = '@'
                        que_sg.append((x+r, y+c))
                
                if escape: break
    
    print(ans if escape else 'IMPOSSIBLE')
    