from collections import deque

# 현재 로봇 상태(pos)에서 이동/회전으로 갈 수 있는 다음 상태들을 반환
def get_next_pos(pos, board):
    next_pos = []  # 이동 가능한 위치들의 리스트
    pos = list(pos)
    (x1, y1), (x2, y2) = pos[0], pos[1]

    # 상, 하, 좌, 우 평행 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})

    # 회전 (가로인 경우)
    if x1 == x2:  # 두 점의 x가 같으면 가로로 놓여 있는 상태 (행이 같다)
        for d in [-1, 1]:  # 위쪽(-1), 아래쪽(1)
            if board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                # 왼쪽 칸을 축으로 회전
                next_pos.append({(x1, y1), (x1 + d, y1)})
                # 오른쪽 칸을 축으로 회전
                next_pos.append({(x2, y2), (x2 + d, y2)})

    # 회전 (세로인 경우)
    if y1 == y2:  # 두 점의 y가 같으면 세로로 놓여 있는 상태 (열이 같다)
        for d in [-1, 1]:  # 왼쪽(-1), 오른쪽(1)
            if board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                # 위쪽 칸을 축으로 회전
                next_pos.append({(x1, y1), (x1, y1 + d)})
                # 아래쪽 칸을 축으로 회전
                next_pos.append({(x2, y2), (x2, y2 + d)})

    return next_pos


def solution(board):
    n = len(board)

    # 보드 바깥을 1(벽)로 둘러싸서 인덱스 체크를 단순화
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # 시작 상태: (1,1)과 (1,2)에 로봇이 가로로 놓여 있음
    start = {(1, 1), (1, 2)}
    q = deque()
    q.append((start, 0))  # (현재 위치 집합, 시간)
    visited = [start]

    while q:
        pos, cost = q.popleft()
        # 목표 지점 (n, n)에 도달했는지 확인
        if (n, n) in pos:
            return cost

        # 현재 상태에서 이동/회전 가능한 모든 상태 탐색
        for nxt in get_next_pos(pos, new_board):
            if nxt not in visited:
                visited.append(nxt)
                q.append((nxt, cost + 1))

    return 0