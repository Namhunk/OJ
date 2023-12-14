import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = []
    
    for _ in range(2):
        arr.append([0] + list(map(int, sys.stdin.readline().strip().split())))
    
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    for i in range(1, n+1):
        if i <= 1:
            dp[0][i] = arr[0][i]
            dp[1][i] = arr[1][i]
        
        else:
            dp[0][i] = arr[0][i] + max(dp[0][i-2], dp[1][i-2], dp[1][i-1])
            dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
    
    print(max(dp[0][n], dp[1][n]))