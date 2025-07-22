import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 식 f를 true 로 만들 수 있으면 1, 없으면 0

# 변수의 개수 N(1 <= N <= 10,000); 절의 개수 M(1 <= M <= 100,000)
N, M = map(int, input().strip().split())

graph = [[] for _ in range(N*2+1)]
reverse_graph = [[] for _ in range(N*2+1)]
# 두 정수 i, j (1 <= |i|, |j| <= N)
for _ in range(M):
    i, j = map(int, input().strip().split())
    graph[-i].append(j)
    graph[-j].append(i)

    reverse_graph[i].append(-j)
    reverse_graph[j].append(-i)

def dfs(x):
    visit[x] = 1
    for nx in graph[x]:
        if visit[nx]: continue
        dfs(nx)
    stack.append(x)

def reverse_dfs(x):
    visit[x] = 1
    ids[x] = idx
    for nx in reverse_graph[x]:
        if visit[nx]: continue
        reverse_dfs(nx)

visit = [0]*(N*2+1)
stack = []

for i in range(1, N*2+1):
    if visit[i]: continue
    dfs(i)

visit = [0]*(N*2+1)
ids = [0]*(N*2+1)
idx = 0

while stack:
    x = stack.pop()
    if visit[x]: continue
    reverse_dfs(x)
    idx += 1

for i in range(1, N+1):
    if ids[i] == ids[-i]:
        print(0)
        break
else:
    print(1)

"""

"""