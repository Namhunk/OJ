import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # N, M (1 <= N, M <= 100), A(1 <= A), B(0 <= B)
    N, M, A, B = map(int, input().strip().split())

    # 맵 생성
    MAP = [[[0]*(A+1) for _ in range(M+1)] for _ in range(N+1)]

    # 방문 표시 배열(장애물 -1, 아직 지나가지 않았다면 0, 아이템은 1)
    visit = [[0]*(M+1) for _ in range(N+1)]

    # 아이템 위치마다 +1
    for _ in range(A):
        x, y = map(int, input().strip().split())
        visit[x][y] = 1
    
    # 장애물
    for _ in range(B):
        x, y = map(int, input().strip().split())
        visit[x][y] = -1
    
    cnt = 0
    MAP[1][1][0] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if visit[i][j] == 1:
                MAP[i][j][cnt+1] = MAP[i-1][j][cnt] + MAP[i][j-1][cnt]
                cnt += 1
            elif visit[i][j] == -1:
                continue
            else:
                MAP[i][j][cnt] += MAP[i-1][j][cnt] + MAP[i][j-1][cnt]
    
    print(MAP[N][M][A])

if __name__ == '__main__':
    solve()

"""
N x M 맵에 아이템, 장애물이 존재
맵 왼쪽 아래에서 오른쪽 위로 갈 예정
중간에 모든 아이템을 먹으려 함
이동은 오른쪽이나 위로만 갈 수 있음

이동하는 경로의 수를 구해라

모든 아이템을 먹으면서 최종 위치에 도착하는 경우

"""