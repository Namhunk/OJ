import sys
sys.setrecursionlimit(10**6)
# 호텔의 고객을 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값을 구해라

# 고객의 최소 수 C (1 <= C <= 1,000), 도시의 개수 N (1 <= N <= 20)
C, N = map(int, input().strip().split())

# 각 도시에서 홍보할 때 대는 비용, 그 비용으로 얻을 수 있는 고객의 수 (1 <= data[i][0], data[i][1] <= 100)
data = [[0, 0]]+[list(map(int, input().strip().split())) for _ in range(N)]
# 비용, 고객수 적은 순으로 정렬
data.sort()

# 값을 저장할 DP 배열
dp = [[float('inf')]*(C+1) for _ in range(N+1)]

for i in range(1, N+1):
    cost = data[i][0] # 각 data[i]의 비용, 고객 수
    cnt = data[i][1]

    for j in range(1, C+1):
        dp[i][j] = dp[i-1][j] # 이전 행의 최소값

        k = 0 # 해당 비용을 몇 번 사용 하는지
        while 1:
            if j-k*cnt <= 0: # 고객의 수가 현재 j값을 넘는다면 비용의 최소 비교
                dp[i][j] = min(dp[i][j], k*cost)
                break
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-k*cnt]+k*cost)

            k+=1

print(dp[N][-1])