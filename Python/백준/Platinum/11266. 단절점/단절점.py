import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 1. 단절점의 개수, 2. 단절점의 번호를 공백으로 구분해 오름차순으로 출력
# 단절점이란 그 정점을 제거했을 때, 그래프가 두 개 또는 그 이상으로 나누어지는 정점을 의미

# V(1 <= V <= 10,000); E(1 <= E <= 100,000)
V, E = map(int, input().strip().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B = map(int, input().strip().split())
    graph[A].append(B)
    graph[B].append(A)

visit = [0]*(V+1)
cut = [0]*(V+1)
cnt = 0

def dfs(x, root):
    global cnt
    cnt += 1
    visit[x] = cnt
    child = 0
    min_num = visit[x]
    for nx in graph[x]:
        if not visit[nx]:
            child += 1
            child_num = dfs(nx, 0)

            if not root and child_num >= visit[x]:
                cut[x] = 1

            min_num = min(min_num, child_num)
        else:
            min_num = min(min_num, visit[nx])

    if root and child > 1:
        cut[x]=1
    return min_num

for i in range(1, V+1):
    if not visit[i]:
        dfs(i, 1)

print(sum(cut))
for i in range(1, V+1):
    if cut[i]:
        print(i, end=' ')