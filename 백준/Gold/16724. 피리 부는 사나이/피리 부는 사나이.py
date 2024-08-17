import sys
input = sys.stdin.readline

# 첫 번째 줄에 'SAFE ZONE'의 최소 개수를 출력한다

# 지도의 행, 열의 수 N(1 <= N <= 1,000), M(1 <= M <= 1000)
N, M = map(int, input().strip().split())

# N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열
MAP = [list(input().strip()) for _ in range(N)]

# 성우가 정해 놓은 방향
# U : 위, D : 아래, L : 왼쪽, R : 오른쪽
# 지도가 주어졌을 때 어느 위치에 있더라도 피리를 불 때, 'SAFE ZONE'에 들어갈 수 있게 하는 'SAFE ZONE'의 최소 개수
# 지도 밖으로 나가는 방향의 입력은 주어지지 않음

# 지도 밖으로 나가는 경우가 없을 때 사이클의 개수 만큼 추가

visit= [[-1]*M for _ in range(N)]
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

cnt = 0
def dfs(x, y):
    global cnt
    visit[x][y] = 0 # 현재 위치 방문 표시
    r, c = move[MAP[x][y]] # 이동 방향
    nx, ny = x+r, y+c # 다음 위치

    if visit[nx][ny] < 0: # 다음 위치를 아직 방문하지 않았다면
        visit[x][y] = dfs(nx, ny) # 다음 위치 방문
    elif visit[nx][ny] < 1: # 현재 사이클의 끝이라면 
        cnt += 1 # 번호 1 증가
        visit[x][y] = cnt # 새로운 사이클 생성
    else: # 이전 사이클에 포함되는 경우라면
        visit[x][y] = visit[nx][ny]

    return visit[x][y]

ans = 0 # 정답 변수
for i in range(N):
    for j in range(M):
        if visit[i][j] < 0: # 아직 방문하지 않았다면
            visit[i][j] = 0
            dfs(i, j)

        if visit[i][j] > ans:
            ans = visit[i][j]

print(ans)