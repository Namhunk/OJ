import sys

N = int(sys.stdin.readline().strip())
dp = [0 for i in range(N+1)]

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if not i % 2 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
    
    if not i % 3 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[N])
"""
주어진 숫자를 1로 만드는 연산의 최소 횟수
dp에 각 숫자에 해당하는 제일 빠른 연산을 저장
연산을 수행 했을때 dp에 있는 숫자가 나온다면 리턴
"""