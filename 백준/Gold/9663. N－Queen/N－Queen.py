import sys

# 퀸의 위치에 대해 검증
def check_safe(x):
    # 이전 행 부터 현재 행 까지
    for i in range(x):
        # col[x] == col[i] : 현재 행의 열과, 이전 행들의 열이 같은가(세로)
        # abs(col[x] - col[i]) == x-i : 행의 차이와 열의 차이가 같은가(대각선)
        if col[x] == col[i] or abs(col[x] - col[i]) == x-i:
            return False
    return True

def N_Queen(x):
    global cnt
    # 마지막에 도달한 경우
    if x == n: cnt += 1
    else:
        for i in range(n):
            col[x] = i
            if check_safe(x):
                N_Queen(x+1)

# n의 값 입력
n = int(sys.stdin.readline().strip())
col = [0]*n # x 행 col[x] 열 위치에 퀸이 있다.
cnt = 0
N_Queen(0)
print(cnt)