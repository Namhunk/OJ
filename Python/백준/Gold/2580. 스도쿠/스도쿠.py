import sys
import random, math
input = sys.stdin.readline

    
def solve(x, rows, cols, cand): # 현재 cand 번호, rows, cols, cand
    if x >= len(cand):
        for i in rows:
            print(*i)

        return True
    
    i, j = cand[x]

    area = set()
    si = 3*(i // 3)
    sj = 3*(j // 3)
    for a in range(si, si+3):
        for b in range(sj, sj+3):
            area.add(rows[a][b])

    nums = set(range(1, 10)) - (set(rows[i]) | set(cols[j]) | area)
    for n in nums:
        rows[i][j] = n
        cols[j][i] = n

        if solve(x+1, rows, cols, cand):
            return True

        rows[i][j] = 0
        cols[j][i] = 0

def main():
    N = 9
    rows = []
    ans = []
    for _ in range(N):
        rows.append(list(map(int, input().strip().split())))

    cand = [] # 원소값이 0인 위치
    cols = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cols[i][j] = rows[j][i]

            if rows[i][j] == 0:
                cand.append((i, j))

    solve(0, rows, cols, cand)

if __name__ == '__main__':
    main()

"""
스도쿠를 완성해야함
숫자는 1 ~ 9

1. 현재 행에 없는 숫자
2. 현재 열에 없는 숫자
3. 현재 3x3 칸에 없는 숫자

-------------------------


"""