import sys
input = sys.stdin.readline

# 동서방향 도로의 개수를 나타내는 정수 N (5 <= N <= 1,000)
N = int(input().strip())

# 처리해야 하는 사건의 개수 W (1 <= W <= 1,000)
W = int(input().strip())

# 사건이 발생한 위치
arr = [list(map(int, input().strip().split())) for _ in range(W)]

car = [[1, 1], [N, N]] + arr # 사건의 진행 순서

def dist(curr, next):
    x1, y1 = curr
    x2, y2 = next
    return abs(x1 - x2) + abs(y1 - y2)

def solve(i, j):
    k = max(i, j)+1
    if k >= W+2: return 0
    if dp[i][j] != float('inf'): return dp[i][j]

    d1 = solve(k, j) + dist(car[i], car[k])
    d2 = solve(i, k) + dist(car[j], car[k])

    if d1 < d2:
        dp[i][j] = d1
        visit[i][j] = 1
    else:
        dp[i][j] = d2
        visit[i][j] = 2

    return dp[i][j]

dp = [[float('inf')]*(W+2) for _ in range(W+2)]
visit = [[0]*(W+2) for _ in range(W+2)]
print(solve(0, 1))

i, j = 0, 1
for k in range(2, W+2):
    print(visit[i][j])
    if visit[i][j] == 1:
        i = k
    else:
        j = k