import sys
input = sys.stdin.readline

# 낚시왕이 잡은 상어 크기의 합을 출력

# 낚시왕은 처음에 첫 열의 왼쪽에 있음, 끝 열의 오른쪽 칸에 이동을 하면 이동을 멈춤
# 1초 동안 다음의 순서대로 수행

# 1. 낚시왕이 오른쪽으로 한 칸 이동
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡음 상어를 잡으면 격자판에서 상어 사라짐
# 3. 상어가 이동
#   상어는 주어진 속도로 이동, 속도는 칸/초 단위, 상어가 격자판의 경계를 넘으면 방향을 바꿈(속력은 유지)
#   한 칸에 두 마리의 이상의 상어가 있는 경우 크기가 큰 상어가 나머지 상어를 모두 잡아먹음

# 낚시왕, 상어 순으로 이동
# 각 상어의 크기는 고유함
"""
상어의 이동방향을 아래, 오른쪽으로만 제한하면
칸의 총 개수는 (R-1)*2, (C-1)*2 이고
각 숫자로 나눴을때 해당 위치로 표시 가능
        0  1  2  3  4
예를들어 [0, 0, 1, 0, 0] 의 위치에서 속력이 8 오른쪽 이동을 한다 하면
 0  1  2  3  4  5  6  7
[0, 0, 1, 0, 0, 0, 0, 0] 의 가상 위치에서 한쪽 방향으로 8번 움직이는 것과 비슷함
이동 = (8+2) % 8 = 2

 0  1  2  3  4
[0, 0, 0, 1, 0] 의 위치에서 왼쪽으로 5 이동을 한다 치면
[0, 0, 0, 0, 0, 1, 0, 0] 위치에서 오른쪽으로 5 이동 하는 하는 것과 비슷
"""
# 격자판의 크기 R, C 상어의 수 M (2 <= R, C <= 100, 0 <= M <= RxC)
R, C, M = map(int, input().strip().split())
MAP = [[0]*C for _ in range(R)] # 상어의 실제 위치
point = set() # 상어의 가상 위치 r, c, s, d, z
# M개의 줄에 상어의 정보
# r, c, s, d, z (1 <= r <= R, 1 <= c <= C, 0 <= s <= 1000, 1 <= d <= 4, 1 <= z <= 10,000)
# (r, c) 상어의 위치, s 속력, d 이동 방향, z 크기
# d = 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
for _ in range(M):
    r, c, s, d, z = map(int, input().strip().split())
    # 0, 0 에 맞춰서 -1 씩 해줌
    r -= 1
    c -= 1

    MAP[r][c] = z
    if d == 1:
        r = (R-1)+(R-r-1)
        point.add((r, c, s, d, z))
    elif d == 2:
        point.add((r, c, s, d, z))
    elif d == 3:
        point.add((r, c, s, d, z))
    else:
        c = (C-1)+(C-c-1)
        point.add((r, c, s, d, z))

def real_point(x, y): # 상어의 실제위치
    if x > (R-1): x = (R-1)*2-x
    if y > (C-1): y = (C-1)*2-y

    return x, y

def move(x, y, s, d): # 상어의 이동
    if d <= 2:
        x = (x+s) % ((R-1)*2)
    else:
        y = (y+s) % ((C-1)*2)

    return x, y

def cycle():
    n_MAP = [[0]*C for _ in range(R)]
    n_point = set()
    for r, c, s, d, z in point:
        rx, ry = real_point(r, c)
        if z != MAP[rx][ry]: continue
        nx, ny = move(r, c, s, d)
        nrx, nry = real_point(nx, ny)

        n_MAP[nrx][nry] = max(n_MAP[nrx][nry], z)
        n_point.add((nx, ny, s, d, z))

    return n_MAP, n_point

ans = 0
for j in range(C):
    for i in range(R):
        if MAP[i][j] != 0:
            ans += MAP[i][j]
            MAP[i][j] = 0
            break

    MAP, point = cycle()

print(ans)

