import sys

n = int(sys.stdin.readline().strip())
dp = [0, 1, 2] + [0]*(n-2)
mod = 10007
for i in range(3, n+1):
    dp[i] = (dp[i-1] % mod + dp[i-2] % mod) % mod

print(dp[n])
