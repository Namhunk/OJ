import heapq
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# union - find
def find(x):
    if x != arr[x]: return find(arr[x])
    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: arr[y] = x
    else: arr[x] = y

# 마을을 2개로 분리할 때 길 유지비의 합의 최소값
# 2 <= N <= 1e5, 1 <= M <= 1e6
N, M = map(int, input().strip().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().strip().split())  # A, B 의 길은 C의 비용
    edges.append([C, A, B])

arr = [i for i in range(N+1)]
edges.sort() # 유지비 작은순 정렬

ans = 0
cnt = 0
for C, A, B in edges:
    if cnt >= N-2: break
    if find(A) == find(B): continue # 연결되지 않았다면
    union(A, B) # 연결
    ans += C
    cnt += 1

print(ans)
