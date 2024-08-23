import sys
input = sys.stdin.readline

# 아래의 규칙을 만족해야함
# 1. 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# 2. N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# 3. i(2 <= i <= N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다

# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력

# 집의 수 N(2 <= N < = 1,000)
N = int(input().strip())

# N개의 줄에 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 집의 순서대로 주어짐 비용은 1,000 보다 작거나 같은 자연수
color = [list(map(int, input().strip().split())) for _ in range(N)]

# 첫집의 색깔을 정해두고 마지막과 다른지만 비교
# 나머지 경우는 이전 집과 다른색을 더해나가서 최소를 구함

INF = sys.maxsize
ans = INF
for i in range(3):
    dp = [[INF]*3 for _ in range(N)]
    dp[0][i] = color[0][i] # 첫 집의 색깔 지정

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2])+color[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2])+color[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1])+color[j][2]

    dp[-1][i] = INF
    ans = min(ans, min(dp[-1]))

print(ans)