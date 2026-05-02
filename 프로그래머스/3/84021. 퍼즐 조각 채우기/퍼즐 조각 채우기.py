# 3 <= len(game_board) <= 50
# len(game_board) == len(game_board[i])

from collections import deque
def solution(game_board, table):
    global visit, N
    N = len(game_board)
    answer = 0
    
    # game_board에서 빈칸의 모양 좌상단을 (0, 0)으로 한 퍼즐 모양
    visit = [[0]*N for _ in range(N)]
    empty = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] or visit[i][j]:
                continue
            empty.append(find_shape(i, j, 0, game_board))
    
    piece = []
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not table[i][j] or visit[i][j]:
                continue
            
            piece.append(find_shape(i, j, 1, table))
    
    used = [False]*len(piece)
    for hole in empty:
        hole.sort()
        for idx in range(len(piece)):
            if used[idx]:
                continue
            if len(hole) != len(piece[idx]):  # 크기 다르면 불가능
                continue
            
            block = piece[idx][:]
            block = norm(block)  # 정규화 한번
            matched = False
            
            for _ in range(4):  # 0,90,180,270
                if block == hole:
                    matched = True
                    break
                block = rotate(block)  # 다음 회전[web:2][web:4]
            
            if matched:
                used[idx] = True
                answer += len(hole)
                break  # 이 hole은 채웠으니 다음 hole로
    
    return answer


def find_shape(i, j, key, arr):
    global visit, N
    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visit[i][j] = 1
    tmp = [(i, j)]
    q = deque([(i, j)])
    MIN_X, MIN_Y = i, j
    
    while q:
        x, y = q.popleft()
        for r, c in move:
            nx, ny = x+r, y+c
            if not (0 <= nx < N and 0 <= ny < N and arr[nx][ny] == key):
                continue
            if visit[nx][ny]:
                continue
            
            MIN_X = min(MIN_X, nx)
            MIN_Y = min(MIN_Y, ny)
            visit[nx][ny] = 1
            tmp.append((nx, ny))
            q.append((nx, ny))
    
    # 여기서 정규화 + 정렬까지 해버리기
    xs = [x for x, y in tmp]
    ys = [y for x, y in tmp]
    min_x, min_y = min(xs), min(ys)
    res = [(x-min_x, y-min_y) for x, y in tmp]
    res.sort()
    return res
    
def norm(arr):
    xs = [x for x, y in arr]
    ys = [y for x, y in arr]
    min_x, min_y = min(xs), min(ys)
    res = [(x-min_x, y-min_y) for x, y in arr]
    res.sort()
    return res

def rotate(arr):
    rotated = [(y, -x) for x, y in arr]
    return norm(rotated)
"""
한 칸이 1x1인 게임 보드가 있음
1. 조각은 한 번에 하나씩
2. 조각을 회전시킬 수 있음
3. 조각을 회전할 수 없음
4. 게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안됨

비어있는 칸들 중 몇칸을 채우는지에 대한 문제
------------------------------

1. 기본적으로 game_board에 는 채워져 있는 부분이 있음
2. table에 있는 퍼즐을 사용해 game_board를 채워야 함
3. 퍼즐 조각은 1x1이 최대 6개까지 연결됨
4. 퍼즐 조각을 채울 때 비어있는 칸과 딱 맞아 떨어져야 함

-------------------------------
1. 현재 보유중인 퍼즐들의 형태를 알아야 함
2. 채워야 하는 빈 칸의 형태를 알아야 함
"""