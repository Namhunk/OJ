import sys

n, m = map(int, sys.stdin.readline().strip().split())
h = list(map(int, sys.stdin.readline().strip().split()))

arr = [0]*(n+1)
for i in range(m):
    a, b, k = map(int, sys.stdin.readline().strip().split())

    arr[a-1] += k
    arr[b] += -k

for i in range(n):
    arr[i+1] += arr[i]

for i in range(n):
    print(h[i] + arr[i], end=" ")