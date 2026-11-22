import sys
input = sys.stdin.readline

# 그 그림을 소유 했던 사람들 (잠시라도 소유했던 사람도 포함)의 최대값을 출력

# 모든 그림의 거래는 아래의 조건을 만족해야 함
# 1. 그림을 팔 때, 그림을 산 가격보다 크거나 같은 가격으로 팔아야 한다
# 2. 같은 그림을 두 번 이상 사는 것은 불가능 하다

# 예술가의 수 N (2 <= N <= 15)
N = int(input().strip())

# N개의 줄에 N개의 수 i번째 줄의 j번째 수는 j번 예술가가 i번 예술가에게 그 그림을 살 때의 가격.
# 모든 가격은 0이 제일 낮은 가격, 9가 제일 높은 가격
price = [list(map(int, input().strip())) for _ in range(N)]

# 이전 구매자, 현재 소유자, 현재 가격을 표시
dp = [[[0] * 10 for _ in range(N)] for _ in range(1 << N)]

def solve(visit, curr, cost): # visit = 이전 구매자, curr = 현재 소유자, cost = 현재 가격
    if dp[visit][curr][cost] != 0: # 현재 위치에 값이 0이 아닌 경우
        return dp[visit][curr][cost]

    cnt = 0 # 구매자 수
    for i in range(1, N): # 첫 구매자를 제외한 나머지
        if price[curr][i] >= cost and visit & (1 << i) <= 0: # 다음 가격이 현재 가격보다 같거나 크고, 이전 구매자가 아닌 경우
            cnt  = max(cnt, solve(visit|(1<<i), i, price[curr][i]) + 1)

    dp[visit][curr][cost] = cnt

    return cnt

print(solve(1, 0, 0)+1)
