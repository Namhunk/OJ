# 1 <= n <= 100
# len(cost) <= (n-1)*n / 2
def solution(n, costs):
    graph = [[] for _ in range(n)]
    for a, b, c in costs:
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    answer = prim(graph, n)
    return answer

from heapq import heappush, heappop
def prim(graph, n):
    res = 0
    cnt = 0
    visit = [False]*n
    heap = [(0, 0)]
    
    while heap:
        c, x = heappop(heap)
        if visit[x]: continue
        visit[x] = True
        res += c
        cnt += 1
        
        for nc, nx in graph[x]:
            heappush(heap, (nc, nx))
        
    return res
    
"""
n개의 섬 사이에 다리를 건설하는 비용이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록
만드려 할 때 필요한 최소 비용


"""