import sys
input = sys.stdin.readline

# 필요한 메모리 M 바이트를 확보하기 위한 앱 비활성화의 최소 비용을 계산하여 한 줄에 출력

# N, M (1 <= N <= 100, 1 <= M <= 10,000,000)
N, M = map(int, input().strip().split())
# N개의 앱 m (1 <= m[i] <= 10,000,000)
m = [0] + list(map(int, input().strip().split()))
# 각 앱을 비활성화 했을 경우의 비용 c(0 <= c[i] <= 100
c = [0] + list(map(int, input().strip().split()))

# c[i]의 합이 최소를 가지며, m[i]의 합이 M 이상 이어야 함
# 배낭 문제로 접근
# 비용 -> 무게, 메모리 -> 가치
MAX = 10001 # c의 최대 비용의 합 + 1
dp = [[0]*MAX for _ in range(N+1)]
# j 비용일때 최대의 메모리를 구하기
for i in range(1, N+1):
    for j in range(MAX):
        if c[i] > j: # i번째 앱의 비용이 j 보다 큰 경우
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]] + m[i])

for j in range(MAX):
    if dp[N][j] >= M: # 만약 j의 비용일떄 메모리가 M이상 이라면
        print(j)
        exit()