import sys, heapq

# 최소 스패닝 트리의 가중치 출력

# kruskal MST         

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: parent[y] = x
    else: parent[x] = y

# 정점의 개수 V, 간선의 수 E
V, E = map(int, sys.stdin.readline().strip().split())
# 간선 정보 입력
parent = [i for i in range(V+1)]
ans = 0
heap = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(heap, (C, A, B))

while heap:
    w, a, b = heapq.heappop(heap)
    if find(a) != find(b):
        union(a, b)
        ans += w
    
print(ans)