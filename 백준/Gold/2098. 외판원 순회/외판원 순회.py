import sys
input = sys.stdin.readline
inf = sys.maxsize

# TSP(Traveling Salesman Problem)

# 외판원 순회에 필요한 최소 비용을 출력

# 도시의 수 N
N = int(input().strip()) # 2 <= N <= 16
# W[i][j]는 i에서 j로 가기 위한 비용, 현재 위치이거나, i에서 j로 갈 수 없는 경우 0
W = [list(map(int, input().strip().split())) for _ in range(N)]

# 현재 어떤 위치들을 지났는지 비트 형태의 배열을 생성
# N = 4 이면 방문을 하지 않은 경우는 0000 = 0, 1번, 3번을 방문한 경우 0101 = 5, 모두 방문한 경우 1111 = 15
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(x, visit): # x = 현재 위치, visit = 방문한 위치들의 기록
    if visit == (1 << N) - 1: # 모두 방문을 했다면
        return W[x][0] or inf # 마지막 위치에서 처음 위치로 갈 수 없다면 inf

    if dp[x][visit] != -1: # dp에 값이 있어 계산할 필요가 없는 경우
        return dp[x][visit]

    MIN = inf
    for NEXT in range(1, N):
        if not visit & (1 << NEXT) and W[x][NEXT] != 0: # 아직 방문하지 않았고 다음 위치로 갈 수 있는 경우
            MIN = min(MIN, tsp(NEXT, visit | 1 << NEXT) + W[x][NEXT])

    dp[x][visit] = MIN # 최소값 저장
    return dp[x][visit]

print(tsp(0, 1))