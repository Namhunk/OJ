import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 식 f를 true 로 만들 수 있으면 1, 없으면 0

# 변수의 개수 N(1 <= N <= 10,000); 절의 개수 M(1 <= M <= 100,000)
N, M = map(int, input().strip().split())

graph = [[] for _ in range(N*2+1)]

# 두 정수 i, j (1 <= |i|, |j| <= N)
for _ in range(M):
    i, j = map(int, input().strip().split())
    graph[-i].append(j)
    graph[-j].append(i)

def dfs(x):
    global cnt
    cnt += 1
    stack.append(x)
    visit[x] = cnt
    parent = visit[x]
    for nx in graph[x]:
        if visit[nx] == -1:
            parent = min(parent, dfs(nx))
        elif visit[nx] > 0:
            parent = min(parent, visit[nx])

    if visit[x] == parent:
        scc = set()
        while stack:
            curr = stack.pop()
            if -curr in scc:
                print(0)
                exit()

            scc.add(curr)
            visit[curr] = 0
            if curr == x: break

    return parent

stack = []
visit = [-1]*(N*2+1)
cnt = 0

for i in range(-N, N+1):
    if i == 0: continue
    if visit[i] > 0: continue
    dfs(i)
else:
    print(1)
"""

"""