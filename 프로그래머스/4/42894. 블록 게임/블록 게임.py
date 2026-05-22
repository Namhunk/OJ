def can_fill(board, r, c):
    """
    맨 위에서부터 (r, c) 위치까지 검은 블록이 떨어질 수 있는지 확인하는 함수
    """
    for i in range(r):
        if board[i][c] != 0:
            return False  # 중간에 다른 블록(장애물)이 있으면 떨어질 수 없음
    return True

def find_and_remove(board, N):
    """
    보드 전체를 스캔하며 지울 수 있는 블록을 찾아 하나 지우고 True를 반환
    """
    # 1. 2x3 크기의 직사각형 검사 (가로로 넓은 블록)
    for r in range(N - 1):
        for c in range(N - 2):
            block_id = -1
            zeros = []
            is_valid_window = True
            
            for i in range(r, r + 2):
                for j in range(c, c + 3):
                    val = board[i][j]
                    if val == 0:
                        zeros.append((i, j))
                        if len(zeros) > 2:  # 빈 공간이 2개를 초과하면 탈락
                            is_valid_window = False
                    else:
                        if block_id == -1:
                            block_id = val
                        elif block_id != val: # 다른 종류의 블록이 섞여 있으면 탈락
                            is_valid_window = False
                
                if not is_valid_window:
                    break
                    
            # 한 종류의 블록 4개와 빈 공간 2개로 이루어져 있다면
            if is_valid_window and len(zeros) == 2 and block_id != -1:
                # 두 빈 공간 위로 막힌 곳이 없는지 확인
                if can_fill(board, zeros[0][0], zeros[0][1]) and can_fill(board, zeros[1][0], zeros[1][1]):
                    # 블록 지우기
                    for i in range(r, r + 2):
                        for j in range(c, c + 3):
                            if board[i][j] == block_id:
                                board[i][j] = 0
                    return True # 하나를 지웠으면 즉시 종료 후 재탐색 지시

    # 2. 3x2 크기의 직사각형 검사 (세로로 긴 블록)
    for r in range(N - 2):
        for c in range(N - 1):
            block_id = -1
            zeros = []
            is_valid_window = True
            
            for i in range(r, r + 3):
                for j in range(c, c + 2):
                    val = board[i][j]
                    if val == 0:
                        zeros.append((i, j))
                        if len(zeros) > 2:
                            is_valid_window = False
                    else:
                        if block_id == -1:
                            block_id = val
                        elif block_id != val:
                            is_valid_window = False
                
                if not is_valid_window:
                    break
                    
            if is_valid_window and len(zeros) == 2 and block_id != -1:
                if can_fill(board, zeros[0][0], zeros[0][1]) and can_fill(board, zeros[1][0], zeros[1][1]):
                    # 블록 지우기
                    for i in range(r, r + 3):
                        for j in range(c, c + 2):
                            if board[i][j] == block_id:
                                board[i][j] = 0
                    return True

    return False # 지울 수 있는 블록이 없음

def solution(board):
    N = len(board)
    answer = 0
    
    # 더 이상 지울 수 있는 블록이 없을 때까지 반복
    while True:
        removed = find_and_remove(board, N)
        if not removed:
            break # 지울 블록이 없다면 루프 종료
        answer += 1
        
    return answer