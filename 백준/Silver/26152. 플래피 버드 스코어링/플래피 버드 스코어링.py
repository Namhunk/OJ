import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))
h = [0]* n

for i in range(n):
    h[i] = a[i] - b[i]

for i in range(1, n):
    if h[i] > h[i-1]: h[i] = h[i-1]

for i in range(n):
    h[i] *= -1

q = int(sys.stdin.readline().strip())
w = list(map(int, sys.stdin.readline().strip().split()))

for size in w:
    size *= -1
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2

        if size >= h[mid]: low = mid + 1
        else: high = mid 
    
    print(low)
