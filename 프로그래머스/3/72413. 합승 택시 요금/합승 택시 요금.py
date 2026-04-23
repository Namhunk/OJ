from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    # 각 위치마다 이동 가능 경로와 요금 저장
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
    
    base = dijkstra(n, s, graph)
    answer = base[a] + base[b] # 기본값 서로 합승을 하지 않는 방법
    for i in range(1, n+1):
        curr = dijkstra(n, i, graph)
        answer = min(answer, curr[a] + curr[b] + base[i])
        
    return answer

def dijkstra(n, s, graph): # n: 배열의 크기, s: 시작지점
    dp = [float('inf')]*(n+1)
    dp[s] = 0
    
    heap = [(0, s)]
    while heap:
        c, x = heappop(heap)
        if c > dp[x]: continue
        
        for nc, nx in graph[x]:
            SUM = c + nc
            if SUM >= dp[nx]: continue
            
            dp[nx] = SUM
            heappush(heap, (SUM, nx))
    
    return dp
                

"""
지점의 개수 n (3 <= n <= 200)
출발지점 s, A의 도착지점 a, B의 도착지점 b (1 <= a, s, b <= n | a!=b!=s)
요금 fares (2 <= fares <= n x (n-1) / 2)

두 사람 A, B가 있을때, 방향이 같다면 합승을 해서 요금을 절약
합승을 안하는게 더 적다면 합승 x

"""