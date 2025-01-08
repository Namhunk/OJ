import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 자료구조, 트리, 최소 공통 조상

# M개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다

# N개의 정점으로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 떄 두 노드 사이의 거리를 출력하라

def dfs(now, pre, dep, d): # 각 정점들의 부모, 부모와의 거리, 깊이를 구함
    visit[now] = 1
    depth[now] = dep

    for next, dist in graph[now]: # 현재 정점과 연결된 다음 정점들 중
        if visit[next] == 0: # 아직 방문하지 않은 정점들만 수행
            dfs(next, now, dep+1, dist)

    parent[now] = [pre, d]

def lca(a, b, size): # 최소 공통 조상, 거리를 구함
    if depth[a] < depth[b]:
        a, b = b, a

    ans = 0
    for i in range(size, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a, d = table[i][a]
            ans += d

    if a == b:
        return ans
    else:
        for i in range(size, -1, -1):
            if table[i][a][0] != table[i][b][0]:
                a, d1 = table[i][a]
                b, d2 = table[i][b]
                ans += (d1+d2)

        ans += (table[0][a][1] + table[0][b][1])
        return ans

# 첫째 줄에 노드의 개수 N (2 <= N <= 40,000) 입력
N = int(input().strip())

graph = [[] for _ in range(N+1)] # 각 정점들의 연결
parent = [[-1, 0] for _ in range(N+1)] # 각 정점들의 부모, 부모와의 거리
depth = [0 for _ in range(N+1)] # 각 정점들의 깊이
visit = [0 for _ in range(N+1)] # 각 정점들의 방문 상태


# N-1개의 줄에 트리 상에 연결된 두 점과 거리를 입력
for _ in range(N-1):
    x, y, d = map(int, input().strip().split())
    graph[x].append([y, d])
    graph[y].append([x, d])

dfs(1, -1, 0, 0)

size = int(math.ceil(math.log2(N+1)))
table = [[[0, 0] for _ in range(N+1)] for _ in range(size+1)]

for i in range(1, N+1):
    table[0][i] = [parent[i][0], parent[i][1]]

for k in range(1, size+1):
    for i in range(1, N+1):
        table[k][i] = [
            table[k-1][table[k-1][i][0]][0],
            table[k-1][table[k-1][i][0]][1] + table[k-1][i][1]
        ]

# M (1 <= M <= 10,000) 입력
M = int(input().strip())

# M개의 줄에 거리를 알고 싶은 노드 쌍이 한 줄에 한 쌍씩 입력된다, 두 점 사이 거리는 10,000보다 작거나 같은 자연수
for _ in range(M):
    x, y = map(int, input().strip().split())
    print(lca(x, y, size))