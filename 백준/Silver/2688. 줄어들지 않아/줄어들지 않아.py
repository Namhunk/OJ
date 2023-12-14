import sys

dp = [[0 for _ in range(10)] for _ in range(65)]
for i in range(1, 65):
    if i <= 1:
        for j in range(10):
            dp[i][j] = 1

    else:
        dp[i][0] = sum(dp[i-1])
        for j in range(1, 10):
            dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(sum(dp[n]))