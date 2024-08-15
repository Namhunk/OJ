import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
# Q 줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력

# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력

# 트리의 정점 수 N(2 <= N <= 1e5), 루트의 번호 R(1<= R <= N), 쿼리의 수 Q(1 <= Q <= 1e5)
N, R, Q = map(int, input().strip().split())

edges = [[] for _ in range(N+1)] # 정점들 간의 간선에 대한 정보

# 위상정렬을 응용 해봄
indegree = [0]*(N+1) # 각 정점에 대한 방문 차수
# N-1 줄에 U, V 형태로 트리에 속한 간선의 정보 (1 <= U, V <= N, U != V)
# 이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미
for _ in range(N-1):
    U, V = map(int, input().strip().split())
    edges[U].append(V)
    edges[V].append(U)
    indegree[U] += 1
    indegree[V] += 1

from collections import deque
que = deque()
for i in range(1, N+1):
    if indegree[i] == 1: # 간선이 1개인 정점들을 추가
        que.append(i)

ans = [1]*(N+1) # 정답 배열 기본값 1
while que:
    curr = que.popleft()
    if curr == R: continue # 루트 정점을 제외하고
    indegree[curr] -= 1 # 자신의 차수를 빼줌

    for i in edges[curr]:
        if indegree[i] > 0: # 연결 정점이 모든 정점들을 거치지 않았다면
            ans[i] += ans[curr] # 더해줌
        indegree[i] -= 1
        if indegree[i] == 1:
            que.append(i)

for _ in range(Q):
    U = int(input().strip())
    print(ans[U])
    