# 1 <= n <= 100,000
# 1 <= len(money) <= 100
def solution(n, money):
    money.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    MOD = 1_000_000_007
    for coin in money:
        for i in range(coin, n+1):
            dp[i] = (dp[i] + dp[i-coin]) % MOD
    
    answer = dp[n]
    return answer

"""
거스름돈 n원을 줄 때 방법의 경우의 수
거스름돈의 재고는 무한

예제
n = 5, money = [1, 2, 5]

1. 1원 5개
2. 1원 3개, 2원 1개
3. 1원 1개, 2원 2개
4. 5원 1개
-------------------
1. money[i] <= n
2. DP로 이전 경우를 모두 구함

n = 5, [1, 2, 5]

dp[0] = 1
dp[1] = 0 + 1 + 
"""