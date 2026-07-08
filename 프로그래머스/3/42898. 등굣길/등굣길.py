# 1 <= m, n <= 100 (1 != m and 1 != n)
# 0 <= len(puddles) <= 10

def solution(m, n, puddles):
    MOD = 1_000_000_007
    
    puddles = set((x, y) for x, y in puddles)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if x == 1 and y == 1:
                continue

            # 물웅덩이 처리
            if (x, y) in puddles:
                dp[y][x] = 0
                continue

            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD

    return dp[n][m]

'''
m x n 맵
가장 왼쪽 위는 (1, 1)
오른쪽과 아래쪽으로만 움직여 집에서 학교로 갈 수 있는 최단 경로의 수


'''