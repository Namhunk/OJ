import sys
input = sys.stdin.readline

# 맵의 형태로 정답을 출력, 원래 빈 칸인 곳은 0을 출력, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력

# N x N 의 행렬로 표현되는 맵에서 0은 이동할 수 있는 곳, 1은 이동할 수 없는 벽이 있는 곳
# 한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다.(두 칸이 변을 공유함)
# 1. 벽을 부수고 이동할 수 있는 곳으로 변경
# 2. 그 위치에서 이동할 수 있는 칸의 개수를 세어봄

# N(1 <= N <= 1,000), M(1 <= M <= 1,000)
N, M = map(int, input().strip().split())
MAP = [list(map(int, input().strip())) for _ in range(N)]

# 현재 위치가 벽일떄, 자신의 위치를 포함한 이동 가능한 위치들의 개수
# 0이 하나 있거나, 여러개 있거나 0이 있는 범위에 고유한 번호를 부여
# 그리고 벽의 주변에 0이 있다면 번호를 찾아 개수를 반환

from collections import deque
que = deque()
area = [0] # 각 영역의 번호
visit = [[0]*M for _ in range(N)] # 방문 표시
num = 0 # 영역의 개수
move = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 이동 방향

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0 and visit[i][j] == 0: # 방문하지 않은 0을 탐색
            cnt = 1 # 개수 카운트
            num += 1 # 영역의 번호
            visit[i][j] = num

            que.append((i, j))
            while que:
                x, y = que.popleft()

                for r, c in move:
                    nx, ny = x+r, y+c
                    if not (0 <= nx < N and 0 <= ny < M): continue # N, M 의 범위
                    if MAP[nx][ny] == 1: continue # 1이 아니고
                    if visit[nx][ny] != 0: continue # 방문하지 않은 위치만

                    visit[nx][ny] = num
                    cnt += 1
                    que.append((nx, ny))

            area.append(cnt) # 해당 영역의 개수 저장

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1: # 1 일떄
            numbers = set()
            for r, c in move: # 주변에 영역이 있는지 확인
                nx, ny = i+r, j+c
                if not (0 <= nx < N and 0 <= ny < M): continue
                numbers.add(visit[nx][ny])

            for k in numbers:
                MAP[i][j] += area[k]
                MAP[i][j] %= 10

for i in MAP:
    print(''.join(map(str, i)))
