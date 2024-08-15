import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
# Q 줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력

# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력

# 트리의 정점 수 N(2 <= N <= 1e5), 루트의 번호 R(1<= R <= N), 쿼리의 수 Q(1 <= Q <= 1e5)
N, R, Q = map(int, input().strip().split())

edges = [[] for _ in range(N+1)] # 정점들 간의 간선에 대한 정보

# N-1 줄에 U, V 형태로 트리에 속한 간선의 정보 (1 <= U, V <= N, U != V)
# 이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미
for _ in range(N-1):
    U, V = map(int, input().strip().split())
    edges[U].append(V)
    edges[V].append(U)

count = [-1]*(N+1) # 서브트리의 개수
def solv(x):
    count[x] = 1 # 기본 값 1

    for i in edges[x]:
        if count[i] == -1: # 방문하지 않은 정점에 대해
            count[x] += solv(i) # 이전 정점의 서브트리 개수를 더함

    return count[x]

solv(R)

for _ in range(Q):
    U = int(input().strip())
    print(count[U])

