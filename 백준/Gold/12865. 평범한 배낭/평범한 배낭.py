import sys

# 물품의 수 = N, 배낭이 버틸 수 있는 무게 = K
N, K = map(int, sys.stdin.readline().strip().split())
# arr[i][0]에 물건의 무게 = W, arr[i][1]에 물건의 가치 = V 저장
arr = [[0, 0]] + [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = arr[i]
        # 만약 물건의 무게가 현재 배낭의 용량보다 무거우면
        if j < W:
            # 이전 가치 저장
            dp[i][j] = dp[i-1][j]
        # 물건의 무게가 현재 배낭의 무게 보다 가벼우면
        else:
            # 현재 가치 + 현재 무게 에서 물건의 무게를 뺀 곳의 가치
            # 또는 이전 물건의 가치 중 큰 것을 선택
            dp[i][j] = max(V+dp[i-1][j-W], dp[i-1][j])

# 최종값 출력
print(dp[N][K])