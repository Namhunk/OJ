import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = arr[i][2]
    
    elif i == 1:
        dp[i] = max(arr[i][2], dp[i-1])
    
    else:
        dp[i] = max(dp[i-2] + arr[i][2], dp[i-1])

print(dp[n-1])