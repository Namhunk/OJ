from collections import deque
import sys

#입력값
n, m, k = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
parr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]

#이동
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pat = []
for i in range(5):
    for j in range(5):
        if parr[i][j]: pat.append((i-2, j-2))

#배열, bfs
visited = [[[[-1]*2 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
visited[0][0][k][0] = 0

que = deque([(0, 0, k, 0)])
while que:
    x, y, cnt, visit = que.popleft()
    for r, c in move:
        if 0 <= x+r < n and 0 <= y+c < m and arr[x+r][y+c] != 1:
            if visit:
                if visited[x+r][y+c][cnt][visit] < 0:
                    visited[x+r][y+c][cnt][visit] = visited[x][y][cnt][visit] + 1
                    if (x+r, y+c) == (n-1, m-1): print(visited[x+r][y+c][cnt][visit]); exit()
                    que.append((x+r, y+c, cnt, visit))
            
            else:
                if arr[x+r][y+c] != 2:
                    if visited[x+r][y+c][cnt][visit] < 0:
                        visited[x+r][y+c][cnt][visit] = visited[x][y][cnt][visit] + 1
                        que.append((x+r, y+c, cnt, visit))
                else:
                    if visited[x+r][y+c][cnt][visit+1] < 0:
                        visited[x+r][y+c][cnt][visit+1] = visited[x][y][cnt][visit] + 1
                        if (x+r, y+c) == (n-1, m-1): print(visited[x+r][y+c][cnt][visit+1]); exit()
                        que.append((x+r, y+c, cnt, visit+1))
    
    if cnt:
        for r, c in pat:
            if 0 <= x+r < n and 0 <= y+c < m and arr[x+r][y+c] != 1:
                if visit:
                    if visited[x+r][y+c][cnt-1][visit] < 0:
                        visited[x+r][y+c][cnt-1][visit] = visited[x][y][cnt][visit] + 1
                        if (x+r, y+c) == (n-1, m-1): print(visited[x+r][y+c][cnt-1][visit]); exit()
                        que.append((x+r, y+c, cnt-1, visit))
                
                else:
                    if arr[x+r][y+c] != 2:
                        if visited[x+r][y+c][cnt-1][visit] < 0:
                            visited[x+r][y+c][cnt-1][visit] = visited[x][y][cnt][visit] + 1
                            que.append((x+r, y+c, cnt-1, visit))
                    else:
                        if visited[x+r][y+c][cnt-1][visit+1] < 0:
                            visited[x+r][y+c][cnt-1][visit+1] = visited[x][y][cnt][visit] + 1
                            if (x+r, y+c) == (n-1, m-1): print(visited[x+r][y+c][cnt-1][visit+1]); exit()
                            que.append((x+r, y+c, cnt-1, visit+1))
print(-1)