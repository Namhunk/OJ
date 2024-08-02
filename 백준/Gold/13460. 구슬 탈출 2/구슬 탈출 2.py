import sys
input = sys.stdin.readline

from collections import deque
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력, 만약 10번 이하로 움직여 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1 출력

# 보드의 세로, 가로 N, M(3 <= N, M <= 10)
N, M = map(int, input().strip().split())
# '.': 빈칸, '#': 장애물 또는 벽, 'O': 구멍의 위치, 'R': 빨간 구슬의 위치, 'B': 파란 구슬의 위치
board = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

visit = set()
visit.add((rx, ry, bx, by))
que = deque()
que.append([rx, ry, bx, by, 0])

def move(x, y, i, j):
    cnt = 0
    while board[x+i][y+j] != '#' and board[x][y] != 'O':
        x += i
        y += j
        cnt += 1

    return x, y, cnt

def bfs():
    while que:
        rx, ry, bx, by, cnt = que.popleft()
        if cnt > 10: continue
        if board[rx][ry] == 'O': return cnt
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] == 'O': continue
            if (nrx, nry) == (nbx, nby):
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visit:
                visit.add((nrx, nry, nbx, nby))
                que.append([nrx, nry, nbx, nby, cnt+1])
    return -1
print(bfs())