import sys
input = sys.stdin.readline

# 1: 기계오리가 작동한 전력량의 종류의 수, 2: 전력량들을 공백을 사이에 두고 오름차순 출력

# 배터리의 개수 N (1 <= N <= 500), 배터리의 최대 개수 K (1 <= K <= min(N, 100))
N, K = map(int, input().strip().split())

# 배터리의 전력량 I (1 <= I[i] <= 500)
I = [0] + list(map(int, input().strip().split()))

dp = [float('inf')]*(100*500+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(100*500-I[i], -1, -1):
        dp[j+I[i]] = min(dp[j+I[i]], dp[j]+1)

ans = []
for i in range(1, 500*100+1):
    if dp[i] <= K:
        ans.append(i)

print(len(ans))
print(*ans)
"""

"""