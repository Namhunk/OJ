import sys
input = sys.stdin.readline
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지 출력
# 세그먼트 트리

# 수의 개수 N (1 <= N <= 1,000,000)
# 수의 변경이 일어나는 횟수 M (1 <= M <= 10,000)
# 구간의 곱을 구하는 횟수 K (1 <= K <= 10,000)
N, M, K = map(int, input().strip().split())

# N개의 수
arr = [0] + [int(input().strip()) for _ in range(N)]
tree = [0]*(4*N)

mod = int(1e9+7)
def init(start, end, idx): # 트리 초기화
    if start == end: # 두 값이 같다면
        tree[idx] = arr[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) * init(mid+1, end, idx*2+1) % mod
    return tree[idx] % mod

def update(start, end, idx, change, value): # 값을 바꾸는 함수
    if change < start or change > end:
        return

    if start == end:
        tree[idx] = value
        return 

    mid = (start + end) // 2
    update(start, mid, idx*2, change, value)
    update(mid+1, end, idx*2+1, change, value)

    tree[idx] = tree[idx*2] * tree[idx*2+1] % mod
    

def  mul(start, end, idx, left, right):
    if left > end or right < start:
        return 1

    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return mul(start, mid, idx*2, left, right) * mul(mid+1, end, idx*2+1, left, right) % mod

init(1, N, 1)
# a == 1 : b번째 수를 c로 변경
# a == 2 : b부터 c까지의 곱 출력
for _ in range(M+K):
    a, b, c = map(int, input().strip().split())

    if a == 1:
        update(1, N, 1, b, c)
        arr[b] = c

    if a == 2:
        print(mul(1, N, 1, b, c))