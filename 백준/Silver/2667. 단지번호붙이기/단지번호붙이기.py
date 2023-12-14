from collections import deque
import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, " ".join(sys.stdin.readline().strip()).split())))

cnt = 0
size = []

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = 0
            cnt += 1
            s = 0
            que = deque()
            que.append((i, j))
            while que:
                s += 1
                x, y = que.popleft()
                for k in range(-1, 2, 2):
                    if 0 <= x+k < n and arr[x+k][y]:
                        arr[x+k][y] = 0
                        que.append((x+k, y))
                    
                    if 0 <= y+k < n and arr[x][y+k]:
                        arr[x][y+k] = 0
                        que.append((x, y+k))
            
            size.append(s)

print(cnt)
print(*sorted(size), sep= "\n")
