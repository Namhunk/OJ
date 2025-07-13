import sys
input = sys.stdin.readline

# M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다

# 노드의 개수 N (2 <= N <= 100,000)
N = int(input().strip())

graph = [[] for _ in range(N+1)] # 각 노드와 연결된 다른 노드 표시
parent = [0]*(N+1) # 부모 노드 표시
depth = [0]*(N+1) # 각 노드의 깊이
visit = [0]*(N+1) # 깊이 계산 여부

# 트리 상에서 연결된 두 정점
for _ in range(N-1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

que = deque([[1, 0]])
while que:
    x, d = que.popleft() # 현재 노드, 깊이
    visit[x] = 1 # 방문표시
    depth[x] = d # 깊이
    for nx in graph[x]:
        if visit[nx]: continue # 방문하지 않은 노드 중
        parent[nx] = x # 부모 노드 표시
        que.append([nx, d+1]) # 다음 노드, 깊이 + 1

from math import ceil, log2

size = int(ceil(log2(N+1))) # 깊이의 최대
table = [[0]*(N+1) for _ in range(size+1)] # 부모를 저장할 table

for i in range(1, N+1):
    table[0][i] = parent[i] # 가장 가까운 부모 표시

for i in range(1, size+1):
    for j in range(1, N+1):
        table[i][j] = table[i-1][table[i-1][j]] # 이전 부모의 부모를 테이블에 저장

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a # a의 깊이가 더 깊게

    for i in range(size, -1, -1):
        if depth[a]-depth[b] >= (1 << i):
            a = table[i][a] # 더 깊이가 깊은 a의 부모를 찾음

    if a == b: return a # 두 조상이 같다면 반환
    else:
        for i in range(size, -1, -1):
            if table[i][a] != table[i][b]: # 깊이가 같을 때, 두 조상이 같을 때 까지
                a = table[i][a]
                b = table[i][b]

    return table[0][a]

# 공통 조상을 알고싶은 쌍의 개수 M (1 <= M <= 100,000)
M = int(input().strip())

# 각 정점 쌍
for _ in range(M):
    a, b = map(int, input().strip().split())
    ans = lca(a, b)
    print(ans)
