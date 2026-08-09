from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = -1
    
    arr = []
    # 시작, 출구를 찾음
    for i in range(n):
        row = list(maps[i].strip())
        arr.append(row)
        
        for j in range(m):
            if row[j] == 'S': # 시작
                start = (i, j)
            if row[j] == 'E': # 종료
                end = (i, j)
            if row[j] == 'L': # 레버
                L = (i, j)
    
    S2L = bfs(start, L, n, m, arr) # start -> L 거리
    L2E = bfs(L, end, n, m, arr) # L -> end 거리
    
    if S2L == -1 or L2E == -1:
        return -1
    else:
        return S2L + L2E

def bfs(start, target, n, m, arr):
    visit = [[-1]*m for _ in range(n)] # 방문표시
    
    # 이동방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visit[start[0]][start[1]] = 0 # 시작위치 방문처리
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        if (x, y) == target:
                return visit[x][y]
            
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m): continue # 맵 범위를 벗어나는지
            if arr[nx][ny] == 'X': continue # 벽이 아닌지
            if visit[nx][ny] != -1: continue # 이미 방문했는지
            visit[nx][ny] = visit[x][y] + 1
            q.append((nx, ny))
            
    return -1
            
            
        
'''
5 <= len(maps) <= 100
5 <= len(maps[i]) <= 100

S: 시작
E: 출구
L: 레버
O: 통로
X: 벽

통로로만 이동 가능

'''