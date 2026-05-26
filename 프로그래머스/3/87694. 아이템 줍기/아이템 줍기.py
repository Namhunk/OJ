from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 2배 스케일 좌표
    sx, sy = characterX * 2, characterY * 2
    tx, ty = itemX * 2, itemY * 2

    # 맵 초기화
    arr = [[0] * 102 for _ in range(102)]

    # 직사각형 전체 영역 채우기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                arr[i][j] = 1

    # 내부 지우기 (테두리만 남기기)
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                arr[i][j] = 0

    # BFS
    q = deque()
    q.append((sx, sy))
    visited = [[0] * 102 for _ in range(102)]
    visited[sx][sy] = 1
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        x, y = q.popleft()
        if x == tx and y == ty:
            # 2배 스케일을 실제 거리로 환산
            return (visited[x][y] - 1) // 2

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))