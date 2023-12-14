import sys

dp = [[0 for _ in range(11)] for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
for i in range(2, 101):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] % (10**9)
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % (10**9)

n = int(sys.stdin.readline().strip())
print(sum(dp[n]) % (10**9))