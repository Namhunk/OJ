import sys
from collections import deque
from string import ascii_uppercase
input = sys.stdin.readline

# 각 테스트 케이스 마다, 상근이가 훔칠 수 있는 문서의 최대 개수 출력

# 1. '.'는 빈 공간을 나타냄
# 2. '*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없음
# 3. '$'는 상근이가 훔쳐야 하는 문서이다.
# 4. 알파벳 대문자는 문을 나타냄
# 5. 알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다
# 열쇠는 여러 번 사용 가능
# 상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나 들 수 있다
# 상근이는 상 하 좌 우 로만 움직임

# 테스트 케이스의 개수 T, 0 <= T <= 100
T = int(input().strip())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상근이의 이동 방향
for _ in range(T):
    h, w = map(int, input().strip().split()) # 높이 h, 너비 w (2 <= h, w <= 100)
    arr = [list(input().strip()) for _ in range(h)] # 평면도
    keys = set() # 보유 열쇠
    door = {U: [] for U in ascii_uppercase} # 문들의 좌표를 저장할 dict

    for k in input().strip():
        if k == '0': break
        keys.add(k.upper())

    visit = [[True]*w for _ in range(h)] # 방문 표시
    ans = 0
    que = deque()
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1: # 가장자리인 경우
                if arr[i][j] == '*': continue # 벽이 아닌 경우
                if arr[i][j].isupper(): # 문이면 좌표 저장
                    door[arr[i][j]].append((i, j))
                else: # 다른 경우
                    if arr[i][j] == '$': # 문서면 정답 +1
                        ans += 1
                    elif arr[i][j].islower(): # 열쇠면 보유 열쇠에 추가
                        keys.add(arr[i][j].upper())

                    que.append((i, j))
                    visit[i][j] = False

    for k in keys:
        for i, j in door[k]:
            que.append((i, j))
            visit[i][j] = False

    while que:
        x, y = que.popleft()

        for r, c in move:
            nx, ny = x+r, y+c
            # 다음 위치가 방문 가능한 위치일때
            if not (0 <= nx < h and 0 <= ny < w and visit[nx][ny]): continue
            if arr[nx][ny] == '*': continue

            if arr[nx][ny].isupper(): # 문인 경우
                if arr[nx][ny] in keys: # 열쇠가 있다면 방문
                    que.append((nx, ny))
                    visit[nx][ny] = False
                else: # 열쇠가 없다면 나중에 방문 할 수 있으므로 저장
                    door[arr[nx][ny]].append((nx, ny))
            else:
                if arr[nx][ny] == '$': # 문서인 경우 정답 +1
                    ans += 1
                if arr[nx][ny].islower(): # 열쇠인 경우 열쇠 저장후 저장한 문의 위치 추가
                    keys.add(arr[nx][ny].upper())
                    for i, j in door[arr[nx][ny].upper()]:
                        que.append((i, j))
                        visit[i][j] = False

                que.append((nx, ny))
                visit[nx][ny] = False

    print(ans)
