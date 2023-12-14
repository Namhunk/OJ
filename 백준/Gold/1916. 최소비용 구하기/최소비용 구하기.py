import sys
import heapq

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().strip().split())
    graph[s].append([c, e])

start, end = map(int, sys.stdin.readline().strip().split())

def dijkstra(start):
    heap = []
    dp = [float('inf') for _ in range(N+1)]
    dp[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        c, n = heapq.heappop(heap)
        if c > dp[n]: continue

        for c_n, n_e in graph[n]:
            n_w = c_n + c
            if dp[n_e] > n_w:
                dp[n_e] = n_w
                heapq.heappush(heap, [n_w, n_e])
    
    return dp

ans = dijkstra(start)
print(ans[end])
