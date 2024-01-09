import sys
from itertools import combinations
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 치킨 거리는 집을 기준으로 정해짐

# 거리가 최소인 M개의 치킨집을 고르고 나머지는 폐업
# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값

# 거리가 작은 순으로 M개를 골라 합을 출력

# N, M 입력
N, M = map(int, sys.stdin.readline().strip().split())
# N x N 도시 정보(0 = 빈 칸, 1 = 집, 2 = 치킨집)
city = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# 집
house = []
# 치킨집
chicken = []
# 정답
ans = float('inf')

# 집, 치킨집의 좌표를 구함
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 치킨집 중 3개 선택
for c in combinations(chicken, M):
    temp = 0 # 도시의 치킨 거리
    for h in house:
        cd = float('inf') # 각 집마다 치킨 거리
        for j in range(M):
            cd = min(cd, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += cd
    ans = min(ans, temp)

print(ans)