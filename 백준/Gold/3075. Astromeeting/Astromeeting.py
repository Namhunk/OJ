import sys, heapq

def floyd_warshall():
    for k in range(1, p+1):
        for x in range(1, p+1):
            for y in range(1, p+1):
                arr[x][y] = min(arr[x][y], arr[x][k] + arr[k][y])

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, p, q = map(int, sys.stdin.readline().strip().split())
    arr = [[float('inf')] * (p+1) for _ in range(p+1)]
    meet = []

    for x in range(1, p+1):
        for y in range(1, p+1):
            if x == y: arr[x][y] = 0

    for _ in range(n):
        meet.append(int(sys.stdin.readline().strip()))
    
    for _ in range(q):
        i, j, d = map(int, sys.stdin.readline().strip().split())
        arr[i][j] = min(arr[i][j], d)
        arr[j][i] = min(arr[i][j], d)
    
    floyd_warshall()
    ans1 = 0
    ans2 = float('inf')

    for y in range(1, p+1):
        cost = 0
        for x in meet:
            cost += (arr[x][y]**2)
        
        if cost < ans2:
            ans1 = y
            ans2 = cost

    
    print(ans1, ans2)
