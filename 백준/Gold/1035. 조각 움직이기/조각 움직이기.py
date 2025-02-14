import sys
from itertools import combinations, permutations
input = sys.stdin.readline

# 최소 몇 번 이동해야 모든 조각이 연결 요소를 이루게 되는지 출력

# 5 x 5 크기의 보드의 모든 조각을 적절히 움직여 모든 조각을 연결하는데
# 상하좌우로 인접한 조각을 모두 연결했을 때, 모든 쌍의 조각이 적어도 하나의 경로로 연결되어 있어야 함

# 보드의 상태 '.' 빈 곳, '*' 조각 조각은 1개 이상 5개 이하
board = [list(input().strip()) for _ in range(5)]
pieces = []
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            pieces.append((i, j))

def connected(cells): # 연결 확인
    visit = set()
    stack = [cells[0]]
    visit.add(cells[0])

    while stack:
        x, y = stack.pop()
        for r, c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = x+r, y+c
            if (nx, ny) in cells and (nx, ny) not in visit: # 연결된 위치중 방문하지 않은 곳이라면
                visit.add((nx, ny)) # 방문표시
                stack.append((nx, ny))

    return len(visit) == len(cells) # 두 길이가 같은지

def move(start, curr): # 이동 거리
    return abs(start[0]-curr[0]) + abs(start[1]-curr[1])

n = len(pieces)
all_cell = [(i, j) for i in range(5) for j in range(5)] # 전체 칸
ans = float('inf')

for comb in combinations(all_cell, n): # 조각의 개수만큼
    if connected(comb): # 연결 상태 확인
        d = float('inf')
        for perm in permutations(comb, n): # 각 조각의 위치를 다르게
            dist_sum = 0
            for i in range(n):
                dist_sum += move(pieces[i], perm[i])

            d = min(d, dist_sum)

        ans = min(ans, d)

print(ans)

