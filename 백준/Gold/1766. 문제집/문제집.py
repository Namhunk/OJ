import heapq
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# 1.N개의 문제는 모두 풀어야 한다.
# 2.먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 풀어야 한다.
# 3. 가능하면 쉬운 문제부터 풀어야 한다.

# 1 <= N <= 32,000, 1 <= M, 100,000
N, M = map(int, input().strip().split()) # 문제의 수 N, 먼저 푸는 것이 좋은 문제 M
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().strip().split())  # A번 문제는 B번 문제보다 먼저 푸는 것이 좋다
    graph[A].append(B) # A번 문제를 푼 다음 풀어야 할 문제 번호
    indegree[B] += 1 # B번 문제를 풀기위해 이전에 풀어야할 문제의 수

heap = []
ans = []

for i in range(1, N+1): # 처음 푸는게 좋은 문제들 선택
    if not indegree[i]: heappush(heap, i)

while heap:
    x = heappop(heap)
    ans.append(x)

    for i in graph[x]:
        indegree[i] -= 1
        if not indegree[i]: # 이전에 풀어야 할 문제들을 다 풀었다면
            heappush(heap, i)

print(*ans)