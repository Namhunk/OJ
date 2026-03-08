import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # H, W (0 <= H, W <= 100)
    H, W = map(int, input().strip().split())
    grid = []
    for _ in range(H):
        grid.append(list(input().strip()))
    
    visit = [[0]*W for _ in range(H)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    q = deque()
    # 맵 전체를 탐색
    for i in range(H):
        for j in range(W):
            if visit[i][j]: continue
            if grid[i][j] == '.': continue
            cnt += 1
            q.append((i, j))
            visit[i][j] = cnt
            while q:
                x, y = q.popleft()
                for r, c in move:
                    nx, ny = x+r, y+c
                    if not (0 <= nx < H and 0 <= ny < W): continue
                    if grid[nx][ny] == '.' or visit[nx][ny]: continue

                    visit[nx][ny] = cnt
                    q.append((nx, ny))
    
    return cnt

if __name__ == '__main__':
    # 테스트 케이스의 개수 T (0 <= T <= 100)
    T = int(input().strip())
    for _ in range(T):
        print(solve())

"""
양: #
풀: .



"""