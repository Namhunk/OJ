import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # N (5 <= N <= 200)
    N = int(input().strip())

    # (r1, c1) -> (r2, c2) 최소 이동 횟수
    r1, c1, r2, c2 = map(int, input().strip().split())

    # 횟수 저장
    visit = [[-1]*N for _ in range(N)]
    visit[r1][c1] = 0

    move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

    q = deque([(r1, c1)])
    while q:
        x, y = q.popleft()

        if (x, y) == (r2, c2):
            return visit[x][y]

        for r, c in move:
            nx, ny = x+r, y+c

            if not (0 <= nx < N and 0 <= ny < N): continue
            if visit[nx][ny] >= 0: continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))
        
    return -1
   
if __name__ == '__main__':
    print(solve())

"""
데스나이트가 (r, c) 라면 (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1) 중 
한 곳으로 이동 가능

체스판의 행, 열은 0, 0 부터 시작
BFS 로 이동
"""