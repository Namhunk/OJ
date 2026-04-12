import sys
input = sys.stdin.readline

def solve(N):
    P = []
    # P[i] (-10,000 <= P[i] <= 10,000)
    for _ in range(N):
        P.append(int(input().strip()))
    
    dp = [0] * N
    dp[0] = P[0]
    
    # 점화식을 통해 dp 배열 채우기
    for i in range(1, N):
        dp[i] = max(dp[i-1] + P[i], P[i])
        
    # 구간이 어디서 끝나든 상관없으므로, 끝나는 지점들 중 가장 큰 값이 정답
    print(max(dp))

if __name__ == '__main__':
    while 1:
        N = int(input().strip())
        if N <= 0: break
        solve(N)

"""
각 N일에 대한 수익 P가 주어졌을 때 가장 많은 수익을 올린 구간의 수익을 출력
가장 많이 수익을 올린 구간은 연속된 날의 값이어야 함

"""