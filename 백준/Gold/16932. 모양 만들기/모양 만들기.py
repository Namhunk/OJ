import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # N, M (2 <= N, M <= 1,000)
    N, M = map(int, input().strip().split())
    
    arr = [list(map(int, input().strip().split())) for _ in range(N)]

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 이동 방향

    visit = [[0]*M for _ in range(N)] # 방문을 표시할 배열
    num = 1 # 현재 위치가 어떤 집단에 속하는지
    area_cnt = {} # 각 집단의 개수

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visit[i][j] == 0: # 방문하지 않았고 1을 가진 위치라면
                visit[i][j] = num
                cnt = 1
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for r, c in move:
                        nx, ny = x+r, y+c

                        if not (0 <= nx < N and 0 <= ny < M): continue
                        if not (visit[nx][ny] == 0 and arr[nx][ny] == 1): continue
                        visit[nx][ny] = num
                        cnt += 1
                        q.append((nx, ny))
                
                area_cnt[num] = cnt
                num += 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0: # 0인 값들에 대해서
                connect = set()
                temp = 0
                for r, c in move:
                    ni, nj = i+r, j+c
                    if not (0 <= ni < N and 0 <= nj < M): continue
                    if visit[ni][nj] > 0:
                        connect.add(visit[ni][nj])
                
                for k in connect:
                    temp += area_cnt[k]
                
                ans = max(ans, temp+1)
    
    print(ans)

if __name__ == '__main__':
    solve()

"""
N x M 인 배열에서 모양을 찾으려 함
배열의 각 칸에는 0 or 1 이 존재, 두 칸이 서로 변을 공유할떄
두 칸을 인접하다고 한다.

배열의 칸 하나에 들어있는 수를 변경해서 만들 수 있는 모양의 최대 크기를 구해라

배열에서 0값을 갖는 위치들 중 하나만을 1로 바꿨을 때
가장 큰 크기

크기는 1의 값을 갖는 위치들끼리 대각선이 아닌 상하좌우로 인접해야 함

"""