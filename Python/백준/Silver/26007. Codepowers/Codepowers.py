import sys

n, m, k, x = map(int, sys.stdin.readline().strip().split())
arr = [x] + list(map(int, sys.stdin.readline().strip().split()))

ans = [0]*len(arr)
for i in range(1, n+1):
    arr[i] += arr[i-1]
    if arr[i] < k:
        ans[i] += 1
    
    ans[i] += ans[i-1]

for _ in range(m):
    l, r = map(int, sys.stdin.readline().strip().split())

    print(ans[r-1] - ans[l-1])
