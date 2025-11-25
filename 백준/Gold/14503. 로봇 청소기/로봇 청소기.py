import sys
from collections import deque
input = sys.stdin.readline

# 시작 지점부터 빈칸이 없을때 까지 청소

# 0: 청소되지 않은 빈칸, 1: 벽

# N, M (3 <= N, M <= 50)
N, M = map(int, input().strip().split())
r, c, d = map(int, input().strip().split()) # 로봇의 시작위치, 시작 방향

arr = [] # 벽 위치 저장
visit = [] # 청소 상태 저장

for _ in range(N):
    row = list(map(int, input().strip().split()))

    arr.append(tuple(row)) # 변경되는걸 막기 위한 튜플
    visit.append(row)

# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
#   - 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#   - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다

# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
#   - 반시계 방향으로 90도 회전한다.
#   - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
#   - 1번으로 돌아간다.

# 청소기는 무조건 직진만 함 제자리에서 반시계 방향으로 90도 회전함
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
# 반시계 방향이라면 d-1 수행

move = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3:(0, -1)} # 각 북동남서 순서 
def check_clean(x, y): # 현재 위치 주변의 청소 상태 확인
    for i, j in move.values():
        nx, ny = x+i, y+j
 
        if not visit[nx][ny]: # 청소 안한곳이 있으면 0
            return 0
    
    return 1 # 없으면 1

def run(r, c, d): # 전체 작동 함수
    que = deque([(r, c, d)])
    cnt = 0
    while que: # 반복문 수행으로 종료 조건을 만족할때 까지 수행
        x, y, d = que.popleft()
        if not visit[x][y]:
            cnt += 1
            visit[x][y] = cnt
        
        if check_clean(x, y): # 주변에 청소 안한 곳이 없으면
            i, j = move[(d-2)%4] # 180도 뒤의 위치
            nx, ny = x+i, y+j

            if not arr[nx][ny]: # 벽이 아니라면
                que.append((nx, ny, d))
            else: # 벽이라면
                return cnt
        else: # 청소 안한 곳이 있으면
            nd = (d-1)%4 # 반시계 방향으로 회전
            i, j = move[nd] # 현재 보는 방향의 다음 칸
            nx, ny = x+i, y+j

            if not visit[nx][ny]: # 앞쪽이 청소되지 않은 경우
                que.append((nx, ny, nd)) # 앞으로 이동
            else:
                que.append((x, y, nd)) # 현재 위치에서 바라보는 방향만 변경

print(run(r, c, d))