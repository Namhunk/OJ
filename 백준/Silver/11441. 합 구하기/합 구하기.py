import sys

n = int(sys.stdin.readline().strip())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
for i in range(1, n+1):
    arr[i] += arr[i-1]

m = int(sys.stdin.readline().strip())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().strip().split())
    print(arr[y] - arr[x-1])