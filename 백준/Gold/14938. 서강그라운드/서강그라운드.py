import sys, heapq

# 얻을 수 있는 최대 아이템의 개수
# 어떤 지점에 떨어졌을때 다른 지역으로 이동하는 길이가 수색 범위를 넘으면 안됨

# 다익스트라로 현재 위치에 떨어졌을때 다른 지점까지의 최소 거리를 구함
def dijkstra(x):
    heap = [(0, x)]
    dp = [float('inf')] * (n+1)
    dp[x] = 0
    while heap:
        d, now = heapq.heappop(heap)
        if d <= dp[now]:
            for nd, nnow in graph[now]:
                SUM = nd + d
                if SUM < dp[nnow]:
                    dp[nnow] = SUM
                    heapq.heappush(heap, (SUM, nnow))
    
    # 수색 범위보다 작은 거리의 지역을 구해 아이템의 개수를 저장
    result = 0 # 아이템의 개수
    for i in range(1, n+1):
        if dp[i] <= m:
            result += t[i]
    
    return result
    

# n = 지역의 개수, m = 수색 범위, r = 길의 개수
n, m, r = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]

# t = 아이템의 수
t = [0] + list(map(int, sys.stdin.readline().strip().split()))
for _ in range(r):
    # a, b = 지역의 번호, l = 길의 길이
    a, b, l = map(int, sys.stdin.readline().strip().split())
    graph[a].append([l, b]) # a 지점에서 l의 거리인 b와 연결됨
    graph[b].append([l, a]) # 위와 반대

ans = 0 # 최대값
for i in range(1, n+1):
    ans = max(ans, dijkstra(i))

print(ans)