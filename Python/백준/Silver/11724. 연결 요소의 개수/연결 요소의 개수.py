import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: arr[y] = x
    elif x > y: arr[x] = y

n, m = map(int, sys.stdin.readline().strip().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    union(u, v)

cnt = 0
for i in range(1, n+1):
    if arr[i] == i: cnt += 1

print(cnt)