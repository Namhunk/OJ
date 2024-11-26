import sys
input = sys.stdin.readline

# 첫째 줄 부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단 정답은 -2e63 <= ans <= 2e63-1 범위의 정수
# 세그먼트 트리?

# 수의 개수 N (1 <= N <= 1,000,000)
# 수의 변경이 일어나는 횟수 M (1 <= M <= 10,000)
# 구간의 합을 구하는 횟수 K (1 <= K <= 10,000)
N, M, K = map(int, input().strip().split())

# N+1 줄까지 N개의 수
arr = [0] + [int(input().strip()) for _ in range(N)]

# N+2 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c 가 주어짐
# a == 1 일때 b (1 <= b <= N) 번째 수를 c로 변경
# a == 2 일때 b ( 1 <= b <= N) 번째 수부터 c(b <= c <= N)번째 수까지의 합을 구하여 출력

tree = [0] * (4*N) # 트리 생성

def init(start, end, idx): # 트리 값 초기화 start = arr의 시작, end = arr의 끝, idx = 현재 트리의 위치
    if start == end: # 현재 구간이 아닌 하나의 위치라면
        tree[idx] = arr[start] # 배열의 값 추가
        return tree[idx]

    mid = (start + end) // 2 # 범위를 나눔
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

def interval_sum(start, end, idx, left, right): # 합을 구하는 함수 left, right = 합을 구하려는 범위
    if left > end or right < start: # 범위를 벗어난 경우
        return 0

    if left <= start and right >= end: # 범위 안에 있는 경우
        return tree[idx]

    mid = (start + end) // 2
    return interval_sum(start, mid, idx*2, left, right) + interval_sum(mid+1, end, idx*2+1, left, right)

def update(start, end, idx, change, value): # change = 구간합을 수정한고자 하는 노드, value = 수정할 값
    if change < start or change > end: # 범위를 벗어난다면 수행하지 않음
        return

    tree[idx] += (value - arr[change])
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx*2, change, value)
    update(mid+1, end, idx*2+1, change, value)

init(1, N, 1)
for _ in range(M+K):
    a, b, c = map(int, input().strip().split())

    if a == 1:
        update(1, N, 1, b, c)
        arr[b] = c
    else:
        print(interval_sum(1, N, 1, b, c))
