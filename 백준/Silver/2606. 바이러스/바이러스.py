import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: arr[y] = x
    elif x > y: arr[x] = y

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

arr = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    union(a, b)

cnt = 0
for i in range(2, N+1):
    if find(i) == 1: cnt += 1

print(cnt)