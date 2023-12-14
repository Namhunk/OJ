import sys

n = int(sys.stdin.readline().strip())
boj = [i for i in sys.stdin.readline().strip()]
boj = [0] + boj

dp = [float('inf') for _ in range(n+1)]
dp[1] = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if boj[i] == "B" and boj[j] == "O":
            dp[j] = min(dp[j], (j-i)**2 + dp[i])

        elif boj[i] == "O" and boj[j] == "J":
            dp[j] = min(dp[j], (j-i)**2 + dp[i])

        elif boj[i] == "J" and boj[j] == "B":
            dp[j] = min(dp[j], (j-i)**2 + dp[i])
        
print(dp[n] if dp[n] != float('inf') else -1)