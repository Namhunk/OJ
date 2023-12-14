import sys, heapq

m, n = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
wall = [[float('inf')]*m for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

wall[0][0] = 0
heap = [[0, 0, 0]]
while heap:
    cnt, x, y = heapq.heappop(heap)

    if cnt <= wall[x][y]:
        for r, c in move:
            if 0 <= x+r < n and 0 <= y+c < m:
                if wall[x][y] + arr[x+r][y+c] < wall[x+r][y+c]:
                    wall[x+r][y+c] = wall[x][y] + arr[x+r][y+c]
                    heapq.heappush(heap, [wall[x+r][y+c], x+r, y+c])

print(wall[n-1][m-1])