import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

from math import ceil, log2

# K개 줄에 D, E를 연결하는 경로에서 가장 짧은 도로의 길이와 가장 긴 도로의 길이를 출력

# N (2 <= N <= 100,000)
N = int(input().strip())

road = [[] for _ in range(N + 1)]  # 도로 정보
depth = [0] * (N + 1)  # 깊이
visit = [0] * (N + 1)

size = int(ceil(log2(N + 1)))
parent = [[0]*(N+1) for _ in range(size)]
MIN = [[float('inf')]*(N+1) for _ in range(size)]
MAX = [[-float('inf')]*(N+1) for _ in range(size)]
# 세 정수 A, B, C; A와 B사이 길이가 C인 도로; (1 <= A, B <= N); (1  <= C <= 100,000)
for _ in range(N - 1):
    A, B, C = map(int, input().strip().split())
    road[A].append([B, C])
    road[B].append([A, C])


def dfs(x, d):
    visit[x] = 1
    depth[x] = d

    for nx, nd in road[x]:
        if visit[nx]: continue

        parent[0][nx] = x
        MIN[0][nx] = nd
        MAX[0][nx] = nd
        dfs(nx, d + 1)

def set_table():
    dfs(1, 0)

    for i in range(1, size):
        for j in range(1, N+1):
            parent[i][j] = parent[i-1][parent[i-1][j]]
            MIN[i][j] = min(MIN[i-1][j], MIN[i-1][parent[i-1][j]])
            MAX[i][j] = max(MAX[i-1][j], MAX[i-1][parent[i-1][j]])

set_table()

def lca(a, b):
    ans = [10**6, 0]

    if depth[a] < depth[b]:
        a, b = b, a

    for i in range(size-1, -1, -1):
        if depth[a]-depth[b] >= (1 << i):
            ans[0] = min(ans[0], MIN[i][a])
            ans[1] = max(ans[1], MAX[i][a])
            a = parent[i][a]

    if a == b: return ans
    else:
        for i in range(size-1, -1, -1):
            if parent[i][a] != parent[i][b]:
                ans[0] = min(ans[0], MIN[i][a], MIN[i][b])
                ans[1] = max(ans[1], MAX[i][a], MAX[i][b])
                a = parent[i][a]
                b = parent[i][b]

        ans[0] = min(ans[0], MIN[0][a], MIN[0][b])
        ans[1] = max(ans[1], MAX[0][a], MAX[0][b])

        return ans

# K (1 <= K <= 100,000)
K = int(input().strip())

# D, E (1 <= D, E <= N)
for _ in range(K):
    D, E = map(int, input().strip().split())
    print(*lca(D, E))