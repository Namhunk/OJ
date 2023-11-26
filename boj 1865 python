import sys

# 벨만_포드를 사용하여 음수의 순환이 존재하는지 구한다.
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
    
    # 벨만_포드 실행
    for _ in range(n-1):
        for s, e, t in edges:
            if arr[e] > arr[s] + t:
                arr[e] = arr[s] + t
    
    # 한번 더 실행해서 음수 사이클 존재 여부 판단
    for s, e, t in edges:
        if arr[e] > arr[s] + t:
            print('YES')
            break
    
    else:
        print('NO')
