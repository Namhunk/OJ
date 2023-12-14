import sys

c = float(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr = [0] + arr
cnt = (c * 100) // 99


dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n+1)]

for i in range(1, n+1):
    if arr[i]:
        for j in range(3):
            dp[i][j][0] = dp[i-1][j][0] + 1
            dp[i][j][1] = max(dp[i-1][j][1], arr[i])
    
    else:
        for j in range(1, 3):
            if cnt >= j:
                dp[i][j][0] = dp[i-1][j-1][0] + 1
                dp[i][j][1] = dp[i-1][j-1][1]
ans, r = 0, 0
for i in range(1, n+1):
    for j in range(3):
        if ans <= dp[i][j][0]:
            ans = dp[i][j][0]
            r = max(r, dp[i][j][1])

print(ans)
print(r)
