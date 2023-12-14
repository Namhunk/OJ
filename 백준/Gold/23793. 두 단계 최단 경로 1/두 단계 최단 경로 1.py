import sys, heapq

N, M = map(int, sys.stdin.readline().strip().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    arr[u].append([v, w])

X, Y, Z = map(int, sys.stdin.readline().strip().split())

def dijkstra(start, end, check):
    dp = [float('inf') for _ in range(N+1)]
    dp[start] = 0

    heap = [[0, start]]
    while heap:
        weight, idx = heapq.heappop(heap)

        if weight <= dp[idx]:
            for next_idx, next_weight in arr[idx]:
                sum_weight = weight + next_weight

                if check and next_idx == Y: continue
                if sum_weight < dp[next_idx]:
                    dp[next_idx] = sum_weight
                    heapq.heappush(heap, [sum_weight, next_idx])
    
    return dp[end]

ans1 = dijkstra(X, Y, False) + dijkstra(Y, Z, False)
ans2 = dijkstra(X, Z, True)

check = (lambda x: x if x != float('inf') else -1)
print(check(ans1), check(ans2))