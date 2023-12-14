import sys

n = int(sys.stdin.readline().strip())
dp = [0, 1]

for i in range(2, n+1):
    num = 1e9
    for j in range(1, int(i**0.5)+1):
        num = min(num, dp[i - j**2])
    
    dp.append(num+1)

print(dp[n])