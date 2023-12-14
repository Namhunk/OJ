import sys

n = int(sys.stdin.readline().strip())
tri = [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
tri = [[0]] + tri

dp = [[0 for _ in range(i)] for i in range(1, n+2)]
dp[1][1] = tri[1][1]

for i in range(1, n):
    for j in range(1, i+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + tri[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + tri[i+1][j+1])
    
print(max(dp[n]))
"""
0 0
0 7 = 1 / 
0 3 8 = 2
0 8 1 0 = 3
0 2 7 4 4 = 4
0 4 5 2 6 5 = 5

"""