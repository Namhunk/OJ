from collections import deque
from itertools import combinations
import sys

# 다른 방식 itertools의 cominations 사용
# N, M 입력
N, M = map(int, sys.stdin.readline().strip().split())
# 실험실 입력
lab = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

empty = set() # 빈 공간
virus = set() # 바이러스

# 실험실에서 각각 요소들의 위치를 저장
for i in range(N):
    for j in range(M):
        if not lab[i][j]: empty.add((i, j))
        elif lab[i][j] == 2: virus.add((i, j))

ans = 0 # 정답
move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 이동 방향

# combinations를 사용해 빈 공간 3개를 뽑아냄
for pos in combinations(empty, 3):
    add = set(pos) # 추가로 막을 부분
    visit = set(virus) # 방문 표시
    que = deque(virus)
    
    while que:
        x, y = que.popleft()
        for r, c in move:
            # 다음 위치가 실험실 범위 안에 있고, 빈 공간인가?
            if not (0 <= x+r < N and 0 <= y+c < M and not lab[x+r][y+c]): continue
            # 생성한 벽의 위치와 다른가?
            if (x+r, y+c) in add: continue
            # 방문하지 않은 위치인가?
            if (x+r, y+c) in visit: continue
            
            visit.add((x+r, y+c))
            que.append((x+r, y+c))
    
    area = 0 # 현재 안전 구역의 크기
    for i in range(N):
        for j in range(M):
            if lab[i][j]: continue
            if (i, j) in add: continue
            if (i, j) in visit: continue
            area += 1
            
    ans = max(ans, area)

print(ans)
            