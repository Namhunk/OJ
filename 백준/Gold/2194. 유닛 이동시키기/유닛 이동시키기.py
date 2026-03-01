import sys
input = sys.stdin.readline

from collections import deque

def build_prefix_sum(N, M, K):
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(lambda t: int(t) - 1, input().split())
        grid[x][y] = 1

    ps = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        row_sum = 0
        for j in range(M):
            row_sum += grid[i][j]
            ps[i + 1][j + 1] = ps[i][j + 1] + row_sum
    return ps

def rect_sum(ps, x1, y1, x2, y2):
    # x1, y1, x2, y2 모두 0-index, x2, y2 포함
    return ps[x2 + 1][y2 + 1] - ps[x1][y2 + 1] - ps[x2 + 1][y1] + ps[x1][y1]

def can_place(ps, N, M, A, B, x1, y1):
    # (x1, y1)를 왼쪽 위로 하는 A x B 유닛이 맵 안에 있고, 장애물이 없는지 확인
    x2 = x1 + A - 1
    y2 = y1 + B - 1
    if not (0 <= x1 < N and 0 <= y1 < M):
        return False
    if not (0 <= x2 < N and 0 <= y2 < M):
        return False
    return rect_sum(ps, x1, y1, x2, y2) == 0

def solve():
    # N, M: 맵의 크기, A, B: 유닛의 크기, K 장애물이 설치된 위치
    # (1 <= N, M <= 500), (1 <= A, B <= 10), (0 <= K <= 100,000)
    N, M, A, B, K = map(int, input().split())

    ps = build_prefix_sum(N, M, K)

    sx, sy = map(lambda t: int(t) - 1, input().split())
    ex, ey = map(lambda t: int(t) - 1, input().split())

    # 시작 지점에 유닛을 둘 수 없는 경우
    if not can_place(ps, N, M, A, B, sx, sy):
        print(-1)
        return

    dist = [[-1] * M for _ in range(N)]
    dist[sx][sy] = 0
    q = deque()
    q.append((sx, sy))

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        if (x, y) == (ex, ey):
            print(dist[x][y])
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if dist[nx][ny] != -1:
                continue
            # 유닛 전체가 맵 안 + 장애물 없는지
            if not can_place(ps, N, M, A, B, nx, ny):
                continue

            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

    # 도착 지점을 방문하지 못한 경우
    print(-1)
    
if __name__ == '__main__':
    solve()

"""
- N x M 크기의 맵이 있을 때, A x B 크기의 유닛을 S -> E로 이동 시키는 최소 이동 횟수
- 장애물은 K개
- 예제 1을 보면 유닛 위치의 왼쪽 상단을 기준으로 두는 것 같음
- 유닛은 상, 하, 좌, 우 4개의 방향으로만 이동이 가능함

1. BFS로 모든 경로 중 가장 빠른 경로로 
2. 모든 MAP의 초기 값은 -1 
3. 이동 중 현재 위치부터 AxB의 크기 여유가 있어야 함 (장애물이 없는 통로가 유닛의 크기 이상이어야 함)
4. 장애물은 누적합으로 AxB 크기 안에 장애물이 있는지 검사
"""