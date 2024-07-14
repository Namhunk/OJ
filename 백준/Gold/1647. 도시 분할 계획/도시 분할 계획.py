import heapq
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 마을을 2개로 분리할 때 길 유지비의 합의 최소값
# 2 <= N <= 1e5, 1 <= M <= 1e6
N, M = map(int, input().strip().split())
edge = [[] for _ in range(N+1)] # 간선 정보
for _ in range(M):
    A, B, C = map(int, input().strip().split())  # A, B 의 길은 C의 비용
    edge[A].append([C, B])
    edge[B].append([C, A])

visit = [True]*(N+1) # 방문 표시
heap = [[0, 1]] # heap을 통해 최소 비용 가져옴
ans = []

while heap:
    w, x = heappop(heap)
    if not visit[x]: continue # 방문하지 않고
    if len(ans) == N: break
    visit[x] = False # 방문처리
    ans.append(w) # 정답에 최소 비용 추가

    for NEXT in edge[x]:
        if not visit[NEXT[1]]: continue
        heappush(heap, NEXT)

print(sum(ans) - max(ans))