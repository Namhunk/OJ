import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
for idx in range(1, n+1):
    arr[idx] += arr[idx-1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(arr[j] - arr[i-1])