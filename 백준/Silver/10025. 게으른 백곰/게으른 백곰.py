import sys

arr = [0]*(10**6 + 1)
n, k = map(int, sys.stdin.readline().strip().split())
for _ in range(n):
    g, x = map(int, sys.stdin.readline().strip().split())
    arr[x-k if x-k > 0 else 1] += g
    arr[x+k+1 if x+k+1 < len(arr) else 10**6] -= g

ans = 0
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
    ans = max(ans, arr[i])

print(ans)