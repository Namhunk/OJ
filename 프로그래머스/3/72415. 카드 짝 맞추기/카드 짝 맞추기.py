# board.shape = (4, 4)
# 0 <= r, c <= 3
from collections import deque
def solution(board, r, c):
    global N, move, card
    N = len(board) # 맵의 크기
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 이동 방향
    card = {} # 각 숫자별 카드 2개의 위치
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                card.setdefault(board[i][j], []).append((i, j))
    
    answer = dfs(board, r, c)
    return answer

def ctrl(board, x, y, dx, dy): # x, y = 현재위치, dx, dy = 이동 방향
    nx, ny = x, y
    while 1:
        tx, ty = nx+dx, ny+dy # 다음 위치
        
        if not (0 <= tx < N and 0 <= ty < N): # 위치를 벗어나면
            return nx, ny
        
        nx, ny = tx, ty
        if board[nx][ny] != 0: # 카드 위치라면
            return nx, ny
        

def bfs(board, sx, sy, tx, ty): # 현재 위치에서 (tx, ty)로 가는 최소 횟수
    q = deque([(sx, sy, 0)])
    visit = [[False]*N for _ in range(N)] # 방문 표시
    visit[sx][sy] = True
    
    while q:
        x, y, d = q.popleft()
        if (x, y) == (tx, ty): # 현재 위치가 목표 위치라면
            return d
        
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if (0 <= nx < N and 0 <= ny < N and not visit[nx][ny]): # 범위안에 있고 방문하지 않은 위치
                visit[nx][ny] = True
                q.append((nx, ny, d+1))
            
            cx, cy = ctrl(board, x, y, dx, dy)
            if not visit[cx][cy]: # 방문하지 않은 위치만
                visit[cx][cy] = True
                q.append((cx, cy, d+1))

def dfs(board, r, c): # 모든 카드 위치에 대해 탐색
    start = []
    for num, p in card.items():
        x1, y1 = p[0]
        if board[x1][y1] != 0: # 현재 위치가 카드가 맞으면
            start.append(num) # 번호 추가
    
    if not start: # 값이 없다면 0
        return 0
    
    ans = float('inf') # 최종 정답을 저장할 변수
    for num in start:
        (x1, y1), (x2, y2) = card[num] # 시작위치
        
        # 현재 카드의 짝을 찾아준 다음의 맵
        new_board = [list(row) for row in board]
        new_board[x1][y1] = 0
        new_board[x2][y2] = 0
        new_board = tuple(tuple(row) for row in new_board)
        
        # 1. 현재 위치에서 x1, y1 부터 방문 (r, c) -> (x1, y1) -> (x2, y2)
        cost1 = bfs(board, r, c, x1, y1) + bfs(board, x1, y1, x2, y2) + 2 # 엔터 두번
        cost1 += dfs(new_board, x2, y2) # 새 위치에서 시작
        
        # 2. 현재 위치에서 x2, y2 부터 방문 (r, c) -> (x2, y2) -> (x1, y1)
        cost2 = bfs(board, r, c, x2, y2) + bfs(board, x2, y2, x1, y1) + 2
        cost2 += dfs(new_board, x1, y1)
        
        ans = min(ans, cost1, cost2) # 가장 작은 횟수만
    return ans
        

"""
카드 16장이 4x4의 형태로 뒷면이 보이게 있음
각 카드에는 8가지 캐릭터 그림이 2개씩 존재

유저가 2장을 선택해 뒤집었을 때
같은 그림이 그려졌다면 사라짐

모든 카드를 제거하기 위한 키조작의 횟수 최솟값

방향키:        상하좌우 중 1칸 이동
ctrl + 방향키: 공개된 카드 위치 or 마지막
enter:        카드 뒤집기

1. 현재 위치에서 다른 카드까지 가는 모든 거리
2. 현재 카드에서 짝꿍 카드까지 가는 모든 거리
3. 1 - 2 반복을 구해서 모든 경우에 대한 최소

"""