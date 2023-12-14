import sys

tc = int(sys.stdin.readline().strip())
for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().strip().split())
    
    arr = [1e9]*(n+1)
    arr[1] = 0
    edges = []

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().strip().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().strip().split())
        edges.append((s,e,-t))
    
    for _ in range(n):
        for s, e, t in edges:
            if arr[e] > arr[s] + t:
                arr[e] = arr[s] + t
    
    for s, e, t in edges:
        if arr[e] > arr[s] + t:
            print('YES')
            break
    
    else:
        print('NO')