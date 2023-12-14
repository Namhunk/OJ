import sys

sys.setrecursionlimit(10**7)
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x > y: parents[x] = y
    else: parents[y] = x

N, M = map(int, sys.stdin.readline().strip().split())
parents = [i for i in range(N+1)]

for _ in range(M):
    q, a, b = map(int, sys.stdin.readline().strip().split())
    
    if not q: union(a, b)
    else: print('YES' if  find(a) == find(b) else 'NO')