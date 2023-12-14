import sys, heapq

N, M, X = map(int, sys.stdin.readline().strip().split())
go_arr = [[] for _ in range(N+1)]
back_arr = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().strip().split())
    go_arr[s].append([e, t])
    back_arr[e].append([s, t])

go_dp = [float('inf')] * (N+1)
back_dp = [float('inf')] * (N+1)
go_dp[X], back_dp[X] = 0, 0

def go_dijk():
    heap = [[0, X]]
    while heap:
        time, idx = heapq.heappop(heap)

        if time <= go_dp[idx]:
            for next in go_arr[idx]:
                if next[1] + time < go_dp[next[0]]:
                    go_dp[next[0]] = next[1]  + time
                    heapq.heappush(heap, [go_dp[next[0]], next[0]])

def back_dijk():
    heap = [[0, X]]
    while heap:
        time, idx = heapq.heappop(heap)

        if time <= back_dp[idx]:
            for next in back_arr[idx]:
                if next[1] + time < back_dp[next[0]]:
                    back_dp[next[0]] = next[1] + time
                    heapq.heappush(heap, [back_dp[next[0]], next[0]])

go_dijk()
back_dijk()
ans = 0
for i in range(1, N+1):
    ans = max(ans, go_dp[i] + back_dp[i])

print(ans)