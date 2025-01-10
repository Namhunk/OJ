import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 그래프 이론, 강한 연결 요소

# 첫째 줄에 SCC의 개수 K를 출력, 다음 K개의 줄에는 각 줄에 하나의 SCC에 속한 정점의 번호를 출력.
# 각 줄의 끝에는 -1을 출력, 각각의 SCC를 출력할 때 그 안에 속한 정점들은 오름차순으로 출력
# 여러 개의 SCC에 대해서는 그 안에 속해있는 가장 작은 정점의 정점 번호 순으로 출력

# 방향 그래프가 주어졌을 때, 그 그래프를 SCC들로 나누는 프로그램을 작성
# 방향 그래프의 SCC는 우선 정점의 최대 부분집합이며, 그 부분집합에 들어있는 서로 다른 임의의 두 정점 u, v에 대해
# u에서 v로 가는 경로와 v에서 u로 가는 경로가 모두 존재하는 경우를 말함

# 두 정수 V(1 <= V <= 10,000), E(1 <= E <= 100,000) V개의 정점, E개의 간선
V, E = map(int, input().strip().split())

graph = [[] for _ in range(V+1)]
# E개의 줄에는 간선에 대한 정보를 나타내는 두 정수 A, B가 주어짐 A -> B
for _ in range(E):
    A, B = map(int, input().strip().split())
    graph[A].append(B)

visit = [-1 for _ in range(V+1)]
stack = []
cnt = 0
ans = []
# 사이클이 생기는지 판단

# 방법은 타잔 알고리즘, 코사라주 알고리즘이 있다고 함
# 타잔 알고리즘
def dfs(x):
    global cnt
    cnt += 1
    visit[x] = cnt
    stack.append(x)

    parent = visit[x]
    for next in graph[x]:
        if visit[next] == -1:
            parent = min(parent, dfs(next))
        elif visit[next] != 0:
            parent = min(parent, visit[next])

    if parent == visit[x]:
        scc = []
        while True:
            node = stack.pop()
            scc.append(node)
            visit[node] = 0
            if x == node:
                break

        scc.sort()
        ans.append(scc)

    return parent

for i in range(1, V+1):
    if visit[i] == -1:
        dfs(i)

print(len(ans))
ans.sort()
for i in ans:
    print(*i, -1)