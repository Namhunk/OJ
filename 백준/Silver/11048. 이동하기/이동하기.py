import sys

n, m = map(int, sys.stdin.readline().strip().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + arr[i-1][j-1]
    
print(dp[n][m])