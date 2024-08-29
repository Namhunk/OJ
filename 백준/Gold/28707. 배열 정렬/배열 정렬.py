import heapq
import sys
input = sys.stdin.readline

# 첫 줄에 배열 A를 비내림차순으로 정렬하기 위해 필요한 비용 총합의 최솟값을 출력
# 단, 배열을 비내림차순으로 만드는 것이 불가능한 경우 -1 출력

# 배열 A의 길이 N(2 <= N <= 8)
N = int(input().strip())

# A의 각 원소 A[i](1 <= A[i] <= 10)
A = list(map(int, input().strip().split()))

# 조작의 개수 M(1 <= M <= 10)
M = int(input().strip())

# M개의 줄의 i번째 줄에 조작을 의미하는 l, r, c (1 <= l <= r <= N; 1 <= c <= 10)
cmd = []
for _ in range(M):
    # A[l], A[r]의 값을 바꾸는데 c의 비용이 든다
    l, r, c = map(int, input().strip().split())
    l -= 1
    r -= 1
    cmd.append([l, r, c])

asc = tuple(sorted(A)) # 최종 완성 배열
ans = float('inf') # 최소값 저장
visit = set() # 배열의 순서 중복 방지, 들어가는 값들은 원소들의 형태 + 현재까지의 비용
visit.add(tuple(A)) # 최초 상태 저장

from heapq import heappush, heappop
def solv(A):
    A = tuple(A)
    visit = {A: 0} # 배열의 상태에 따른 비용
    heap = [(0, A)] # 비용, 배열 상태

    while heap:
        cost, arr = heappop(heap)
        if cost > visit[arr]: # 현재 비용이 같은 상태일때의 비용보다 작을 때
            continue

        for l, r, c in cmd:
            temp = list(arr) # 값 변경을 위한 리스트 형태
            temp[l], temp[r] = temp[r], temp[l]
            temp = tuple(temp)

            n_cost = cost + c # 다음 비용
            if temp not in visit:
                visit[temp] = n_cost
                heappush(heap, (n_cost, temp))
                continue

            if n_cost < visit[temp]:
                visit[temp] = n_cost
                heappush(heap, (n_cost, temp))

    return visit.setdefault(asc, -1)

print(solv(A))