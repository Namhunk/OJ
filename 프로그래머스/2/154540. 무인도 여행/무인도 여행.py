from collections import deque
# 3 <= len(maps) <= 100
# 3 <= len(maps[i]) <= 100
def solution(maps):
    answer = []
    
    N, M = len(maps), len(maps[0])
    q = deque()
    
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동
    visit = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'X': continue
            if visit[i][j]: continue
            visit[i][j] = True
            answer.append(int(maps[i][j]))
            q.append((i, j))
            
            while q:
                x, y = q.popleft()
                for r, c in move:
                    nx, ny = x+r, y+c
                    if not (0 <= nx < N and 0 <= ny < M and not visit[nx][ny]): continue
                    if maps[nx][ny] == 'X': continue
                    visit[nx][ny] = True
                    answer[len(answer)-1] += int(maps[nx][ny])
                    q.append((nx, ny))
        
        if len(answer):
            answer.sort()
        else:
            answer.append(-1)
    
    return answer

"""
X: 바다
1 ~ 9: 식량의 개수


"""