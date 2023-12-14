import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
arr = [[float('inf')]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    arr[i][i] = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().strip().split())
    arr[A][B] = 1
    arr[B][A] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

ans, MIN = 0, float('inf')
for i in range(1, N+1):
    num = sum(arr[i][1:])
    if num < MIN:
        MIN = num
        ans = i

print(ans)