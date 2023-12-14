import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())

arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    arr[u].append([v, w])

def dijkstra(K):
    dp = [float("inf") for _ in range(V+1)]
    dp[K] = 0
    heap = []
    heapq.heappush(heap, [0, K])

    while heap:
        cost, idx = heapq.heappop(heap)

        if cost <= dp[idx]:
            for  next_idx, next_cost in arr[idx]:
                sum_cost = cost + next_cost

                if sum_cost < dp[next_idx]:
                    dp[next_idx] = sum_cost
                    heapq.heappush(heap, [sum_cost, next_idx])
    
    return dp

ans = dijkstra(K)
for i in range(1, V+1):
    print(ans[i] if ans[i] != float('inf') else "INF")