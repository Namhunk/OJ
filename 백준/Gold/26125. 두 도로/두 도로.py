import sys, heapq

N, M, S, T = map(int, sys.stdin.readline().strip().split())
arr = [[float('inf')] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: arr[i][j] = 0

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    arr[u][v] = min(arr[u][v], w)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

Q = int(sys.stdin.readline().strip())
for _ in range(Q):
    a1, b1, c1, a2, b2, c2 = map(int, sys.stdin.readline().strip().split())
    ans = min(arr[S][T],
              arr[S][a1] + c1 + arr[b1][T], 
              arr[S][a2] + c2 + arr[b2][T],
              arr[S][a1] + c1 + arr[b1][a2] + c2 + arr[b2][T],
              arr[S][a2] + c2 + arr[b2][a1] + c1 + arr[b1][T])
    
    print(ans if ans != float('inf') else -1)