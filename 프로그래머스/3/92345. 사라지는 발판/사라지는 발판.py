# directions: 상하좌우
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(board, ax, ay, bx, by):
    n, m = len(board), len(board[0])

    # 현재 플레이어의 발판이 이미 없는 경우: 여기서 시작할 수 없음 → 패배 상태
    if board[ax][ay] == 0:
        return 0

    can_move = False
    best = 0  # 0으로 초기화 (아직 최선 수 없음, 패배 기준)

    for dx, dy in DIRS:
        nx, ny = ax + dx, ay + dy
        # 범위 밖이거나, 발판이 없으면 이동 불가
        if not in_range(nx, ny, n, m):
            continue
        if board[nx][ny] == 0:
            continue

        can_move = True

        # 현재 위치 발판 제거
        board[ax][ay] = 0
        # 턴 교대: 상대(b)가 먼저, 나는 다음 위치(nx, ny)
        val = dfs(board, bx, by, nx, ny) + 1
        # 보드 복구
        board[ax][ay] = 1

        if best == 0:
            best = val
            continue

        # val: 이번 선택 결과, best: 지금까지의 최선 결과

        # 1) val이 승리(홀수)이고, best가 패배(짝수)면 → 승리 케이스로 바로 갱신
        if val % 2 == 1 and best % 2 == 0:
            best = val
        # 2) 둘 다 패배(짝수)라면 → 최대 턴 수(오래 버티기)
        elif val % 2 == 0 and best % 2 == 0:
            best = max(best, val)
        # 3) 둘 다 승리(홀수)라면 → 최소 턴 수(빨리 이기기)
        elif val % 2 == 1 and best % 2 == 1:
            best = min(best, val)

    # 더 이상 갈 수 있는 칸이 없다면 패배 → 0 반환
    if not can_move:
        return 0

    return best

def solution(board, aloc, bloc):
    # 보드는 1/0으로 주어짐
    n, m = len(board), len(board[0])
    ax, ay = aloc
    bx, by = bloc
    return dfs(board, ax, ay, bx, by)