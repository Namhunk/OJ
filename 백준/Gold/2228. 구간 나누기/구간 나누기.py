import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [0] + [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [[0] + [-float('inf')]*m for _ in range(n+1)]
sum_arr = []
SUM = 0
for i in range(n+1):
    SUM += arr[i]
    sum_arr.append(SUM)

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, i+1):
            if k >= 2:
                dp[i][j] = max(dp[i][j], dp[k-2][j-1] + sum_arr[i] - sum_arr[k-1])
            
            elif j == 1:
                dp[i][j] = max(dp[i][j], sum_arr[i])
        
print(dp[n][m])