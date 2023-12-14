import sys
import heapq

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0

while True:
    cnt += 1

    n = int(sys.stdin.readline().strip())
    if not n: break

    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    visit = [[True]*n for _ in range(n)]
    heap = [(arr[0][0], 0, 0)]
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        if visit[x][y]:
            visit[x][y] = False

            if (x, y) == (n-1, n-1): print(f'Problem {cnt}: {cost}'); break

            for r, c in move:
                if 0 <= x+r < n and 0 <= y+c < n and visit[x+r][y+c]:
                    heapq.heappush(heap, [cost+arr[x+r][y+c], x+r, y+c])