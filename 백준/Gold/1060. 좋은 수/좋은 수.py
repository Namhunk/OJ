import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# 좋은 수 N개를 공백으로 구분해 출력

# 집합 S의 크기 L
L = int(input().strip())

# 집합에 포함된 정수 S
S = sorted(list(map(int, input().strip().split())))

# 좋은 수의 개수 N
N = int(input().strip())

def get_count(x, l, r): # 구간의 개수를 구하는 함수 x: 현재 숫자, l: 왼쪽 끝, r: 오른쪽 끝
    left = x - l # x의 왼쪽 숫자들
    right = r - x # x의 오른쪽 숫자들

    # left * right 는 왼쪽 사작 범위 - 오른쪽 끝 범위를 나타냄
    return left + right + left * right

def solve(L, S, N):
    ans = []  # 정답 배열

    # 1. N 값이 1 - S[L-1] 구간의 길이보다 작은 경우
    heap = [] # 좋은 수의 우선 순위 배열
    visit = set() # 정답에 담을 숫자들

    for i in range(L): # 현재 집합 안의 숫자들은 좋은 구간의 개수가 0
        visit.add(S[i])
        heappush(heap, (0, S[i], S[i], S[i]))

    if 1 <= S[0]-1: # 집합 안의 최소 값이 1보다 큰 경우
        l, r = 1, S[0]-1

        if l not in visit:
            visit.add(l)
            cnt = get_count(l, l, r)
            heappush(heap, (cnt, l, l, r))

        if r not in visit:
            visit.add(r)
            cnt = get_count(r, l, r)
            heappush(heap, (cnt, r, l, r))

    for i in range(L-1): # 집합 안에서 크가가 가까운 두 숫자의 사이 구간
        l, r = S[i]+1, S[i+1]-1
        if l <= r:
            if l not in visit:
                visit.add(l)
                cnt = get_count(l, l, r)
                heappush(heap, (cnt, l, l, r))

            if r not in visit:
                visit.add(r)
                cnt = get_count(r, l, r)
                heappush(heap, (cnt, r, l, r))

    while len(ans) < N and heap:
        _, x, l, r = heappop(heap)
        ans.append(x) # 우선순위가 높은 순서대로 추가

        if l <= x-1 <= r and x-1 not in visit:
            visit.add(x-1)
            cnt = get_count(x-1, l, r)
            heappush(heap, (cnt, x-1, l, r))

        if l <= x+1 <= r and x+1 not in visit:
            visit.add(x+1)
            cnt = get_count(x+1, l, r)
            heappush(heap, (cnt, x+1, l, r))

    x = S[L-1] + 1
    while len(ans) < N:
        ans.append(x)
        x += 1

    return ans

print(*solve(L, S, N))