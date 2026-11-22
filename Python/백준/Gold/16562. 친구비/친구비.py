import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    
    if cost[x] < cost[y]: arr[y] = arr[x]
    else: arr[x] = arr[y]

n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [i for i in range(n+1)]
cost = [0] + list(map(int, sys.stdin.readline().strip().split()))

for _ in range(m):
    v, w = map(int, sys.stdin.readline().strip().split())
    union(v, w)

ans = 0
for i in range(1, n+1):
    if arr[i] == i: ans += cost[i]

print(ans if k-ans >= 0 else "Oh no")