import sys
input = sys.stdin.readline

# 2번 쿼리에 대해서 정답을 한 줄에 하나씩 순서대로 출력한다

# 첫째 줄에 수열의 크기 N이 주어진다 (1 <= N <= 100,000)
N = int(input().strip())

# 둘째 줄에는 A1, A2, .., An이 주어진다 (1 <= Ai <= 10^9)
A = [0] + list(map(int, input().strip().split()))

"""
세그먼트 트리 문제로 보여짐
"""

def init(start, end, idx): # 트리 초기화 함수
    if start == end: # 한 지점을 가르키면
        tree[idx] = (A[start], start) # 값 추가
        return tree[idx] # 값 반환

    mid = (start + end) // 2 # 범위를 둘로 나눔
    left = init(start, mid, idx*2)
    right = init(mid+1, end, idx*2+1)

    if left[0] <= right[0]:
        tree[idx] = left
    else:
        tree[idx] = right

    return tree[idx]

def find_minimum(start, end, idx, left, right):
    if left > end or right < start:
        return (float('inf'), -1) # 범위를 벗어난 경우

    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    left_min = find_minimum(start, mid, idx*2, left, right)
    right_min = find_minimum(mid+1, end, idx*2+1, left, right)

    if left_min[0] <= right_min[0]:
        return left_min
    else:
        return right_min

def update(start, end, idx, change, value):
    if change < start or change > end:
        return

    if start == end:
        tree[idx] = (value, change)
        return

    mid = (start + end) // 2
    update(start, mid, idx*2, change, value)
    update(mid+1, end, idx*2+1, change, value)

    left = tree[idx*2]
    right = tree[idx*2+1]

    if left[0] <= right[0]:
        tree[idx] = left
    else:
        tree[idx] = right

tree = [(0, 0)]*N*4
init(1, N, 1)

# 셋째 줄에는 쿼리의 개수 M이 주어진다 (1 <= M <= 100,000)
M = int(input().strip())

# 넷째 줄부터 M개의 줄에는 쿼리가 주어진다
for _ in range(M):
    q, i, j = map(int, input().strip().split())

    if q == 1: # 1인 경우 A[i]를 j로 변경
        update(1, N, 1, i, j)
        A[i] = j
    else: # 2인 경우 A[i], A[i+1], ..., A[j]에서 크기가 가장 작은 값의 인덱스를 출력
        val, idx = find_minimum(1, N, 1, i, j)
        print(idx)