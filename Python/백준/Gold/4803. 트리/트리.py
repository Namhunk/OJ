import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    
    if x < y: arr[y] = x
    elif x > y: arr[x] = y
    else:
        arr[x], arr[y] = 0, 0

t = 0
while True:
    t += 1
    n, m = map(int, sys.stdin.readline().strip().split())
    if not n and not m: break
    
    arr = [i for i in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        union(a, b)
    
    cnt = set()
    for i in range(1, n+1):
        p = find(arr[i])
        
        if p and p not in cnt:
            cnt.add(arr[i])
    
    if len(cnt) <= 0: print(f'Case {t}: No trees.')
    elif len(cnt) <= 1: print(f'Case {t}: There is one tree.')
    else: print(f'Case {t}: A forest of {len(cnt)} trees.')