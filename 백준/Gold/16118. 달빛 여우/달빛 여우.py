import sys
input = sys.stdin.readline

def solve():
    # N, M (2 <= N <= 4,000, 1 <= M <= 100,000)
    N, M = map(int, input().strip().split())
    fox_graph  = [[] for _ in range(N+1)]
    wolf_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, d = map(int, input().strip().split())
        fox_graph[a].append((d, b))
        fox_graph[b].append((d, a))
        
        wolf_graph[a].append((d/2, d*2, b))
        wolf_graph[b].append((d/2, d*2, a))
    
    fox  = fox_dijkstra(N, fox_graph)
    wolf = wolf_dijkstra(N, wolf_graph)

    ans = 0
    for i in range(2, N+1):
        if fox[i] < min(wolf[i]):
            ans += 1

    print(ans)
from heapq import heappush, heappop
def fox_dijkstra(N, graph):
    dp = [float('inf')]*(N+1)
    dp[1]= 0

    heap = [(0, 1)] # 횟수, 거리, 위치
    while heap:
        d, x = heappop(heap)
        if dp[x] < d: continue

        for nd, nx in graph[x]:
            dist = nd + d
            if dp[nx] <= dist: continue
            dp[nx] = dist
            heappush(heap, (dist, nx))

    return dp

def wolf_dijkstra(N, graph):
    dp = [[float('inf')]*2 for _ in range(N+1)]
    dp[1][0] = 0

    heap = [(0, 0, 1)]
    while heap:
        d, c, x = heappop(heap)
        if dp[x][c] < d: continue

        for nfd, nsd, nx in graph[x]:
            if c == 0:
                dist = nfd + d
            else:
                dist = nsd + d
            
            if dp[nx][c^1] <= dist: continue
            dp[nx][c^1] = dist
            heappush(heap, (dist, c^1, nx))
    
    return dp

if __name__ == '__main__':
    solve()

"""

"""