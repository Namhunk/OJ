import sys
input = sys.stdin.readline

# i번 롤러코스터를 k번째로 탔을 때 느끼는 재미는
# f(i, k) = ai - (k-1)**2 * bi

# 각 시간 T에 대해 상근이가 느낄 수 있는 최대 재미 점수 출력

# N (0 < N <= 100)
N = int(input().strip())

size = 25_000
item0 = [] # b값이 0이라 무한히 탈 수 있는 경우
item = [] # b != 0 인 경우

for _ in range(N):
    a, b, t = map(int, input().strip().split())

    if b == 0: # 재미가 줄어들지 않는 경우
        item0.append((a, t))
    else: # 줄어드는 경우
        k = 1
        while 1:
            fun = a - (k - 1)**2 * b

            if fun <= 0: break

            item.append((fun, t)) # 모든 감소하는 값들 추가
            k += 1

MAX_T = 25_000
dp = [0]*(MAX_T + 1)

for fun, cost in item: # 재미가 줄어드는 롤러코스터
    for j in range(MAX_T, cost-1, -1): # 모든 시간대에 대해
        if dp[j-cost] + fun > dp[j]: # 이전 시간대 + cost 가 현재 보다 크다면
            dp[j] = dp[j-cost] + fun

for fun, cost in item0: # 재미가 줄어들지 않는 롤러코스터
    for j in range(cost, MAX_T+1):
        if dp[j-cost] + fun > dp[j]:
            dp[j] = dp[j-cost] + fun

for i in range(1, MAX_T + 1):
        if dp[i-1] > dp[i]:
            dp[i] = dp[i-1]

ans = []
Q = int(input().strip())
for _ in range(Q):
    T = int(input().strip())
    print(dp[T])