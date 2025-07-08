import sys
sys.setrecursionlimit(10**6)
# 호텔의 고객을 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값을 구해라

# 고객의 최소 수 C (1 <= C <= 1,000), 도시의 개수 N (1 <= N <= 20)
C, N = map(int, input().strip().split())

# 각 도시에서 홍보할 때 대는 비용, 그 비용으로 얻을 수 있는 고객의 수 (1 <= data[i][0], data[i][1] <= 100)
data = [[0, 0]]+[list(map(int, input().strip().split())) for _ in range(N)]
# 비용, 고객수 적은 순으로 정렬
data.sort()

dp = [float('inf') for _ in range(C+100)]
dp[0] = 0

for i in range(1, N+1):
    cost = data[i][0]
    cnt = data[i][1]

    for j in range(cnt, C+100):
        dp[j] = min(dp[j], dp[j-cnt]+cost)

print(min(dp[C:]))