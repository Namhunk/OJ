import sys
input = sys.stdin.readline

# 2048 게임에서 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
N = int(input().strip()) # 보드의 크기 N (1 <= N <= 20)
block = [list(map(int, input().strip().split())) for _ in range(N)]

# N의 크기가 작으므로 백트래킹 시도
# 블럭의 이동은 상, 하, 좌, 우 4 방향만 가능
# 블럭안의 숫자가 일치해야 합쳐짐
# 0은 빈칸
def up(block): # 블럭들을 위로 이동
    temp = [[0]*N for _ in range(N)] # 이동 결과를 저장할 임시 배열

    for j in range(N): # 현재 열
        idx = 0 # 임시 배열에 저장할 행 위치
        before = -1 # 이전 블럭 값
        flag = 0 # 이전 블럭과 현재 블럭이 일치 하는지 검사
        for i in range(N):
            if block[i][j] == 0: continue # 블럭의 값이 0이 아니라면
            if not flag: # flag가 0이면
                before = block[i][j] # 현재값 저장
                flag = 1
            else: # flag가 1이면
                if before == block[i][j]: # 이전값과 현재 값이 일치하면
                    temp[idx][j] = before*2 # 현재 값의 2배 추가
                    before = -1 # before 초기화
                    flag = 0 # flag 초기화
                else: # 다르다면
                    temp[idx][j] = before
                    before = block[i][j]
                idx += 1

        if before != -1: # 이전값이 초기화가 안됬다면
            temp[idx][j] = before

    return temp
# 나머지 방향도 위와 비슷함

def right(block):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        idx = N-1
        before = -1
        flag = 0
        for j in range(N-1, -1, -1):
            if block[i][j] == 0: continue
            if not flag:
                before = block[i][j]
                flag = 1
            else:
                if before == block[i][j]:
                    temp[i][idx] = before*2
                    before = -1
                    flag = 0
                else:
                    temp[i][idx] = before
                    before = block[i][j]
                idx -= 1

        if before != -1:
            temp[i][idx] = before

    return temp

def down(block):
    temp = [[0]*N for _ in range(N)]
    for j in range(N):
        idx = N-1
        before = -1
        flag = 0
        for i in range(N-1, -1, -1):
            if block[i][j] == 0: continue
            if not flag:
                before = block[i][j]
                flag = 1
            else:
                if before == block[i][j]:
                    temp[idx][j] = before*2
                    before = -1
                    flag = 0
                else:
                    temp[idx][j] = before
                    before = block[i][j]
                idx -= 1

        if before != -1:
            temp[idx][j] = before

    return temp

def left(block):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        idx = 0
        before = -1
        flag = 0
        for j in range(N):
            if block[i][j] == 0: continue
            if not flag:
                before = block[i][j]
                flag = 1
            else:
                if before == block[i][j]:
                    temp[i][idx] = before*2
                    before = -1
                    flag = 0
                else:
                    temp[i][idx] = before
                    before = block[i][j]
                idx += 1

        if before != -1:
            temp[i][idx] = before

    return temp

def solv(block, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, block[i][j])
        return
    else:
        temp = up(block)
        solv(temp, cnt+1)
        temp = down(block)
        solv(temp, cnt+1)
        temp = left(block)
        solv(temp, cnt+1)
        temp = right(block)
        solv(temp, cnt+1)

ans = 0
solv(block, 0)
print(ans)