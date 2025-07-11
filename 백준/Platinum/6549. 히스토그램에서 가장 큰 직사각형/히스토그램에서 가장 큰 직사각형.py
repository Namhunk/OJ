import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 히스토그램에서 가장 넓이가 큰 직사각형을 구해라

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(x,  y):
    x, y = find(x), find(y)

    if h[x] == 0: return
    if h[y] == 0: return

    if h[x] < h[y]:
        x, y = y, x

    parent[x] = y
    size[y] += size[x]


while 1:
    query = list(map(int, input().strip().split()))
    if len(query) == 1 and query[0] == 0: break
    # n (1 <= n <= 100,000); (0 <= h[i] <= 1,000,000,000)
    n, h = query[0], query[1:]

    parent = [i for i in range(n)]
    size = [1]*n
    visit = [False]*n

    ans = 0
    h_idx = sorted([(h[i], i) for i in range(n)], key=lambda x: -x[0])

    for height, idx in h_idx:
        visit[idx] = True
        if 0 <= idx-1 < n and visit[idx-1]:
            union(idx-1, idx)
        if 0 <= idx+1 < n and visit[idx+1]:
            union(idx+1, idx)

        ans = max(ans, height*size[find(idx)])

    print(ans)