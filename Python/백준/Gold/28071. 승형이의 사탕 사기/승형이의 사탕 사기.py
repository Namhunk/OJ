import sys

N, M, K = map(int, input().strip().split())
a = [0] + list(map(int, input().strip().split()))

dp = [float('inf')]*(300**2+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(a[i], 300**2+1):
        dp[j] = min(dp[j], dp[j-a[i]]+1)

ans = 0

for i in range(0, 300**2+1, K):
    if dp[i] <= M:
        ans = max(ans, i)

print(ans)