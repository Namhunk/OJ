import sys

# 보드의 상태가 주어졌을 때, 형택이가 최대 몇 번 동전을 움직일 수 있는지 구해라

# 1. 동전이 있는 곳에 쓰여 있는 숫자 X를 본다.
# 2. 위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다
# 3. 동전을 위에서 고른 방향으로 X만큼 움직인다.
# 동전이 구멍에 빠지거나, 보드의 밖으로 나가면 게임은 종료된다.
# H는 구멍멍

# 동전을 무한번 움직일 수 있다면 -1 출력

def check(x):
    if x.isnumeric():
        return int(x)
    else:
        return x

# 보드의 세로 크기 N, 가로 크기 M (1 <= N, M <= 50)
N, M = map(int, input().strip().split())

# 보드의 상태 (N 행)
board = [list(map(check, input().strip())) for _ in range(N)]

# 이동 방향
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[True]*M for _ in range(N)]
finished = [[True]*M for _ in range(N)]

arr = []

def Game(i, j): # x, y : 현재 위치
    for r, c in move:
        dx, dy = i+r*board[i][j], j+c*board[i][j]

        if not (0 <= dx < N and 0 <= dy < M) or board[dx][dy] == 'H': continue
        if not finished[dx][dy]: continue

        if not visit[dx][dy]:
            print(-1)
            exit()
        
        visit[dx][dy] = False
        Game(dx, dy)
        visit[dx][dy] = True

    finished[i][j] = False
    arr.append([i, j])

visit[0][0] = False
Game(0, 0)

dp = [[1]*M for _ in range(N)]

while arr:
    x, y = arr.pop()
    for r, c in move:
        dx, dy = x+r*board[x][y], y+c*board[x][y]

        if not (0 <= dx < N and 0 <= dy < M) or board[dx][dy] == 'H': continue
        dp[dx][dy] = max(dp[dx][dy], dp[x][y]+1)

ans = 1
for i in dp:
    for j in i:
        ans = max(ans, j)

print(ans)