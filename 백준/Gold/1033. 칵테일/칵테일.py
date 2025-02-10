import sys
from math import gcd
input = sys.stdin.readline

# 칵테일을 만드는데 필요한 각 재료의 질량을 0번 재료부터 순서대로 공백으로 구분해 출력

# august14를 만드는데 필요한 재료의 개수 N(1 <= N <= 10)
N = int(input().strip())
lcm = 1
# 재료 쌍의 비율
# 0 <= a, b <= N-1, 1<= p, q <= 9
graph = [[] for _ in range(N)]
visit = [False]*N
arr = [0]*N
for _ in range(N-1):
    a, b, p, q = map(int, input().strip().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))

    lcm *= ((p*q)//gcd(p, q))

arr[0] = lcm
def DFS(v):
    visit[v] = True
    for i in graph[v]:
        next = i[0]
        if not visit[next]:
            arr[next] = arr[v]*i[2]//i[1]
            DFS(next)

DFS(0)
mgcd = arr[0]

for i in range(1, N):
    mgcd = gcd(mgcd, arr[i])

for i in range(N):
    print(int(arr[i]//mgcd), end=" ")

