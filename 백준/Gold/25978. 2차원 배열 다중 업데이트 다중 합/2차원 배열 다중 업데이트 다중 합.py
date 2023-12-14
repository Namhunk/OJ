from collections import deque
import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [[0]*(n+2)] + [[0] + list(map(int, sys.stdin.readline().strip().split())) + [0] for _ in range(n)] + [[0]*(n+2)]
plus = [[0]*(n+2) for _ in range(n+2)]

que = deque()
    
for _ in range(m):
    query = list(map(int, sys.stdin.readline().strip().split()))
    if query[0] == 2: que.append(query)
    else:
        q, i1, j1, i2, j2, k = query
        i1 += 1; j1 += 1; i2 += 1; j2 += 1
        plus[i1][j1] += k
        plus[i2+1][j2+1] += k
        plus[i1][j2+1] -= k
        plus[i2+1][j1] -= k

for i in range(1, n+1):
    for j in range(1, n+1):
        plus[i][j] += plus[i-1][j] + plus[i][j-1] - plus[i-1][j-1]
        arr[i][j] += plus[i][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

for _ in range(len(que)):
    q, i1, j1, i2, j2 = que.popleft()
    print(arr[i2+1][j2+1] - arr[i1][j2+1] - arr[i2+1][j1] + arr[i1][j1])