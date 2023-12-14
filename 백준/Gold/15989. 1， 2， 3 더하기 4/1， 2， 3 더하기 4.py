import sys

dp = [[0, 0, 0] for _ in range(10001)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [2, 0, 1]

for i in range(4, 10001):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-2][1] + dp[i-2][2]
    if i % 3 == 0: dp[i][2] = 1

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    print(sum(dp[n]))