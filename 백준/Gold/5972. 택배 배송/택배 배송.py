import sys
import heapq

n, m = map(int, sys.stdin.readline().strip().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    arr[a].append([c, b])
    arr[b].append([c, a])

def dijkstra():
    heap = []
    dp = [float('inf') for _ in range(n+1)]
    heapq.heappush(heap, [0, 1])

    while heap:
        cow, idx = heapq.heappop(heap)
        if cow <= dp[idx]:
            for next_cow, next_idx in arr[idx]:
                sum_cow = next_cow + cow
                if dp[next_idx] > sum_cow:
                    dp[next_idx] = sum_cow
                    heapq.heappush(heap, [sum_cow, next_idx])
    
    return dp

ans = dijkstra()
print(ans[n])