import sys
input = sys.stdin.readline

def solve():
    # 수의 길이 N (1 <= N <= 1,000)
    N = int(input().strip())
    dp = [[0]*10 for _ in range(N+1)] # 행은 수의 최대 길이, 열은 각 숫자의 개수
    
    mod = 10_007
    
    # N = 1
    dp[1][0] = 1
    for i in range(1, 10): 
        dp[1][i] = dp[1][i-1] + 1
    
    # N >= 2 일때
    for i in range(2, N+1):
        for j in range(1, 10):
            dp[i][j] = (dp[i][j-1] + (dp[i-1][-1] - dp[i-1][j-1]))
    
    ans = 0
    for i in range(N+1):
        ans = (ans + dp[i][-1]) % mod
    
    print(ans)

if __name__ == '__main__':
    solve()

"""
수의 길이가 N일때 오르막의 개수

N = 1 -> 10
0 - 9 = 10

N = 2 -> 45
11 - 19 = 9 
22 - 29 = 8
33 - 39 = 7
44 - 49 = 6
55 - 59 = 5
66 - 69 = 4
77 - 79 = 3
88 - 89 = 2
99      = 1

N = 3 ->  165
1 = 45
2 = 36
3 = 28
4 = 21
5 = 15
6 = 10
7 = 6
8 = 3
9 = 1

"""