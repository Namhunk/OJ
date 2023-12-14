from collections import deque
import sys

while True:
    w, h = map(int, sys.stdin.readline().strip().split())
    if not w and not h: break

    Map = []
    for _ in range(h):
        Map.append(list(map(int, sys.stdin.readline().strip().split())))
    
    s = 0
    visited = [[True for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if visited[i][j]:
                visited[i][j] = False
                if Map[i][j] == 1:
                    s += 1
                    que = deque()
                    que.append((i, j))
                    while que:
                        x, y = que.popleft()
                        for k in range(-1, 2, 2):
                            if 0 <= x+k < h and visited[x+k][y] and Map[x+k][y] == 1:
                                visited[x+k][y] = False
                                que.append((x+k, y))
                            if 0 <= y+k < w and visited[x][y+k] and Map[x][y+k] == 1:
                                visited[x][y+k] = False
                                que.append((x, y+k))
                            if 0 <= x+k < h and 0 <= y+k < w and visited[x+k][y+k] and Map[x+k][y+k] == 1:
                                visited[x+k][y+k] = False
                                que.append((x+k, y+k))
                            if 0 <= x+k < h and 0 <= y+(-1*k) < w and visited[x+k][y+(-1*k)] and Map[x+k][y+(-1*k)] == 1:
                                visited[x+k][y+(-1*k)] = False
                                que.append((x+k, y+(-1*k)))
                                
    print(s)