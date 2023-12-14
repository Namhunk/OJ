import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    for j in range(m):
        if arr[i][j]:
            if j == 0:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % (10**9 + 7)
            elif j == m-1:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % (10**9 + 7)
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % (10**9 + 7)

print(sum(dp[n-1]) % (10**9 + 7))