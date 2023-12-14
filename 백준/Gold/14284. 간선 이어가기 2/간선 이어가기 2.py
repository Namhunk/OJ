import sys
import heapq

n, m = map(int, sys.stdin.readline().strip().split())

arr = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    arr[a].append([c, b])
    arr[b].append([c, a])

s, t = map(int, sys.stdin.readline().strip().split())

def dijkstra(s, t):
    dp = [float('inf') for _ in range(n+1)]
    heap = []
    heapq.heappush(heap, [0, s])

    while heap:
        cost, idx = heapq.heappop(heap)

        if cost <= dp[idx]:
            for next_cost, next_idx in arr[idx]:
                sum_cost = cost + next_cost

                if dp[next_idx] > sum_cost:
                    dp[next_idx] = sum_cost
                    heapq.heappush(heap, [sum_cost, next_idx])
    
    return dp[t]

ans = dijkstra(s, t)
print(ans)