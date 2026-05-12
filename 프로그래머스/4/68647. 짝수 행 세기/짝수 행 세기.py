MOD = 10**7 + 19
def solution(a):
    MOD = 10000019
    R, C = len(a), len(a[0])

    # 각 열의 1 개수
    cnt = [0] * C
    for i in range(R):
        for j in range(C):
            cnt[j] += a[i][j]

    # 조합 미리 계산
    comb = [[0] * (R + 1) for _ in range(R + 1)]
    for n in range(R + 1):
        comb[n][0] = comb[n][n] = 1
        for k in range(1, n):
            comb[n][k] = (comb[n - 1][k - 1] + comb[n - 1][k]) % MOD

    # dp[e] = 현재 짝수 행이 e개인 경우의 수
    dp = [0] * (R + 1)
    dp[R] = 1  # 아직 아무 열도 처리하지 않았으니 모든 행은 합 0 -> 짝수

    for ones in cnt:
        ndp = [0] * (R + 1)

        for e in range(R + 1):
            if dp[e] == 0:
                continue

            # x = 짝수 행에 놓는 1의 개수
            lo = max(0, ones - (R - e))
            hi = min(e, ones)

            for x in range(lo, hi + 1):
                ne = e + ones - 2 * x
                ways = comb[e][x] * comb[R - e][ones - x]
                ndp[ne] = (ndp[ne] + dp[e] * ways) % MOD

        dp = ndp

    return dp[R]
