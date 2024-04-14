import sys

N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]

# dp[0][i][j] = 가로, dp[1][i][j] = 대각, dp[2][i][j] = 세로
dp[0][0][1] = 1
for i in range(2, N):
    if arr[0][i] == 0: dp[0][0][i] = dp[0][0][i-1]

for i in range(1, N):
    for j in range(1, N):
        if not arr[i][j] and not arr[i-1][j] and not arr[i][j-1]:
            dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

        if not arr[i][j]:
            dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]
            dp[2][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

print(sum(dp[i][N-1][N-1] for i in range(3)))