import sys

dp = [0] * 10001

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr = [0] + arr
for i in range(1, n+1):
    if i < 3:
        dp[i] = max(arr[i-1], arr[i-1] + arr[i])
    
    else:
        dp[i] = max(dp[i-1], dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

print(dp[n])
