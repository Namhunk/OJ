import sys

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

dp = [0] * (N)
for i in range(N):
    if i < 1: dp[i] = arr[i]
    elif i == 1: dp[i] = max(dp[i-1] + arr[i], arr[i])
    elif i == 2: dp[i] = max(dp[i-2] + arr[i], arr[i-1] + arr[i])
    else: dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(dp[N-1])
