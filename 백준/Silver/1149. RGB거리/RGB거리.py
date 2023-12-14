import sys

sys.setrecursionlimit(10**6)
dp = [[0 for _ in range(3)] for _ in range(1001)]
def color(i, j):
    if i > n: return 0
    if i <= 0:
        dp[i][j] = min(color(i+1, 0), color(i+1, 1), color(i+1, 2))
        return dp[i][j]
    else:
        if not dp[i][j]:
            if j == 0:
                dp[i][j] = min(arr[i][1] + color(i+1, 1), arr[i][2] + color(i+1, 2))
            if j == 1:
                dp[i][j] = min(arr[i][0] + color(i+1, 0), arr[i][2] + color(i+1, 2))
            if j == 2:
                dp[i][j] = min(arr[i][0] + color(i+1, 0), arr[i][1] + color(i+1, 1))
        
        return dp[i][j]


n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
arr = [[0] * 3] + arr

print(color(0, 0))