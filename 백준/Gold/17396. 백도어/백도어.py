import sys
import heapq

n, m = map(int, sys.stdin.readline().strip().split())
sight = list(map(int, sys.stdin.readline().strip().split()))
sight[n-1] = 0

arr = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().strip().split())
    arr[a].append([b, t])
    arr[b].append([a, t])

def dijkstra():
    dp = [float('inf') for _ in range(n)]
    heap = []
    heapq.heappush(heap, [0, 0])
    dp[0] = 0

    while heap:
        time, idx = heapq.heappop(heap)

        if time <= dp[idx]:
            for next_ in arr[idx]:
                sum_time = time + next_[1]

                if sum_time < dp[next_[0]] and not sight[next_[0]]:
                    dp[next_[0]] = sum_time
                    heapq.heappush(heap, [sum_time, next_[0]])
    
    return dp[n-1]

ans = dijkstra()
print(ans if ans != float('inf') else -1)
