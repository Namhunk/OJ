import sys, heapq

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

arr = [[float('inf')]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: arr[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    arr[a][b] = min(arr[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j] if arr[i][j] != float('inf') else 0, end= " ")
    
    print()