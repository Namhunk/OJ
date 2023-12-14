import sys

sys.setrecursionlimit(10**6)

dp = [[-1 for _ in range(100)] for _ in range(100)]
def jump(i, j):
    if dp[i][j] < 0:
        if i > n-1 or j > n-1:
            dp[i][j] = 0
        elif i == n-1 and j == n-1:
            dp[i][j] = 1
        else:
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = jump(i+arr[i][j], j) + jump(i, arr[i][j]+j)
    
    return dp[i][j]
    

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

print(jump(0, 0))