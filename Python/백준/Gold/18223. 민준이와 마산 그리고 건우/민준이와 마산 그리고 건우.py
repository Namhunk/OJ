import sys, heapq

V, E, P = map(int, sys.stdin.readline().strip().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

def dijkstra(start, end):
    dp = [float('inf') for _ in range(V+1)]
    dp[start] =  0
    heap = [[0, start]]

    while heap:
        cost, idx = heapq.heappop(heap)
        
        if cost <= dp[idx]:
            for next_idx, next_cost in arr[idx]:
                sum_cost = cost + next_cost

                if sum_cost < dp[next_idx]:
                    dp[next_idx] = sum_cost
                    heapq.heappush(heap, [sum_cost, next_idx])
    
    return dp[end]

MIN = dijkstra(1, V)
ans = dijkstra(1, P) + dijkstra(P, V)
print("SAVE HIM" if ans <= MIN else "GOOD BYE")