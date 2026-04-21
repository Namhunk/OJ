from math import comb
# 1 <= n <= 14
def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    
    answer = dp[n]
    return answer

"""
괄호 쌍의 개수 n이 주어질 때 n개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 개수

1. 시작은 무조건 열린 괄호, 끝은 닫힌 괄호의 형태

개수가 n일때 나올 수 있는 경우
가장 밖의 괄호 기준

(A) B
A: 첫 괄호 내부
B: 첫 괄호 외부

n = 1, 1
n = 2, 2

dp[2] = dp[0]*dp[1] + dp[1]*dp[0]
dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]

"""