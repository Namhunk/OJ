import heapq
 
def solution(board):
    n = len(board)
    INF = float('inf')

    dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    heap = [(0, 0, 0, -1)]
    answer = INF
    
    while heap:
        cost, r, c, d = heapq.heappop(heap)
        if r == n - 1 and c == n - 1:
            answer = min(answer, cost)
            continue
            
        if d != -1 and cost > dist[r][c][d]:
            continue
            
        for nd, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                add = 100 if (d == -1 or d == nd) else 600  # 직진 100 / 코너 500+100
                ncost = cost + add
                if ncost < dist[nr][nc][nd]:
                    dist[nr][nc][nd] = ncost
                    heapq.heappush(heap, (ncost, nr, nc, nd))
                    
    return answer