import sys, heapq

N, M, T = map(int, sys.stdin.readline().strip().split())
arr = [[float('inf')] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: arr[i][j] = 0

for _ in range(M):
    u, v, h = map(int, sys.stdin.readline().strip().split())
    arr[u][v] = h

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], max(arr[i][k], arr[k][j]))

for _ in range(T):
    s, e = map(int, sys.stdin.readline().strip().split())
    print(arr[s][e] if arr[s][e] != float('inf') else -1)