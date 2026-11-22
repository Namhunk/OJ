import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[[float('inf')]*3 for _ in range(m)] for _ in range(n)]

for y in range(n):
    if y == 0:
        for x in range(m):
            for z in range(3):
                dp[y][x][z] = arr[y][x]
    else:
        for x in range(m):
            if x == 0:
                dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + arr[y][x]
                dp[y][x][1] = dp[y-1][x][0] + arr[y][x]
            elif x == m-1:
                dp[y][x][1] = dp[y-1][x][2] + arr[y][x]
                dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + arr[y][x]
            else:
                dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + arr[y][x]
                dp[y][x][1] = min(dp[y-1][x][0], dp[y-1][x][2]) + arr[y][x]
                dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + arr[y][x]
r = float('inf')
for x in range(m):
    r = min(min(dp[n-1][x]), r)
print(r)
