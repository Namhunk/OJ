import sys, heapq

def dijkstra(start):
    dp = [float('inf') for _ in range(n+1)]
    dp[start] = 0
    heap = [[0, start]]

    while heap:
        time, idx = heapq.heappop(heap)

        if time <= dp[idx]:
            for next_idx, next_time in arr[idx]:
                sum_time = time + next_time

                if sum_time < dp[next_idx]:
                    dp[next_idx] = sum_time
                    heapq.heappush(heap, [sum_time, next_idx])
    
    cnt, ans = 0, 0
    for i in dp:
        if i != float('inf'): cnt += 1; ans = max(ans, i)

    return cnt, ans

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().strip().split())
    arr = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().strip().split())
        arr[b].append([a, s])
    
    print(*dijkstra(c))