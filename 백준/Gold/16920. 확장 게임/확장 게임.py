from collections import deque
import sys

n, m, p = map(int, sys.stdin.readline().strip().split())
s = [0] + list(map(int, sys.stdin.readline().strip().split()))
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = [0] * 10
dic = {i: deque() for i in range(1, p+1)}
for i in range(n):
    for j in range(m):
        if arr[i][j].isnumeric():
            ans[int(arr[i][j])] += 1
            dic[int(arr[i][j])].append((i, j))

while True:
    cnt = 0
    for k in range(1, 1+p):
        for _ in range(s[k]):
            if not dic[k]: break
            
            for _ in range(len(dic[k])):
                x, y = dic[k].popleft()

                for r, c in move:
                    if not(0 <= x+r < n and 0 <= y+c < m and arr[x+r][y+c] == '.'): continue
                    dic[k].append((x+r, y+c))
                    arr[x+r][y+c] = arr[x][y]
                    ans[k] += 1
                    cnt = 1
    
    if not cnt: break

print(*list(filter(lambda x : x > 0, ans)))