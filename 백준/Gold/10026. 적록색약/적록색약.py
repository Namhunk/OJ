from collections import deque
import sys

n = int(sys.stdin.readline().strip())
arr = [list(" ".join(sys.stdin.readline().strip()).split()) for _ in range(n)]
v1, v2 =[[True] * n for _ in range(n)], [[True] * n for _ in range(n)]
cnt1, cnt2 = 0, 0
for i in range(n):
    for j in range(n):
        if v1[i][j]:
            v1[i][j] = False
            cnt1 += 1
            que = deque()
            que.append((i, j))
            while que:
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if 0 <= x+k < n and v1[x+k][y] and arr[x][y] == arr[x+k][y]:
                        v1[x+k][y] = False
                        que.append((x+k, y))
                    if 0 <= y+k < n and v1[x][y+k] and arr[x][y] == arr[x][y+k]:
                        v1[x][y+k] = False
                        que.append((x, y+k))
        
        if v2[i][j]:
            v2[i][j] = False
            cnt2 += 1
            que = deque()
            que.append((i, j))
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                while que:
                    x, y = que.popleft()
                    for k in range(-1, 2, 2):
                        if 0 <= x+k < n and v2[x+k][y]:
                            if arr[x+k][y] == 'R' or arr[x+k][y] == 'G':
                                v2[x+k][y] = False
                                que.append((x+k, y))
                        
                        if 0 <= y+k < n and v2[x][y+k]:
                            if arr[x][y+k] == 'R' or arr[x][y+k] == 'G':
                                v2[x][y+k] = False
                                que.append((x, y+k))
            
            else:
                while que:
                    x, y = que.popleft()
                    for k in range(-1, 2, 2):
                        if 0 <= x+k < n and v2[x+k][y] and arr[x][y] == arr[x+k][y]:
                            v2[x+k][y] = False
                            que.append((x+k, y))
                        
                        if 0 <= y+k < n and v2[x][y+k] and arr[x][y] == arr[x][y+k]:
                            v2[x][y+k] = False
                            que.append((x, y+k))

print(cnt1, cnt2)