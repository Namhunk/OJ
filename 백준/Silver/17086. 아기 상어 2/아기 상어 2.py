import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # 공간의 크기 N, M (2 <= N, M <= 50)
    N, M = map(int, input().strip().split())

    # N개의 줄에 공간의 상태가 주어짐 빈칸: 0, 상어: 1
    visit = [[-1]*M for _ in range(N)]
    q = deque()

    for i in range(N):
        row = list(map(int, input().strip().split()))
        for j in range(M):
            if row[j] == 1:
                visit[i][j] = 0
                q.append((i, j))
    
    ans = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for r in range(-1, 2):
                for c in range(-1, 2):
                    if (r, c) == (0, 0): continue
                    
                    nx, ny = x+r, y+c
                    if not (0 <= nx < N and 0 <= ny < M): continue
                    if visit[nx][ny] < 0:
                        visit[nx][ny] = visit[x][y] + 1
                        q.append((nx, ny))
                    
                    if visit[nx][ny] > ans:
                        ans = visit[nx][ny]
    
    print(ans)

if __name__ == '__main__':
    solve()

"""
안전거리의 최댓값을 출력

방향은 x -> -1, 0, 1, y -> -1, 0, 1 단 x, y = (0, 0) 은 불가능

"""