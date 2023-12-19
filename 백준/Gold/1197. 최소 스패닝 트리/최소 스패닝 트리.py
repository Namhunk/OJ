import sys, heapq

# 최소 스패닝 트리의 가중치 출력

# prim MST

# V, E
V, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

ans = 0
heap = [(0, 1)]
visit = [0] + [1]*(V)

while heap:
    cw, cn = heapq.heappop(heap)
    if visit[cn]:
        visit[cn] = 0
        ans += cw
        for nw, nn in graph[cn]:
            if visit[nn]:
                heapq.heappush(heap, (nw, nn))

print(ans)