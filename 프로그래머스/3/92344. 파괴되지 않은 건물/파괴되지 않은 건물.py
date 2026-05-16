def solution(board, skill):
    N = len(board)      # board의 행 개수
    M = len(board[0])   # board의 열 개수
    
    arr = [[0]*(M+1) for _ in range(N+1)] # 공격, 회복의 수치만 나타낼 배열
    
    for Type, r1, c1, r2, c2, degree in skill:
        if Type == 1:      # 공격: 내구도 감소
            degree = -degree
    
        arr[r1][c1]     += degree
        arr[r1][c2+1]   -= degree
        arr[r2+1][c1]   -= degree
        arr[r2+1][c2+1] += degree
    
    
    for i in range(N):
        for j in range(M):
            arr[i+1][j] += arr[i][j]

    for i in range(N):
        for j in range(M):
            arr[i][j+1] += arr[i][j]
    
    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
        
    return answer

"""


0   0   0   0
0  -4  -4   0
0  -4  -4   0
0   0   0   0
"""