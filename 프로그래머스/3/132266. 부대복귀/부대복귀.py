# 3 <= n <= 100,000
# 2 <= len(roads) <= 500,000

def solution(n, roads, sources, destination):
    global graph
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = []
    arr = dijkstra(destination, n)
    for x in sources:
        if arr[x] == float('inf'):
            answer.append(-1)
        else:
            answer.append(arr[x])
    return answer

from heapq import heappush, heappop
def dijkstra(end, n):
    dp = [float('inf')]*(n+1)
    dp[end] = 0
    
    heap = [(end, 0)]
    while heap:
        x, dist = heappop(heap)
        if dist > dp[x]:
            continue
        
        for nx in graph[x]:
            if dist+1 >= dp[nx]:
                continue
                
            dp[nx] = dist+1
            heappush(heap, (nx, dist+1))
    
    return dp

'''
총 지역의 수 n
간선 정보 roads
부대원 위치 sources
부대 위치 destination

'''