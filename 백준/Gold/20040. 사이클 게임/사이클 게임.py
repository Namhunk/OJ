import sys

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        if x < y: arr[y] = arr[x]
        elif x > y: arr[x] = arr[y]
        return False
    else:
        return True
    
n, m = map(int, sys.stdin.readline().strip().split())
arr = [i for i in range(n)]

for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    if union(a, b):
        print(i)
        exit()
else:
    print(0)