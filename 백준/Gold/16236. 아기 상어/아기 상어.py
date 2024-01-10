import sys
from collections import deque

# 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어짐
# 0 : 빈칸
# 1, 2, 3, 4, 5, 6 : 칸에 있는 물고기의 크기
# 9 : 아기 상어의 위치(아기 상어는 공간에 한 마리 있다)

# 아기 상어의 처음 크기는 2(상, 하, 좌, 우 이동)
# 아기 상어는 크기가 작은 물고기만 먹을 수 있고 크기가 같으면 그 칸은 지나갈 수 있다.
# 아기 상어는 자신의 크기 개수만큼 물고기를 먹어야 크기가 +1 증가함

# 1. 먹을 수 있는 물고기가 공간에 없다면 엄마 상어에게 도움 요청
# 2. 먹을 수 있는 물고기가 1마리면 그 물고기를 먹으러감
# 3. 먹을 수 있는 물고기가 1마리 보다 많으면 거리가 가장 가까운 물고기를 먹으러감
# 4. 거리는 칸의 개수의 최솟값
# 5. 거리가 가까운 물고기가 많다면 가장 위, 그런 물고기가 여러마리면 가장 왼쪽
# (상어의 이동은 1초)

# 엄마 상어에게 도움을 요청하기 전 몇 초 동안 물고기를 잡아먹을 수 있는지 구해라

#arr 구성
N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
#이동 방향
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#최단 거리를 위한 값
INF = 1e9
#아기 상어 크기
shark_size = 2
#아기 상어의 현재 좌표
now_x, now_y = 0, 0

#아기 상어 초기 위치 확인
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            now_x, now_y = i, j
            arr[i][j] = 0

#현재 위치에서 각 물고기까지의 거리를 반환, 지나는 경로마다 값을 저장
def BFS():
    queue = deque([(now_x, now_y)])
    # 방문 여부
    visited = [[-1]*N for _ in range(N)]
    visited[now_x][now_y] = 0
    while queue:
        x, y = queue.popleft()

        for r, c in move:
            nx, ny = x + r, y + c
            #arr 범위 확인
            if 0 <= nx < N and 0 <= ny < N:
                #상어가 이동 가능한지 확인
                if shark_size >= arr[nx][ny] and visited[nx][ny] < 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

#먹을 물고기 찾기
def solve(visited):
    x, y = 0, 0
    time = INF
    for i in range(N):
        for j in range(N):
            #BFS에서 지나지 않는 경로는 최단 경로가 아님 + 아기 상어가 먹을 수 있는지 확인
            if visited[i][j] != -1 and 0 < arr[i][j] < shark_size:
                if visited[i][j] < time:
                    time = visited[i][j]
                    x, y = i, j
    #모두 탐색해도 그대로 INF이면 먹을 물고기가 없다는 것
    if time == INF:
        return False
    else:
        return x, y, time


answer = 0
food = 0

while True:
    result = solve(BFS())

    if not result:
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        arr[now_x][now_y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0