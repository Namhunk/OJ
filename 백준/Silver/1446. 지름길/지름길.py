import sys

n, d = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
arr = [[0, 0, 0]] + arr
arr.sort()

dp = [i for i in range(10001)]
for i in range(1, n+1):
    if arr[i][1] <= d:
        dp[arr[i][1]] = min(dp[arr[i][0]] + arr[i][2], dp[arr[i][1]])

        for j in range(arr[i][0], d+1):
            dp[j] = min(dp[j-1] + 1, dp[j])

print(dp[d])