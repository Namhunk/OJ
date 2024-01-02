import sys, copy
from collections import deque

# 연구소의 크기는 N x M 인 직사각형 
# 바이러스는 상하좌우 인접한 빈 칸으로 퍼져나감
# 새로 세울 수 있는 벽의 개수는 3개 (*반드시 3개를 세워야함*)
# 빈칸 = 0, 벽 = 1, 바이러스 = 2

# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역의 크기의 최댓값

# 벽을 설치한다 or 벽을 설치하지 않는다.
# 벽 3개를 설치 했다면 테스트를 해본다.
def Create_Wall(cnt):
    if cnt < 3:
        for i in range(N):
            for j in range(M):
                if not lab[i][j]:
                    lab[i][j] = 1
                    Create_Wall(cnt+1)
                    lab[i][j] = 0
    else:
        BFS()
    
def BFS():
    global ans
    safe_area = 0
    temp_lab = copy.deepcopy(lab)
    visit = set(virus)
    que = deque(virus)
    
    while que:
        x, y = que.popleft()
        for r, c in move:
            if 0 <= x+r < N and 0 <= y+c < M and (x+r, y+c) not in visit:
                if not temp_lab[x+r][y+c]:
                    temp_lab[x+r][y+c] = 2
                    visit.add((x+r, y+c))
                    que.append((x+r, y+c))
    
    for i in range(N):
        for j in range(M):
            if not temp_lab[i][j]: safe_area += 1
    
    ans = max(ans, safe_area)
        
# 세로 N, 가로 M
N, M = map(int, sys.stdin.readline().strip().split())
lab = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 바이러스의 이동 방향
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 바이러스의 위치를 구해놓음
virus = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2: virus.append((i, j))

# 정답
ans = 0
Create_Wall(0)
print(ans)