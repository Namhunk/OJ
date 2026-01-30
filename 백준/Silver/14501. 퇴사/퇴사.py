import sys
input = sys.stdin.readline

"""
N일 동안 최대한 많은 상담을 한다
기간 T, 금액 P
상담을 적절히 했을 때, 얻을 수 있는 최대 수익

T[i] - i
"""
N = int(input().strip())
arr = [[0, 0]] + [list(map(int, input().strip().split())) for _ in range(N)]
dp = [0]*(N+1)

for i in range(1, N+1):
    ni = arr[i][0] + i - 1
    if ni > N:
        dp[i] = max(dp[i], dp[i-1])
    else:
        dp[ni] = max(dp[ni], arr[i][1] + dp[i-1])
    
    dp[i] = max(dp[i], dp[i-1])

print(dp[-1])