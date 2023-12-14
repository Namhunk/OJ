import sys

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr = [0] + arr

dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i < 3:
        dp[i] = max(arr[i], dp[i-1], arr[i-1] + arr[i]//2)
    
    else:
        dp[i] = max(dp[i-1],dp[i-2] + arr[i],dp[i-3] + arr[i-1] + arr[i]//2)

print(dp[n])