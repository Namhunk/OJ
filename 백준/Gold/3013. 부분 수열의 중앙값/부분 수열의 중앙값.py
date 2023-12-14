import sys

n, b = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (2*10**5+1)
idx = arr.index(b)

cnt = 1
ans = 0

for i in range(idx, n):
    if arr[i] > b: cnt += 1
    else: cnt -= 1
    dp[10**5 + cnt] += 1

cnt = -1
for i in range(idx, -1, -1):
    if arr[i] > b: cnt -= 1
    else: cnt += 1
    ans += dp[10**5 + cnt]

print(ans)