import sys

def dfs(x, y, area, cnt):
    if cnt >= 4:
        global ans
        ans = max(ans, area)
        return
    
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in move:
        if 0 <= x+r < n and 0 <= y+c < m and not visited[x+r][y+c]:
            visited[x+r][y+c] = True
            dfs(x+r, y+c, area+arr[x+r][y+c], cnt+1)
            visited[x+r][y+c] = False

def another(x, y):
    global ans
    move = [[(-1, 0), (1, 0), (0, -1)],
            [(-1, 0), (1, 0), (0, 1)],
            [(0, -1), (0, 1), (-1, 0)],
            [(0, -1), (0, 1), (1, 0)]
    ]

    for case in range(4):
        area = arr[x][y]
        for r, c in move[case]:
            if 0 <= x+r < n and 0 <= y+c < m:
                area += arr[x+r][y+c]
        
        ans = max(ans, area)

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = False
        another(i, j)

print(ans)