import sys
input = sys.stdin.readline
from collections import deque

# M개의 도로를 가진 도로의 집합 중 연결되어 있으면서 우선 순위가 가장 높은 것
# 집합에 속하는 도로 중 0을 끝점으로 갖는 도로의 개수, 1을 끝점으로 갖는 도로의 개수 .. N-1을 끝점으로 갖는 도로의 개수
# 없으면 -1

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])

    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        if x > y:
            x, y = y, x
        parents[y] = x
        return True
    return False

# 도시의 개수 N (1 <= N <= 50), 도로의 개수 M (N-1 <= M <= 1,000)
N, M = map(int, input().strip().split())
parents = [i for i in range(N)] # 연결 상태
ans = [0]*N

# 인접행렬 arr[i][j] = Y : 도로 존재, arr[i][n] = N : 도로 없음
arr = []
cnt = 0
for i in range(N):
    row = list(input().strip())
    for j in range(i+1, N):
        if row[j] == 'Y':
            if union(i, j):
                ans[i] += 1
                ans[j] += 1
                cnt += 1
            else:
                arr.append((i, j))

if cnt < N-1 or cnt+len(arr) < M:
    print(-1)
else:
    remain = M-cnt
    for i, j in arr:
        if remain <= 0: break
        ans[i] += 1
        ans[j] += 1
        remain -= 1

    print(*ans)