import sys
INF = sys.maxsize

from heapq import heappush, heappop
def solution(n, edge):
    vertex = [[] for _ in range(n+1)] # 이동 경로
    for a, b in edge:
        vertex[a].append(b)
        vertex[b].append(a)
    
    arr = dijkstra(1, n, vertex)
    MAX = max(arr[2:])
    answer = 0
    for i in range(2, n+1):
        if arr[i] == MAX:
            answer += 1
    return answer

def dijkstra(x, n, vertex):
    dp = [INF]*(n+1)
    dp[x] = 0
    heap = [(0, x)]
    while heap:
        d, x = heappop(heap)
        if d > dp[x]: continue
        
        for nx in vertex[x]:
            if d+1 >= dp[nx]: continue
            dp[nx] = d+1
            heappush(heap, (d+1, nx))
    
    return dp
"""
n개의 노드가 있는 그래프가 있음
각 노드는 1 - n 의 숫자
1번 노드에서 가장 멀리 떨어진 노드의 개수를 구해라
가장 멀리 떨어진 노드란 최단 경로로 이동했을 때
간선의 개수가 가장 많은 노드


"""