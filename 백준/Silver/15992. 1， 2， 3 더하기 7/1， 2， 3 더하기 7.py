import sys

dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1] = [0, 1, 0, 0] + [0] * 997
dp[2] = [0, 1, 1, 0] + [0] * 997
dp[3] = [0, 1, 2, 1] + [0] * 997

for i in range(4, 1001):
    for j in range(2, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % (10**9 + 9)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(dp[n][m] % (10**9 + 9))
