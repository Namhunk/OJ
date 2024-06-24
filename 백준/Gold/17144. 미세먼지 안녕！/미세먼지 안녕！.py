import sys

# 1초 동안 일어나는 일
# 1. 미세먼지의 확산 -> 상하좌우로 퍼짐 현재값의 1/5배 공기청정기 있으면 x, floor 값 남은 현재값 -= 개수 * 현재값//5
# 2. 공기청정기 작동 -> 위쪽 : 반시계, 아래쪽 : 시계, 공기청정기에 들어가면 정화됨

# 먼지의 확산
def spread(): # 전체 배열, 현재 먼지위치
    arr = [[0]* C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] > 0: # 먼지인 경우
                tmp = 0
                for r, c in move:
                    dx, dy = x+r, y+c
                    if not (0 <= dx < R and 0 <= dy < C and A[dx][dy] != -1): continue # 범위 안에 있고 공기청정기가 아니면
                    arr[dx][dy] += A[x][y] // 5
                    tmp += A[x][y]//5
                A[x][y] -= tmp
    
    for x in range(R):
        for y in range(C):
            A[x][y] += arr[x][y]

def run_cleaner(): # 공기청정기 가동
    def top(): # 위쪽 공기청정기
        before = 0 # 이전값
        x, y = cleaner[0], 1 # 오른쪽 부터
        d = 0
        while True:
            r, c = move[d]
            dx, dy = x+r, y+c
            if not (0 <= dx < R and 0 <= dy < C): d = (d + 1) % 4; continue # 꼭지점인경우
            if (x, y) == (cleaner[0], 0): break # 공기청정기인 경우

            A[x][y], before = before, A[x][y]
            x, y = dx, dy
    
    def bottom():
        before = 0
        x, y = cleaner[1], 1
        d = 0
        while True:
            r, c = move[d]
            dx, dy = x+r, y+c
            if not (0 <= dx < R and 0 <= dy < C): d = (d - 1) % 4; continue
            if (x, y) == (cleaner[1], 0): break
            A[x][y], before = before, A[x][y]
            x, y = dx, dy
    
    top()
    bottom()

R, C, T = map(int, sys.stdin.readline().strip().split())
move = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 우, 상, 좌, 하 로 이동
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
cleaner = [] # 공기청정기 위치
for i in range(R):
    if A[i][0] == -1:
        cleaner = [i, i+1] # 위치 저장
        break

for _ in range(T):
    spread()
    run_cleaner()

ans = 0
for i in A:
    ans += sum(i)

print(ans+2)