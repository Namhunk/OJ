import sys
import heapq

N, E = map(int, sys.stdin.readline().strip().split())
arr = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().strip().split())

def dijkstra(start, end):
    dp = [float('inf') for _ in range(N+1)]
    dp[start] = 0
    
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        cost, idx = heapq.heappop(heap)

        if cost <= dp[idx]:
            for next_idx, next_cost in arr[idx]:
                sum_cost = cost + next_cost

                if sum_cost < dp[next_idx]:
                    dp[next_idx] = sum_cost
                    heapq.heappush(heap, [sum_cost, next_idx])
    
    return dp[end]

ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),\
          dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

print(ans if ans != float('inf') else -1)