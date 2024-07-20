import sys
input = sys.stdin.readline

# 체스판 위에 놓을 수 있는 비숍의 최대 개수
"""
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) 
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) 
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) 
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4)
"""
# / 방향의 대각선을 보면 (i, j)일때 i+j의 값이 같음
# / 은 5개일때 0부터 8(4+4)까지 N개일때 2N-2까지 있음
# / 방향을 돌려서 ㅡ 로 만들었을때 2N-2개의 행으로 볼 수 있음
# 2N-2개의 행에는 각 1개씩 있어야 함

# \ 방향의 대각선을 보면 (i, j)일때 i-j의 값이 같음 i-j를 열로 봄 -N < i-j < N
# 2N-2개의 행을 보면서 i-j가 겹치는지 확인하며 백트래킹을 시도

def solv(row, curr): # 현재 위치, 현재 개수
    global ans
    if row >= 2*N-1: # 마지막까지 확인을 한 경우
        ans = max(ans, curr)
        return

    cnt = check(row)
    if cnt + curr <= ans: # 현재 + 앞으로 놓을 개수가 최대 보다 작으면 수행 x
        return

    for j in range(row + 1):
        i = row-j
        if not (0 <= i < N and 0 <= j < N): continue  # 실제 배열의 범위 안에 있고
        if not arr[i][j]: continue  # 비숍을 놓을 수 있는 위치이고
        if col[i - j]: continue  # 비숍이 겹치지 않는 열이면

        col[i-j] = 1
        solv(row+1, curr+1)
        col[i-j] = 0

    solv(row+1, curr)

def check(row): # 현재 행 부터 마지막 행 까지 놓을 수 있는 비숍의 개수
    cnt = 0
    for k in range(row, 2*N-1):
        for j in range(k+1):
            i = k-j
            if not (0 <= i < N and 0 <= j < N): continue # 실제 배열의 범위 안에 있고
            if not arr[i][j]: continue # 비숍을 놓을 수 있는 위치이고
            if col[i-j]: continue# 비숍이 겹치지 않는 열이면
            cnt += 1
            break

    return cnt

N = int(input().strip()) # 1 <= N <= 10
col = [0]*(2*N-1) # -N < i-j < N
arr = [list(map(int, input().strip().split())) for _ in range(N)]
# 비숍을 놓을 수 있는 곳 1
# 비숍을 놓을 수 없는 곳 0

ans = 0 # 정답
solv(0, 0)
print(ans)