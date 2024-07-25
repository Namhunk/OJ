import sys
input = sys.stdin.readline

# 하다만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내라
# 9개의 줄에 9개의 숫자가 보드로 입력됨, 숫자가 채워지지 않는 칸은 0
sudoku = [list(map(int, input().strip())) for _ in range(9)]

# 9개의 줄에 9개의 숫자로 답을 출력, 답이 여러개라면 그 중 사전식으로 앞서는 것을 출력, 즉 81자리의 수가 제일 작은 경우를 출력


def check(i, j, k): # 행, 열, 3x3을 검사하는 함수
    for c in range(9): # 행 검사
        if k == sudoku[i][c]: return False

    for r in range(9): # 열 검사
        if k == sudoku[r][j]: return False

    ti, tj = (i//3)*3, (j//3)*3
    for r in range(3): # 3x3 검사
        for c in range(3):
            if k == sudoku[ti+r][tj+c]: return False

    return True

def solv(x):
    if x == len(nums): # 마지막까지 숫자를 입력했다면 출력
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end='')
            print()
        exit()

    i, j = nums[x] # 현재 검사할 위치
    for k in range(1, 10):
        if check(i, j, k): # 만약 현재 숫자가 입력 조건에 맞는다면 입력
            sudoku[i][j] = k
            solv(x+1)
            sudoku[i][j] = 0

# 숫자가 0인 (i, j)를 저장
nums = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            nums.append((i, j))

solv(0)