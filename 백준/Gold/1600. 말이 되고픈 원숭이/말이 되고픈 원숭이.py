from collections import deque
import sys

def bfs(i, j, count):
    visited = [[[float('inf')]*(k+1) for _ in range(w)] for _ in range(h)]
    visited[i][j] = [0]*(count+1)

    que = deque([(i, j, count)])
    while que:
        for _ in range(len(que)):
            x, y, cnt = que.popleft()
            if x == h-1 and y == w-1: return visited[x][y][cnt]

            if cnt:
                for r, c in udlr:
                    if 0 <= x+r < h and 0 <= y+c < w and visited[x+r][y+c][cnt] == float('inf') and not arr[x+r][y+c]:
                        visited[x+r][y+c][cnt] = visited[x][y][cnt] + 1
                        que.append((x+r, y+c, cnt))
                
                for r, c in horse:
                    if 0 <= x+r < h and 0 <= y+c < w and visited[x+r][y+c][cnt-1] == float('inf') and not arr[x+r][y+c]:
                        visited[x+r][y+c][cnt-1] = visited[x][y][cnt] + 1
                        que.append((x+r, y+c, cnt-1))
            else:
                for r, c in udlr:
                    if 0 <= x+r < h and 0 <= y+c < w and visited[x+r][y+c][cnt] == float('inf') and not arr[x+r][y+c]:
                        visited[x+r][y+c][cnt] = visited[x][y][cnt] + 1
                        que.append((x+r, y+c, cnt))
    
    return -1

k = int(sys.stdin.readline().strip())
w, h = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

horse = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
udlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(bfs(0, 0, k))