import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 두 수열의 길이 n (1 <= n <= 2e5)
n = int(input().strip())
# n개의 정수 a[1~n], (1 <= a[i] <= n)
a = [0] + list(map(int, input().strip().split()))
# n개의 정수 b[1~n], (1 <= b[i] <= n)
b = [0] + list(map(int, input().strip().split()))

# 모든 값은 1보다 작거나, n 보다 커지게 됨
G = [[] for _ in range(n+2)]
for x in range(1, n+1):
    G[max(0, x-a[x])].append((b[x], x)) # 모든 값은 0보다 큼
    G[min(n+1, x+a[x])].append((b[x], x)) # n+1 보다 작음

def dijkstra():
    heap = [[0, 0], [0, n+1]]
    dp = [float('inf')]*(n+2)
    dp[0] = dp[n+1] = 0

    while heap:
        t, x = heappop(heap)
        if t > dp[x]: continue

        for  nt, nx in G[x]:
            SUM = t+nt
            if SUM >= dp[nx]: continue
            dp[nx] = SUM
            heappush(heap, [SUM, nx])

    return dp[1:n+1]

print(*dijkstra())