import sys

dp = [[0 for _ in range(1001)] for _ in range(51)]
def f(i, p):
    if i > n: return p
    if not dp[i][p]:
        dp[i][p] = -1
        
        if p + v[i] <= m:
            dp[i][p] = max(dp[i][p], f(i+1, p + v[i]))
        
        if p >= v[i]:
            dp[i][p] = max(dp[i][p], f(i+1, p - v[i]))
        
    return dp[i][p]


n, s, m = map(int, sys.stdin.readline().strip().split())
v = list(map(int, sys.stdin.readline().strip().split()))
v = [0] + v
print(f(0, s))