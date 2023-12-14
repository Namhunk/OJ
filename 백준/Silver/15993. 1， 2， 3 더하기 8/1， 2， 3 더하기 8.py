import sys

dp = [[0, 0] for _ in range(100001)]
dp[1] = [1, 0]
dp[2] = [1, 1]
dp[3] = [2, 2]

for i in range(4, 100001):
    if i % 2 == 0:
        dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][1]) % (10**9+9)
        dp[i][1] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][0]) % (10**9+9)
    else:
        dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % (10**9+9)
        dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % (10**9+9)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(*dp[n])
