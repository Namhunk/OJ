import sys

n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))
p = [0] + p
dp = [0 for _ in range(1001)]
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j] + dp[i-j])

print(dp[n])