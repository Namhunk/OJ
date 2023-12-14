import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
a = [0] + a

dp = [0] * (n+1)

for j in range(2, n+1):
    l = [float('inf')] * n
    for i in range(1, j):
        l[i] = max(dp[i], (j-i) * (1+abs(a[i]-a[j])))
    
    dp[j] = min(l)

print(dp[n])